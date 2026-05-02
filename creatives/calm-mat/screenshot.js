/**
 * PAXA Calm Mat — Screenshot Script
 * Renders all 10 HTML creatives to PNG via Puppeteer.
 * Run from repo root: node creatives/calm-mat/screenshot.js
 */

const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const DIR = path.resolve(__dirname);

const creatives = [
  { file: '01_hook_lick.html',       width: 1080, height: 1080 },
  { file: '02_cortisol_stat.html',   width: 1080, height: 1080 },
  { file: '03_two_mat_science.html', width: 1080, height: 1080 },
  { file: '04_product_hero.html',    width: 1080, height: 1080 },
  { file: '05_feature_callout.html', width: 1080, height: 1080 },
  { file: '06_story_hook.html',      width: 1080, height: 1920 },
  { file: '07_story_product.html',   width: 1080, height: 1920 },
  { file: '08_shopify_hero.html',    width: 1200, height: 628  },
  { file: '09_shopify_bundle.html',  width: 1200, height: 900  },
  { file: '10_shopify_science.html', width: 1200, height: 628  },
];

async function run() {
  console.log('Launching Puppeteer…');

  const browser = await puppeteer.launch({
    headless: 'new',
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-dev-shm-usage',
      '--font-render-hinting=none',
    ],
  });

  let passed = 0;
  let failed = 0;

  for (const c of creatives) {
    const htmlPath = path.join(DIR, c.file);
    const pngPath  = path.join(DIR, c.file.replace('.html', '.png'));

    if (!fs.existsSync(htmlPath)) {
      console.error(`  SKIP  ${c.file} — file not found`);
      failed++;
      continue;
    }

    const page = await browser.newPage();
    await page.setViewport({ width: c.width, height: c.height, deviceScaleFactor: 1 });

    // file:// URL — works on Windows with triple-slash + forward slashes
    const fileUrl = 'file:///' + htmlPath.replace(/\\/g, '/');

    try {
      await page.goto(fileUrl, { waitUntil: 'networkidle0', timeout: 30000 });
    } catch (err) {
      // networkidle0 can time out if Google Fonts is slow — continue anyway
      console.warn(`  WARN  ${c.file} — networkidle0 timed out, continuing`);
    }

    // Extra wait for Google Fonts render
    await new Promise(r => setTimeout(r, 1500));

    await page.screenshot({
      path: pngPath,
      clip: { x: 0, y: 0, width: c.width, height: c.height },
    });

    console.log(`  OK    ${c.file.replace('.html', '.png')}  ${c.width}×${c.height}px`);
    await page.close();
    passed++;
  }

  await browser.close();
  console.log(`\nDone — ${passed} saved, ${failed} failed.`);

  // Verify sizes
  console.log('\nFile sizes:');
  for (const c of creatives) {
    const pngPath = path.join(DIR, c.file.replace('.html', '.png'));
    if (fs.existsSync(pngPath)) {
      const kb = Math.round(fs.statSync(pngPath).size / 1024);
      console.log(`  ${c.file.replace('.html', '.png').padEnd(30)} ${kb} KB`);
    }
  }
}

run().catch(err => {
  console.error('Fatal:', err);
  process.exit(1);
});
