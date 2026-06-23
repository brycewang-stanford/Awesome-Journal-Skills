---
name: pnasnexus-figures
description: Use to finalize PNAS Nexus display items — count figures and tables against the graphical-element budget, size to journal column widths, set legible fonts, show-the-data with n and defined error bars, scale bars, colorblind-safe palettes, legend structure, and image integrity (raw, unprocessed images must be retained). Enforces figure rigor before submission.
---

# Display Items (pnasnexus-figures)

## When to trigger

- Figures and tables push the page / graphical-element budget (`pnasnexus-writing`).
- Fonts are unreadable at print size, or colors are not colorblind-safe.
- Bar charts hide the underlying data (no points, no n).
- Panels are screenshots of software output pasted into the figure.
- You are unsure how figures count against the length limit.

## Figures count toward the page budget

PNAS Nexus measures length in **pages**, and **figures and tables are part of that budget**: a standard 6-page Research Report is described as roughly **4,000 words, 50 references, and 4 medium-size graphical elements**. So every figure/table competes with text for space.

- Treat **~4 medium display items** as the working target for a 6-page Research Report; more is possible up to the 12-page max, but each item costs page budget.
- Move secondary/supporting figures and tables to **Supporting Information** rather than inflating the main text.
- Confirm exact figure-count and sizing rules in the current PNAS Nexus author/digital-art guidelines.

## Sizing and legibility

Design each figure to render at the journal's print column widths **without rescaling text** (PNAS Nexus is a multi-column OUP journal; confirm the exact widths — they are commonly on the order of a single column ≈ 9 cm, 1.5 column ≈ 11–12 cm, and full width ≈ 18 cm).

- Minimum font in the final figure: legible after reduction to print size (sans-serif, e.g., Helvetica/Arial; aim for ~6–8 pt at final size — confirm).
- Line weights heavy enough to survive printing (avoid hairlines).
- Submit at the required resolution (line art high-dpi; halftones/photos at the specified dpi) — confirm specs.

## Show the data, not just the summary

- Replace bar-of-means with **dot plots / box+points / violins+points** wherever n is small.
- Always state **n** in the legend, and **what n is** (cells? animals? subjects? independent experiments?).
- Error bars must be **defined** in the legend (SD vs SEM vs 95% CI) — never undefined.
- For images (blots, micrographs): include **scale bars**.

## Color and accessibility (an open-access advantage)

- Because PNAS Nexus is fully online and open access, **color figures display freely** — use color where it aids understanding (confirm there are no separate color charges).
- Use a **colorblind-safe palette** (avoid red/green as the only contrast); don't encode meaning by color alone — add shape/pattern/labels.
- No rainbow/jet colormaps for continuous data — use perceptually uniform maps (viridis, etc.).
- Check that figures remain interpretable in grayscale for readers who print.

## Figure legend structure

Each legend: a short **title sentence** (the claim of the figure), then per-panel descriptions (A, B, C…), then statistics (test, n, error-bar definition, exact P or values). The legend should let the figure stand alone. Remember legends count toward the page budget — keep them tight.

## Integrity rules (non-negotiable — and tied to the data policy)

- No selective deletion, splicing, or beautification of gels/blots/images without a labeled boundary; disclose any grouping.
- Quantitative comparisons must come from the **same** experiment/exposure.
- **Retain raw, unprocessed images and source data.** PNAS Nexus requires that *"all data and any direct outputs from imaging systems must be retained in their raw, unprocessed versions"* — editors/reviewers can request them, and failure to provide data can be grounds for rejection or retraction (`pnasnexus-data`).

## Output format

```
【Item count】 figures + tables vs graphical-element budget (~4 for a 6-pp Research Report; confirm) → ok / over
【Sizing】 designed at journal column widths? fonts legible at print size? yes/no
【Data shown】 points + n + defined error bars? yes/no
【Color】 used freely (OA)? colorblind-safe? grayscale-readable? yes/no
【Integrity】 scale bars / disclosed splices / raw unprocessed images retained? yes/no
【Main vs SI】 secondary items moved to SI? 
【Fixes】 [...]
【Next】 pnasnexus-statistics
```

## Anti-patterns

- **Do not** paste raw Stata/Prism/ImageJ screenshots as figures.
- **Do not** use bars to hide n=3 with huge spread — show the points.
- **Do not** leave error bars undefined or mix SD and SEM across panels.
- **Do not** discard raw image files — the data policy requires retaining them.
- **Do not** inflate the main text with secondary figures — move them to SI.
