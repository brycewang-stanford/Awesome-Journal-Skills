---
name: jeg-data-analysis
description: Use when building or auditing Journal of Economic Growth empirical estimates, calibrated growth models, transition paths, cross-country panels, historical datasets, robustness, and reproducibility.
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

## Output format

```text
[Paper type] empirical / theory / mixed
[Data or model object] ...
[Main estimator/calibration] ...
[Robustness or sensitivity] ...
[Reproducibility gaps] ...
[Next step] jeg-tables-figures
```
