# MLCC 下一站：PCB / CCL / 高速材料研究優先名單

Date: 2026-06-19
Status: Research Priority Note
Framework: 癌大派 Bottleneck OS / Product Cycle Delta Gate
Timeframe: 2-12 weeks swing-trade research
Final Action: Watch

---

## 1. 核心結論

MLCC 是 current cycle 的 scarce layer，PCB / CCL 是 Rubin → Feynman 下一輪需要優先研究的 scarce layer。

更精準講，下一站不是普通 PCB，而是：

1. Low-loss CCL / 高速材料
2. AI server 高多層 PCB / backplane
3. 光通訊 / CPO PCBA 外溢
4. Advanced substrate / high-end packaging substrate
5. MLCC / 被動元件延伸

研究排序應該由「板廠」前移到「高速材料」。PCB 廠較容易被市場看見，但 CCL / 銅箔 / 樹脂 / 玻纖布更可能藏住真正擴產約束。

這是高質研究方向，但不是可立即買入標的。未跑 Execution Gate 前，只能 Watch / Research Basket。

---

## 2. Product Cycle Delta Gate

| Product Cycle | Architecture Delta | Physical Constraint | Required Components | Scarce Layer | Research Maturity | Research Focus |
|---|---|---|---|---|---|---|
| Current Gen: Blackwell / GB300 | AI server 放量，power density 上升 | 電力、散熱、MLCC、高速連接、HBM | MLCC、HBM、power module、液冷、PCB | MLCC / HBM / Power | Stage 3 部分已財報驗證 | 不追新聞，等回踩與財報驗證 |
| Next Gen: Rubin / Rubin Ultra | Rack-scale co-design，NVLink 6，800G / 1.6T networking，HBM4 | 訊號損耗、層數、低延遲、材料可靠度 | 高多層 PCB、backplane、low-loss CCL、銅箔、玻纖布 | CCL / 高階 PCB | Stage 1-2，需法說與月營收驗證 | 主研究方向 |
| Next+1 Gen: Feynman | Optical NVLink、CPO scale-up、die stacking、custom HBM | 銅互連極限、封裝密度、光電整合 | CPO、silicon photonics、advanced substrate、光通 PCBA | CPO / 光電封裝 / advanced substrate | Stage 1，偏前瞻 | 建立早期追蹤，不宜當即時買點 |

Interpretation:

- MLCC = current scarcity
- PCB / CCL = next research layer
- CPO / optical packaging = next+1 optionality layer

不可將三個週期混在一起交易，否則容易出現「長線故事正確，但 swing timing 錯」。

---

## 3. Scarce Layer Ranking

### Rank 1: Low-loss CCL / 高速材料

Classification: Controls Scarce Layer / Supplies Scarce Layer

Why it matters:

Rubin / Feynman 令 rack-scale interconnect、NVLink、Ethernet、CPO、HBM4 / HBM4E 需求提升。真正變難的不只是 PCB 數量，而是高速訊號完整性、低損耗材料、層間可靠度與材料認證。

What to verify:

- AI server / HPC CCL 佔收入比例
- Low-Dk / Low-Df 材料出貨
- ASP 是否提升
- 毛利率是否改善
- 客戶 qualification / design-in / capacity reservation
- 是否有供應緊張或交期拉長

Priority companies:

- Elite Material / 台光電 2383.TW
- ITEQ / 台燿 6274.TW
- Nan Ya / 南亞 1303.TW
- Mitsui Kinzoku
- Mitsubishi Gas Chemical / MGC
- Copper foil / resin / glass cloth suppliers to be mapped

Risk:

- 大型材料公司純度不足
- 擴產太快，scarcity 消失
- AI exposure 無法從收入與毛利驗證
- 市場已提前 price in

---

### Rank 2: AI server 高多層 PCB / backplane

Classification: Supplies Scarce Layer

Why it matters:

AI server rack-scale design 推高板層數、訊號速度、散熱與可靠度要求。普通 PCB 不等於 scarce layer，真正值得研究的是 high-layer AI server PCB、backplane、switch / accelerator board。

What to verify:

- AI server / HPC 佔收入比例
- 是否有 Nvidia / hyperscaler / ODM / switch / accelerator board exposure
- High-layer board mix 是否提升
- 毛利率是否跟收入一起改善
- 客戶集中度與 dual-source 風險
- 產能利用率與擴產節奏

Priority companies:

