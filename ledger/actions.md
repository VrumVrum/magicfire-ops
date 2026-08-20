# Actions — what was decided, done, and what it produced

One entry per cycle: what · why · what changed · verify date · measured outcome.

---

## 2026-07-30 (Thursday) — Action #1: title/meta rewrite on the cold-fireworks landing page

**Status:** PROPOSED (not applied — WordPress write access is not wired yet; this is the implementation-ready spec for the owner/desktop to apply).

**Page:** `https://magicfire.ro/artificii-reci-fantani-scantei-t1/`

**Evidence (`data/gsc.json`, 28d):**
- Query "artificii reci" → this page: position 7.8, 18 impressions, 2 clicks (query-level aggregate across all pages: position 8.1, 21 impressions, 2 clicks, CTR 9.5%).
- Page-level aggregate: position 7.7, 29 impressions, 2 clicks, CTR 6.9%.
- This sits squarely in the "position 4-15, on-page fix could reach top 3-5" bracket that CLAUDE.md STEP 2(a) prioritises as the fastest path to more calls — no new content needed, just a sharper title/meta on a page that already exists and already has real (if thin) search demand.
- "Artificii reci" (cold/indoor fireworks — smokeless, low-spark effects) is a real product category on the site (confirmed via search index: dedicated product tags/pages exist), and it is directly relevant to the wedding/indoor-event side of the business, not incidental shop traffic.

**Current title/meta:** **NOT VERIFIED THIS SESSION.** This session's outbound network policy blocks direct HTTPS access to magicfire.ro (proxy returned "403 to CONNECT / policy denial" on every attempt, both via WebFetch and curl). `data/site.json` only records the homepage's title/meta, not this page's. Search-engine snippets did not surface this exact URL's current `<title>`/meta. **Do not paste the proposed text over the live page blind — open the page (or its Yoast/RankMath fields in wp-admin) first and confirm what's actually there**, in case it already partially matches or an unrelated recent edit needs preserving.

**Proposed title tag** (53 chars):
`Artificii Reci și Fântâni de Scântei Iași | MagicFire`

**Proposed meta description** (133 chars):
`Artificii reci, fântâni de scântei și efecte pirotehnice de interior pentru nunți și evenimente în Iași. Cerere ofertă: 0746 883 228.`

