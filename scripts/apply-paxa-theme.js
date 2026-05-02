#!/usr/bin/env node
/**
 * PAXA Shopify Theme Patcher
 * Run: node scripts/apply-paxa-theme.js
 *
 * Requires: SHOPIFY_ACCESS_TOKEN env var
 * Get token from: Shopify Admin > Apps > claude-mcp1 > API credentials
 * Or check: .claude/settings.json for MCP config
 */

const SHOP = 'paxa-7714.myshopify.com';
const THEME_ID = '197891162449';
const TOKEN = process.env.SHOPIFY_ACCESS_TOKEN;

if (!TOKEN) {
  console.error('❌ Set SHOPIFY_ACCESS_TOKEN env var first');
  console.error('   export SHOPIFY_ACCESS_TOKEN=shpat_xxxxx');
  process.exit(1);
}

const BASE = `https://${SHOP}/admin/api/2024-01`;
const HEADERS = {
  'Content-Type': 'application/json',
  'X-Shopify-Access-Token': TOKEN,
};

async function api(method, path, body) {
  const res = await fetch(`${BASE}${path}`, {
    method,
    headers: HEADERS,
    body: body ? JSON.stringify(body) : undefined,
  });
  if (!res.ok) {
    const err = await res.text();
    throw new Error(`${method} ${path} → ${res.status}: ${err}`);
  }
  return res.json();
}

const PAXA_CSS = `/* PAXA CALM MAT — Premium Brand CSS */
body, .shopify-section, main { background-color: #E8E0D5; }
.color-scheme-1 { --color-background: 232 224 213 !important; background-color: #E8E0D5 !important; }
.announcement-bar { background: #0A0A0A !important; }
.announcement-bar__message { color: #E8E0D5 !important; font-size: 11px; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; }
.header, .section-header { background-color: #E8E0D5 !important; border-bottom: 1px solid rgba(10,10,10,0.1) !important; }
.header__heading-link { letter-spacing: 0.2em; text-transform: uppercase; font-weight: 800; color: #0A0A0A !important; }
.header__menu-item span { font-size: 10px !important; letter-spacing: 0.12em !important; text-transform: uppercase !important; font-weight: 700 !important; }
.header__menu-item:hover span { color: #4A6741 !important; }
.button, .btn { border-radius: 0 !important; font-size: 11px !important; letter-spacing: 0.15em !important; text-transform: uppercase !important; font-weight: 700 !important; padding: 16px 36px !important; transition: all 0.25s ease !important; }
.button--primary, .product-form__submit { background: #4A6741 !important; color: #F5F5F0 !important; border: 2px solid #4A6741 !important; }
.button--primary:hover, .product-form__submit:hover { background: #3d5636 !important; transform: translateY(-1px); box-shadow: 0 6px 20px rgba(74,103,65,0.28) !important; }
.button--secondary { background: transparent !important; color: #0A0A0A !important; border: 2px solid #0A0A0A !important; }
.button--secondary:hover { background: #0A0A0A !important; color: #E8E0D5 !important; }
.product__title { font-size: clamp(1.8rem, 3vw, 2.8rem) !important; font-weight: 400 !important; letter-spacing: -0.01em !important; }
.price, .price__regular { font-size: 1.8rem !important; font-weight: 800 !important; color: #0A0A0A !important; }
.product__media-wrapper { background: #EDE5D8; border-radius: 4px; }
.thumbnail-list__item.is-active .thumbnail { border-color: #4A6741 !important; border-width: 2px !important; }
.product__description { border-top: 1px solid rgba(10,10,10,0.1) !important; padding-top: 2rem !important; line-height: 1.7 !important; }
.select, select { border: 1.5px solid rgba(10,10,10,0.3) !important; border-radius: 0 !important; background-color: #E8E0D5 !important; }
.card, .card-wrapper { background: #EDE5D8 !important; border-radius: 3px !important; transition: transform 0.25s ease, box-shadow 0.25s ease !important; overflow: hidden; }
.card:hover { transform: translateY(-4px) !important; box-shadow: 0 12px 40px rgba(10,10,10,0.1) !important; }
.card__heading a { color: #0A0A0A !important; }
.card__heading a:hover { color: #4A6741 !important; }
.banner { background-color: #0A0A0A !important; }
.banner__heading, .banner__text { color: #E8E0D5 !important; }
.title-wrapper__title, .collection__title { font-weight: 400 !important; letter-spacing: 0.06em !important; text-transform: uppercase !important; color: #0A0A0A !important; }
.footer, .footer__content-top, .footer__content-bottom { background: #0A0A0A !important; }
.footer a { color: #B8A898 !important; }
.footer a:hover { color: #E8E0D5 !important; }
.footer__column-header { color: #E8E0D5 !important; font-size: 10px !important; letter-spacing: 0.18em !important; text-transform: uppercase !important; font-weight: 700 !important; }
.field__input, input[type="text"], input[type="email"] { border: 1.5px solid rgba(10,10,10,0.2) !important; border-radius: 0 !important; background-color: #F5F0E8 !important; }
.field__input:focus, input[type="email"]:focus { border-color: #4A6741 !important; outline: none !important; box-shadow: 0 0 0 2px rgba(74,103,65,0.15) !important; }
.badge { border-radius: 0 !important; font-size: 10px !important; background: #4A6741 !important; color: #F5F5F0 !important; }
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #E8E0D5; }
::-webkit-scrollbar-thumb { background: #B8A898; border-radius: 3px; }
:focus-visible { outline: 2px solid #4A6741 !important; outline-offset: 3px !important; }`;

