---
name: hrm-methods
description: Use when the research design is the bottleneck for a Human Resource Management (Wiley "HRM") manuscript — matching multilevel structure, multi-source/multi-wave timing, construct validity, and common-method-bias defenses to the theoretical claim. Designs the study; it does not run the estimation (hrm-data-analysis).
---

# Research Design & Methods (hrm-methods)

## When to trigger

- Predictor and outcome are single-source, single-wave, self-reported (common-method-bias risk)
- The theory is cross-level (unit HR system → individual outcome) but data are one level
- HR-system or practice constructs lack validated measures or a defended aggregation
- The causal claim ("HPWS raises performance") rests on cross-sectional correlation
- A reviewer says "the design cannot test this hypothesis," "CMB," or "HPWS adoption is endogenous"

## HRM accepts any rigorous design — the bar is fit, not method

HRM welcomes qualitative, quantitative, meta-analytic, and critical-review work, exploratory or confirmatory, inductive/deductive/abductive. The judgment is **fit and rigor**, plus the journal's demand that the design support a **practice-relevant** conclusion. Match the design to the claim:

| Theoretical claim | Design that earns it |
|-------------------|----------------------|
| HR practice/system → individual attitudes & behavior | Multi-source, multi-wave survey; predictor and outcome from different sources/times |
| Unit HR system → individual outcomes (cross-level) | Nested data (employees in units); HLM-appropriate structure; aggregation justified |
| HR system → firm/establishment performance | Panel archival with fixed effects + an endogeneity/identification strategy |
| Causal effect of an HR intervention | Field experiment, natural experiment, or quasi-experiment (DiD) |
| Rich, contested, or emergent HR phenomenon | Qualitative / multi-method, with grounded rigor and a transparent audit trail |

A **two-study design** (e.g., a field study for generalizability plus an experiment for the mechanism) is a recognized HRM strength.

## Designing against the threats HRM referees punish

- **Common-method bias (CMB).** Procedural remedies beat statistical fixes: separate the **source** (self-report predictor, supervisor/objective outcome) and the **time** (multi-wave lag) of measurement, and plan this *before* data collection. A Harman single-factor test or a single unmeasured-latent-method-factor model is a supplement, not a defense.
- **Endogeneity of HR adoption (archival/strategic HRM).** Firms choose HPWS for reasons correlated with performance. Anticipate omitted variables, reverse causality, and selection; specify an identification strategy (panel fixed effects, DiD, instrument, or natural experiment) and state the assumption each requires.
- **Construct validity.** Use validated multi-item scales; pilot new HR-practice measures; plan a CFA establishing convergent/discriminant validity. Be explicit whether you measure the **intended**, **implemented**, or **perceived** HR system — they are different constructs and require different respondents.
- **Aggregation.** When measuring a unit-level HR system from individual reports, justify aggregation with **r_wg**, **ICC(1) / ICC(2)**, and a substantive composition model (referent-shift vs. direct consensus). Do not aggregate without a theory of why the construct is shared.
- **Sampling and power.** Justify the sampling frame and response rate; power the **interaction/cross-level** effects, which need more power than main effects.

## Level-of-analysis discipline

State the level for theory, measurement, and analysis, and keep them aligned. If theory is unit-level but data are individual, justify aggregation; if effects are cross-level, the analysis must model the nesting — do not run OLS on nested data.

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). HRM is empirical HR — multilevel survey data, field experiments, and panels; multilevel inference and many-outcome corrections matter most.

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

- [ ] Design can actually test each hypothesis (causal claims have causal leverage)
- [ ] CMB addressed by **designed** source/time separation, not just a post-hoc test
- [ ] Endogeneity strategy specified for HR-adoption / archival causal claims
- [ ] Constructs use validated measures; new HR measures piloted; CFA planned
- [ ] Intended vs. implemented vs. perceived HR system stated and matched to respondent
- [ ] Aggregation justified (r_wg, ICC) with a stated composition model
- [ ] Levels aligned across theory, measurement, analysis; nesting modeled
- [ ] Power justified for cross-level / interaction effects, not just main effects

## Anti-patterns

- **Cross-sectional causal claim**: "HR practice causes outcome" from one-wave self-report
- **CMB as afterthought**: a Harman test standing in for designed separation
- **Endogeneity ignored**: an HPWS→performance coefficient with an obviously self-selected adopter set
- **Aggregation by fiat**: averaging individuals into a "unit HR system" with no r_wg/ICC
- **Construct slippage**: measuring perceived practices but theorizing the implemented system
- **Underpowered cross-level interaction** reported as a null boundary condition

## Output format

```text
【Design】multi-source survey / multilevel nested / panel-archival / experiment / qualitative / multi-method
【Hypothesis–design fit】each H testable? notes ...
【CMB plan】source separation + time lag ...
【Endogeneity strategy】(if archival) FE / DiD / IV / natural experiment ...
【Constructs】validated? new (piloted)? CFA? intended/implemented/perceived?
【Aggregation】r_wg / ICC(1)/ICC(2); composition model
【Levels & power】theory/measurement/analysis aligned; power for cross-level/interaction
【Next skill】hrm-data-analysis
```
