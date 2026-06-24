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

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). APSR is general-interest political science — observational causal designs (DiD/IV/RDD) and survey/field experiments alike; cluster by the right unit and foreground identification.

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

## What APSR reviewers probe, by analytic tradition

APSR is the flagship of the American Political Science Association, published by Cambridge University
Press, and its reviewers are drawn from across the discipline — so the same results section can be
read by a formal theorist, a survey methodologist, and a comparativist at once. Calibrate the
analysis to whichever lens is decisive, but expect all three to be in the room.

| Analytic tradition | The check an APSR referee runs first | The fix that earns the benefit of the doubt |
|--------------------|--------------------------------------|---------------------------------------------|
| Survey / lab experiment | Is inference randomization-based and pre-registered? | Randomization inference, pre-registered estimand, MDE reported |
| Observational causal | Is the "causal" word doing more than the design licenses? | State estimand + assumption; sensitivity to an unobserved confounder |
| Text-as-data / computational | Was the model validated against human labels? | Held-out validation set, stability across seeds, version pinned |
| Formal-empirical | Do the tests follow comparative statics, or a loose analogy? | Map each prediction to a parameter the model moves |
| Multi-method | Do quant and qual estimates actually corroborate? | Show where they agree, and own where they diverge |

## Worked micro-example (illustrative numbers)

A hypothetical APSR survey experiment tests whether co-partisan endorsements raise support for a
redistricting reform. The pre-registered ATE is **+6.2 points (95% CI 3.1 to 9.3)** on a 0–100
support scale, randomization-inference *p* = 0.004. The exploratory subgroup "low political-knowledge
respondents" shows **+11.8 points**, but it was *not* pre-registered and the interaction *p* = 0.04
before any multiplicity correction — after a Bonferroni adjustment across the six exploratory
subgroups it crosses 0.20. The disciplined write-up reports the +6.2 confirmatory effect with its
interval and substantive meaning, flags the +11.8 figure as **exploratory and not multiplicity-robust**,
and frames it as a hypothesis for future work rather than a finding. (All numbers illustrative.)

## Referee-pushback patterns and the APSR-specific repair

- *"This reads as a subfield result, not a general one."* → Re-anchor the estimate to a
  discipline-wide stake (representation, accountability, institutional design) before the numbers.
- *"The robustness table only reruns near-identical specs."* → Replace decorative checks with
  specifications that could *break* the result, and say what you learned when they did not.
- *"Theory and empirics are loosely coupled."* → Tie each estimate back to an observable implication
  the argument named in advance, not to a pattern noticed afterward.
- *"I cannot tell registered from exploratory analyses."* → Segregate them explicitly; the editorial
  office will later re-run the deposited code, so the split must survive verification.

## Calibration anchors (hedged)

- The bar is **general-political-science significance**, not within-subfield novelty: an effect that
  only a specialist would value rarely clears APSR review.
- APSR practices **methodological pluralism** — a rigorous qualitative or formal analysis is not
  second-class to a regression. Match the inference standard to the design.
- Transparency expectations follow **DA-RT / APSR Dataverse** norms: write the analysis so a
  conditionally-accepted package reproduces every printed number. Exact deposit mechanics can change —
  confirm against the journal's current submission and transparency guidelines.

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — estimation, inference, and text-as-data packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — reproducibility-verification policy
