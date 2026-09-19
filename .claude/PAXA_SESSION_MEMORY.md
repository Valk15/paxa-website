# PAXA — Current State
*Single source of truth. Read first in every session. Last updated: 19 September 2026.*
*Every figure below was verified against Cloudflare, Search Console, Gumroad, GA4 and this repo.*

---

## OWNERSHIP

**Youness is the sole founder and owner.** There is no team. He holds every account —
Cloudflare, GitHub, Gumroad, Klaviyo, GA4, Search Console, TikTok, Instagram — and does
every role. Never assign a task to another person, never wait on anyone, never write
"pending X". Every task is his.

---

## GATE STATUS

**Gate 2: 1 of 5 organic sales.** Everything serves this number. No paid ads until it passes.

The one sale: 15 Sep, GBP 29, Gumroad referrer `paxapet.co.uk` — from the website, not
Gumroad Discover. The buyer never took the free preview; she bought cold at full price,
almost certainly from a blog post.

Gumroad shows 6 records but only 1 is a sale: 1 x GBP 29, 1 x GBP 4 tip on the free
preview, 3 real free-preview leads, 1 internal. Klaviyo has four real people in it.
Do not review email open rates until that number is far higher.

---

## TRAFFIC — Search Console, 28 days to 13 Sep

41 clicks, 3,790 impressions, 1.1% CTR, average position 25.7.
12 pages get impressions, 5 get clicks. **7 pages indexed, 12 not.**

| Page | Clicks | Impressions | Position |
|---|---|---|---|
| how-long-to-fix | 23 | 1,880 | 9.1 |
| the-40-minute-rule | 11 | 452 | 7.7 |
| how-to-stop | 3 | 1,017 | 72.3 |
| homepage | 3 | 37 | 6.4 |
| why-calming-treats | 2 | 426 | 11.3 |

The top ten queries by impressions have zero clicks between them — eight are "treatment"
variants at positions 61-76. Fixed 16 Sep; results not yet confirmed. Check Search Console
before assuming improvement.

---

## INFRASTRUCTURE

| Thing | Reality |
|---|---|
| Hosting | Cloudflare Pages, project `paxa-website.pages.dev` — NOT Netlify |
| Repo | github.com/Valk15/paxa-website, branch `main`, auto-deploys on push |
| DNS / WAF | Cloudflare zone paxapet.co.uk |
| GA4 | `G-E6VF2S1GQX` — consent-gated, fires only after `paxa_cookie_consent === 'accepted'`, so it always undercounts. Search Console is the reliable traffic number |
| Klaviyo | company `R3fCTy`, 5-email flow off the free preview |
| Local repo | `C:\Users\lenovo\OneDrive\Desktop\Ai Projects\paxa-website` — in OneDrive, which has repeatedly corrupted git. `core.autocrlf` is `false` |

**GA4 data before 16 Sep is not usable** — the tag was missing from 9 of 17 pages,
including the top entry page.

---

## CONTENT

14 blog posts live plus the blog index. One finished post
(`dog-separation-anxiety-cost-uk`) is staged on branch `publish/cost-uk`, deliberately
unpublished until the indexing backlog clears.

**Discontinued — never reference as live:** PAXA Calm Mat (GBP 34 lick mat) and Shopify.
Both removed from the deploy, pages 301'd.

---

## OPEN

1. Confirm in Search Console whether the 7 indexing requests landed, then publish `publish/cost-uk`
2. **Testimonials** — three named testimonials on the site must be real or removed. UK ASA treats fake reviews as a violation. Legal exposure, not a task
3. `.claude/` — 380 files still deployed publicly (WAF-blocked, not removed). Real fix: move the site into `/public` and set that as the Cloudflare build output directory
4. Dog-name field on the Klaviyo capture form
5. FAQPage + Product schema markup

---

## QUICK REFERENCE

Product: https://paxapet.gumroad.com/l/PAXA-Solo · Site: https://paxapet.co.uk
CTA: "Start the protocol — GBP 29 ->"
Voice: calm authority, science-backed, counter-intuitive hooks, UK English
Never: vet-reviewed, fur baby, revolutionary, guaranteed overnight results, urgency theatre
