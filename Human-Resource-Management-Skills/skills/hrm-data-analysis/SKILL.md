---
name: hrm-data-analysis
description: Use when estimation and analysis are the bottleneck for a Human Resource Management (Wiley "HRM") manuscript — fitting HLM/SEM, testing mediation and cross-level moderation, defending aggregation, and qualitative coding rigor. Runs and validates the analysis; it does not design the study (hrm-methods).
---

# Data Analysis (hrm-data-analysis)

## When to trigger

- You have nested data (employees in units/firms) and need the right multilevel model
- A mediation/moderation hypothesis needs a defensible test (not just a significant indirect effect)
- A measurement model (CFA) must establish discriminant validity before structural tests
- A reviewer challenges the aggregation, the estimator, or asks for robustness
- Qualitative data need a transparent, auditable coding and trustworthiness account

## Match the estimator to the data structure

| Data / claim | Estimator | What referees will check |
|--------------|-----------|--------------------------|
| Individuals nested in units; cross-level effects | **HLM / mixed models** (random intercepts/slopes) | Variance decomposition; ICC justifying multilevel; correct level for each predictor |
| Latent constructs + structural paths | **SEM** (with measurement model first) | CFA fit (CFI/TLI ≥ ~.95, RMSEA ≤ ~.06, SRMR ≤ ~.08); discriminant validity (AVE > shared variance) |
| Mediation (the HR black box) | Bootstrap **indirect effect** CIs; multilevel mediation if cross-level | Theorized mechanism, not inference from significance alone; 1-1-1 vs. 2-1-1 structure stated |
| Moderation / interaction | Product terms; simple slopes; **interaction plot** | Centering; region of significance; power; theory for the slope change |
| HR system → firm performance (panel) | **Fixed-effects / DiD / IV** | Endogeneity strategy; clustered SEs; pre-trends if DiD |
| Meta-analysis | Random-effects (e.g., Hunter–Schmidt / HVZ) | Coding reliability; heterogeneity (I², Q); publication-bias checks; moderator analysis |

## Multilevel and SEM discipline (HRM's bread and butter)

- **Justify going multilevel.** Report ICC(1)/ICC(2); if essentially zero between-unit variance, a multilevel model is not warranted — say so.
- **Group-mean center** lower-level predictors when testing within-unit effects; grand-mean center for cross-level; state which and why (the choice changes the meaning of the coefficient).
- **Measurement before structure.** Run the CFA and establish discriminant validity *before* interpreting structural paths; a saturated SEM with a poor measurement model is not evidence.
- **Mediation is a theory claim.** Report the indirect effect with bias-corrected bootstrap CIs, but the mechanism must have been theorized a priori; do not back-fill the mechanism from a significant indirect path.
- **Aggregation evidence travels with the analysis.** r_wg, ICC(1), ICC(2) belong in the results, tied to the composition model from `hrm-methods`.

## Robustness and transparency HRM expects

- Report **alternative specifications** (controls in/out, alternative operationalizations of the HR system) and show the focal effect is stable.
- Address **endogeneity** for adoption/performance claims (FE, DiD, IV) and report clustered standard errors at the assignment level.
- Provide **effect sizes in practitioner-meaningful terms** (e.g., a 1-SD increase in HPWS is associated with X% higher productivity) — HRM rewards results an HR leader can act on.
- For **qualitative** work, give a transparent audit trail: data structure (first-order codes → second-order themes → aggregate dimensions), coding reliability or consensus process, and trustworthiness (member checks, triangulation).
- Follow Wiley's **data-availability** policy: include a data-availability statement and prepare materials for sharing where permitted (检索于 2026-06；以官网为准).

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). HRM is empirical HR — multilevel survey data, field experiments, and panels; multilevel inference and many-outcome corrections matter most.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or
  `benjamini_hochberg` — report the adjusted threshold.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`;
  multilevel data → cluster at the right level.
- **Re-fit off one handle:** `audit_result(result_id)` lists the missing checks and the
  exact `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Keep the decisive checks in the body and the exhaustive battery in the appendix. See the
executed chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Estimator matches the data structure (nesting modeled; latent constructs in SEM)
- [ ] ICC reported and the multilevel choice justified
- [ ] CFA fit + discriminant validity established before structural interpretation
- [ ] Centering choice stated and matched to the effect being tested
- [ ] Indirect effects via bootstrap CIs; mechanism theorized a priori
- [ ] Endogeneity addressed; SEs clustered at the right level
- [ ] Effect sizes translated into practitioner-meaningful magnitudes
- [ ] Qualitative: transparent data structure + trustworthiness account
- [ ] Data-availability statement prepared per Wiley policy

## Anti-patterns

- **OLS on nested data**: ignoring clustering and inflating significance
- **Structure before measurement**: interpreting SEM paths with a failing CFA
- **Mediation by significance**: claiming a mechanism from a significant indirect effect never theorized
- **Centering silence**: not stating group- vs. grand-mean centering in multilevel models
- **p-value-only results**: no effect sizes, no practitioner translation
- **Aggregation without evidence**: a unit-level construct with no r_wg/ICC
- **Opaque qualitative coding**: themes with no audit trail or reliability account

## Output format

```text
【Journal】Human Resource Management (Wiley "HRM")
【Skill】hrm-data-analysis
【Data structure】nested / latent-SEM / panel / meta / qualitative
【Estimator】HLM / SEM / FE-DiD-IV / bootstrap mediation / RE meta
【Measurement】CFA fit + discriminant validity status
【Multilevel】ICC reported; centering choice
【Mediation/moderation】indirect-effect CIs; interaction plot; a-priori mechanism?
【Robustness】alt specs / endogeneity / clustered SEs
【Practitioner magnitude】effect translated to an actionable number
【Data policy】availability statement prepared? 检索于 2026-06；以官网为准
【Next skill】hrm-contribution-framing
```
