# Opportunities — scored, deduped

Every opportunity: evidence (real GSC data or a live-page fact) · expected local calls · effort · score · status.
Rejected ones stay here with the reason so they are not re-proposed.

## 2026-07-30 batch (source: data/gsc.json 28d pull, data/site.json)

| Opportunity | Evidence | Expected local calls | Effort | Status |
|---|---|---|---|---|
| Title/meta rewrite, `/artificii-reci-fantani-scantei-t1/` for "artificii reci" | pos 7.8-8.1, 18-21 impr/28d, CTR 6.9-9.5%, existing page, wedding/indoor-event relevant | Low-modest (+1-3 clicks/28d est.) | Very low (2 fields) | **ACTIONED** — see actions.md #1, verify 2026-08-27 |
| Title/meta rewrite, homepage, for "petarde" | pos 5.9, 37 impr/28d, **0 clicks/0% CTR** — biggest raw CTR gap in the dataset; confirmed real product line exists on-site (product-tag pages found via search index) | Uncertain — likely shop/self-serve purchase intent, not call/WhatsApp/form conversion per CLAUDE.md mission | Low-modest (homepage copy is higher-blast-radius than a low-traffic subpage) | **DEFERRED** — real gap, but doesn't clearly serve "qualified local calls" mission; revisit if a future pull shows this query converting on a dedicated page instead of the homepage |
| Consolidate/fix "artificii nunta" targeting across homepage (pos 9.6, 10 impr) vs `/artificii-nunta-pret-2026-romania/` (ranks #1 for the narrower "pret" query) vs `/artificii-nunta-iasi-ghid-locatii-tendinte-2026/` (pos 2.5 but only 2 impr total — looks unindexed/thin-signal) | Core wedding-season money term ranking worse on the homepage than a purpose-built page ranks for a narrower variant; possible cannibalization or an under-linked new page | Potentially the highest of this batch — this is the actual "artificii nunta" query | Medium-high — needs internal-linking review across 3 URLs, not a 2-field edit | **DEFERRED** — too big for one reversible bet this cycle; revisit next cycle with fresh internal-linking read |
| `/artificii-galati/` scope check | 2nd-biggest page by clicks (16/182, pos 5.8, 28d) but targets Galați, outside the Iași+județ scope defined in CLAUDE.md | N/A — scope question, not an SEO fix | N/A | **FLAGGED FOR OWNER** — confirm if Galați is in scope; not touched |
| `/servicii` and `/despre-noi` 404s (`data/site.json`) | No GSC impressions/clicks for either URL, ever, in this pull — no evidence they were live/linked pages | N/A | N/A | **FLAGGED FOR OWNER** — likely a stale health-check assumption, not a real regression; not actioned without evidence a real page broke |
| "fireworks" (English query, 45 impr, 0 clicks, pos 6.0, homepage) and similar EN/foreign-language queries | High impressions but international searchers — CLAUDE.md: "a visitor from another country is worth ~zero here" | None | N/A | **REJECTED** — out of mission by definition, will not be re-proposed |

## 2026-08-03 batch (source: data/gsc.json 28d pull, generated 2026-08-02; data/site.json)

| Opportunity | Evidence | Expected local calls | Effort | Status |
|---|---|---|---|---|
| Title/meta rewrite, `/preturi/` (pricing page) | pos 5.7, 120 impr/28d, **1 click (0.83% CTR)** — worst CTR-to-impression ratio of any page this pull, high buyer-intent page type | High relative to effort (+4-6 clicks/28d est. if snippet is the cause) | Very low (2 fields) | **ACTIONED** — see actions.md #2, verify 2026-09-14 |
| `/category/artificii-iasi-evenimente/` CTR gap | pos 7.0, 97 impr/28d, 3 clicks, 3.1% CTR | Moderate | Higher — category archive template/settings, not a single page's title/meta | **DEFERRED** — real gap, filed for a future cycle once `/preturi/` is scored |
| "artificii nunta" cannibalization (carried forward from 2026-07-30) | Still ranks 9.1 on homepage (10 impr) vs. purpose-built pages ranking narrower variants better; no new evidence this pull | Potentially highest in the dataset | Medium-high — internal-linking review across 3 URLs | **DEFERRED, no new evidence** — carrying forward unscored |
| `/artificii-galati/`, `/servicii`, `/despre-noi` (carried forward from 2026-07-30) | Unchanged since last pull | N/A | N/A | **STILL FLAGGED FOR OWNER** — no new evidence, not re-actioned |
