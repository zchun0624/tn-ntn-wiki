# 衛星軌道（Satellite Orbits）

> 類型：概念頁｜來源：3gpp2025、lin2021、tutorial2024、ericsson2025｜更新：2026-11-23

## 一句話白話解釋

衛星飛得越低，訊號來回越快、越省電，但每顆衛星看到的地面範圍越小，需要越多顆才能涵蓋全球 [3gpp2025, p.2]。

## 詳細說明

| 軌道 | 高度 | 特性 | 出處 |
|---|---|---|---|
| 低軌（Low Earth Orbit, LEO） | 約 500～2,000 km | 延遲較低、鏈路預算較好，但需要較多衛星才能涵蓋 | [3gpp2025, p.2] |
| 中軌（Medium Earth Orbit, MEO） | 約 8,000～20,000 km | 介於 LEO 和 GEO 之間 | [3gpp2025, p.2] |
| 同步軌道（Geostationary Earth Orbit, GEO） | 赤道上空 35,786 km | 繞行週期和地球自轉相同，從地面看好像靜止不動 | [3gpp2025, p.38] |
| 高橢圓軌道（Highly Elliptical Orbit, HEO） | 橢圓軌道 | — | [3gpp2025, p.2] |

- LEO 繞地球一圈約 88 分鐘（500 km）到 127 分鐘（2,000 km）[3gpp2025, p.38]。
- LEO 和 MEO 合稱非同步軌道（Non-Geostationary Satellite Orbit, NGSO），繞行週期約 1.5～10 小時，必須用多顆衛星組成星系，搭配換手才能維持服務 [3gpp2025, p.38]。
- 即使是 GEO，衛星也會因重力影響在標稱位置附近幾公里內移動 [3gpp2025, p.2]。
- 近年 Starlink、Kuiper、OneWeb 等大型 LEO 星系，讓 LEO 寬頻再度受到重視 [lin2021, p.1]。
- LEO 衛星移動速度約 7.5 km/s [tutorial2024, p.45]，從地平線一端飛到另一端只要 5～10 分鐘，所以地面使用者被同一顆衛星服務的時間很短 [tutorial2024, p.63]。
- 三顆位置適當的 GEO 衛星就能涵蓋幾乎全球 [ericsson2025, p.2]。

> ⚠️ 說法不一致
> - 說法 A：GEO 高度 35,786 km [3gpp2025, p.2]、[figaro2026, p.5]。
> - 說法 B：GEO 高度 35,768 km [ericsson2025, p.2]。
> - 可能原因：數字只差在兩位數字的順序，ericsson2025 很可能是筆誤。
> - 目前結論：以 3GPP 官方為準，35,786 km [3gpp2025, p.2]。

> ⚠️ 說法不一致
> - 說法 A：LEO 衛星速度約 7.5 km/s [tutorial2024, p.45]。
> - 說法 B：LEO 衛星速度約 7.8 km/s，繞一圈約 90 分鐘 [ericsson2025, p.2]。
> - 可能原因：衛星速度和高度有關，兩份資料都寫「約」，假設的高度可能不同。
> - 目前結論：3GPP 官方沒有寫速度，依規則以最新的 ericsson2025 為準，寫「約 7.8 km/s」，並說明會隨高度改變 [ericsson2025, p.2]。

- LEO 衛星壽命約 5～10 年，業者必須持續汰換與擴充星系 [tutorial2024, p.64]。

> ⚠️ 說法不一致
> - 說法 A：LEO 約 500～2,000 km，MEO 約 8,000～20,000 km [3gpp2025, p.2]。
> - 說法 B：LEO 約 300～1,500 km，MEO 約 7,000～25,000 km [tutorial2024, p.4, Fig. 1]。
> - 說法 C：LEO 在 2,000 km 以下，有時低到 180 km [ericsson2025, p.2]。
> - 可能原因：tutorial2024 的數字出自示意圖，沒有說明定義來源；ericsson2025 描述的是實際部署（有些商用衛星飛得更低）；3gpp2025 是官方定義。
> - 目前結論：以 3GPP 官方為準，LEO 約 500～2,000 km、MEO 約 8,000～20,000 km [3gpp2025, p.2]。

## 和其他概念的關係

- [GEO、MEO、LEO 比較](../comparisons/geo-vs-meo-vs-leo.md)：三種軌道的完整比較表
- [NTN 和地面網路不一樣的地方](ntn-challenges.md)：軌道高度決定延遲和都卜勒大小
- [NTN 的移動性管理](ntn-mobility.md)：NGSO 衛星一直在動，所以需要換手

## 延伸閱讀

- [3gpp2025](../sources/3gpp2025.md)
- [lin2021](../sources/lin2021.md)
- [tutorial2024](../sources/tutorial2024.md)
- [ericsson2025](../sources/ericsson2025.md)
