---
name: jue-identification
description: Use when the spatial identification argument is the bottleneck for a Journal of Urban Economics (JUE) manuscript — boundary discontinuity, shift-share/Bartik, historical or geographic IV, place-based DiD, or mobility experiment. Stress-tests the spatial design against sorting, spillovers, and spatial-autocorrelation confounds before exhibits are finalized.
---

# Spatial Identification (jue-identification)

## When to trigger

- A causal claim rests on OLS + region controls, or TWFE on staggered place-based policy
- A shift-share/Bartik instrument's exogeneity (shares vs shocks) is asserted, not argued
- A boundary/border discontinuity lacks a continuity-of-confounders defense
- The estimate could be driven by **spatial sorting/selection** across locations rather than the treatment
- Control areas may be contaminated by **spillovers/displacement** (SUTVA failure)
- Inference ignores **spatial autocorrelation** (Conley/HAC) and overstates precision

## The JUE identification bar

JUE referees are sophisticated about the failure modes that are *specific to space*. A clean national design is not enough; you must defend it against the three spatial confounds that recur in every urban paper: **(1) sorting/selection** — people, firms, and developers choose locations, so cross-location comparisons mix treatment with composition; **(2) spillovers/SUTVA** — treating one place moves activity to or from neighbors, contaminating controls and biasing reduced forms; **(3) spatial autocorrelation** — nearby units are correlated, so naive SEs are too small. State the estimand, name the identifying variation, show the diagnostic that could have failed, and address all three confounds explicitly.

## Design paths

### Path A: Boundary / spatial discontinuity (school zones, jurisdiction borders, corridors)
- **Continuity defense:** show pre-determined covariates are smooth across the boundary; the running variable is geographic distance.
- Local-linear with data-driven bandwidth; **bias-corrected robust CIs**; donut to drop units at the exact line; bandwidth sensitivity.
- Defend that the boundary is not also a discontinuity in *something else* (other jurisdiction services, zoning, natural features).
- The estimand is the **local** effect at the border — resist extrapolating to the whole city.

### Path B: Shift-share / Bartik (local labor demand, immigration, trade exposure)
- State whether identification rests on **exogenous shares** (Goldsmith-Pinkham–Sorkin–Swift; report Rotemberg weights) or **exogenous shocks** (Borusyak–Hull–Jaravel).
- Show the implied just-identified instruments and which industries/shocks drive the estimate.
- Address that initial shares reflect prior sorting; defend pre-period balance and exclusion.

### Path C: Historical / geographic IV (terrain, soil, historical infrastructure, lines on maps)
- Argue the instrument affects the outcome **only through** the spatial channel of interest — the exclusion restriction is where these papers live or die.
- Falsification on placebo outcomes and never-treated channels; control for the geography the instrument correlates with.

### Path D: Place-based policy DiD / event study (zones, infrastructure, rezoning)
- With staggered rollout, **move beyond TWFE** (Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille); clean event-study leads; Goodman-Bacon decomposition.
- **Spillover-robust controls:** ring/donut specifications around treated areas; estimate displacement to neighbors rather than assuming SUTVA.
- Rambachan–Roth honest-DID sensitivity to parallel-trend violations.

### Path E: Mobility / neighborhood experiment (MTO-style, voucher lotteries)
- Lottery/randomization as the source of variation; ITT and LATE/TOT distinguished; non-compliance handled.
- Selection into take-up addressed; neighborhood exposure measured, not assumed.

## Cross-cutting spatial inference

- **Spatial autocorrelation:** Conley spatial-HAC SEs (with a defended distance cutoff) or cluster at the spatial-market level; report how SEs change versus naive.
- **Sorting/selection:** show composition is balanced or model the sorting; never present a cross-location comparison as if locations were randomly assigned.
- **SUTVA/spillovers:** define the treated and control geography so that spillovers do not contaminate controls; estimate the spillover itself where possible.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JUE is urban/spatial economics — sorting and spatial dependence; identification + Conley/spatial-robust inference.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Estimand named (local-at-boundary / ATT / LATE) and matched to the design
- [ ] The spatial variation is stated in one sentence; the diagnostic that could have failed is shown
- [ ] **Sorting/selection** addressed (balance, composition, or explicit sorting model)
- [ ] **Spillovers/SUTVA** addressed (rings/donuts; displacement estimated, not assumed away)
- [ ] **Spatial autocorrelation** in inference (Conley/spatial cluster), reported vs naive SEs
- [ ] Shift-share: shares-vs-shocks identification stated; Rotemberg weights or BHJ reported
- [ ] Modern estimator where TWFE/2SLS would bias; the claim never exceeds the local estimand

## Anti-patterns

- TWFE on staggered place-based policy with no heterogeneity-bias discussion
- A boundary RD with no covariate-smoothness test or with the boundary confounding other services
- "Plausibly exogenous" shares/geography asserted with no falsification or Rotemberg/BHJ diagnostic
- Treating control regions as clean when treatment plausibly displaced activity into them
- Naive (non-spatial) standard errors on geographically clustered data
- Reading a local boundary or LATE estimate as a city-wide or national effect

## Referee pushback mapped to the identification fix

- *"This is sorting, not the treatment."* → Show pre-period composition is balanced across treated/control, or model the location choice; add a placebo on pre-trends.
- *"Your controls are contaminated by displacement."* → Add a spillover ring; estimate the displacement to neighbors rather than assuming SUTVA; show controls outside the ring give the same answer.
- *"Your standard errors ignore spatial correlation."* → Report Conley spatial-HAC SEs at a defended distance cutoff and contrast them with the naive SEs.
- *"Staggered TWFE is biased here."* → Re-estimate with Callaway–Sant'Anna or Sun–Abraham; show flat event-study leads and a Goodman-Bacon decomposition.
- *"Your shift-share shares are not exogenous."* → Report Rotemberg weights (which industries drive it) or move to a Borusyak–Hull–Jaravel shock-exogeneity argument.

## Worked vignette (illustrative)

A new light-rail line is evaluated with a DiD comparing corridor tracts to the rest of the metro. A referee flags two spatial confounds: richer households **sort** into the corridor, and demand **displaced** from control tracts contaminates them. The JUE fix: a boundary-distance design with ring controls (0–800m treated, 800–1600m as a spillover ring, >1600m control), covariate-smoothness across the ring boundary, Conley SEs with a 5km cutoff, and a sorting check on pre-period demographics. The capitalization estimate settles at 4.5% (Conley s.e. 1.3) and the spillover ring shows measurable displacement — reported, not hidden.

## Output format

```text
【Design】boundary-RD / shift-share / historical-IV / place-based-DiD / mobility-experiment
【Spatial variation → estimand】one sentence
【Estimand】local-at-boundary / ATT / LATE
【Sorting/selection】how addressed
【Spillovers/SUTVA】rings/donut; displacement estimated?
【Spatial inference】Conley/spatial cluster + cutoff; vs naive SEs
【What it does NOT identify】[...]
【Next skill】jue-theory-model (if a model is needed) or jue-robustness
```
