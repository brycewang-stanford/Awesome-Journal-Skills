---
name: jbf-tables-figures
description: Use when preparing Journal of Banking & Finance (JBF) tables and figures — descriptive statistics, regression tables, event-study plots, mechanism and heterogeneity exhibits, appendix robustness inventories, and self-contained notes that report sample, fixed effects, clustering, and units.
---

# Tables & Figures (jbf-tables-figures)

## When to trigger

- Main empirical results exist but the exhibits are hard to read
- You need JBF-ready descriptive, regression, event-study, or robustness tables
- Figure and table notes do not identify sample, fixed effects, clustering, or units

## Exhibit architecture

1. **Table 1: sample and summary statistics.** Include variable definitions,
   units, winsorization, and observation counts.
2. **Table 2: baseline results.** Build from sparse to saturated specifications
   so readers can see identifying variation.
3. **Table 3: identification checks.** Pre-trends, placebo outcomes, alternative
   fixed effects, alternative clustering, or IV first stage.
4. **Table 4: mechanisms and heterogeneity.** Tie each split to banking/finance
   theory, not to fishing.
5. **Appendix tables: robustness inventory.** Alternative samples, definitions,
   windows, and estimation methods.

## Figures that work for JBF

- Event-study coefficient plots with confidence intervals and a clear omitted period
- Sample-selection flow charts for complex merges
- Binned scatter or marginal-effect plots for nonlinear mechanisms
- Time-series plots for policy shocks, treatment timing, or market conditions

## Table notes

Every regression table note should state:

- Dependent variable and units
- Sample and period
- Fixed effects
- Clustering level
- Controls
- Treatment or event-window definition
- Stars or confidence-interval convention

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JBF is empirical banking/finance — corporate/bank causal designs around regulation and shocks.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- Ten nearly identical coefficient columns with no specification logic
- Statistical significance without economic magnitude
- Appendix robustness that is impossible to map back to the main claim
- Figure axes with undefined units

## JBF exhibit calibration

Accepted JBF empirical papers commonly carry roughly six to nine main-text exhibits — summary statistics, baseline, identification diagnostics, mechanism/heterogeneity, and one or two robustness pieces — with deeper batteries in an appendix (a stylized norm, not a journal rule). Event-study figures usually earn main-text space when the design is staggered adoption; pure robustness plots rarely do.

## Worked magnitude conversion (illustrative)

Suppose the baseline coefficient on a post-LCR × exposure interaction is −0.014 with loans/assets as the outcome.

- A one-standard-deviation exposure (0.6, illustrative) implies −0.014 × 0.6 = −0.84 percentage points of loans/assets.
- Against a sample-mean loans/assets of 62%, that is a 1.4% relative decline; against mean quarterly loan growth of 1.1%, it is most of one quarter's growth.
- Put the conversion in the results text and the benchmarks (mean, SD) in Table 1 so the table note can stay short.

## Regression table skeleton

```text
Table X: [Outcome] and [treatment], bank-quarter panel
               (1)       (2)       (3)       (4)
Treat x Post   b/se      b/se      b/se      b/se
Controls       No        Yes       Yes       Yes
Bank FE        Yes       Yes       Yes       Yes
Quarter FE     Yes       Yes       --        Yes
State x Qtr FE --        --        Yes       --
Cluster        Bank      Bank      State     State
N / R2         ...
Note: sample, period, units, winsorization, FE, clustering, star convention.
```

Columns must encode a specification logic (sparse → saturated → alternative FE and clustering), not a sensitivity dump.

## Figure conventions for bank panels

- Event-study plots: mark the omitted period, shade confidence intervals, and date both announcement and implementation when they differ.
- Treatment-rollout plots: show adoption timing across states or countries for staggered designs so readers see the control pool.
- Bunching or density plots around supervisory asset thresholds whenever a cutoff design is used.
- Sample-attrition flowcharts when merging Call Reports with DealScan-style loan data; match the counts to the attrition table.

## Referee exhibit complaints

- "I cannot reconstruct N across columns." → report observations per column, not once per table.
- "Stars without magnitudes." → add a standardized-effect or economic-magnitude row.
- "Appendix Table A12 contradicts Table 3." → audit the specification map before resubmission; mismatches read as carelessness.

## Exhibit economy

Keep the main exhibit set to: sample/table 1, baseline, identification check, mechanism, and one decisive
robustness table. Move specification inventories to the appendix and make the appendix map back to the main
claim so reviewers can audit without rereading the whole paper.

## Output format

```text
[Main exhibit claim] ...
[Table/Figure role] baseline / identification / mechanism / robustness
[Required note fields] sample, FE, clustering, units, controls
[Missing diagnostics] ...
[Next step] jbf-contribution-framing or jbf-writing-style
```
