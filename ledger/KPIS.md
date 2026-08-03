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

## 2026-08-03 — second scored pull (28d vs prior 28d)

Source: `data/gsc.json`, generated 2026-08-02.

| Metric | Last 28d | Prior 28d | Δ |
|---|---|---|---|
| Clicks | 139 | 77 | **+62 (+80.5%)** |
| Impressions | 1,746 | 1,029 | **+717 (+69.7%)** |
| CTR | 7.96% | 7.48% | +0.48pp |
| Avg. position | 5.01 | 5.71 | **+0.70 (better)** |

Growth continues in the same direction as the 2026-07-30 pull (clicks/impressions both up strongly, position improving). CTR is no longer dipping — it recovered to slightly above the prior period, consistent with the earlier read that the impression surge was diluting CTR with broad/international queries rather than a real quality problem.

**Device split (28d):** Mobile 119 clicks / 1,493 impr (85% of impressions, CTR 7.97%, pos 4.8), Desktop 20/250 (CTR 8.0%, pos 6.4), Tablet 0/3. Mobile-first remains the correct lens.

**Top queries by clicks (28d):**
| Query | Clicks | Impr | Position |
|---|---|---|---|
| artificii iasi | 23 | 122 | 2.9 |
| magic fire (brand) | 4 | 29 | 1.4 |
| magicfire (brand) | 4 | 8 | 1.0 |
| artificii galati | 3 | 40 | 7.1 |
| fumigene iasi | 3 | 19 | 3.8 |
| artificii | 2 | 31 | 4.4 |
| artificii reci | 2 | 24 | 7.6 |

**Top pages by clicks (28d):** homepage 107/1,180 (pos 4.3) · `/artificii-galati/` 17/167 (pos 6.0) · `/artificii-iasi/` 4/114 (pos 4.7) · `/artificii-nunta-pret-2026-romania/` 4/148 (pos 5.8) · `/category/artificii-iasi-evenimente/` 3/97 (pos 7.0) · `/shop/` 3/52 (pos 7.9) · `/artificii-reci-fantani-scantei-t1/` 2/29 (pos 7.7).

**Biggest CTR gap this pull:** `/preturi/` — 120 impressions, position 5.7, only **1 click (0.83% CTR)**. This is the largest impression volume with the worst CTR of any page in the dataset, on a page whose entire purpose is buyer-intent (pricing). See Action #2 in `ledger/actions.md`.

**Action #1 status check** (`/artificii-reci-fantani-scantei-t1/`, verify date 2026-08-27 — not due yet): page-level aggregate is 29 impressions / 2 clicks / position 7.7 in this pull, essentially unchanged from the 2026-07-30 baseline (29 impr / 2 clicks / pos 7.7). Too early to score — flagging only that it hasn't moved yet, as expected before the verify date.

**Site health (`data/site.json`, generated 2026-08-02):** 10/12 checks green, same as last pull. `/servicii` and `/despre-noi` still 404 — same stale flag as 2026-07-30, no new evidence either was ever a real live page; not re-escalated without new information.

Note: this session's outbound network policy still blocks direct fetches to magicfire.ro (WebFetch returned HTTP 403 on `/preturi/`). No live-page verification was possible from this session — flagged in `ledger/actions.md`.
