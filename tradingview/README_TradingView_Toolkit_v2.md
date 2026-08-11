# TradingView Swing Toolkit v2

Two Pine Script v6 indicators designed to compress the user's 2–12 week US-stock swing workflow into at most two TradingView indicator slots.

## 1. Swing Structure Toolkit v2 (overlay)

Default / Clean Mode behavior is achieved by defaults rather than a hard lock: only EMA10, EMA20, SMA50, SMA200 and the compact dashboard are visible. All other modules default OFF and can be enabled independently.

### Six MA slots
Default periods: 5 / 10 / 20 / 50 / 150 / 200.
Each slot supports ON/OFF, EMA/SMA/WMA/HMA/RMA, length, price source, color, width and line/stepline/circles.

### Optional modules
- Daily Minervini price Trend Template (price criteria only; no fabricated IBD RS)
- 52-week high/low
- Daily ADR20 / ATR14 / EMA10/EMA20 extension engine
- Inside bar detector
- Three-week tight-close detector (weekly calculation)
- Confirmed pivot H/L labels and swing %
- Support / resistance channels with ATR or range-based width
- Optional structural execution-plan helper (stop %, stop in daily ATR, target, reward %, available R)

### Risk helper semantics
The helper is measurement only. It never issues Buy/Sell instructions.
- stop < 0.8 daily ATR: TOO TIGHT
- 0.8–1.2 daily ATR: PROBE BAND
- stop > configured max (default 8%): TOO WIDE
- available R < 2.5R: INSUFFICIENT

## 2. Market Vote Lab v2 (lower pane)

Only one main mode is plotted at a time; other metrics remain in dashboard/data window.

Modes:
1. MRS-DB
2. Rolling RS
3. Corrected Weighted RS
4. Mansfield RS
5. Relative Volume at Time

### Benchmark defaults
Primary: QQQ.
Sector preset: SMH. Sector presets also include SOXX, IGV, CIBR, XLI, XLE, XLF, Custom and OFF.
If sector confirmation is enabled and sector data is invalid, classification fails closed.

### State model
Leadership: LEADER / EMERGING / WATCH / LAGGARD plus data errors.
Momentum: IMPROVING / STABLE / WEAKENING.
Position: EXTENDED / NORMAL / EMA20 TEST / UNDERCUT / BROKEN / PULLBACK WATCH.
Research state: RESEARCH FOCUS / WATCH / WAIT / AVOID.

`RESEARCH FOCUS` is not an execution signal. Full Market Regime, ETF rotation, thesis validation and position sizing remain outside the Pine indicator.

### RVOL-at-time
Default session: US regular 09:30–16:00 exchange time.
Supports cumulative and same-bar modes.
Uses only completed prior sessions and excludes the current session from the denominator. Clock-time keys are used so missing bars do not shift comparisons. Fewer than the configured minimum comparable sessions returns insufficient history.

## Installation
TradingView does not import `.pine` files directly. Open Pine Editor, create a new indicator, paste one file's full source, Save, then Add to chart. Repeat for the second file.

## Validation status
This package has undergone source review, formula spot checks, future-leak scan and Pine resource-limit prechecks. It has NOT been claimed as TradingView-compiled in the ChatGPT environment. Codex is instructed to run the strongest available Pine/TradingView compiler and runtime validation before marking the task complete.