Notes on the copy: no safety/authorization claims (§1 — pyrotechnics is regulated, "sigur"/"autorizat"-type wording was deliberately left out since it can't be substantiated from here), no invented numbers, phone number matches the verified live `tel:` link in `data/site.json`. Adds "Iași" (currently the query is competing nationally/regionally without a clear local anchor in the visible snippet) and names the wedding/event use case that matches actual buyer intent for this term.

**Why this one, not something else:** see rejected/deferred list in `ledger/opportunities.md` filed this cycle — "petarde" has a bigger CTR gap (0% at position 5.9, 37 impressions) but is shop/self-serve product intent, not the call/WhatsApp/form conversions the business runs on, so it's lower priority under the mission in CLAUDE.md even though the number looks flashier.

**Expected effect:** modest — this is a low-volume query (~20 impressions/28d). A CTR lift from ~9.5% toward local-pack-adjacent norms (15-20%) at this position would add roughly 1-3 clicks/28d directly, plus any position gain from improved engagement signals. Sized correctly for "one small reversible bet," not a page rewrite.

**Verify date:** 2026-08-27 (next-but-one biweekly cycle after this one — gives ~4 weeks for Search Console position/CTR to stabilize post-change). On that date: re-pull `data/gsc.json`, compare this query/page's position and CTR against the 2026-07-30 baseline above, score Win/Loss/Inconclusive.

**Seasonal read (STEP 2d):** Today, 2026-07-30, is not inside either spike-prep window — the Dec 31 spike's 6-10-week lead-in starts ~Oct 22; wedding season (May-Sep) is already underway and closing in ~6 weeks, so a title/meta change now captures the tail of it but isn't timed to a spike. This is filed as an evergreen local-relevance fix (also serves baptisms/corporate events year-round), not a seasonal bet. No seasonal action was identified this cycle with strong enough evidence to justify jumping ahead of this fix — see opportunities.md.

**Needs the owner:** applying this change (WordPress access not wired to this routine yet), and confirming current on-page text before overwriting it, per above.

---

### Cycle report — 2026-07-30

**What the numbers say:** Clicks +50% and impressions +65% over the trailing 28d vs. the prior 28d, average position improved from 5.69 to 5.02. CTR dipped slightly (8.2%→7.5%), consistent with the impression growth pulling in more broad/international/low-intent queries rather than a genuine ranking-quality problem — 85% of clicks and impressions are mobile, matching the business's actual customer. "artificii iasi" (the core local query) sits at position 3 with an 18.5% CTR on the homepage — already strong; no changes recommended there this cycle.

**Recommended action:** rewrite title + meta on `/artificii-reci-fantani-scantei-t1/` (Action #1 above).

**Rejected/deferred this cycle** (full detail in `ledger/opportunities.md`):
- "petarde" 0% CTR at position 5.9 (37 impr) — real gap, but product/shop-purchase intent, not a local-call conversion; deferred, not rejected outright.
- "artificii nunta" — the money term for the wedding side ranks only 9.6 on the homepage while a dedicated page (`/artificii-nunta-pret-2026-romania/`) ranks #1 for the narrower "artificii nunta pret" query and a newer guide page (`/artificii-nunta-iasi-ghid-locatii-tendinte-2026/`) ranks 2.5 but has only 2 impressions total — looks like page cannibalization/thin-signal, not a one-line fix. Needs a proper look at internal linking between these three URLs before touching anything; too big for "one small reversible bet" this cycle.
- `/artificii-galati/` — second-biggest page by clicks (16/182, pos 5.8), but Galați is outside the Iași+județ scope CLAUDE.md defines for this business; not acted on, flagged for the owner to confirm whether Galați is actually in scope.
- `/servicii` and `/despre-noi` 404s in `data/site.json` — no GSC evidence either URL ever ranked or was linked; likely a stale assumption in the health-check's URL list rather than a real broken page. Not acted on; flagged for the owner to confirm intended URL structure.
- No prior actions existed to score this cycle (first real KPI pull — `ledger/KPIS.md` was empty coming in).

**Needs the owner:** apply Action #1 in wp-admin (WordPress write access not yet wired to this routine); confirm whether `/artificii-galati/` targeting Galați is intentional; confirm `/servicii` and `/despre-noi` URL expectations.

---

## 2026-08-03 (Monday) — Action #2: title/meta rewrite on the pricing page

**Status:** PROPOSED (not applied — WordPress write access still not wired; this is the implementation-ready spec for the owner/desktop to apply).

**Page:** `https://magicfire.ro/preturi/`

**Evidence (`data/gsc.json`, 28d, generated 2026-08-02):**
- Page-level aggregate: position 5.7, **120 impressions, only 1 click (0.83% CTR)**.
- This is the largest CTR gap in the entire `pages_28d` dataset this cycle: it has the 4th-highest impression count (behind only the homepage, `/artificii-galati/`, and `/artificii-nunta-pret-2026-romania/`) but by far the worst conversion of impressions into clicks — every other page above 40 impressions converts at 3-10% CTR.
- Position 5.7 sits squarely in the "position 4-15, on-page fix could reach top 3" bracket CLAUDE.md STEP 2(a) prioritises — the page is already being shown, it just isn't being clicked.
- A pricing page is inherently high buyer-intent: someone searching pricing terms is closer to calling/messaging than someone searching a generic informational term. Per the mission (local visibility → site visit → call/WhatsApp/form), this is one of the highest-leverage pages on the whole site to fix, because the traffic is already there — the only failure is the snippet not earning the click.
- `query_page_28d` does not break out individual queries landing on `/preturi/` at the row-count threshold GSC exports at this volume, so the specific search terms behind these 120 impressions aren't visible — the page-level aggregate is still strong enough evidence to act on (STEP 2 does not require query-level granularity, and the CTR gap is unambiguous regardless of which exact queries make it up).

**Current title/meta:** **NOT VERIFIED THIS SESSION.** Same network restriction as Action #1 — this session's outbound policy blocks direct HTTPS access to magicfire.ro (WebFetch returned HTTP 403 on `/preturi/`). **Do not paste the proposed text over the live page blind — open the page (or its Yoast/RankMath fields in wp-admin) first and confirm what's actually there**, in case the low CTR is caused by something other than the title/meta (e.g. a misleading snippet, a rich-result eating the click, or the page ranking for a mismatched query) — if so, hold this change and re-diagnose rather than applying text that doesn't address the real cause.

**Proposed title tag** (56 chars):
`Prețuri Artificii și Foc de Artificii Iași | MagicFire`

**Proposed meta description** (152 chars):
`Prețuri artificii pentru nunți, botezuri și evenimente în Iași. Pachete pe măsura bugetului tău. Cerere ofertă rapidă: 0746 883 228.`

Notes on the copy: no fabricated numbers, no authorization/safety claims (§1, §7 — pricing pages don't need them and shouldn't invent them), phone number matches the verified live `tel:` link in `data/site.json`. Adds "Iași" for local anchoring, names the two biggest non-NYE occasions (nunți, botezuri) that drive this business per CLAUDE.md, and leads with "Prețuri" since that's the exact intent signal a pricing-page searcher is scanning results for.

**Why this one, not something else:** the `/artificii-nunta` cannibalization question (deferred both 2026-07-30 and again this cycle — no new signal since last pull to justify the internal-linking review effort) and `/artificii-galati/` scope question remain open for the owner but neither has fresh evidence this cycle. `/category/artificii-iasi-evenimente/` also has a real CTR gap (97 impr, 3 clicks, 3.1% CTR, pos 7.0) but it's a category archive page, not a single page with one title/meta to fix — lower-leverage edit for the same effort. `/preturi/` is the single clearest, cleanest, lowest-effort, highest-buyer-intent gap this cycle.

**Expected effect:** if the CTR problem is genuinely the snippet (not yet confirmed — see caveat above), moving from 0.83% toward even a modest 4-6% CTR at 120 impressions/28d would add roughly 4-6 clicks/28d — the single biggest realistic click gain of any opportunity in this pull, several times the size of Action #1's expected effect.

**Verify date:** 2026-09-14 (~6 weeks out — one full cycle later than Action #1's 4-week window, since this page's current snippet hasn't been seen yet and the owner may need an extra cycle to both confirm current text and apply the change). On that date: re-pull `data/gsc.json`, compare `/preturi/` clicks/CTR/position against the 2026-08-02 baseline above (120 impr / 1 click / 0.83% CTR / pos 5.7), score Win/Loss/Inconclusive.

**Seasonal read (STEP 2d):** Today, 2026-08-03, is inside the tail of wedding season (May-Sep, closing in ~8 weeks) and well before the Dec 31 spike's 6-10-week lead-in window (starts ~Oct 22). A pricing page is evergreen and serves both weddings now and the NYE spike later without needing separate seasonal copy, so there's no timing conflict — but it does mean this fix should land soon to still catch tail-end wedding pricing searches this season, not slip past September.

**Needs the owner:** applying this change (WordPress access not wired to this routine yet); confirming current on-page title/meta on `/preturi/` before overwriting it, per above; and — unchanged from 2026-07-30 — confirming `/artificii-galati/` scope and `/servicii`/`/despre-noi` URL expectations.

---

### Cycle report — 2026-08-03

**What the numbers say:** Clicks +80.5% and impressions +69.7% over the trailing 28d vs. the prior 28d (139 vs 77 clicks, 1,746 vs 1,029 impressions), average position improved from 5.71 to 5.01, and this time CTR moved up slightly too (7.48%→7.96%) rather than dipping — the growth trend from the last pull is holding and broadening, not just an impression spike diluting engagement. Mobile remains 85% of impressions at a slightly better position than desktop (4.8 vs 6.4), confirming mobile-first is still the right lens.

**Recommended action:** rewrite title + meta on `/preturi/` (Action #2 above) — the clearest, best-evidenced, single highest-value move this cycle: a high buyer-intent page ranking respectably (pos 5.7) but converting almost none of its 120 impressions into clicks.

**Action #1 scoring:** not due — verify date is 2026-08-27. Logged a status check in `ledger/KPIS.md`: no meaningful movement yet on `/artificii-reci-fantani-scantei-t1/` (29 impr / 2 clicks / pos 7.7, unchanged from baseline), which is expected this early.

**Rejected/deferred this cycle** (full detail in `ledger/opportunities.md`):
- "artificii nunta" cannibalization across homepage / `/artificii-nunta-pret-2026-romania/` / `/artificii-nunta-iasi-ghid-locatii-tendinte-2026/` — still open, no fresh evidence this cycle to justify prioritizing the internal-linking review over the cleaner `/preturi/` fix. Carrying forward, not re-scored.
- `/category/artificii-iasi-evenimente/` CTR gap (97 impr, 3 clicks, 3.1% CTR, pos 7.0) — real, but a category archive rather than a single editable page/post; lower leverage per unit of effort than `/preturi/` this cycle. Filed as a candidate for a future cycle.
- `/artificii-galati/` scope question and `/servicii`/`/despre-noi` 404s — unchanged since 2026-07-30, still awaiting owner confirmation, not re-actioned without new evidence.
- "petarde" 0% CTR — unchanged, still deferred as product/shop intent rather than call-conversion intent.
- No seasonal-spike-specific action taken: today is before the Dec 31 prep window (starts ~Oct 22) and wedding season is closing, not opening — `/preturi/` was chosen as an evergreen fix that still helps both, per the seasonal read above.

**Needs the owner:** apply Action #2 in wp-admin (and Action #1 if not already applied); confirm current `/preturi/` title/meta before overwriting; confirm `/artificii-galati/` scope and `/servicii`/`/despre-noi` URL expectations (carried forward, unresolved since 2026-07-30).

---

## 2026-08-06 (Thursday) — Action #3: title/meta rewrite on the events category archive

**Status:** PROPOSED (not applied — WordPress write access still not wired; this is the implementation-ready spec for the owner/desktop to apply).

**Page:** `https://magicfire.ro/category/artificii-iasi-evenimente/` (category archive)

**Evidence (`data/gsc.json`, 28d, generated 2026-08-05):**
- Page-level aggregate: position 6.9, 92 impressions, 2 clicks, 2.17% CTR — flagged as a candidate in `ledger/opportunities.md` on 2026-08-03 ("filed for a future cycle"); this is that cycle, and the gap has not closed on its own (was 97 impr / 3 clicks / 3.1% CTR / pos 7.0 on 2026-08-03 — flat to slightly worse).
- Position 6.9 sits in the "position 4-15, on-page fix could reach top 3-5" bracket CLAUDE.md STEP 2(a) prioritises, and a category archive's SEO title/meta is a single Yoast/RankMath field — same very-low-effort shape as Actions #1 and #2.
- The sharper signal is at query level: `query_page_28d` shows "artificii iasi" — the site's single best-performing query (pos 2.9, 22 clicks on the homepage) — landing on *this* page at **position 12.1** (9 impressions, 0 clicks). The category archive appears to be competing for the exact commercial term the homepage already owns comfortably, and losing by ~9 positions instead of serving a distinct intent. That's wasted relevance, not just a weak snippet.
- The fix proposed here is not just a copy tweak: it repositions this page's on-page SEO target away from head-on "artificii iasi" competition and toward what a category archive of blog/guide posts actually is — a content/ghid hub — so it stops cannibalizing the homepage's stronger ranking for the money query while still capturing informational searches (nunți, botezuri, evenimente) that funnel toward a call.

**Current title/meta:** **NOT VERIFIED THIS SESSION.** Same network restriction as Actions #1 and #2 — this session's outbound policy blocks direct HTTPS access to magicfire.ro. **Do not paste the proposed text over the live page blind — open the page (or its Yoast/RankMath category SEO fields in wp-admin) first and confirm what's actually there.**

**Proposed title tag** (53 chars):
`Articole Artificii pentru Evenimente Iași | MagicFire`

**Proposed meta description** (138 chars):
`Ghiduri și noutăți despre artificii, fum greu și efecte pirotehnice pentru nunți, botezuri și evenimente în Iași. Sună acum: 0746 883 228.`

Notes on the copy: no fabricated data or authorization/safety claims (§1), phone number matches the verified live `tel:` link in `data/site.json`. "Articole"/"Ghiduri" signals this is a content hub (matching what a category archive of blog posts actually is) rather than re-competing with the homepage for "artificii iasi" — deliberately does NOT lead with "Artificii Iași" the way the homepage title does, to reduce cannibalization risk rather than add to it.

**Why this one, not something else:** `/preturi/`'s CTR fell further this pull (1 click → 0 clicks) but Action #2 is already proposed and not yet due (2026-09-14) — proposing a second fix on the same unapplied page would violate "one bet per cycle" without new diagnostic value. "artificii nunta" cannibalization (deferred twice, still no fresh evidence this pull) and `/artificii-galati/` scope (owner-gated, unchanged) remain open but inactionable without new signal. This category page is the one item with both fresh, unambiguous evidence and a clean two-field fix.

**Expected effect:** modest but real — closing even part of the position-12.1-vs-2.9 gap for "artificii iasi" reduces internal competition rather than adding clicks directly; the CTR-focused title/meta change on the page's own 92 impressions, if it lifts CTR from 2.17% toward a more typical 5-8% for this position band, would add roughly 3-5 clicks/28d. Sized as one small reversible bet, consistent with the two prior actions.

**Verify date:** 2026-09-21 (~6.5 weeks out, matching Action #2's cadence since this also depends on the owner both confirming current text and applying the change through an unwired WordPress connection).

**Seasonal read (STEP 2d):** Today, 2026-08-06, is in the tail of wedding season (May-Sep, closing in ~8 weeks) and well before the Dec 31 spike's 6-10-week lead-in window (starts ~Oct 22, i.e. ~11 weeks away). This is filed as an evergreen relevance/cannibalization fix, not a seasonal bet — it should land soon so it has time to settle before the Dec 31 prep window needs the calendar clear for NYE-specific work.

**Needs the owner:** applying this change (WordPress access not wired to this routine yet); confirming current on-page title/meta before overwriting it; and — unchanged and still open — applying Actions #1 and #2, confirming `/artificii-galati/` scope, and confirming `/servicii`/`/despre-noi` URL expectations.

---

### Cycle report — 2026-08-06

**What the numbers say:** Clicks +25.3% and impressions +61.1% over the trailing 28d vs. the prior 28d (114 vs 91 clicks, 1,732 vs 1,075 impressions), average position kept improving (5.67→5.09). This is the first cycle where click growth clearly decelerated relative to impression growth — CTR fell 1.89pp (8.47%→6.58%), a bigger dip than the first cycle's -0.74pp and the opposite of the second cycle's small CTR gain. Saying the honest number: clicks did not accelerate this cycle the way they did the previous two. Most likely cause, consistent with the prior read, is impression growth (broad/international queries) outpacing genuine local demand growth — mobile is still 86% of impressions at a better position than desktop (4.9 vs 6.4), so the core local audience read hasn't changed. Worth re-checking next cycle rather than treating as settled.

**Recommended action:** rewrite title + meta on `/category/artificii-iasi-evenimente/` (Action #3 above) — real, unchanged-or-worsening CTR gap plus a genuine cannibalization signal against the homepage's strongest query, fixable with a two-field edit.

**Action #1 scoring:** not due — verify date 2026-08-27 (21 days out). Status check in `ledger/KPIS.md`: no movement, identical to both prior pulls (29 impr / 2 clicks / pos 7.7), expected this early.

**Action #2 scoring:** not due — verify date 2026-09-14 (~39 days out). Status check in `ledger/KPIS.md`: CTR fell further (1 click → 0 clicks on 107 impressions, position held at 5.7). Not scored — the fix still hasn't been applied — but flagged because the gap it targets is getting worse while it waits.

**Rejected/deferred this cycle** (full detail in `ledger/opportunities.md`):
- Second fix on `/preturi/` — CTR is now 0%, the worst signal yet, but Action #2 already targets this exact page and isn't due; stacking a second unapplied proposal on the same page breaks "one bet per cycle" without adding diagnostic value. Carrying the worsened number forward instead.
- "artificii nunta" cannibalization across homepage / `/artificii-nunta-pret-2026-romania/` / `/artificii-nunta-iasi-ghid-locatii-tendinte-2026/` — still open, no fresh evidence this cycle (12 impr on homepage vs ~10-12 in prior pulls). Carrying forward unscored for a third cycle.
- `/artificii-galati/` scope question and `/servicii`/`/despre-noi` 404s — unchanged since 2026-07-30, still awaiting owner confirmation.
- "petarde" 0% CTR — unchanged, still deferred as product/shop intent rather than call-conversion intent.
- No seasonal-spike-specific action taken: today is ~11 weeks before the Dec 31 prep window opens (~Oct 22) and wedding season is closing, not opening. Action #3 is filed as evergreen relevance work that should still land before the NYE prep window needs the calendar.

**Needs the owner:** apply Action #3 in wp-admin (and Actions #1/#2 if not already applied); confirm current `/category/artificii-iasi-evenimente/` title/meta before overwriting; confirm `/artificii-galati/` scope and `/servicii`/`/despre-noi` URL expectations (carried forward, unresolved since 2026-07-30, now three cycles running).

---

## 2026-08-10 (Monday) — Action #4: title/meta rewrite on the wedding-pricing page

**Status:** PROPOSED (not applied — WordPress write access still not wired; this is the implementation-ready spec for the owner/desktop to apply).

**Page:** `https://magicfire.ro/artificii-nunta-pret-2026-romania/`

**Evidence (`data/gsc.json`, 28d, generated 2026-08-10):**
- Page-level aggregate: position 6.3, **311 impressions, 9 clicks, 2.89% CTR**.
- Four-cycle trend on this exact page (from `ledger/KPIS.md`): 144 impr/4 clicks (07-30) → 148/4 (08-03) → 185/4 (08-06) → **311/9 (08-10)**. Impressions nearly doubled in the last four days alone, and this is the fourth consecutive cycle of growth — a real, sustained signal, not a one-off blip. CTR has stayed low and essentially flat across all four pulls (2.8% → 2.7% → 2.2% → 2.9%), so the growth in impressions has not been matched by proportional growth in clicks.
- `query_page_28d` shows this page landing on unambiguous high-buyer-intent, price-question queries: "cat costa artificiile la nunta" (12 impr, pos 5.9), "cat costa un foc de artificii la nunta" (11 impr, pos 6.6), "pret artificii nunta" (11 impr, pos 7.4), "foc de artificii nunta pret" (7 impr, pos 8.7), "artificii nunta interior" (10 impr, pos 8.2), plus others — all people actively asking "how much does this cost," the exact mid-funnel intent this page exists to answer. Named queries only account for ~65 of the 311 impressions (GSC's per-row threshold suppresses the long tail at this volume), but the visible sample confirms the traffic is on-topic, not stray/irrelevant.
- Position 6.3 sits in the "position 4-15, on-page fix could reach top 3" bracket CLAUDE.md STEP 2(a) prioritises, and this is now the single largest buyer-intent impression pool in the entire dataset that has never had a title/meta change proposed (bigger than `/preturi/`'s 103 impr, `/category/artificii-iasi-evenimente/`'s 90 impr, or Action #1's 29 impr).
- Country split confirms this volume is not foreign dilution: Romania is 88.9% of impressions / 90% of clicks sitewide this pull (see `ledger/KPIS.md`), so the CTR gap here reads as a snippet problem, not an audience-mismatch problem.

**Current title/meta:** **NOT VERIFIED THIS SESSION.** This session's outbound network policy blocks direct HTTPS access to magicfire.ro — WebFetch returned `EGRESS_BLOCKED` on this exact URL. **Do not paste the proposed text over the live page blind — open the page (or its Yoast/RankMath fields in wp-admin) first and confirm what's actually there**, in case the flat 2-3% CTR across four cycles has a different cause than the snippet (e.g. a misleading title already, a rich result, or the URL's own "2026" datedness reading stale by the time this is applied).

**Proposed title tag** (55 chars):
`Cât Costă Artificii de Nuntă 2026 | Preț MagicFire Iași`

**Proposed meta description** (145 chars):
`Cât costă artificiile la nuntă în 2026? Prețuri orientative pentru foc de artificii și efecte pirotehnice, Iași și Moldova. Ofertă: 0746 883 228.`

Notes on the copy: no fabricated numbers or price figures (§1 — "prețuri orientative" language deliberately avoids stating a number we have not verified we can substantiate), no authorization/safety claims, phone number matches the verified live `tel:` link in `data/site.json`. Title leads with "Cât Costă" to mirror the exact phrasing of the top queries landing on this page ("cat costa artificiile la nunta", "cat costa un foc de artificii la nunta") — matching searcher phrasing in the visible snippet is the most direct lever for CTR at a fixed position. Keeps "Iași" as the local anchor consistent with Actions #1-#3, even though this page's URL is nationally framed ("romania") — the business itself is Iași-based, and CLAUDE.md's local-relevance principle applies regardless of the page's existing URL structure.

**Why this one, not something else:** `/preturi/` (Action #2, still not due, 0 clicks unchanged) and `/category/artificii-iasi-evenimente/` (Action #3, still not due, ticked up slightly) both remain open but neither has fresh evidence this cycle — this page does, and its evidence (impressions nearly doubling in four days, on a page carrying 3x the buyer-intent volume of any pending action) is the strongest single signal in this pull. "artificii nunta" cannibalization on the *homepage* (still pos 7.9, 14 impr, 0 clicks) remains a separate, deferred, medium-high-effort question — this action targets the dedicated pricing page directly and does not depend on resolving that cannibalization first.

**Expected effect:** potentially the largest of any action proposed so far, but sized cautiously because the impression surge itself is new and unconfirmed to persist. If CTR moves from 2.89% toward a more typical 5-7% for position ~6 on a high-intent query, and the 311-impression volume holds, that's roughly +6-13 clicks/28d. If the volume normalizes back toward the ~150-185 range seen in prior cycles, the same CTR lift would still add roughly +3-7 clicks/28d. Either way this is a bigger realistic gain than Actions #1-#3.

**Verify date:** 2026-09-28 (~7 weeks out — slightly longer than the other actions, to give both the CTR change and the fresh impression-volume trend time to show whether the surge is durable or transient before scoring).

**Seasonal read (STEP 2d):** Today, 2026-08-10, is in the tail of wedding season (May-Sep, closing in ~7 weeks) and ~10 weeks before the Dec 31 spike's 6-10-week lead-in window opens (~Oct 22). This page is wedding-specific, not NYE-specific, so it should land now to still catch the remainder of this year's wedding-pricing searches — and title/meta improvements are evergreen, so they carry forward into next year's wedding season too rather than expiring with "2026" in the URL.

**Needs the owner:** applying this change (WordPress access not wired to this routine yet); confirming current on-page title/meta before overwriting it, per above; and — unchanged and carried forward — applying Actions #1-#3, confirming `/artificii-galati/` scope, and confirming `/servicii`/`/despre-noi` URL expectations.

---

### Cycle report — 2026-08-10

**What the numbers say:** Clicks +25.0% and impressions +58.0% over the trailing 28d vs. the prior 28d (120 vs 96 clicks, 1,836 vs 1,162 impressions). Average position improved only slightly, +0.20 (5.58→5.38) — the smallest gain of the four pulls so far. CTR fell again, -1.72pp (8.26%→6.54%), the second straight cycle of a CTR drop of similar size to the last (-1.89pp on 2026-08-06). Unlike prior cycles, this one cannot be waved off as "foreign/broad query dilution": Romania is 88.9% of impressions and 90% of clicks this pull, essentially unchanged from what a healthy local mix should look like. Saying the honest number: two consecutive CTR declines with a domestic-majority audience is a real pattern worth watching, not noise — if it continues next cycle, that becomes its own investigation rather than a side note.

**Recommended action:** title/meta rewrite on `/artificii-nunta-pret-2026-romania/` (Action #4 above) — the clearest fresh signal this cycle: impressions nearly doubled in four days on the site's single largest pool of high-buyer-intent (wedding pricing) traffic, with CTR flat and low across four consecutive pulls.

**Action #1 scoring:** not due — verify date 2026-08-27 (17 days out). Status check in `ledger/KPIS.md`: no movement, identical to all three prior pulls (29 impr / 2 clicks / pos 7.7).

**Action #2 scoring:** not due — verify date 2026-09-14 (35 days out). Status check in `ledger/KPIS.md`: 103 impr / 0 clicks / pos 5.8, essentially unchanged, still 0 clicks for a second straight pull.

**Action #3 scoring:** not due — verify date 2026-09-21 (42 days out). Status check in `ledger/KPIS.md`: 90 impr / 3 clicks / 3.33% CTR / pos 6.9, a small uptick from 2.17% but within noise at this volume, not yet a real movement.

**Rejected/deferred this cycle** (full detail in `ledger/opportunities.md`):
- "artificii nunta" cannibalization on the homepage (pos 7.9, 14 impr, 0 clicks) — still open, still no fresh evidence pointing at a specific fix beyond the internal-linking review already deferred three cycles running. Action #4 addresses the dedicated pricing page directly without requiring this broader question to be resolved first.
- `/artificii-galati/` scope question and `/servicii`/`/despre-noi` 404s — unchanged since 2026-07-30, still awaiting owner confirmation, now four cycles running.
- "petarde" — not re-checked this cycle (not in the top-15 query list this pull); no new evidence either way, still deferred as product/shop intent rather than call-conversion intent per the original reasoning.
- The CTR-decline pattern flagged above is not itself an action — there's no single page/query fix that explains it yet. Flagging for next cycle rather than guessing at a cause without evidence.
- No separate seasonal-spike action taken beyond Action #4: today is ~10 weeks before the Dec 31 prep window opens (~Oct 22) and wedding season is closing, not opening. Action #4 is itself the seasonal pick this cycle — it's the wedding-pricing page, timed to catch the remainder of this year's wedding season while the fix carries forward evergreen.

**Needs the owner:** apply Action #4 in wp-admin (and Actions #1-#3 if not already applied); confirm current `/artificii-nunta-pret-2026-romania/` title/meta before overwriting; confirm `/artificii-galati/` scope and `/servicii`/`/despre-noi` URL expectations (carried forward, unresolved since 2026-07-30, now four cycles running).

---

## 2026-08-17 (Monday) — Action #5: title/meta rewrite on `/artificii-iasi/` to fix keyword cannibalization on the site's top query

**Status:** PROPOSED (not applied — WordPress write access still not wired; this is the implementation-ready spec for the owner/desktop to apply).

**Page:** `https://magicfire.ro/artificii-iasi/`

**Evidence (`data/gsc.json`, 28d, generated 2026-08-17):**
- "artificii iasi" is the single highest-value query in the entire dataset (17 clicks / 105 impressions / 28d — more than 5× the next-best query). Its blended position this pull is 5.1, the worst it has ever measured. `query_page_28d` shows why, broken out per page:
  - Homepage: position **4.4**, 103 impr, 16 clicks.
  - `/artificii-iasi/` — the page whose own URL slug *is* this exact query: position **17.1**, 7 impr, 1 click.
  - `/category/artificii-iasi-evenimente/`: position **19.6**, 9 impr, 0 clicks.
- Three pages on the same site are actively splitting relevance signal for the one term the business most needs to win, and the page built specifically for it (`/artificii-iasi/`) is the *most* suppressed of the three — a textbook keyword-cannibalization pattern, not noise.
- This is fresh, concrete evidence, not a repeat of the vague carried-forward flag: the homepage's own position on this query held stable at 2.9-3.0 across all four prior pulls (2026-07-30 through 2026-08-10) and only moved this pull — to 4.4, the wrong direction — the same pull where `/category/artificii-iasi-evenimente/`'s position on this query also worsened (12.1 → 19.6, per `ledger/KPIS.md` 2026-08-06 and this pull). Both moving the wrong way together, on the exact same query, at the same time, is the cannibalization signature.
- "Keyword cannibalization" (b, local-intent gap) and STEP 2(a) (position 4-15 fixable by on-page change) both apply here: the homepage sits at 4.4, squarely in the top-3-reachable bracket, and the likely blocker is the two other pages competing for the identical phrase rather than the homepage's own content being weak.
- This exact opportunity ("artificii nunta"'s sibling issue, "artificii iasi" cannibalization) has been logged as **DEFERRED, no new evidence** in `ledger/opportunities.md` for five straight cycles (2026-07-30 through 2026-08-10) specifically because it was "too big for one reversible bet" / lacked a concrete trigger. This pull provides one: a measurable, fresh regression on the money query, with a clear single-page fix available (retarget the one page that's never had a proposal, `/artificii-iasi/`) rather than the full 3-URL internal-linking review previously deemed too large.

**Current title/meta:** **NOT VERIFIED THIS SESSION.** This session's outbound network policy blocks direct HTTPS access to magicfire.ro — WebFetch returned `EGRESS_BLOCKED` on this exact URL. **Do not paste the proposed text over the live page blind — open the page (or its Yoast/RankMath fields in wp-admin) first and confirm what's actually there.** In particular, confirm whether the current title/meta already targets the bare phrase "artificii iasi" head-on (which would explain the direct duplication with the homepage) — if it targets something else already, the cannibalization has a different cause and this proposal should be reconsidered before applying.

**Proposed title tag** (50 chars):
`Spectacol Artificii Iași – Cere Ofertă | MagicFire`

**Proposed meta description** (150 chars):
`Organizăm spectacole de artificii personalizate în Iași: nunți, botezuri, evenimente corporate. Efecte pirotehnice profesionale. Ofertă: 0746 883 228.`

Notes on the copy: no fabricated numbers, review counts, or authorization claims (§1). Phone number matches the verified live `tel:` link in `data/site.json`. The rewrite deliberately does **not** lead with the bare contiguous phrase "artificii iasi" — it keeps both words (so the page stays topically relevant and doesn't lose all signal for the term) but reframes around booking/offer intent ("Cere Ofertă", "Ofertă rapidă") instead of duplicating the homepage's head-term targeting. This is metadata-only — no change to the page's URL, H1, body content, or any redirect — so it stays as reversible and low-risk as Actions #1-#4 despite touching the site's most important query. `/category/artificii-iasi-evenimente/` is deliberately **not** touched again this cycle: Action #3 (still pending application, verify 2026-09-21) already proposed a title for that page that de-emphasizes the exact contiguous phrase, so a second edit there this cycle would stack an unapplied change on top of another unapplied change without new page-specific evidence — one bet per cycle.

**Why this one, not something else:** Actions #1-#4 all remain open (none due for scoring — nearest is Action #1 at 10 days out) and none show a fresh evidence trigger this pull beyond normal small movement. This action does have a fresh trigger: the site's #1 query regressed for the first time in five pulls, and the per-page breakdown (newly visible via `query_page_28d` cross-referenced across pages) pinpoints a specific, previously-unactioned page as the likely cause. It also finally converts the long-carried "artificii iasi cannibalization" opportunity from a deferred, oversized idea into a small, concrete, reversible bet — consistent with the "one bet per cycle" and "small, reversible" discipline in `CLAUDE.md`, rather than attempting the full 3-URL internal-linking review in one move.

**Expected effect:** primary goal is defensive — stop the regression on the site's highest-value query and let the homepage recover toward its 2.9-3.0 historical position, which would be worth several additional clicks/28d on its own given 100+ impressions/28d at that query. Secondary goal: `/artificii-iasi/` itself may pick up a small amount of new impressions/clicks on the differentiated booking-intent phrasing it will now target, rather than losing entirely to the homepage. Sized cautiously — this is a metadata change addressing a suspected but not directly provable cause (Google does not publish cannibalization diagnostics); if the homepage's position does not recover, that itself is useful evidence the cause lies elsewhere (e.g. algorithmic noise, a backlink change, a technical issue) and should be said honestly at scoring time rather than reinterpreted to fit the hypothesis.

**Verify date:** 2026-09-14 (~4 weeks out — same horizon as Action #2, chosen to give the homepage's position at least a few weeks to move given it only just regressed this pull; long enough to distinguish signal from week-to-week noise, short enough to catch it before the wedding season / NYE prep windows need attention).

**Seasonal read (STEP 2d):** Today, 2026-08-17, wedding season (May-Sep) has about 6 weeks left, and the Dec 31 spike's 6-10-week lead-in window opens around 2026-10-22 — still ~9 weeks away, so no NYE-specific content push is due yet. "artificii iasi" is a year-round core term (not season-specific), so protecting/recovering its ranking now is timing-neutral — it matters in every season — and is not competing with a more time-sensitive seasonal pick this cycle.

**Needs the owner:** applying this change (WordPress access not wired to this routine yet); confirming current on-page title/meta on `/artificii-iasi/` before overwriting it, per above; and — unchanged and carried forward — applying Actions #1-#4, confirming `/artificii-galati/` scope, and confirming `/servicii`/`/despre-noi` URL expectations.

---

### Cycle report — 2026-08-17

**What the numbers say:** Clicks +33.3% and impressions +71.8% over the trailing 28d vs. the prior 28d (136 vs 102 clicks, 2,215 vs 1,289 impressions) — the fastest impression growth of any pull so far. But CTR fell for the third straight cycle (-1.77pp, 7.91%→6.14%) and, new this pull, average position got measurably *worse* for the first time in five pulls (5.38→5.56). Romania remains the large majority of traffic (85.7% of impressions, 88.2% of clicks), so this isn't foreign-query dilution. The concrete, page-level explanation surfaced this pull: "artificii iasi" — the site's single highest-value query — is being cannibalized across three internal pages (homepage pos 4.4, `/artificii-iasi/` pos 17.1, `/category/artificii-iasi-evenimente/` pos 19.6), and the homepage's own position on this term moved for the first time in five pulls, the wrong direction (2.9→4.4). Mobile's share of impressions also dropped from ~85-86% to 80.1% this pull — flagged as worth watching, not yet acted on.

**Recommended action:** title/meta rewrite on `/artificii-iasi/` (Action #5 above) — converts the long-deferred "artificii iasi cannibalization" opportunity into a small, concrete, reversible bet now that there's a fresh trigger (the homepage's first-ever regression on this query, plus worsening per-page evidence pinpointing the cause) and a specific previously-unactioned page to fix.

**Action #1 scoring:** not due — verify date 2026-08-27 (10 days out). Status check in `ledger/KPIS.md`: 36 impr / 2 clicks / pos 7.4 — impressions ticked up, clicks unchanged.

**Action #2 scoring:** not due — verify date 2026-09-14 (28 days out). Status check in `ledger/KPIS.md`: 87 impr / 0 clicks / pos 5.4 — still 0 clicks, third straight pull.

**Action #3 scoring:** not due — verify date 2026-09-21 (35 days out). Status check in `ledger/KPIS.md`: 104 impr / 4 clicks / 3.85% CTR / pos 7.4 — small uptick, but the cannibalization angle it partly addresses is confirmed worse at the query level this pull.

**Action #4 scoring:** not due — verify date 2026-09-28 (42 days out). Status check in `ledger/KPIS.md`: 567 impr / 15 clicks / pos 6.1 / CTR 2.65% — impressions nearly doubled again, fifth straight cycle of growth, CTR still flat.

**Rejected/deferred this cycle** (full detail in `ledger/opportunities.md`):
- `/category/artificii-iasi-evenimente/` — not given a second, separate title/meta edit this cycle even though its cannibalization signal also worsened (pos 12.1→19.6 on "artificii iasi"): Action #3 already has a pending, unapplied proposal for this exact page; stacking a second unapplied change on the same page breaks "one bet per cycle" without new page-specific evidence beyond what Action #3 already targets.
- "artificii nunta" cannibalization across homepage / `/artificii-nunta-pret-2026-romania/` / `/artificii-nunta-iasi-ghid-locatii-tendinte-2026/` (carried forward, 6th cycle) — no fresh evidence this pull; remains separate from the "artificii iasi" issue actioned above.
- `/artificii-galati/` scope question and `/servicii`/`/despre-noi` 404s (carried forward, 5th cycle) — unchanged since 2026-07-30, still awaiting owner confirmation.
- "petarde" — still 0 clicks on 40 impr/28d, pos 6.6; unchanged reasoning (shop/self-serve intent, not call conversion), not re-proposed.
- The mobile-share drop (85-86%→80.1% of impressions) is flagged, not acted on — one pull is not enough to call it a trend, and mobile remains the clearly better-converting channel either way.
- No separate seasonal-spike action taken: wedding season has ~6 weeks left and the Dec 31 prep window doesn't open until ~2026-10-22 (~9 weeks out). Action #5 targets a year-round core term, so it isn't competing with a more time-sensitive seasonal pick this cycle.

**Needs the owner:** apply Action #5 in wp-admin (and Actions #1-#4 if not already applied); confirm current `/artificii-iasi/` title/meta before overwriting it, per above; confirm `/artificii-galati/` scope and `/servicii`/`/despre-noi` URL expectations (carried forward, unresolved since 2026-07-30, now five cycles running).

---

## 2026-08-20 (Thursday) — no new numbered action; escalation

**Status:** No new title/meta proposal this cycle. Actions #1-#5 (all proposed, none applied) remain the complete backlog. This cycle's highest-value move is escalating that backlog, with fresh evidence it now has a measurable cost — not proposing a 6th unapplied item on top of five.

**Why no new action, per STEP 2:** every position-4-15 gap and local-intent candidate visible in `data/gsc.json` this pull is either (a) already covered by an open action (`/preturi/`, `/category/artificii-iasi-evenimente/`, `/artificii-nunta-pret-2026-romania/`, `/artificii-iasi/`), (b) previously rejected/deferred with unchanged reasoning ("petarde" — shop intent, still 0 clicks; `/artificii-galati/` — scope question; foreign-language queries), or (c) owner-gated by §7 before it can even be drafted: `/pirotehnician-autorizat-romania/` has a real CTR gap (62 impr, 1 click, 1.6% CTR, pos 6.1) but its entire topic is an authorization claim, which CLAUDE.md explicitly reserves for the owner — proposing wording there without sign-off would risk exactly the "false claim = legal problem" failure mode §1/§7 exist to prevent. No fabricated opportunity was manufactured to fill the "one move" slot this cycle.

**The escalation, with evidence (`ledger/KPIS.md` 2026-08-20 pull):**
- WordPress write access has been requested every cycle since 2026-07-30 — this is the **seventh** cycle running with zero of the five proposed fixes applied.
- In that time, site-wide CTR has fallen for **four consecutive cycles**, this cycle's drop (-2.14pp) the steepest yet; average position has now **worsened for two consecutive cycles**, the second regression (-0.52) nearly 3× the first (-0.18); clicks growth has stalled to +4.3% this cycle, the weakest of six pulls by a wide margin, even as impressions keep climbing (+44.6%).
- The clearest single thread: "artificii iasi" — the site's #1 query by clicks — is the exact term Action #5 (proposed 2026-08-17, unapplied) targets. In the three days since it was proposed, the regression it describes **got worse, not better**: homepage position on this query 4.4→4.7, blended query position 5.1→5.5, clicks on the query 17→15. Nothing on the live site has changed to explain this other than the cannibalization Action #5 already diagnosed — the fix sits ready and unapplied while the problem it targets compounds.
- This is not proof that applying the backlog would reverse the trend — no live-page change has been tested yet, so causation isn't established either way. But five reversible, evidence-based, zero-cost fixes sitting unapplied for up to seven weeks, on a site now showing four straight cycles of CTR decline and its highest-value query actively losing ground, is itself the highest-value thing to flag this cycle.

**Needs the owner (escalated, not new):** wire WordPress REST API write access (Application Password) so this routine can apply Actions #1-#5 itself, or apply all five manually in wp-admin this week — they are implementation-ready, unchanged, and listed in full above (dates 2026-07-30, 08-03, 08-06, 08-10, 08-17). Also unresolved, carried forward six-plus cycles: confirm `/artificii-galati/` scope (Galați is outside the Iași+județ area CLAUDE.md defines) and confirm `/despre-noi` — still HTTP 404 — is expected (note: `/servicii`, flagged alongside it since 2026-07-30, now returns HTTP 200 on its own, see KPIS.md).

---

### Cycle report — 2026-08-20

**What the numbers say:** Clicks +4.3% (120 vs 115) and impressions +44.6% (2,161 vs 1,494) over the trailing 28d vs. prior 28d — the weakest clicks growth of any of the six pulls to date, against continued fast impression growth. CTR fell for the fourth straight cycle, -2.14pp (7.70%→5.55%), the steepest single-cycle drop yet. Average position worsened for the second straight cycle, -0.52 (5.17→5.69), nearly three times the first regression (-0.18 on 2026-08-17). Romania remains ~85-90% of traffic, ruling out foreign-query dilution as the explanation for the third pull running. `daily_28d` confirms this is a real trend inside the 28-day window, not a comparison artifact.

**Recommended action:** no new numbered action — escalate the WordPress-access blocker (see above). Five implementation-ready, zero-cost fixes (Actions #1-#5) remain unapplied after up to seven weeks, and this cycle's data shows the cost of that delay concretely for the first time: the site's top query is actively regressing while its fix sits waiting.

**Action #1 scoring:** not due — verify date 2026-08-27 (7 days out). Status check in `ledger/KPIS.md`: 11 impr / 0 clicks / pos 6.2 — both metrics down from last pull, but at this page's very low volume this reads as noise, not signal.

**Action #2 scoring:** not due — verify date 2026-09-14 (25 days out). Status check: 83 impr / 0 clicks / pos 5.2 — fourth straight pull with zero clicks.

**Action #3 scoring:** not due — verify date 2026-09-21 (32 days out). Status check: 93 impr / 4 clicks / 4.30% CTR / pos 7.1 — roughly flat. Cannibalization check: "artificii iasi" on this page still at pos 19.5, unchanged.

**Action #4 scoring:** not due — verify date 2026-09-28 (39 days out). Status check: 625 impr / 16 clicks / pos 6.3 / CTR 2.56% — sixth straight cycle of impression growth, CTR still flat and low.

**Action #5 scoring:** not due — verify date 2026-09-14 (25 days out). Status check: the regression it targets worsened further — homepage position on "artificii iasi" 4.4→4.7, blended query position 5.1→5.5, query clicks 17→15 — while the fix remains unapplied.

**Rejected/deferred this cycle** (full detail in `ledger/opportunities.md`):
- `/pirotehnician-autorizat-romania/` CTR gap (62 impr, 1 click, 1.6% CTR, pos 6.1) — real gap, position in the fixable 4-15 band, but the page's entire topic is an authorization claim; owner-gated by §7, not drafted without sign-off.
- "artificii nunta" cannibalization across homepage / `/artificii-nunta-pret-2026-romania/` / `/artificii-nunta-iasi-ghid-locatii-tendinte-2026/` (carried forward, 7th cycle) — no fresh evidence this pull distinct from the "artificii iasi" issue already actioned.
- `/artificii-galati/` scope question (carried forward, 6th cycle) — unchanged, still awaiting owner confirmation. `/despre-noi` 404 also carried forward; `/servicii` (previously flagged alongside it) now resolved to HTTP 200 on its own.
- "petarde" 0% CTR (carried forward) — unchanged reasoning, shop/self-serve intent not call conversion.
- "magic fire" (two-word brand query) — 0 clicks on 29 impressions at position 1.4, a break from every prior pull's normal branded CTR (14-16%). Flagged as a watch item — small sample, no page-level fix available for a query-only signal, needs a second cycle or live-SERP visibility (blocked from this session) before acting.
- Mobile impression share held at ~80% for a second straight pull (down from 85-86% baseline) — now a two-cycle pattern, still not acted on, mobile remains the better-converting channel regardless.
- No seasonal-spike action taken: wedding season (May-Sep) has ~6 weeks left, and the Dec 31 prep window doesn't open until ~2026-10-22 (~9 weeks out). No pick was time-critical enough to override the escalation above this cycle.

**Needs the owner:** wire WordPress write access or apply Actions #1-#5 manually (escalated above — now the top-priority ask, with evidence the delay has a measurable cost); confirm `/artificii-galati/` scope; confirm `/despre-noi` 404 is expected (carried forward, unresolved since 2026-07-30, now six-plus cycles running).
