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

## 2026-08-10 — fourth scored pull (28d vs prior 28d)

Source: `data/gsc.json`, generated 2026-08-10.

| Metric | Last 28d | Prior 28d | Δ |
|---|---|---|---|
| Clicks | 120 | 96 | **+24 (+25.0%)** |
| Impressions | 1,836 | 1,162 | **+674 (+58.0%)** |
| CTR | 6.54% | 8.26% | **-1.72pp** |
| Avg. position | 5.38 | 5.58 | **+0.20 (better)** |

Growth continues but position improvement is the smallest of the four pulls so far (+0.20 vs +0.58 to +0.70 previously), and CTR is down again, similar magnitude to the 2026-08-06 dip (-1.72pp vs -1.89pp). Clicks growth (+25.0%) roughly matches the 2026-08-06 cycle (+25.3%) rather than reaccelerating — the deceleration flagged last cycle has not reversed, it has stabilized at a lower growth rate. Impressions keep climbing fast. Romania is still 88.9% of impressions / 90% of clicks (1,633/1,836 impr, 108/120 clicks) — the impression growth is not primarily foreign traffic this pull, which weakens the "broad/international dilution" explanation used in prior cycles for the CTR dip. Saying the honest number: CTR is down for the second cycle in a row and the cause is less clear than previously assumed — worth a harder look if it continues next cycle.

**Device split (28d):** Mobile 108 clicks / 1,570 impr (85.5% of impressions, CTR 6.88%, pos 5.0), Desktop 12/264 (CTR 4.55%, pos 7.5), Tablet 0/2 (pos 4.0). Mobile-first remains the correct lens; desktop position and CTR both worsened this pull.

**Top queries by clicks (28d):**
| Query | Clicks | Impr | Position |
|---|---|---|---|
| artificii iasi | 19 | 107 | 2.9 |
| magicfire (brand) | 4 | 7 | 1.0 |
| artificii | 3 | 35 | 4.6 |
| artificii galati | 3 | 30 | 7.1 |
| artificii reci | 2 | 23 | 7.6 |
| cat costa artificiile la nunta | 2 | 12 | 5.9 |

**Top pages by clicks (28d):** homepage 90/1,128 (pos 4.7) · `/artificii-galati/` 10/130 (pos 6.1) · `/artificii-nunta-pret-2026-romania/` 9/311 (pos 6.3) · `/shop/` 4/65 (pos 7.1) · `/category/artificii-iasi-evenimente/` 3/90 (pos 6.9) · `/artificii-iasi/` 2/95 (pos 4.8) · `/artificii-reci-fantani-scantei-t1/` 2/29 (pos 7.7).

**New signal this pull — `/artificii-nunta-pret-2026-romania/` (the wedding-pricing page):** impressions jumped from 185 (2026-08-06) to **311** — a genuine, sharp rise, not a rounding blip, and the fourth straight cycle of growth on this exact page (144 → 148 → 185 → 311). Clicks more than doubled too (4 → 9), but CTR has stayed flat and low across all four pulls (2.8% → 2.7% → 2.2% → 2.9%) — for a page ranking ~6th on high buyer-intent queries ("cat costa artificiile la nunta", "pret artificii nunta", "cat costa un foc de artificii la nunta", "foc de artificii nunta pret" — all visible in `query_page_28d`), a CTR this low across four consecutive pulls suggests the snippet itself, not the ranking, is the bottleneck. This is now the single largest buyer-intent impression pool in the dataset on a page that has never had a title/meta change proposed. See Action #4 in `ledger/actions.md`.

**Action #1 status check** (`/artificii-reci-fantani-scantei-t1/`, verify date 2026-08-27 — not due, 17 days out): page-level aggregate is 29 impressions / 2 clicks / position 7.7 — identical to all three prior pulls. Still no movement, as expected before the fix is applied.

**Action #2 status check** (`/preturi/`, verify date 2026-09-14 — not due, 35 days out): 103 impressions / 0 clicks / 0% CTR / position 5.8 — essentially unchanged from 2026-08-06 (107 impr / 0 clicks / pos 5.7). Still 0 clicks across two consecutive pulls now.

**Action #3 status check** (`/category/artificii-iasi-evenimente/`, verify date 2026-09-21 — not due, 42 days out): 90 impressions / 3 clicks / 3.33% CTR / position 6.9 — a small tick up from 2026-08-06 (92 impr / 2 clicks / 2.17% / pos 6.9), but within cycle-to-cycle noise at this volume, not a real movement yet. The cannibalization signal is unchanged: "artificii iasi" on this page still sits at position 12.1 (9 impressions, 0 clicks) vs. 2.9 on the homepage.

**Site health (`data/site.json`, generated 2026-08-10):** 10/12 checks green, unchanged. `/servicii` and `/despre-noi` still 404 — same stale flag, no new evidence, not re-escalated.

Note: this session's outbound network policy still blocks direct fetches to magicfire.ro (WebFetch returned `EGRESS_BLOCKED` on both `/artificii-nunta-pret-2026-romania/` and `/preturi/`). No live-page verification was possible from this session — flagged in `ledger/actions.md`.

## 2026-08-17 — fifth scored pull (28d vs prior 28d)

Source: `data/gsc.json`, generated 2026-08-17.

| Metric | Last 28d | Prior 28d | Δ |
|---|---|---|---|
| Clicks | 136 | 102 | **+34 (+33.3%)** |
| Impressions | 2,215 | 1,289 | **+926 (+71.8%)** |
| CTR | 6.14% | 7.91% | **-1.77pp** |
| Avg. position | 5.56 | 5.38 | **-0.18 (worse)** |

