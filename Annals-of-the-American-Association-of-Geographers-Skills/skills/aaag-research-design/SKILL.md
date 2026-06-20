---
name: aaag-research-design
description: Use when defending the research design of an Annals of the American Association of Geographers manuscript — spatial/quantitative analysis and GIScience, remote-sensing and physical-environmental methods, qualitative human-geography inference, or nature-society mixed methods. The Annals judges each tradition on its own terms. Strengthens the design; it does not write code.
---

# Research Design (aaag-research-design)

The Annals spans four areas and accepts many methodologies, but is demanding about each. The design
must credibly connect the geographic argument (`aaag-theory-building`) to the evidence, and must take
**space and scale seriously** — spatial dependence, the MAUP, projection, and sampling are design
issues, not afterthoughts. This skill is mode-aware: pick the section that matches your work.

## When to trigger

- Specifying identification, sampling, case selection, or measurement
- A reviewer questioned spatial autocorrelation, scale/MAUP, edge effects, validation, or a confound
- Justifying why the design adjudicates the rival account from `aaag-literature-positioning`

## Spatial / quantitative analysis & GIScience
- **Take space seriously.** Test and model **spatial dependence** (Moran's I, spatial lag/error,
  GWR/MGWR where heterogeneity is the point); state how the **MAUP / scale** could change conclusions.
- **Geography of the data.** Document projection/CRS, areal units, edge effects, and the support of
  measurements; spatial sampling and its biases.
- **Inference.** Cluster or use spatial SEs at the right level; for spatial autocorrelation, report
  diagnostics; for prediction, use spatially-aware cross-validation (blocked/spatial CV), not random folds.

## Remote sensing / physical-environmental
- **Measurement validity.** Sensor/resolution choices, atmospheric/geometric correction, and ground
  truth; quantify accuracy (confusion matrix, kappa/F1, RMSE) with an independent validation sample.
- **Process linkage.** Tie observed pattern to an earth-surface process and its scale; state the
  uncertainty budget end to end.

## Qualitative / human-geography
- **Case selection** by design logic (typical, extreme, paired, regional contrast) — say what the case
  is a *case of*. Convenience is not a rationale.
- **Positionality, reflexivity, and rigor** appropriate to the method (ethnography, interviews,
  archives, discourse/textual analysis); state how interpretations were checked.
- **Source/field transparency**: plan how fieldnotes, interviews, and archives are documented and cited
  (see `aaag-transparency-and-data`), including consent and geoprivacy.

## Nature-society / mixed methods
- **Integrate, don't staple.** Specify how the biophysical and social strands inform one another
  (e.g., land-change observation + livelihood interviews), and how convergence/divergence is handled.

## The adjudication test (Annals-specific)

For the **single strongest rival explanation**, write: *"If the rival held rather than my argument, the
[spatial pattern / measurements / accounts] would look like ___; instead they look like ___."* If the
design cannot distinguish them — including ruling out a **scale or spatial-autocorrelation artifact** —
it does not yet identify the contribution.

## Referee pushback → Annals-specific fix

| Likely objection | Area | The fix |
|------------------|------|---------|
| "Your OLS ignores spatial autocorrelation." | Methods/Human | Test residual Moran's I; move to a spatial model and report diagnostics. |
| "This is a unit-of-analysis artifact (MAUP)." | Methods/Nature-Society | Re-run across areal units/bandwidths; show stability or scope the claim by scale. |
| "Random CV overstates accuracy on spatial data." | Methods/RS | Use blocked/spatial CV; report the spatial structure of error. |
| "No independent validation of the classification." | RS/Physical | Add a held-out reference sample + area-adjusted accuracy. |
| "Convenience case; what is it a case *of*?" | Human/Nature-Society | State the case-selection logic and the population it represents. |
| "Whose voice / positionality?" | Human | Make reflexivity and interpretation-checking explicit. |

## Calibration anchors

- **Space is a design issue, not a covariate.** Dependence, scale, projection, and sampling are decided
  in the design, not patched in robustness.
- **Each tradition on its own terms.** A qualitative design is not weaker for lacking an estimand; it
  needs case logic, reflexivity, and disconfirmation criteria instead.
- **Mixed means integrated.** Two parallel analyses are not mixed methods; specify the linkage.

## Anti-patterns

- Ignoring spatial autocorrelation, then reporting OLS SEs as if observations were independent
- No MAUP/scale sensitivity when the result could be a unit-of-analysis artifact
- Classification/prediction with no independent validation, or random CV on spatial data
- Convenience case selection dressed up as theory-driven; positionality omitted in interpretive work
- A nature-society design that never actually links the two strands

## Output format

```
【Mode】spatial-quant / remote-sensing-physical / qualitative / mixed
【Estimand or claim】what is identified/shown
【Spatial integrity】dependence / MAUP-scale / projection / validation handled? [Y/N]
【Rival ruled out】the adjudication sentence (incl. scale/spatial-artifact)
【Robustness】planned checks
【Next】aaag-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — spatial-analysis, GIS, remote-sensing, and CAQDAS tooling by area
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — areas, scope, and review model
