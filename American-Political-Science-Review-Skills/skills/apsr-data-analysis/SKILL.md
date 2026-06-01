---
name: apsr-data-analysis
description: Use when executing and reporting the analysis for an American Political Science Review (APSR) manuscript so it survives expert, double-anonymous review — honest uncertainty, robustness, and triangulation appropriate to quantitative, experimental, or computational work. Guides analysis norms; it does not fabricate results.
---

# Data Analysis (apsr-data-analysis)

APSR reviewers are methodologically sophisticated and the editorial office will later **re-run your
code** against the manuscript's tables and figures (see `apsr-transparency-and-data-policy`). Analyze
as if both are true — because they are. This skill covers execution and reporting norms; design
decisions live in `apsr-research-design`.

## When to trigger

- Running main and supporting analyses; building the results section
- A reviewer asked for robustness, heterogeneity, or alternative specifications
- Reconciling preregistered vs. exploratory analyses
- Making the analysis reproducible before deposit

## Analysis norms APSR expects

1. **Report uncertainty honestly.** Confidence/credible intervals, not just stars; the magnitude and
   substantive meaning of the estimate, not just its significance.
2. **Robustness that probes, not decorates.** Show specifications that could *break* the result
   (alternative measures, samples, estimators, fixed effects), and say what you learn.
3. **Heterogeneity with discipline.** Pre-specify subgroups where possible; correct for multiple
   comparisons; do not mine for a significant interaction and theorize it post hoc.
4. **Right inference.** Cluster at the assignment/sampling level; randomization inference for
   experiments; small-cluster corrections (wild-cluster bootstrap) when clusters are few.
5. **Preregistration discipline.** Clearly separate **registered** analyses from **exploratory**
   ones; reconcile deviations from the plan and justify them.
6. **Measurement.** Validate constructs; report reliability; show that results are not an artifact of
   a coding/scaling choice.

## Computational / text-as-data specifics
- Document model/version, hyperparameters, seeds, and validation against human-labeled samples.
- For topic models/embeddings/LLM pipelines: report stability and a validation step; don't treat
  outputs as ground truth.

## Reproducibility while you work (not at the end)
- One **master script** regenerates every table and figure from the (raw or constructed) data.
- **Set and report seeds** for bootstrap, randomization inference, simulation, and any stochastic step.
- Pin software/package versions (`renv.lock`, `requirements.txt`, recorded `ssc`/`net` installs).
- Keep table/figure numbers in the manuscript matched to script outputs — the editors will check.

## Anti-patterns

- Stars-only tables with no effect sizes or intervals
- "Robustness" that only reruns near-identical specs to manufacture stability
- p-hacking / fishing for a significant interaction; HARKing exploratory results into hypotheses
- Clustering at the wrong level or ignoring few-cluster problems
- A results section whose numbers the code cannot reproduce

## Output format

```
【Main estimate】magnitude + interval + substantive meaning
【Identification check】(per research-design) result
【Robustness】specs that could break it → what held
【Heterogeneity】pre-specified? MHT-adjusted?
【Registered vs exploratory】clearly separated?
【Reproducible】master script + seeds + pinned versions? [Y/N]
【Next】apsr-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — estimation, inference, and text-as-data packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — reproducibility-verification policy
