---
name: cell-figures
description: Use to finalize Cell Press display items — column-width sizing, minimum fonts, RGB, show-the-data with defined error bars/n/replicate type, scale bars, colorblind-safe palettes, multi-panel discipline, stand-alone legends, and image integrity.
---

# Display Items (cell-figures)

## When to trigger

- Figures will not render legibly at Cell Press print widths.
- Bar charts hide the underlying data (no points, no n, no defined error bars).
- Panels are raw software screenshots; blots are cropped without disclosure.
- Color is the sole encoding, or rainbow/jet maps are used for continuous data.

## Sizing for Cell Press columns

Design figures to render at final print width without rescaling text:

- **1 column** ≈ **85 mm** wide
- **1.5 column** ≈ **114 mm** wide
- **2 columns (full width)** ≈ **174 mm** wide
- **Minimum font** in the final figure: **~6–7 pt** (sans-serif, e.g., Helvetica/Arial), legible after reduction.
- **RGB** color mode (Cell is online-first); line weights heavy enough to survive reduction.

> Confirm exact widths, resolution, and file formats against the current Cell Press figure/digital-image guidelines.

## Show the data, not just the summary

- Replace bar-of-means with **dot plots / box+points / violins+points**, especially for small n.
- State **n** and **what n is** in every legend: cells? animals? independent biological replicates? technical replicates?
- **Error bars must be defined** (SD vs SEM vs 95% CI) — never undefined — and the **replicate type** stated.
- For images (blots, micrographs): show **scale bars**; present full, **uncropped** key blots in the supplement.

## Color and accessibility

- Use a **colorblind-safe palette**; avoid red/green as the only contrast.
- Do not encode meaning by color alone — add shape/pattern/labels.
- No rainbow/jet colormaps for continuous data — use perceptually uniform maps (viridis, etc.).
- Ensure adequate contrast; check the figure in grayscale.

## Multi-panel discipline

- Group panels by the **claim** they support; one message per figure.
- Consistent axis scales across comparable panels.
- Label panels A, B, C…; the legend title states the figure's message.
- Move overflow panels to Supplemental Information rather than shrinking fonts.

## Figure legend structure (stand-alone)

Each legend: a short **title sentence** (the claim of the figure), then **per-panel** descriptions (A, B, C…), then **statistics** (test used, exact n, replicate type, error-bar definition, P values or exact values). The figure + legend should be interpretable without the main text. Cross-reference related STAR Methods where relevant.

## Image integrity (non-negotiable)

- No inappropriate manipulation: no selective deletion, splicing, or beautification of gels/blots/images; disclose any grouping with a clear dividing line.
- Quantitative comparisons must come from the **same** experiment/exposure.
- Keep **unprocessed source images and source data** — Cell may request them.
- Follow the **Cell Press digital image guidelines** for adjustments (apply linearly to the whole image; no obscuring/eliminating features).

## Worked legend (stand-alone structure)

A Cell legend leads with the claim, walks the panels, then consolidates statistics — so the figure is readable without the Results text:

> **Figure 3. XYZ1 restrains stem-cell division by excluding ABC2 from the nucleus.**
> (A) Schematic of the organoid CRISPR screen. (B) Confocal images of ABC2 (green) in control vs. *Xyz1*-knockout crypts; scale bar, 20 µm. (C) Quantification of nuclear ABC2 signal. (D) Stem-pool size by lineage tracing.
> Data in (C) and (D) are mean ± SD; n = 6 independent biological replicates (organoid lines from separate mice) per condition. Statistical test: two-tailed Mann-Whitney U; exact P values shown. See STAR Methods, "Quantification and Statistical Analysis."

The title states the message, each panel is named, the scale bar lives in the panel it belongs to, and the stats block defines n, replicate type, error bar, and test in one place — then points to STAR Methods rather than re-deriving it.

## What a Cell referee checks in figures

Cell referees are asked to interrogate a *complete* story, so they read figures for evidence sufficiency, not decoration. Common figure-driven rejection or major-revision triggers: a mechanistic claim resting on a single assay with no orthogonal confirmation; bar-of-means hiding an n of 3 with wide spread; representative micrographs with no quantification across replicates; error bars whose definition or n is missing; and any blot that looks spliced without a disclosed boundary. Pre-empt each: pair every key claim with a second method in the same or an adjacent panel, show the points, and keep uncropped source images ready — Cell may request them during review.

## Graphical Abstract vs. main figures

The Graphical Abstract (see `cell-highlights`) is a single-panel *story* image, not a display item — do not carry a main-figure panel into it or vice versa. Keep the two consistent in color and iconography so a reader who scans the abstract recognizes the same scheme in the figures, but never let the Graphical Abstract stand in for a quantified figure.

## Output format

```
【Item count】 N (typical Cell Article ≤ ~7–8 main) → ok / over → move to Supplemental
【Sizing】 designed at 85 / 114 / 174 mm? fonts ≥6–7 pt? RGB? yes/no
【Data shown】 points + n + replicate type + defined error bars? yes/no
【Colorblind-safe】 yes/no (palette used)
【Integrity】 scale bars / uncropped blots in supplement / source data kept? yes/no
【Legends】 title + per-panel + stats, stand-alone? yes/no
【Fixes】 [...]
【Next】 cell-star-methods
```

## Anti-patterns

- **Do not** paste raw Prism/ImageJ/instrument screenshots as figures.
- **Do not** use bars to hide a tiny, variable n — show the points.
- **Do not** leave error bars undefined or omit what n represents.
- **Do not** crop or splice blots without a visible boundary and disclosure.
- **Do not** rely on red-vs-green as the sole encoding.

> Confirm specs against the current Cell Press figure and digital-image guidelines.
