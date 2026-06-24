---
name: jfqa-identification-strategy
description: Use when building a credible identification / research design for a Journal of Financial and Quantitative Analysis (JFQA) empirical finance paper — portfolio sorts and Fama-MacBeth, panel fixed effects, staggered DID on regulatory shocks, IV / natural experiments, RDD at thresholds, and event studies — with the inference finance referees demand. For theoretical submissions, pivot to assumptions, results, and proof exposition.
---

# JFQA Identification Strategy (jfqa-identification-strategy)

Use this skill to make the research design defensible for **JFQA**, an empirical and quantitative finance journal. JFQA referees press hard on whether a correlation is causal (or, in asset pricing, whether a premium is robust and not data-mined).

## Empirical finance designs (the common case)

Pick the design that matches the question and defend it:

- **Cross-section of returns** — portfolio sorts and **Fama-MacBeth** regressions; Newey-West / clustered SEs; control for standard factors; report economic magnitudes (return per one-SD change), not only t-stats; guard against data snooping (out-of-sample, multiple-testing awareness).
- **Corporate finance panels** — **firm and time fixed effects**, two-way clustering; show the variation that identifies the coefficient.
- **Policy / regulatory shocks** — **staggered DID** with a modern estimator (Callaway-Sant'Anna, de Chaisemartin-D'Haultfœuille), event-study leads/lags, and parallel-trends evidence; avoid naive TWFE on staggered timing.
- **Natural experiments / IV** — instrument relevance (first-stage F), exclusion logic backed by an economic story, weak-IV-robust CIs.
- **Thresholds / index reconstitution** — **RDD** with manipulation/density tests and bandwidth robustness.
- **Announcements** — **event study** with CARs/BHARs, a defensible market model, and attention to calendar clustering.

## What referees demand

- The right standard errors (clustering dimension justified, two-way where needed).
- Economic significance reported alongside statistical significance.
- Endogeneity confronted explicitly, not waved away with "controls."

## Theoretical submissions

JFQA also publishes theory. If your paper is a model, pivot this skill to: stating **assumptions** transparently, deriving **results/propositions**, clean **proof exposition**, and **testable implications** a finance reader can take to data. Keep generality matched to the question.

## Threat-to-remedy matrix for the JFQA referee report

| Endogeneity threat | How it surfaces in the draft | JFQA-grade remedy |
|---|---|---|
| Reverse causality | outcome plausibly drives the regressor | timing structure, a shock that moves only the regressor, or an IV with an economic exclusion story |
| Omitted firm-level variation | "we control for size and B/M" | firm FE plus a within-firm variation count showing the coefficient is still identified |
| Selection into treatment | treated and control firms differ pre-event | matching or entropy balancing **plus** pre-trend evidence, not either alone |
| Anticipation of regulation | effects appear before adoption | shift the event date, drop the anticipation window, show announcement-date returns |
| Data-mined anomaly | one sort, one sample, large t-stat | sub-period splits, out-of-sample evidence, multiple-testing discussion |
| Bad controls | post-treatment variables on the RHS | re-specify; report with and without, and explain which is the estimand |

## Worked vignette: staggered adoption done the JFQA way (illustrative)

Suppose 23 states adopt a disclosure rule between 2008 and 2016 and the outcome is the credit spread of in-state issuers. A naive TWFE regression gives -4.1%; the Callaway-Sant'Anna group-time ATT gives -2.6% because late-vs-already-treated comparisons inflated the TWFE number. The JFQA presentation: CS estimator as the headline, TWFE relegated to the appendix with the discrepancy explained, an event-study figure whose lead coefficients are jointly insignificant (p = 0.42), and — with only 23 clusters — wild cluster bootstrap inference (p = 0.03) instead of leaning on asymptotics. That package answers the three referee questions (estimator, pre-trends, inference) before they are asked.

## The anomaly-credibility bar in asset pricing

- Acknowledge the multiple-testing problem head-on: the post-2016 factor-zoo literature argues for materially higher t-hurdles for new predictors; state how many specifications were examined.
- Show tradability: turnover, transaction-cost drag, and whether the premium survives value-weighting and the exclusion of microcaps.
- Run spanning tests against the standard factor models in current use; a new "factor" that the existing ones price is a robustness row, not a contribution.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the identification claim, don't only argue it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JFQA is empirical finance (asset pricing + corporate) — the DiD / IV / RDD chain for corporate causal claims, the factor-zoo haircut for cross-sectional pricing.

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
## Output format

```
【Design】sorts/FMB / panel FE / staggered DID / IV / RDD / event study / theory
【Identifying variation】what makes it credible
【Inference】clustering / weak-IV / multiple-testing handling
【Economic magnitude】effect size in finance units
【Next step】jfqa-data-analysis
```
