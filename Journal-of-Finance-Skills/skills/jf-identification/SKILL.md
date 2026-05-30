---
name: jf-identification
description: Use when the causal-identification strategy is the bottleneck for a corporate / empirical The Journal of Finance (JF) manuscript — natural experiments, IV, DID, RDD. Stress-tests the design; for asset-pricing tests use jf-empirical-design.
---

# Causal Identification (jf-identification)

## When to trigger

- The empirical core is OLS + controls and a referee will say "this is endogenous"
- DID uses two-way fixed effects but does not address staggered-adoption / heterogeneous-treatment bias
- IV first stage is weak, or the exclusion restriction is asserted rather than argued
- You claim a treatment is "exogenous" without a research design behind it

> Scope: this skill is for **corporate / empirical finance** causal claims. For cross-sectional or time-series **asset-pricing tests**, route to `jf-empirical-design`.

## What JF rewards (strong → weak)

1. **Natural experiment / policy shock** with a clean source of variation (regulatory change, court ruling, plausibly exogenous reform)
2. **Regression discontinuity** at a sharp institutional threshold (index inclusion cutoffs, covenant triggers, voting thresholds)
3. **Difference-in-differences** with a credible control group and modern estimators for staggered timing
4. **Instrumental variables** with an instrument whose exclusion restriction is defended on institutional grounds
5. **Matching / selection-on-observables** — accepted only with a strong design narrative and sensitivity analysis
6. OLS + rich fixed effects + a candid endogeneity discussion — only when the question is descriptive or no design is feasible

## Branch paths

### Branch A — Natural experiment / DID
- Is treatment timing staggered? If so, address heterogeneous-treatment bias: Goodman-Bacon decomposition; estimators from Callaway & Sant'Anna, Sun & Abraham, or de Chaisemartin & D'Haultfœuille.
- Parallel-trends evidence: event-study plot with pre-period coefficients and 95% CIs.
- Placebo / falsification: pseudo-treatment dates and pseudo-treated units.
- Is the shock plausibly unrelated to the firms' pre-existing trajectory? Argue it, do not assert it.

### Branch B — Regression discontinuity
- Density / manipulation test at the cutoff (McCrary or Cattaneo-Jansson-Ma).
- Optimal bandwidth (Calonico-Cattaneo-Titiunik) plus several bandwidths as sensitivity.
- Covariate continuity at the threshold; no jumps in predetermined characteristics.

### Branch C — Instrumental variables
- First-stage F well above conventional weak-IV thresholds; if weak, report Anderson-Rubin / weak-IV-robust CIs.
- Exclusion restriction argued on three legs: theory, institutional detail, and a falsification test.
- Report the reduced form, not just 2SLS.
- Defend the instrument's own exogeneity (why it does not belong in the outcome equation).

### Branch D — Matching / selection-on-observables
- Show covariate balance after matching.
- Report a sensitivity bound (e.g., Oster's δ for selection on unobservables; Rosenbaum bounds).
- Be explicit that this is the weakest design and frame claims accordingly.

## Checklist

- [ ] The identifying variation is named and its exogeneity is argued, not assumed
- [ ] Parallel trends / density / covariate-balance test appropriate to the design is reported
- [ ] Placebo / falsification test is included
- [ ] Standard errors are clustered at the level of treatment assignment (and two-way where relevant)
- [ ] Staggered DID uses a modern estimator, not bare TWFE
- [ ] Economic magnitude of the estimated effect is interpreted, not just its sign and significance
- [ ] Anticipation / pre-trends and spillover to controls are addressed

## Anti-patterns

- TWFE on staggered treatment with no discussion of heterogeneous-treatment bias
- "Lagged endogenous variable as instrument" — a referee will ask why the lag is excludable
- Asserting "the shock is exogenous to firm decisions" with no evidence
- RDD with a single ad hoc bandwidth and no manipulation test
- Reporting only significance while the implied magnitude is economically trivial

## Output format

```
【Design】natural experiment / DID / RDD / IV / matching
【Identifying variation】...
【Tests done】[parallel trends, placebo, first-stage F, density, balance, ...]
【Tests missing】[...]
【Clustering level】...
【Economic magnitude stated?】yes / no
【Next step】jf-robustness
```
