# 衛星直連手機的兩種做法（ericsson2025）

> 類型：來源頁｜來源：ericsson2025｜更新：2026-11-23

## 基本資訊

- 標題：Satellite direct-to-device communication: two approaches for 3GPP global connectivity
- 作者：Sichao Song、Sebastian Euler、Fatemeh Ghasemifard、Hieu Do、Stephane Boichon、Marie-Laure Charles（Ericsson）
- 年份：2025 年 12 月（Ericsson Technology Review #10）
- 類型：產業報告
- 網址：https://www.ericsson.com/en/reports-and-papers/ericsson-technology-review

## 一句話總結

比較讓手機直接連衛星的兩種做法：「直接用現有 4G 手機」短期可行但限制多；「3GPP NR-NTN」需要新手機，但長期更有彈性、效能更好 [ericsson2025, p.2, p.6]。

## 重點

- 全球行動訂閱數預計在 2025 年底達到 88 億，但偏遠、海上、山區與災區仍有覆蓋缺口 [ericsson2025, p.2]。
- 可重複使用的火箭讓發射成本大幅下降，加上窄點波束天線與衛星上的晶片進步，讓衛星直連手機變得可行 [ericsson2025, p.2]。
- 兩種頻譜模式：和電信業者合作使用地面行動頻譜，或使用 ITU 分配給行動衛星服務（MSS）的頻譜 [ericsson2025, p.3]。
- 未修改 4G 做法：網路端替所有人補償延遲與都卜勒，但只能對準波束內的一個參考點，離參考點越遠誤差越大 [ericsson2025, p.4]。
- NR-NTN 做法：每支手機用 GNSS 自己補償，不受波束大小限制，但只有 Rel-17 之後的晶片支援 [ericsson2025, p.5–6]。
- 衛星細胞內各處的訊號強度差不多，所以傳統「比訊號強弱」的換手方式不可靠 [ericsson2025, p.5]。
- NB-IoT 開始被整合進手機晶片，可以用現有的 GEO 衛星傳簡訊，已經在幾個國家商用 [ericsson2025, p.6]。
- 6G 預計一開始就內建 NTN 支援，包括不依賴 GNSS 的運作 [ericsson2025, p.6]。

## 這份資料貢獻到的頁面

- [手機直連衛星（D2D）](../concepts/direct-to-device.md)
- [未修改 4G 和 NR-NTN 兩種直連做法比較](../comparisons/unmodified-4g-vs-nr-ntn.md)
- [衛星軌道](../concepts/satellite-orbits.md)
- [時序提前與都卜勒預補償](../concepts/timing-advance-and-doppler.md)
- [NTN 的 HARQ](../concepts/harq-in-ntn.md)
- [NTN 的移動性管理](../concepts/ntn-mobility.md)
- [IoT NTN](../concepts/iot-ntn.md)
- [NTN 的應用情境](../concepts/ntn-use-cases.md)
