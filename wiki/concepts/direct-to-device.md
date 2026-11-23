# 手機直連衛星（Direct-to-Device, D2D）

> 類型：概念頁｜來源：ericsson2025、tutorial2024｜更新：2026-11-23

## 一句話白話解釋

不用額外買衛星電話，你口袋裡的手機就能在沒有基地台的山上或海上，直接連到天上的衛星傳簡訊 [ericsson2025, p.2–3]。

## 詳細說明

- **為什麼現在做得到**：可重複使用的火箭降低發射成本，窄點波束天線提升訊號強度，衛星上的晶片也能執行 RAN 功能與衛星間鏈路 [ericsson2025, p.2]。
- **3GPP 的進展**：Rel-17 推出 NR-NTN 與 IoT-NTN；之後已有支援 IoT-NTN 的手機和穿戴裝置商用，主要用於緊急訊息 [ericsson2025, p.2]。
- **早期案例**：部分業者用 LEO 衛星直接發送標準 4G LTE 訊號給現有手機，曾在颶風災害時用於緊急警報和簡訊 [ericsson2025, p.3]。
- **兩種做法**：「未修改 4G」和「NR-NTN」，詳見[兩種直連做法比較](../comparisons/unmodified-4g-vs-nr-ntn.md) [ericsson2025, p.3]。

### 頻譜從哪裡來

| 模式 | 做法 | 優缺點 | 出處 |
|---|---|---|---|
| 地面行動頻譜 | 衛星業者（SNO）和電信業者（MNO）合作，使用電信業者的頻譜 | 可以用現有手機；但不能干擾地面網路、也不受保護，需要設定排除區，只有少數國家允許 | [ericsson2025, p.3] |
| 行動衛星服務（MSS）頻譜 | 使用 ITU 分配給衛星的 L、S 頻段 | 國際法規成熟、干擾風險低、有 3GPP 規格；但支援的手機還很少 | [ericsson2025, p.3–4] |

- ITU-R 正在考慮在 700～2,700 MHz 新增 MSS 頻段，於 2027 年世界無線電大會（WRC-27）討論 [ericsson2025, p.3]。

### 未來

- 6G 預計一開始就內建 NTN 支援，包括不依賴 GNSS 的運作，以及多種無線技術共享頻譜 [ericsson2025, p.6]。

## 和其他概念的關係

- [未修改 4G 和 NR-NTN 兩種直連做法比較](../comparisons/unmodified-4g-vs-nr-ntn.md)：兩種做法的詳細比較
- [時序提前與都卜勒預補償](timing-advance-and-doppler.md)：兩種做法最大的差別在誰來補償
- [NTN 的應用情境](ntn-use-cases.md)：緊急簡訊是 D2D 最早的應用
- [IoT NTN](iot-ntn.md)：NB-IoT 也開始進入手機

## 延伸閱讀

- [ericsson2025](../sources/ericsson2025.md)
- [tutorial2024](../sources/tutorial2024.md)