async function main() {
  console.log('🐾 PAXA Theme Patcher starting...\n');

  // Step 1: Upload paxa-custom.css
  console.log('1/4 Uploading paxa-custom.css...');
  await api('PUT', `/themes/${THEME_ID}/assets.json`, {
    asset: { key: 'assets/paxa-custom.css', value: PAXA_CSS }
  });
  console.log('   ✅ paxa-custom.css uploaded');

  // Step 2: Inject into theme.liquid
  console.log('2/4 Patching layout/theme.liquid...');
  const { asset } = await api('GET', `/themes/${THEME_ID}/assets.json?asset[key]=layout/theme.liquid`);
  let liquid = asset.value;

  const cssTag = "\n  {{ 'paxa-custom.css' | asset_url | stylesheet_tag }}";
  if (!liquid.includes('paxa-custom.css')) {
    liquid = liquid.replace('</head>', cssTag + '\n</head>');
    await api('PUT', `/themes/${THEME_ID}/assets.json`, {
      asset: { key: 'layout/theme.liquid', value: liquid }
    });
    console.log('   ✅ theme.liquid patched');
  } else {
    console.log('   ✅ theme.liquid already has PAXA CSS (skipped)');
  }

  // Step 3: Update settings_data.json
  console.log('3/4 Updating brand colours in settings_data.json...');
  const { asset: settingsAsset } = await api('GET', `/themes/${THEME_ID}/assets.json?asset[key]=config/settings_data.json`);
  const settings = JSON.parse(settingsAsset.value);
  const preset = settings.presets.Dawn;

  // Apply PAXA brand colors
  preset.color_schemes = preset.color_schemes || {};
  preset.color_schemes['scheme-1'] = {
    settings: {
      background: '#E8E0D5',
      background_gradient: '',
      text: '#0A0A0A',
      button: '#4A6741',
      button_label: '#F5F5F0',
      secondary_button_label: '#0A0A0A',
      shadow: '#0A0A0A'
    }
  };
  preset.color_schemes['scheme-2'] = {
    settings: {
      background: '#0A0A0A',
      background_gradient: '',
      text: '#E8E0D5',
      button: '#4A6741',
      button_label: '#F5F5F0',
      secondary_button_label: '#E8E0D5',
      shadow: '#E8E0D5'
    }
  };

  // Apply design tokens
  preset.buttons_radius = 0;
  preset.buttons_border_thickness = 2;
  preset.card_corner_radius = 3;
  preset.inputs_radius = 0;

  await api('PUT', `/themes/${THEME_ID}/assets.json`, {
    asset: { key: 'config/settings_data.json', value: JSON.stringify(settings, null, 2) }
  });
  console.log('   ✅ settings_data.json updated');

  // Step 4: Done
  console.log('\n4/4 All done. Changes are live on:');
  console.log('   https://paxa-7714.myshopify.com');
  console.log('\nNext steps:');
  console.log('  → Set the PAXA logo in Theme Settings > Logo');
  console.log('  → Update the announcement bar text');
  console.log('  → Remove the default landscape hero image');
  console.log('  → Ensure product is in a collection');
}

main().catch(err => {
  console.error('❌ Error:', err.message);
  process.exit(1);
});
