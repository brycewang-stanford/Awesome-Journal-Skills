---
name: jeea-identification
description: Use when the identification argument is the bottleneck for a Journal of the European Economic Association (JEEA) manuscript — credible causal identification in an empirical design, parameter identification in a structural/quantitative model, or the source of identification in a theory paper. Stress-tests the strategy to JEEA's general-interest bar before exhibits are finalized.
---

# Identification Strategy (jeea-identification)

## When to trigger

- An empirical causal claim rests on OLS + controls, or TWFE on staggered timing
- A structural model's parameters are estimated but it is unclear *what in the data* identifies them
- A theory paper's result depends on assumptions whose role is not transparent
- You are unsure the identification clears JEEA's general-interest theory-and-empirics bar

## The JEEA identification bar

JEEA spans **theory and empirics**, so "identification" means different things by branch — but in every case the **mapping from assumptions/data to the object of interest must be explicit and defended**, and credible enough for a general-interest readership and a co-editor who is not a subfield specialist. JEEA's house norms reinforce this: report **standard errors and confidence sets** (no significance asterisks/boldface for significance) and make the empirical strategy reproducible for the **JEEA Data Editor's pre-acceptance replication check** (DCAS). Pick the branch and make the argument legible.

## Branch paths

### Branch A: Structural / quantitative identification
- **Name what identifies each parameter.** Tie parameters to specific data features / moments; argue identification from the model's structure, not "the estimator converged."
- **Targeted vs. untargeted moments:** report fit to targeted moments and untargeted-moment validation as out-of-sample discipline.
- **Sensitivity / informativeness:** report parameter sensitivity to moments (sensitivity matrix) so readers see which data move which parameters.
- **Estimation regularity:** state the objective (MLE / GMM / MSM / indirect inference), starting values, tolerances, multi-start; report Monte Carlo evidence recovering known parameters.
- **Counterfactual validity:** argue the estimated parameters are policy-invariant enough for the counterfactual (Lucas critique).

### Branch B: Empirical causal design (applied micro / development / finance)
- **DID / event study:** with staggered adoption move beyond TWFE (Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille); show clean event-study leads; report a Goodman–Bacon decomposition.
- **IV:** strong first stage; with weak instruments use Anderson–Rubin / weak-IV-robust sets; defend the exclusion restriction in theory, institutions, and falsification.
- **RDD:** Cattaneo–Jansson–Ma density test; optimal bandwidth + robustness; covariate smoothness; bias-corrected CIs.
- Inference clustered at the assignment level; address few-cluster issues (wild-cluster bootstrap).

### Branch C: Theory / mechanism identification
- **What assumptions do the work.** Identify the minimal assumptions driving the headline result; show which can be relaxed and which are essential.
- **Comparative statics as identification:** make clear which primitive moves which prediction, so the model's empirical content is testable.
- **Source of the result:** distinguish a genuinely new mechanism from a re-parameterization; route to `jeea-theory-model` for generality and proof discipline.

### Branch D: Experimental / own-data
- **Pre-registration** in a recognized registry; report deviations and the explicit estimand.
- Randomization balance; attrition (Lee bounds if differential); multiple-hypothesis adjustment; external-validity discussion.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JEEA is a general-interest European economics flagship; credible identification across applied fields.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Branch chosen; the assumption/data-to-object mapping stated in one sentence
- [ ] Structural: each parameter tied to identifying moments; sensitivity + Monte Carlo recovery shown
- [ ] Empirical: design-appropriate diagnostics (pre-trends / density / first-stage / balance); modern estimator where TWFE would bias
- [ ] Theory: minimal assumptions named; what is essential vs. relaxable made explicit
- [ ] Inference reported as SEs / confidence sets (no asterisks); clustering/assignment level correct
- [ ] The claim never exceeds what the identification supports

## Anti-patterns

- "The estimator converged" presented as if it were identification (structural)
- TWFE on staggered treatment with no heterogeneity-bias discussion (empirical)
- A theory result whose driving assumption is hidden in notation, so its empirical content is unclear
- Calibrating parameters and running a counterfactual without arguing policy-invariance
- Reporting significance with asterisks instead of standard errors / confidence sets

## Referee pushback mapped to the identification fix

- *"This is OLS with controls dressed up as causal."* → Provide a design (DID/IV/RDD) or a credible selection-on-observables defense with sensitivity (Oster) and falsification.
- *"Staggered TWFE here is biased."* → Re-estimate with Callaway–Sant'Anna or Sun–Abraham; show flat event-study leads.
- *"Your structural estimates are calibration in disguise."* → Show the sensitivity matrix and which moment moves which parameter; report untargeted fit.
- *"The model's headline result is an artifact of one assumption."* → Name the assumption, relax it, and show the result survives (or scope it honestly).

## Output format

```
【Branch】structural / empirical / theory / experimental
【Assumption-or-data-to-object mapping】one sentence
【Identification evidence】[moments+sensitivity / pre-trends+density+first-stage / minimal-assumptions / balance]
【Estimation/inference】objective + SEs/confidence sets (no asterisks); clustering if any
【What it does NOT identify】[...]
【Next step】jeea-theory-model or jeea-robustness
```
