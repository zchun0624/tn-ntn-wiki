# TN-NTN LLM Wiki

依 Karpathy 的 LLM Wiki 構想建立的「地面網路（TN）與非地面網路（NTN）」知識庫，並用它產生教學 HTML 簡報。

- 🔗 網站：https://zchun0624.github.io/tn-ntn-wiki/
- 📚 Wiki 目錄：[`wiki/index.md`](wiki/index.md)
- ▶ 教學簡報：[`slides/tn-ntn-intro/deck.html`](slides/tn-ntn-intro/deck.html)
- ✅ 檢查報告：[`slides/tn-ntn-intro/report.md`](slides/tn-ntn-intro/report.md)

| 路徑 | 內容 |
|---|---|
| `AGENTS.md` | wiki 規則（經 10 題需求訪談後建立）；`CLAUDE.md` 只寫 `@AGENTS.md` |
| `raw/sources.md` | 6 份原始資料清單（PDF 不上傳，依網址取得） |
| `wiki/` | 34 頁：概念頁、比較頁、標準演進頁、來源頁、術語表、操作紀錄 |
| `workflows/topic-slides.md` | 主題 → 簡報的 graph |
| `scripts/lint.py` | wiki 的 6 項檢查 |
| `scripts/make_cards.py`、`check_slides.py`、`build_deck.py`、`render_check.js` | 簡報流程的節點與檢查關卡 |
| `slides/tn-ntn-intro/` | 一次實際執行的所有中間產物：sources、cards、outline、drafts、deck、report |

本機檢查：`python3 scripts/lint.py`、`python3 scripts/check_slides.py slides/tn-ntn-intro --stage drafts`
