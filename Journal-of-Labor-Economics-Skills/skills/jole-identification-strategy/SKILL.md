---
name: jole-identification-strategy
description: Use when the causal identification strategy is the bottleneck for a Journal of Labor Economics (JOLE) manuscript — DID/event study, IV including shift-share, RDD, RCT, and AKM firm–worker designs common in labor economics. Stress-tests the design to JOLE's bar before tables are drafted.
---

# Identification Strategy (jole-identification-strategy)

## When to trigger

- The empirical core is OLS + controls with an undefended causal claim
- A DID uses two-way fixed effects (TWFE) on staggered policy timing without modern estimators
- A shift-share / Bartik IV's exclusion or exposure-share exogeneity is unargued
- An RDD at an eligibility threshold lacks a density test or bandwidth robustness
- AKM firm–worker fixed effects may carry limited-mobility bias

## The JOLE identification bar

JOLE publishes empirical labor papers only when the causal claim is **credible and the data are replicable**. Labor referees apply the standard credibility ladder, tuned to labor settings (strong → weaker):

1. **RCT / field experiment** (e.g., training, hiring, job-search interventions) with balance and pre-registration
2. **RDD** at a clean eligibility threshold (program cutoffs, age/score rules)
3. **DID / event study** off a credibly exogenous labor reform (minimum wage, UI, mandate) with **modern estimators**
4. **IV**, including **shift-share / Bartik** designs, with a strong first stage and a defended exclusion restriction
5. **AKM two-way (firm + worker) fixed effects** for wage decompositions, with limited-mobility-bias correction
6. **Matching / selection-on-observables** — a complement, rarely the spine

A novel or newly linked labor dataset (matched employer–employee registers, administrative earnings) answering a first-order question can carry a paper even when the design is more descriptive — but only with disciplined measurement and a clear labor lesson.

## Branch paths

### Branch A: DID / event study (policy reforms)
- Staggered adoption? Move beyond TWFE: Callaway–Sant'Anna, Sun–Abraham, or de Chaisemartin–D'Haultfœuille; report a Goodman-Bacon decomposition to expose invalid negative-weight comparisons.
- Pre-trends: clean event-study plot with leads near zero.
- Inference: cluster at the treatment-assignment level (often state); wild-cluster bootstrap with few clusters.
- Placebo timing and placebo outcomes that should not move.

### Branch B: IV (incl. shift-share / Bartik)
- First-stage F strong; with weak instruments use Anderson–Rubin / weak-IV-robust sets.
- For shift-share: argue exogeneity of the **shares** (or of the shocks, per the design) and run share-level balance / falsification.
- Exclusion argued in three registers: labor theory, institutional detail, and falsification where the channel is absent.
- Report reduced form and OLS alongside IV; state the LATE/complier interpretation.

### Branch C: RDD (eligibility thresholds)
- Density / manipulation test at the cutoff; covariate smoothness and placebo cutoffs.
- Optimal bandwidth (Calonico–Cattaneo–Titiunik) plus bandwidth-robustness; bias-corrected CIs.
- Fuzzy RDD: report the first stage in the discontinuity.

### Branch D: RCT / field experiment
- Pre-analysis plan referenced; deviations reported.
- Balance table; attrition analysis (Lee bounds if differential).
- Multiple-hypothesis adjustment across outcomes/subgroups.
- External validity: what does this labor population teach beyond itself?

### Branch E: AKM firm–worker FE
- Identify off the **connected set** of firms linked by job movers.
- Address **limited-mobility (incidental-parameter) bias** — leave-out (KSS) or bias-corrected estimators — before interpreting firm-effect variance.
- Be explicit about what the firm and worker effects do and do not identify (exogenous-mobility assumption).

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JOLE is labor economics — the home of clean identification; DiD/IV/RDD and selection corrections are the binding constraint.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Identifying variation named in one sentence and defended as exogenous
- [ ] Design-appropriate diagnostics (pre-trends / density / first-stage F / balance / connected set)
- [ ] Modern estimator where TWFE would be biased (staggered policy DID)
- [ ] Shift-share exogeneity (shares or shocks) argued and tested
- [ ] AKM limited-mobility bias corrected before variance decomposition
- [ ] Inference matched to assignment level; few-cluster issues addressed
- [ ] LATE / ATT / external-validity interpretation stated
- [ ] The claim never exceeds what the design supports

## Anti-patterns

- TWFE on staggered minimum-wage / reform timing with no heterogeneity-bias discussion
- A shift-share IV with no argument for share (or shock) exogeneity
- Interpreting AKM firm-effect dispersion without correcting limited-mobility bias
- RDD reporting one bandwidth and hiding sensitivity
- A clean local labor estimate oversold as a universal structural parameter

## Output format

```
【Design】RCT / RDD / DID / IV (incl. shift-share) / AKM / descriptive
【Identifying variation】one sentence
【Diagnostics done】[pre-trends, density, first-stage F, balance, connected set, ...]
【Diagnostics missing】[...]
【Inference】clustering level + few-cluster handling
【Interpretation】LATE / ATT / firm-effect caveat / external validity
【Next step】jole-data-analysis
```
