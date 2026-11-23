#!/usr/bin/env python3
"""簡報流程的程式檢查關卡（workflows/topic-slides.md）。

用法：
  python3 scripts/check_slides.py slides/<slug> --stage coverage   # A 覆蓋率
  python3 scripts/check_slides.py slides/<slug> --stage drafts     # C 逐頁稿
  python3 scripts/check_slides.py slides/<slug> --stage render     # E 渲染
通過 exit 0，不通過 exit 1。
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
CITE_CARD = re.compile(r"〔卡:([\w-]+)#F(\d+)〕")
NUM_UNIT = re.compile(r"(?<![A-Za-z\d.])(\d[\d,]*(?:\.\d+)?)\s*(ms|km/s|km|MHz|GHz|kHz|dB|%|分鐘|小時|年|倍)?")
TERM_RE = re.compile(r"(?<![A-Za-z0-9])[A-Z][A-Z0-9]+(?![A-Za-z0-9])")
IGNORE_TERMS = {"II", "III", "IV", "PDF"}


def norm(n):
    return n.replace(",", "")


def numbers(text, with_unit=False):
    text = CITE_CARD.sub("", text)
    text = re.sub(r"\[[a-z0-9]+, p\.[^\]]*\]", "", text)      # wiki 出處 [id, p.X]
    text = re.sub(r"(?<=[A-Za-z])-?\d+", "", text)             # Rel-17、n255、SA2 這類編號
    out = []
    for n, u in NUM_UNIT.findall(text):
        out.append((norm(n), u) if with_unit else norm(n))
    return out


# ---------- A 覆蓋率 ----------
def stage_coverage(d):
    errs, all_pages, topic = [], set(), None
    groups = {}
    for line in (d / "sources.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            topic = line[3:]
            groups[topic] = []
        m = re.search(r"`(wiki/[\w/.-]+\.md)`", line)
        if m and topic:
            p = m.group(1)
            if not (ROOT / p).exists():
                errs.append(f"{topic}：頁面不存在 {p}")
            groups[topic].append(p)
            all_pages.add(p)
    for t, ps in groups.items():
        if len(ps) < 2:
            errs.append(f"{t}：只有 {len(ps)} 頁相關，少於 2 頁")
    if len(all_pages) < 3:
        errs.append(f"全部只有 {len(all_pages)} 頁相關，少於 3 頁 → 停下")
    print(f"子題 {len(groups)} 個，相關頁 {len(all_pages)} 頁")
    return errs


# ---------- C 逐頁稿 ----------
def load_cards(d):
    cards = {}
    for p in (d / "cards").glob("*.md"):
        facts = {}
        for line in p.read_text(encoding="utf-8").splitlines():
            m = re.match(r"- F(\d+)｜[^｜]*｜(.*)", line)
            if m:
                facts[int(m.group(1))] = m.group(2)
        cards[p.stem] = facts
    return cards


def disputed_pairs():
    """⚠️ 區塊中被否決的「說法」的（數字, 單位）。
    「目前結論」引用的來源＝被採用的說法，那些說法的數字可以用；
    其他說法的數字，只要沒出現在任何「目前結論」裡，就是爭議數字。"""
    claims, allowed = set(), set()
    cite_id = re.compile(r"\[([a-z0-9]+), p\.")
    for p in WIKI.rglob("*.md"):
        lines = p.read_text(encoding="utf-8").splitlines()
        for i, line in enumerate(lines):
            if not line.strip().startswith("> ⚠️"):
                continue
            block = []
            for b in lines[i + 1:]:
                if not b.strip().startswith(">"):
                    break
                block.append(b)
            concl = [b for b in block if "目前結論" in b]
            accepted = {x for b in concl for x in cite_id.findall(b)}
            for b in block:
                pairs = {x for x in numbers(b, True) if x[1]}
                if "目前結論" in b:
                    allowed |= pairs
                elif "說法" in b:
                    ids = set(cite_id.findall(b))
                    if ids and ids <= accepted:
                        allowed |= pairs
                    else:
                        claims |= pairs
    return claims - allowed


def parse_draft(p):
    text = p.read_text(encoding="utf-8")
    fm, body = {}, text
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    if m:
        body = m.group(2)
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
    return fm, body


def glossary():
    terms = {}
    for line in (WIKI / "glossary.md").read_text(encoding="utf-8").splitlines():
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) >= 5 and c[0] not in ("縮寫",) and not set(c[0]) <= set("-: "):
            for t in re.split(r"[／/、\s]+", c[0]):
                terms[t] = c[2]
    return terms


def stage_drafts(d):
    errs, warns = [], []
    cards = load_cards(d)
    bad_pairs = disputed_pairs()
    gl = glossary()
    drafts = sorted((d / "drafts").glob("*.md"))
    if not 8 <= len(drafts) <= 15:
        errs.append(f"頁數 {len(drafts)}，不在 8～15 頁")
    seen_terms, figures = set(), 0
    for p in drafts:
        fm, body = parse_draft(p)
        name = p.name
        if fm.get("figure", "none") != "none":
            figures += 1
        is_concept = fm.get("type", "content") == "content"
        if is_concept and not fm.get("analogy"):
            errs.append(f"{name}：缺少生活比喻（analogy）")
        text_all = fm.get("analogy", "") + "\n" + body
        prev_table = False
        for line in text_all.splitlines():
            s = line.strip()
            is_table = s.startswith("|")
            is_header = is_table and not prev_table  # 表格第一列是欄位名稱
            prev_table = is_table
            if not s or s.startswith("#"):
                continue
            if is_header:
                for t in TERM_RE.findall(s):
                    if t not in IGNORE_TERMS and t not in seen_terms:
                        seen_terms.add(t)
                        if not re.search(rf"（[^）]*{t}[^）]*）|{t}（", s):
                            errs.append(f"{name}：縮寫 {t} 第一次出現沒有附中文說明 → {s[:30]}")
                continue
            cites = CITE_CARD.findall(s)
            if fm.get("type") != "cover" and not cites:
                errs.append(f"{name}：沒有出處 → {s[:30]}")
                continue
            facts_txt = ""
            for c, f in cites:
                if c not in cards:
                    errs.append(f"{name}：卡片不存在 {c}")
                elif int(f) not in cards[c]:
                    errs.append(f"{name}：{c} 沒有 F{f}")
                else:
                    facts_txt += cards[c][int(f)] + " "
            fact_nums = set(numbers(facts_txt))
            for n in numbers(s):
                if cites and n not in fact_nums:
                    errs.append(f"{name}：數字 {n} 在引用的卡片裡找不到 → {s[:30]}")
            for n, u in numbers(s, True):
                if u and (n, u) in bad_pairs:
                    errs.append(f"{name}：{n} {u} 是 ⚠️ 爭議數字，必須用「目前結論」→ {s[:30]}")
            clean = CITE_CARD.sub("", s)
            for t in TERM_RE.findall(clean):
                if t in IGNORE_TERMS or t in seen_terms:
                    continue
                seen_terms.add(t)
                if not re.search(rf"（[^）]*{t}[^）]*）|{t}（", clean):
                    errs.append(f"{name}：縮寫 {t} 第一次出現沒有附中文說明 → {s[:30]}")
                if t not in gl and re.sub(r"\d+$", "", t) not in gl:
                    warns.append(f"{name}：{t} 不在術語表")
    if figures < 3:
        errs.append(f"示意圖只有 {figures} 張，少於 3 張")
    print(f"逐頁稿 {len(drafts)} 頁，示意圖 {figures} 張，爭議數字 {len(bad_pairs)} 組")
    for w in warns:
        print("   ⚠", w)
    return errs


# ---------- E 渲染 ----------
def stage_render(d):
    import subprocess, json
    js = ROOT / "scripts" / "render_check.js"
    r = subprocess.run(["node", str(js), str(d / "deck.html"), str(d / "shots")],
                       capture_output=True, text=True)
    if r.returncode != 0 and not r.stdout:
        return [f"渲染失敗：{r.stderr[:200]}"]
    res = json.loads(r.stdout)
    errs = []
    n = len(res)
    if not 8 <= n <= 15:
        errs.append(f"頁數 {n}，不在 8～15 頁")
    for s in res:
        if s["overflow"]:
            errs.append(f"第 {s['no']} 頁文字溢出（內容高 {s['h']}px > 版面 {s['box']}px）")
        if s["hscroll"]:
            errs.append(f"第 {s['no']} 頁有橫向溢出")
    print(f"渲染 {n} 頁，截圖放在 shots/")
    return errs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir")
    ap.add_argument("--stage", required=True, choices=["coverage", "drafts", "render"])
    a = ap.parse_args()
    d = ROOT / a.dir
    errs = {"coverage": stage_coverage, "drafts": stage_drafts, "render": stage_render}[a.stage](d)
    if errs:
        print(f"❌ 未通過：{len(errs)} 個問題")
        for e in errs:
            print("   -", e)
        sys.exit(1)
    print("✅ 通過")


if __name__ == "__main__":
    main()
