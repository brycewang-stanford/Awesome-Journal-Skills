---
name: bjps-data-analysis
description: Use when executing and reporting the analysis for a British Journal of Political Science (BJPS) manuscript so it survives expert, double-blind review — honest uncertainty, robustness, and triangulation appropriate to quantitative, experimental, or computational work. Guides analysis norms; it does not fabricate results.
---

# Data Analysis (bjps-data-analysis)

BJPS reviewers are methodologically sophisticated, and the journal — a DA-RT signatory — expects the
replication data and code behind every reported result to be deposited at acceptance (see
`bjps-transparency-and-data`). Analyze as if a referee will re-run your code, because the materials
will be public. This skill covers execution and reporting norms; design decisions live in
`bjps-research-design`.

## When to trigger

- Running main and supporting analyses; building the results section
- A reviewer asked for robustness, heterogeneity, or alternative specifications
- Reconciling preregistered vs. exploratory analyses
- Making the analysis reproducible before deposit

## Analysis norms BJPS expects

1. **Report uncertainty honestly.** Confidence/credible intervals, not just stars; the magnitude and
   substantive meaning of the estimate, not just its significance.
2. **Robustness that probes, not decorates.** Show specifications that could *break* the result
   (alternative measures, samples, estimators, fixed effects), and say what you learn.
3. **Heterogeneity with discipline.** Pre-specify subgroups where possible; correct for multiple
   comparisons; do not mine for a significant interaction and theorize it post hoc.
4. **Right inference.** Cluster at the assignment/sampling level; randomization inference for
   experiments; small-cluster corrections (wild-cluster bootstrap) when clusters are few.
5. **Preregistration discipline.** Clearly separate **registered** analyses from **exploratory** ones;
   reconcile deviations from the plan and justify them.
6. **Measurement.** Validate constructs; report reliability; show that results are not an artifact of a
   coding/scaling choice — especially for cross-national measures that must travel across contexts.

## Computational / text-as-data specifics
- Document model/version, hyperparameters, seeds, and validation against human-labeled samples.
- For topic models/embeddings/LLM pipelines: report stability and a validation step; don't treat
  outputs as ground truth.

## Cross-national / comparative specifics
- Check **measurement equivalence** across countries/waves before pooling; report whether constructs
  mean the same thing across contexts.
- Be explicit about what is identified within vs. between units, and where the variation comes from.

## Reproducibility while you work (not at the end)
- One **master script** regenerates every table and figure from the (raw or constructed) data.
- **Set and report seeds** for bootstrap, randomization inference, simulation, and any stochastic step.
- Pin software/package versions (`renv.lock`, `requirements.txt`, recorded `ssc`/`net` installs).
- Keep table/figure numbers in the manuscript matched to script outputs — the package must reproduce them.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). BJPS is comparative/IR-heavy — cross-country panels with confounded institutions; emphasize fixed effects, clustering, and weak-IV-robust inference.

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
- Pooling across countries without checking measurement equivalence
- A results section whose numbers the deposited code cannot reproduce

## Output format

```
【Main estimate】magnitude + interval + substantive meaning
【Identification check】(per research-design) result
【Robustness】specs that could break it → what held
【Heterogeneity】pre-specified? MHT-adjusted?
【Registered vs exploratory】clearly separated?
【Measurement equivalence】(if cross-national) checked?
【Reproducible】master script + seeds + pinned versions? [Y/N]
【Next】bjps-tables-figures
```

## Referee-pushback patterns and the BJPS-specific repair

- *"This reads as a single-case result, not a general one."* → Re-anchor the estimate to the general
  mechanism and show what it implies beyond the studied country before the numbers.
- *"The robustness table only reruns near-identical specs."* → Replace decorative checks with
  specifications that could *break* the result, and say what you learned when they held.
- *"You pooled countries without checking the measure travels."* → Report measurement equivalence; show
  the construct means the same thing across contexts before pooling.
- *"I cannot tell registered from exploratory analyses."* → Segregate them explicitly; the deposited code
  is public via the BJPolS Dataverse, so the split must survive independent re-running.

## Calibration anchors (hedged)

- The bar is **wide political-science interest**, not within-niche novelty: an effect only a country or
  subfield specialist would value rarely clears BJPS review on its own.
- Transparency follows **DA-RT / BJPolS Dataverse** norms — write the analysis so the deposited package
  reproduces every printed number; deposit mechanics can change, so confirm the current policy.

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — estimation, inference, and text-as-data packages
- [`../../resources/code/`](../../resources/code/) — reproducible Stata + Python skeleton to adapt
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — DA-RT / replication-data policy
