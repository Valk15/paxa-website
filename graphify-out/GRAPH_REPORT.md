# Graph Report - .  (2026-04-13)

## Corpus Check
- Corpus is ~17,437 words - fits in a single context window. You may not need a graph.

## Summary
- 71 nodes · 100 edges · 11 communities detected
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 11 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Telegram Bot System|Telegram Bot System]]
- [[_COMMUNITY_Agent Infrastructure|Agent Infrastructure]]
- [[_COMMUNITY_Brand Identity|Brand Identity]]
- [[_COMMUNITY_Lead Magnet Funnel|Lead Magnet Funnel]]
- [[_COMMUNITY_Science & Content|Science & Content]]
- [[_COMMUNITY_Content Distribution|Content Distribution]]
- [[_COMMUNITY_Product & Positioning|Product & Positioning]]
- [[_COMMUNITY_Social Media Content|Social Media Content]]
- [[_COMMUNITY_30-Day Protocol Phases|30-Day Protocol Phases]]
- [[_COMMUNITY_SEO Configuration|SEO Configuration]]
- [[_COMMUNITY_Downloads Placeholder|Downloads Placeholder]]

## God Nodes (most connected - your core abstractions)
1. `PAXA Solo Product` - 10 edges
2. `Blog Post 1: Complete Science-Backed Guide to Dog Separation Anxiety` - 10 edges
3. `sendMessage()` - 7 edges
4. `PAXA Brand` - 7 edges
5. `PAXA Agent System (6 Agents)` - 7 edges
6. `30-Day Protocol (4 Phases)` - 6 edges
7. `TikTok Script: Boring Goodbyes` - 6 edges
8. `TikTok Script: Leaving Your Dog Home Alone` - 6 edges
9. `requestApproval()` - 5 edges
10. `handleNaturalLanguage()` - 5 edges

## Surprising Connections (you probably didn't know these)
- `PAXA Free Day 1 Preview PDF` --semantically_similar_to--> `Phase 1: Foundation (Days 1-7)`  [INFERRED] [semantically similar]
  downloads/PAXA_Free_Day1_Preview.pdf → content/blog-post-1.md
- `Day 1: Find Your Dog's Threshold` --semantically_similar_to--> `Threshold Management`  [INFERRED] [semantically similar]
  downloads/PAXA_Free_Day1_Preview.pdf → content/blog-post-1.md
- `PAXA Favicon (P on Black Background)` --references--> `PAXA Brand`  [INFERRED]
  favicon.png → CLAUDE.md
- `30-Day Protocol (4 Phases)` --semantically_similar_to--> `PAXA Solo Product`  [INFERRED] [semantically similar]
  content/blog-post-1.md → CLAUDE.md
- `Calm Dog Resting on Sofa (Blog Image)` --references--> `Blog Post 1: Complete Science-Backed Guide to Dog Separation Anxiety`  [INFERRED]
  images/calm-dog-resting.jpg → content/blog-post-1.md

## Hyperedges (group relationships)
- **PAXA Core Science Framework** — claudemd_systematic_desensitisation, claudemd_counter_conditioning, blogpost1_threshold_management, blogpost1_cortisol_peak, blogpost1_amygdala, blogpost1_neuroplasticity [INFERRED 0.90]
- **PAXA Content Distribution Pipeline** — blogpost1_science_backed_guide, blogpost3_distribution, tiktok_boring_goodbyes, tiktok_leaving_home_alone, blogpost3_facebook_groups, blogpost3_pinterest_pins [INFERRED 0.85]
- **PAXA Lead Magnet to Sale Funnel** — claudemd_free_lead_magnet, pdf_day1_preview, pdf_day2_preview, pdf_day3_upsell, claudemd_paxa_solo [EXTRACTED 0.95]

## Communities

### Community 0 - "Telegram Bot System"
Cohesion: 0.37
Nodes (11): answerCallback(), apiRequest(), approvalKeyboard(), editMessage(), handleCallbackQuery(), handleCommand(), handleMessage(), handleNaturalLanguage() (+3 more)

