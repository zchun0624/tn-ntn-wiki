# TN 和 NTN 怎麼整合（TN-NTN Integration）

> 類型：概念頁｜來源：jeon2026、3gpp2025、tutorial2024｜更新：2026-11-23

## 一句話白話解釋

手機同時有「地面」和「衛星」兩條路可以走：地面快、容量大，衛星涵蓋廣；整合的重點是在對的時間，把對的人分到對的路上 [jeon2026, p.1]。

## 詳細說明

### 為什麼要整合

- 地面網路容量大、延遲低；LEO 衛星的 NTN 能覆蓋沒有地面設施的地方，兩者互補 [jeon2026, p.1]。
- 3GPP 要求 5G 支援地面與衛星接取之間的服務連續性，也要能同時使用兩種接取 [3gpp2025, p.12–13]。

### 整合方式的演進

| 階段 | 做法 | 出處 |
|---|---|---|
| Rel-16 研究 | 研究 NTN-TN 服務連續性，以及一個 UE 同時由 NTN 和 TN 服務的多重連線情境 | [3gpp2025, p.10] |
| Rel-17 | UE 可以在 NTN 和 TN 之間換手，但不要求同時連到兩者 | [3gpp2025, p.16] |
| Rel-18 | 加強 NTN-TN 移動性，例如在系統資訊中廣播地面網路區域 | [3gpp2025, p.21] |
| Rel-19 | DualSteer：UE 用兩張 USIM 同時維持 TN 與 NTN 兩個連線 | [jeon2026, p.1] |

- 業界整合 TN 與 NTN 的方式包括漫遊、共用核心網的多重連線、RAN 共享等，不同方式能共享的資訊不同 [tutorial2024, p.21]。

### DualSteer 怎麼運作

- 每個 UE 有兩張 USIM，各自建立一個 PDU 連線，兩個連線綁成一個 DualSteer 連線群組（DSG）[jeon2026, p.1]。
- 只能導引和切換，不能分流：同一時間，每個 UE 的流量只走一條路徑 [jeon2026, p.1]。
- PCF 下發規則給 SMF，SMF 再轉成給 UE 的 DualSteer Rule 和給 H-UPF 的 N4 rule，規則裡寫明導引模式和門檻 [jeon2026, p.2]。
- UE 和 H-UPF 透過 PMFP 定期探測兩條路徑（包含沒在用的那條），取得即時 PLR 與 RTT [jeon2026, p.1]。

### 三種規則式導引模式

| 模式 | 做法 | 出處 |
|---|---|---|
| Active-Standby | 一條主用、一條備用，主路徑不能用時才切換 | [jeon2026, p.1] |
| Smallest Delay | 選 RTT 較小的路徑 | [jeon2026, p.1] |
| Priority-Based | 依優先順序與門檻選擇 | [jeon2026, p.1] |

- **問題**：三種模式都是每個 UE 各自選，不管別人；地面延遲永遠比衛星短，Smallest Delay 會把大多數 UE 都丟到地面，造成回程壅塞 [jeon2026, p.1]。

### 研究範例：用強化學習導引

- jeon2026 用集中式 DQN 一次決定所有 UE 的路徑，在地面塞車前先把部分 UE 分流到衛星 [jeon2026, p.2]。
- 8 個 UE 時，PLR 從 Smallest Delay 的 9.5% 降到 2.0%，RTT 3.9 ms [jeon2026, p.5]。
- 關鍵觀念：把 NTN 當成「主動分擔負載的資源」，而不只是備援；多幾毫秒延遲，就能換來大幅降低封包遺失 [jeon2026, p.1]。

## 和其他概念的關係

- [ATSSS 和 DualSteer 比較](../comparisons/atsss-vs-dualsteer.md)：兩種多重接取架構的差別
- [NTN 的移動性管理](ntn-mobility.md)：Rel-17 的 TN-NTN 換手
- [AI 在 NTN 的應用](ai-for-ntn.md)：強化學習的其他應用
- [TN 和 NTN 比較](../comparisons/tn-vs-ntn.md)：兩者的特性差異

## 延伸閱讀

- [jeon2026](../sources/jeon2026.md)
- [3gpp2025](../sources/3gpp2025.md)
- [tutorial2024](../sources/tutorial2024.md)
