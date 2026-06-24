---
name: jegeo-robustness
description: Use when results for a Journal of Economic Geography (JEG) manuscript may be sensitive to spatial scale, the weight matrix, spatial autocorrelation, sample, or specification. Organizes robustness by spatial threat; it does not invent results.
---

# Robustness Strategy (jegeo-robustness)

## When to trigger

- The headline result might flip at a different spatial scale (region vs. commuting zone vs. grid cell)
- A spatial-econometric model's results depend on the chosen spatial weight matrix W
- Standard errors ignore spatial correlation across units, so inference is overstated
- Reviewers may suspect the effect is driven by a few large regions, a boundary artifact, or one definition of the spatial unit
- You have a long appendix of checks with no story about which threat each one answers

## The spatial robustness threats unique to JEG

Most JEG robustness work is not generic — it answers threats that arise *because the data are spatial*. Organize by threat, not by a mechanical list, and lead with the spatial ones because that is where both communities probe hardest.

| Threat | What a referee fears | The check that answers it |
|--------|----------------------|---------------------------|
| **Modifiable Areal Unit Problem (MAUP)** | the result is an artifact of how space was carved into units | re-estimate at ≥2 spatial scales / aggregations; show the effect survives |
| **Spatial weight matrix sensitivity** | W was reverse-engineered to fit | vary W (contiguity, k-nearest, distance-decay, economic distance); report the spread |
| **Spatial autocorrelation in errors** | inference is overstated; "significance" is spurious | Conley spatial-HAC SEs over a range of cutoff distances; Moran's I on residuals |
| **Spatial spillovers / SUTVA** | the effect leaks into "control" units | ring/donut specs; spatial-lag or SDM models; bound the leakage |
| **Boundary / edge effects** | border units behave differently | drop border units; buffer zones; alternative boundary definitions |
| **Driven by a few places** | one metro or region carries the result | leave-one-region-out; jackknife the largest units |
| **Scale-dependent mechanism** | the mechanism only "works" at one resolution | show the sign/magnitude pattern is coherent across scales |

## Sequencing the robustness section

1. **Spatial-scale / MAUP first** — if the result is scale-fragile, nothing else matters. Show it holds (or is honestly bounded) across aggregations.
2. **Inference next** — Conley SEs and residual Moran's I; this is where overclaiming dies at JEG.
3. **Spillovers / spatial model** — the SDM/SAR/SEM choice should be motivated by the mechanism, not run for completeness; report direct vs. indirect (spillover) effects if you use a spatial-lag model.
4. **Sample / influence** — leave-one-region-out, alternative samples, outlier regions.
5. **Specification** — alternative controls, functional form — last, and brief.

Each robustness exhibit should answer "which threat does this kill?" in its title or note.

## The two robustness checks JEG referees ask for most

Across submissions, two requests recur so reliably that strong authors pre-empt them in the first version:

1. **"Show it at another spatial scale."** Have the alternative-aggregation result ready (commuting zone if you used regions, or a finer grid), and report the attenuation honestly. This is the MAUP defense and it is almost always asked.
2. **"Are your standard errors honest about spatial correlation?"** Have Conley SEs over a few cutoff distances plus a residual Moran's I in hand. Reviewers from the economics side treat the absence of this as a reason to discount every t-statistic.

Building both before submission converts two likely R&R demands into evidence of rigor — and, if either weakens the result, you would far rather discover it yourself than have a referee surface it.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JEG is spatial economics — spatial dependence and sorting; emphasize identification and Conley/spatial-robust inference.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] MAUP confronted: result shown across ≥2 spatial scales or aggregations
- [ ] Spatial weight matrix W varied; sensitivity of the estimate reported
- [ ] Spatial autocorrelation in errors addressed (Conley SEs over cutoffs; residual Moran's I)
- [ ] Spillovers/SUTVA: spatial-lag/SDM or ring spec; direct vs. indirect effects if relevant
- [ ] Boundary/edge effects checked
- [ ] Leave-one-region-out / influence of the largest units shown
- [ ] Every robustness exhibit is labeled by the threat it answers, not "Appendix Table A7"

## Anti-patterns

- A single spatial scale with no MAUP check, presented as if the unit were natural
- One spatial weight matrix, never varied, with results that depend on it
- Default or one-way-clustered SEs when residuals are visibly spatially correlated
- A spatial-lag model run only to look sophisticated, with indirect effects never interpreted
- A 15-table robustness appendix with no mapping from check to identifying threat
- Hiding a scale-fragile result by reporting only the scale where it is significant

## Worked vignette (illustrative)

A cluster-productivity result is significant at the NUTS-3 region level with region-clustered SEs. A referee asks two spatial questions: does it survive at the commuting-zone scale (MAUP), and are the SEs honest given that adjacent regions co-move? Re-aggregating to commuting zones, the point estimate holds but attenuates ~20%; Conley SEs at a 100km cutoff roughly double the standard error, and the effect remains positive but now marginal. Reporting both — rather than only the favorable NUTS-3/clustered combination — is what earns referee trust at JEG, even though it weakens the headline. Honesty about spatial fragility beats a fragile asterisk.

## Referee pushback mapped to the robustness fix

- *"How do I know this isn't a MAUP artifact?"* → Show the estimate across ≥2 scales/aggregations; report attenuation honestly.
- *"You chose W to get this result."* → Vary W (contiguity, k-NN, distance-decay, economic distance) and report the spread, not one favorable matrix.
- *"Your t-stats assume spatial independence."* → Conley SEs over several cutoffs plus residual Moran's I.
- *"It's all driven by [the capital region]."* → Leave-one-region-out and a jackknife of the largest units.
- *"The 'spillover' is just spatial trend."* → Distinguish a spatial-lag spillover from a common spatial trend by including the trend and testing the lag separately.

## A note on what NOT to over-do

JEG referees value an honest, threat-organized robustness section over a wall of tables. A spatial-Durbin model, a spatial-error model, and three W matrices run "for completeness," with none interpreted, signals fishing rather than rigor. Choose the spatial model that matches the mechanism (does theory predict spillovers? then SDM and interpret the indirect effect; if not, do not bolt one on), and let each remaining check answer one named threat. Candor about a bounded or scale-fragile result reads as strength here; a defended asterisk reads as weakness.

## Output format

```text
【Journal】Journal of Economic Geography
【Skill】jegeo-robustness
【Top spatial threat】MAUP / W-sensitivity / spatial autocorrelation / spillovers / boundary / influence
【MAUP check】scales tested + result
【Inference】Conley SEs (cutoffs) + residual Moran's I
【Spillover/spatial-model】spec + direct vs indirect effects
【Influence】leave-one-region-out result
【Honest verdict】robust / bounded / fragile (and where)
【Next skill】jegeo-tables-figures
```
