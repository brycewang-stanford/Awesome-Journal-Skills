---
name: crim-data-analysis
description: Use when executing and reporting the analysis for a Criminology (ASC / Wiley) manuscript so it survives expert review — honest uncertainty, robustness, and methods appropriate to crime counts, longitudinal panels, trajectory models, and recidivism survival. Guides analysis norms; it does not fabricate results.
---

# Data Analysis (crim-data-analysis)

*Criminology* reviewers are methodologically sophisticated and increasingly expect that your results
can be reproduced from deposited materials (see `crim-data-and-transparency`). Analyze as if both are
true. This skill covers execution and reporting norms; design decisions live in `crim-research-design`.

## When to trigger

- Running main and supporting analyses; building the results section
- A reviewer asked for robustness, heterogeneity, or alternative specifications
- Fitting a trajectory model, fixed-effects panel, count model, or survival model
- Making the analysis reproducible before deposit

## Analysis norms Criminology expects

1. **Report uncertainty honestly.** Confidence/credible intervals, not just stars; the **magnitude and
   substantive meaning** (e.g., incident-rate ratios, predicted counts, change in offending), not just
   significance.
2. **Right model for crime data.** Counts are over-dispersed and zero-heavy — prefer negative binomial /
   zero-inflated / hurdle over OLS on raw counts; rates need exposure offsets; rare-event cautions apply.
3. **Within- vs. between-person.** When the theory is developmental, isolate within-individual change
   (fixed effects / hybrid models); do not interpret a between-person association as a life-course effect.
4. **Trajectory models with discipline.** Report BIC across solutions, group shares, average posterior
   probabilities (AvePP ≥ 0.7), and odds of correct classification; do not over-interpret the group count.
5. **Survival / recidivism.** Handle right-censoring and competing risks; report the relevant hazard, not
   just a binary "recidivated."
6. **Robustness that probes, not decorates.** Show specs that could *break* the result (alternative crime
   measures, samples, estimators, fixed effects) and say what you learn.
7. **Right inference.** Cluster at the assignment/sampling level (often place or agency); randomization
   inference for experiments; few-cluster corrections when clusters are sparse.

## Crime-measurement specifics
- State whether the outcome is reported crime, victimization, or self-report, and how the **dark figure**,
  reporting, and recording changes (e.g., UCR→NIBRS transition) could bias trends.
- Validate scales (self-report delinquency, legitimacy, collective efficacy); report reliability.

## Reproducibility while you work (not at the end)
- One **master script** regenerates every table and figure from the (raw or constructed) data.
- **Set and report seeds** for bootstrap, randomization inference, EM-based trajectory fitting, simulation.
- Pin software/package versions (`renv.lock`, `requirements.txt`, recorded `ssc`/`net`/`traj` installs).
- Keep table/figure numbers matched to script outputs; document restricted-data steps that others can't rerun.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Criminology is observational — place/person panels where selection is pervasive; foreground DiD/IV/RDD and the selection objection.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or
  `benjamini_hochberg` — report the adjusted threshold.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`;
  multilevel data → cluster at the right level.
- **Re-fit off one handle:** `audit_result(result_id)` lists the missing checks and the
  exact `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Keep the decisive checks in the body and the exhaustive battery in the supplement. See
the executed chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- OLS on raw, over-dispersed crime counts; ignoring exposure/offsets
- Stars-only tables with no rate ratios, effect sizes, or intervals
- Treating trajectory groups as literal offender types; cherry-picking the group count
- Reading a between-person coefficient as within-individual desistance
- "Robustness" that only reruns near-identical specs; p-hacking a significant interaction

## Estimator choice keyed to the crime outcome (Criminology decision table)

*Criminology* reviewers are quantitatively literate and will name a mismatch between model and the
data-generating process for offending. Use the outcome to pick the estimator, then defend the
assumption the reviewer will probe.

| Outcome shape | Default estimator | Reviewer will probe |
|---------------|-------------------|---------------------|
| Over-dispersed offense counts | negative binomial w/ exposure offset | dispersion test, offset justification |
| Excess-zero counts (most offend zero times) | zero-inflated / hurdle | what the inflation stage means theoretically |
| Repeated within-person offending | fixed-effects / hybrid panel | within vs. between separation |
| Time-to-recidivism, censored | Cox / competing-risks | proportional hazards, censoring mechanism |
| Developmental offending paths | GBTM / growth mixture | BIC, AvePP ≥ 0.7, group shares not reified |

## Worked micro-example: reading a within-person estimate (illustrative)

Suppose a hybrid model returns an incident-rate ratio of 0.62 on the within-person "employed" indicator
(illustrative): entering employment maps to roughly a 38% lower offending rate *for the same person*,
95% CI [0.49, 0.78], net of stable traits. The between-person column, IRR 0.80, is weaker and reading
it as desistance would conflate selection (people prone to desist also find work) with the within-person
change the life-course claim requires. Report both; tell the reader which identifies the mechanism.

## Analysis-stage referee pushback (with the Criminology fix)

- *"Official-records bias is unaddressed."* Fix: state whether the outcome is arrest, victimization, or self-report, and how the dark figure and UCR→NIBRS recording shifts could bias it.
- *"Between-person read as within-person."* Fix: report and interpret only the fixed-effects/hybrid within column for developmental claims.
- *"Robustness only decorates."* Fix: show a spec that could break the result; say what held.

## Output format

```
【Main estimate】magnitude (IRR / predicted count / hazard) + interval + substantive meaning
【Crime measure】reported / victimization / self-report + dark-figure caveat
【Within vs between】isolated correctly? [Y/N/NA]
【Model fit】counts: dispersion handled? trajectory: BIC/AvePP reported? [Y/N/NA]
【Robustness】specs that could break it → what held
【Reproducible】master script + seeds + pinned versions? [Y/N]
【Next】crim-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — count, trajectory, survival, and spatial packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — transparency expectations and crime-data sources
