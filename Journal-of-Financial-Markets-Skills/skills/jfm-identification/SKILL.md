---
name: jfm-identification
description: Use when the identification argument is the bottleneck for a Journal of Financial Markets (JFM) manuscript — causal effects on market quality, or what pins down a microstructure model. Stress-tests the design against JFM's microstructure-insider bar before exhibits are finalized.
---

# Identification Strategy (jfm-identification)

## When to trigger

- A causal claim about liquidity, spreads, depth, or price discovery rests on OLS + controls
- An event study uses a window so wide that confounding news or contemporaneous market-wide shocks contaminate it
- A market-structure change is exploited but the parallel-trends / no-anticipation logic is not argued
- Reverse causality is live: liquidity and the regressor (volume, volatility, ownership) are jointly determined
- A microstructure model is fit but it is unclear what *moment in the data* identifies the key parameter (PIN, lambda, adverse-selection share)

## The JFM identification bar

JFM referees know that market-quality variables are **endogenous to almost everything** — volume, volatility, information arrival, and prices co-move mechanically. So the bar is high for any causal liquidity/price-impact claim, and the journal especially rewards designs built on **exogenous changes in market structure**. The credible JFM toolkit is design-based, not control-saturated.

### Branch A: Market-structure natural experiments (the JFM sweet spot)
- **Canonical shocks:** decimalization, the SEC Tick-Size Pilot (2016-18), Reg NMS, MiFID/MiFID II, short-sale bans, circuit-breaker/LULD triggers, venue entry/exit, fee/rebate (maker-taker) changes, tick-size regime changes.
- **Design:** DiD across affected vs. unaffected stocks/venues; RDD at a price/market-cap threshold (e.g., tick-size eligibility); event study around a known implementation date.
- **With staggered timing,** move beyond TWFE (Callaway-Sant'Anna, Sun-Abraham, de Chaisemartin-D'Haultfœuille); show clean pre-trends in spreads/depth; cluster at the assignment level (stock/venue), not the observation.

### Branch B: Intraday / high-frequency event studies
- Tight, pre-registered windows around a discrete event (an order-type launch, a latency upgrade, a halt). Justify the window from market mechanics, not from where the effect is biggest.
- Control for **market-wide microstructure shocks** (index moves, scheduled macro releases) and for the diurnal (U-shaped) intraday pattern in spreads/volume.

### Branch C: Instruments for liquidity / order flow
- Honest about weak instruments: report first-stage F, use Anderson-Rubin / weak-IV-robust sets. Defend exclusion in market-mechanism terms (the instrument moves trading frictions only through the channel claimed).

### Branch D: Structural microstructure models
- Tie each parameter to an identifying data feature: adverse-selection component from the permanent price impact / spread decomposition; PIN from the trade-imbalance distribution; Kyle's lambda from the price-impact regression. State estimator (MLE/GMM), and show the parameter is not just a fit artifact.

## Referee pushback mapped to the identification fix

- *"Liquidity and your regressor are jointly determined."* → Replace the panel regression with an exogenous market-structure shock (DiD/RDD), or a defensible IV; show the result is not a mechanical co-movement with volume/volatility.
- *"Your staggered TWFE is biased with heterogeneous effects."* → Re-estimate with Callaway-Sant'Anna or Sun-Abraham; plot flat pre-event leads in spreads/depth.
- *"The event window is cherry-picked."* → Justify the window from market mechanics (settlement, implementation date), show robustness to nearby windows, and rule out contemporaneous macro releases.
- *"What identifies PIN/lambda?"* → Point to the data moment (trade-imbalance distribution; permanent price impact) and report estimation diagnostics, not just the point estimate.
- *"Your control group is contaminated."* → Show the control stocks/venues were not indirectly affected (e.g., order flow migrating from treated to control); report a clean, unaffected comparison or a spillover-robust design.

## Separating mechanical from behavioral effects

A recurring identification subtlety in market-structure work is that a rule change has both a **mechanical** effect (a wider tick arithmetically widens the minimum quotable spread) and a **behavioral** effect (liquidity suppliers and informed traders re-optimize). A credible JFM design isolates the behavioral channel, because the mechanical one is not a finding. Show the effect on stocks where the tick does not bind, decompose the spread change into the binding-tick component and the residual, or condition on pre-period spread relative to the new tick. Conflating the two is a frequent reviewer catch.

## Worked vignette: the tick-size pilot (illustrative)

