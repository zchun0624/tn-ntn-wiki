# 卡：ATSSS 和 DualSteer 比較（ATSSS vs DualSteer）

> 來源頁：`wiki/comparisons/atsss-vs-dualsteer.md`（只讀這一頁，原句照抄）

- F1｜一句話差別｜ATSSS 管的是「行動網路＋Wi-Fi」這種一張 SIM 卡的多重接取；DualSteer 管的是「兩個 3GPP 網路」（例如地面＋衛星），用兩張 SIM 卡同時連線 [jeon2026, p.1]。
- F2｜比較表｜項目＝管理的接取；ATSSS＝3GPP 與非 3GPP（例如 NR 和 Wi-Fi）；DualSteer＝兩個 3GPP 接取網路（例如 TN 和 NTN）；出處＝[jeon2026, p.1]
- F3｜比較表｜項目＝用戶身分；ATSSS＝單一用戶身分；DualSteer＝兩張 USIM，各自獨立的用戶身分；出處＝[jeon2026, p.1]
- F4｜比較表｜項目＝連線；ATSSS＝一個多重接取 PDU 連線；DualSteer＝兩個 PDU 連線，綁成 DSG；出處＝[jeon2026, p.1]
- F5｜比較表｜項目＝導引／切換／分流；ATSSS＝名稱即包含三者（Steering, Switching and Splitting）；DualSteer＝只支援導引和切換，不支援分流；出處＝[jeon2026, p.1]
- F6｜比較表｜項目＝導引規則；ATSSS＝定義 Active-Standby、Smallest Delay、Priority-Based 等規則；DualSteer＝沿用 ATSSS 的三種規則；出處＝[jeon2026, p.1]
- F7｜比較表｜項目＝標準版本；ATSSS＝既有框架；DualSteer＝Rel-19；出處＝[jeon2026, p.1]
- F8｜什麼時候用哪一個｜手機同時用行動網路和 Wi-Fi：ATSSS [jeon2026, p.1]。
- F9｜什麼時候用哪一個｜手機同時用地面網路和衛星網路：DualSteer [jeon2026, p.1]。
- F10｜什麼時候用哪一個｜因為 DualSteer 不能分流，每個 UE 只能整個走某一條路，所以「哪些 UE 走哪條路」的分配決策特別重要 [jeon2026, p.1–2]。
