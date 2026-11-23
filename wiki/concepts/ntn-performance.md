# NTN 的實際效能（NTN Performance）

> 類型：概念頁｜來源：figaro2026｜更新：2026-11-23

## 一句話白話解釋

用模擬實際跑一次衛星網路：LEO 延遲短，GEO 在高頻段反而跑得更快；但這些結果很依賴參數設定，不能直接說哪種軌道比較好 [figaro2026, p.6–7]。

## 詳細說明

- **模擬方式**：用 ns-3 的 ns3-NTN 模組，依 3GPP 校準情境做端到端系統模擬；衛星是再生式（gNB 在衛星上），地面一個 UE 從遠端主機下載資料 [figaro2026, p.5]。
- **四種情境**：LEO 600 km 和 GEO 35,786 km，各在 S-band（2 GHz、30 MHz）和 Ka-band（20 GHz、400 MHz）[figaro2026, p.5, Table II]。
- **評估指標**：端到端吞吐量、封包送達率（PDR）、應用層延遲 [figaro2026, p.5]。

| 結果 | 數字 | 出處 |
|---|---|---|
| Ka-band 下可支撐的來源速率 | LEO 約 300 Mbps，GEO 約 450 Mbps | [figaro2026, p.6] |
| Ka-band 最大吞吐量 | GEO 比 LEO 高最多 50%（LEO 的 SNR 較低：8.5 dB vs 11.6 dB） | [figaro2026, p.6, Table II] |
| 1000 Mbps 時的 PDR | GEO 0.47，LEO 0.30 | [figaro2026, p.7] |
| 單位面積容量 | LEO 約 170 Kbps/km²，GEO 約 1.4 Kbps/km² | [figaro2026, p.7] |
| 單程傳播延遲 | GEO 約 120 ms，LEO 約 2 ms | [figaro2026, p.7] |
| 通道容量 | Ka-band 約 390 Mbps，S-band 約 125 Mbps | [figaro2026, p.7] |

- **為什麼 GEO 比較快**：GEO 衛星可以用大天線、高功率，天線增益最高 58.5 dBi；LEO 為了降低成本，硬體較簡單，增益只有 38.5 dBi [figaro2026, p.6]。提高 LEO 的發射功率後，LEO 在 Ka-band 可以到 750 Mbps [figaro2026, p.6]。
- **但 GEO 不一定比較好**：GEO 細胞很大，要分給更多 UE，所以單位面積容量遠低於 LEO [figaro2026, p.7]。
- **作者結論**：S-band 下 LEO 勝過 GEO，Ka-band 下則相反；這是參數設定的結果，不是軌道本身決定的 [figaro2026, p.7]。
- **模擬的限制**：單一 UE、靜止、UDP、沒有換手，和實際商用系統（仰角通常 >70°）不同 [figaro2026, p.5, p.7]。

## 和其他概念的關係

- [GEO、MEO、LEO 比較](../comparisons/geo-vs-meo-vs-leo.md)：軌道的理論比較
- [S-band 和 Ka-band 比較](../comparisons/s-band-vs-ka-band.md)：頻段對效能的影響
- [NTN 和地面網路不一樣的地方](ntn-challenges.md)：延遲數字的來源之一

## 延伸閱讀

- [figaro2026](../sources/figaro2026.md)
