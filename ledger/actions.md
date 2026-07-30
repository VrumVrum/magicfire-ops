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
