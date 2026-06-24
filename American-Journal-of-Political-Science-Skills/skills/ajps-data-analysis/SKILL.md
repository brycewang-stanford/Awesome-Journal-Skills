---
name: ajps-data-analysis
description: Use when executing and reporting the analysis for an American Journal of Political Science (AJPS) manuscript. AJPS will have a third-party verifier re-run your exact code against the numerical results in the main text before publication, so analyze reproducibly from the first line. Guides analysis and reporting norms; it does not fabricate results.
---

# Data Analysis (ajps-data-analysis)

AJPS reviewers are methodologically sophisticated, and after acceptance an **independent third-party
verifier re-runs your code** against the numbers in the main text before the article is published (see
`ajps-replication-and-verification`). Analyze as if both facts are true — because they are. This skill
covers execution and reporting; design choices live in `ajps-research-design`.

## When to trigger

- Running main and supporting analyses; building the results section
- A reviewer asked for robustness, heterogeneity, or alternative specifications
- Reconciling preregistered vs. exploratory analyses
- Making the analysis reproducible so the verifier's re-run will match

## Analysis norms AJPS expects

1. **Report uncertainty and magnitude.** Confidence/credible intervals and substantive effect sizes,
   not just significance stars — say what the estimate *means*.
2. **Robustness that probes, not decorates.** Show specifications that could *break* the result
   (alternative measures, samples, estimators, fixed effects) and say what you learn.
3. **Heterogeneity with discipline.** Pre-specify subgroups where possible; adjust for multiple
   comparisons; do not mine for a significant interaction and theorize it post hoc.
4. **Right inference.** Cluster at the assignment/sampling level; randomization inference for
   experiments; wild-cluster bootstrap when clusters are few.
5. **Preregistration discipline.** Separate **registered** from **exploratory** analyses; justify any
   deviation from the plan.
6. **Measurement.** Validate constructs; report reliability; show results are not an artifact of a
   single coding/scaling choice.

## Computational / text-as-data specifics
- Document model/version, hyperparameters, seeds, and validation against human-labeled samples.
- For topic models/embeddings/LLM pipelines: report stability and a validation step; do not treat raw
  outputs as ground truth.

## Reproducibility while you work (so the verifier's re-run matches)
- One **master script** regenerates every table and figure from the (raw or constructed) data, in
  order, setting the working directory once.
- **Set and report seeds** for every stochastic step (bootstrap, randomization inference, simulation,
  jittered plots) — the verifier needs identical draws.
- Record exact **software versions** (e.g., "R 4.3.2", "Stata/MP 18.0") and pin packages
  (`renv.lock` / `requirements.txt` / logged `ssc`/`net` installs).
- Keep the manuscript's table/figure numbers matched to script outputs — the verifier checks the
  **numerical results in the main text** line by line.

## Analysis-decision checklist a quantitative AJPS referee runs

| Question the referee asks | Pass condition | Fix if it fails |
|---------------------------|----------------|-----------------|
| Does the estimator recover the stated estimand? | Estimand named; estimator matches | Name the target quantity before the table |
| Is inference at the right level? | Clustered at assignment/sampling level | Re-cluster; wild-cluster bootstrap if few clusters |
| Will the verifier's re-run match the printed numbers? | Master script regenerates every exhibit | Script everything; set seeds; pin versions |

## Worked micro-example (illustrative numbers)

A survey experiment tests whether a co-partisan endorsement raises policy support. The pre-analysis plan
names the estimand (ITT on a 0-100 scale), the primary contrast, and one moderator (political knowledge).
Result: **+7.4 points (95% CI 3.1-11.7), randomization-inference p = 0.004** *(illustrative)*. A knowledge
interaction that was *not* pre-specified as confirmatory goes to an exploratory subsection, flagged, with a
multiple-comparison note. Every number is emitted by one seeded master script, so the AJPS verifier's
re-run reproduces the main-text figures exactly.

## Referee-pushback patterns and the venue-specific fix

- *"Identification leans on selection-on-observables."* -> Report an unobserved-confounder sensitivity
  bound (how strong a confounder must be to overturn the estimate); soften causal language if fragile.
- *"This interaction looks mined."* -> Show it was pre-registered, or relabel it exploratory and adjust for
  multiple comparisons; never HARK it into a hypothesis.
- *"I cannot reproduce Table 2 from your code."* -> Fatal at AJPS verification; rebuild the master script so
  every number regenerates with fixed seeds and pinned versions.

Calibration anchor: AJPS's independent verifier re-runs deposited code against the main-text numbers before
publication, so "it works on my machine" is not enough — confirm the live verification wording against the
journal's current guidelines.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). AJPS prizes credible identification across American / comparative / IR subfields; DiD/IV/RDD for observational claims, randomization inference for experiments.

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
- Clustering at the wrong level or ignoring few-cluster problems
- Hand-edited numbers in the manuscript that the deposited code cannot regenerate (verification fails)

## Output format

```
【Main estimate】magnitude + interval + substantive meaning
【Identification check】(per research-design) result
【Robustness】specs that could break it -> what held
【Heterogeneity】pre-specified? MHT-adjusted?
【Registered vs exploratory】clearly separated?
【Reproducible】master script + seeds + pinned versions, numbers match? [Y/N]
【Next】ajps-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — estimation, inference, and text-as-data packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — third-party verification of numerical results
