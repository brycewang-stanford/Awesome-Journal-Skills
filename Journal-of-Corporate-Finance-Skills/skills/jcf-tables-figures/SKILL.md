---
name: jcf-tables-figures
description: Use when building the tables and figures for a Journal of Corporate Finance (JCF) empirical paper — summary statistics, main regression tables with fixed effects and clustering disclosed, event-study/CAR plots, and self-contained notes. It shapes the exhibits; pair with jcf-data-analysis for the underlying estimates.
---

# Tables & Figures (jcf-tables-figures)

## When to trigger

- Designing the summary-statistics, main-result, and robustness tables
- Building event-study or CAR figures with confidence bands
- Writing self-contained table/figure notes a reviewer can read without the text

## Table conventions (empirical corporate finance)

- **Summary statistics**: N, mean, SD, key percentiles; flag winsorizing and units. Match the sample to the regression sample.
- **Main regression tables**: coefficients with standard errors (or t-stats) clearly labeled; report the **fixed effects included**, the **clustering level**, N, and within/adjusted R². Show **economic magnitude** (e.g., a 1-SD change) near the headline coefficient.
- **Robustness tables**: vary one thing per panel/column (definition, subsample, FE, estimator) so the reader sees what moves the result.
- Use a consistent decimal precision; do not hide the dependent variable's scaling.

## Figure conventions

- **Event-study / CAR plots**: plot coefficients (or cumulative abnormal returns) with **confidence bands**; mark the event date; show **pre-event leads** to support parallel trends.
- Binned scatters for nonlinearity; avoid 3D, gradients, and chartjunk.
- **Vector output (PDF/EPS)** for print resolution.

## Self-contained notes (required)

Each exhibit's note states: sample and period, variable definitions or a pointer, **fixed effects**, **clustering**, winsorizing, and significance markers. A referee should not need the body text to read the table.

## Formatting and policy

- "Your paper, your way" at first submission means exhibit styling need only be **consistent**; full Elsevier styling comes at revision.
- Tables/figures count toward the paper's exhibits but JCF states **no fixed length ceiling** (待核实) — still, keep the set tight and non-redundant.

## Anti-patterns

- A regression table that hides the FE and clustering structure.
- "Stars only" with no economic magnitude.
- Event-study plots without confidence bands or pre-trend leads.
- Summary stats computed on a different sample than the regressions.

## Output

```
【Tables】headline FE/cluster/N disclosed? [Y/N]; magnitude shown? [Y/N]
【Figures】event/CAR with CIs + leads? [Y/N]; vector output? [Y/N]
【Notes】each exhibit self-contained? [Y/N]
```
