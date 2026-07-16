---
name: molcell-figures
description: Use to finalize Molecular Cell display items — column-width sizing, minimum fonts, RGB, show-the-data with defined error bars/n/replicate type, gel/blot and structural-figure integrity, colorblind-safe palettes, multi-panel discipline, and stand-alone legends built for a mechanism proof.
---

# Display Items (molcell-figures)

## When to trigger

- Figures will not render legibly at Cell Press print widths.
- Bar charts hide the data (no points, no n, no defined error bars) behind a mechanistic claim.
- Gels/blots are cropped without disclosure; structural figures over-render the model.
- Color is the sole encoding, or rainbow/jet maps are used for continuous data.

## Sizing for Cell Press columns

Design figures to render at final print width without rescaling text:

- **1 column** ≈ **85 mm** wide
- **1.5 column** ≈ **114 mm** wide
- **2 columns (full width)** ≈ **174 mm** wide
- **Minimum font** in the final figure: **~6–7 pt** sans-serif (Helvetica/Arial), legible after reduction.
- **RGB** color mode (Cell Press is online-first); line weights heavy enough to survive reduction.

> Confirm exact widths, resolution, and file formats against the current Cell Press figure/digital-image guidelines.

## Show the mechanism's data, not just a summary

- Replace bar-of-means with **dot plots / box+points / violins+points**, especially for small n.
- State **n** and **what n is** in every legend: independent biological replicates? technical replicates? molecules? cells?
- **Error bars must be defined** (SD vs SEM vs 95% CI) — never undefined — and the **replicate type** stated.
- For a mechanistic claim, pair the quantification with the **primary data** (the gel, the trace, the density map) in the same or an adjacent panel.

## Molecular-biology figure integrity (non-negotiable)

- **Gels/blots**: show representative full lanes; disclose any splicing with a clear dividing line; present **uncropped key blots** in Supplemental; keep unprocessed scans.
- **Quantitative comparisons** must come from the **same** gel/exposure/experiment.
- **Structures (cryo-EM/X-ray)**: report resolution, map-to-model fit, and the region actually resolved; do not draw side chains or interactions the density does not support. Include a validation/FSC or Ramachandran summary per Cell Press/PDB norms.
- **Genomics tracks (ChIP/RNA/ATAC-seq)**: state normalization, show replicates or a replicate-correlation metric, and give the genomic scale.
- **Single-molecule / kinetics**: show example traces and the distribution, not only a fitted rate.

## Color and accessibility

- Use a **colorblind-safe palette**; avoid red/green as the only contrast (common in merge micrographs).
- Do not encode meaning by color alone — add shape/pattern/labels.
- No rainbow/jet colormaps for continuous data — use perceptually uniform maps (viridis, etc.); for structures, use consistent domain/chain coloring.
- Check the figure in grayscale.

## Multi-panel discipline

- Group panels by the **mechanistic step** they prove; one message per figure.
- Consistent axis scales across comparable panels; align structure orientations across panels.
- Label panels A, B, C…; the legend title states the figure's mechanistic claim.
- Move orthogonal-confirmation panels to Supplemental rather than shrinking fonts.

## Figure legend structure (stand-alone)

Each legend: a short **title sentence** (the mechanistic claim), then **per-panel** descriptions (A, B, C…), then **statistics** (test, exact n, replicate type, error-bar definition, P values or exact values), plus any structure/genomics metadata (resolution, normalization). The figure + legend must be interpretable without the main text; cross-reference STAR Methods where relevant.

## What a Molecular Cell referee checks in figures

Referees interrogate the *proof* of mechanism, so they read figures for evidence sufficiency. Common figure-driven major-revision triggers: a mechanistic claim resting on one assay with no orthogonal confirmation; a point-mutant panel missing the wild-type-rescue control; a structure figure asserting an interaction the density cannot resolve; bar-of-means hiding n = 3 with wide spread; genomics tracks with no replicate metric; error bars whose definition or n is missing; and any blot spliced without a disclosed boundary. Pre-empt each: pair every key claim with a second method, show the points and the primary data, and keep uncropped scans and half-maps ready — Molecular Cell may request them.

## Output format

```
【Item count】 N (standard Article ≤ ~7 main) → ok / over → move to Supplemental
【Sizing】 designed at 85 / 114 / 174 mm? fonts ≥6–7 pt? RGB? yes/no
【Data shown】 points + n + replicate type + defined error bars + primary data? yes/no
【Blot/structure/genomics integrity】 uncropped blots? resolution/fit stated? replicate metric? yes/no
【Colorblind-safe】 yes/no (palette used)
【Legends】 title + per-panel + stats, stand-alone? yes/no
【Fixes】 [...]
【Next】 molcell-star-methods
```

## Anti-patterns

- **Do not** paste raw Prism/ImageJ/instrument screenshots as figures.
- **Do not** use bars to hide a tiny, variable n — show the points.
- **Do not** draw structural contacts the density does not support.
- **Do not** crop or splice blots without a visible boundary and disclosure.
- **Do not** show a single genomics replicate as if it were the result.

> Confirm specs against the current Cell Press figure and digital-image guidelines.
