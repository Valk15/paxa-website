# PAXA Shopify Store Redesign — Claude Code Prompt

Paste this entire prompt into Claude Code in your terminal from the `paxa-website` folder.

---

## PROMPT TO RUN IN CLAUDE CODE

```
You are working on the PAXA Shopify store (paxa-7714.myshopify.com). 
Store Theme ID: 197891162449 (Dawn v15.4.1, currently LIVE).

Your task is to fully redesign this store to look premium and on-brand.
Read .claude/paxa-brand-identity.md first before doing anything.

BRAND PALETTE:
- Background: #E8E0D5 (warm bone — matches logo background, use EVERYWHERE)
- Ink/Text: #0A0A0A
- Sage (CTA/accent): #4A6741
- Bone (card bg): #EDE5D8
- Stone (muted): #B8A898
- Footer bg: #0A0A0A

REFERENCE STORES FOR DESIGN INSPIRATION (scrape these for patterns):
1. https://lickimat.us — premium product layout, clean hero
2. https://flufftrough.com — premium pet product, professional grid
3. https://farmtopettreats.com — clean, nature-inspired, trust signals
4. https://mywoof.com — UK pet brand, lifestyle imagery

---

## TASK 1 — Upload PAXA Logo to Shopify

1. Read the logo file: images/calm-dog-resting.jpg (or find any PAXA logo in images/ folder)
2. If there's a logo PNG/SVG in the images/ folder, upload it to the theme as an asset
3. Use the Shopify API to set it as the store logo in theme settings:
   - Update config/settings_data.json: set `logo` to the uploaded asset URL
   - Set `logo_width` to 120

---

## TASK 2 — Create paxa-custom.css Asset

Use the Shopify Admin REST API to PUT a new asset `assets/paxa-custom.css` with this content:

```css
/* ============================================
   PAXA CALM MAT — PREMIUM BRAND CSS v1.0
   Brand: paxapet.co.uk
   ============================================ */

