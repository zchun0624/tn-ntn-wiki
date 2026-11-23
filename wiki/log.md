# 操作紀錄

> 只增不刪。每筆開頭：`## [YYYY-MM-DD] 操作 | 對象`

## [2026-11-23] setup | 建立 wiki

- 經 10 題需求訪談後建立 AGENTS.md、資料夾與 lint 腳本。
- raw/ 放入 6 份資料：lin2021、3gpp2025、tutorial2024、figaro2026、ericsson2025、jeon2026。

## [2026-11-23] ingest | lin2021、3gpp2025（第一批，待檢查）

- 新增來源頁 2 頁、概念頁 10 頁、比較頁 3 頁、標準演進頁 1 頁、術語表 56 個縮寫。
- 發現 1 處說法不一致：HARQ 程序數 32 個夠不夠用（lin2021 vs 3gpp2025），已在 `concepts/harq-in-ntn.md` 標記，結論以 3GPP 為準。
- 撰寫時發現比較表有 4 格內容資料沒寫（MEO 延遲、GEO／MEO 需要的衛星數、部分版本年份），改成「（資料未提及）」，避免用自己的知識補。
- lint 第 1 次：4/6 通過。2 處粗體小標題被判定為沒有出處的內容行 → 改成 `###` 標題；7 個縮寫不在術語表（ASN、CT、F1、GPS、MCC、SA、SIB19）→ 補進術語表，MCC 改寫掉。
- lint 第 2 次：6/6 通過。
- 兩份資料共用大部分概念頁，所以一起 ingest；使用者檢查通過後 commit。

## [2026-11-23] ingest | tutorial2024

- 83 頁依 8 個章節分段讀完（參考文獻除外）。
- 新增來源頁 1 頁、概念頁 5 頁（3GPP 標準怎麼制定、AI 在 NTN 的應用、無人機與高空平台、NTN 的多重接取、RIS）；更新 7 頁（ntn、satellite-orbits、ntn-challenges、ntn-use-cases、tn-vs-ntn、geo-vs-meo-vs-leo、3gpp-ntn-releases）；術語表新增 18 個。
- 新增 3 處說法不一致：軌道高度（tutorial2024 vs 3gpp2025）、TN／NTN 誰比較常換手（tutorial2024 vs lin2021、3gpp2025）、GEO 來回時間（tutorial2024 自己前後不一）。
- 發現 tutorial2024 的 Fig. 2 把 n255 寫成 n225，記在來源頁，以內文為準。
- lint 第 1 次：4/6 通過（1 行沒有出處、22 個縮寫不在術語表）。
- 修改 lint 腳本：`RAN1`、`SA5` 這類「縮寫＋編號」，去掉結尾數字後在術語表找得到就算通過，避免每個編號都要收錄。
- lint 第 2 次：6/6 通過。

## [2026-11-23] ingest | figaro2026

- 新增來源頁 1 頁、概念頁 1 頁（NTN 的實際效能）、比較頁 1 頁（S-band vs Ka-band）；更新 11 頁；術語表新增 6 個、合併 FR1／FR2。
- 標準演進頁補上 Rel-14～Rel-18 的年份，新增 Rel-20。
- 新增 3 處說法不一致：Rel-17 日期（3 月 vs 6 月）、Ka-band 上下行剛好相反（tutorial2024 vs figaro2026）、無人機高度（500 m 以下 vs 9～11.5 km vs 3GPP 8～50 km）。
- 更新既有的 GEO 延遲矛盾：figaro2026 單程 120 ms × 2 ≈ 240 ms，和 tutorial2024 的 250 ms 接近，推測 500 ms 是含饋線鏈路。
- lint 第 1 次：5/6 通過（7 個縮寫不在術語表）；補上後 6/6 通過。

## [2026-11-23] ingest | ericsson2025

- 新增來源頁 1 頁、概念頁 1 頁（手機直連衛星）、比較頁 1 頁（未修改 4G vs NR-NTN）；更新 7 頁；術語表新增 6 個。
- 新增 2 處說法不一致：GEO 高度 35,768 km（ericsson2025，疑似筆誤）vs 35,786 km；LEO 速度 7.5 vs 7.8 km/s。軌道高度的矛盾區塊加入第 3 種說法（LEO 低到 180 km）。
- HARQ 的既有矛盾：ericsson2025 支持 3GPP 的說法（32 個程序與逐一關閉回饋兩者都有），加強了目前結論。
- lint 第 1 次：5/6 通過（6 個縮寫不在術語表）；補上後 6/6 通過。

## [2026-11-23] ingest | jeon2026

- 新增來源頁 1 頁、概念頁 1 頁（TN 和 NTN 怎麼整合）、比較頁 1 頁（ATSSS vs DualSteer）；更新 4 頁（tn-vs-ntn、ai-for-ntn、3gpp-ntn-releases、index）；術語表新增 11 個。
- 沒有發現新的說法不一致；jeon2026 補上 Rel-19 DualSteer，接續 3gpp2025「Rel-17 不要求同時連兩者」的說法，整理成整合方式的演進表。
- lint 第 1 次：5/6 通過（13 個詞不在術語表）。其中 EUCNC 是出現在裸網址裡的字串，屬於腳本誤判 → 修改 lint 腳本，掃術語前先去掉裸網址。
- lint 第 2 次：6/6 通過。6 份資料全部 ingest 完成。

## [2026-11-23] query | 教學簡報「衛星怎麼幫手機上網？」

- 依 `workflows/topic-slides.md` 產生 14 頁簡報，只使用 wiki 內容。完整紀錄見 `slides/tn-ntn-intro/report.md`。
- 簡報過程中發現 wiki 本身的一個問題：`concepts/satellite-orbits.md` 的內文仍寫 LEO 速度 7.5 km/s，和同頁 ⚠️ 目前結論（7.8 km/s）不一致。已記為待辦，下次 lint 時處理。
