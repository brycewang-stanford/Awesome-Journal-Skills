// Render the banner HTML sources to 2400x860 PNGs (1200x430 @2x).
// Usage: node assets/banner-src/render_banners.mjs
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';
import { createRequire } from 'module';
import { execSync, spawnSync } from 'child_process';

const require = createRequire(import.meta.url);
let chromium = null;
try {
  const gRoot = execSync('npm root -g').toString().trim();
  ({ chromium } = require(path.join(gRoot, 'playwright')));
} catch {
  // A fresh maintainer checkout may have Chrome but no global Playwright.
}

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, '..', '..');

function* walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name === '.git') continue;
    const target = path.join(dir, entry.name);
    if (entry.isDirectory()) yield* walk(target);
    else yield target;
  }
}

const catalogData = JSON.parse(fs.readFileSync(path.join(root, 'catalog.json'), 'utf8'));
const venues = catalogData.venues ?? catalogData;
const counts = {
  SKILL_COUNT: [...walk(root)].filter((p) => p.endsWith(`${path.sep}SKILL.md`)).length,
  PACK_COUNT: JSON.parse(fs.readFileSync(path.join(root, '.claude-plugin', 'marketplace.json'), 'utf8')).plugins.length,
  JOURNAL_COUNT: venues.filter((v) => v.venue_type === 'journal').length,
  CONFERENCE_COUNT: venues.filter((v) => v.venue_type === 'conference').length,
  VENUE_COUNT: venues.length,
};

function renderTemplate(file) {
  let html = fs.readFileSync(file, 'utf8');
  for (const [key, value] of Object.entries(counts)) {
    html = html.replaceAll(`{{${key}}}`, String(value));
  }
  return html;
}

const jobs = [
  { html: path.join(__dirname, 'banner-zh.html'), out: path.join(root, 'assets', 'banner-zh.png') },
  { html: path.join(__dirname, 'banner-en.html'), out: path.join(root, 'assets', 'banner-en.png') },
];

if (chromium) {
  let browser;
  try {
    browser = await chromium.launch({ channel: 'chrome' });
  } catch {
    browser = await chromium.launch();
  }
  for (const job of jobs) {
    const page = await browser.newPage({ viewport: { width: 1200, height: 430 }, deviceScaleFactor: 2 });
    await page.setContent(renderTemplate(job.html));
    await page.waitForTimeout(300);
    await page.locator('.banner').screenshot({ path: job.out });
    await page.close();
    console.log('rendered', path.relative(root, job.out));
  }
  await browser.close();
} else {
  const chrome = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
  const tempDir = fs.mkdtempSync(path.join(process.env.TMPDIR || '/tmp', 'ajs-banner-'));
  try {
    for (const job of jobs) {
      const rendered = path.join(tempDir, path.basename(job.html));
      const profile = path.join(tempDir, `${path.basename(job.html, '.html')}-profile`);
      fs.writeFileSync(rendered, renderTemplate(job.html));
      const result = spawnSync(chrome, [
        '--headless', '--hide-scrollbars', '--no-first-run', '--disable-default-apps',
        `--user-data-dir=${profile}`, '--force-device-scale-factor=2',
        '--window-size=1200,430', `--screenshot=${job.out}`, `file://${rendered}`,
      ], { encoding: 'utf8' });
      if (result.status !== 0) throw new Error(result.stderr || `Chrome exited ${result.status}`);
      console.log('rendered', path.relative(root, job.out));
    }
  } finally {
    fs.rmSync(tempDir, { recursive: true, force: true });
  }
}
console.log('done');
