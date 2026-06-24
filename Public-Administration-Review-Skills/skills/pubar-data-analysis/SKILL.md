---
name: pubar-data-analysis
description: Use when executing and reporting the analysis for a Public Administration Review (PAR) manuscript so it survives expert, double-blind review and supports honest Evidence for Practice — uncertainty, robustness, and triangulation appropriate to quantitative, experimental, or mixed work. Guides analysis norms; it does not fabricate results.
---

# Data Analysis (pubar-data-analysis)

PAR reviewers are methodologically capable public-management scholars, and the journal endorses the
**TOP transparency guidelines** — so analyses should be reproducible and documented (see
`pubar-transparency-and-data`). Because PAR articles carry **Evidence for Practice**, every estimate
that drives a managerial takeaway must be analyzed honestly enough to bear that weight. This skill
covers execution and reporting; design decisions live in `pubar-research-design`.

## When to trigger

- Running main and supporting analyses; building the results section
- A reviewer asked for robustness, heterogeneity, or alternative specifications
- Reconciling preregistered vs. exploratory analyses
- Making the analysis reproducible before deposit

## Analysis norms PAR expects

1. **Report uncertainty honestly.** Confidence/credible intervals, not just stars; the **magnitude and
   substantive/managerial meaning** of the estimate, not just its significance. A practitioner needs
   effect size, not a p-value.
2. **Robustness that probes, not decorates.** Show specifications that could *break* the result
   (alternative measures, samples, estimators, fixed effects), and say what you learn.
3. **Heterogeneity with discipline.** Pre-specify subgroups where possible (agency type, jurisdiction
   size, sector); correct for multiple comparisons; don't mine an interaction and theorize it post hoc.
4. **Right inference.** Cluster at the assignment/sampling level (agency, district); wild-cluster
   bootstrap when clusters are few — a common public-management data situation.
5. **Preregistration discipline.** Clearly separate **registered** from **exploratory** analyses;
   reconcile and justify deviations.
6. **Measurement.** Validate constructs (red tape, PSM, performance); report reliability; show results
   are not an artifact of a coding/scaling choice — measurement debates are central in PA.

## Mixed-methods integration
- State explicitly where the qualitative evidence corroborates, refines, or contradicts the
  quantitative estimate; do not present them in parallel silos with no integration.

## Reproducibility while you work (not at the end)
- One **master script** regenerates every table and figure from the (raw or constructed) data.
- **Set and report seeds** for bootstrap, randomization inference, simulation, any stochastic step.
- Pin software/package versions (`renv.lock`, `requirements.txt`, recorded `ssc`/`net` installs).
- Keep table/figure numbers matched to script outputs; document design/prep decisions in the
  supplementary document PAR recommends.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). PAR is public administration — survey/observational and some experimental work; identification + clustered/multilevel inference, magnitude for practice.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- Stars-only tables with no effect sizes or intervals (a practitioner can't act on stars)
- "Robustness" that only reruns near-identical specs to manufacture stability
- p-hacking / fishing for a significant interaction; HARKing exploratory results into hypotheses
- Clustering at the wrong level or ignoring few-cluster problems
- An Evidence-for-Practice point that the analysis does not actually support

## Output format

```
【Main estimate】magnitude + interval + managerial meaning
【Identification check】(per research-design) result
【Robustness】specs that could break it → what held
【Heterogeneity】pre-specified? MHT-adjusted?
【Registered vs exploratory】clearly separated?
【Reproducible】master script + seeds + pinned versions? [Y/N]
【Next】pubar-tables-figures
```

## What PAR reviewers probe, by analytic tradition

| Analytic tradition | The check a PAR referee runs first | The fix that earns the benefit of the doubt |
|--------------------|------------------------------------|---------------------------------------------|
| Survey / managerial experiment | Is inference randomization-based and pre-registered? | Randomization inference, pre-registered estimand, MDE reported |
| Observational causal (reform) | Is the "causal" word (and the policy advice) doing more than the design licenses? | State estimand + assumption; sensitivity to an unobserved confounder |
| Performance / administrative data | Are measures validated, and is gaming/selection ruled out? | Construct validation, reliability, selection checks |
| Mixed methods | Do quant and qual estimates actually corroborate? | Show where they agree, and own where they diverge |

## Worked micro-example (illustrative numbers)

A hypothetical PAR survey experiment tests whether a performance-feedback framing raises frontline
managers' willingness to adopt a new reporting tool. The pre-registered ATE is **+7.4 points (95% CI
3.0 to 11.8)** on a 0–100 willingness scale, randomization-inference *p* = 0.006. An exploratory
subgroup ("low-tenure managers") shows **+13 points**, but it was *not* pre-registered and after a
Bonferroni adjustment across five exploratory subgroups its interval crosses zero. The disciplined
write-up reports the +7.4 confirmatory effect with its interval and a managerial interpretation, flags
the +13 figure as **exploratory and not multiplicity-robust**, and frames it as a hypothesis — so the
Evidence-for-Practice point rests on the confirmatory estimate only. (All numbers illustrative.)

## Calibration anchors (hedged)

- The bar is **field-wide PA significance plus honest practice relevance**; an effect only a specialist
  values, or a takeaway the data can't support, rarely clears PAR review.
- PAR practices methodological breadth — a rigorous mixed-methods or case analysis is not second-class
  to a regression. Match the inference standard to the design.
- TOP transparency expectations evolve; confirm the current data-policy wording on the journal's page
  (检索于 2026-06；以官网为准).

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — estimation, inference, and survey packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — TOP transparency policy
