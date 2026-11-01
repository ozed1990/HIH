// Renders content/media/*.svg to 1200x900 PNG with the site's Manrope font (then PIL converts to WebP).
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const dir = path.resolve(__dirname, '../content/media');
  const font = 'file://' + path.resolve(__dirname, '../../assets/hih-manrope-var.woff2');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 900 } });
  await page.goto('file://' + dir + '/'); // a file:// origin, so the local font URL may load (about:blank blocks it)
  for (const f of fs.readdirSync(dir).filter((x) => x.endsWith('.svg'))) {
    const svg = fs.readFileSync(path.join(dir, f), 'utf8');
    await page.setContent(`<style>@font-face{font-family:Manrope;src:url(${font})}body{margin:0}</style>${svg}`);
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.join(dir, f.replace('.svg', '.png')) });
  }
  await browser.close();
})();
