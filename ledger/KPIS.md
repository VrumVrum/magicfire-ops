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

## 2026-08-06 — third scored pull (28d vs prior 28d)

Source: `data/gsc.json`, generated 2026-08-05.

| Metric | Last 28d | Prior 28d | Δ |
|---|---|---|---|
| Clicks | 114 | 91 | **+23 (+25.3%)** |
| Impressions | 1,732 | 1,075 | **+657 (+61.1%)** |
| CTR | 6.58% | 8.47% | **-1.89pp** |
| Avg. position | 5.09 | 5.67 | **+0.58 (better)** |

Growth continues but the rate is decelerating: clicks growth slowed from +80.5% (last cycle) to +25.3%, and CTR dropped harder this time (-1.89pp vs -0.48pp two cycles ago). Impressions are still climbing fast (+61.1%), so the CTR dip reads the same as the first cycle's read — impression growth is outpacing click growth, most likely broad/international query volume diluting CTR, not a ranking-quality regression (position kept improving, 5.67→5.09). Flagging honestly: this is the first cycle where clicks did not also accelerate, worth watching next cycle rather than assuming it's noise.

**Device split (28d):** Mobile 98 clicks / 1,494 impr (86% of impressions, CTR 6.56%, pos 4.9), Desktop 16/236 (CTR 6.78%, pos 6.4), Tablet 0/2 (pos 4.0). Mobile-first remains the correct lens.

**Top queries by clicks (28d):**
| Query | Clicks | Impr | Position |
|---|---|---|---|
| artificii iasi | 22 | 120 | 2.9 |
| magicfire (brand) | 4 | 9 | 1.0 |
| magic fire (brand) | 3 | 30 | 1.5 |
| artificii | 2 | 34 | 4.5 |
| artificii galati | 2 | 36 | 7.1 |
| artificii reci | 2 | 24 | 7.6 |

**Top pages by clicks (28d):** homepage 90/1,141 (pos 4.4) · `/artificii-galati/` 12/147 (pos 6.0) · `/artificii-nunta-pret-2026-romania/` 4/185 (pos 6.5) · `/artificii-iasi/` 2/103 (pos 4.7) · `/artificii-reci-fantani-scantei-t1/` 2/29 (pos 7.7) · `/category/artificii-iasi-evenimente/` 2/92 (pos 6.9) · `/shop/` 2/52 (pos 7.4).

**New signal this pull — `/category/artificii-iasi-evenimente/`:** 92 impressions, 2 clicks, 2.17% CTR, position 6.9 — essentially unchanged/slightly worse than the 2026-08-03 pull (97 impr, 3 clicks, 3.1% CTR, pos 7.0), which had already filed this as a candidate for "a future cycle." Query-level breakdown shows "artificii iasi" landing on this page at **position 12.1** (9 impressions) — nearly 10 positions worse than the same query on the homepage (2.9). This looks like the page is trying to compete for the exact commercial term the homepage already owns, and losing badly, instead of serving a distinct intent. See Action #3 in `ledger/actions.md`.

**Action #1 status check** (`/artificii-reci-fantani-scantei-t1/`, verify date 2026-08-27 — not due, 21 days out): page-level aggregate is 29 impressions / 2 clicks / position 7.7, identical to both prior pulls (2026-07-30 and 2026-08-03). Genuinely no movement yet — expected, not yet due.

**Action #2 status check** (`/preturi/`, verify date 2026-09-14 — not due, ~39 days out): page-level aggregate is **107 impressions / 0 clicks / 0% CTR / position 5.7** — CTR actually fell further, from 0.83% (1 click) to 0% (0 clicks). Position held steady. Too early to score, but flagging the number moved the wrong direction while the fix sits unapplied (WordPress write access still not wired) — reinforces the case for applying Action #2 soon, not evidence the proposed fix is wrong.

**Site health (`data/site.json`, generated 2026-08-05):** 10/12 checks green, unchanged. `/servicii` and `/despre-noi` still 404 — same stale flag as prior two pulls, no new evidence, not re-escalated without new information.

Note: this session's outbound network policy still blocks direct fetches to magicfire.ro. No live-page verification was possible from this session — flagged in `ledger/actions.md`.
