# ATSSS 和 DualSteer 比較（ATSSS vs DualSteer）

> 類型：比較頁｜來源：jeon2026｜更新：2026-11-23

## 一句話差別

ATSSS 管的是「行動網路＋Wi-Fi」這種一張 SIM 卡的多重接取；DualSteer 管的是「兩個 3GPP 網路」（例如地面＋衛星），用兩張 SIM 卡同時連線 [jeon2026, p.1]。

## 比較表

| 項目 | ATSSS | DualSteer | 出處 |
|---|---|---|---|
| 管理的接取 | 3GPP 與非 3GPP（例如 NR 和 Wi-Fi） | 兩個 3GPP 接取網路（例如 TN 和 NTN） | [jeon2026, p.1] |
| 用戶身分 | 單一用戶身分 | 兩張 USIM，各自獨立的用戶身分 | [jeon2026, p.1] |
| 連線 | 一個多重接取 PDU 連線 | 兩個 PDU 連線，綁成 DSG | [jeon2026, p.1] |
| 導引／切換／分流 | 名稱即包含三者（Steering, Switching and Splitting） | 只支援導引和切換，不支援分流 | [jeon2026, p.1] |
| 導引規則 | 定義 Active-Standby、Smallest Delay、Priority-Based 等規則 | 沿用 ATSSS 的三種規則 | [jeon2026, p.1] |
| 標準版本 | 既有框架 | Rel-19 | [jeon2026, p.1] |

## 什麼時候用哪一個

- 手機同時用行動網路和 Wi-Fi：ATSSS [jeon2026, p.1]。
- 手機同時用地面網路和衛星網路：DualSteer [jeon2026, p.1]。
- 因為 DualSteer 不能分流，每個 UE 只能整個走某一條路，所以「哪些 UE 走哪條路」的分配決策特別重要 [jeon2026, p.1–2]。
