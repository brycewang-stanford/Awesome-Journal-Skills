---
name: jhr-data-analysis
description: Use when building or auditing Journal of Human Resources (JHR) empirical pipelines — sample construction, design-based causal estimates with correct clustering, robustness, comparative estimation against prior published work, online appendix material, and reproducible analysis.
---

# Data Analysis (jhr-data-analysis)

## When to trigger

- You are preparing the empirical pipeline for a JHR paper
- Sample construction, reconciliation, or robustness is still unsettled
- The paper needs a replication-ready workflow before acceptance

## Applied-micro analysis checklist

- Define unit, population, period, treatment, comparison group, and outcome.
- Show sample attrition and merge rules.
- Report baseline balance or pre-treatment comparability when relevant.
- Estimate main effects with the right clustering and fixed effects.
- Add reconciliation estimates against the closest prior published work.
- Add robustness for sample windows, functional form, controls, treatment
  definitions, and outlier handling.

## JHR-specific constraints

- Keep main tables inside the page limit; move overflow to Online Appendix.
- Prepare a data-archive plan from the start, especially for restricted data.
- For RCTs, track pre-analysis plan registration and deviations.

## Comparative-estimate workflow

Build one reconciliation table before submission:

| Column | Purpose |
|---|---|
| Prior published estimate | Reproduce or quote the closest estimate with sample/design notes |
| Prior specification on your data | Shows whether the difference is data or specification |
| Your preferred specification | Shows the incremental design or measurement change |
| Sensitivity bridge | Changes one assumption at a time: sample, controls, weights, clustering, outcome |

This table can live in the Online Appendix, but the introduction should summarize the lesson in one
sentence. Without it, a JHR referee can ask for reconciliation late in the process.

## Estimator defaults JHR referees assume

| Design | Default estimator | Diagnostics referees expect alongside |
|---|---|---|
| Staggered DID | Callaway-Sant'Anna, Sun-Abraham, or imputation (Borusyak-Jaravel-Spiess); never TWFE alone with heterogeneous timing | Event study with pre-period coefficients, Goodman-Bacon style decomposition when TWFE is reported |
| Sharp/fuzzy RDD | Local linear with MSE-optimal bandwidth and robust bias-corrected CIs | Density/manipulation test, covariate continuity, bandwidth and donut sensitivity |
| IV | 2SLS plus weak-IV-robust inference when first stage is marginal | First-stage table per endogenous variable, effective F, Anderson-Rubin CI |
| Lottery / admissions experiment | ITT plus LATE via lottery-fixed-effects 2SLS | Balance within randomization strata, compliance and attrition by arm |
| RCT | PAP-aligned ITT with randomization-inference check where feasible | Balance, attrition, multiple-testing adjustment |

## Inference choices that draw referee fire

- Cluster at the level of treatment assignment (state policy → state clusters),
  not at the individual or county level just because N is larger.
- With few treated clusters, add wild cluster bootstrap or randomization
  inference; report how many clusters drive identification.
- Survey-weight decisions must match the estimand: weighted for population
  parameters, unweighted (with justification) for design-based comparisons.
- Show that significance survives the correct clustering before any
  heterogeneity cuts are interpreted.

## Linked-data hygiene

- Document match rates for administrative-survey linkages and show that match
  quality does not differ by treatment status; differential linkage is a
  selection story referees raise unprompted.
- Date-stamp policy adoption variables from primary legal sources; miscoded
  effective dates are a classic catch in JHR rollout papers.

## Worked numbers: postpartum-coverage pipeline

Illustrative pipeline for a Medicaid postpartum-coverage extension paper using
linked birth records (numbers invented for the walkthrough):

1. Sample: 1.9M births, 12 adopting and 19 comparison states; attrition table
   shows 4 percent lost to cross-state moves.
2. Main estimate: Callaway-Sant'Anna ATT of -1.3 severe-morbidity events per
   1,000 births, SE clustered on 31 states, wild-bootstrap p reported.
3. Reconciliation: prior single-state estimate of -3.0 shrinks to -1.6 when its
   specification is run on the multi-state sample — difference is sample, not
   specification; one sentence in the introduction states this.
4. Archive: scripts run end-to-end from a clean clone; restricted birth-record
   access documented for the waiver request.

## Robustness ledger to maintain

```text
Check | Spec changed | Estimate | SE | Verdict | Exhibit
pre-trends        | event study, t-4..t-1   | ... | ... | flat/violated | Fig 2
alt control group | never-treated only      | ... | ... | stable/moved  | App T3
clustering        | state vs state-by-year  | ... | ... | robust/fragile| App T4
sample window     | drop early adopters     | ... | ... | stable/moved  | App T5
prior-spec bridge | prior paper's controls  | ... | ... | reconciled    | App T6
```

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JHR is labor/education economics — program evaluation with selection; DiD/IV/RDD and the selection objection are central.

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
[Sample] unit + population + period
[Design] ...
[Main estimates] ...
[Reconciliation tests] ...
[Archive-readiness gaps] ...
[Next step] jhr-contribution-framing
```
