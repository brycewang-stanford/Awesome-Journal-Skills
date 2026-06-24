---
name: aerj-data-analysis
description: Use when planning or reporting the analysis for an American Educational Research Journal (AERJ) manuscript — multilevel/HLM and growth models, IRT/measurement, quasi-experimental estimation, or qualitative coding and thematic analysis. Analysis must meet the AERA reporting standards (warrant + transparency). Strengthens analysis reporting; it does not run models for you.
---

# Data Analysis (aerj-data-analysis)

AERJ analyses must be **warranted** (adequate evidence for the claim) and **transparent** (explicit
logic of inquiry), per the AERA reporting standards. Whatever the method, report enough that a reader
can judge — and a replicator could reproduce — the result.

## When to trigger

- Specifying the analytic strategy or writing the results section
- A reviewer questioned model specification, uncertainty, or coding rigor
- Reporting effect sizes, fit, robustness, or qualitative warrant
- Reconciling quantitative and qualitative results in a mixed-methods paper

## Quantitative analysis norms
- **Respect nesting.** Multilevel/HLM (or cluster-robust) inference for students-in-schools data;
  report ICC, level-specific predictors, and random effects. Center predictors deliberately (group- vs
  grand-mean) and say which.
- **Report effect sizes and uncertainty**, not just p-values: standardized effects, confidence
  intervals, and practical significance for education stakes.
- **Measurement.** Report reliability and validity evidence; for scales, factor/IRT results; handle
  measurement error rather than ignoring it.
- **Missing data.** State the mechanism assumption and method (multiple imputation / FIML), not
  listwise-by-default. Report attrition for longitudinal/experimental data.
- **Multiplicity.** Adjust or pre-specify when testing many outcomes/subgroups.
- **Large-scale assessment data.** Use plausible values and replicate/survey weights correctly.
- **Robustness.** Show the result survives reasonable alternative specifications.

## Qualitative analysis norms
- **Make the analytic process explicit**: how codes/themes were developed, who coded, how disagreements
  were resolved, and how interpretations were warranted by data.
- **Evidence the claims**: quotations/excerpts tied to themes; negative cases acknowledged; saturation
  or sufficiency addressed where relevant.
- **Reflexivity**: how the researcher's position shaped generation and interpretation.

## Mixed-methods integration
- Report how the strands were **integrated** (joint displays, meta-inferences) and what the integration
  revealed that neither strand alone could. Do not report two disconnected analyses.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). AERJ is empirical education research — field experiments and observational school data; multilevel inference and many-outcome corrections are central.

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

- OLS/single-level models on clustered data; ignoring ICC
- p-values with no effect sizes, CIs, or practical interpretation
- Listwise deletion treated as harmless; unreported attrition
- "Themes emerged" with no account of how, by whom, or with what reliability
- A mixed-methods results section that never integrates

## Warrant-and-transparency checklist by method (AERJ referees)

The AERA reporting standards apply to every tradition AERJ publishes, but referees probe different
things by design and evidentiary tradition. Audit your results section against the row that matches
your design.

| Design | What must be reported for warrant | What transparency requires made explicit |
|--------|-----------------------------------|------------------------------------------|
| Multilevel / growth | ICC, level-specific estimates, random effects, centering choice | Why each level enters; how missingness handled |
| IRT / measurement | Reliability, dimensionality, item/factor evidence | How measurement error was modeled, not ignored |
| Quasi-experimental | Identifying assumption, pre-trend or balance, sensitivity | Estimand defined; alternative specs shown |
| Qualitative | Coding process, who coded, exemplar evidence, negative cases | Reflexivity; how interpretations were warranted |
| Mixed | Both strands plus the integration result | What integration revealed that neither alone could |

## Worked analysis vignette (illustrative)

An AERJ quasi-experimental evaluation of a **ninth-grade early-warning system** uses a
difference-in-differences design across 25 districts. Warranted reporting states the estimand (effect
on on-track-to-graduate rates), shows the parallel pre-trend, reports an illustrative **+4.1
percentage points** (95% CI [1.2, 7.0]) with district-clustered SEs, and adds a sensitivity check
that survives dropping the two largest districts. The transparency layer names the missing-data
mechanism (FIML under MAR) and the attrition rate (illustrative **6%**). A weak version would report
a single coefficient with a star, no pre-trend, and listwise deletion — the AERA standard for adequate
evidence is not met.

## Referee pushback and the AERA-standard fix

- *"You ran OLS on clustered data."* → Refit with multilevel or cluster-robust inference; report ICC.
- *"P-values with no practical meaning."* → Add standardized effect sizes and CIs interpreted against
  education stakes.
- *"'Themes emerged' tells me nothing."* → Document how codes/themes were developed, by whom, with
  what reliability, and acknowledge negative cases.
- *"The mixed strands never meet."* → Add a joint display and a meta-inference; confirm any reporting
  detail against the journal's current submission guidelines.

## Output format

```
【Method】multilevel / IRT-measurement / quasi-exp / qualitative / mixed
【Specification】model or coding scheme + key choices (centering, levels, coders)
【Uncertainty / warrant】effect sizes + CIs (quant) or evidence + reflexivity (qual)
【Missing data / trustworthiness】approach stated
【Robustness】alternative specs / negative cases
【Next】aerj-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — R / Stata / Mplus / HLM and CAQDAS by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — AERA reporting standards (warrant + transparency)
