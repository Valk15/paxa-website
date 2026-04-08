# PAXA — Master Context File
**Paste this at the start of every new Claude.ai conversation.**
**This file restores full project context instantly.**
*Last updated: April 2026 — Gate 2 in progress (0/5 organic sales)*

---

## WHO YOU ARE TALKING TO

**Youness** — Co-founder, Brand & Marketing Lead, PAXA.
- Moroccan, 28 years old
- Responsible for: strategy, content scripts, ad creative, brand voice, Klaviyo email
- Uses Claude.ai for content, strategy, and planning sessions
- Claude Code installed on Youness's own machine (Windows, VS Code)

**The team:**
| Person | Role |
|--------|------|
| Youness | Co-founder — Brand & Marketing Lead |
| Ayoub | Co-founder — Technical Lead (GitHub, Cloudflare, Telegram bot) |
| Hamza | Co-founder — Operations (posting, Reddit, Facebook, customer support) |

---

## WHAT PAXA IS

Premium UK digital pet wellness brand. Solving dog separation anxiety with behavioral science.

**Core product:** PAXA Solo — 42-page interactive PDF workbook. £29 one-time. Instant download.
**Product URL:** https://paxapet.gumroad.com/l/PAXA-Solo
**Website:** https://paxapet.co.uk
**Email:** hello@paxapet.co.uk

**The science foundation:**
- Systematic desensitisation
- Counter-conditioning
- Functional relaxation
- Threshold management

**4 phases of the protocol:**
- Days 1–7: Foundation (calm baseline, independence tools, threshold identification)
- Days 8–14: Desensitisation (defuse departure triggers — keys, coat, doorknob)
- Days 15–21: Incremental Distance (first real absences, Pavlovian food toy safety cue)
- Days 22–30: Real-World Resilience (40-min cortisol peak, 90-min proof, 4-hour graduation)

**Key science facts — use in all copy:**
- 73% of UK dogs experience separation anxiety
- Cortisol peaks at 30–40 minutes after departure (the "40-minute window")
- 30 minutes aerobic exercise reduces cortisol by up to 30%
- Counter-conditioning rewires the amygdala's threat response permanently

---

## BRAND POSITIONING

**One sentence:** Science-backed premium protocol that treats the neurological cause of separation anxiety — not the symptoms.

**Against every competitor:** Calming treats, anxiety wraps, and YouTube videos mask symptoms. PAXA rewires behaviour.

**Taglines:**
- Primary: "Peace for your pet. Science for you."
- Product: "30 days. One protocol. A different dog."
- Challenger: "Every other brand treats the symptoms. We treat the cause."
- Minimalist: "Calm, by design."

**Target customer:** UK dog owner, 28–55, has an anxious/velcro dog, tried calming treats and YouTube that didn't work, educated enough to respond to science framing, willing to pay £29 for something that actually works.

---

## BRAND VOICE RULES — APPLY IN EVERY SESSION

**Always:**
- UK English — behaviour, desensitisation, recognise, colour, licence
- Science-backed framing — cortisol, amygdala, neuroplasticity, threshold
- Counter-intuitive hooks — "The worst thing you can do when you leave your dog..."
- Calm authority — no hype, no urgency theatre
- Empathetic but precise — one sentence acknowledging the feeling, then move forward
- CTA text: "Start the protocol — £29 →"
- CTA URL: paxapet.gumroad.com/l/PAXA-Solo

**Never:**
- "Fur baby", "pawesome", "puppy parent", "paw-fect", any cutesy portmanteau
- Exclamation marks in product copy
- "Vet-reviewed" (not verified — use "science-backed" only)
- Countdown timers, "only X left", "act now", urgency theatre
- "Revolutionary", "guaranteed overnight results"
- AU market content (Phase 2 only — not yet)
- Hashtag spam (max 5 relevant hashtags)

---

## WHAT IS LIVE RIGHT NOW

