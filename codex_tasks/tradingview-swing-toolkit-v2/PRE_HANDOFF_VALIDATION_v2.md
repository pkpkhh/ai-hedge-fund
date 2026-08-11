# Pre-handoff validation — TradingView Swing Toolkit v2

## Status
Implementation complete for handoff. Final TradingView compiler/runtime verification remains required.

## Static checks performed
- Balanced (), [], {} delimiters: PASS for both files.
- `lookahead_on`: 0 occurrences in both files.
- Unique `request.security()` call sites: SST 16, MVL 14; both below the broad-plan 40-call ceiling documented by TradingView.
- Largest RVOL arrays at maximum 20 sessions: 28,800 elements each, below the 100,000-element collection limit.
- S/R stored pivots capped at 80; clustering only recomputes on a newly confirmed pivot.
- No Buy/Sell output states in Market Vote Lab.
- Clean defaults: MA5 OFF, EMA10 ON, EMA20 ON, SMA50 ON, SMA150 OFF, SMA200 ON; optional overlay modules OFF; dashboard ON.
- MVL main modes are mutually exclusive by one dropdown.
- MRS/Rolling/Weighted alerts require confirmed 1D chart bars; Mansfield requires confirmed 1W; RVOL requires confirmed intraday in-session bars.

## Formula spot checks
1. ADR equivalence checked: average `100*(H-L)/L` == `100*(average(H/L)-1)` for sample bars.
2. Relative return checked: stock +20%, benchmark +8% => +11.1111% relative return.
3. Negative benchmark direction checked: stock +10%, benchmark -5% => +15.7895%, not a reversed negative result.
4. Weighted quarterly indexing checked on segments 0–63, 63–126, 126–189, 189–252 with weights 40/20/20/20.
5. Stop ATR bands checked for <0.8, 0.8–1.2, >1.2 daily ATR behavior.

## Important implementation fixes from v1
- SST ADR/ATR/EMA extension risk engine now uses true daily requested data on every chart timeframe.
- Weekly tight state is requested from weekly context; weekly chart visualization remains weekly-only.
- S/R score now uses pivot count + capped touches + recency + proximity, so old far-away zones do not dominate only because of many historical touches.
- S/R break state requires confirmed chart close.
- Optional risk helper added and kept out of Clean default UI.
- Structural stop helper uses the lower edge of the nearest support channel, not the upper edge.
- MVL sector presets added; invalid active sector fails closed.
- Self-history percentile is explicitly not IBD/universe rank and flat-history cases return insufficient history.
- Leader requires configurable absolute 63D RS floor vs primary (default +3%).
- EMA20 state is split into TEST / UNDERCUT / BROKEN instead of close<EMA20 => AVOID.
- Research state renamed RESEARCH FOCUS, not execution/buy.
- RVOL rewritten around selected session, completed-prior-session denominator, exact minute-of-day matching, sample count and stale-cell protection.
- First partial dataset session is excluded as a completed RVOL comparator.
- RVOL session-start detection also keys off a new trading day, so regular-session-only charts still roll sessions correctly.
- Rolling/Weighted signal EMA is only produced on a 1D chart so intraday repeated daily values do not create a fake 10D smoothing line.

## Required Codex final verification
- Pine v6 compile with zero errors for both files.
- Runtime test matrix from CODEX_TASK.md.
- Confirm no plot-count / request-count / object / loop-time runtime errors.
- Validate real-symbol numerical outputs against manual calculations.
- Verify RVOL on regular and extended-hours charts, including early-close/missing-bar behavior.
- Review higher-timeframe repaint behavior and document any developing-current-day dashboard semantics.

If TradingView compiler access is unavailable, report exactly: `BLOCKED: TRADINGVIEW_COMPILER_UNAVAILABLE` and do not claim full completion.