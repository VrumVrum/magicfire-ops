# magicfire.ro — Operating System (read this first, every session)

**This repo is the entire world for magicfire.ro. It has no connection to any other project. Do not reference, fetch, or reason about other sites — if something is not in this repo or in the live magicfire.ro site, it does not exist for you.**

## The business (this drives every decision)
**MagicFire — artificii și efecte pirotehnice, Iași, România.** Local service business. A visitor is worth something only if they **call, message on WhatsApp, or send the contact form** — there is no e-commerce checkout, no SaaS subscription, no PDF to sell.

**Demand is violently seasonal.** Fireworks demand concentrates on: **31 December** (the single biggest spike, buildup from ~1 December), **weddings May–September**, plus baptisms/corporate events year-round. SEO work must land **6–10 weeks BEFORE** a spike to be indexed and ranking in time. Optimizing for December in December is too late.

## The mission
Get more **qualified local calls**. In order:
**Local visibility (Iași + județ) → site visit → phone call / WhatsApp / form → booking.**

Not: traffic for traffic's sake. A visitor from another country is worth ~zero here.

## What actually moves the needle for a local service site
1. **Local pack / Google Business Profile** — the map results above the organic list. For "artificii Iasi"-type queries this is where the clicks are.
2. **Local intent pages** — city/service combinations that people actually search (artificii nuntă, artificii botez, efecte pirotehnice, scenă/fum/confetti, focuri de artificii Iași).
3. **Contact friction** — the phone number must be visible, tappable (`tel:`), and above the fold on mobile. Most local searches are on a phone, mid-decision.
4. **Trust signals** — real photos/video of real events, reviews, authorization/permits (pyrotechnics is regulated — being visibly legitimate converts).
5. **Seasonal timing** — publish and fix ahead of the spike, not during it.

## Hard rules (non-negotiable)
- **§1 No fabricated data.** No invented review counts, no fake client names, no made-up statistics, no claimed authorizations we do not hold. Pyrotechnics is a regulated field — a false claim is a legal problem, not just an SEO one.
- **§2 This is a LIVE site with real customers.** Every write is: snapshot first → change → verify on the **rendered live page** → roll back on any doubt. HTTP 200 is not verification.
- **§3 Never break the phone number, the contact form, or the Google Business listing.** These are the revenue. A ranking gain that breaks a call button is a loss.
- **§4 Romanian content stays Romanian.** The audience is local. Do not "internationalize" pages.
- **§5 One change at a time on the live site.** No mass edits. Small, reversible, verified.
- **§6 Zero budget** unless the owner explicitly approves a spend.
- **§7 Owner-gated:** anything touching money, legal/authorization claims, the Google Business Profile itself, or the site's reputation.

## How this system runs (the three layers)
1. **Eyes** — GitHub Actions in this repo (free, no PC needed): pulls real Google Search Console data + checks the live site, commits to `data/`.
2. **Brain** — a scheduled cloud routine that reads `data/`, decides ONE highest-value action, and writes it to `ledger/`.
3. **Hands** — changes reach WordPress via the REST API (Application Password) with snapshot + rollback. Until that is wired, the brain produces a prioritized action list and the owner/desktop applies it.

## Ledgers (the memory — always read before acting)
- `ledger/KPIS.md` — the real numbers (GSC clicks/impressions/positions, calls if measurable). Never write a number here you did not measure.
- `ledger/actions.md` — what was decided, why, what changed, verify date, outcome.
- `ledger/opportunities.md` — scored opportunities, deduped. Rejected ones stay with the reason.
- `data/` — machine-written: `gsc.json` (Search Console), `site.json` (live-site health).

## The discipline (learned the hard way on another project — do not repeat those mistakes)
- **A routine that is "configured" but never fires does not exist.** Prove it ran by its output.
- **Verify like a human**, not like a monitor: open the page, check it renders, check the phone link works on a 390px screen.
- **Score every change.** Set a verify date, then actually go back and score it Win/Loss with the measured delta.
- **One bet per cycle.** Publishing volume does not work on a small local site — relevance and local signals do.
- **Say the honest number.** If something did not move, say it did not move.