/* === GLOBAL BACKGROUND === */
body,
.shopify-section,
main { background-color: #E8E0D5; }

.color-scheme-1,
.color-scheme-1 .shopify-section {
  --color-background: 232 224 213 !important;
  background-color: #E8E0D5 !important;
}

/* === ANNOUNCEMENT BAR === */
.announcement-bar {
  background: #0A0A0A !important;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}
.announcement-bar__message,
.announcement-bar a {
  color: #E8E0D5 !important;
  font-size: 11px;
  font-weight: 600;
}

/* === HEADER === */
.header,
.section-header {
  background-color: #E8E0D5 !important;
  border-bottom: 1px solid rgba(10,10,10,0.1) !important;
}
.header__heading-link,
.header__heading a {
  letter-spacing: 0.2em;
  text-transform: uppercase;
  font-weight: 800;
  color: #0A0A0A !important;
}
.header__menu-item span {
  font-size: 10px !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  font-weight: 700 !important;
}
.header__menu-item:hover span { color: #4A6741 !important; }

/* === BUTTONS === */
.button,
.btn {
  border-radius: 0 !important;
  font-size: 11px !important;
  letter-spacing: 0.15em !important;
  text-transform: uppercase !important;
  font-weight: 700 !important;
  padding: 16px 36px !important;
  transition: all 0.25s ease !important;
}
.button--primary,
.product-form__submit {
  background: #4A6741 !important;
  color: #F5F5F0 !important;
  border: 2px solid #4A6741 !important;
}
.button--primary:hover,
.product-form__submit:hover {
  background: #3d5636 !important;
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(74,103,65,0.28) !important;
}
.button--secondary {
  background: transparent !important;
  color: #0A0A0A !important;
  border: 2px solid #0A0A0A !important;
}
.button--secondary:hover {
  background: #0A0A0A !important;
  color: #E8E0D5 !important;
}

/* === PRODUCT PAGE === */
.product__title {
  font-size: clamp(1.8rem, 3vw, 2.8rem) !important;
  font-weight: 400 !important;
  letter-spacing: -0.01em !important;
  line-height: 1.2 !important;
  color: #0A0A0A !important;
}
.price,
.price__regular {
  font-size: 1.8rem !important;
  font-weight: 800 !important;
  color: #0A0A0A !important;
}
.product__media-wrapper { background: #EDE5D8; border-radius: 4px; }
.thumbnail-list__item.is-active .thumbnail {
  border-color: #4A6741 !important;
  border-width: 2px !important;
}
.product__description {
  border-top: 1px solid rgba(10,10,10,0.1) !important;
  padding-top: 2rem !important;
  line-height: 1.7 !important;
}
.select,
select {
  border: 1.5px solid rgba(10,10,10,0.3) !important;
  border-radius: 0 !important;
  background-color: #E8E0D5 !important;
}
.select:focus { border-color: #4A6741 !important; }

/* === PRODUCT CARDS === */
.card,
.card-wrapper {
  background: #EDE5D8 !important;
  border-radius: 3px !important;
  transition: transform 0.25s ease, box-shadow 0.25s ease !important;
  overflow: hidden;
}
.card:hover {
  transform: translateY(-4px) !important;
  box-shadow: 0 12px 40px rgba(10,10,10,0.1) !important;
}
.card__heading a { color: #0A0A0A !important; }
.card__heading a:hover { color: #4A6741 !important; }

/* === HERO BANNER === */
.banner { background-color: #0A0A0A !important; }
.banner__heading,
.banner__text { color: #E8E0D5 !important; }

/* === SECTION TITLES === */
.title-wrapper__title,
.collection__title,
.section-heading {
  font-weight: 400 !important;
  letter-spacing: 0.06em !important;
  text-transform: uppercase !important;
  color: #0A0A0A !important;
}

/* === FOOTER === */
.footer,
.footer__content-top,
.footer__content-bottom { background: #0A0A0A !important; }
.footer p,
.footer li,
.footer span { color: #B8A898 !important; }
.footer a { color: #B8A898 !important; transition: color 0.2s ease !important; }
.footer a:hover { color: #E8E0D5 !important; }
.footer__column-header,
.footer__heading {
  color: #E8E0D5 !important;
  font-size: 10px !important;
  letter-spacing: 0.18em !important;
  text-transform: uppercase !important;
  font-weight: 700 !important;
}

/* === FORMS / INPUTS === */
.field__input,
input[type="text"],
input[type="email"],
textarea {
  border: 1.5px solid rgba(10,10,10,0.2) !important;
  border-radius: 0 !important;
  background-color: #F5F0E8 !important;
  color: #0A0A0A !important;
  padding: 12px 16px !important;
}
.field__input:focus,
input[type="text"]:focus,
input[type="email"]:focus {
  border-color: #4A6741 !important;
  outline: none !important;
  box-shadow: 0 0 0 2px rgba(74,103,65,0.15) !important;
}

/* === BADGES === */
.badge {
  border-radius: 0 !important;
  font-size: 10px !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
  background: #4A6741 !important;
  color: #F5F5F0 !important;
}

/* === SCROLLBAR === */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #E8E0D5; }
::-webkit-scrollbar-thumb { background: #B8A898; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #6B6860; }

/* === FOCUS === */
:focus-visible {
  outline: 2px solid #4A6741 !important;
  outline-offset: 3px !important;
}

/* === TRUST SIGNALS (product page) === */
.paxa-trust-bar {
  display: flex;
  gap: 1.5rem;
  padding: 1.2rem 0;
  border-top: 1px solid rgba(10,10,10,0.08);
  border-bottom: 1px solid rgba(10,10,10,0.08);
  margin: 1.5rem 0;
}
.paxa-trust-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #0A0A0A;
}
```

---

## TASK 3 — Inject CSS into layout/theme.liquid

1. Fetch the current `layout/theme.liquid` via Shopify API
2. Find the `</head>` closing tag
3. Insert this line just before `</head>`:
   `{{ 'paxa-custom.css' | asset_url | stylesheet_tag }}`
4. PUT the updated `layout/theme.liquid` back via API

---

## TASK 4 — Update settings_data.json

Fetch `config/settings_data.json` and update these values in `presets.Dawn`:

```json
{
  "color_schemes": {
    "scheme-1": {
      "settings": {
        "background": "#E8E0D5",
        "text": "#0A0A0A",
        "button": "#4A6741",
        "button_label": "#F5F5F0",
        "secondary_button_label": "#0A0A0A",
        "shadow": "#0A0A0A"
      }
    },
    "scheme-2": {
      "settings": {
        "background": "#0A0A0A",
        "text": "#E8E0D5",
        "button": "#4A6741",
        "button_label": "#F5F5F0",
        "secondary_button_label": "#E8E0D5"
      }
    }
  },
  "buttons_radius": 0,
  "buttons_border_thickness": 2,
  "card_corner_radius": 3,
  "inputs_radius": 0
}
```

---

## TASK 5 — Update Announcement Bar

In the header-group.json section data, update the announcement bar text to:
`"Science-backed separation anxiety protocol — 30 days, £29"`

---

## TASK 6 — Set Product Page to Use Media Carousel

In `config/settings_data.json`, ensure these product media settings are set:
- `media_size`: `"large"` 
- `gallery_layout`: `"thumbnail_slider"` (enables carousel with thumbnails)
- `media_position`: `"left"`

---

## TASK 7 — Commit and Push

After all changes:
1. `git add -A`
2. `git commit -m "feat: apply PAXA brand identity to Shopify Dawn theme"`
3. `git push origin main`

---

## API AUTHENTICATION

The Shopify MCP (claude-mcp1) is already connected with write access.
For direct REST API calls use:
- Store: paxa-7714.myshopify.com  
- Theme ID: 197891162449
- The MCP connector handles auth — use its tools or call via its session token

If using curl/fetch directly, the access token is in your MCP server config.

---

## IMPORTANT RULES

- UK English only: behaviour, colour, recognise
- Never add exclamation marks to product copy
- CTA text: "Start the protocol — £29 →" → https://paxapet.gumroad.com/l/PAXA-Solo
- Background color #E8E0D5 must apply to EVERY section sitewide
- The sage green #4A6741 is the ONLY accent color for buttons and CTAs
```
