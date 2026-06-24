---
name: restud-identification
description: Use when selecting, implementing, or stress-testing the causal identification strategy for an empirical The Review of Economic Studies (REStud) manuscript — DID (incl. staggered), IV (incl. weak-IV-robust inference), RDD, synthetic control, shift-share, or RCT. Apply before writing results; for theory papers route to restud-theory-model.
---

# REStud Identification (restud-identification)

## When to trigger

- The empirical core is OLS + controls and a referee will flag selection-on-observables
- DID uses TWFE on staggered data with no modern estimator
- IV first-stage F is being cited as proof of instrument strength
- RDD uses a high-order polynomial or one untested bandwidth
- A prior rejection cited identification grounds and the design needs rebuilding

## REStud identification bar

REStud was founded in 1933 to advance **both theoretical and applied** economics, and that balance is its signature: unlike a purely empirical top-5 outlet, REStud weighs design-based causal work and structural/theory-consistent identification on equal terms. So the bar is a **state-of-the-art causal design**, OR — for a structural/theoretical-empirical paper — a rigorous identification of the model's parameters with the identifying assumptions stated explicitly and mapped to data features. The empirical contribution can itself be *a new identification strategy*; in that case the design is the paper and must be defended to the hilt. Editorial assignment reflects the breadth: handling Joint Managing Editors span IO/applied econometrics (Jan De Loecker), micro theory / mechanism design (Antonio Penta), and behavioral/information economics (Jakub Steiner) — write the identification so the right one of them sees a rigorous argument. Identification is not a section to be footnoted; if the design is fragile, no prose, controls, or sample size rescues it.

## Master decision tree

```
Is treatment plausibly random by design (RCT, lottery)?
├── Yes → analyze as an experiment; pre-register / PAP where applicable
└── No → identification comes from variation
    ├── Sharp threshold in a running variable → RDD (sharp / fuzzy)
    ├── Policy hits some units over time, not others → DID
    │     ├── One treatment date → canonical 2x2 DID
    │     └── Staggered adoption → Callaway-Sant'Anna / Borusyak-Jaravel-Spiess / Sun-Abraham
    ├── Endogenous regressor + plausibly exogenous shifter → IV
    │     ├── Shifter x exposure shares → shift-share / Bartik
    │     └── Single instrument, F < 50 → weak-IV-robust inference (AR)
    ├── One / few treated aggregate units → synthetic control
    └── Structural parameter of interest → restud-theory-model (state identifying assumptions)
```

## Branch A — Difference-in-Differences

- **Staggered adoption:** do **not** use TWFE. Use Callaway-Sant'Anna (`csdid` / `did`), Borusyak-Jaravel-Spiess imputation, de Chaisemartin-D'Haultfœuille, or Sun-Abraham.
- Report a **Goodman-Bacon decomposition** to expose the weight on forbidden comparisons under TWFE.
- **Pre-trends:** event-study plot *and* the formal joint test, not just the visual.
- **Honest DiD (Rambachan-Roth 2023)** sensitivity bounds for the post-period.

## Branch B — Instrumental Variables

- The first-stage **F > 10 rule is obsolete.** For just-identified models report **Anderson-Rubin confidence sets** as primary inference; for F < 50, AR is required, not optional. Use the Olea-Pflueger effective F.
- **Exclusion restriction** is a story, not a test: state it in one sentence, defend with institutional narrative + a placebo where the instrument should have no effect + Conley et al. (2012) plausibly-exogenous sensitivity.
- Report the **reduced form** and argue the instrument's own exogeneity.

## Branch C — Regression Discontinuity

- Local linear, triangular kernel; polynomials of order > 1 discouraged (Gelman-Imbens 2019).
- MSE-optimal bandwidth with robust bias-corrected CI (`rdrobust`).
- Diagnostics: McCrary / Cattaneo-Jansson-Ma density test; covariate balance at the cutoff; placebo cutoffs; estimate stable across ≥ 3 bandwidths; an `rdplot` with the binning stated.

## Branch D — Synthetic control / shift-share

- **SCM:** in-time and in-space placebos; permutation / Fisher exact p-value; weight vector in the appendix. Consider generalized SCM (Xu 2017) or synthetic DiD (Arkhangelsky et al. 2021).
- **Shift-share:** declare the source of identification — exogenous shares (Goldsmith-Pinkham-Sorkin-Swift; report Rotemberg weights) **or** exogenous shocks (Borusyak-Hull-Jaravel; Adão-Kolesár-Morales). Do not hand-wave between them.

## Branch E — Structural / theory-consistent

- State each identifying assumption explicitly and map it to a feature of the data.
- Provide identification arguments (which moments identify which parameters) before estimation.
- Route the model and proofs to `restud-theory-model`; supply counterfactuals.
- This is squarely REStud territory: the journal's canon includes structural identification of policy-relevant parameters — e.g., Mirrlees (1971), "An Exploration in the Theory of Optimum Income Taxation," REStud 38(2), where the structure *is* the identification. Hold your structural argument to that standard.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). REStud is top-5 general-interest economics; credible identification with modern estimators is the bar across applied fields.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Design-based strategy named; not "OLS with controls" as the headline
- [ ] Modern estimator used where the textbook default is biased (staggered DID, weak IV, naive RDD)
- [ ] Pre-trends / density / balance / weak-IV diagnostics reported as required by the branch
- [ ] Inference method correct (cluster-robust at the right level / AR / wild bootstrap / permutation)
- [ ] Identifying assumption stated in one sentence in the introduction
- [ ] Placebo / falsification test present

## Anti-patterns

- TWFE on staggered data with no Goodman-Bacon decomposition
- First-stage F = 12 cited as evidence of instrument strength
- RDD with a 4th-order polynomial and one untested bandwidth
- IV exclusion restriction defended only by "we control for X"
- Reporting OLS-with-controls as the main spec and IV/RD as "robustness"
- Footnoting the identifying assumption instead of stating it up front

## Output format

```
【STRATEGY】DiD | IV | RDD | SCM | shift-share | RCT | structural
【MODERN ESTIMATOR】yes / no / which
【DIAGNOSTICS REPORTED】[...]
【INFERENCE】cluster-robust / AR / wild bootstrap / permutation
【RED FLAGS】[... or "none"]
【NEXT SKILL】restud-robustness (or restud-theory-model if structural)
```
