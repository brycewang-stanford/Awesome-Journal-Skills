---
name: rfs-identification
description: Use when the causal-inference or asset-pricing identification strategy is the bottleneck for a The Review of Financial Studies (RFS) manuscript — quasi-experiments (DID, IV, RDD, event study) and factor-model identification. Stress-tests the design before drafting tables.
---

# Identification Strategy (rfs-identification)

## When to trigger

- The empirical core is OLS + controls with an open endogeneity threat
- A DID uses two-way fixed effects (TWFE) without addressing staggered-adoption bias
- An IV has a weak first stage or a contestable exclusion restriction
- A cross-sectional asset-pricing claim rests on a factor that may be data-mined
- Reviewers will ask "what is your source of variation?" and you lack a crisp answer

## The RFS identification bar

RFS applies the **same high causal-inference standard as JF and JFE**: a claim of causality requires a credible source of exogenous variation, not a richer control set. RFS is more receptive than the others to *genuinely new questions* and to *structural / theoretical* identification — but novelty never substitutes for a clean design. Pick the strongest feasible strategy below.

**RFS-specific lever — Stage 1 design review.** Because RFS pioneered **Registered Reports** (pre-results review; Karolyi, "Kick-Starting the Review Process," RFS 27(2), 2014), an identification strategy can be **refereed before the results exist**. If you pursue this route, the design must be airtight on paper: pre-specified sample, treatment definition, estimator, diagnostics, and the exact tables to be produced — because that protocol becomes the binding commitment that earns *in-principle acceptance*. Even for a standard submission, draft the design as if it had to survive Stage 1 review with no results to fall back on.

### Design priority (corporate / household / empirical finance)

1. **Natural experiment / policy shock + DID** (incl. staggered and continuous treatment)
2. **Regression discontinuity** (a sharp institutional threshold: index inclusion, rating cutoff, covenant)
3. **Instrumental variables** (strong first stage + a defensible, finance-grounded exclusion)
4. **Event study** with clean windows and confound discussion
5. **Matching / propensity-score + DID** as a supplement, rarely as the sole strategy
6. **Structural estimation** when the question is about a parameter or counterfactual

### Branch A — DID
- Staggered adoption? → diagnose with Goodman-Bacon decomposition; estimate with Callaway–Sant'Anna, Sun–Abraham, or de Chaisemartin–D'Haultfœuille.
- Parallel trends: show an event-study plot with pre-trends, not a single pre-period dummy.
- Placebo: randomize treatment timing / units; report the placebo distribution.
- Continuous/dose treatment: justify the dose measure and its exogeneity.

### Branch B — IV
- First-stage F well above conventional weak-IV thresholds; if borderline, report Anderson–Rubin or other weak-IV-robust inference.
- Exclusion restriction defended in three registers: theory, institutional detail, and a placebo/falsification.
- Report the reduced form, not only the second stage.
- Address the instrument's own potential endogeneity explicitly.

### Branch C — RDD
- McCrary / density test for manipulation at the cutoff.
- Optimal bandwidth (Calonico–Cattaneo–Titiunik) plus at least three bandwidth-robustness checks.
- Covariate smoothness across the threshold.

### Branch D — Asset-pricing identification
- Factor construction: pre-register the sort/breakpoints logic; avoid look-ahead and survivorship bias.
- Standard errors: Fama–MacBeth or panel with errors clustered/adjusted appropriately (e.g., Newey–West, Driscoll–Kraay) — never naive OLS SEs on overlapping returns.
- Multiple testing: when the claim is a new predictor, confront the data-mining critique (see `rfs-robustness`).
- Out-of-sample and subsample stability for any predictability claim.

### Branch E — Structural / theory-driven
- State the identifying assumptions and which moments identify which parameters.
- Provide a counterfactual or decomposition that reduced form cannot deliver.
- Show the model fits untargeted moments.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). RFS is finance top-3 (with JF, JFE) — corporate-causal chain for corporate papers, factor-zoo haircut for asset pricing.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] The source of exogenous variation is stated in one sentence
- [ ] Design-appropriate diagnostics run (parallel trends / density / first-stage F / SE choice)
- [ ] Placebo or falsification test included
- [ ] Standard-error structure matches the data (clustering / overlap / cross-section)
- [ ] Endogeneity threats are listed and each is addressed, not waved away
- [ ] For asset pricing, multiple-testing and out-of-sample concerns are anticipated
- [ ] Design is specified tightly enough to survive a Stage 1 (Registered Report) review with no results

## Anti-patterns

- TWFE on staggered treatment with no discussion of heterogeneous-effect bias.
- "We control for many observables, so the effect is causal."
- An IV that is "an exogenous event × a lagged endogenous variable."
- A new return predictor reported without confronting the multiple-testing critique.
- Naive standard errors on overlapping or autocorrelated returns.

## Output format

```
【Strategy】DID / RDD / IV / event study / asset-pricing / structural
【Source of variation】one sentence
【Diagnostics done】[parallel trends, density, first-stage F, SE choice, ...]
【Missing diagnostics】[...]
【SE structure】...
【Next step】rfs-empirical-design
```
