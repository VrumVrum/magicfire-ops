# KPIs — magicfire.ro

**Only measured numbers. Never write a figure you did not pull.** Source: `data/gsc.json` (auto, daily).

## 2026-07-30 — first scored pull (28d vs prior 28d)

| Metric | Last 28d | Prior 28d | Δ |
|---|---|---|---|
| Clicks | 123 | 82 | **+41 (+50.0%)** |
| Impressions | 1,649 | 1,000 | **+649 (+64.9%)** |
| CTR | 7.46% | 8.20% | -0.74pp |
| Avg. position | 5.02 | 5.69 | **+0.67 (better)** |

Clicks and impressions both up strongly, average position improved ~0.7. CTR dipped slightly — expected side-effect of the impression surge pulling in more low-intent/broad queries (English-language and out-of-area terms are a growing share of impressions, see below), not a ranking-quality regression.

**Device split (28d):** Mobile 104 clicks / 1,416 impr (85% of impressions), Desktop 18/224, Tablet 1/9. Confirms mobile-first is the correct lens — matches `data/site.json` mobile-first checks (phone `tel:` link present and above the fold, no horizontal overflow at 390px).

**Top queries by clicks (28d):**
| Query | Clicks | Impr | Position |
|---|---|---|---|
| artificii iasi | 22 | 119 | 3.0 |
| magic fire (brand) | 4 | 25 | 1.4 |
| artificii galati | 3 | 45 | 7.1 |
| fumigene iasi | 3 | 16 | 3.9 |
| artificii | 2 | 31 | 4.3 |
| artificii reci | 2 | 21 | 8.1 |

**Top pages by clicks (28d):** homepage 94/1,096 (pos 4.4) · /artificii-galati/ 16/182 (pos 5.8) · /artificii-iasi/ 4/101 (pos 4.3) · /artificii-nunta-pret-2026-romania/ 4/144 (pos 5.8).

**Site health (`data/site.json`, generated 2026-07-30):** 10/12 checks green. Phone `tel:+40746883228` present (7×), tappable, above the fold on mobile. Contact form present. No JS errors, no mobile overflow. Homepage/`/contact`/`/blog` all HTTP 200. `/servicii` and `/despre-noi` return 404 — flagged in opportunities, not acted on this cycle (no evidence these URLs were ever live pages vs. a stale check-list assumption).

Note: this session's outbound network policy blocks direct fetches to magicfire.ro (proxy denies CONNECT to the domain). All numbers above are read from committed `data/` files as designed; no live-page verification was possible from this session — flagged in `ledger/actions.md`.
