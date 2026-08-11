# Codex Task: TradingView Swing Toolkit v2 — two-indicator production handoff

## Objective
Build, debug, and validate a production-ready Pine Script v6 toolkit for a **2–12 week US-stock swing-trading workflow**, while consuming **at most two TradingView indicator slots**.

The output must be exactly two primary scripts:

1. `Swing_Structure_Toolkit_v2.pine` — overlay / main-chart structure, volatility, S/R, plan-risk helper.
2. `Market_Vote_Lab_v2.pine` — one-pane-at-a-time RS / RVOL modes plus a compact dashboard.

This is not an auto-trading system. It must never turn research/RS strength into a Buy signal by itself. Market regime / ETF rotation / thesis validation remain external hard gates.

---

## User workflow and non-negotiable constraints

- Market: US stocks primary; Japan/HK secondary, but defaults should optimize for US equities.
- Holding period: 2–12 week swing trades.
- Technical style: Martin / JLaw / Minervini-style momentum and price structure.
- Key execution rules:
  - Market/ETF support comes before stock action.
  - Prefer sector top 2–3 leaders.
  - Setup must mature before entry; do not treat first random trendline reclaim as a clean breakout.
  - Entry confirmation should be based on closing acceptance, not an intrabar wick.
  - Stop must sit at a real invalidation point and respect normal volatility.
  - Stop < ~0.8 ATR is usually too tight for a normal swing; 0.8–1.2 ATR is probe territory.
  - Stop distance > 8–10% is not a normal swing setup.
  - Require at least 2.5R available space for a normal trade.
  - A strong thesis or RS score never overrides the execution gate.
- Clean Mode is the default UI.
- Six universal MA slots. Default periods: **5 / 10 / 20 / 50 / 150 / 200**.
- Default visible MAs: **EMA10 / EMA20 / SMA50 / SMA200**. EMA5 and SMA150 default OFF.
- Every optional visual module must be independently switchable.
- In the lower pane, **only one main mode is plotted at once**. Other computed metrics remain in the dashboard/data window.
- Do not add RSI/MACD/Stochastic or unrelated oscillators.

---

## Architecture rule

Do not mechanically concatenate legacy scripts. Reimplement as two modular Pine v6 indicators with shared concepts but independent calculation layers. Preserve attribution where logic is materially reused.

Concept lineage:

- Fred6724 — Mark Minervini overlay concepts.
- LonesomeTheBlue — Support Resistance Channels concepts.
- e2e4mfck + LucF — Relative Volume at Time concepts.
- stageanalysis — Mansfield Relative Strength concept.
- bharatTrader — rolling Relative Strength concept.
- Skyte — “IBD Style” weighted RS concept; original formula/indexing contained defects, so retain only corrected methodology.
- ArmerSchlucker / MikeC / TheScrutiniser / GlinckEastwoot — ADR% formula lineage.

Keep MPL 2.0 notices/attribution where required. Never claim any implementation is the official IBD RS Rating.

---

# A. Swing Structure Toolkit v2 (overlay)

## A1. Six universal MA slots
Each slot must support:

- Show ON/OFF
- Type: EMA / SMA / WMA / HMA / RMA
- Length
- Source: Close / Open / High / Low / HL2 / HLC3 / OHLC4
- Color
- Width
- Plot style: Line / Stepline / Circles if Pine allows the selected style safely

Default configuration:

| Slot | Type | Length | Default show |
|---|---|---:|---|
| MA1 | EMA | 5 | OFF |
| MA2 | EMA | 10 | ON |
| MA3 | EMA | 20 | ON |
| MA4 | SMA | 50 | ON |
| MA5 | SMA | 150 | OFF |
| MA6 | SMA | 200 | ON |

Do not let changing a user MA slot silently alter internal risk calculations. Internal daily EMA20/SMA50/SMA200 used by models must be explicit and independent.

## A2. Daily Trend Template / 52-week structure
Implement the Minervini **price criteria only**. Do NOT fabricate IBD RS Rating.

Calculate in a true daily context regardless of chart timeframe:

- Price > SMA150 and SMA200
- SMA150 > SMA200
- SMA200 rising for approximately one month (21 trading days; document exact implementation)
- SMA50 > SMA150 and SMA200
- Price > SMA50
- Price >= 30% above 52-week low
- Price within 25% of 52-week high

