#!/usr/bin/env python3
"""② 證據卡：每張卡只讀一頁 wiki，把內容行原句照抄並編號（F1、F2…）。

用法：python3 scripts/make_cards.py slides/<slug>
讀 slides/<slug>/sources.md 列出的 wiki 頁，輸出到 slides/<slug>/cards/<卡片名>.md
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAV = {"和其他概念的關係", "延伸閱讀", "這份資料貢獻到的頁面", "基本資訊"}


def page_list(slide_dir):
    pages, in_topic = [], False
    for line in (slide_dir / "sources.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            in_topic = True  # 只讀子題底下列出的頁，說明文字裡提到的頁不算
        m = re.search(r"`(wiki/[\w/.-]+\.md)`", line)
        if in_topic and m and m.group(1) not in pages:
            pages.append(m.group(1))
    return pages


def facts(page_text):
    """回傳 (段落, 事實文字) 的清單；表格列轉成「欄名＝值」。"""
    out, section, header, in_code = [], "", None, False
    for line in page_text.splitlines():
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not s or s.startswith("> 類型："):
            continue
        if s.startswith("## "):
            section, header = s[3:], None
            continue
        if s.startswith("#"):
            header = None  # 小標題之後的表格是新表格，表頭要重新讀
            continue
        if section in NAV:
            continue
        if s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if set("".join(cells)) <= set("-: "):
                continue
            if header is None:
                header = cells
                continue
            pairs = [f"{h}＝{c}" for h, c in zip(header, cells)]
            out.append((section, "；".join(pairs)))
            continue
        header = None
        out.append((section, re.sub(r"^[-*>]\s*", "", s)))
    return out


def main():
    slide_dir = ROOT / sys.argv[1]
    (slide_dir / "cards").mkdir(exist_ok=True)
    for rel in page_list(slide_dir):
        text = (ROOT / rel).read_text(encoding="utf-8")
        title = text.splitlines()[0].lstrip("# ").strip()
        name = Path(rel).stem
        lines = [f"# 卡：{title}", "", f"> 來源頁：`{rel}`（只讀這一頁，原句照抄）", ""]
        for i, (sec, f) in enumerate(facts(text), 1):
            lines.append(f"- F{i}｜{sec}｜{f}")
        (slide_dir / "cards" / f"{name}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"cards/{name}.md：{i} 條事實")


if __name__ == "__main__":
    main()
