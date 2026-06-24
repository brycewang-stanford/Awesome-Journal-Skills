---
name: eer-identification
description: Use when the empirical causal-identification argument is the bottleneck for a European Economic Review (EER) manuscript — DiD/event-study, IV, RDD, or experiment. Stress-tests the design to EER's general-interest credibility bar before exhibits are finalized; it does not build the theory model or the robustness battery.
---

# Identification Strategy (eer-identification)

## When to trigger

- A causal claim rests on OLS + controls, or TWFE on staggered timing
- An IV's exclusion restriction or first-stage strength is contested
- An RDD's continuity/manipulation assumptions are unexamined
- An experiment's estimand, balance, or pre-registration is unclear
- You are unsure the design clears EER's credibility bar for a general-interest readership

## The EER identification bar

EER publishes broadly across empirical economics, so identification is judged on **credibility legible to a general reader**: the **mapping from variation in the data to the causal object** must be explicit, the key assumption stated, and the most obvious threat pre-empted. Because review is **single-anonymized**, the referee is often a methods expert in your exact design — modern, design-appropriate estimators and honest inference are expected. Report **standard errors and confidence intervals** (EER house style; do not lean on significance stars — see `eer-tables-figures`). Match the size of the causal claim to what the design supports.

## Branch paths

### Branch A: DiD / event study
- With **staggered adoption**, move beyond TWFE (Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille); a TWFE coefficient on staggered timing must be defended against heterogeneity bias.
- Show a clean **event-study** with pre-treatment leads (flat, precisely estimated) and dynamic post effects.
- Report a **Goodman-Bacon decomposition** when using two-way fixed effects.
- State the parallel-trends assumption and a **pre-trends / sensitivity** argument (e.g., Rambachan–Roth honest DiD).

### Branch B: IV
- **Strong first stage** (report the first-stage F / effective F); with weak instruments use **Anderson–Rubin / weak-IV-robust** sets.
- Defend the **exclusion restriction** in theory, institutions, and a falsification/placebo test.
- Be explicit about the **LATE / complier** interpretation; do not generalize beyond it.

### Branch C: RDD
- **Density/manipulation test** (McCrary or Cattaneo–Jansson–Ma); covariate smoothness at the cutoff.
- **Optimal bandwidth + bias-corrected CIs** (Calonico–Cattaneo–Titiunik); show sensitivity to bandwidth.
- State the **local** nature of the estimate.

### Branch D: Experiment / behavioral
- **Pre-registration** where applicable; report deviations; include **instructions / survey transcripts**.
- **Randomization balance**; attrition (Lee bounds if differential); **multiple-hypothesis** adjustment.
- State the estimand and external-validity scope.

> Clustering at the level of treatment assignment; with **few clusters** use wild-cluster bootstrap. Pair this skill with `eer-robustness` for the specification/sample battery.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). EER is a general economics field journal; the DiD/IV/RDD chain serves its applied lane.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Branch chosen; the variation-to-causal-object mapping stated in one sentence
- [ ] DiD: heterogeneity-robust estimator where TWFE would bias; flat pre-trends shown
- [ ] IV: first-stage strength reported; exclusion defended + falsification; LATE stated
- [ ] RDD: density test + bias-corrected CI + bandwidth sensitivity
- [ ] Experiment: pre-registered (if applicable); balance/attrition/MHT handled; estimand stated
- [ ] Inference: SEs/CIs reported, clustering at assignment level, few-cluster fix if needed
- [ ] Causal claim never exceeds what the design supports

## Anti-patterns

- TWFE on staggered treatment with no heterogeneity-bias discussion
- An IV with an asserted-but-undefended exclusion restriction
- RDD with no manipulation test and a single hand-picked bandwidth
- An experiment with no pre-registration mention and no estimand
- Reporting significance with asterisks instead of SEs/CIs (against EER house style)
- Generalizing a LATE or a local RDD effect to a population it does not identify

## Worked vignette (illustrative)

A migration paper uses a staggered visa-liberalization rollout. A weak version runs TWFE and reports a wage effect with stars. An EER version re-estimates with Callaway–Sant'Anna, shows flat leads and a dynamic post path, reports the effect as -1.4% local wages (s.e. 0.5, illustrative), runs Rambachan–Roth sensitivity, and states the estimand is the effect on incumbents in receiving regions — not a national average. The general-interest lesson (how labor supply shocks transmit to local wages) is named so a non-migration economist sees the point.

## Output format

```
【Branch】DiD / IV / RDD / experiment
【Variation→object mapping】one sentence
【Key assumption】stated + the main threat pre-empted
【Design evidence】[pre-trends / first-stage F / density test / balance]
【Inference】SEs/CIs; clustering level; few-cluster fix?
【What it does NOT identify】[...]
【Next step】eer-theory-model (if a mechanism is needed) or eer-robustness
```
