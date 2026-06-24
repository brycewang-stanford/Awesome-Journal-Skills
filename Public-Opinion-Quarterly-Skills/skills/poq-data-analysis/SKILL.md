---
name: poq-data-analysis
description: Use when executing and reporting the analysis for a Public Opinion Quarterly (POQ) manuscript so it survives expert, double-blind review — design-based inference that respects survey weights, strata, and clusters, honest uncertainty, robustness, and reproducibility. POQ verifies that code reproduces every table and figure. Guides analysis norms; it does not fabricate results.
---

# Data Analysis (poq-data-analysis)

POQ reviewers are methodologically sophisticated, and the journal requires replication materials that
**reproduce exactly all published tables and figures** (see `poq-transparency-and-data-policy`).
Analyze as if both are true — because they are. The defining POQ demand is **design-based inference**:
survey weights, strata, and clusters belong in the variance estimator, not just the point estimate.
Design decisions live in `poq-survey-design-and-measurement`.

## When to trigger

- Running main and supporting analyses; building the results section
- A reviewer asked for design-based SEs, robustness, or alternative weighting
- Reconciling preregistered vs. exploratory analyses
- Making the analysis reproducible before deposit

## Analysis norms POQ expects

1. **Design-based inference.** Use complex-survey estimators (`svy:` / `survey` / `samplics`); declare
   weights, strata, and PSUs. Report the **design effect (DEFF)**; do not present naive IID standard
   errors on a clustered, weighted sample.
2. **Report uncertainty honestly.** Confidence intervals, not just stars; the magnitude and
   substantive meaning of the estimate. For opinion shares, show the margin of error and the
   definition of precision.
3. **Weighted vs. unweighted.** Show both where they diverge and explain why; do not let weighting
   silently drive the headline result.
4. **Robustness that probes, not decorates.** Alternative weighting/calibration, alternative codings,
   sensitivity to nonresponse assumptions, mode controls — specs that could *break* the result.
5. **Heterogeneity with discipline.** Pre-specify subgroups; correct for multiple comparisons; do not
   mine for a significant interaction and theorize it post hoc.
6. **Measurement carries through.** Show the result is not an artifact of a coding/scaling choice;
   report reliability and, where relevant, measurement invariance across groups/modes.

## Missing data, nonresponse & trends
- Distinguish item nonresponse handling (multiple imputation vs. listwise) and report the choice.
- Adjust for nonresponse explicitly; state assumptions (MAR vs. not) and probe sensitivity.
- For trend/Polls-in-Context analyses, hold question wording and mode constant or flag the break.

## Reproducibility while you work (not at the end)
- One **master script** regenerates every table and figure from the (raw or constructed) data.
- **Set and report seeds** for bootstrap, multiple imputation, simulation, and any stochastic step.
- Pin software/package versions (`renv.lock`, `requirements.txt`, recorded `ssc`/`net` installs).
- Keep table/figure numbers matched to script outputs — POQ re-runs the package against the exhibits.

## POQ replication acceptance gate

Before writing results prose, run a local replication gate that mirrors the journal's expectations:

| Gate | Required evidence |
|------|-------------------|
| Survey design object | A single declared object listing weights, strata, PSUs, finite-population corrections where used, and missing-data handling. |
| Table/figure manifest | Every exhibit has a script target, input data file, and output path; no manual spreadsheet edits. |
| Sensitivity queue | Alternative weights, nonresponse adjustments, mode/question wording breaks, and subgroup corrections listed before results are interpreted. |
| Exact reproduction | A clean checkout or temporary directory regenerates all published numbers with matching rounding. |

Only after this gate should the manuscript claim that the analysis is reproducible. POQ readers notice
when design-based inference is described in text but not actually encoded in the scripts.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Public Opinion Quarterly is survey methodology and public opinion; the chain serves causal/experimental claims, while survey-design and measurement contributions use their own standards (sampling, weighting, measurement error).

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

- Naive IID standard errors on a weighted, clustered survey (the most common POQ analysis flaw)
- Stars-only tables with no effect sizes, intervals, or margins of error
- Weighting the estimate but ignoring the weights/design in the variance
- p-hacking / HARKing exploratory subgroup results into hypotheses
- A results section whose numbers the deposited code cannot reproduce

## Output format

```
【Estimator】complex-survey (weights/strata/PSUs declared)? [Y/N]
【Main estimate】magnitude + interval/MOE + substantive meaning
【Design effect】DEFF reported?
【Weighted vs unweighted】reconciled where they differ?
【Robustness】specs that could break it → what held
【Heterogeneity】pre-specified? MHT-adjusted?
【Reproducible】master script + seeds + pinned versions? [Y/N]
【Next】poq-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — complex-survey estimation, weighting, imputation packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — reproducibility / replication-archive policy