Optional visuals:

- Trend Template zone/fill, OFF by default
- 52-week high/low, OFF by default

Handle insufficient history cleanly (`n/a`, no false pass).

## A3. Daily volatility engine — P0
All metrics called ADR/ATR/LoD/EMA20-extension must stay **daily** even when the chart is 1m/5m/1h/1W.

Required daily metrics:

- ADR20% = 20-day average of `100 * (high/low - 1)` or equivalent
- ATR14 = daily `ta.atr(14)`
- Daily EMA10 and EMA20
- Current daily low / LoD distance expressed in daily ATR
- Close extension above/below daily EMA20 expressed in ADR units
- Optional extension vs daily EMA10 in ATR units for legacy comparison

Do not accidentally recalculate them from chart-timeframe bars.

Extension states:

- Normal
- Extended
- Extreme / exhaustion-risk

User-selectable thresholds, sensible defaults around 2.5 ADR and 3.5 ADR. These are **risk warnings**, never sell commands.

If the chart is intraday, clearly distinguish developing current-day daily values from last confirmed daily values. Prefer non-repainting confirmed values for alerts; dashboard may show developing values if labeled.

## A4. Inside Day
- Chart-timeframe inside bar detector.
- OFF by default.
- Avoid unlimited box/label creation; only create visuals when enabled and enforce object limits.
- Alert should only fire on a confirmed chart bar.

## A5. Three-week tight
- Weekly calculation, not “three bars of whatever chart timeframe”.
- It can be visualized on weekly charts or surfaced in dashboard on other charts, but calculation must be weekly.
- Use an adaptive ATR-based tolerance.
- Document exact rule; do not claim official IBD 3WT if materially different.
- OFF by default.

## A6. Pivot high/low
- Configurable left/right pivot length; default 9.
- Source: High/Low or Close/Open.
- Optional swing % labels.
- OFF by default.
- Make confirmation delay explicit in comments/tooltips: a `rightBars` pivot is only known after those future bars complete.
- No misleading historical “signal at pivot date” alert. Alerts, if any, fire when the pivot becomes confirmed, not retroactively.

## A7. Support / Resistance Channels
Retain the useful concept but improve ranking.

Required inputs:

- Pivot period
- Source: High/Low or Close/Open
- Channel width mode: ATR / historical-range %
- ATR width default around 0.75 ATR
- Range width fallback 2–3%
- Lookback ~180–220 daily bars default
- Minimum pivots >= 2
- Max visible channels default 4

Ranking must not equal “more touches = always stronger”. Score can incorporate:

1. pivot count / structural importance
2. recency
3. proximity to current price
4. rejection/acceptance evidence where practical
5. diminishing benefit from repeated tests

Prefer nearest meaningful support/resistance zones for execution planning. Old far-away levels must not occupy all four slots merely because they had many touches.

Break detection:

- Resistance break = confirmed close above zone top
- Support break = confirmed close below zone bottom
- Never call this a buy/sell signal
- Optional alerts OFF by default

Performance:

- Recompute heavy clustering only when a new pivot is confirmed or necessary.
- Cap stored pivots and objects.

## A8. Manual execution-plan helper (optional / OFF by default)
Translate structure into risk information without making trade decisions.

Inputs:

- Planned entry price (0/off if unused)
- Planned stop price (0/off if unused)
- Optional manual target; otherwise use nearest valid resistance above planned entry if available

Dashboard outputs when active:

- Stop distance %
- Stop distance in daily ATR
- Nearest resistance / target
- Available reward %
- Available R multiple
- Stop validity:
  - `<0.8 ATR` => TOO TIGHT for normal swing
  - `0.8–1.2 ATR` => PROBE RANGE
  - `>8–10%` => TOO WIDE for normal swing
- R/R:
  - `<2.5R` => REJECT FOR NORMAL SWING
  - `>=2.5R` => SPACE OK

These are local structural checks only. Never output “BUY”.

## A9. Clean dashboard
Default compact rows:

- Daily ADR20%
- Daily ATR14
- LoD distance (daily ATR)
- Daily EMA20 extension (ADR)
- Trend Template: PASS/FAIL/n/a
- Structure: NORMAL / IN CHANNEL / R BREAK / S BREAK / INSIDE / 3W TIGHT
- Nearest support
- Nearest resistance
- Execution helper summary only if enabled

