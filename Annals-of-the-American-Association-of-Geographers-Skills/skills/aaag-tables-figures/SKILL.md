---
name: aaag-tables-figures
description: Use when building maps, figures, and tables for an Annals of the American Association of Geographers manuscript. The Annals has a dedicated Cartography Editor and Graphics Guidelines; maps are held to cartographic standards, not just plotted. Improves exhibits; it does not run the analysis.
---

# Maps, Figures & Tables (aaag-tables-figures)

The Annals is a geography journal: **maps are arguments**, and the journal holds them to cartographic
standards. There is a **Cartography Editor** and **Graphics Guidelines** (检索于 2026-06；以官网为准),
and every exhibit counts toward the **11,000-word cap** (figure captions are included). Make each
exhibit carry its weight and read correctly in print and grayscale.

## When to trigger

- Designing or revising maps, remote-sensing figures, model plots, or tables
- A reviewer/editor flagged a map's projection, classification, legend, or legibility
- Trimming exhibits to fit the inclusive word cap

## Cartographic essentials (maps are held to standard here)

- **Projection chosen on purpose** — appropriate to area/distance/shape for the analysis; name it.
- **Classification stated** — method (quantiles, equal-interval, natural breaks) and class count, with
  a rationale; the choropleth message must not be an artifact of the break scheme.
- **Map elements present** — scale bar, north arrow where needed, legend, data source, and date; graticule/inset where it aids reading.
- **Normalize areal data** — rates/densities, not raw counts, on choropleths; avoid MAUP-driven artifacts.
- **Accessible color** — colorblind-safe, sequential/diverging schemes matched to the data type;
  legible in grayscale; sufficient figure-ground contrast.

## Remote-sensing & physical figures

- State band combination/stretch; include a **spatial error/uncertainty** panel where accuracy matters.
- Give coordinates/extent and resolution so the figure is reproducible and locatable.

## Model & statistical figures

- Prefer effect/marginal-effect, GWR-surface, and event/trend plots over dense tables; show uncertainty
  bands. Tables carry effect sizes and CIs, not stars alone.

## Self-containment & house style

- Every exhibit is **readable standalone**: caption states what, where, when, source, and the takeaway.
- Follow the **Graphics Guidelines** for resolution, fonts, and file format; vector for line art,
  high-resolution raster for imagery (verify current specs on the page).
- Count captions, tables, and figures toward the **11,000-word cap** — budget exhibits deliberately.

## Common map failure → fix (what the Cartography Editor flags)

| Failure | Why it misleads | Fix |
|---------|-----------------|-----|
| Raw counts on a choropleth | bigger/more-populous units always look "high" | map rates/densities; normalize |
| Default Web Mercator for area analysis | distorts area at high latitudes | choose an equal-area projection; name it |
| Auto "natural breaks" with no rationale | the message is an artifact of the break scheme | justify method + class count; test alternatives |
| Rainbow palette | not colorblind-safe; false ordering | sequential/diverging colorblind-safe scheme |
| No scale bar / source / date | unverifiable, not reproducible | add required map elements |
| Tiny multiples illegible in print | reviewer cannot read the result | resize, simplify, or split exhibits |

## Checklist

- [ ] Projection named and appropriate to the analysis
- [ ] Classification method + class count stated and justified
- [ ] Scale bar / legend / source / date present; areal data normalized
- [ ] Colorblind-safe and grayscale-legible; adequate contrast
- [ ] RS figures: band/stretch + accuracy/error panel; extent + resolution given
- [ ] Captions self-contained; exhibit budget fits the inclusive word cap
- [ ] Graphics meet the journal's resolution/format specs (verify)

## Anti-patterns

- Default-software projection and auto-classification with no rationale (artifactual choropleth)
- Raw counts on a choropleth instead of rates/densities
- Rainbow / non-colorblind-safe palettes; maps illegible in grayscale
- Missing scale bar, legend, or data source/date
- Overrunning the word cap because captions and tables were not counted

## Output format

```
【Exhibit】map / RS figure / model plot / table
【Cartography】projection + classification + required elements? [Y/N]
【Accessibility】colorblind-safe + grayscale-legible? [Y/N]
【Self-contained】caption states what/where/when/source/takeaway? [Y/N]
【Word-cap budget】exhibits + captions counted? [Y/N]
【Next】aaag-writing-style
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — GIS/cartography and figure tooling (QGIS, ggplot2/tmap, matplotlib)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Graphics Guidelines and Cartography Editor
