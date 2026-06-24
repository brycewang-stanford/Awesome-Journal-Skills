---
name: joc-data-analysis
description: Use when executing and reporting the analysis for a Journal of Communication (JoC) manuscript so it survives expert, double-anonymous review — honest uncertainty, robustness, reliability, and triangulation appropriate to quantitative, computational, or content-analytic work. Guides analysis norms; it does not fabricate results.
---

# Data Analysis (joc-data-analysis)

JoC reviewers are methodologically sophisticated, and the journal **requires a Data Availability
Statement** so others can scrutinize how your numbers were produced (see
`joc-open-science-and-transparency`). Analyze as if both are true — because they are. This skill covers
execution and reporting norms; design decisions live in `joc-research-design`.

## When to trigger

- Running main and supporting analyses; building the results section
- A reviewer asked for robustness, heterogeneity, or alternative specifications
- Reconciling preregistered vs. exploratory analyses
- Making the analysis reproducible before deposit

## Analysis norms JoC expects

1. **Report uncertainty honestly.** Confidence/credible intervals and effect sizes, not just stars or
   p-values; the substantive magnitude and meaning of the estimate.
2. **Robustness that probes, not decorates.** Show specifications that could *break* the result
   (alternative measures, samples, estimators, covariate sets), and say what you learn.
3. **Heterogeneity with discipline.** Pre-specify subgroups where possible; correct for multiple
   comparisons; do not mine for a significant interaction and theorize it post hoc.
4. **Mediation/moderation done right.** For PROCESS/SEM-style models, justify the causal ordering;
   report indirect effects with bootstrap CIs; acknowledge cross-sectional limits on process claims.
5. **Measurement and reliability.** Report scale reliability (e.g., alpha/omega) and, for content
   analysis, **intercoder reliability**; show results are not an artifact of a coding/scaling choice.
6. **Preregistration discipline.** Clearly separate **registered** from **exploratory** analyses;
   reconcile and justify deviations from the plan.

## Computational / text-as-data specifics
- Document model/version, hyperparameters, seeds, and **validation against human-labeled samples**.
- For topic models/embeddings/LLM pipelines: report stability and a validation step; don't treat
  outputs as ground truth.

## Reproducibility while you work (not at the end)
- One **master script** regenerates every table and figure from the (raw or constructed) data.
- **Set and report seeds** for bootstrap, simulation, and any stochastic step.
- Pin software/package versions (`renv.lock`, `requirements.txt`, recorded installs; note Mplus/SPSS versions).
- Keep table/figure numbers in the manuscript matched to script outputs.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Journal of Communication spans experiments, surveys, and content analysis; randomization inference for experiments, DiD/IV for observational media-effects claims.

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
- "Robustness" that only reruns near-identical specs to manufacture stability
- p-hacking / fishing for a significant interaction; HARKing exploratory results into hypotheses
- Reporting a content analysis without intercoder reliability
- A results section whose numbers the code cannot reproduce


## Evidence pass for Journal of Communication

Treat this skill as an executable review pass, not a prose hint. First lock the communication process, platform/media setting, construct measurement, and study design; then judge whether the current manuscript answers the venue's real reader: communication reviewers who balance theory, media context, measurement, and social implications.

- **Do the pass:** Audit the research design before polishing prose: unit of analysis, comparison set, uncertainty, sensitivity, missingness, and reproducibility must be visible.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Communication Research for quantitative communication, New Media & Society for platform focus, Human Communication Research for theory testing; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Main estimate】magnitude + interval + substantive meaning
【Identification/validity check】(per research-design) result
【Robustness】specs that could break it → what held
【Heterogeneity】pre-specified? MHT-adjusted?
【Reliability】scale / intercoder reliability reported?
【Registered vs exploratory】clearly separated?
【Reproducible】master script + seeds + pinned versions? [Y/N]
【Next】joc-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — estimation, reliability, mediation/SEM, and text-as-data packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Data Availability Statement requirement