Allow dashboard OFF.

---

# B. Market Vote Lab v2 (lower pane)

## B1. One display mode at a time
Dropdown modes:

1. `MRS-DB`
2. `Rolling RS`
3. `Weighted RS`
4. `Mansfield RS`
5. `Relative Volume at Time`

Only selected mode occupies pane scale. Other metrics may remain dashboard/data-window calculations if Pine limits permit.

## B2. Benchmark engine
Primary presets:

- QQQ default
- SPY
- IWM
- Custom

Sector presets:

- Semiconductors: SMH
- Semiconductors alt: SOXX
- Software: IGV
- Cybersecurity: CIBR
- Industrials: XLI
- Energy: XLE
- Financials: XLF
- Custom
- OFF

Dashboard must show actual ticker.

If sector confirmation is enabled and sector data invalid, **fail closed**:

- show `SECTOR DATA ERROR`
- do not classify Leader from primary-only data
- never silently fall back

## B3. MRS-DB core model
Daily model defaults:

- Fast 21D, weight 30%
- Core 63D, weight 50%
- Structural 126D, weight 20%
- Primary/sector blend default 65/35 or 70/30; configurable

Use correct relative-return math:

`(1 + stock_return) / (1 + benchmark_return) - 1`

Do not divide a percentage spread by a negative/near-zero benchmark percentage.

Calculate stock and benchmark returns in the same daily context.

Detail metrics:

- 21D RS vs primary
- 63D RS vs primary
- 126D RS vs primary
- 21/63/126 vs sector
- composite raw relative momentum / alpha

## B4. Self-history percentile
`ta.percentrank(compositeRaw, lookback)` compares a stock with **its own history**, not the market universe.

Name clearly:

- `Self-History RS Percentile` or `Historical RS Percentile`

Never label IBD RS or market percentile.

Edge cases:

- insufficient history => n/a
- near-flat raw series / stock equals benchmark => avoid misleading 100/0 score; use n/a or neutral with documented logic

## B5. Leadership classification
Do not rely solely on self-history percentile.

Axes:

- LEADER
- EMERGING
- WATCH
- LAGGARD
- data error states

Leader should require minimum:

- Primary data valid
- Sector valid if enabled
- Self-history percentile above threshold default ~80
- 63D RS vs primary above configurable absolute floor, initial default ~+3%
- 63D RS vs sector > 0 if enabled
- absolute daily trend healthy: close > EMA20, EMA20 > SMA50, close > SMA200, SMA50 rising

Do NOT require 20D percentile change to be strictly positive for every Leader. A high-quality leader consolidating near a high percentile may remain `LEADER + STABLE`.

Emerging should represent genuine acceleration, e.g. percentile 65–80 plus improving slope and positive primary/sector RS.

## B6. Orthogonal states
Separate:

### Leadership
LEADER / EMERGING / WATCH / LAGGARD

### Momentum
IMPROVING / STABLE / WEAKENING

### Position relative to daily EMA20 using ADR
Suggested states:

- EXTENDED: >= +2.5 ADR configurable
- NORMAL
- EMA20 TEST: approximately within ±0.30 ADR
- UNDERCUT: below EMA20 by >0.30 and <=0.75 ADR
- BROKEN: below EMA20 by >0.75 ADR and/or confirmed structural deterioration; refine with two-close or volume logic

The old rule `close < EMA20 => AVOID` is prohibited.

### Research focus
Use explicit wording:

- `RESEARCH FOCUS`
- `WATCH`
- `WAIT`
- `AVOID`

`RESEARCH FOCUS` means worth attention, **not executable**.

Never display `BUY`, `A1 Executable`, or a full Execution Gate because this script does not know complete market regime, ETF rotation breadth, bottleneck thesis, earnings validation, or actual position sizing.

## B7. Healthy pullback
Minimum suggested criteria:

- leadership not laggard/error
- daily EMA20 rising
- EMA20 > SMA50
- close > SMA50
- within chosen ADR band around EMA20
- recent volume contraction, e.g. 5D avg < 20D avg
- RS deterioration mild, not collapse