### Website — paxapet.co.uk ✅ LIVE
- Hosted on Cloudflare (migrated from Netlify)
- GitHub repo: bayoubnassibi-prog/paxa-website
- Full landing page: hero, 4 protocol phases, what's inside, science section, testimonials, FAQ
- Free 2-day preview section + exit intent popup with email capture
- Cookie consent banner
- Legal pages: Privacy Policy, Terms & Conditions, Cookie Policy, Refund Policy
- "Vet-reviewed" claim removed — now "Science-Backed Protocol" ✅
- sitemap.xml created and submitted to Google Search Console

### Blog — paxapet.co.uk/blog ✅ 3 POSTS LIVE
| # | Title | URL | Status |
|---|-------|-----|--------|
| 1 | How to Stop Dog Separation Anxiety: The Complete Science-Backed Guide | /blog/how-to-stop-dog-separation-anxiety/ | ✅ Live |
| 2 | Why Calming Treats Don't Fix Dog Separation Anxiety | /blog/why-calming-treats-dont-fix-separation-anxiety/ | ✅ Live |
| 3 | The 40-Minute Rule: Why Your Dog's Anxiety Peaks When You Leave | /blog/the-40-minute-rule-dog-separation-anxiety/ | ✅ Live (pending Ayoub push) |

Next blog topics (priority order):
4. "Separation anxiety vs boredom: how to tell the difference"
5. "Dog desensitisation: a step-by-step guide for UK owners"

### Product — PAXA Solo PDF ✅ LIVE
- 42-page interactive PDF, full PAXA branding
- Delivered via Gumroad instantly on purchase
- Graduation certificate on final page

### Email System — Klaviyo ✅ LIVE + DNS FIXED
- DNS records added to Cloudflare — 4 NS records for mail.paxapet.co.uk ✅
- 5-email nurture flow connected to free 2-day preview lead magnet

**Flow structure:**
| Day | Email | Content |
|-----|-------|---------|
| Day 0 | Welcome + Day 1 | Delivers Day 1 PDF |
| Day 1 | Day 2 delivery | Delivers Day 2 PDF |
| Day 3 | Science insight | Counter-intuitive science fact, no sell |
| Day 5 | Soft sell | What Days 3–30 look like |
| Day 7 | Hard close | Objection handling, guarantee, final CTA |

**Pending:** Add dog's name field to Klaviyo email capture — Ayoub, 30 min

### Social Media
- TikTok: ✅ 2 videos live, ~475 views total, avg watch time 4–5s (hook retention problem)
- Instagram: ✅ Carousel #1 live — dark editorial 8-slide brand introduction post
- Reddit: ✅ Hamza started seeding today (r/dogs, r/dogadvice, r/puppy101)
- Facebook groups: Hamza starting this week

### Technical Infrastructure
- GitHub: bayoubnassibi-prog/paxa-website
- Hosting: Cloudflare (migrated from Netlify)
- Claude Code: installed on Youness's machine (Windows, VS Code, v2.1.42) ✅ authenticated
- Telegram bot: built — Youness sends tasks → executes in Claude Code → output returned
- 6-agent PAXA system in .claude/agents/

---

## THE CLAUDE CODE AGENT SYSTEM

6 agents in `.claude/agents/`:

| Agent | Purpose |
|-------|---------|
| paxa-supervisor | Master orchestrator — routes all tasks, runs weekly workflow |
| paxa-seo | Keywords, meta tags, blog topics, site audit, GEO |
| paxa-content | Instagram, TikTok scripts, email copy, blog posts |
| paxa-ads | Meta ad creative, headlines, CTAs, 3 variations per brief |
| paxa-analytics | Weekly reports, sales data, gate status tracking |
| paxa-competitor | UK market intelligence, competitor pricing and positioning |

Brand context skill: `.claude/skills/paxa-brand/SKILL.md` — auto-loaded by all agents.

**Known issue:** Stop hook error on Windows (`'_R' is not recognized`) — cosmetic only, does not affect output. To be fixed by removing bash hook from settings.

