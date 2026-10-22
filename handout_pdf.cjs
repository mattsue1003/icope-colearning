// handout.html → 直式 A4 PDF
//   NODE_PATH=<含 puppeteer-core 的 node_modules> node handout_pdf.cjs <輸出.pdf> [預覽圖資料夾]
const puppeteer = require('puppeteer-core');
const path = require('path');
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
(async () => {
  const out = process.argv[2] || path.join(__dirname, 'handout.pdf');
  const browser = await puppeteer.launch({executablePath: CHROME, headless: 'new'});
  const page = await browser.newPage();
  const errs = [];
  page.on('pageerror', e => errs.push(e.message));
  await page.setViewport({width: 794, height: 1123});
  await page.emulateMediaFeatures([{name: 'prefers-color-scheme', value: 'light'}]);
  await page.goto('file://' + path.join(__dirname, 'handout.html'), {waitUntil: 'networkidle0'});
  await page.evaluateHandle('document.fonts.ready');
  await new Promise(r => setTimeout(r, 500));
  await page.pdf({path: out, format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: '<div></div>',
    footerTemplate: '<div style="width:100%;font-size:8px;color:#728B91;text-align:center;font-family:\'PingFang TC\',sans-serif">ICOPE 長者量六力共學活動講義　<span class="pageNumber"></span> / <span class="totalPages"></span></div>'});
  console.log('pdf:', out, 'errors:', errs.length ? errs.join(' | ') : 'none');
  await browser.close();
})();