Label `PULLBACK WATCH`, not buy trigger.

## B8. Rolling RS
- Fixed-period daily relative return vs primary benchmark.
- Default 50D.
- Correct ratio-return math.
- Optional 10D EMA signal.
- Zero line.
- Can be displayed from other chart timeframes using daily data, but avoid repaint ambiguity in alerts.

## B9. Corrected Weighted RS
Old “IBD Style” script had two defects:

1. quarterly indexing compounded offsets incorrectly
2. `(stock_perf - ref_perf)/ref_perf` reverses/explodes with negative/near-zero benchmark performance

Correct quarterly segments:

- 0–63 bars
- 63–126
- 126–189
- 189–252

Weights:

- most recent quarter 40%
- each older quarter 20%

Compare stock weighted growth factor vs benchmark weighted growth factor safely. Do not call official IBD RS Rating.

## B10. Mansfield RS
Calculate strictly in **weekly context**:

- stock weekly close
- benchmark weekly close
- ratio
- 52-week ratio MA default
- Mansfield = `(ratio / MA - 1) * 100`

Must not mix daily stock close with weekly benchmark close.

If supporting display on non-weekly chart, request the entire weekly calculation, not only weekly benchmark.

## B11. Relative Volume at Time — P0 session rewrite
Default target: **US regular session 09:30–16:00 exchange time**, user-configurable.

Requirements:

- Regular Session default
- optional Extended / Custom
- detect session boundaries with `time()`/session strings, not `change(time("D"))`
- compare current bar offset only with **completed prior sessions**
- current session must never contaminate historical average
- support cumulative from session start and same-bar point volume
- historical lookback default 5 completed sessions
- display sample count e.g. `4/5 sessions`
- fewer than 3 valid comparable sessions => `INSUFFICIENT HISTORY` / n/a
- handle missing bars safely
- handle early closes/session-length mismatch by using only available matching offsets
- clear profile-overflow warning
- optimize session rotation; avoid clearing huge arrays every bar
- no future leakage/lookahead

Display:

- columns
- 1.0 reference line
- configurable threshold default 2.0x
- optional EMA of RVOL
- up/down color by current bar direction

## B12. Alerts and confirmation — P0
Alerts must match model timeframe, not merely chart bar:

- MRS / Rolling RS / Weighted RS: confirmed daily information
- Mansfield: confirmed weekly information
- RVOL: confirmed current intraday bar

Do not use `barstate.isconfirmed` inside a `request.security()` expression.

If script is on intraday chart and dashboard displays daily metrics, an intraday bar close must not masquerade as confirmed daily signal.

Use official Pine non-repainting HTF patterns.

---

# C. Performance / Pine constraints

Target broad TradingView compatibility, not Ultimate-only assumptions.

- Keep unique `request.*()` calls <= 40.
- Keep arrays well below 100,000 elements.
- Stay within object limits and delete/reuse boxes/labels/lines deliberately.
- Avoid O(N^2) work on every bar. S/R clustering may be O(N^2) only on new confirmed pivots with capped N.
- Minimize redundant `request.security()` calls; tuples are allowed if tuple-element limits stay safe.
- Avoid huge input surfaces where presets are enough.
- No runtime errors on missing data/history.

---

# D. Repainting / historical honesty

For every module classify behavior in comments/docs:

- confirmed/non-repainting
- developing current-bar value
- delayed confirmation, e.g. pivots

Never create a historical alert at the pivot bar when the pivot became knowable only `rightBars` later.

For higher-timeframe data on lower-timeframe charts, explicitly choose developing vs last-confirmed values. Alerts must use confirmed data.

---

# E. Test matrix

Do not declare complete after visual review only.

## Compile
Both scripts compile Pine v6 with zero compiler errors.

## Symbols
At minimum:

- AAPL
- NVDA
- MU or another high-ADR semiconductor
- a lower-volatility US stock
- QQQ with primary benchmark = QQQ as self-benchmark edge case

## Timeframes

### SST
- 1D
- 1W
- 5m
- 15m
- 60m

Verify daily ADR/ATR/EMA extension remains daily on all chart timeframes.

### MVL
- MRS mode 1D
- Rolling/Weighted on 1D and one intraday chart if supported
- Mansfield 1W
- RVOL 1m/5m/15m