---

## CURRENT STRATEGY & PHASE

**Budget: $1,000 total**
| Allocation | Amount | Status |
|-----------|--------|--------|
| Meta ads (30-day test) | $450 | HELD — waiting for Gate 2 |
| Tools & infrastructure | $150 | In use |
| Content & creative | $150 | In use |
| Domain + email | $50 | Spent |
| Reserve | $150 | HELD |

**Market: UK ONLY (Phase 1)**

**Current Phase: ORGANIC**
The only metric that matters: **5 organic sales.**

**Decision Gates:**
- ✅ Gate 1: Product built, site live, social accounts warmed up
- → **Gate 2 (CURRENT):** 5 organic sales → then paid ads. Count: 0/5
- Gate 3 (future): ROAS ≥ 2 after $300 ad spend → scale
- Gate 4 (future): Week 12 review → AU + physical product research

**Active channels:**
- TikTok + Instagram (Hamza posts, Youness writes scripts — 3x/week)
- Reddit: r/dogs, r/dogadvice, r/puppy101 (Hamza — genuine value, no spam)
- UK Facebook dog groups (Hamza)
- Email: Klaviyo 5-email flow via free 2-day preview lead magnet
- Blog: 3 posts live, distributing via Facebook groups + Pinterest

---

## WHAT STILL NEEDS DOING

### Urgent
1. **Testimonials** — Sarah M. / James & Rachel T. / Anna K. must be real or removed. UK ASA risk.
2. **Add dog name field** to Klaviyo email capture — Ayoub, 30 min
3. **Fix stop hook error** in Claude Code Windows — remove `_R` bash hook from .claude/settings
4. **Post Instagram carousel #1** — 8 slides built, copy ready, Hamza to post today
5. **Hamza posts Facebook group copy** for blog post #3 — file in repo: blog-post-3-distribution.txt
6. **Hamza posts Pinterest pins** for blog post #3 — same file

### This Month
7. **First 5 organic sales** — everything else is secondary
8. **Blog post #4** — "Separation anxiety vs boredom: how to tell the difference"
9. **Schema markup** — FAQPage + Product schema — Ayoub
10. **Email flow review** — after first 50 subscribers, check open rates
11. **TikTok hook fix** — avg watch time 4–5s means hook is failing, rewrite needed

### Completed ✅
- sitemap.xml created and submitted
- "Vet-reviewed" claim removed from site
- Klaviyo DNS fixed (4 NS records added to Cloudflare)
- Claude Code authenticated on Youness's machine
- 3 blog posts live
- Instagram carousel #1 live (dark editorial, 8 slides)
- TikTok: 2 videos live (~475 views)
- Reddit seeding started (Hamza)
- Blog post #3 distribution copy created

---

## TECHNICAL STACK

| Tool | Purpose | Owner |
|------|---------|-------|
| paxapet.co.uk | Landing page + blog | Ayoub (Cloudflare) |
| GitHub (paxa-website) | Codebase + agents | Ayoub |
| Gumroad | Product delivery + payments | Youness |
| Klaviyo | Email marketing, 5-email flow | Youness |
| Telegram bot | Youness → Claude Code bridge | Ayoub built |
| Claude Code v2.1.42 | 6-agent PAXA system | Youness (Windows) |
| Claude.ai | Strategy, content, planning | Youness |
| Canva | Design (Education plan — no AI gen) | Youness |
| TikTok / Instagram | Organic content | Hamza posts |

---

## PHASE 2 VISION (post-revenue, UK profitable)

- **AU launch:** Same product, $59 AUD, adapted copy
- **PAXA Calm:** Physical pheromone diffuser (white label), companion to PAXA Solo
- **Bundle:** Protocol + diffuser, £49–59
- **B2B channel:** Protocol licences to UK vet clinics and dog trainers
- **Credential upgrade:** Pay UK CCAB behaviourist to review protocol

---

*Last updated: April 2026 — Gate 2 in progress (0/5 organic sales)*
