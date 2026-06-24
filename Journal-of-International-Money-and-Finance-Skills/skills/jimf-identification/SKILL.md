---
name: jimf-identification
description: Use when the identification argument is the bottleneck for a Journal of International Money and Finance (JIMF) manuscript — open-economy causal designs, high-frequency policy/FX surprises, capital-control natural experiments, or parameter identification in an open-economy model. Stress-tests the strategy to JIMF's international-finance bar.
---

# Identification Strategy (jimf-identification)

## When to trigger

- A cross-country result rests on OLS-plus-controls and a referee will call it a correlation
- A high-frequency event study's "surprise" measure may be contaminated (information channel, anticipation, overlapping windows)
- A capital-control / FX-intervention / regime-switch design lacks a credible control group
- An open-economy model is estimated but it is unclear *what in the data* identifies each parameter
- You are unsure the design clears JIMF's bar for an international causal claim

## The JIMF identification bar

JIMF judges identification through an **open-economy lens**: the threat to causality usually comes from a *global* confounder (the global financial cycle, a common US monetary shock, world risk appetite) or from *policy endogeneity* (countries impose controls or intervene precisely when flows or the exchange rate move). State the data-to-object mapping in one sentence, then defend it against the international-specific confounder. Pick the branch.

### Branch A: High-frequency / surprise identification (FX, policy spillovers)
- **Construct the surprise cleanly**: narrow event windows (intraday or daily), surprises measured from futures/swaps (e.g. fed funds futures, OIS), and a window short enough to exclude other news.
- **Separate the monetary shock from the information shock**: a Fed/ECB announcement moves both policy expectations and the central bank's signal about the economy; show the sign/co-movement test (e.g. with stock prices) or use a poor-man's information-robust shock. JIMF referees now expect this.
- **Spillover design**: regress foreign asset prices / flows on the cleaned foreign (usually US) surprise in the tight window; cluster appropriately; report the first-stage strength if used as an IV.

### Branch B: Cross-country panel causal design
- **Push vs. pull**: isolate the *global push* (common foreign factor) from *country pull* (domestic fundamentals) — interact the global shock with ex-ante country exposure rather than running a pooled regression that conflates them.
- **Staggered policy adoption** (capital controls, macroprudential, regime change): move beyond TWFE (Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille); show event-study leads and a Goodman–Bacon decomposition; the control group must be plausibly unaffected by the same global shock.
- **Endogenous policy**: argue why the control/intervention timing is not a response to the outcome; use an instrument (e.g. exposure shares interacted with a global shock — a Bartik/shift-share, defended on the shares or the shocks) or an institutional discontinuity.

### Branch C: Capital-control / FX-intervention natural experiment
- Define treatment date and intensity precisely; identify a comparison set of countries or assets not subject to the measure but exposed to the same external environment.
- Address anticipation and circumvention (controls leak; interventions are sterilized); test pre-trends and placebo countries/assets.

### Branch D: Open-economy model / parameter identification
- Tie each structural parameter to an identifying data feature or moment (e.g. UIP deviation pins the risk-premium parameter; the term-structure slope pins persistence); report a sensitivity matrix and Monte Carlo recovery.
- Argue counterfactual / policy-invariance for the exchange-rate or capital-flow experiment you run (Lucas critique under a regime change).

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JIMF is international macro-finance; cross-country panels + asset pricing — identification plus factor/Newey-West inference.

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
- [ ] The *global* confounder (GFCy / common US shock / world risk) is named and addressed, not ignored
- [ ] High-frequency: window justified; monetary vs. information shock separated; surprise source stated
- [ ] Panel: push/pull separated; modern estimator where staggered TWFE would bias; control group not hit by the same global shock
- [ ] Policy experiment: endogenous-timing concern argued; anticipation/leakage tested; placebos shown
- [ ] Inference clusters at the right level (country, time, or two-way); few-cluster cross-country inference handled (wild bootstrap / Driscoll–Kraay where serial/cross correlation matters)
- [ ] Push-pull made explicit where relevant: global shock × predetermined country exposure, with time FE
- [ ] Exposure / instrument variables are predetermined (lagged/pre-sample), not contemporaneous
- [ ] The claim never exceeds what the design supports (correlation labeled as correlation)