## RVOL session tests

- Regular hours only
- Extended-hours chart enabled
- first 30 minutes
- midday
- near close
- missing bars if reproducible
- early-close day if available

## Data-error tests

- invalid custom sector
- sector confirmation OFF
- insufficient history/recent IPO
- poor/no volume symbol if practical

## Numerical spot checks
Manually calculate at least:

- ADR20%
- ATR14 source context daily
- one Rolling RS
- one Weighted RS quarter set
- one Mansfield weekly value
- one RVOL same-time example

Record expected vs actual.

## Behavior checks

- QQQ vs QQQ Rolling RS ~0
- negative benchmark periods do not invert relative-strength sign incorrectly
- invalid sector + confirmation ON fails closed
- current RVOL session excluded from historical denominator
- tiny EMA20 undercut does not auto-Avoid
- leader in tight consolidation can remain LEADER + STABLE

---

# F. UX acceptance

Default SST after Add to chart:

- EMA10 / EMA20 / SMA50 / SMA200 only + compact dashboard
- no pivot labels
- no S/R boxes
- no Trend Template fill
- no inside-day boxes
- no 3WT boxes
- no execution-plan markers unless enabled

Default MVL:

- MRS-DB mode
- one main scale
- compact dashboard
- restrained background

Unambiguous labels:

- `Self-History RS %ile`, not `RS Rating`
- `RESEARCH FOCUS`, not ambiguous `FOCUS`
- actual primary and sector ticker names
- `PULLBACK WATCH`, not `PULLBACK BUY`

---

# G. Documentation

Create `README_TradingView_Toolkit.md` including:

- install instructions: TradingView does not import `.pine`; copy each script into Pine Editor, Save, Add to chart
- default configuration
- modes
- alerts
- repaint/confirmation caveats
- known limitations
- source attribution/licenses

---

# H. Verification loop / stop rule

Work as a bounded engineering loop:

1. Inspect code/spec.
2. Fix highest-impact gap.
3. Run strongest available validation.
4. Review diff for regressions/unnecessary complexity.
5. Repeat until acceptance passes or a real external blocker exists.

Do NOT:

- claim success from a rename
- claim TradingView compile verification if it never ran
- weaken hard requirements to pass tests
- add auto-buy/sell recommendations
- silently drop modules due to Pine limits
- optimize visuals at expense of calculation correctness

If a Sol/reviewer subagent is available, use it as final independent acceptance reviewer. It must explicitly PASS the checklist before stopping. If unavailable, perform a separate final reviewer pass and state the limitation.

---

# I. Definition of Done

- [ ] Exactly two primary Pine v6 scripts.
- [ ] Both compile in TradingView with zero errors, OR explicitly `BLOCKED: TRADINGVIEW_COMPILER_UNAVAILABLE`; static checks alone are not full verification.
- [ ] SST Daily ADR/ATR/EMA/LoD stay daily on intraday/weekly charts.
- [ ] Six MA slots work; Clean Mode defaults correct.
- [ ] Trend Template daily/history-safe.
- [ ] S/R efficient and proximity/recency-aware.
- [ ] Optional stop/R helper reports ATR distance and >=2.5R without issuing trades.
- [ ] MVL plots only one primary mode at once.
- [ ] MRS dual-benchmark math correct; sector errors fail closed.
- [ ] Self-history percentile clearly labeled, not IBD ranking.
- [ ] EMA20 state uses TEST/UNDERCUT/BROKEN logic; tiny undercuts do not auto-Avoid.
- [ ] Rolling RS math checked.
- [ ] Weighted RS indexing/negative-benchmark bug checked.
- [ ] Mansfield true weekly context.
- [ ] RVOL session-aware, completed-prior-session denominator, sample count.
- [ ] Alerts use correct daily/weekly/intraday confirmation semantics.
- [ ] No obvious repaint/future leak.
- [ ] Request/object/collection limits reviewed.
- [ ] Test matrix documented.
- [ ] README complete.
- [ ] Final reviewer pass complete.

Final Codex response must include:

1. Architecture/fix summary
2. Files changed
3. Exact validation performed
4. Test matrix results
5. Numerical spot-check results
6. Remaining limitations/blockers
7. PASS/FAIL against every Definition-of-Done item
