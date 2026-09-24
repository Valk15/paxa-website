## AUTO-LOAD ON EVERY SESSION
Read these files at the start of every session before doing anything else:
1. .claude/00_PAXA_MASTER_CONTEXT.md — full project context, strategy, gate status
2. .claude/PAXA_SESSION_MEMORY.md — latest changes, active tasks, known issues

## CURRENT STATUS (verified 24 Sep 2026)
- Gate 2: 1/5 organic sales (15 Sep, £29, referrer paxapet.co.uk)
- Hosting: Cloudflare Pages (paxa-website.pages.dev), auto-deploys from main on github.com/Valk15/paxa-website
- Only live product: PAXA Solo. Calm Mat and Shopify are discontinued — never reference as live
- Search Console (28 days to ~22 Sep): 49 clicks, 4.3K impressions, avg position 20.8. 16 pages indexed (was 7)
- Blog: 14 posts live; publish/cost-uk staged, unpublished — owner's decision
- Social: TikTok 2 videos (~475 views), Instagram 1 carousel — account access being recovered
- No reviews or testimonials exist. Never add review text, star ratings or aggregateRating schema until real reviews exist (UK ASA)
- Pixels: TikTok and Meta pixels were only on the removed calm-mat pages. Paid ads locked until Gate 2
- Local repo sits in OneDrive — if git errors on index.lock, delete .git/index.lock and retry

# PAXA — Claude Code Project Intelligence

## What This Project Is

PAXA is a premium UK dog behavioral wellness brand. Our core product is **PAXA Solo** — a £29 digital PDF workbook that solves dog separation anxiety using systematic desensitisation and counter-conditioning. We sell via Gumroad at paxapet.co.uk, hosted on Cloudflare Pages.

**This is not a hobby project. Every output must be production-ready, ROI-focused, and brand-correct.**

---

## Project Files

| File | Purpose |
|------|---------|
| `index.html` | Main landing page — live at paxapet.co.uk |
| `.claude/agents/` | 6 PAXA-specific agents |
| `.claude/skills/` | Brand + marketing skills |
| `.claude/paxa-brand-identity.md` | Full brand system — READ THIS FIRST |
| `.claude/paxa-operator-guide.md` | How to think, decide, prioritise |
| `.claude/paxa-output-formats.md` | Templates for every output type |

---

## Before Every Task — Load These

1. Read `.claude/paxa-brand-identity.md` for voice, colours, tone rules
2. Read `.claude/paxa-operator-guide.md` for business context and decision rules
3. Read `.claude/paxa-output-formats.md` for the correct output format

---

## Core Business Facts

- **Product:** PAXA Solo — 30-day PDF workbook — £29 one-time
- **Buy link:** https://paxapet.gumroad.com/l/PAXA-Solo
- **Free lead magnet:** https://paxapet.gumroad.com/l/PAXA_Free_2Days (Days 1 & 2 free)
- **Website:** https://paxapet.co.uk
- **Email:** hello@paxapet.co.uk
- **Market:** UK only (Australia is Phase 2 — not now)
- **ICP:** UK dog owners, 28–55, Labrador/Cockapoo/Spaniel breeds, post-pandemic velcro dogs
- **Budget:** $1,000 total — currently pre-paid-ads phase
- **Gate:** 5 organic sales before any Meta ad spend

---

## Ownership

**Youness is the sole founder and owner.** He holds every account and does every role:
brand, marketing, content, ads, code, SEO, GitHub, Cloudflare, Gumroad, Klaviyo, social.
There is no team. Never assign a task to anyone else or wait on anyone else.

---

## Current Phase — Week 1-3 (Foundation)

- [x] Landing page live
- [x] Klaviyo email flow (5 emails)
- [x] Free 2-day lead magnet PDF
- [x] GA4 tracking installed
- [x] Popup with email capture
- [ ] 5 real beta tester testimonials
- [ ] Organic content (TikTok + Instagram)
- [ ] Reddit + Facebook community seeding
- [ ] First 5 organic sales

---

## Non-Negotiables

- Never write "fur baby", "pawesome", "puppy parent", or any cutesy pet portmanteau
- Never use exclamation marks in product copy
- Never promise overnight results
- Never make the dog the butt of a joke
- Always write from calm authority — science-backed, not hype-based
- UK English spelling always (behaviour not behavior, colour not color) — except in code
