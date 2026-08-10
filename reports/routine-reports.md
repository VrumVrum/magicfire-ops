# Routine Reports — magicfire (verbatim, newest first)

## run — 2026-08-10T00:00Z

**What the numbers say:** Clicks +25.0% and impressions +58.0% over the trailing 28d vs. the prior 28d (120 vs 96 clicks, 1,836 vs 1,162 impressions). Average position improved only slightly, +0.20 (5.58→5.38) — the smallest gain of the four pulls so far. CTR fell again, -1.72pp (8.26%→6.54%), the second straight cycle of a CTR drop of similar size to the last (-1.89pp on 2026-08-06). Unlike prior cycles, this one cannot be waved off as "foreign/broad query dilution": Romania is 88.9% of impressions and 90% of clicks this pull, essentially unchanged from what a healthy local mix should look like. Saying the honest number: two consecutive CTR declines with a domestic-majority audience is a real pattern worth watching, not noise — if it continues next cycle, that becomes its own investigation rather than a side note.

**Recommended action:** title/meta rewrite on `/artificii-nunta-pret-2026-romania/` (Action #4, filed in `ledger/actions.md`) — the clearest fresh signal this cycle. This is the site's dedicated wedding-pricing landing page. Its impressions nearly doubled in four days (185→311) — the fourth straight cycle of growth on this exact page (144→148→185→311) — while CTR has stayed flat and low (2.2-2.9%) across all four pulls, at position 6.3, on unambiguous high-buyer-intent queries ("cat costa artificiile la nunta," "pret artificii nunta," "cat costa un foc de artificii la nunta"). This is now the largest buyer-intent impression pool in the whole dataset that has never had a title/meta fix proposed — bigger than any of Actions #1-#3. Proposed title: "Cât Costă Artificii de Nuntă 2026 | Preț MagicFire Iași" (55 chars). Proposed meta: "Cât costă artificiile la nuntă în 2026? Prețuri orientative pentru foc de artificii și efecte pirotehnice, Iași și Moldova. Ofertă: 0746 883 228." (145 chars). No fabricated prices or claims — "prețuri orientative" deliberately avoids stating a number we can't substantiate. Not applied — WordPress write access is not wired yet; this is the implementation-ready spec for the owner/desktop to apply. Verify date: 2026-09-28.

**Action #1 scoring** (`/artificii-reci-fantani-scantei-t1/`): not due — verify date 2026-08-27 (17 days out). Status check: no movement, identical to all three prior pulls (29 impr / 2 clicks / pos 7.7).

**Action #2 scoring** (`/preturi/`): not due — verify date 2026-09-14 (35 days out). Status check: 103 impr / 0 clicks / pos 5.8, essentially unchanged, still 0 clicks for a second straight pull.

**Action #3 scoring** (`/category/artificii-iasi-evenimente/`): not due — verify date 2026-09-21 (42 days out). Status check: 90 impr / 3 clicks / 3.33% CTR / pos 6.9, a small uptick from 2.17% but within noise at this volume, not yet a real movement. Cannibalization signal unchanged: "artificii iasi" still ranks pos 12.1 on this page vs. 2.9 on the homepage.

**Rejected/deferred this cycle** (full detail in `ledger/opportunities.md`):
- "artificii nunta" cannibalization on the homepage (pos 7.9, 14 impr, 0 clicks) — still open, no fresh evidence pointing at a specific fix beyond the internal-linking review already deferred three cycles running. Action #4 addresses the dedicated pricing page directly without requiring this broader question to be resolved first.
- `/artificii-galati/` scope question and `/servicii`/`/despre-noi` 404s — unchanged since 2026-07-30, still awaiting owner confirmation, now four cycles running.
- "petarde" — not re-checked this cycle (not in the top-15 query list this pull); no new evidence either way, still deferred as product/shop intent rather than call-conversion intent.
- The two-cycle CTR-decline pattern flagged above is not itself an action — there's no single page/query fix that explains it yet. Flagging for next cycle rather than guessing at a cause without evidence.
- No separate seasonal-spike action taken beyond Action #4: today is ~10 weeks before the Dec 31 prep window opens (~Oct 22) and wedding season is closing, not opening. Action #4 is itself the seasonal pick this cycle — it's the wedding-pricing page, timed to catch the remainder of this year's wedding season while the fix carries forward evergreen into next year.

**Needs the owner:** apply Action #4 in wp-admin (and Actions #1-#3 if not already applied); confirm current `/artificii-nunta-pret-2026-romania/` title/meta before overwriting it (this session's network policy blocks direct fetches to magicfire.ro, so the current on-page text is unverified); confirm `/artificii-galati/` scope and `/servicii`/`/despre-noi` URL expectations (carried forward, unresolved since 2026-07-30, now four cycles running).

Site health (`data/site.json`, generated 2026-08-10): 10/12 checks green, unchanged. Phone `tel:+40746883228` present and tappable above the fold, contact form present, no JS errors, no mobile overflow. `/servicii` and `/despre-noi` still 404, no new evidence either was ever a real live page.

Note: this session's outbound network policy blocks direct fetches to magicfire.ro (WebFetch returned `EGRESS_BLOCKED`). No live-page verification was possible from this session — all numbers above are read from committed `data/` files as designed.

## run — 2026-08-06T00:00Z

**What the numbers say:** Clicks +25.3% and impressions +61.1% over the trailing 28d vs. the prior 28d (114 vs 91 clicks, 1,732 vs 1,075 impressions), average position kept improving (5.67→5.09). This is the first cycle where click growth clearly decelerated relative to impression growth — CTR fell 1.89pp (8.47%→6.58%), a bigger dip than the first cycle's -0.74pp and the opposite of the second cycle's small CTR gain. Saying the honest number: clicks did not accelerate this cycle the way they did the previous two. Most likely cause, consistent with the prior read, is impression growth (broad/international queries) outpacing genuine local demand growth — mobile is still 86% of impressions at a better position than desktop (4.9 vs 6.4), so the core local audience read hasn't changed. Worth re-checking next cycle rather than treating as settled.

**Recommended action:** rewrite title + meta on `/category/artificii-iasi-evenimente/` (Action #3, filed in `ledger/actions.md`) — real, unchanged-or-worsening CTR gap (92 impr/28d, 2 clicks, 2.17% CTR, pos 6.9) plus a genuine cannibalization signal: "artificii iasi" — the site's best-performing query at pos 2.9 on the homepage — ranks only pos 12.1 on this category archive. Proposed title: "Articole Artificii pentru Evenimente Iași | MagicFire" (53 chars). Proposed meta: "Ghiduri și noutăți despre artificii, fum greu și efecte pirotehnice pentru nunți, botezuri și evenimente în Iași. Sună acum: 0746 883 228." (138 chars). Not applied — WordPress write access is not wired yet; this is the implementation-ready spec for the owner/desktop to apply. Verify date: 2026-09-21.

**Action #1 scoring** (`/artificii-reci-fantani-scantei-t1/`): not due — verify date 2026-08-27 (21 days out). Status check: no movement, identical to both prior pulls (29 impr / 2 clicks / pos 7.7), expected this early.

**Action #2 scoring** (`/preturi/`): not due — verify date 2026-09-14 (~39 days out). Status check: CTR fell further — 1 click → 0 clicks on 107 impressions, position held at 5.7. Not scored — the fix still hasn't been applied — but flagged because the gap it targets is getting worse while it waits. This reinforces the case for applying it soon, not evidence the proposed fix is wrong.

**Rejected/deferred this cycle** (full detail in `ledger/opportunities.md`):
- Second fix on `/preturi/` — CTR is now 0%, the worst signal yet, but Action #2 already targets this exact page and isn't due; stacking a second unapplied proposal on the same page breaks "one bet per cycle" without adding diagnostic value. Carrying the worsened number forward instead.
- "artificii nunta" cannibalization across homepage / `/artificii-nunta-pret-2026-romania/` / `/artificii-nunta-iasi-ghid-locatii-tendinte-2026/` — still open, no fresh evidence this cycle. Carrying forward unscored for a third cycle.
- `/artificii-galati/` scope question and `/servicii`/`/despre-noi` 404s — unchanged since 2026-07-30, still awaiting owner confirmation, now three cycles running.
- "petarde" 0% CTR — unchanged, still deferred as product/shop intent rather than call-conversion intent.
- No seasonal-spike-specific action taken: today is ~11 weeks before the Dec 31 prep window opens (~Oct 22) and wedding season is closing, not opening. Action #3 is filed as evergreen relevance work that should still land before the NYE prep window needs the calendar.

**Needs the owner:** apply Action #3 in wp-admin (and Actions #1/#2 if not already applied); confirm current `/category/artificii-iasi-evenimente/` title/meta before overwriting; confirm `/artificii-galati/` scope and `/servicii`/`/despre-noi` URL expectations (carried forward, unresolved since 2026-07-30, now three cycles running).

Site health (`data/site.json`, generated 2026-08-05): 10/12 checks green, unchanged. Phone `tel:+40746883228` present and tappable above the fold, contact form present, no JS errors, no mobile overflow. `/servicii` and `/despre-noi` still 404, no new evidence either was ever a real live page.

Note: this session's outbound network policy blocks direct fetches to magicfire.ro. No live-page verification was possible from this session — all numbers above are read from committed `data/` files as designed.
