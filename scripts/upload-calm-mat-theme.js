#!/usr/bin/env node
/**
 * PAXA Calm Mat — Shopify Theme Uploader
 * Uploads the 3 theme files and sets the product template
 *
 * Run: SHOPIFY_ACCESS_TOKEN=shpat_xxxx node scripts/upload-calm-mat-theme.js
 * Get token: Shopify Admin → Settings → Apps → Develop apps → claude-mcp1 → API credentials
 */

const fs   = require('fs');
const path = require('path');

const SHOP     = 'paxa-7714.myshopify.com';
const THEME_ID = '197891162449';
const PRODUCT_ID = '10755216605521';
const TOKEN    = process.env.SHOPIFY_ACCESS_TOKEN;

if (!TOKEN) {
  console.error('❌  SHOPIFY_ACCESS_TOKEN not set');
  console.error('    export SHOPIFY_ACCESS_TOKEN=shpat_xxxxx');
  process.exit(1);
}

const BASE    = `https://${SHOP}/admin/api/2024-01`;
const HEADERS = { 'Content-Type': 'application/json', 'X-Shopify-Access-Token': TOKEN };

async function api(method, url, body) {
  const res = await fetch(`${BASE}${url}`, {
    method,
    headers: HEADERS,
    body: body ? JSON.stringify(body) : undefined,
  });
  const text = await res.text();
  if (!res.ok) throw new Error(`${method} ${url} → ${res.status}: ${text}`);
  return JSON.parse(text);
}

function read(rel) {
  return fs.readFileSync(path.join(__dirname, '..', rel), 'utf8');
}

async function main() {
  console.log('🐾  PAXA Calm Mat Theme Uploader\n');

  // ── 1. Upload paxa-product.css ──────────────────────────────
  console.log('1/4  Uploading assets/paxa-product.css...');
  await api('PUT', `/themes/${THEME_ID}/assets.json`, {
    asset: { key: 'assets/paxa-product.css', value: read('shopify-theme/assets/paxa-product.css') }
  });
  console.log('     ✅  paxa-product.css uploaded');

  // ── 2. Upload paxa-logo.jpg if not already there ────────────
  console.log('2/4  Checking paxa-logo.jpg...');
  try {
    await api('GET', `/themes/${THEME_ID}/assets.json?asset[key]=assets/paxa-logo.jpg`);
    console.log('     ✅  paxa-logo.jpg already exists (skipped)');
  } catch (e) {
    // Try uploading from local shopify-theme/assets folder
    const logoPath = path.join(__dirname, '..', 'shopify-theme/assets/paxa-logo.jpg');
    if (fs.existsSync(logoPath)) {
      const logoData = fs.readFileSync(logoPath).toString('base64');
      await api('PUT', `/themes/${THEME_ID}/assets.json`, {
        asset: { key: 'assets/paxa-logo.jpg', attachment: logoData }
      });
      console.log('     ✅  paxa-logo.jpg uploaded from local file');
    } else {
      console.log('     ⚠️   paxa-logo.jpg not in local assets — using Shopify CDN version');
      console.log('     →   Set logo manually in Shopify Admin > Theme Settings > Logo');
    }
  }

  // ── 3. Upload sections/paxa-calm-mat-product.liquid ─────────
  console.log('3/4  Uploading sections/paxa-calm-mat-product.liquid...');
  await api('PUT', `/themes/${THEME_ID}/assets.json`, {
    asset: {
      key:   'sections/paxa-calm-mat-product.liquid',
      value: read('shopify-theme/sections/paxa-calm-mat-product.liquid')
    }
  });
  console.log('     ✅  paxa-calm-mat-product.liquid uploaded');

  // ── 4. Upload templates/product.calm-mat.json ───────────────
  console.log('4/4  Uploading templates/product.calm-mat.json...');
  const templateJson = {
    sections: {
      'paxa-calm-mat-product': {
        type: 'paxa-calm-mat-product',
        settings: {}
      }
    },
    order: ['paxa-calm-mat-product']
  };
  await api('PUT', `/themes/${THEME_ID}/assets.json`, {
    asset: {
      key:   'templates/product.calm-mat.json',
      value: JSON.stringify(templateJson, null, 2)
    }
  });
  console.log('     ✅  product.calm-mat.json uploaded');

  // ── 5. Set product template suffix ──────────────────────────
  console.log('\n5/5  Assigning "calm-mat" template to product...');
  try {
    await api('PUT', `/products/${PRODUCT_ID}.json`, {
      product: { id: PRODUCT_ID, template_suffix: 'calm-mat' }
    });
    console.log('     ✅  Template assigned');
  } catch (e) {
    console.log('     ⚠️   Could not assign template via API:', e.message);
    console.log('     →   Do it manually (30 sec):');
    console.log(`         https://${SHOP}/admin/products/${PRODUCT_ID}`);
    console.log('         Scroll to "Theme template" → select "calm-mat" → Save');
  }

  console.log('\n════════════════════════════════════════');
  console.log('✅  All done. Product page is live at:');
  console.log(`   https://${SHOP}/products/paxa-calm-mat-bundle-of-2`);
  console.log('\nIf the page still shows Dawn default:');
  console.log('   Wait 30 seconds then hard-refresh (Ctrl+Shift+R)');
  console.log('════════════════════════════════════════\n');
}

main().catch(err => {
  console.error('\n❌  Error:', err.message);
  process.exit(1);
});
