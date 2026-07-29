# -*- coding: utf-8 -*-
"""Google Search Console pull for magicfire.ro (URL-prefix property).

Runs on GitHub Actions (free) so it never depends on a PC being on.
Key comes from the GSC_KEY_JSON secret. Writes data/gsc.json.
"""
import json, os, io, time, base64, urllib.request, urllib.parse
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

SITE = urllib.parse.quote(os.environ.get('GSC_SITE', 'https://magicfire.ro/'), safe='')
OUT = os.environ.get('GSC_OUT', 'data/gsc.json')


def token():
    k = os.environ.get('GSC_KEY_JSON')
    sa = json.loads(k) if k else json.load(open(os.environ['GSC_KEY_PATH']))
    hdr = base64.urlsafe_b64encode(json.dumps({'alg': 'RS256', 'typ': 'JWT'}).encode()).rstrip(b'=')
    now = int(time.time())
    claims = {'iss': sa['client_email'], 'scope': 'https://www.googleapis.com/auth/webmasters.readonly',
              'aud': sa['token_uri'], 'iat': now, 'exp': now + 3600}
    pb = base64.urlsafe_b64encode(json.dumps(claims).encode()).rstrip(b'=')
    pk = serialization.load_pem_private_key(sa['private_key'].encode(), password=None)
    sig = pk.sign(hdr + b'.' + pb, padding.PKCS1v15(), hashes.SHA256())
    jwt = (hdr + b'.' + pb + b'.' + base64.urlsafe_b64encode(sig).rstrip(b'=')).decode()
    d = urllib.parse.urlencode({'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
                                'assertion': jwt}).encode()
    return json.loads(urllib.request.urlopen(
        urllib.request.Request(sa['token_uri'], data=d, method='POST')).read())['access_token']


def q(tok, body):
    req = urllib.request.Request(
        f'https://www.googleapis.com/webmasters/v3/sites/{SITE}/searchAnalytics/query',
        method='POST', headers={'Authorization': f'Bearer {tok}', 'Content-Type': 'application/json'},
        data=json.dumps(body).encode())
    return json.loads(urllib.request.urlopen(req, timeout=40).read()).get('rows', [])


def days_ago(n):
    return time.strftime('%Y-%m-%d', time.gmtime(time.time() - n * 86400))


if __name__ == '__main__':
    t = token()
    out = {'site': os.environ.get('GSC_SITE', 'https://magicfire.ro/'),
           'generated': time.strftime('%Y-%m-%d', time.gmtime())}
    base = {'startDate': days_ago(28), 'endDate': days_ago(1)}
    prev = {'startDate': days_ago(56), 'endDate': days_ago(29)}

    def totals(rng):
        r = q(t, {**rng, 'dimensions': []})
        return r[0] if r else {}
    out['totals_28d'] = totals(base)
    out['totals_prev_28d'] = totals(prev)
    for dim, key, n in (('query', 'queries_28d', 200), ('page', 'pages_28d', 200),
                        ('country', 'countries_28d', 20), ('device', 'devices_28d', 5),
                        ('date', 'daily_28d', 30)):
        try:
            rows = q(t, {**base, 'dimensions': [dim], 'rowLimit': n})
            out[key] = [{dim: r['keys'][0], 'clicks': r.get('clicks', 0),
                         'impressions': r.get('impressions', 0),
                         'ctr': round(r.get('ctr', 0), 4), 'position': round(r.get('position', 0), 1)}
                        for r in rows]
        except Exception as e:
            out[key] = {'error': str(e)[:120]}
    # query x page — which page answers which query (for cannibalisation + targeting)
    try:
        rows = q(t, {**base, 'dimensions': ['query', 'page'], 'rowLimit': 200})
        out['query_page_28d'] = [{'query': r['keys'][0], 'page': r['keys'][1], 'clicks': r.get('clicks', 0),
                                  'impressions': r.get('impressions', 0), 'position': round(r.get('position', 0), 1)}
                                 for r in rows]
    except Exception as e:
        out['query_page_28d'] = {'error': str(e)[:120]}

    os.makedirs(os.path.dirname(OUT) or '.', exist_ok=True)
    io.open(OUT, 'w', encoding='utf-8').write(json.dumps(out, indent=2, ensure_ascii=False) + '\n')
    print('wrote', OUT, '| 28d:', out.get('totals_28d'))
