#!/usr/bin/env python3
"""TN-NTN Wiki 健康檢查（AGENTS.md 第 4 節的 6 項 lint）。

用法：python3 scripts/lint.py
全部通過時 exit code 為 0，有任何錯誤時為 1。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
SOURCES_MD = ROOT / "raw" / "sources.md"

# 不需要出處的導覽段落（AGENTS.md 第 6 節）
NAV_SECTIONS = {"和其他概念的關係", "延伸閱讀", "這份資料貢獻到的頁面", "基本資訊"}
# 不需要出處的整頁
NO_CITE_PAGES = {"index.md", "log.md"}
# 不算縮寫的大寫字（羅馬數字、檔案格式）
IGNORE_TERMS = {"II", "III", "IV", "VI", "VII", "VIII", "IX", "XI", "XII", "PDF", "URL"}
PLAIN_MAX = 100

CITE_RE = re.compile(r"\[([a-z0-9]+), p\.\s?(\d+)(?:[–-](\d+))?[^\]]*\]")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
TERM_RE = re.compile(r"(?<![A-Za-z0-9])[A-Z][A-Z0-9]+(?![A-Za-z0-9])")


def load_sources():
    """讀 raw/sources.md，回傳 {id: PDF 頁數}。"""
    sources = {}
    for line in SOURCES_MD.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 6 or cells[0] in ("id", "") or set(cells[0]) <= set("-"):
            continue
        m = re.match(r"(\d+)", cells[5])
        sources[cells[0]] = int(m.group(1)) if m else None
    return sources


def wiki_pages():
    return sorted(p for p in WIKI.rglob("*.md"))


def rel(p):
    return p.relative_to(ROOT).as_posix()


def content_lines(text):
    """逐行回傳 (行號, 所在 H2 段落, 內容)，跳過程式碼區塊。"""
    section, in_code = "", False
    for no, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if line.startswith("## "):
            section = line[3:].strip()
        yield no, section, line


def needs_citation(no, section, line):
    s = line.strip()
    if not s or s.startswith("#") or s.startswith("> 類型："):  # 空行、標題、後設資料行
        return False
    if section in NAV_SECTIONS:
        return False
    if re.fullmatch(r"\|?[\s:|-]+\|?", s):  # 表格分隔列
        return False
    if s.startswith("> ⚠️") or "可能原因" in s:
        return False
    return True


def check_citations(pages, sources):
    errors = []
    for p in pages:
        if p.name in NO_CITE_PAGES:
            continue
        lines = list(content_lines(p.read_text(encoding="utf-8")))
        header_rows = set()
        for i, (no, sec, line) in enumerate(lines):  # 表頭＝分隔列的上一列
            if re.fullmatch(r"\|?[\s:|-]+\|?", line.strip()) and i > 0:
                header_rows.add(lines[i - 1][0])
        for no, sec, line in lines:
            if no in header_rows or not needs_citation(no, sec, line):
                continue
            cites = CITE_RE.findall(line)
            if not cites:
                errors.append(f"{rel(p)}:{no} 沒有出處：{line.strip()[:40]}")
            for sid, a, b in cites:
                if sid not in sources:
                    errors.append(f"{rel(p)}:{no} 來源 id 不存在：{sid}")
                elif sources[sid] and int(b or a) > sources[sid]:
                    errors.append(f"{rel(p)}:{no} 頁碼超出範圍：{sid} 只有 {sources[sid]} 頁")
    return errors


def resolve_links(p):
    text = p.read_text(encoding="utf-8")
    for no, line in enumerate(text.splitlines(), 1):
        for target in LINK_RE.findall(line):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            yield no, target, (p.parent / target.split("#")[0]).resolve()


def check_links(pages):
    return [f"{rel(p)}:{no} 連結斷掉：{t}"
            for p in pages for no, t, path in resolve_links(p) if not path.exists()]


def check_orphans(pages):
    index = WIKI / "index.md"
    listed = {path for _, _, path in resolve_links(index)}
    errors = []
    for p in pages:
        if p.parent.name in ("concepts", "sources", "comparisons", "timeline") and p.resolve() not in listed:
            errors.append(f"{rel(p)} 沒有列在 index.md（孤兒頁）")
    return errors


def check_conflicts(pages):
    errors = []
    for p in pages:
        lines = p.read_text(encoding="utf-8").splitlines()
        for i, line in enumerate(lines):
            if not line.strip().startswith("> ⚠️"):
                continue
            block = []
            for nxt in lines[i + 1:]:
                if not nxt.strip().startswith(">"):
                    break
                block.append(nxt)
            ids = {sid for b in block for sid, _, _ in CITE_RE.findall(b)}
            if len(ids) < 2:
                errors.append(f"{rel(p)}:{i + 1} ⚠️ 區塊少於 2 個不同來源")
            if not any("目前結論" in b for b in block):
                errors.append(f"{rel(p)}:{i + 1} ⚠️ 區塊缺少「目前結論」")
    return errors


def glossary_terms():
    terms = set()
    for line in (WIKI / "glossary.md").read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 5 and cells[0] not in ("縮寫", "") and not set(cells[0]) <= set("-: "):
            for t in re.split(r"[／/、,\s]+", cells[0]):
                if t:
                    terms.add(t)
    return terms


def check_terms(pages):
    known = glossary_terms()
    missing = {}
    for p in pages:
        if p.name in ("glossary.md", "log.md", "index.md"):
            continue
        for no, sec, line in content_lines(p.read_text(encoding="utf-8")):
            clean = CITE_RE.sub("", line)
            clean = re.sub(r"\]\([^)]*\)", "]", clean)   # 去掉連結網址
            clean = re.sub(r"`[^`]*`", "", clean)        # 去掉行內程式碼
            clean = re.sub(r"https?://\S+", "", clean)   # 去掉裸網址
            for t in TERM_RE.findall(clean):
                base = re.sub(r"\d+$", "", t)  # RAN1、SA5 → RAN、SA
                if t not in known and base not in known and t not in IGNORE_TERMS:
                    missing.setdefault(t, f"{rel(p)}:{no}")
    return [f"{t} 不在術語表（第一次出現：{where}）" for t, where in sorted(missing.items())]


def check_plain(pages):
    errors = []
    for p in pages:
        if p.parent.name != "concepts":
            continue
        body, grab = [], False
        for no, sec, line in content_lines(p.read_text(encoding="utf-8")):
            if line.startswith("## "):
                grab = line.strip() == "## 一句話白話解釋"
                continue
            if grab and line.strip():
                body.append(line.strip())
        if not body:
            errors.append(f"{rel(p)} 缺少「一句話白話解釋」")
            continue
        text = CITE_RE.sub("", "".join(body))
        text = re.sub(r"[*_`>]", "", text).strip()
        if len(text) > PLAIN_MAX:
            errors.append(f"{rel(p)} 白話解釋 {len(text)} 字，超過 {PLAIN_MAX} 字")
    return errors


def main():
    sources = load_sources()
    pages = wiki_pages()
    checks = [
        ("出處", check_citations(pages, sources)),
        ("連結", check_links(pages)),
        ("孤兒頁", check_orphans(pages)),
        ("矛盾標記", check_conflicts(pages)),
        ("術語", check_terms(pages)),
        ("白話解釋", check_plain(pages)),
    ]
    print(f"TN-NTN Wiki lint：{len(pages)} 頁，{len(sources)} 份來源\n")
    failed = 0
    for name, errs in checks:
        mark = "✅" if not errs else "❌"
        print(f"{mark} {name}：{'通過' if not errs else f'{len(errs)} 個問題'}")
        for e in errs[:30]:
            print(f"   - {e}")
        if len(errs) > 30:
            print(f"   …還有 {len(errs) - 30} 個")
        failed += bool(errs)
    print(f"\n結果：{6 - failed}/6 項通過")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
