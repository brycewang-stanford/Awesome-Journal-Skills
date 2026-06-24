---
name: jue-robustness
description: Use when a Journal of Urban Economics (JUE) manuscript's headline spatial estimate must be shown to survive specification, spatial-scale, sorting, spillover, and inference choices before submission or in an R&R. Builds the spatially-aware robustness suite a JUE referee expects; it does not establish the identification (jue-identification) or format the maps (jue-tables-figures).
---

# Spatial Robustness Suite (jue-robustness)

## When to trigger

- The main spatial estimate is in hand and must be shown not to be an artifact of one specification
- A referee asks "is this robust to the spatial scale / the buffer / the geography you chose?"
- The result depends on a bandwidth, a ring radius, a fixed-effects geography, or a clustering choice
- You need to rule out that **spatial sorting** or **MAUP** (modifiable areal unit problem) drives the result
- The estimate could move under a spatial-spillover or boundary-definition change

## The JUE robustness bar

JUE referees probe whether the spatial estimate is **stable across the spatial choices the researcher made** — the scale of the units, the boundaries, the buffer/ring radii, the fixed-effects geography — and whether inference accounts for spatial dependence. Robustness here is not a wall of regressions; it is a **targeted set of checks, each tied to a spatial threat**, reported so the reader sees the point estimate barely moves.

| Spatial threat to the result | The check that answers it |
|------------------------------|---------------------------|
| Modifiable areal unit problem (MAUP) | re-estimate at multiple spatial scales (tract / block-group / zip); show the estimate is scale-stable |
| Boundary/buffer arbitrariness | vary ring radii and donut widths; show insensitivity to the cut |
| Spatial sorting / selection | balance on pre-period composition; control for or model sorting; placebo on pre-trends |
| Spillovers / SUTVA | estimate the spillover ring; show controls outside the spillover zone give the same answer |
| Spatial autocorrelation in inference | Conley SEs across distance cutoffs; spatial cluster vs naive |
| Geographic confounders | add finer geographic fixed effects (commuting zone, grid cell) and show stability |
| Omitted local trends | region-specific linear trends; pre-trend leads flat |
| Specification search | a specification curve over scale × FE × bandwidth; declare the primary spec |

## Robustness craft

1. **Lock the primary spatial specification first** — the scale, FE geography, and bandwidth you prefer — then perturb around it. Do not present five co-equal spatial specs.
2. **One spatial threat → one check.** Each robustness exhibit reads "here is the worry (MAUP / spillover / sorting / spatial SEs), here is the evidence it is not the story."
3. **Show stability of the point estimate**, not just that significance survives — across scales, radii, and FE geographies the coefficient should barely move.
4. **Stress-test inference for spatial dependence.** Report Conley SEs at several distance cutoffs; wrong (non-spatial) SEs are the most common JUE robustness failure.
5. **Report honestly where it weakens.** A check that shifts the estimate is information — bound the implication rather than hiding the specification.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JUE is urban/spatial economics — sorting and spatial dependence; identification + Conley/spatial-robust inference.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Primary spatial spec declared (scale, FE geography, bandwidth) before perturbations
- [ ] MAUP addressed: estimate stable across at least two spatial scales
- [ ] Boundary/ring choices varied; result insensitive to radius and donut width
- [ ] Sorting/selection check (pre-period balance / placebo pre-trends)
- [ ] Spillover ring estimated; controls outside the spillover zone give the same answer
- [ ] Conley/spatial-cluster SEs reported across distance cutoffs, vs naive
- [ ] Finer geographic FE / local trends show the point estimate barely moves
- [ ] A spatial placebo (fake boundary / pre-period / unaffected outcome) is shown to be null
- [ ] For a QSM, counterfactual sensitivity to the least-identified elasticity is reported
- [ ] Any check that moves the estimate is reported and bounded honestly

## Anti-patterns

- A 20-column robustness table with no map from check to *spatial* threat (kitchen-sink robustness)
- Reporting one spatial scale only, leaving MAUP unaddressed
- Naive standard errors on geographically clustered data, then claiming robustness
- Hand-picking the ring radius or bandwidth that maximizes significance
- Reporting that significance survives while the point estimate wanders across scales
- Hiding the FE geography or boundary definition that breaks the result

## Referee pushback mapped to the robustness fix

- *"This is an artifact of your spatial scale."* → Re-estimate at tract / block-group / commuting-zone; show the coefficient is scale-stable (MAUP not driving it).
- *"Your boundary/ring radius is arbitrary."* → Vary radii and donut widths; show insensitivity across the grid of cuts.
- *"Did you cluster for spatial dependence?"* → Conley SEs at several distance cutoffs (and a spatial-cluster alternative), contrasted with naive SEs.
- *"This is specification search."* → Declare the primary spatial spec; show a specification curve over scale × FE × bandwidth in which the point estimate barely moves.

## Robustness for a structural / QSM paper

When the JUE paper is a quantitative spatial model, robustness shifts from specification perturbations to **parameter sensitivity and counterfactual stability**. Report how the headline counterfactual moves as the least-identified elasticities (migration, commuting, agglomeration) are varied across plausible ranges from the literature; show that the qualitative conclusion and the order of magnitude survive. A counterfactual that is fragile to one elasticity is a finding to bound and disclose, not to bury — the same honesty norm as reduced-form stability.

## Worked vignette (illustrative)

A density-wage elasticity is 0.045 (Conley s.e. 0.012). The spatial robustness suite: (i) re-estimated at tract, block-group, and commuting-zone scale, the elasticity stays in [0.041, 0.049] — MAUP is not driving it; (ii) Conley SEs at 50/100/200 km cutoffs keep the CI away from zero; (iii) adding commuting-zone fixed effects moves it to 0.043; (iv) a placebo on pre-period wage growth is flat, arguing against sorting on trends; (v) the spillover specification shows neighboring-area contamination is small. The point estimate barely moves — the JUE target.

## Spatial placebo and falsification

Beyond perturbing the main spec, the most persuasive JUE robustness evidence is a placebo that *should* show nothing and does. Useful spatial placebos: assign the treatment to a pre-period and show no effect (rules out pre-trends/sorting on trends); apply the design to an outcome that the mechanism should not move (rules out a generic local shock); shift the boundary or corridor to a fake location and show the discontinuity vanishes. A clean placebo is often worth more to a referee than another robustness column, because it tests the design rather than re-running it — and a placebo that unexpectedly *does* fire is critical information to report, not suppress.

## Output format

```text
【Primary spatial spec】scale / FE geography / bandwidth — estimate: ___ (Conley s.e. ___)
【MAUP】scales tested: ___ ; range: [___, ___]
【Boundary/ring】radii/donut varied? result stable? [Y/N]
【Sorting check】pre-period balance / placebo pre-trend: ___
【Spillover】ring estimated; controls-outside-zone consistent? [Y/N]
【Spatial inference】Conley cutoffs: ___ ; vs naive: ___
【Estimate stability】range across checks: [___, ___]; checks that move it: ___
【Next skill】jue-tables-figures
```
