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

## Exhibit architecture (calibration, hedged)

Accepted empirical JCF papers tend to follow a recognizable arc — treat the counts as calibration, not rules, and confirm against the journal's current author guidelines:

- Table 1: sample construction and/or summary statistics on the regression sample.
- Table 2: main fixed-effects estimates, sparse controls first, saturated last.
- Tables 3–4: identification exhibits — event-study dynamics, pre-trends, first stage, or density tests.
- Tables 5+: mechanism splits and robustness, one varied dimension per panel.
- Figure 1 is frequently the event-study or RDD plot — many JCF readers judge identification from this figure alone.
- Six to nine main exhibits is a common footprint; overflow robustness belongs in an appendix or internet appendix numbered IA.1, IA.2, and cited by number in the text.

## Worked headline-table sketch

Illustrative skeleton for a governance-shock paper (numbers invented):

```text
                       (1)        (2)        (3)
Treated x Post        0.014**    0.015**    0.013**
                     (0.006)    (0.006)    (0.006)
Firm FE                 Y          Y          Y
Year FE                 Y          —          —
Industry x Year FE      —          Y          Y
Controls                —          —          Y
N                    21,043     21,043     20,877
Within R²             0.08       0.11       0.12
Magnitude: 1 SD of treatment exposure ≈ 12% of mean investment
```

The magnitude line beneath the table body is the JCF habit worth copying — it answers "is this economically big?" before the referee asks.

## Exhibit pushback and the fix

- "I cannot tell what is clustered." → Put FE and clustering rows in every regression table, not in a global footnote.
- "The event-study figure has no bands." → Re-plot with 95% CIs and at least four pre-period leads visible.
- "Summary stats do not match the regression N." → Recompute Table 1 on the estimation sample; reconcile any drop in a sample-construction panel.
- "Too many tables." → Merge robustness variants into panels; push the remainder to the internet appendix and cite IA numbers in the text.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JCF is corporate finance — endogeneity of corporate policies is the central threat; foreground IV/DiD identification.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
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
