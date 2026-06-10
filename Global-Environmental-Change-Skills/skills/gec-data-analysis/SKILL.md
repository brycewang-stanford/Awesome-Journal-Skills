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

## What interdisciplinary GEC referees check, by strand

GEC sends papers to reviewers from more than one tradition, so the analysis is judged twice — once for technical correctness and once for whether the human-dimensions claim is earned. Use this as a self-audit before submission.

| Strand | The reviewer's first probe | Pass signal at GEC |
|--------|---------------------------|--------------------|
| Quantitative | "Is the inference level right, and does the effect mean anything socially?" | Clustered/spatially-corrected SEs plus a sentence translating the coefficient into adaptation, exposure, or equity terms |
| Qualitative | "Can I trace a claim back to the data?" | Visible coding scheme, an evidence trail, and quotes that let the reader adjudicate |
| Mixed methods | "Did the strands actually meet?" | A joint display where convergence and divergence are both interpreted, not two appendices |
| Measurement | "Is the vulnerability/governance index an artifact?" | Reliability reported and the result shown stable to an alternative scaling or weighting |

## Worked micro-example (illustrative — land-use change drivers)

A global analysis regresses forest-loss rates on a governance-quality index and commodity-price exposure across districts. Numbers are illustrative.

- **Thin version:** a stars-only table reporting "governance significant at p<0.01" and a closing claim that "better governance reduces deforestation."
- **GEC-rigorous version:** reports the magnitude — a one-SD rise in governance quality is associated with 0.8 percentage points (95% CI 0.3–1.3, illustrative) lower annual forest loss — clusters SEs at the administrative unit, and shows the estimate survives dropping the top commodity-exporting decile and re-weighting the index. Heterogeneity by tenure regime is pre-specified and Holm-adjusted, so the one significant interaction is not mined.
- **Why it clears review:** the magnitude is socially interpretable, the robustness probes could have broken it, and the human-dimensions reading (institutions, not just biophysics) is licensed by the design.

## Referee-pushback patterns and the fix

- *"Robustness only reruns near-identical specs"* → swap in specifications that could plausibly overturn the result (different aggregation scale, alternative measure) and report what you learned, including nulls.
- *"The qualitative claims have no visible evidence trail"* → expose the coding scheme and quote enough raw material for the reader to judge the inference.
- *"This is two parallel papers, not mixed methods"* → build one joint display and interpret where the strands disagree.

## Calibration anchors (hedged)

- **Honest-uncertainty bar:** intervals and effect sizes, not significance stars alone, are the GEC norm; a magnitude a policy reader can act on beats a p-value.
- **Triangulation bar:** convergence across methods strengthens a claim; unexplained divergence is a finding, not an embarrassment to hide.
- Confirm the journal's current research-data and reproducibility expectations against its author guidelines before deposit, as Elsevier policy detail evolves.

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