### Community 1 - "Agent Infrastructure"
Cohesion: 0.18
Nodes (11): Ayoub (Email Flows), Hamza (Community Management), Klaviyo Email Platform, paxa-ads Agent, paxa-analytics Agent, paxa-competitor Agent, paxa-content Agent, paxa-seo Agent (+3 more)

### Community 2 - "Brand Identity"
Cohesion: 0.22
Nodes (9): Brand Tagline: Peace for your pet. Science for you., Cloudflare Hosting, Gate 2 Milestone (5 Organic Sales), PAXA Brand, UK Market Phase 1, Youness (Founder), PAXA Favicon (P on Black Background), PAXA Favicon SVG (Georgia Serif P) (+1 more)

### Community 3 - "Lead Magnet Funnel"
Cohesion: 0.25
Nodes (9): Threshold Management, PAXA Free 2-Day Lead Magnet, Day 1: Find Your Dog's Threshold, PAXA Free Day 1 Preview PDF, Day 2: Cut the Velcro in Half, PAXA Free Day 2 Preview PDF, Day 3 Upsell CTA (Functional Relaxation), Functional Relaxation (Day 3 Cornerstone) (+1 more)

### Community 4 - "Science & Content"
Cohesion: 0.4
Nodes (6): Amygdala Threat Detection, 40-Minute Cortisol Peak, Blog Post 1: Complete Science-Backed Guide to Dog Separation Anxiety, Calm Dog Resting on Sofa (Blog Image), Counter-Conditioning, Cortisol Stress Hormone

### Community 5 - "Content Distribution"
Cohesion: 0.4
Nodes (5): Flooding (Harmful Exposure Method), Learned Helplessness, Blog Post 3 Distribution Copy (40-Minute Rule), Facebook Group Distribution (3 Versions), Pinterest Pin Distribution (2 Pins)

### Community 6 - "Product & Positioning"
Cohesion: 0.4
Nodes (5): Neuroplasticity / Extinction, Gumroad Sales Platform, ICP: UK Dog Owners 28-55, PAXA Solo Product, Systematic Desensitisation

### Community 7 - "Social Media Content"
Cohesion: 0.7
Nodes (5): Dog Separation Anxiety, Youssef (Social Media Content), TikTok Script: Boring Goodbyes, Pre-Departure Cue Concept, TikTok Script: Leaving Your Dog Home Alone

### Community 8 - "30-Day Protocol Phases"
Cohesion: 0.4
Nodes (5): 30-Day Protocol (4 Phases), Phase 1: Foundation (Days 1-7), Phase 2: Desensitisation (Days 8-14), Phase 3: Incremental Distance (Days 15-21), Phase 4: Real-World Resilience (Days 22-30)

### Community 9 - "SEO Configuration"
Cohesion: 1.0
Nodes (2): Sitemap XML, robots.txt Configuration

### Community 10 - "Downloads Placeholder"
Cohesion: 1.0
Nodes (1): Downloads Placeholder

## Knowledge Gaps
- **28 isolated node(s):** `Gumroad Sales Platform`, `Cloudflare Hosting`, `Klaviyo Email Platform`, `Youness (Founder)`, `Hamza (Community Management)` (+23 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `SEO Configuration`** (2 nodes): `Sitemap XML`, `robots.txt Configuration`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Downloads Placeholder`** (1 nodes): `Downloads Placeholder`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `PAXA Solo Product` connect `Product & Positioning` to `Brand Identity`, `Lead Magnet Funnel`, `Science & Content`, `Social Media Content`, `30-Day Protocol Phases`?**
  _High betweenness centrality (0.207) - this node is a cross-community bridge._
- **Why does `PAXA Brand` connect `Brand Identity` to `Product & Positioning`?**
  _High betweenness centrality (0.127) - this node is a cross-community bridge._
- **Why does `Blog Post 1: Complete Science-Backed Guide to Dog Separation Anxiety` connect `Science & Content` to `Lead Magnet Funnel`, `Content Distribution`, `Product & Positioning`, `Social Media Content`, `30-Day Protocol Phases`?**
  _High betweenness centrality (0.115) - this node is a cross-community bridge._
- **What connects `Gumroad Sales Platform`, `Cloudflare Hosting`, `Klaviyo Email Platform` to the rest of the system?**
  _28 weakly-connected nodes found - possible documentation gaps or missing edges._