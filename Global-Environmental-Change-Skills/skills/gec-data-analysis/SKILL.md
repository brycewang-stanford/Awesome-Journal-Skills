---
name: gec-data-analysis
description: Use when executing and reporting the analysis for a Global Environmental Change (GEC) manuscript so it survives expert, interdisciplinary review — honest uncertainty, robustness, and triangulation appropriate to quantitative, qualitative, or mixed-methods work. Guides analysis norms; it does not fabricate results.
---

# Data Analysis (gec-data-analysis)

GEC reviewers span disciplines and are demanding about rigor on each tradition's own terms. The analysis
must deliver the test the framework (`gec-conceptual-framework`) and design (`gec-research-design`) set
up, and report it so a reader in another discipline can judge it. This skill covers execution and
reporting norms across methods.

## When to trigger

- Running main and supporting analyses; building the results section
- A reviewer asked for robustness, heterogeneity, alternative measures, or qualitative depth
- Reconciling quantitative and qualitative strands in a mixed-methods paper
- Making the analysis reproducible before deposit (see `gec-submission`)

## Analysis norms GEC expects

1. **Report uncertainty honestly.** Confidence/credible intervals and effect magnitudes, not just
   stars; the substantive meaning of the estimate for the human/policy question.
2. **Robustness that probes, not decorates.** Show specifications that could *break* the result
   (alternative measures, samples, estimators, fixed effects, scale of aggregation), and say what you learn.
3. **Heterogeneity with discipline.** Pre-specify subgroups where possible (e.g., by vulnerability,
   region, income); correct for multiple comparisons; avoid mining and post-hoc theorizing.
4. **Right inference.** Cluster at the assignment/sampling level; address spatial autocorrelation;
   use small-cluster corrections when clusters are few.
5. **Measurement.** Validate constructs (vulnerability indices, governance measures, attitude scales);
   report reliability; show results are not an artifact of a coding/scaling/weighting choice.

## Qualitative & mixed-methods analysis
- For qualitative work, show the **coding scheme, intercoder agreement where relevant, and evidence
  trail** from data to interpretation; quote enough to let readers judge.
- For mixed methods, present the **integration** (joint displays, triangulation) and interpret
  convergence *and* divergence — do not report two parallel papers.

## Reproducibility while you work (not at the end)
- One **master script / documented workflow** regenerates every table and figure from the data.
- **Set and report seeds** for any stochastic step (bootstrap, simulation, randomization inference).
- Pin software/package versions (`renv.lock`, `requirements.txt`, recorded installs).
- Prepare the **Data Availability Statement** and a clean archive as you go (see `gec-submission`).

## Anti-patterns

- Stars-only tables with no effect sizes or intervals
- "Robustness" that only reruns near-identical specs to manufacture stability
- p-hacking / fishing for a significant interaction; HARKing exploratory results into hypotheses
- Qualitative claims with no visible evidence trail; mixed methods that never integrate
- A results section whose numbers the workflow cannot reproduce

## Output format

```
【Main result】magnitude + interval (or qualitative finding) + substantive meaning
【Identification / evidence check】(per research-design) result
【Robustness】specs that could break it → what held
【Heterogeneity】pre-specified? MHT-adjusted?
【Integration】(mixed methods) convergence/divergence interpreted?
【Reproducible】workflow + seeds + pinned versions? [Y/N]
【Next】gec-figures-and-tables
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — estimation, inference, qualitative, and mixed-methods tools
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Elsevier research-data policy notes