- Victory Giant / 勝宏科技 300476.SZ
- TTM Technologies / TTMI
- Unimicron / 欣興 3037.TW
- Compeq / 華通 2313.TW
- Tripod / 健鼎 3044.TW
- Gold Circuit / 金像電 2368.TW

Risk:

- 股價已先炒，估值過熱
- 只是二線 proxy，非真正 leader
- 收入升但毛利不升
- 客戶 dual-source 壓價
- AI server mix 不夠高

---

### Rank 3: 光通訊 / CPO PCBA 外溢

Classification: Revenue Beneficiary / Supplies Scarce Layer candidate

Why it matters:

若 Feynman 推向 optical NVLink / CPO scale-up，傳統光模組產能可能不足。部分組裝或 PCBA 打件需求可能外溢至傳統 PCBA 廠。這一層彈性高，但控制力較弱。

What to verify:

- 是否有光通訊 / CPO / optical assembly 訂單
- 客戶是否放設備進廠
- 產線是否專用化
- Revenue 是否快速上升
- 毛利是否仍極低
- 客戶可否隨時抽單

Priority companies:

- Fabrinet / FN
- 台股 PCBA 打件廠池，需再建 universe
- 光模組 / silicon photonics 相關供應商另建 watchlist

Risk:

- 客戶可抽單
- 低毛利，收入升但 EPS 未必升
- 消息真假難驗證
- 更偏事件交易，不宜當核心倉

---

### Rank 4: Advanced substrate / ASIC / chiplet support

Classification: Supplies Scarce Layer / Revenue Beneficiary

Why it matters:

Feynman / custom ASIC / chiplet / die stacking 可能提升 advanced substrate 需求。這層潛力大，但時間可能更偏 2027-2028，未必適合作為 2-12 週 swing 主線，除非有財報或價格提前驗證。

Priority companies:

- Kinsus / 景碩 3189.TW
- Unimicron / 欣興 3037.TW
- Ibiden 4062.JP
- Shinko Electric 6967.JP
- Related IC substrate suppliers to be mapped

Risk:

- Timing 太遠
- 市場把 2028 故事當成 2026 收入炒
- 技術路線改變
- 收入驗證慢

---

### Rank 5: MLCC / 被動元件延伸

Classification: Current Cycle Scarcity / Supplies Scarce Layer

Why it matters:

MLCC / high-voltage passive components 仍受 AI server power density 與資料中心需求支持，但它已經較接近 current cycle，市場認知度高，不再是最早期 alpha。

Priority companies:

- Murata
- TDK
- Taiyo Yuden
- 國巨
- 華新科
- 禾伸堂

Risk:

- 題材已擴散
- 替代料天花板
- 追高賠率差
- 只適合等回調、量縮、均線支撐後再評估

---

## 4. Initial Company Priority List

| Rank | Company | Market | Layer | Bottleneck Type | Research Status | Action |
|---:|---|---|---|---|---|---|
| 1 | Elite Material / 台光電 | Taiwan | Low-loss CCL | Controls / Supplies Scarce Layer | Highest priority | Deep dive first |
| 2 | Victory Giant / 勝宏科技 | A-share / HK listing to verify | AI/HPC PCB | Supplies Scarce Layer | Strong theme evidence, valuation risk | Deep dive with price-in check |
| 3 | TTM Technologies / TTMI | US | Advanced PCB | US-listed proxy | Medium purity | Deep dive required |
| 4 | ITEQ / 台燿 | Taiwan | CCL | Supplies Scarce Layer | Need AI mix validation | Research |
| 5 | Unimicron / 欣興 | Taiwan | PCB / substrate | Mixed exposure | Needs segmentation | Research |
| 6 | Compeq / 華通 | Taiwan | PCB | Possible server exposure | Needs validation | Watch |
| 7 | Tripod / 健鼎 | Taiwan | PCB | Possible server exposure | Needs validation | Watch |
| 8 | Gold Circuit / 金像電 | Taiwan | PCB | Possible AI server exposure | Needs validation | Watch |
| 9 | Fabrinet / FN | US | Optical PCBA | Revenue Beneficiary / possible scarce assembly | Needs order validation | Watch |
| 10 | Kinsus / 景碩 | Taiwan | IC substrate | Next+1 optionality | Timing risk | Watch |
| 11 | Ibiden | Japan | IC substrate | Next+1 optionality | Timing risk | Watch |
| 12 | Shinko Electric | Japan | IC substrate | Next+1 optionality | Timing risk | Watch |

