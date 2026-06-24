---
name: restat-identification
description: Use when the causal-identification or measurement strategy is the bottleneck for a The Review of Economics and Statistics (REStat) manuscript — a DID / RD / IV / shift-share design, or a measurement / measurement-error problem. Stress-tests the design to REStat's applied-econometrics-and-measurement bar before exhibits are finalized.
---

# Identification & Measurement Strategy (restat-identification)

## When to trigger

- A causal claim rests on OLS + controls, or TWFE on staggered timing
- An IV's exclusion restriction or first-stage strength is contestable
- An RD's continuity / manipulation assumptions are not yet defended
- A shift-share / exposure design's exogeneity (shares vs shocks) is unargued
- The outcome or key regressor is **measured with error**, or you built a **new measure/index**

## The REStat identification-and-measurement bar

REStat is **applied econometrics with a measurement tradition**, so two things are judged together: the **mapping from data to the causal object** must be explicit and defended, **and** the **quality of measurement** behind every variable must be credible. A clean design on a badly measured construct does not clear the bar; neither does a beautifully measured variable in a hopelessly confounded regression. Report **standard errors and modern inference**; clustering at the assignment level; address attenuation and other measurement-error biases head-on — REStat referees raise measurement objections sibling journals sometimes wave through.

## Branch paths

### Branch A: Difference-in-differences / event study
- With staggered adoption, **move beyond TWFE** (Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille — the last has REStat-published estimators).
- Show a clean **event-study with leads** (flat pre-trends) and report a Goodman–Bacon decomposition.
- State the parallel-trends assumption and probe it (pre-trend tests + Rambachan–Roth honest bounds where relevant).

### Branch B: Regression discontinuity
- **McCrary / Cattaneo–Jansson–Ma density test** for manipulation; covariate smoothness at the cutoff.
- Optimal bandwidth + **bias-corrected, robust CIs**; sensitivity to bandwidth and polynomial order.
- Fuzzy RD: report first stage; defend exclusion of the running variable's other channels.

### Branch C: Instrumental variables
- **Strong first stage** (report effective F / Montiel-Olea–Pflueger); with weak instruments use **Anderson–Rubin / weak-IV-robust** sets.
- Defend the **exclusion restriction** in theory, institutions, and falsification tests.
- Shift-share / Bartik: argue exogeneity of **shares** (Goldsmith-Pinkham–Sorkin–Swift) or of **shocks** (Borusyak–Hull–Jaravel); report the implied just-identified estimates.

### Branch D: Measurement (REStat signature)
- **Construct validity:** what does the measure actually capture; validate against an external benchmark.
- **Measurement error:** classical vs non-classical; attenuation correction, validation samples, or bounds.
- New index / data: document construction, sensitivity to choices, and show the applied conclusion is not an artifact of how you measured.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). REStat is applied econometrics/empirical micro — the home of careful identification; DiD/IV/RDD with weak-IV-robust CIs.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Branch chosen; data-to-object mapping stated in one sentence
- [ ] DID: heterogeneity-robust estimator + flat event-study leads + Bacon decomposition
- [ ] RD: density test + smoothness + bias-corrected robust CIs + bandwidth sensitivity
- [ ] IV: first-stage strength + weak-IV-robust inference + defended exclusion
- [ ] Shift-share: exogeneity of shares or shocks argued explicitly
- [ ] Measurement: construct validity shown; measurement error addressed (correction / bounds)
- [ ] Inference: SEs reported, clustered at the right level; few-cluster issues handled (wild bootstrap)
- [ ] The claim never exceeds what identification AND measurement jointly support

## Anti-patterns

- TWFE on staggered treatment with no heterogeneity-bias discussion
- An RD with no manipulation test or no bandwidth sensitivity
- A weak first stage reported with conventional t-stats as if robust
- Ignoring attenuation from a noisily measured regressor — a classic REStat referee catch
- A new index presented without validation against any external benchmark
- Conflating "statistically significant" with "credibly identified and well measured"

## Worked vignette: a noisily measured regressor (illustrative)

A paper regresses earnings on a survey-reported measure of training hours and finds a small effect. A REStat referee notes the training measure is self-reported and likely error-ridden, biasing the coefficient toward zero. The fix: bring an administrative validation subsample, estimate the reliability ratio (say 0.6, illustrative), and show the attenuation-corrected effect is roughly 1/0.6 larger — turning a "small" effect into an economically meaningful one, with the correction's assumptions stated. Measurement, not just identification, moved the answer.

## Output format

```
【Branch】DID / RD / IV / shift-share / measurement
【Data-to-object mapping】one sentence
【Identification evidence】[event-study+Bacon / density+smoothness / first-stage+AR / shares-or-shocks]
【Measurement evidence】[construct validity / error correction / bounds] — or "n/a, cleanly measured"
【Inference】SEs + clustering level; few-cluster fix if any
【What it does NOT identify】[...]
【Next step】restat-theory-model (or restat-robustness if theory is minimal)
```
