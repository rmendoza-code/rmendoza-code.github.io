// Regenera el CV (PDF) y la imagen de vista previa (og-image.png).
// Requisitos: Node 18+ y Playwright →  npm i -D playwright && npx playwright install chromium
// Uso (desde la raíz del repo):  node tools/render.js cv   |   node tools/render.js og
const { chromium } = require('playwright');
const path = require('path');
const root = path.resolve(__dirname, '..');
(async () => {
  const what = process.argv[2] || 'cv';
  const b = await chromium.launch();
  const p = await b.newPage(what === 'og' ? { viewport: { width: 1200, height: 630 } } : {});
  if (what === 'og') {
    await p.goto('file://' + path.join(root, 'tools/og/og.html'));
    await p.waitForTimeout(800);
    await p.screenshot({ path: path.join(root, 'assets/og-image.png') });
    console.log('assets/og-image.png actualizado');
  } else {
    await p.goto('file://' + path.join(root, 'tools/cv/cv.html'));
    await p.waitForTimeout(800);
    await p.pdf({ path: path.join(root, 'CV_Rodrigo_Mendoza_Cortes.pdf'), format: 'Letter', printBackground: true, preferCSSPageSize: true });
    console.log('CV_Rodrigo_Mendoza_Cortes.pdf actualizado (revisa que sean 2 páginas)');
  }
  await b.close();
})();
