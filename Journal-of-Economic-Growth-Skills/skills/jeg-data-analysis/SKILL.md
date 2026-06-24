---
name: jeg-data-analysis
description: Use when building or auditing Journal of Economic Growth (JEG) empirical estimates, calibrated growth models, transition paths, cross-country and subnational panels, historical datasets, spatial (Conley) inference, robustness, and reproducibility for growth and comparative-development manuscripts.
---

# Data Analysis (jeg-data-analysis)

## When to trigger

- You are estimating cross-country, panel, historical, or regional growth models
- A theory paper includes calibration, simulation, or transition dynamics
- Results need robustness, decomposition, or sensitivity checks for JEG

## Empirical growth checklist

- Define the growth outcome: level, growth rate, convergence speed, productivity,
  human capital, fertility, technology, institutions, or development outcome.
- Document the unit and horizon: country-year, region-decade, cohort, household,
  firm, or historical panel.
- Separate long-run levels from short-run growth dynamics.
- Show sample construction, merge rules, missingness, and influential observations.
- Use specifications that match the question: convergence regressions, panel FE,
  IV, DID/RDD around reforms, synthetic controls, or structural estimates.

## Theory / calibration checklist

- State calibrated parameters, data moments, and source for each moment.
- Separate targeted from untargeted moments.
- Report transition paths and steady states clearly.
- Stress-test key elasticities, discount rates, depreciation, fertility, human
  capital, and technology parameters.
- Make code reproducible enough to regenerate figures and tables.

## Growth-mechanism audit table

Before drafting results, create a table with:

- **Mechanism**: human capital, fertility, technology, institutions, trade, finance, migration, or OLG channel.
- **Object**: growth rate, income level, TFP, convergence speed, transition path, or welfare.
- **Discipline**: data moment, calibration target, theorem assumption, or identification source.
- **Main sensitivity**: parameter or sample choice most likely to overturn the result.
- **Replication artifact**: code or file that regenerates the exhibit.

If an estimate or simulation does not map to a mechanism row, it is probably not central enough for JEG.

## Spatial and historical inference discipline

Comparative-development empirics at JEG are usually geocoded, which changes the inference defaults:

- Report Conley standard errors at multiple distance cutoffs (e.g., 100/250/500 km) for any gridded or regional outcome; clustered SEs at the modern administrative level are necessary but not sufficient.
- When historical units do not coincide with modern ones, cluster at the historical unit — the level at which the treatment was assigned — and document the crosswalk.
- Pre-empt the critique that persistence t-statistics can be inflated by smooth spatial trends: include flexible geographic controls (latitude-longitude polynomials or macro-region fixed effects) plus a spatial-noise placebo test.
- For very long panels, keep measurement vintages separate: reconstructed pre-1950 series, modern national accounts, and nighttime lights are not interchangeable; show the result within each vintage where feasible.

## Worked vignette — auditing a comparative-development panel

Illustrative setup: 2,400 grid cells in 41 countries; outcome is log light density in 2020; regressor is distance to a historical trade hub; candidate instrument is least-cost-path placement.

- **Unit/horizon**: cell-level cross-section answering a long-run *level* question, so convergence-dynamics machinery is unnecessary; the persistence design applies.
- **Inference**: coefficient 0.21; country-clustered SE 0.05, Conley 250 km SE 0.08, Conley 500 km SE 0.09 — report all three; the claim survives the widest cutoff.
- **Mechanism row**: schooling in 1960 absorbs roughly 40% of the coefficient (illustrative), so human capital becomes a lead exhibit, not a robustness afterthought.
- **Main sensitivity**: dropping cells within 50 km of modern capitals moves the estimate to 0.17; capital proximity goes into the audit table as the result's weakest joint.

## Estimator defaults by growth question

- Long-run level question (deep determinants, persistence) → cross-sectional or grid design + Conley inference + mechanism decomposition.
- Convergence-speed question → panel estimation alert to Nickell bias; system GMM only with instrument-count discipline and Hansen/AR(2) reporting.
- Reform-timing question → modern staggered-adoption DID estimators with pre-trend evidence, never naive TWFE.
- Theory-driven quantitative question → calibrated model with targeted and untargeted moments kept visibly separate.
- Demographic or fertility question → cohort or census microdata aggregated to the mechanism's unit; verify the transition timing is identified by the data rather than assumed by the specification.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JEG (growth) uses cross-country and long-run panels with deep endogeneity; foreground identification and robustness to alternatives.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Output format

```text
[Paper type] empirical / theory / mixed
[Data or model object] ...
[Main estimator/calibration] ...
[Robustness or sensitivity] ...
[Reproducibility gaps] ...
[Next step] jeg-tables-figures
```
