---
name: jhr-tables-figures
description: Use when preparing Journal of Human Resources (JHR) tables, figures, online appendix exhibits, reconciliation tables, event-study and first-stage diagnostics, and policy-readable empirical displays that fit inside the page limit counting tables and figures.
---

# Tables & Figures (jhr-tables-figures)

## When to trigger

- Results are ready but tables are dense or over the page limit
- You need reconciliation, robustness, or design diagnostics in exhibit form
- The Online Appendix needs a clear structure

## Exhibit plan

- Table 1: sample, descriptive statistics, and key balance where relevant.
- Main table: preferred specification with transparent controls and clustering.
- Design diagnostic: pre-trends, first stage, manipulation, balance, or event
  study depending on design.
- Reconciliation table: compare your estimate to prior estimates and explain the
  bridge.
- Appendix: robustness, sensitivity, alternative samples, and extra outcomes.

## Notes must state

- Unit, sample, period, outcome units
- Fixed effects and controls
- Clustering level
- Treatment definition
- Survey weights or population weights if used
- Page/appendix location

## Main-text exhibit budget

Use the scarce main-text pages for exhibits that change a reader's belief:

1. **Sample and balance**: proves the population and comparison are understandable.
2. **Main estimate with magnitude**: preferred result plus units and confidence interval.
3. **Design diagnostic**: pre-trend, first stage, manipulation test, balance, or attrition.
4. **Reconciliation**: prior estimate vs. your bridge specification vs. preferred specification.
5. **Policy heterogeneity**: only if it maps to a real policy margin, not a fishing cut.

Everything else belongs in the Online Appendix with clear cross-references.

## Appendix map

Organize appendix exhibits by reviewer use, not by the order scripts happen to run:

- **Design validity**: balance, pre-trends, manipulation, attrition, first stage, or placebo evidence.
- **Specification sensitivity**: alternative controls, bandwidths, estimators, samples, weights, and
  clustering levels.
- **Reconciliation**: bridge specifications that explain differences from prior estimates.
- **Mechanism and heterogeneity**: only after the main effect and design validity are clear.
- **Data construction**: variable definitions, sample filters, merges, missingness, and coding decisions.

Each appendix table should be referenced from exactly one main-text claim or robustness sentence. Orphaned
appendix exhibits create page and credibility costs.

## Event-study figure standard

The event-study plot is often the single most scrutinized exhibit in a JHR
design paper. Hold it to this bar:

- Name the estimator in the note (heterogeneity-robust group-time aggregation,
  interaction-weighted, or imputation — not just "event study").
- Reference period marked (usually t = -1) and at least four pre-periods shown
  when the data allow; binned endpoints labeled as bins.
- 95 percent confidence intervals from SEs clustered at the assignment level,
  with the cluster count in the note.
- Y-axis in outcome units, not standardized indices, so the policy reader can
  judge magnitude directly.
- If TWFE and robust estimates diverge, plot both series rather than choosing
  silently.

## First-stage and RD display conventions

- IV papers: a first-stage table adjacent to the 2SLS table — coefficient,
  effective F per endogenous regressor, and the reduced form; referees read
  these three together.
- RD papers: the binned outcome plot and the density plot are a pair; show the
  bandwidth on the figure and put manipulation-test results in the note.
- Lottery papers: a balance exhibit within randomization strata precedes any
  effect figure.

## Worked exhibit ledger

Illustrative ledger for a childcare-subsidy DID paper (titles invented):

```text
Fig 1  Rollout map + timing of county adoption          claim: variation exists
Tab 1  Sample means, adopters vs not, pre-period        claim: comparability
Tab 2  ATT on maternal employment, 3 estimators         claim: main effect
Fig 2  Event study, 5 pre / 6 post, CIs, clusters=42    claim: no pre-trends
Tab 3  Bridge to prior state-level estimate             claim: reconciliation
Tab 4  Heterogeneity by single-parent status            claim: policy margin
App A  Sensitivity: windows, controls, clustering       referenced from Tab 2
```

Seven main exhibits is a sensible ceiling under the page cap; every appendix
entry must be cited from one main-text sentence.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JHR is labor/education economics — program evaluation with selection; DiD/IV/RDD and the selection objection are central.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Output format

```text
[Exhibit] main table / diagnostic / reconciliation / appendix
[Claim] ...
[Required note fields] ...
[Page-limit action] keep / move to appendix / compress
[Next step] jhr-writing-style
```
