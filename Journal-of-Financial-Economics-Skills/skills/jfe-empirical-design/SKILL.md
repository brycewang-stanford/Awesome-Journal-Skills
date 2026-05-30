---
name: jfe-empirical-design
description: Use when settling the measurement and estimation choices of a Journal of Financial Economics (JFE) manuscript — factor construction, portfolio sorts, Fama-MacBeth/GMM, standard-error clustering, and multiple-testing discipline. Covers the design/estimator layer; for causal identification of corporate-finance effects use jfe-identification.
---

# Empirical Design & Inference (jfe-empirical-design)

## When to trigger

- You sort on a characteristic but have not justified the variable, the breakpoints, or weighting
- You are choosing between Fama–MacBeth, panel regression, and GMM and unsure how to report
- Your standard errors are unclustered, or clustered on one dimension when two are needed
- You have an asset-pricing predictor but no out-of-sample or multiple-testing treatment
- Variable definitions are ad hoc and would not replicate

## The JFE design bar

JFE is known for nuts-and-bolts methodological rigor. Referees scrutinize measurement, estimator choice, standard errors, and inference discipline line by line. The goal is a design that a skeptical expert cannot dismantle on technical grounds. Verify any current data-and-code availability requirements on the official author guidelines.

## Asset pricing

### Factor / portfolio construction
- Justify the sorting variable economically and define it precisely (data source, lag, winsorization).
- State breakpoints (e.g., NYSE breakpoints vs. all-stock) and value- vs. equal-weighting, and show the choice does not drive the result.
- Report turnover and whether the strategy survives plausible transaction costs.

### Cross-sectional inference
- **Fama–MacBeth:** report Newey–West / Shanken-corrected standard errors; state lags.
- **GMM / SDF:** state moment conditions, weighting matrix, and over-identification (J-test).
- Report alphas against standard factor models (e.g., CAPM, FF3, FF5, q-factor) — not a single benchmark.

### Inference discipline
- **Out-of-sample:** show the predictor holds out of sample or in a holdout period.
- **Multiple testing:** when the predictor is one of many candidates, adjust (e.g., FDR / Bonferroni / data-mining-aware thresholds) and say so. Ignoring this is a known JFE red flag.

## Corporate finance

- Define every variable with source, timing, and units; tabulate in a variable-definition table.
- Winsorize/trim consistently and state the rule; show results are not winsorization artifacts.
- Choose fixed effects deliberately (firm, industry-by-year, etc.) and justify what each absorbs.
- **Standard errors:** cluster at the level of correlation in the residuals (often firm and/or time); use two-way clustering when both matter; match the cluster level to treatment assignment for causal designs.
- Report economic magnitudes, not just significance — a coefficient is a number with units.

## Checklist

- [ ] Every variable is defined with source, lag, and transformation
- [ ] Winsorization/trimming rule stated and shown not to drive results
- [ ] Sorting/breakpoint/weighting choices justified and stress-tested
- [ ] Estimator matches the question (FM / GMM / panel FE) and is reported correctly
- [ ] Standard errors clustered/corrected appropriately (often two-way)
- [ ] Alphas reported against multiple benchmark models
- [ ] Out-of-sample and multiple-testing discipline applied for predictors
- [ ] Economic magnitudes interpreted, not just t-stats

## Anti-patterns

- A new factor reported only in-sample, with no multiple-testing acknowledgment
- Standard errors that ignore cross-sectional or time-series correlation
- Breakpoints/weighting cherry-picked to maximize the spread
- Fama–MacBeth without Newey–West or Shanken corrections
- Variable definitions too vague to replicate
- Reporting t-statistics while never stating the economic size of the effect

## Output format

```
【Field】asset pricing | corporate finance
【Estimator】FM / GMM / panel FE / portfolio sort
【SE treatment】cluster dims / NW lags / Shanken
【Benchmarks】[models alphas are measured against]
【Inference discipline】out-of-sample? multiple-testing adjusted?
【Magnitudes stated】yes/no
【Next】jfe-robustness
```
