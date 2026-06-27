#!/usr/bin/env node
/**
 * render_posters.mjs — render an HTML poster deck to PNG screenshots.
 *
 * Each <article class="poster" id="poster-NN"> in the HTML is screenshotted at
 * its native CSS size (1080x1920) and saved at 2x device scale (2160x3840) for
 * crisp social-media output. Re-run this after editing the HTML to refresh the
 * exported PNGs.
 *
 * Usage:
 *   node tools/render_posters.mjs                       # default deck below
 *   node tools/render_posters.mjs <deck.html>           # custom HTML, PNGs next to it
 *   node tools/render_posters.mjs <deck.html> <outDir>  # custom output dir
 *
 * Requires Playwright (global install is fine): `npm i -g playwright`.
 * No Playwright browser download needed if a recent Chromium is already cached;
 * otherwise run `npx playwright install chromium` once.
 */
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';
import { execSync } from 'node:child_process';

const require = createRequire(import.meta.url);
const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

// --- resolve Playwright (local node_modules first, then global) ---
function loadPlaywright() {
  try {
    return require('playwright');
  } catch {
    const globalRoot = execSync('npm root -g').toString().trim();
    return require(path.join(globalRoot, 'playwright'));
  }
}
const { chromium } = loadPlaywright();

// --- deck + output paths (overridable via argv) ---
const htmlPath = process.argv[2]
  ? path.resolve(process.argv[2])
  : path.join(repoRoot, '社媒文件/6.24 小红书/light-blue-posters.html');
const outDir = process.argv[3] ? path.resolve(process.argv[3]) : path.dirname(htmlPath);

// Semantic export names for the AJS Xiaohongshu deck. Falls back to "<id>.png"
// for any poster id not listed here, so the script also works on other decks.
const NAME_MAP = {
  'poster-01': '01-ajs-overview.png',
  'poster-02': '02-workflow-atlas.png',
  'poster-03': '03-discipline-map.png',
  'poster-04': '04-journal-cover-wall.png',
  'poster-05': '05-copaper-cta.png',
};

const browser = await chromium.launch();
const page = await browser.newPage({
  viewport: { width: 1280, height: 2000 },
  deviceScaleFactor: 2,
});

await page.goto(pathToFileURL(htmlPath).href, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(400);

// Discover every poster element with an id in document order.
const ids = await page.$$eval('.poster[id]', (els) => els.map((e) => e.id));
if (ids.length === 0) {
  console.error('No ".poster[id]" elements found in', htmlPath);
  await browser.close();
  process.exit(1);
}

for (const id of ids) {
  const el = page.locator('#' + id);
  await el.scrollIntoViewIfNeeded();
  const box = await el.boundingBox();
  const out = path.join(outDir, NAME_MAP[id] || `${id}.png`);
  await el.screenshot({ path: out });
  console.log(`${path.basename(out)}  (${Math.round(box.width)}x${Math.round(box.height)} css px @2x)`);
}

await browser.close();
console.log(`done — ${ids.length} poster(s) → ${outDir}`);