## Anti-patterns

- A pooled cross-country regression that conflates global push with country pull and calls the coefficient causal
- Treating an announcement-day return as a clean monetary shock without addressing the central-bank information channel
- Staggered capital-control adoption analyzed with plain TWFE and no heterogeneity-bias discussion
- A control group of countries that were hit by the same global financial-cycle shock as the treated group
- Ignoring that capital controls leak and FX intervention is often sterilized, then interpreting a null as "no effect"
- Calibrating an open-economy model and running a regime-change counterfactual with no invariance argument

## What this skill does not cover

This skill stress-tests the *identification logic*. It does not build the dataset or defend the measurement choices (use `jimf-empirical-design` for the country set, frequency, and series choices) and it does not design the robustness layer that shows the identified effect is stable (use `jimf-robustness`). Identification and robustness are distinct objects at JIMF: identification answers "is this causal?"; robustness answers "is the causal estimate stable across reasonable choices?" Settle identification first — a robustness section defending a non-identified estimate persuades no one.

## Worked vignette (illustrative)

A paper claims a Fed tightening surprise causes EM portfolio outflows. The referee says the result is the global financial cycle, not US monetary policy. The JIMF fix: build the surprise from fed funds / OIS in a tight window, purge the information component (drop or sign-correct announcements where the surprise co-moves "wrongly" with US equities), and interact it with each country's *ex-ante* bond-market openness so identification comes from differential exposure, not the common time series. Suppose outflows load 0.6 (s.e. 0.2, illustrative) per 25bp on high-exposure vs. low-exposure countries — the cross-sectional interaction, not the aggregate time series, is what survives.

## Referee pushback mapped to the identification fix

- *"This is the global financial cycle, not your variable."* → Add time fixed effects that absorb all common shocks; show the within-time (cross-country) coefficient survives, identified by differential ex-ante exposure.
- *"Your announcement-window return is not a monetary shock."* → Purge the central-bank information component (sign-restriction / poor-man's sign test against equities); report the cleaned series and the affected announcements.
- *"Capital-control timing is endogenous to the flow surge."* → Argue timing exogeneity from the institutional rule; add placebo countries hit by the same surge without controls; show pre-trends are flat.
- *"Staggered TWFE is biased here."* → Re-estimate with Callaway–Sant'Anna or Sun–Abraham; show the event-study leads and the Goodman–Bacon decomposition.
- *"Your instrument's exclusion restriction fails."* → Defend it on the shares (shift-share) or the shocks; show a falsification where the instrument should have no effect.

## Inference notes for cross-country international panels

Cross-country international data are serially and cross-sectionally correlated (common global shocks), so default one-way clustering understates standard errors. Match the inference to the structure: two-way (country and time) clustering when both dimensions matter; Driscoll–Kraay when cross-sectional dependence is pervasive; wild-cluster bootstrap when the country count is small (≈20–40). State the clustering level and why; a mismatched standard error is a common, avoidable JIMF rejection trigger.

## The push-pull decomposition, made explicit

Many JIMF identification problems reduce to separating a *global push* from a *country pull*. The clean design interacts the global shock (a foreign monetary surprise, a world-risk move) with ex-ante, predetermined country exposure (capital-account openness, foreign-currency debt share, bank-funding reliance), and absorbs the common time effect with time fixed effects. Identification then comes from *differential exposure*, not the aggregate time series — which is exactly what answers the "it's the global financial cycle" objection, because the cycle is in the time effect while your coefficient is on the interaction. Make the exposure measure predetermined (lagged, pre-sample) so it cannot itself respond to the shock, and report the main effect and the interaction so the reader sees the decomposition.

## Output format

```text
【Branch】high-frequency / cross-country panel / policy experiment / open-economy model
【Data-to-object mapping】one sentence
【Global confounder addressed】GFCy / common US shock / world risk → how
【Identification evidence】cleaned surprise / push-pull interaction / pre-trends + placebos / sensitivity matrix
【Inference】clustering level; few-cluster / serial-correlation fix
【What it does NOT identify】[...]
【Next skill】jimf-empirical-design
```
