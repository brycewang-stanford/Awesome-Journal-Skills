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

## Anti-patterns

- OLS/single-level models on clustered data; ignoring ICC
- p-values with no effect sizes, CIs, or practical interpretation
- Listwise deletion treated as harmless; unreported attrition
- "Themes emerged" with no account of how, by whom, or with what reliability
- A mixed-methods results section that never integrates

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
