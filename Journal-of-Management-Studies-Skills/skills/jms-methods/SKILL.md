---
name: jms-methods
description: Use when the research design is the bottleneck for a Journal of Management Studies (JMS) manuscript — matching design (qualitative case/ethnography, process/longitudinal, survey, archival, experiment, multi-method) to the theoretical question, with qualitative rigor treated as first-class. Designs the study; it does not run the estimation or trustworthiness checks (jms-data-analysis).
---

# Research Design & Methods (jms-methods)

## When to trigger

- The design may not match the theory's level, timing, or causal claim
- A qualitative study's case selection, saturation, or analytic procedure is under-specified
- Quantitative data are single-source, single-wave, self-reported (common-method bias risk)
- The theory is causal but the design is cross-sectional/correlational
- A reviewer says "the design cannot test/show this" or "the method is not rigorous enough"

## Match the design to the question — pluralism with rigor

JMS welcomes **all** rigorous designs and is, distinctively, a friendly home for **qualitative and process** work — but rigor must clear a top-tier bar regardless of method. Choose the design the question demands:

| Theoretical claim / question | Design that earns it |
|------------------------------|----------------------|
| *How/why* a phenomenon emerges or works | Inductive multi-case (Eisenhardt) or ethnography |
| *How* something unfolds over time | Process / longitudinal (temporal bracketing, visual mapping) |
| Causal effect of a manipulable cause | Experiment (lab / field / online) or natural experiment |
| Whether & how much, with generalisation | Survey (multi-wave) or panel archival |
| Cross-level mechanism (firm → individual) | Multilevel / nested design (HLM-appropriate) |
| Contested, novel, or richly contextual | Multi-method (e.g., qual study 1 + quant study 2) |

## Designing qualitative rigor (first-class at JMS)

- **Case/site selection** is theoretical, not convenient: state the sampling logic (extreme, polar, theoretically replicating). Justify the number of cases and why they let the theory travel.
- **Data sources triangulated**: interviews + archives + observation; report counts (informants, hours, documents) and the period.
- **Analytic procedure stated**: which approach (Gioia, Eisenhardt cross-case, grounded theory, narrative/temporal bracketing) and how codes became constructs.
- **Trustworthiness** in the qualitative idiom: member checking, an audit trail, negative-case analysis, inter-coder agreement where appropriate — not p-values.

## Designing against the threats JMS reviewers cite (quantitative)

- **Common-method bias**: separate sources / temporal separation across waves; objective or archival outcomes where possible. Procedural design beats a post-hoc Harman test (the Podsakoff guidance is standard).
- **Endogeneity (archival/survey)**: anticipate omitted variables, reverse causality, selection; plan an identification strategy (panel FE, DiD, IV/2SLS, natural experiment, matching) and state each one's assumptions.
- **Measurement**: validated multi-item scales; pilot new measures; plan a CFA; state the level each construct is measured at and justify any aggregation (ICC, r_wg).
- **Power & sampling**: justify the frame, response rate, and power — interactions need more power than main effects.

## Level-of-analysis discipline

State the level for theory, measurement, and analysis, and keep them aligned. If theory is at the firm level but data are individual, justify aggregation; for cross-level effects, model the nesting — do not run OLS on nested data.

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JMS mixes qualitative and quantitative management research; the chain below is for the quantitative-empirical lane.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result` to
  enumerate the checks the design owes.
- **Panel / staggered DiD:** `callaway_santanna` / `sun_abraham` + `bacon_decomposition`
  + `honest_did_from_result`. **IV:** `effective_f_test` + `anderson_rubin_ci`. **RDD:**
  `rdrobust` + `mccrary_test`.
- **Experiments:** randomization-based inference and `romano_wolf` for the many-outcome
  family-wise correction reviewers expect.

Match the toolchain to the **reviewer pool**, and report the effect size the venue
wants. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Design can actually answer the question (causal claims have causal leverage)
- [ ] Qualitative: theoretical case selection, triangulated sources with counts, named analytic procedure, trustworthiness checks
- [ ] Quantitative: CMB addressed by design; endogeneity strategy specified; validated/piloted measures; CFA planned
- [ ] Level of analysis aligned across theory, measurement, analysis; aggregation justified
- [ ] Sampling frame, N, and power (incl. interactions) justified
- [ ] Where useful, a second study triangulates the mechanism

## Anti-patterns

- **Qualitative-by-default vagueness**: "we did a case study" with no selection logic or analytic procedure
- **Cross-sectional causal claims**: "X causes Y" from one-wave correlational data
- **CMB as afterthought**: relying on a single Harman test instead of designed separation
- **Ignored endogeneity**: an obviously endogenous regressor with no identification strategy
- **Mismatched levels**: theorising at the firm level, testing disaggregated individual data via OLS
- **Method theatre**: a fashionable estimator or qualitative label not justified by the question

## Output format

```text
【Design】qual multi-case / ethnography / process / experiment / survey / panel-archival / multi-method
【Question-design fit】can the design answer each claim? notes …
【Qualitative rigor】(if qual) case selection · sources+counts · analytic procedure · trustworthiness
【CMB / endogeneity】(if quant) procedural remedy · identification strategy
【Measures】validated? new (piloted)? CFA planned?
【Levels】theory / measurement / analysis aligned? aggregation justified?
【Next step】jms-data-analysis
```
