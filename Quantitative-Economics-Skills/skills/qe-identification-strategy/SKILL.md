---
name: qe-identification-strategy
description: Use when the identification argument is the bottleneck for a Quantitative Economics (QE) manuscript — whether causal identification in an empirical design, parameter identification in a structural/computational model, or treatment-effect identification in an experiment. Stress-tests the strategy to the QE general-interest quantitative bar before exhibits are finalized.
---

# Identification Strategy (qe-identification-strategy)

## When to trigger

- A structural model's parameters are estimated but it is unclear *what in the data* identifies them
- An empirical causal claim rests on OLS + controls, or TWFE on staggered timing
- An experiment's estimand or its assumptions are not pinned down
- You are unsure the identification clears QE's quantitative, general-interest bar

## The QE identification bar

QE is the Econometric Society's **empirical/quantitative** general-interest journal, so identification is judged through an ES lens: the **mapping from data to the object of interest** must be explicit and defended, whatever the method. Because QE spans empirical, structural/computational, experimental, and simulation work, "identification" means different things by branch — pick the branch and make the argument transparent. QE's house norms reinforce this: report **standard errors and confidence/coverage sets** (never significance asterisks), and make the strategy reproducible for the pre-acceptance ES Data Editor check.

## Branch paths

### Branch A: Structural / computational identification
- **Name what identifies each parameter.** Tie parameters to specific data features / moments; argue identification from the model's structure, not just "the estimator converged."
- **Targeted vs. untargeted moments:** report fit to targeted moments and show untargeted-moment validation as out-of-sample discipline.
- **Sensitivity / informativeness:** report parameter sensitivity to moments (e.g., a sensitivity matrix) so readers see which data move which parameters.
- **Estimation regularity:** state the objective (MLE / GMM / MSM / indirect inference), starting values, tolerances, and that the optimum is global enough (multi-start). Report Monte Carlo evidence that the procedure recovers known parameters.
- **Counterfactual validity:** argue the estimated parameters are policy-invariant enough for the counterfactual you run.

### Branch B: Empirical causal design (applied micro / finance)
- **DID / event study:** with staggered adoption move beyond TWFE (Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille); show a clean event-study with leads; report a Goodman-Bacon decomposition.
- **IV:** strong first stage; with weak instruments use Anderson–Rubin / weak-IV-robust sets; defend the exclusion restriction in theory, institutions, and falsification.
- **RDD:** McCrary / Cattaneo–Jansson–Ma density test; optimal bandwidth + robustness; covariate smoothness; bias-corrected CIs.
- Inference clustered at the assignment level; address few-cluster issues (wild-cluster bootstrap).

### Branch C: Experimental
- **Pre-registration** in a recognized registry (AEA RCT Registry / AsPredicted / OSF) — required for own-data studies effective Jan 1, 2026; report deviations.
- Detailed **instructions / survey transcripts** included at initial submission.
- Randomization balance; attrition (Lee bounds if differential); multiple-hypothesis adjustment; explicit estimand and external-validity discussion.

### Branch D: Simulation / measurement
- Documented data-generating process; seeds set and reported.
- Show the measured object is robust to grid/tuning choices and disciplined against measurement error and alternatives.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Quantitative Economics spans structural and applied micro; the chain serves its reduced-form lane, structural estimation uses its own toolkit.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Branch chosen; the data-to-object mapping stated in one sentence
- [ ] Structural: each parameter tied to identifying moments; sensitivity + Monte Carlo recovery shown
- [ ] Empirical: design-appropriate diagnostics (pre-trends / density / first-stage / balance); modern estimator where TWFE would bias
- [ ] Experimental: pre-registered; instructions included; balance/attrition/MHT handled
- [ ] Inference reported as SEs / coverage sets (no asterisks); clustering/assignment level correct
- [ ] The claim never exceeds what the identification supports

## Anti-patterns

- "The estimator converged" presented as if it were identification (structural)
- TWFE on staggered treatment with no heterogeneity-bias discussion (empirical)
- Calibrating parameters and running a counterfactual without arguing policy-invariance
- An experiment with no pre-registration or no reported estimand
- Reporting significance with asterisks instead of standard errors / coverage sets

## Worked vignette: identifying a search-cost parameter (illustrative)

A labor-search model is estimated on matched employer–employee data. The referee asks what identifies the search-cost parameter. A weak answer points at the likelihood; a QE answer points at a data moment: the elasticity of the job-finding hazard to local vacancy density pins the cost, because a steeper hazard maps to a lower cost. Suppose the sensitivity matrix shows a 0.4 elasticity moves the estimate from 0.9 to 0.6 — that number makes identification visible. Pair it with Monte Carlo recovery (simulated panels return the true cost within 5%, illustrative).

## Referee pushback mapped to the identification fix

- *"Estimates are not credibly identified — calibration in disguise."* → Show the sensitivity matrix and which moment moves which parameter; report untargeted fit.
- *"Your counterfactual assumes policy-invariant parameters you never defend."* → Argue invariance (Lucas critique); show parameters are not functions of the policy.
- *"Staggered TWFE here is biased."* → Re-estimate with Callaway–Sant'Anna or Sun–Abraham; show flat event-study leads.

## Output format

```
【Branch】structural / empirical / experimental / simulation
【Data-to-object mapping】one sentence
【Identification evidence】[moments+sensitivity / pre-trends+density+first-stage / balance / DGP]
【Estimation/inference】objective + SEs/coverage (no asterisks); clustering if any
【What it does NOT identify】[...]
【Next step】qe-data-analysis
```
