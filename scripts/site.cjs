// Live-site health for magicfire.ro — checks what matters for a LOCAL business:
// the phone must be visible and tappable on a phone-sized screen, the contact
// path must work, pages must render. Runs on GitHub Actions (free, no PC).
const { chromium } = require('playwright');
const fs = require('fs');
const BASE = process.env.SITE || 'https://magicfire.ro';
const OUT = process.env.SITE_OUT || 'data/site.json';

(async () => {
  const browser = await chromium.launch({ headless: true });
  const checks = [];
  const add = (n, ok, d) => checks.push({ name: n, ok: !!ok, detail: String(d) });

  // mobile-first: most local searches are on a phone
  const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  const page = await ctx.newPage();
  const errs = [];
  page.on('pageerror', e => errs.push(String(e).slice(0, 100)));

  try {
    const r = await page.goto(BASE, { waitUntil: 'domcontentloaded', timeout: 45000 });
    add('homepage loads', r && r.status() === 200, `HTTP ${r ? r.status() : 0}`);
    await page.waitForTimeout(1200);

    // phone: present, tappable, and visible without scrolling far
    const tel = await page.evaluate(() => {
      const a = [...document.querySelectorAll('a[href^="tel:"]')];
      if (!a.length) return { count: 0 };
      const first = a[0].getBoundingClientRect();
      return { count: a.length, number: a[0].getAttribute('href'),
               visibleAboveFold: first.top >= 0 && first.top < window.innerHeight && first.width > 0 };
    });
    add('phone link (tel:) exists', tel.count > 0, `${tel.count} found ${tel.number || ''}`);
    add('phone visible above the fold (mobile)', tel.visibleAboveFold, tel.visibleAboveFold ? 'yes' : 'NO — buried');

    // contact route
    const forms = await page.locator('form').count();
    add('a form exists on homepage', forms > 0, `${forms} form(s)`);

    // no horizontal overflow (breaks local mobile UX)
    const of = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 2);
    add('no horizontal overflow (390px)', !of, of ? 'HAS overflow' : 'clean');

    add('no JS errors', errs.length === 0, errs.slice(0, 2).join(' | ') || 'clean');

    // title/meta present (basic SEO hygiene)
    const meta = await page.evaluate(() => ({
      title: document.title,
      desc: (document.querySelector('meta[name="description"]') || {}).content || '',
    }));
    add('title present', meta.title && meta.title.length > 10, meta.title.slice(0, 70));
    add('meta description present', meta.desc && meta.desc.length > 40, `${meta.desc.length} chars`);
  } catch (e) { add('homepage', false, String(e).slice(0, 90)); }
  await ctx.close();

  // key pages still 200
  for (const p of ['/contact', '/servicii', '/despre-noi', '/blog']) {
    try {
      const c = await browser.newContext();
      const pg = await c.newPage();
      const r = await pg.goto(BASE + p, { waitUntil: 'domcontentloaded', timeout: 30000 });
      add(`page ${p}`, r && r.status() < 400, `HTTP ${r ? r.status() : 0}`);
      await c.close();
    } catch (e) { add(`page ${p}`, false, 'unreachable'); }
  }

  await browser.close();
  const pass = checks.filter(c => c.ok).length;
  const out = { generated_utc: new Date().toISOString(), passed: pass, total: checks.length,
                all_green: pass === checks.length, checks };
  fs.mkdirSync(require('path').dirname(OUT), { recursive: true });
  fs.writeFileSync(OUT, JSON.stringify(out, null, 2) + '\n');
  console.log(`SITE: ${pass}/${checks.length}`);
  checks.filter(c => !c.ok).forEach(c => console.log('  FAIL:', c.name, '|', c.detail));
})();
