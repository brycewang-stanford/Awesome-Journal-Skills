---
name: jue-tables-figures
description: Use when the exhibits of a Journal of Urban Economics (JUE) manuscript must make the spatial pattern visible — maps, event-study plots, RD/boundary figures, and clean regression tables. Designs the spatial exhibits a JUE referee expects; it does not run the analysis (jue-robustness) or write the prose (jue-writing-style).
---

# Spatial Exhibits: Maps, Tables & Figures (jue-tables-figures)

## When to trigger

- The paper has a spatial result but **no map** — the reader cannot see where the variation is
- A boundary/RD or event-study design is in tables only; the figure that would convince is missing
- Tables are dense with controls and the headline coefficient is hard to find
- The geography of treatment vs control is described in words, not shown
- Reviewers cannot tell whether the spatial pattern is real or an artifact of the units chosen

## Maps earn their place — but only when they carry information

JUE is one of the few economics journals where a **map is often the central exhibit**, because the identifying variation is geographic. But a map must do econometric work, not decorate:

- **Show the identifying variation, not just the data.** Map the treatment boundary, the corridor, the discontinuity, the shift-share exposure — the thing your design exploits — so the reader sees what generates the estimate.
- **Make scale and units explicit.** State the spatial unit (tract, block, grid cell), include a scale bar and north arrow, and pick a classification (quantile vs equal-interval) that does not manufacture a pattern.
- **Pair the map with the design figure.** A boundary map plus an RD plot; a treatment map plus an event-study; an exposure map plus the first stage.

## Exhibit-by-design checklist

| Design | The figure that convinces | The table that supports it |
|--------|---------------------------|----------------------------|
| Boundary / spatial RD | RD plot in distance-to-boundary with binned means + local-linear fit; covariate-smoothness panel | RD estimates across bandwidths; density test |
| Place-based DiD / event study | event-study plot with leads/lags and CIs; treatment-geography map | heterogeneity-robust ATT vs TWFE; Bacon decomposition |
| Shift-share / Bartik | map of exposure; first-stage scatter | Rotemberg-weight / BHJ diagnostics; second stage |
| Capitalization / housing | map of price gradient or treatment area | hedonic estimates; spatial-SE comparison |
| QSM counterfactual | map of the counterfactual spatial reallocation | parameter table with identification source; sensitivity |

## Table craft for JUE

1. **Headline coefficient first**, controls collapsed to "Yes/No" rows — the reader should find the estimate in two seconds.
2. **Report spatial standard errors** (Conley / spatial cluster) alongside or instead of naive; note the distance cutoff in the table notes.
3. **Self-contained notes:** sample, geography, FE level, clustering, units. A JUE table should be readable without the text.
4. **House style:** follow the journal's significance-reporting convention (检索于 2026-06；以官网为准); always show standard errors, and prefer reporting the magnitude in interpretable units (% capitalization, elasticity).
5. **Figures legible in grayscale** for print; do not encode the only signal in color.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JUE is urban/spatial economics — sorting and spatial dependence; identification + Conley/spatial-robust inference.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] A map shows the *identifying variation* (boundary / corridor / exposure), not just raw data
- [ ] Map has spatial unit stated, scale bar, north arrow, and a non-misleading classification
- [ ] The design's convincing figure (RD plot / event-study / first-stage) is present
- [ ] Headline coefficient is immediately findable; controls collapsed to indicator rows
- [ ] Spatial SEs reported with the distance cutoff noted
- [ ] Table notes are self-contained (sample, geography, FE, clustering, units)
- [ ] Figures remain legible in grayscale

## Anti-patterns

- A spatial paper with no map, or a map that shows the data but not the identifying variation
- A map whose classification (bins/colors) manufactures a visual pattern the estimate does not support
- Burying the headline coefficient under fifteen control rows
- Naive standard errors in the table for geographically clustered data
- An event-study or RD reported only as a table when the figure is the convincing object
- Color-only encoding that disappears in print or for color-blind readers

## Common map mistakes that draw referee fire

- **Classification gaming.** Quantile bins on a skewed variable can manufacture a stark gradient; show the result is not an artifact of the binning, and prefer a classification the reader can interpret.
- **The wrong unit.** Mapping at a coarse unit (county) when the identification is at a fine unit (tract/parcel) hides the variation that does the work; map at the scale of the design.
- **Projection distortion.** An unstated or inappropriate CRS distorts distances and areas — fatal when the design is distance-based; state the projection.
- **Decorative maps.** A choropleth of the raw outcome with no treatment boundary or exposure overlay shows the data but not the identifying variation; every map should advance the argument.

## What belongs in the appendix vs the main text

JUE main text carries the map and the design figure that *convince*; the appendix carries the supporting battery. Put in the main text: the treatment-geography map, the RD/event-study/first-stage figure, the headline table. Push to the appendix: full robustness tables across scales and radii, covariate-balance batteries, alternative-classification maps, and the spatial-SE-cutoff grid. Do not let the appendix carry an exhibit the main claim depends on — the editor and first referee may not reach it.

## Worked vignette (illustrative)

A boundary-discontinuity paper on school-zone capitalization first presents only a regression table. The JUE exhibit upgrade: (1) a map of the attendance boundary with the price gradient, so the reader sees the discontinuity is geographic and not confounded by a highway; (2) an RD plot in distance-to-boundary with binned means and a local-linear fit, the visual that makes the jump credible; (3) a covariate-smoothness panel showing pre-determined characteristics do not jump; (4) a table with Conley SEs (1km cutoff) and the estimate in percent. The map + RD plot carry the paper.

## The one-figure test

Editors and referees often form an impression from a single exhibit. Ask: if a reader saw only *one* figure from your paper, which would it be, and does it convey both the geography and the result? For a boundary design it is the RD plot in distance-to-boundary; for a place-based policy it is the event-study with the treatment map inset; for an agglomeration paper it is the exposure map paired with the first-stage. Engineer that figure to be self-explanatory — labeled axes in interpretable units, the identifying variation visible, a caption that states the claim — because it is doing more persuasive work than any table. A paper whose single best figure is a generic choropleth has not yet found its convincing exhibit.

## Output format

```text
【Map】shows identifying variation? unit/scale-bar/classification ok? [Y/N]
【Design figure】RD plot / event-study / first-stage present? [Y/N]
【Headline table】coefficient findable; controls collapsed? [Y/N]
【Spatial SEs】Conley/spatial cluster in tables, cutoff noted? [Y/N]
【Notes】self-contained (sample/geography/FE/clustering/units)? [Y/N]
【Grayscale】figures legible without color? [Y/N]
【Next skill】jue-writing-style
```
