# NTN 的系統架構（NTN Architecture）

> 類型：概念頁｜來源：lin2021、3gpp2025、figaro2026｜更新：2026-11-23

## 一句話白話解釋

手機先連到天上的衛星，衛星再把訊號轉給地面的閘道站，閘道站接到一般的 5G 核心網，跟平常上網走的是同一套後端 [lin2021, p.3]。

## 詳細說明

- **基本路徑**（透明式酬載）：5G 核心網（5GC）透過 NG 介面連到地面的基地台（gNB），gNB 連到 NTN 閘道站，閘道站經由饋線鏈路（feeder link）連到衛星上的 NTN 酬載，酬載再經由服務鏈路（service link）用 Uu 介面連到 UE [lin2021, p.3]。
- **服務鏈路**：終端（手機、IoT 裝置或 VSAT）和空中／太空平台之間的鏈路，也叫 user link [3gpp2025, p.4]。
- **饋線鏈路**：NTN 閘道站和衛星之間的鏈路，也叫衛星無線介面（Satellite Radio Interface, SRI）[3gpp2025, p.5]。
- **NTN 閘道站**：位在地面、經由饋線鏈路連到 NTN 酬載的地面站 [3gpp2025, p.38]。閘道站經由 NG 介面連到 5G 核心網，經由 N6 介面連到公共網際網路 [figaro2026, p.2]。
- **基地台放在哪裡**：透明式酬載時，閘道站端的地面設備就是 gNB，衛星只是遠端射頻頭；再生式酬載時，gNB 在衛星上，閘道站只是連到核心網的路由器 [3gpp2025, p.4–5]。詳見[透明式和再生式酬載比較](../comparisons/transparent-vs-regenerative-payload.md) [3gpp2025, p.2]。
- **拆分架構**：gNB 可以拆成 DU 放在衛星上、CU 留在地面，饋線鏈路傳 F1 協定；多顆衛星上的 DU 可以接到同一個地面 CU [3gpp2025, p.10]。
- **衛星間鏈路（Inter-Satellite Link, ISL）**：衛星之間的傳輸鏈路，必須是再生式酬載才能使用 [3gpp2025, p.5]。
- **間接接取**：衛星也可以先連到地面的中繼節點（例如 VSAT），再由中繼節點服務附近的 UE [3gpp2025, p.4]。
- **波束**：分成跟著衛星移動的「移動波束」，以及用波束成形對準地面固定點的「地球固定波束」[3gpp2025, p.5]。Rel-17 支援地球固定、準地球固定、隨地球移動三種細胞 [figaro2026, p.4]。

## 和其他概念的關係

- [非地面網路（NTN）](ntn.md)：NTN 的定義與種類
- [透明式和再生式酬載比較](../comparisons/transparent-vs-regenerative-payload.md)：架構中最重要的選擇
- [NTN 的移動性管理](ntn-mobility.md)：衛星移動時，饋線和服務鏈路都要切換

## 延伸閱讀

- [lin2021](../sources/lin2021.md)
- [3gpp2025](../sources/3gpp2025.md)
- [figaro2026](../sources/figaro2026.md)