Impressions grew the fastest of any pull so far (+71.8%, previous best was +69.7%). Clicks kept growing too (+33.3%), but CTR fell for the third straight cycle (8.26%→6.54%→6.14%, or looking at this file's own prev/current framing: -1.72pp then -1.77pp) and — new this pull — **average position got measurably worse, not better, for the first time in five pulls** (5.38→5.56). Romania is still the large majority of traffic (85.7% of impressions, 88.2% of clicks), so this cannot be waved off as foreign-query dilution, same conclusion as last cycle. Saying the honest number: three consecutive CTR declines plus the first position regression is a real pattern, and this pull surfaces a concrete, page-level explanation for at least part of it (see below) rather than an unexplained site-wide drift.

**Device split (28d):** Mobile 117 clicks / 1,773 impr (80.1% of impressions, CTR 6.60%, pos 5.0), Desktop 19/438 (19.8%, CTR 4.34%, pos 7.9), Tablet 0/4 (pos 3.5). Mobile's share of impressions dropped from ~85-86% in every prior pull to 80.1% this pull — desktop's share nearly doubled (438 impr vs 264 last pull). Mobile is still clearly the dominant, better-converting channel (CTR 6.60% vs desktop 4.34%), so mobile-first remains the correct lens, but this shift is worth watching, not acted on without more evidence.

**Top queries by clicks (28d):**
| Query | Clicks | Impr | Position |
|---|---|---|---|
| artificii iasi | 17 | 105 | 5.1 |
| artificii galati | 3 | 32 | 6.8 |
| magicfire (brand) | 3 | 8 | 1.0 |
| artificii | 2 | 35 | 4.5 |
| artificii reci | 2 | 23 | 7.6 |
| cat costa artificiile la nunta | 2 | 19 | 5.7 |

**Top pages by clicks (28d):** homepage 100/1,215 (pos 4.9) · `/artificii-nunta-pret-2026-romania/` 15/567 (pos 6.1) · `/artificii-galati/` 9/123 (pos 6.0) · `/category/artificii-iasi-evenimente/` 4/104 (pos 7.4) · `/shop/` 4/66 (pos 8.3) · `/artificii-iasi/` 2/112 (pos 5.8) · `/artificii-reci-fantani-scantei-t1/` 2/36 (pos 7.4).

**New signal this pull — "artificii iasi" cannibalization has gotten measurably worse, with query-level page data confirming it for the first time.** This is the site's single highest-value query (17 clicks/28d — more than 5× the next query). Its blended position (5.1) is the worst it has ever been; per-page breakdown from `query_page_28d` shows why:
- Homepage: position **4.4**, 103 impr, 16 clicks — down from a stable 2.9-3.0 across all four prior pulls (07-30, 08-03, 08-06, 08-10). First real movement in five pulls, and it moved the wrong direction.
- `/artificii-iasi/` (the page whose own URL slug *is* this exact query): position **17.1**, 7 impr, 1 click — badly suppressed on the one query it should own.
- `/category/artificii-iasi-evenimente/`: position **19.6**, 9 impr, 0 clicks — worse than the 12.1 already flagged as a cannibalization signal in the 2026-08-06 pull.
Three internal pages are actively splitting relevance signal for the site's most important commercial term, and the page best-positioned to win it (the URL literally named `/artificii-iasi/`) is the most suppressed of the three. This has been carried forward as a "DEFERRED, no new evidence" item for five straight cycles (`ledger/opportunities.md`) — this pull has fresh, concrete, worsening evidence. See Action #5 in `ledger/actions.md`.

**Action #1 status check** (`/artificii-reci-fantani-scantei-t1/`, verify date 2026-08-27 — not due, 10 days out): 36 impr / 2 clicks / pos 7.4 / CTR 5.56% — impressions ticked up from 29, clicks unchanged, position slightly better than 7.7. Still not due.

**Action #2 status check** (`/preturi/`, verify date 2026-09-14 — not due, 28 days out): 87 impr / 0 clicks / pos 5.4 — impressions down from 103, still 0 clicks for a third straight pull. Position slightly better (5.4 vs 5.8).

**Action #3 status check** (`/category/artificii-iasi-evenimente/`, verify date 2026-09-21 — not due, 35 days out): 104 impr / 4 clicks / 3.85% CTR / pos 7.4 — a small uptick in impressions and clicks from 90/3/3.33%, but position slipped slightly (7.4 vs 6.9). The cannibalization angle this action already partially addresses (its proposed title de-emphasizes the exact "artificii iasi" phrase) is now confirmed worse at the query level — see the new signal above.

**Action #4 status check** (`/artificii-nunta-pret-2026-romania/`, verify date 2026-09-28 — not due, 42 days out): 567 impr / 15 clicks / pos 6.1 / CTR 2.65% — impressions nearly doubled again (311→567), the **fifth consecutive cycle of growth** on this exact page (144→148→185→311→567). Clicks grew too (9→15) but CTR stayed flat and low (2.89%→2.65%), consistent with the snippet-bottleneck read the pending fix targets. Still not due for scoring.

**Site health (`data/site.json`, generated 2026-08-17):** 10/12 checks green, unchanged. `/servicii` and `/despre-noi` still 404 — same stale flag, five cycles running, no new evidence.

Note: this session's outbound network policy still blocks direct fetches to magicfire.ro (WebFetch returned `EGRESS_BLOCKED` on `/artificii-iasi/` and `/category/artificii-iasi-evenimente/`). No live-page verification was possible from this session — flagged in `ledger/actions.md`.
