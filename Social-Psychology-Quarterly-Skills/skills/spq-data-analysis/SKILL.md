---
name: spq-data-analysis
description: Use when executing and reporting the analysis for a Social Psychology Quarterly (SPQ) manuscript so it survives expert, masked review — honest uncertainty, robustness, sound measurement, and reporting appropriate to experiments, surveys/secondary data, or interpretive analysis in sociological social psychology. Guides analysis norms; it does not fabricate results.
---

# Data Analysis (spq-data-analysis)

SPQ reviewers are sophisticated about both social-psychological measurement and the methods of each
tradition. Analyze and report so an expert can trust the result and see the **structure–individual link**
in the numbers (or the interpretation). This skill covers execution and reporting norms; design decisions
live in `spq-research-design`.

## When to trigger

- Running main and supporting analyses; building the results section
- A reviewer asked for robustness, heterogeneity, alternative measures, or model checks
- Reconciling preregistered (where used) vs. exploratory analyses
- Reporting measurement quality for latent social-psychological constructs

## Analysis norms SPQ expects

1. **Report uncertainty honestly.** Confidence/credible intervals, not just stars; the **magnitude** and
   substantive meaning of the estimate, in the metric of the construct, not just significance.
2. **Measurement quality up front.** For identity salience, mastery, sentiment, status, etc.: report
   reliability (alpha/omega), and where relevant CFA/SEM fit; show the result is not a scaling artifact.
3. **Robustness that probes, not decorates.** Alternative measures, samples, model specifications, or
   estimators that could *break* the result — and say what you learn.
4. **Right inference for the design.** Survey weights/clustering for complex samples; multilevel models
   for individuals nested in groups/contexts; randomization-appropriate inference for experiments;
   multiple-comparison adjustment when testing many implications.
5. **Heterogeneity with discipline.** Pre-specify subgroups where possible; don't mine for a significant
   interaction and theorize it post hoc.
6. **Mediation/mechanism with care.** If you claim the social-psychological mechanism mediates, test it
   properly (modern mediation/sensitivity), and acknowledge the assumptions.

## Interpretive / qualitative specifics
- Make the analytic procedure transparent: coding scheme, how themes/categories were derived, negative cases.
- Show how the evidence (interaction excerpts, fieldnotes, accounts) supports the claim; quote enough to let the reader judge.

## Structure-individual reporting check

For each main result, add one sentence that links the statistic or qualitative pattern back to the
structure-individual mechanism. SPQ results should not stop at "the coefficient is positive" or "a
theme appears"; they should say how status, identity, exchange, networks, institutions, or interaction
orders shape individual meaning or behavior. If that sentence cannot be written, the analysis has
drifted away from the journal's social-psychological core.

## Reproducibility while you work (good practice, not a gate)
- A **master script** that regenerates every table and figure from the (raw or constructed) data.
- **Set and report seeds** for any stochastic step (bootstrap, simulation, multiple imputation).
- Pin software/package versions (`renv.lock`, `requirements.txt`, recorded installs).
- Keep table/figure numbers matched to outputs. SPQ **encourages** sharing materials but does not require
  it (see `spq-data-and-transparency`) — still analyze reproducibly for your own sake and the reviewers'.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). SPQ spans lab/survey experiments and observational work; randomization inference and mediation done right matter for the experimental lane.

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

- Stars-only tables with no effect sizes or intervals
- Reporting an effect on a construct whose reliability/validity is never shown
- "Robustness" that only reruns near-identical specs to manufacture stability
- p-hacking / fishing for a significant interaction; HARKing exploratory results into hypotheses
- Ignoring clustering/weighting in complex-survey or nested-group data
- Quoting one vivid excerpt as if it established a pattern (interpretive work)

## Output format

```
【Main estimate / claim】magnitude + interval (or analytic claim) + substantive meaning
【Measurement】reliability/validity of key constructs reported? [Y/N]
【Inference correct for design?】weighting/clustering/multilevel/randomization [note]
【Robustness】specs that could break it → what held
【Heterogeneity】pre-specified? adjusted?
【Reproducible】master script + seeds + pinned versions? [Y/N]
【Next】spq-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — estimation, measurement (SEM/reliability), and CAQDAS packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — data-and-materials policy (encouraged, not required)
