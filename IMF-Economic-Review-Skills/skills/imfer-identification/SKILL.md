---
name: imfer-identification
description: Use when the identification argument is the bottleneck for an IMF Economic Review (IMFER) manuscript — cross-country panel, high-frequency policy-surprise, crisis event study, narrative, or open-economy structural identification. Stress-tests the data-to-object mapping to IMFER's policy-relevant bar; it does not build the model (imfer-theory-model) or run the robustness suite (imfer-robustness).
---

# Identification Strategy (imfer-identification)

## When to trigger

- A cross-country causal claim rests on OLS-plus-controls or TWFE on staggered policy adoption
- A high-frequency policy-surprise series (monetary, FX intervention) needs its exclusion defended
- A crisis "event study" cannot separate the policy from the macro shock that triggered it
- A capital-control or program effect is plausibly **endogenous to the crisis** it is meant to address
- An open-economy model's parameters are estimated but it is unclear *what in the data* identifies them

## The IMFER identification bar

IMFER referees read as both frontier econometricians and policy analysts, so the **mapping from data to the policy-relevant object** must be explicit *and* the object must be the one a policymaker cares about. International-macro data make this harder than a clean single-country RCT: small N of countries, endogenous policy adoption, global common shocks, and spillovers that violate SUTVA across borders. Name the variation, defend it against the macro confounder, and report inference that respects cross-country dependence.

### Branch A: Cross-country panel
- Move beyond TWFE under staggered policy adoption: Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille; show clean event-study leads.
- **Global common shocks** (the global financial cycle, US monetary policy) confound country panels — saturate with time effects, or use a shift-share / external-instrument design.
- **Spillovers break SUTVA**: a control imposed in one country affects its neighbors. State the interference assumption or model the network explicitly.
- Inference: cluster on country *and* allow cross-sectional dependence (Driscoll–Kraay); with few countries, wild-cluster bootstrap.

### Branch B: High-frequency policy-surprise
- Build the surprise from a tight window around announcements (intraday futures/yields); show it is unpredictable from the prior information set.
- Defend the exclusion: the surprise moves the outcome *only* through the policy channel, not contemporaneous news. Use a poll-based or sign-restriction purge if needed.
- For spillover designs, identify the foreign transmission (US-shock-to-EM-flows) and rule out the domestic-news confounder.

### Branch C: Crisis event study / narrative
- Define the event window and the counterfactual path; the trigger shock and the policy response are nearly simultaneous — argue what isolates the policy.
- Use narrative classification (IMF program dates, intervention episodes) with documented coding rules; report sensitivity to window length and event definition.
- Address **selection into crisis/program**: countries adopt programs precisely when fundamentals deteriorate.

### Branch D: Open-economy structural / DSGE
- Name what identifies each parameter from a data moment (an impulse response, a comovement, an external-finance premium) — not "the estimator converged."
- Report a sensitivity matrix (which moment moves which parameter) and Monte Carlo recovery of known parameters.
- Argue policy-invariance for the counterfactual (Lucas critique), since IMFER counterfactuals are read as policy advice.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). IMFER is international macro/finance; cross-country panels with confounded policy — emphasize identification and clustering.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Branch chosen; the data-to-policy-object mapping stated in one sentence
- [ ] Global common shocks / the global financial cycle addressed in cross-country designs
- [ ] Cross-border spillovers (SUTVA) acknowledged and handled, not assumed away
- [ ] Staggered-adoption bias handled with a modern estimator; clean event-study leads shown
- [ ] Policy-surprise series shown unpredictable; exclusion defended institutionally and empirically
- [ ] Selection into crisis/program confronted, not ignored
- [ ] Inference respects cross-sectional dependence and few-country issues; SEs not asterisks
- [ ] Structural: each parameter tied to an identifying moment; sensitivity + recovery shown

## Anti-patterns

- TWFE on staggered capital-control / program adoption with no heterogeneity-bias discussion
- A country panel that ignores the global financial cycle / US-policy common shock
- Treating a CFM or IMF program as exogenous when it is adopted in response to the crisis
- A "policy surprise" still predictable from prior macro news
- Clustering only on time, or ignoring spatial/cross-country dependence
- "The model converged" presented as structural identification

## The international-macro confounders to name explicitly

International-macro identification fails in characteristic ways the referee pool knows by heart; name the ones in play.

- **The global financial cycle.** A common push factor (US monetary policy, global risk appetite) drives flows, spreads, and prices in many countries at once. Time effects help only if the loading is homogeneous; otherwise use an explicit factor or external instrument.
- **Reverse causality with the crisis.** CFMs, interventions, and IMF programs are adopted *because* conditions deteriorated; the policy and the outcome share a cause.
- **Cross-border spillovers (SUTVA).** A control unit is contaminated by the treated country's policy (contagion, portfolio rebalancing); the "untreated" counterfactual is not clean.
- **Anticipation.** Markets price an expected regime change before the announcement, contaminating pre-periods.
- **Small N of countries.** Asymptotics in the country dimension are unreliable; report finite-sample-robust inference.

## Worked vignette (illustrative)

A panel claims capital-flow-management measures cut the volatility of inflows. A weak version runs TWFE with country and year effects. An IMFER version: (i) uses Callaway–Sant'Anna for staggered adoption with flat pre-trends; (ii) instruments adoption with a regional-contagion shift-share to break endogeneity to the country's own crisis; (iii) saturates with the global financial cycle (a VIX/US-shock factor) to kill the common shock; (iv) reports Driscoll–Kraay SEs for cross-country dependence. The estimand — the effect *on the adopting country's inflow volatility* — is stated, and the spillover to neighbors is flagged as a separate object.

## Referee pushback mapped to the identification fix

- *"Staggered TWFE is biased here."* → Re-estimate with Callaway–Sant'Anna or Sun–Abraham; show flat event-study leads.
- *"This is the global financial cycle, not your policy."* → Add the common-shock factor / US-shock control and show the result survives.
- *"The policy is endogenous to the crisis."* → Bring an external instrument or narrative timing; defend selection-into-program.

## Output format

```text
【Journal】IMF Economic Review
【Skill】imfer-identification
【Branch】cross-country panel / policy-surprise / crisis event / structural
【Data-to-policy-object mapping】one sentence: ___
【Common-shock / spillover handling】___
【Selection / endogeneity defense】___
【Inference】clustering + cross-sectional dependence; SEs not asterisks: ___
【What it does NOT identify】___
【Next skill】imfer-theory-model
```
