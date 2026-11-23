# TN-NTN Wiki 目錄

> 地面網路（TN）與非地面網路（NTN）的知識庫。讀者：實驗室學弟妹與同學。規則見 [AGENTS.md](../AGENTS.md)。

## 建議閱讀順序

1. [非地面網路（NTN）](concepts/ntn.md)：NTN 是什麼
2. [TN 和 NTN 比較](comparisons/tn-vs-ntn.md)：和地面網路差在哪
3. [NTN 的系統架構](concepts/ntn-architecture.md)：由哪些元件組成
4. [3GPP NTN 標準演進](timeline/3gpp-ntn-releases.md)：標準怎麼一步步完成
5. [TN 和 NTN 怎麼整合](concepts/tn-ntn-integration.md)：地面和衛星一起用

## 概念頁

- [非地面網路（NTN）](concepts/ntn.md)：定義與種類（衛星、高空平台、空對地）
- [衛星軌道](concepts/satellite-orbits.md)：LEO、MEO、GEO、HEO
- [NTN 的系統架構](concepts/ntn-architecture.md)：服務鏈路、饋線鏈路、閘道站
- [NTN 和地面網路不一樣的地方](concepts/ntn-challenges.md)：延遲、都卜勒、移動的細胞
- [時序提前與都卜勒預補償](concepts/timing-advance-and-doppler.md)：UE 怎麼用 GNSS 對準時間與頻率
- [NTN 的 HARQ](concepts/harq-in-ntn.md)：長延遲下的重傳機制
- [NTN 的移動性管理](concepts/ntn-mobility.md)：衛星一直在動時怎麼換手
- [NTN 的應用情境](concepts/ntn-use-cases.md)：NTN 用在哪裡
- [IoT NTN](concepts/iot-ntn.md)：物聯網裝置透過衛星連線
- [跨國覆蓋與 UE 位置](concepts/ue-location-and-regulation.md)：衛星覆蓋跨國時的法規問題
- [3GPP 標準怎麼制定](concepts/3gpp-standardization.md)：TSG、WG、SI／WI、TR／TS、Release
- [AI 在 NTN 的應用](concepts/ai-for-ntn.md)：用 AI 管理複雜的衛星與地面網路
- [無人機與高空平台](concepts/uav-and-haps.md)：空中基地台與空中回程
- [NTN 的多重接取](concepts/multiple-access-in-ntn.md)：OMA、NOMA、SDMA、RSMA
- [可重構智慧表面（RIS）](concepts/ris-in-ntn.md)：可程式化的智慧反射面
- [NTN 的實際效能](concepts/ntn-performance.md)：LEO／GEO、S／Ka-band 的模擬結果
- [手機直連衛星（D2D）](concepts/direct-to-device.md)：一般手機直接連衛星
- [TN 和 NTN 怎麼整合](concepts/tn-ntn-integration.md)：從換手到 DualSteer 同時連線

## 比較頁

- [TN 和 NTN 比較](comparisons/tn-vs-ntn.md)：地面網路 vs 非地面網路
- [GEO、MEO、LEO 比較](comparisons/geo-vs-meo-vs-leo.md)：三種衛星軌道
- [透明式和再生式酬載比較](comparisons/transparent-vs-regenerative-payload.md)：衛星是鏡子還是基地台
- [S-band 和 Ka-band 比較](comparisons/s-band-vs-ka-band.md)：低頻穩定 vs 高頻快速
- [未修改 4G 和 NR-NTN 比較](comparisons/unmodified-4g-vs-nr-ntn.md)：兩種手機直連衛星的做法
- [ATSSS 和 DualSteer 比較](comparisons/atsss-vs-dualsteer.md)：兩種多重接取架構

## 標準演進頁

- [3GPP NTN 標準演進](timeline/3gpp-ntn-releases.md)：Rel-14 到 Rel-20

## 來源頁

- [lin2021](sources/lin2021.md)：5G from Space，3GPP NTN 概論（2021）
- [3gpp2025](sources/3gpp2025.md)：3GPP 官方 NTN 概論（2025 更新）
- [tutorial2024](sources/tutorial2024.md)：NTN 教學文，含 6G 研究方向（2024）
- [figaro2026](sources/figaro2026.md)：Rel-17～Rel-20 最新進展與模擬（2026）
- [ericsson2025](sources/ericsson2025.md)：衛星直連手機的兩種做法（2025）
- [jeon2026](sources/jeon2026.md)：用強化學習做 DualSteer 流量導引（2026）

## 其他

- [術語表](glossary.md)：所有縮寫與白話解釋
- [操作紀錄](log.md)：ingest 與 lint 的紀錄
