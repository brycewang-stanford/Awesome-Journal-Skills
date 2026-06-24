---
name: jeem-robustness
description: Use when a Journal of Environmental Economics and Management (JEEM) manuscript's headline estimate — a damage, WTP, pass-through, or treatment effect — must be shown to survive specification, spatial, sample, and inference choices. Builds the targeted robustness suite environmental-economics referees expect; it does not establish primary identification (jeem-identification) or format exhibits (jeem-tables-figures).
---

# Robustness Strategy (jeem-robustness)

## When to trigger

- The main estimate is in hand and you must show it is not a one-specification artifact
- A referee asks "is this robust to spatial correlation / alternative bandwidth / sample / functional form?"
- The result depends on a market definition, a buffer radius, a weather aggregation, or a pollution-monitor selection that could be questioned
- You suspect specification-search concerns in a hedonic or valuation and want to pre-empt them

## The JEEM robustness bar

JEEM referees probe whether the welfare-relevant number is **stable, spatially honest, and not the product of researcher degrees of freedom**. Robustness here is not a wall of regressions — it is a **targeted set of checks each tied to a specific threat**, several of which are distinctively environmental. Map every plausible objection to the one check that answers it, and report so the reader sees the estimate barely moves.

| Threat to the result | The check that answers it |
|----------------------|---------------------------|
| Spatial correlation in errors | Conley spatial SEs; vary the cutoff distance; cluster on geography |
| Hedonic market / buffer definition | vary the buffer radius, the boundary band, the housing-market boundary |
| Omitted amenities / sorting | parcel/boundary FE; amenity controls in steps; Oster δ for selection |
| Staggered-DiD bias | Callaway–Sant'Anna or Sun–Abraham; honest-DiD pre-trend bounds |
| Weather/climate aggregation | alternative bins/degree-days; alternative gridded products; placebo seasons |
| Monitor/station selection | reweight by coverage; restrict to dense-monitor areas; interpolation sensitivity |
| Valuation functional form | semi-log vs. Box–Cox hedonic; mixed-logit vs. conditional logit; WTP-space estimation |
| Inference too narrow | correct clustering level; wild-cluster bootstrap (few units); randomization inference |
| Multiple outcomes/subgroups | Romano–Wolf / List–Shaikh–Wooldridge MHT adjustment |

## Robustness craft

1. **Lock the primary specification first.** Everything else is a perturbation around it; do not present five co-equal specs and let the reader guess the preferred one.
2. **One threat → one check.** A robustness table reads as "here is the worry, here is the evidence it is not a problem."
3. **Show stability of the welfare number, not just significance.** The persuasive object is that the *damage / WTP / pass-through* barely moves, not that an asterisk survives.
4. **Treat space as first-order.** Wrong (non-spatial) SEs are the single most common JEEM robustness failure; vary the Conley cutoff and report it.
5. **Be honest where it weakens.** A check that shifts the estimate is information — bound the implication rather than hiding it.

## The environmental robustness checks referees expect first

Three checks are close to mandatory at JEEM and should appear in the main results, not the appendix:

1. **Spatial inference.** If the units are geographic and shocks are spatially correlated (almost always, for pollution, weather, land, and housing), report Conley spatial standard errors and vary the cutoff distance. "We cluster by state" is not a defense when the relevant correlation is at the watershed or airshed scale.
2. **Geographic-scope sensitivity.** Vary the buffer radius, the boundary band, or the market definition; show the welfare estimate is not an artifact of one arbitrary spatial window.
3. **Design-timing sensitivity.** For staggered regulations, an honest-DiD bound on the pre-trend; for RD thresholds, a bandwidth sweep and a donut. These show the design, not luck, produced the result.

A paper that omits all three reads as not knowing the field's standards, regardless of how many other columns the robustness table has.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JEEM is environmental economics — policy/regulation designs and non-market valuation; the causal chain serves its program-evaluation lane.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Primary specification declared before perturbations
- [ ] Each check mapped to a specific threat, not added for volume
- [ ] Spatial inference: Conley SEs with a reported cutoff, or geographic clustering, where units are spatial
- [ ] Hedonic/valuation: buffer radius, market boundary, and functional form varied
- [ ] Design-specific sensitivity (honest-DiD bounds / RD bandwidth / weak-IV set) included
- [ ] Selection-on-unobservables addressed (Oster δ or stepwise controls) for hedonics
- [ ] Multiple-hypothesis adjustment if many outcomes/subgroups/regions
- [ ] Stability of the welfare-relevant point estimate shown; any check that moves it reported honestly

## Anti-patterns

- Default standard errors on spatially correlated environmental data ("we clustered by state" when the shock is local)
- A 20-column robustness table with no map from check to threat ("kitchen-sink robustness")
- Reporting only that significance survives while the WTP/damage wanders
- One arbitrary buffer radius / market definition with no sensitivity to it
- Hiding the weather aggregation or monitor sample that breaks the result
- Subgroup or regional p-hacking with no MHT correction

## Worked vignette (illustrative)

A pollution-mortality estimate is 3.1 deaths per 100k per unit (s.e. 0.9, default SEs). The suite: (i) Conley SEs at a 100 km cutoff widen the CI but keep it from zero; (ii) re-binning the pollution exposure barely moves the point estimate; (iii) restricting to dense-monitor counties yields 3.0; (iv) an honest-DiD bound on the staggered regulation pre-trend leaves the sign intact; (v) Oster δ implies selection on unobservables would need to be 2× selection on observables to nullify it. The welfare number barely moves — the JEEM target.

## Branch-specific robustness emphases

- **Hedonic / RP valuation:** the binding worries are sorting and market definition — lead with boundary FE, an amenity-shock specification, and buffer/market-boundary sweeps; report Oster δ for selection on unobservables.
- **Stated preference:** robustness is about the elicitation — show the scope test, sensitivity to the choice-model specification (conditional vs. mixed vs. latent-class logit), WTP-space vs. preference-space estimation, and protest-response handling.
- **Regulation DiD:** honest-DiD bounds on pre-trends, alternative comparison groups, and a Goodman-Bacon decomposition to show no "bad comparisons" drive the result.
- **Climate / weather:** alternative weather products and binning, placebo seasons, and spatial-and-serial-correlation-robust SEs; show the result is not an artifact of one gridded dataset.

Each emphasis answers the threat that is *first-order for that branch* — do not spend the robustness budget on generic checks while the branch's signature worry goes unaddressed.

## Output format

```text
【Journal】Journal of Environmental Economics and Management
【Skill】jeem-robustness
【Primary spec】declared? [Y/N] — estimate: ___ (s.e. ___)
【Threat → check map】spatial: ___ | market-def: ___ | sorting: ___ | weather-agg: ___ | inference: ___
【Spatial inference】Conley cutoff / clustering: ___
【Design sensitivity】honest-DiD / RD bandwidth / weak-IV set: ___
【Estimate stability】range across checks: [___, ___]; checks that move it: ___
【Source status】verified URL / 待核实 / not asserted
【Next skill】jeem-tables-figures
```
