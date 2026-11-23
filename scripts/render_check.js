// E 渲染檢查：逐頁截圖，量測文字是否溢出版面。用法：node render_check.js deck.html shots/
const { chromium } = require('playwright');
const path = require('path'), fs = require('fs');
(async () => {
  const [deck, outDir] = process.argv.slice(2);
  fs.mkdirSync(outDir, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1280, height: 800 } });
  await p.route('https://fonts.**', r => r.abort());
  await p.goto('file://' + path.resolve(deck) + '?all=1');
  await p.waitForTimeout(500);
  const res = await p.$$eval('.slide', ss => ss.map(s => {
    const inner = s.querySelector('.inner');
    let worst = inner.scrollHeight;
    s.querySelectorAll('.content, .text, table, ul').forEach(e => {
      const r = e.getBoundingClientRect(), ir = inner.getBoundingClientRect();
      worst = Math.max(worst, Math.ceil(r.bottom - ir.top));
    });
    return { no: +s.dataset.no, h: worst, box: inner.clientHeight,
             overflow: worst > inner.clientHeight + 1, hscroll: inner.scrollWidth > inner.clientWidth + 1 };
  }));
  const els = await p.$$('.slide');
  for (let k = 0; k < els.length; k++) await els[k].screenshot({ path: `${outDir}/slide-${String(k + 1).padStart(2, '0')}.png` });
  console.log(JSON.stringify(res));
  await b.close();
})();
