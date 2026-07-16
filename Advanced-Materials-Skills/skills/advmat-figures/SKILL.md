---
name: advmat-figures
description: Use when designing or auditing figures for an Advanced Materials manuscript, including the lead figure, multi-panel characterization figures, and the Table-of-Contents graphic, where visual quality is a house expectation. Designs figure strategy; does not run the analysis or write prose.
---

# Advanced Materials Figures (advmat-figures)

## When to trigger

- You have many candidate panels and need a coherent figure set
- Your lead figure does not convey the central advance at a glance
- Characterization panels are crowded, mislabeled, or unreadable at column width
- You have no Table-of-Contents (TOC) graphic, or it is an afterthought
- A coauthor wants to "add one more panel just in case"

## Figure strategy for Adv. Mater.

Advanced Materials is a **visually demanding** journal — striking, cover-quality figures are a house expectation, and the journal actively selects work for cover art. But visual polish must serve the science. The hierarchy:

- **Lead figure (Figure 1)** — usually a schematic of the material/design concept plus the single most decisive piece of evidence. A reader skimming should grasp the advance from this figure and its caption alone.
- **Characterization figures** — each closes one link of the structure → property → function chain (e.g. one figure for structure by XRD/TEM, one for the property, one for the device + benchmarking).
- **The TOC graphic** — a small, self-explaining image plus a short blurb that sells the advance to a browsing reader; treat it as a designed object, not a cropped panel.
- **Everything else** — optimization sweeps, extra samples, raw traces → Supporting Information.

If a panel does not advance the central claim or one essential link, move it to the SI.

## Multi-panel characterization figures

Materials figures are dense by nature; discipline keeps them readable:

| Principle                      | Practice                                                         |
|--------------------------------|-----------------------------------------------------------------|
| One figure, one link           | Group panels that jointly prove one claim (e.g. all structure)  |
| Reading order                  | Label (a),(b),(c) top-left to bottom-right; caption follows it  |
| Scale bars, always             | Every micrograph carries a scale bar in the image, not only the caption |
| Consistent color-coding        | The same sample/condition keeps one color across all figures    |
| Annotate the feature           | Arrow/label the lattice fringe, peak, or interface that matters |
| Overlay, don't scatter         | Show theory-vs-experiment or before-vs-after on shared axes      |

## Production standards (Wiley format)

- Design for the journal's two-column layout; check legibility at final printed width.
- Fonts, axis labels, and tick numbers legible at print size; keep a consistent typeface across figures.
- Vector formats for line art/schematics; high-resolution raster (meeting Wiley's DPI requirement) for micrographs — verify the current DPI/format spec.
- Color is free in Adv. Mater. (online and print), but keep palettes color-blind-safe and distinguishable in grayscale; never encode by color alone.
- Define every symbol, abbreviation, and unit in the caption; give micrographs their scale and technique.
- Match nomenclature and units to the main text; use SI units and consistent significant figures.

## The TOC graphic and cover art

- The TOC entry (graphic + short text) is a required, high-visibility asset — design it to communicate the advance to a non-specialist in one glance.
- If aiming for cover consideration, prepare a separate high-resolution cover image; do not repurpose a cramped data panel. Verify current cover-submission format and dimensions.

## Checklist

- [ ] Figure 1 conveys the central advance (concept + decisive evidence) at a glance
- [ ] Each figure closes exactly one link of the structure → property → function chain
- [ ] Every micrograph has an in-image scale bar and names its technique
- [ ] Sample/condition color-coding is consistent across all figures
- [ ] Legible at two-column print width; consistent fonts and units
- [ ] Color-blind-safe and grayscale-distinguishable; not color-dependent
- [ ] A designed TOC graphic + blurb exists and sells the advance
- [ ] Non-essential panels/datasets moved to the SI

## Anti-patterns

- A lead figure too dense to parse without the main text
- Micrographs with no scale bar, or scale bars only mentioned in the caption
- Ten-panel megafigures that bury the takeaway
- Inconsistent color-coding of the same sample across figures
- Color-only encoding that fails in grayscale or for color-blind readers
- A TOC graphic that is a cropped, unreadable data panel

## Output format

```
【Figure count】N — each essential?  yes / cut list
【Fig. 1 conveys the advance at a glance】yes / redesign
【Per-figure single chain-link】list
【Scale bars on all micrographs】yes / fix
【Consistent color-coding】yes / fix
【Color-blind / grayscale safe】yes / fix
【TOC graphic】designed + blurb?  yes / fix
【Next】advmat-supplementary (SI) or advmat-length-management (fit format)
```

> Figure DPI, format, TOC-graphic, and cover-art specifications are set by Wiley and change — verify current requirements on the official Advanced Materials author page.