---

## 5. Research Tasks

### Task A: CCL / 高速材料 Deep Dive

Priority: Highest

Required checks:

1. Elite Material, ITEQ, Nan Ya, Mitsui Kinzoku, MGC latest IR / filings / earnings call
2. AI server / HPC CCL revenue contribution
3. Low-loss CCL ASP and margin trend
4. Capacity utilization / lead time / capex
5. Customer qualification and design-in evidence
6. Monthly revenue acceleration
7. Relative strength vs Taiwan PCB / electronics peers

Key question:

Rubin / Feynman 是否令 high-speed CCL content value 顯著提升，而不是普通 cyclic PCB recovery？

---

### Task B: AI/HPC PCB Leader Comparison

Priority: High

Required checks:

1. Victory Giant, TTMI, Unimicron, Compeq, Tripod, Gold Circuit latest financials
2. AI server / HPC / data center mix
3. Nvidia / hyperscaler / ODM / switch exposure
4. High-layer board capacity and gross margin
5. Capex and expansion plan
6. Customer concentration and dual-source risk
7. Price action: 20MA / 50MA / relative strength / volume

Key question:

誰是真 leader，誰只是 PCB beta / sympathy proxy？

---

### Task C: Feynman Optionality Basket

Priority: Medium

Required checks:

1. Optical NVLink / CPO roadmap evidence
2. CPO assembly and silicon photonics suppliers
3. PCBA 打件外溢 evidence
4. Advanced substrate / chiplet / die stacking demand path
5. 2026 vs 2027-2028 timing separation

Key question:

這層是 2-12 週可交易主線，還是只應放入 long watchlist？

---

## 6. Upgrade Triggers

A company or layer can upgrade from Watch to Probe Candidate only if several conditions appear together:

1. Official / primary evidence confirms AI server / high-layer PCB / high-speed CCL exposure
2. Revenue or monthly sales acceleration is visible
3. Gross margin improves, not only revenue grows
4. Capacity tightness or customer reservation is visible
5. Stock outperforms sector ETF / QQQ / SMH equivalent benchmark
6. Price completes 5-10 day base / tight range / pullback and reclaims pivot
7. Stop distance is合理 and not wider than normal swing risk

A company can upgrade to Buy Candidate only after full Execution Gate.

---

## 7. Failure Conditions

Downgrade this theme if:

1. Rubin volume ramp delays materially
2. Feynman / optical NVLink timeline moves further out
3. ODM / AI server guidance weakens
4. PCB companies show revenue growth but no margin improvement
5. CCL supply expands quickly and removes scarcity
6. Customers dual-source aggressively and compress pricing
7. Only second-tier proxy stocks rise while true leaders do not confirm
8. Good news appears but price fails to respond
9. Market regime turns Risk-Off

---

## 8. Research Rating / Execution Rating

Research Rating: A2 Research Basket

Reason:

PCB / CCL is a legitimate next research direction after MLCC because Rubin / Feynman increase rack-scale interconnect density, signal integrity requirements, high-speed material demand, and high-layer PCB complexity.

Execution Rating: Watch

Reason:

No individual company in this note has passed current Market Regime, ETF Rotation, Market Vote, Technical Setup, Stop Validity, and Execution Gate checks. This note is not a buy list.

Final Action: Watch

Why Not Buy Now:

The thesis is strong enough for research priority, but not enough for trade execution. PCB is a broad bucket and includes ordinary PCB, low-margin PCBA, high-speed CCL, high-layer server boards, and advanced substrate. Buying the bucket without verification risks confusing true bottleneck with proxy beta.

Trigger to Upgrade:

Upgrade after official evidence, revenue / margin validation, leader price confirmation, and a clean 5-10 day setup with a valid stop.

Failure Condition:

Downgrade if Rubin/Feynman timing slips, AI server demand weakens, PCB/CCL revenue fails to convert into margin, or only second-tier speculative proxies move.

---

## 9. Next Step

Immediate next research note should be:

`Brain/Themes/AI-Infrastructure/CCL-High-Speed-Materials-Universe.md`

Focus on:

- Elite Material
- ITEQ
- Nan Ya
- Mitsui Kinzoku
- MGC
- Copper foil / glass cloth / resin suppliers

This should be treated as the first deep dive, because the best alpha may be upstream of the obvious PCB names.
