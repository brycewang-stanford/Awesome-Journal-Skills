// Render the banner HTML sources to 2400x860 PNGs (1200x430 @2x).
// Usage: node assets/banner-src/render_banners.mjs
import path from 'path';
import { fileURLToPath } from 'url';
import { createRequire } from 'module';
import { execSync } from 'child_process';

const require = createRequire(import.meta.url);
const gRoot = execSync('npm root -g').toString().trim();
const { chromium } = require(path.join(gRoot, 'playwright'));

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, '..', '..');

const jobs = [
  { html: path.join(__dirname, 'banner-zh.html'), out: path.join(root, 'assets', 'banner-zh.png') },
  { html: path.join(__dirname, 'banner-en.html'), out: path.join(root, 'assets', 'banner-en.png') },
];

let browser;
try {
  browser = await chromium.launch({ channel: 'chrome' });
} catch (e) {
  browser = await chromium.launch();
}

for (const job of jobs) {
  const page = await browser.newPage({ viewport: { width: 1200, height: 430 }, deviceScaleFactor: 2 });
  await page.goto('file://' + job.html);
  await page.waitForTimeout(300);
  const el = await page.$('.banner');
  if (el) {
    await el.screenshot({ path: job.out });
  } else {
    await page.screenshot({ path: job.out, clip: { x: 0, y: 0, width: 1200, height: 430 } });
  }
  await page.close();
  console.log('rendered', path.relative(root, job.out));
}

await browser.close();
console.log('done');