The SEC Tick-Size Pilot widened the quoting/trading increment for a randomized set of small-cap stocks. This is close to an ideal JFM design: random treatment assignment, a discrete date, and a treated/control split. The clean identification statement is one sentence — *the effect of a wider tick on depth is identified by the random assignment of stocks to the pilot's test groups.* The credible version shows flat pre-pilot trends in depth, estimates with assignment-level clustering, and separates the mechanical (tick-binding) effect from the behavioral (liquidity-supply) response. A weak version regresses depth on a post-dummy with controls and calls it causal.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the identification claim, don't only argue it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JFM is market microstructure and asset pricing — liquidity, price discovery, and cross-sectional return tests where the factor-zoo multiple-testing haircut is salient.

1. `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result` to list
   the checks the design still owes.
2. **Staggered DiD:** `callaway_santanna` / `sun_abraham` + `bacon_decomposition` +
   `honest_did_from_result` (the pre-trend test is low-power, Roth 2022).
3. **IV:** `effective_f_test` + an `anderson_rubin_ci` (valid under weak instruments),
   not a 2SLS t-stat alone.
4. **RDD:** `rdrobust` (bias-corrected) + `rddensity` / `mccrary_test` for manipulation.
5. **OVB:** `oster_delta` / `sensemakr` — how strong a confounder would have to be.

Report the economic magnitude; route the full battery to the appendix; keep every
number reproducible. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md). If StatsPAI/Stata are not connected, adapt the
vendored `resources/code/` skeleton and flag any unverified number.
## Checklist

- [ ] Branch chosen; the data-to-effect (or data-to-parameter) mapping stated in one sentence
- [ ] Endogeneity of the liquidity/flow variable explicitly addressed, not assumed away
- [ ] Market-structure design: clean pre-trends, modern staggered estimator, assignment-level clustering
- [ ] Intraday events: window justified from mechanics; diurnal pattern and market-wide shocks controlled
- [ ] IV: first-stage strength reported; exclusion defended in microstructure terms
- [ ] Structural: each parameter tied to an identifying moment; estimator and inference stated
- [ ] The causal claim never exceeds what the design supports

## A catalog of clean market-structure shocks

Knowing the field's natural experiments speeds design. Commonly exploited exogenous changes, each with its own caveats: **decimalization (2001)** — tick size from sixteenths to pennies; **the SEC Tick-Size Pilot (2016-18)** — randomized, the cleanest assignment; **Reg NMS (2007)** — order protection and access fees; **MiFID (2007) / MiFID II (2018)** — European venue competition and transparency; **short-sale bans (2008, and country-specific)** — abrupt constraint changes; **maker-taker / fee pilots** — rebate structure; **circuit breakers / LULD** — discrete trading halts; **index reconstitutions** — forced, scheduled order flow; **venue launches/closures and dark-pool entry**. For each, the identification hinges on (a) whether assignment is plausibly exogenous to the stock's liquidity trajectory and (b) whether a clean control group exists. Argue both explicitly; a shock is not self-justifying.

## Anti-patterns

- "Liquidity → outcome" from a panel regression with controls, called identification
- TWFE on a staggered tick-size / decimalization rollout with no heterogeneity-bias discussion
- An event window chosen to maximize significance rather than from market mechanics
- Ignoring the intraday U-shape so that time-of-day masquerades as the treatment effect
- Reporting a PIN/lambda estimate without saying what moment in the data moves it

## Inference choices that travel with the design

Identification is not finished until inference matches the data structure. Microstructure panels are correlated in two dimensions — the same stock is autocorrelated over time and all stocks co-move on a given day — so single-clustered or plain OLS standard errors overstate precision. Default to **two-way clustering by stock and by day**; use **Newey-West** when the time-series autocorrelation is the dominant concern; use a **wild-cluster bootstrap** when the number of treated venues or events is small (few-cluster bias). For event studies, account for cross-sectional correlation in abnormal liquidity across the event window. State the choice and its rationale where the design is described, not as an afterthought — a referee reads the clustering as part of the identification claim.

## Output format

```text
【Journal】Journal of Financial Markets (JFM)
【Skill】jfm-identification
【Branch】market-structure NE / intraday event / IV / structural
【Data-to-effect mapping】one sentence
【Identifying variation】<shock / window / instrument / moment>
【Endogeneity handled】how liquidity/flow endogeneity is broken
【Inference】clustering level + (if needed) weak-IV-robust set
【What it does NOT identify】<…>
【Source status】verified URL / 待核实 / not asserted
【Next skill】jfm-empirical-design
```
