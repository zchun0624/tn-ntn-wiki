# 5G NR 非地面網路：從早期成果到未來方向（figaro2026）

> 類型：來源頁｜來源：figaro2026｜更新：2026-11-23

## 基本資訊

- 標題：5G NR Non-Terrestrial Networks: From Early Results to the Road Ahead
- 作者：Mattia Figaro、Francesco Rossato、Marco Giordani 等（帕多瓦大學、Toyota North America）
- 年份：2026（npj Wireless Communications；arXiv 2601.04882）
- 類型：論文（標準概論＋模擬評估）
- 網址：https://arxiv.org/abs/2601.04882

## 一句話總結

整理 3GPP NR-NTN 從 Rel-17 到 Rel-20 的最新進展，並用 ns-3 模擬比較 LEO／GEO、S-band／Ka-band 的端到端效能 [figaro2026, p.1–2]。

## 重點

- NTN 架構元件：地面 UE、空中／太空站、地面閘道站、服務鏈路、饋線鏈路 [figaro2026, p.2]。
- 透明式又稱「放大轉送」，再生式又稱「解碼轉送」；再生式支援衛星間鏈路 [figaro2026, p.2–3]。
- 整理各版本日期：Rel-15（2019 年 6 月）、Rel-16（2020 年 7 月）、Rel-17（2022 年 3 月）、Rel-18（2024 年 6 月）、Rel-20 目標 2027 年 3 月 [figaro2026, p.3–4]。
- Rel-17 假設 UE 有 GNSS，但在室內、地下等 GNSS 收訊差的地方不適用 [figaro2026, p.4]。
- Rel-20 要研究 GNSS 受干擾或欺騙時，NTN 怎麼繼續運作，並開始討論 6G 的地面與非地面整合設計 [figaro2026, p.4–5]。
- 模擬結果：在 Ka-band 下，GEO 的最大吞吐量比 LEO 高 50%；作者說明這主要是 3GPP 參數設定的結果，不是軌道本身造成的 [figaro2026, p.6]。
- GEO 的單程傳播延遲約 120 ms，LEO（600 km）約 2 ms [figaro2026, p.7]。
- Ka-band 頻寬大（400 MHz），通道容量約 390 Mbps；S-band 只有 30 MHz，約 125 Mbps，但傳播條件較好、較不受天氣影響 [figaro2026, p.7]。
- 限制：模擬只有單一 UE、靜止、UDP 流量，沒有考慮換手 [figaro2026, p.7]。

## 這份資料貢獻到的頁面

- [NTN 的系統架構](../concepts/ntn-architecture.md)
- [NTN 和地面網路不一樣的地方](../concepts/ntn-challenges.md)
- [時序提前與都卜勒預補償](../concepts/timing-advance-and-doppler.md)
- [NTN 的移動性管理](../concepts/ntn-mobility.md)
- [IoT NTN](../concepts/iot-ntn.md)
- [跨國覆蓋與 UE 位置](../concepts/ue-location-and-regulation.md)
- [無人機與高空平台](../concepts/uav-and-haps.md)
- [NTN 的實際效能](../concepts/ntn-performance.md)
- [S-band 和 Ka-band 比較](../comparisons/s-band-vs-ka-band.md)
- [GEO、MEO、LEO 比較](../comparisons/geo-vs-meo-vs-leo.md)
- [透明式和再生式酬載比較](../comparisons/transparent-vs-regenerative-payload.md)
- [3GPP NTN 標準演進](../timeline/3gpp-ntn-releases.md)
