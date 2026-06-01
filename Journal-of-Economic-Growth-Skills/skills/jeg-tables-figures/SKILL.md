---
name: jeg-tables-figures
description: Use when preparing Journal of Economic Growth exhibits: growth-regression tables, convergence plots, transition paths, calibration moments, historical-data maps, robustness tables, and appendix diagnostics.
---

# Tables & Figures (jeg-tables-figures)

## When to trigger

- Main results exist but exhibits do not communicate growth mechanisms
- Calibration or simulation output needs a readable structure
- Empirical tables lack sample, fixed-effect, clustering, or unit notes

## Exhibit architecture

- **Descriptive growth facts**: long-run trends, cross-country dispersion,
  transition paths, or cohort patterns.
- **Main estimates or model results**: one table/figure per claim, not per
  estimator experiment.
- **Mechanism exhibits**: human capital, fertility, technology, institutions,
  financial development, migration, or political economy channels.
- **Robustness/sensitivity**: alternative samples, periods, specifications,
  calibration targets, and parameter values.

## JEG-specific polish

- Use economically meaningful units: annual percentage points of growth, log GDP
  per worker, schooling years, fertility rates, TFP, steady-state ratios.
- Label whether an exhibit is empirical, calibrated, simulated, or theoretical.
- For transition paths, show initial condition, time scale, and steady state.
- For cross-country panels, disclose country coverage and period.

## Output format

```text
[Exhibit] table / figure / appendix
[Claim supported] ...
[Units and sample] ...
[Model/data status] empirical / calibrated / simulated
[Missing note fields] ...
[Next step] jeg-writing-style
```
