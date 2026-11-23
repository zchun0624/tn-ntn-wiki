# ③ 大綱：衛星怎麼幫手機上網？——地面網路與非地面網路入門

> 讀者：完全不懂通訊的人。14 頁。每頁一個重點、一句生活比喻；🖼 表示有示意圖。
> 每頁只能使用「使用卡片」欄列出的證據卡。

| # | 標題 | 這頁要讓聽眾記住的一句話 | 生活比喻來源 | 使用卡片 | 圖 |
|---|---|---|---|---|---|
| 1 | 封面：衛星怎麼幫手機上網？ | — | — | ntn | — |
| 2 | 為什麼需要衛星 | 地球上還有很多地方沒有基地台，衛星可以補位 | ntn-use-cases F1 | ntn-use-cases、direct-to-device | — |
| 3 | 什麼是 NTN | 把基地台或中繼站搬到天上 | ntn F1 | ntn、uav-and-haps | 🖼 天上的三種平台高度 |
| 4 | 地面網路 vs 衛星網路 | 地面快、容量大；衛星涵蓋廣但延遲長 | tn-vs-ntn F1 | tn-vs-ntn | — |
| 5 | 三種衛星軌道 | 越低越快、但要越多顆 | satellite-orbits F1 | satellite-orbits、geo-vs-meo-vs-leo | 🖼 GEO／MEO／LEO 高度比例圖 |
| 6 | 軌道高度帶來的取捨 | 低軌延遲短；高軌一顆就能蓋很大 | geo-vs-meo-vs-leo F1 | geo-vs-meo-vs-leo、ntn-performance | — |
| 7 | 衛星是鏡子還是基地台 | 透明式只轉送，再生式自己處理訊號 | transparent-vs-regenerative-payload F1 | transparent-vs-regenerative-payload、ntn-architecture | 🖼 兩種架構示意 |
| 8 | 問題一：太遠 | 訊號飛很久，重傳機制會卡住 | harq-in-ntn F1 | ntn-challenges、harq-in-ntn | — |
| 9 | 問題二：太快 | 頻率會偏、衛星很快就飛走 | ntn-mobility F1 | ntn-challenges、ntn-mobility | — |
| 10 | 解法：手機先算好再送 | 用定位和衛星軌道，提早送、先調頻 | timing-advance-and-doppler F1 | timing-advance-and-doppler | 🖼 時序提前示意 |
| 11 | 手機直連衛星的兩種做法 | 現有 4G 手機馬上能用 vs 新規格長期更好 | direct-to-device F1 | direct-to-device、unmodified-4g-vs-nr-ntn | — |
| 12 | 地面＋衛星一起用 | 兩條路都有時，要分配好誰走哪條 | tn-ntn-integration F1 | tn-ntn-integration、atsss-vs-dualsteer | 🖼 DualSteer 兩條路 |
| 13 | 標準怎麼一步步完成 | 先研究、再寫規格，Rel-17 才正式上路 | 3gpp-standardization F1 | 3gpp-ntn-releases、3gpp-standardization | 🖼 時間軸 |
| 14 | 三句話帶走 | 衛星補地面不足；又遠又快要特別處理；地面＋衛星一起用是趨勢 | — | ntn、ntn-challenges、tn-ntn-integration | — |

## 檢查重點（給 B 關人工確認）

- 子題 1～8 都有對應頁面，沒有卡片以外的子題。
- 爭議數字提醒：軌道高度、GEO 延遲、Ka-band 上下行、LEO 速度在 wiki 有 ⚠️，只能用「目前結論」。
