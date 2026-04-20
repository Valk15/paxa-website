## AUTO-LOAD ON EVERY SESSION
Read these files at the start of every session before doing anything else:
1. .claude/00_PAXA_MASTER_CONTEXT.md — full project context, team, strategy, gate status
2. .claude/PAXA_SESSION_MEMORY.md — latest changes, active tasks, known issues

## CURRENT STATUS (April 2026)
- Gate 2: 0/5 organic sales
- Hosting: Cloudflare
- Blog: 3 posts live
- TikTok: 2 videos live, ~475 views
- Instagram: carousel #1 live
- Klaviyo DNS: fixed
- Claude Code: Youness machine, Windows, v2.1.42, authenticated
- TikTok Pixel: D7J2053C77U8847ELUI0 — live on calm-mat.html, calm-mat-landing.html, Shopify
- Meta Pixel: 977092621560109 — live on calm-mat.html (advertorial only), Shopify

## Pixel Verification Checklist
When any tracking change is made to HTML files, ALWAYS verify:
1. Visit paxapet.co.uk/calm-mat in browser → accept cookies → check TikTok Pixel Helper shows ViewContent on pixel D7J2053C77U8847ELUI0
2. Check Meta Pixel Helper shows ViewContent on pixel 977092621560109
3. Click a CTA button → both helpers should show AddToCart
4. Visit Shopify store product page → both pixels should fire ViewContent
5. In TikTok Events Manager → Data Sources → confirm "Browser events received" step is green
6. In Meta Events Manager → confirm events show in Test Events tab
7. If Pixel Helper shows "No pixel found" — check if cookies have been accepted (both pixels are consent-gated)
8. If pixel fires on site but not Shopify → check TikTok for Shopify / Meta for Shopify app is connected with correct pixel ID

# PAXA — Claude Code Project Intelligence

## What This Project Is

PAXA is a premium UK dog behavioral wellness brand. Our core product is **PAXA Solo** — a £29 digital PDF workbook that solves dog separation anxiety using systematic desensitisation and counter-conditioning. We sell via Gumroad at paxapet.co.uk, hosted on Netlify.

**This is not a hobby project. Every output must be production-ready, ROI-focused, and brand-correct.**

---

## Project Files

| File | Purpose |
|------|---------|
| `index.html` | Main landing page — live at paxapet.co.uk |
| `.claude/agents/` | 6 PAXA-specific agents |
| `.claude/skills/` | Brand + marketing skills |
| `paxa-brand-identity.md` | Full brand system — READ THIS FIRST |
| `paxa-operator-guide.md` | How to think, decide, prioritise |
| `paxa-output-formats.md` | Templates for every output type |

---

## Before Every Task — Load These

1. Read `paxa-brand-identity.md` for voice, colours, tone rules
2. Read `paxa-operator-guide.md` for business context and decision rules
3. Read `paxa-output-formats.md` for the correct output format

---

## Core Business Facts

- **Product:** PAXA Solo — 30-day PDF workbook — £29 one-time
- **Buy link:** https://paxapet.gumroad.com/l/PAXA-Solo
- **Free lead magnet:** https://paxapet.gumroad.com/l/PAXA_Free_2Days (Days 1 & 2 free)
- **Website:** https://paxapet.co.uk
- **Email:** hello@paxapet.co.uk
- **Market:** UK Phase 1 — Australia Phase 2
- **ICP:** UK dog owners, 28–55, Labrador/Cockapoo/Spaniel breeds, post-pandemic velcro dogs
- **Budget:** $1,000 total — currently pre-paid-ads phase
- **Gate:** 5 organic sales before any Meta ad spend

---

## Team Roles

| Person | Role |
|--------|------|
| Youness | Brand, marketing, content, ads — also all code, SEO, GitHub, Claude Code agents, site updates |
| Ayoub | Klaviyo email flows only |
| Hamza | Community management, customer support, social media posting |
| Youssef | Social media content creation — TikTok + Instagram, especially for physical product |

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
