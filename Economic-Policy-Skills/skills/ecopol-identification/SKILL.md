---
name: ecopol-identification
description: Use when the identification argument is the bottleneck for an Economic Policy (EP) manuscript — causal identification of a policy effect, or parameter identification in a quantitative policy model. Stress-tests it to the EP bar (credible to an academic discussant, legible to a policy discussant) before exhibits are finalized.
---

# Identification Strategy (ecopol-identification)

## When to trigger

- A policy effect rests on OLS + controls, or TWFE on staggered policy rollout
- An IV's exclusion restriction is institutional hand-waving, not an argument
- A structural/quantitative policy model is estimated but it is unclear *what in the data* pins each parameter
- The counterfactual policy scenario relies on parameters whose policy-invariance is undefended
- You must convince **two discussants at once** — one who will probe the econometrics, one who needs the design to be legible enough to trust the policy number

## The EP identification bar

EP papers are debated by two named discussants and read by policymakers, so identification must be **both rigorous and legible**. The academic discussant will apply the modern frontier; the policy discussant must be able to follow *why* the estimate is causal without reading the appendix. The discipline: make the **mapping from data/variation to the policy claim** explicit in the main text in plain language, and carry the formal defense in a technical appendix (EP's house split — accessible main text, rigorous appendix). Because results feed a policy recommendation, the magnitude — not just the sign or the stars — must be defended; report standard errors and confidence intervals, never lean on significance asterisks for the headline claim.

## Branch A: Empirical causal design (most EP papers)

- **DID / event study:** with staggered policy adoption, move beyond TWFE — Callaway–Sant'Anna, Sun–Abraham, or de Chaisemartin–D'Haultfœuille. Show a clean event-study with pre-trends; a Goodman–Bacon decomposition pre-empts the "negative-weights" discussant.
- **IV:** strong first stage (report it); with weak instruments use Anderson–Rubin / weak-IV-robust sets. Defend exclusion in three registers — theory, institutions, and a falsification test — because the policy discussant trusts institutional logic.
- **RDD:** density test (McCrary / Cattaneo–Jansson–Ma), data-driven bandwidth + robustness, covariate smoothness, bias-corrected CIs. State who is at the cutoff and whether they are the policy-relevant population.
- **Inference:** cluster at the policy-assignment level; address few-cluster problems (wild-cluster bootstrap) — many EP designs have few treated jurisdictions.

## Branch B: Structural / quantitative policy model

- **Name what identifies each parameter** — tie it to a data moment, not "the estimator converged."
- **Targeted vs. untargeted moments:** report fit to targeted moments and validate against untargeted ones as out-of-sample discipline.
- **Counterfactual policy-invariance:** the whole point of EP is the counterfactual policy. Argue (Lucas-critique style) that the estimated parameters are invariant to the policy you simulate; if they are not, say so and bound it.
- **Numerical credibility:** state the objective (MLE/GMM/MSM), multi-start for the global optimum, tolerances; report Monte Carlo recovery of known parameters.

## Translate the design for the policy reader

For each design, write the one-sentence plain-language version that goes in the main text: e.g. "Because the reform applied only to firms just above a 50-employee threshold, firms just below serve as a control group — so the difference in their hiring is the reform's effect." The appendix carries the formal estimand and assumptions.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Economic Policy is policy-facing applied economics; foreground a credible design and a policy-relevant magnitude.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] One plain-language sentence in the main text: what variation identifies the policy effect
- [ ] Modern estimator where TWFE would bias (staggered rollout) + clean event-study leads
- [ ] IV: first stage reported; exclusion defended in theory + institutions + falsification
- [ ] RDD: density + bandwidth robustness + bias-corrected CIs; cutoff population is policy-relevant
- [ ] Structural: each parameter tied to a moment; counterfactual policy-invariance argued
- [ ] Inference clustered at assignment level; few-cluster correction if needed
- [ ] Headline magnitude reported with SE/CI; the policy claim never exceeds what identification supports

## Anti-patterns

- TWFE on staggered policy timing with no heterogeneity-bias discussion (the academic discussant pounces)
- An exclusion restriction stated only as "plausibly exogenous" with no institutional or falsification backing
- Running a counterfactual policy scenario on parameters whose invariance is never defended
- Hiding the entire identification argument in the appendix so the policy discussant cannot follow the causal story
- Headlining a policy recommendation off a starred coefficient without reporting the magnitude and its CI

## Output format

```text
【Journal】Economic Policy (EP)
【Skill】ecopol-identification
【Branch】empirical causal / structural-quantitative
【Plain-language identification】one sentence for the policy reader
【Frontier diagnostics】[event-study + Bacon / first-stage + AR / density + bandwidth / moments + invariance]
【Inference】SE/CI + clustering level (no asterisk-driven headline)
【What it does NOT identify】[...]
【Next skill】ecopol-theory-model
```
