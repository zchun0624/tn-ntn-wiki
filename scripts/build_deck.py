#!/usr/bin/env python3
"""⑤ 渲染：把通過 C、D 關的逐頁稿原文轉成 deck.html，不改任何字。

用法：python3 scripts/build_deck.py slides/<slug>
出處：每一頁底部列出引用卡片對應的 wiki 頁，以及原始資料 [id, p.X]。
示意圖：只畫該頁文字裡已經通過檢查的數字。
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CITE = re.compile(r"\s*〔卡:([\w-]+)#F(\d+)〕")
SRC = re.compile(r"\[([a-z0-9]+), (p\.[^\]]*)\]")

FIGS = {
"platforms": """<svg viewBox="0 0 420 380" role="img" aria-label="地面、高空平台與衛星的相對位置示意">
<rect x="0" y="330" width="420" height="50" fill="var(--ground)"/>
<text x="210" y="362" class="lbl" text-anchor="middle">地面</text>
<g transform="translate(70,270)"><rect x="-6" y="0" width="12" height="60" fill="var(--ink)"/><path d="M-22 0 L0 -18 L22 0" fill="none" stroke="var(--ink)" stroke-width="4"/></g>
<text x="70" y="255" class="lbl" text-anchor="middle">地面基地台</text>
<g transform="translate(210,175)"><ellipse rx="46" ry="16" fill="var(--blue)"/><rect x="-10" y="14" width="20" height="10" fill="var(--blue)"/></g>
<text x="210" y="150" class="lbl" text-anchor="middle">高空平台（HAPS）約 20 km</text>
<g transform="translate(340,60)"><rect x="-14" y="-14" width="28" height="28" fill="var(--accent)"/><rect x="-58" y="-6" width="38" height="12" fill="var(--blue)"/><rect x="20" y="-6" width="38" height="12" fill="var(--blue)"/></g>
<text x="340" y="105" class="lbl" text-anchor="middle">衛星</text>
<text x="410" y="20" class="note" text-anchor="end">高度不按比例</text>
</svg>""",
"orbits": """<svg viewBox="0 0 440 400" role="img" aria-label="LEO、MEO、GEO 三種軌道高度示意">
<defs><clipPath id="oc"><rect x="0" y="0" width="440" height="400"/></clipPath></defs>
<g clip-path="url(#oc)">
<path d="M50 400 A170 170 0 0 1 390 400" fill="var(--ground)"/>
<path d="M20 400 A200 200 0 0 1 420 400" fill="none" stroke="var(--accent)" stroke-width="3"/>
<path d="M-60 400 A280 280 0 0 1 500 400" fill="none" stroke="var(--blue)" stroke-width="3" stroke-dasharray="8 6"/>
<path d="M-150 400 A370 370 0 0 1 590 400" fill="none" stroke="var(--ink)" stroke-width="3" stroke-dasharray="2 6"/>
</g>
<text x="220" y="330" class="lbl" text-anchor="middle">地球</text>
<text x="220" y="192" class="lbl" text-anchor="middle">LEO 約 500～2,000 km</text>
<text x="220" y="112" class="lbl" text-anchor="middle">MEO 約 8,000～20,000 km</text>
<text x="220" y="22" class="lbl" text-anchor="middle">GEO 35,786 km</text>
<text x="430" y="392" class="note" text-anchor="end">高度不按比例</text>
</svg>""",
"payload": """<svg viewBox="0 0 460 360" role="img" aria-label="透明式與再生式衛星架構示意">
<text x="0" y="22" class="h">透明式：衛星像鏡子</text>
<g class="row" transform="translate(0,40)">
<rect x="0" y="40" width="70" height="40" rx="8" class="box"/><text x="35" y="66" class="lbl" text-anchor="middle">手機</text>
<rect x="150" y="0" width="80" height="40" rx="8" class="box sat"/><text x="190" y="26" class="lbl" text-anchor="middle">衛星</text>
<rect x="290" y="40" width="160" height="40" rx="8" class="box hl"/><text x="370" y="66" class="lbl" text-anchor="middle">地面基地台（gNB）</text>
<path d="M70 60 L150 22 M230 22 L290 60" class="arrow"/></g>
<text x="0" y="200" class="h">再生式：衛星自己就是基地台</text>
<g transform="translate(0,218)">
<rect x="0" y="60" width="70" height="40" rx="8" class="box"/><text x="35" y="86" class="lbl" text-anchor="middle">手機</text>
<rect x="130" y="0" width="120" height="40" rx="8" class="box hl"/><text x="190" y="26" class="lbl" text-anchor="middle">衛星＝基地台</text>
<rect x="330" y="0" width="120" height="40" rx="8" class="box sat"/><text x="390" y="26" class="lbl" text-anchor="middle">另一顆衛星</text>
<rect x="330" y="80" width="120" height="40" rx="8" class="box"/><text x="390" y="106" class="lbl" text-anchor="middle">地面閘道站</text>
<path d="M70 80 L130 22 M250 20 L330 20 M250 30 L330 100" class="arrow"/>
<text x="290" y="12" class="note" text-anchor="middle">ISL</text></g>
</svg>""",
"timing": """<svg viewBox="0 0 440 360" role="img" aria-label="手機先算好再送的三個步驟">
<g class="step" transform="translate(10,10)"><rect width="420" height="90" rx="12" class="box"/>
<circle cx="45" cy="45" r="24" fill="var(--accent)"/><text x="45" y="53" class="num" text-anchor="middle">1</text>
<text x="88" y="40" class="lbl">衛星廣播自己的軌道</text><text x="88" y="68" class="note">（星曆）</text></g>
<g class="step" transform="translate(10,130)"><rect width="420" height="90" rx="12" class="box"/>
<circle cx="45" cy="45" r="24" fill="var(--accent)"/><text x="45" y="53" class="num" text-anchor="middle">2</text>
<text x="88" y="40" class="lbl">手機用 GNSS 知道自己在哪</text><text x="88" y="68" class="note">算出來回時間和相對速度</text></g>
<g class="step" transform="translate(10,250)"><rect width="420" height="90" rx="12" class="box hl"/>
<circle cx="45" cy="45" r="24" fill="var(--accent)"/><text x="45" y="53" class="num" text-anchor="middle">3</text>
<text x="88" y="40" class="lbl">提早送出＋先調好頻率</text><text x="88" y="68" class="note">訊號剛好準時、準頻到達</text></g>
</svg>""",
"dualsteer": """<svg viewBox="0 0 440 360" role="img" aria-label="一支手機同時連地面與衛星兩條路">
<rect x="10" y="150" width="80" height="60" rx="10" class="box hl"/><text x="50" y="186" class="lbl" text-anchor="middle">手機</text>
<text x="50" y="232" class="note" text-anchor="middle">兩張 SIM 卡</text>
<rect x="170" y="40" width="110" height="44" rx="10" class="box sat"/><text x="225" y="68" class="lbl" text-anchor="middle">衛星</text>
<rect x="170" y="276" width="110" height="44" rx="10" class="box"/><text x="225" y="304" class="lbl" text-anchor="middle">地面基地台</text>
<rect x="330" y="150" width="100" height="60" rx="10" class="box"/><text x="380" y="186" class="lbl" text-anchor="middle">核心網</text>
<path d="M90 165 L170 62 M280 62 L330 165" class="arrow" stroke-dasharray="8 6"/>
<path d="M90 195 L170 298 M280 298 L330 195" class="arrow"/>
<text x="220" y="185" class="note" text-anchor="middle">同一時間只走一條</text>
</svg>""",
"timeline": """<svg viewBox="0 0 460 300" role="img" aria-label="3GPP NTN 版本時間軸">
<line x1="20" y1="150" x2="440" y2="150" stroke="var(--ink)" stroke-width="3"/>
<g class="tick" transform="translate(40,150)"><circle r="10" class="dot"/><text y="-28" class="lbl" text-anchor="middle">Rel-15</text><text y="40" class="note" text-anchor="middle">2019</text></g>
<g class="tick" transform="translate(140,150)"><circle r="14" class="dot hl"/><text y="-28" class="lbl" text-anchor="middle">Rel-17</text><text y="40" class="note" text-anchor="middle">2022</text><text y="64" class="note" text-anchor="middle">第一個正式規格</text></g>
<g class="tick" transform="translate(240,150)"><circle r="10" class="dot"/><text y="-28" class="lbl" text-anchor="middle">Rel-18</text><text y="40" class="note" text-anchor="middle">2024</text></g>
<g class="tick" transform="translate(330,150)"><circle r="10" class="dot open"/><text y="-28" class="lbl" text-anchor="middle">Rel-19</text><text y="40" class="note" text-anchor="middle">預計 2025</text></g>
<g class="tick" transform="translate(420,150)"><circle r="10" class="dot open"/><text y="-28" class="lbl" text-anchor="middle">Rel-20</text><text y="40" class="note" text-anchor="middle">目標 2027</text></g>
</svg>""",
}


def parse(p):
    m = re.match(r"---\n(.*?)\n---\n(.*)", p.read_text(encoding="utf-8"), re.S)
    fm = {}
    for line in m.group(1).splitlines():
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip()
    return fm, m.group(2)


def load_cards(d):
    cards = {}
    for p in (d / "cards").glob("*.md"):
        txt = p.read_text(encoding="utf-8")
        src = re.search(r"`(wiki/[^`]+)`", txt).group(1)
        facts = dict((int(a), b) for a, b in re.findall(r"- F(\d+)｜[^｜]*｜(.*)", txt))
        cards[p.stem] = (src, facts)
    return cards


def strip(s):
    return CITE.sub("", s).strip()


def esc(s):
    return html.escape(s, quote=False)


def slide_html(fm, body, cards):
    used = []
    for c, f in CITE.findall(fm.get("analogy", "") + body):
        if (c, f) not in used:
            used.append((c, f))
    wiki_pages, orig = [], []
    for c, f in used:
        src, facts = cards[c]
        if src not in wiki_pages:
            wiki_pages.append(src)
        for sid, pg in SRC.findall(facts.get(int(f), "")):
            tag = f"{sid}, {pg}"
            if tag not in orig:
                orig.append(tag)
    kind = fm.get("type", "content")
    title = esc(fm["title"])
    lines = [l.strip() for l in body.strip().splitlines() if l.strip()]
    if kind == "cover":
        inner = f'<div class="cover"><p class="kicker">TN-NTN 入門・教學簡報</p><h1>{title}</h1><p class="sub">{esc(strip(lines[0]))}</p><p class="meta">資料來源：TN-NTN LLM Wiki（6 份資料、34 頁）</p></div>'
    else:
        parts = []
        rows = [l for l in lines if l.startswith("|")]
        bullets = [l for l in lines if l.startswith("- ")]
        if rows:
            cells = [[esc(strip(c)) for c in r.strip("|").split("|")] for r in rows]
            th = "".join(f"<th>{c}</th>" for c in cells[0])
            tb = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in cells[1:])
            parts.append(f'<table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table>')
        if bullets:
            lis = "".join(f"<li>{esc(strip(b[2:]))}</li>" for b in bullets)
            parts.append(f'<ul class="{"big" if kind == "summary" else ""}">{lis}</ul>')
        fig = fm.get("figure", "none")
        figure = f'<figure class="fig">{FIGS[fig]}</figure>' if fig != "none" else ""
        analogy = f'<p class="analogy"><span>生活比喻</span>{esc(strip(fm["analogy"]))}</p>' if fm.get("analogy") else ""
        inner = (f'<header><span class="no">{int(fm["no"]):02d}</span><h2>{title}</h2></header>{analogy}'
                 f'<div class="content{" with-fig" if figure else ""}"><div class="text">{"".join(parts)}</div>{figure}</div>')
    foot = f'<footer>出處｜wiki：{"、".join(p.replace("wiki/", "") for p in wiki_pages)}　原始資料：{"；".join(orig)}</footer>'
    return f'<section class="slide k-{kind}" data-no="{fm["no"]}"><div class="inner">{inner}</div>{foot}</section>'


CSS = """
:root{--bg:#F6F4EF;--card:#FFFFFF;--ink:#14213D;--muted:#5C6478;--line:#E3DED3;--blue:#2A6F97;--accent:#E07A2F;--accent-soft:#FCEBDD;--ground:#DCE8E0;
--sans:"Noto Sans TC",system-ui,sans-serif;--mono:"IBM Plex Mono",ui-monospace,monospace}
*{box-sizing:border-box}html,body{margin:0;height:100%;background:#0E1526;font-family:var(--sans);color:var(--ink)}
.stage{position:fixed;inset:0;display:flex;align-items:center;justify-content:center;overflow:hidden}
.deck{width:1280px;height:720px;position:relative;transform-origin:center center}
.slide{position:absolute;inset:0;background:var(--bg);display:none;flex-direction:column;padding:56px 72px 0}
.slide.on{display:flex}
.inner{flex:1;min-height:0;overflow:hidden;display:flex;flex-direction:column}
header{display:flex;align-items:baseline;gap:18px;margin-bottom:18px}
header .no{font-family:var(--mono);color:var(--accent);font-size:24px;font-weight:600}
h2{font-size:44px;line-height:1.2;margin:0;letter-spacing:.01em}
.analogy{align-self:stretch;margin:0 0 22px;padding:14px 20px;background:var(--accent-soft);border-left:6px solid var(--accent);border-radius:8px;font-size:22px;line-height:1.55}
.analogy span{display:inline-block;font-size:14px;font-weight:700;color:var(--accent);margin-right:12px;letter-spacing:.1em;vertical-align:2px}
.content{flex:1;min-height:0;display:grid;grid-template-columns:1fr;gap:36px;align-items:center}
.content.with-fig{grid-template-columns:1.15fr .85fr}
ul{margin:0;padding:0;list-style:none;display:grid;gap:16px}
li{font-size:25px;line-height:1.5;padding-left:30px;position:relative}
li::before{content:"";position:absolute;left:4px;top:.62em;width:12px;height:12px;border-radius:3px;background:var(--blue)}
.content:not(.with-fig) li{font-size:30px}
ul.big li{font-size:34px}
table{width:100%;border-collapse:collapse;font-size:23px;background:var(--card);border-radius:10px;overflow:hidden;box-shadow:0 0 0 1px var(--line)}
th,td{text-align:left;padding:14px 20px;border-bottom:1px solid var(--line);vertical-align:top}
th{background:var(--ink);color:#fff;font-weight:600}tr:last-child td{border-bottom:0}
td:first-child{font-weight:600;color:var(--blue);white-space:nowrap}
.fig{margin:0;height:100%;max-height:380px;display:flex;align-items:center;justify-content:center}
.fig svg{width:100%;height:100%;overflow:visible}
.fig .lbl{font-size:17px;fill:var(--ink);font-weight:500}.fig .note{font-size:14px;fill:var(--muted)}
.fig .h{font-size:19px;font-weight:700;fill:var(--ink)}.fig .num{font-size:24px;fill:#fff;font-weight:700}
.fig .box{fill:var(--card);stroke:var(--line);stroke-width:2}.fig .box.hl{fill:var(--accent-soft);stroke:var(--accent)}.fig .box.sat{fill:#E4EEF4;stroke:var(--blue)}
.fig .arrow{fill:none;stroke:var(--ink);stroke-width:2.5}
.fig .dot{fill:var(--blue)}.fig .dot.hl{fill:var(--accent)}.fig .dot.open{fill:var(--bg);stroke:var(--blue);stroke-width:3}
footer{flex:none;font-size:13px;color:var(--muted);border-top:1px solid var(--line);padding:10px 0 14px;margin-top:12px;line-height:1.5}
.cover{flex:1;display:flex;flex-direction:column;justify-content:center;background:radial-gradient(circle at 85% 20%,#E4EEF4 0,transparent 45%)}
.cover .kicker{font-family:var(--mono);font-size:18px;color:var(--accent);letter-spacing:.12em;margin:0 0 18px}
.cover h1{font-size:72px;line-height:1.15;margin:0 0 18px}.cover .sub{font-size:30px;color:var(--blue);margin:0 0 40px}
.cover .meta{font-size:18px;color:var(--muted);margin:0}
.nav{position:fixed;left:50%;bottom:14px;transform:translateX(-50%);display:flex;gap:10px;align-items:center;font-family:var(--mono);color:#C9D2E3;font-size:14px;z-index:5}
.nav button{background:#1E2A44;color:#fff;border:0;border-radius:999px;width:38px;height:38px;font-size:18px;cursor:pointer}
.bar{position:fixed;left:0;top:0;height:4px;background:var(--accent);z-index:5;transition:width .2s}
body.all .stage{position:static;display:block;overflow:visible}body.all .deck{transform:none!important;height:auto}
body.all .slide{display:flex;position:relative;height:720px;margin:0 0 20px}body.all .nav,body.all .bar{display:none}
@media print{body{background:#fff}.nav,.bar{display:none}.stage{position:static;display:block}.deck{transform:none!important;height:auto}.slide{display:flex;position:relative;height:720px;page-break-after:always}}
"""

JS = """
const deck=document.querySelector('.deck'),slides=[...document.querySelectorAll('.slide')],bar=document.querySelector('.bar'),cnt=document.querySelector('.cnt');
let i=0;const all=new URLSearchParams(location.search).has('all');if(all)document.body.classList.add('all');
function fit(){if(all)return;const s=Math.min(innerWidth/1280,(innerHeight-60)/720);deck.style.transform=`scale(${s})`;}
function show(n){i=Math.max(0,Math.min(slides.length-1,n));slides.forEach((s,k)=>s.classList.toggle('on',k===i));cnt.textContent=`${i+1} / ${slides.length}`;bar.style.width=`${(i+1)/slides.length*100}%`;}
addEventListener('keydown',e=>{if(['ArrowRight','PageDown',' '].includes(e.key)){e.preventDefault();show(i+1)}if(['ArrowLeft','PageUp'].includes(e.key)){e.preventDefault();show(i-1)}});
document.querySelector('.prev').onclick=()=>show(i-1);document.querySelector('.next').onclick=()=>show(i+1);
let x0=null;addEventListener('touchstart',e=>x0=e.touches[0].clientX);addEventListener('touchend',e=>{if(x0===null)return;const dx=e.changedTouches[0].clientX-x0;if(Math.abs(dx)>40)show(i+(dx<0?1:-1));x0=null});
addEventListener('resize',fit);fit();show(0);
"""


def main():
    d = ROOT / sys.argv[1]
    cards = load_cards(d)
    secs = [slide_html(*parse(p), cards) for p in sorted((d / "drafts").glob("*.md"))]
    page = f"""<!DOCTYPE html>
<html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>衛星怎麼幫手機上網</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;600&family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="bar"></div><div class="stage"><div class="deck">{''.join(secs)}</div></div>
<div class="nav"><button class="prev" aria-label="上一頁">‹</button><span class="cnt"></span><button class="next" aria-label="下一頁">›</button></div>
<script>{JS}</script></body></html>"""
    (d / "deck.html").write_text(page, encoding="utf-8")
    print(f"deck.html：{len(secs)} 頁")


if __name__ == "__main__":
    main()
