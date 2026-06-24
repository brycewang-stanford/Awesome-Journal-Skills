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

## Dataset-to-question matrix

| Source | Unit | JBF expectation | Caveat to pre-empt |
| --- | --- | --- | --- |
| US Call Reports / FR Y-9C | bank- or BHC-quarter | merger-adjusted series; top-holder aggregation choice stated | identifier breaks across RSSD changes |
| Orbis Bank Focus (ex-BankScope) | bank-year, cross-country | consolidation-code filters documented | duplicated statements across consolidation levels |
| DealScan | loan facility | facility vs package level stated; lead-arranger roles defined | borrower link tables need documented match rates |
| FDIC SDI / failure data | bank-quarter | survivorship handling for failed and acquired banks | de novo entrants and charter conversions |
| Cross-country regulation surveys | country-wave | survey-wave timing matched to the outcome window | self-reported regulation measures |

## Worked sample build (illustrative)

Target: bank-quarter panel for a liquidity-regulation study, 2005Q1–2019Q4.

- Raw Call Reports: 612,000 bank-quarters (illustrative count).
- Drop de novo banks (<5 years), foreign branches, and banks under $100 million in assets: −118,000.
- Merger-adjust around RSSD changes; drop quarters with >50% asset jumps: −24,000.
- Require non-missing CET1, loans, and core deposits; winsorize ratios at 1/99: final ≈465,000.
- Put exactly this attrition table in the appendix — JBF referees read it before the regressions.

## Pipeline skeleton

```text
01_pull_callreports.*   # raw downloads, data vintage recorded
02_merger_adjust.*      # RSSD link table + asset-jump audit
03_build_panel.*        # ratios, lags, winsorization flags
04_baseline.*           # FE + clustering per jbf-identification-strategy
05_robustness.*         # crisis splits, large-bank drops, alt definitions
06_export_exhibits.*    # tables/figures numbered as in the manuscript
```

## Economic-magnitude benchmarks for bank panels

- Loan growth: report effects relative to sample-mean quarterly growth, not only the raw coefficient.
- Capital: percentage points of CET1, anchored to the regulatory minimum or buffer.
- Spreads: basis points relative to the mean all-in-drawn spread.
- Risk: change in Z-score or NPL ratio relative to the cross-sectional standard deviation.
- Funding: percentage points of the core-deposit or wholesale-funding share.

## Referee data pushbacks

- "Are results a 2008–09 artifact?" → re-estimate excluding 2007Q3–2009Q4 and report both estimates.
- "Bank Focus duplicates inflate your N." → show the consolidation-filter step with before/after counts.
- "DealScan spreads ignore fees." → use the all-in-drawn spread and say so in the variable definitions.
- "Winsorizing at 1/99 hides outliers." → also show 2.5/97.5 and trimmed samples in an appendix column.
- "Results hinge on the largest banks." → report with and without the systemically important institutions.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JBF is empirical banking/finance — corporate/bank causal designs around regulation and shocks.

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
[Sample] unit + period + observations
[Data sources] ...
[Key variables] ...
[Main estimator] ...
[Robustness queue] ...
[Reproducibility gaps] ...
[Next step] jbf-tables-figures
```
