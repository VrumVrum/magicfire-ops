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
