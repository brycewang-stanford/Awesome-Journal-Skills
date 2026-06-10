---
name: jbf-data-analysis
description: Use when building or auditing the empirical data and estimation pipeline for a Journal of Banking & Finance manuscript, including financial datasets, bank panels, winsorization, fixed effects, robustness, and reproducible scripts.
---

# Data Analysis (jbf-data-analysis)

## When to trigger

- You are constructing the sample, variables, or estimation pipeline
- Results need robustness, heterogeneity, mechanism, or economic-magnitude checks
- Proprietary finance datasets require a reproducible but non-redistributable workflow

## Data construction

1. **Document every source**: CRSP, Compustat, Call Reports, BankFocus, Dealscan,
   TRACE, OptionMetrics, FDIC, SEC EDGAR, FRED, or private hand-collected data.
2. **Define the unit of observation**: bank-quarter, firm-year, loan facility,
   security-day, country-year, event-firm, etc.
3. **Show sample attrition**: raw data, filters, merges, missing variables,
   winsorization, final sample.
4. **Name variable construction rules**: scaling, deflation, lagging, exchange
   rates, identifiers, and industry/bank classifications.
5. **Separate proprietary raw data from shareable code** so the replication
   package can be legal and useful.

## Estimation checklist

- Use fixed effects and clustering that match the design.
- Report economic magnitudes in finance units: basis points, percentage of assets,
  capital ratio points, loan-spread basis points, abnormal returns, default odds.
- Provide robustness over winsorization, sample windows, variable definitions, and
  alternative outcome measures.
- For event studies, report CAR/BHAR windows and benchmark choices.
- For bank panels, test sensitivity to crisis periods, large banks, mergers, and
  regulatory regime changes.

## Reproducibility

- Keep a single `run_all` entry point that regenerates tables and figures.
- Pin software versions and random seeds.
- Store intermediate files only when they materially reduce runtime; document how
  they are made.
- Prepare a data-access README for licensed sources.

## Bank-panel stress checks

For bank/intermediation panels, add targeted checks for:

- crisis-period sensitivity;
- large-bank or systemically important institution influence;
- mergers and identifier breaks;
- regulatory regime changes;
- balance-sheet scaling and winsorization choices.

Report which checks are main-text, appendix, or archive-only.

## Output format

```text
[Sample] unit + period + observations
[Data sources] ...
[Key variables] ...
[Main estimator] ...
[Robustness queue] ...
[Reproducibility gaps] ...
[Next step] jbf-tables-figures
```
