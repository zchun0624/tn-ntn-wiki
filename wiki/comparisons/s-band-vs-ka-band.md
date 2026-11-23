# S-band 和 Ka-band 比較（S-band vs Ka-band）

> 類型：比較頁｜來源：figaro2026、lin2021｜更新：2026-11-23

## 一句話差別

S-band 頻率低、訊號穿透好、不怕天氣，但頻寬小；Ka-band 頻率高、頻寬大、速度快，但路徑損耗大，需要更好的天線 [figaro2026, p.7]。

## 比較表

| 項目 | S-band | Ka-band | 出處 |
|---|---|---|---|
| 模擬用的載波頻率 | 2 GHz | 20 GHz | [figaro2026, p.5, Table II] |
| 最大頻寬 | 30 MHz | 400 MHz | [figaro2026, p.7] |
| 頻率範圍 | FR1（6 GHz 以下） | FR2（毫米波） | [figaro2026, p.5] |
| 路徑損耗（LEO 下行） | 159.1 dB | 179.1 dB | [figaro2026, p.7] |
| 天線增益 | 較低 | UE 高約 40 dBi、衛星高約 10 dBi | [figaro2026, p.7] |
| 下行 SNR（LEO） | 6.6 dB | 8.5 dB | [figaro2026, p.7] |
| 通道容量（LEO） | 約 125 Mbps | 約 390 Mbps | [figaro2026, p.7] |
| 天氣影響 | 傳播條件較好，較不受天氣和雲影響 | 較差 | [figaro2026, p.7] |
| 適合的終端 | 手持 UE（LEO、GEO 都可以） | 天線增益高的 UE，例如 VSAT | [lin2021, p.3] |

## 什麼時候用哪一個

- 要手機直連、穩定覆蓋時用 S-band；Rel-16 研究的結論也是手持 UE 可以由 S-band 的 LEO、GEO 服務 [lin2021, p.3]。
- 要高速率、終端可以裝較大天線時，用 Ka-band [figaro2026, p.7]。
- S-band 在流量大時延遲上升很快，R > 250 Mbps 時延遲超過 500 ms [figaro2026, p.7]。
