# 跨國覆蓋與 UE 位置（UE Location and Regulation）

> 類型：概念頁｜來源：lin2021、3gpp2025、figaro2026｜更新：2026-11-23

## 一句話白話解釋

一顆衛星的訊號可能同時蓋到好幾個國家，所以網路要知道手機「實際在哪一國」，才能遵守那個國家的法規 [lin2021, p.4]。

## 詳細說明

- **問題**：地面網路通常只涵蓋一個國家；衛星系統可能涵蓋多個國家或公海，帶來新的監管挑戰 [lin2021, p.4]。
- **AMF 要確認國家**：存取與移動管理功能（Access and Mobility Management Function, AMF）可能需要確認 UE 位在它可以服務的國家，RAN 可以協助 [lin2021, p.4–5]。
- **gNB 換 AMF**：如果 gNB 發現 UE 在另一個國家，應該換到合適的 AMF，或請原 AMF 釋放 UE [3gpp2025, p.18]。
- **PLMN 選擇**：UE 需要選擇核心網位在自己所在國家的公共陸地行動網路（Public Land Mobile Network, PLMN），公海和全球業者的情況需要新規則 [lin2021, p.6]。
- **UE 回報位置**：連線後，UE 應網路要求回報粗略位置，精度約 2 km [3gpp2025, p.17]。
- **網路驗證位置**：Rel-18 研究結論：需要由網路來驗證 UE 回報的位置，精度約 5～10 km，相當於一個地面巨型細胞的直徑 [3gpp2025, p.20]。Rel-18 的做法是用多次 RTT 量測來驗證，即使 GNSS 有限或沒有，而且天上只看得到一顆衛星也能做 [figaro2026, p.4]。

## 和其他概念的關係

- [NTN 和地面網路不一樣的地方](ntn-challenges.md)：跨國覆蓋是 NTN 特有的挑戰
- [NTN 的移動性管理](ntn-mobility.md)：細胞會移動，國界判斷更複雜
- [3GPP NTN 標準演進](../timeline/3gpp-ntn-releases.md)：Rel-18 的網路驗證 UE 位置

## 延伸閱讀

- [lin2021](../sources/lin2021.md)
- [3gpp2025](../sources/3gpp2025.md)
- [figaro2026](../sources/figaro2026.md)
