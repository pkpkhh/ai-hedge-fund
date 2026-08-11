# Codex Review/Debug Task — TradingView Swing Toolkit v2

## Role
The v2 implementation already exists. **Do not redesign or start from scratch.** Treat the current v2 source files as the implementation under review. Your job is to compile, test, debug, and make the smallest necessary corrections until the acceptance contract is met.

Read in this order:
1. `codex_tasks/tradingview-swing-toolkit-v2/CODEX_TASK.md` — full authoritative functional/acceptance specification.
2. `tradingview/Swing_Structure_Toolkit_v2.pine` — completed implementation candidate.
3. `tradingview/Market_Vote_Lab_v2.pine` — completed implementation candidate.
4. `codex_tasks/tradingview-swing-toolkit-v2/PRE_HANDOFF_VALIDATION_v2.md` — checks already performed and remaining gaps.
5. `tradingview/README_TradingView_Toolkit_v2.md` — intended user-facing behavior.

## Required engineering loop
1. Compile both files under Pine Script v6 using the strongest available TradingView/Pine compiler path.
2. Fix compiler errors with minimal diffs; do not remove requested modules just to make compilation pass.
3. Run runtime/timeframe/session/data-error tests from `CODEX_TASK.md`.
4. Numerically spot-check ADR, Rolling RS, Weighted RS, Mansfield and RVOL against manual calculations.
5. Audit repaint/future leakage, especially higher-timeframe data and pivot confirmation.
6. Audit Pine limits: unique requests, plot counts, collections, drawings, loop cost.
7. Review defaults: Clean Mode behavior and six MA slots must remain intact.
8. Review semantic safety: `RESEARCH FOCUS` must never be converted to Buy/A1 Executable; no close<EMA20 automatic AVOID rule.
9. If available, use an independent Sol/reviewer subagent to challenge the implementation and fix real findings.
10. Stop only after every Definition-of-Done item in `CODEX_TASK.md` is explicitly PASS, or after identifying a genuine external blocker.

## Hard rules
- Do not claim compilation was verified unless a real compiler ran.
- If no TradingView compiler is available, report exactly `BLOCKED: TRADINGVIEW_COMPILER_UNAVAILABLE`.
- Preserve attribution/MPL lineage comments.
- Do not add RSI/MACD/Stochastic or extra indicators outside scope.
- Keep at most two primary Pine scripts.
- Prefer correctness and non-repainting behavior over feature count.

## Final output
Commit fixes on `codex/tradingview-swing-toolkit-v2` (or a child branch based on it) and provide:
- files changed
- compiler result
- runtime test matrix
- expected-vs-actual numerical checks
- repaint audit
- resource-limit audit
- remaining limitations
- explicit PASS/FAIL for every DoD item