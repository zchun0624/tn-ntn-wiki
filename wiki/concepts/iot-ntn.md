# IoT NTN（物聯網衛星接取）

> 類型：概念頁｜來源：lin2021、3gpp2025、figaro2026、ericsson2025｜更新：2026-11-23

## 一句話白話解釋

讓省電、便宜的物聯網裝置（例如偏遠地區的感測器）也能直接透過衛星回傳資料 [lin2021, p.6]。

## 詳細說明

- **基礎技術**：3GPP 在 Rel-13 制定了 LTE-M 和窄頻物聯網（Narrowband IoT, NB-IoT），目標是低成本、長電池壽命、加強覆蓋 [lin2021, p.6]。
- **為什麼要上衛星**：在沒有行動網路的地區，可以用 NTN 補足地面部署，支援大規模機器通訊 [lin2021, p.6]。
- **Rel-17 研究的假設**：6 GHz 以下頻段、LEO 或 GEO、透明式酬載，裝置最大輸出功率 20 dBm 或 23 dBm [lin2021, p.7]。
- **以 NR NTN 為基礎**：為了簡化，LTE 版本的 NTN 盡量沿用 NR NTN 的功能 [3gpp2025, p.30]。
- **GNSS**：和 NR NTN 一樣假設裝置有 GNSS，但不假設 GNSS 和 NTN 運作同時進行 [3gpp2025, p.30]。
- **GNSS 量測空檔**：有些 IoT 裝置不能同時做 GNSS 和 NTN 通訊，所以規格支援預留做 GNSS 量測的傳輸空檔 [ericsson2025, p.6]。
- **進入手機**：NB-IoT 原本不在一般手機裡，但晶片廠開始把它整合進手機，因為它只需要很窄的頻寬，適合用現有 GEO 衛星傳簡訊；已經在幾個國家商用 [ericsson2025, p.6]。
- **不連續覆蓋**：IoT NTN 在 EPS 中支援不連續覆蓋，讓 UE 收不到衛星時不會被斷線，網路也能暫存要送給它的資料；這點在 NR 的 Rel-17 沒有考慮 [3gpp2025, p.31]。
- **Rel-19 方向**：支援儲存轉送（Store and Forward）運作，衛星上放完整的 eNB；並加強上行容量 [3gpp2025, p.32]。
- **Rel-20 方向**：IoT NTN 第 4 階段，讓 NB-IoT 也能透過衛星打 IMS 語音電話，UE 發射功率上限提高到 37 dBm [figaro2026, p.4–5]。

## 和其他概念的關係

- [NTN 的應用情境](ntn-use-cases.md)：IoT 是 mMTC 情境的代表
- [時序提前與都卜勒預補償](timing-advance-and-doppler.md)：IoT 裝置一樣靠 GNSS 預補償
- [3GPP NTN 標準演進](../timeline/3gpp-ntn-releases.md)：IoT NTN 在各版本的進度

## 延伸閱讀

- [lin2021](../sources/lin2021.md)
- [3gpp2025](../sources/3gpp2025.md)
- [ericsson2025](../sources/ericsson2025.md)
- [figaro2026](../sources/figaro2026.md)
