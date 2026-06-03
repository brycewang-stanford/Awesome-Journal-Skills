---
name: gcb-figures-and-tables
description: Use when building figures, tables, and the mandatory graphical abstract for a Global Change Biology (GCB) manuscript. GCB rewards mechanism-first, self-contained, accessible exhibits and requires a graphical abstract depicting the driver-to-response link. Guides exhibit design; it does not invent data.
---

# Figures & Tables (gcb-figures-and-tables)

In GCB, exhibits carry the **mechanism**. The strongest papers show a clear **driver → biological
response** relationship in the main figures, with uncertainty visible. GCB also **requires a graphical
abstract** that depicts the mechanistic link (not a site map or phylogeny). Verify current figure specs
on the live guidelines page (see 待核实 in the source map).

## When to trigger

- Designing the main-figure sequence to tell the mechanistic story
- Building the **graphical abstract**
- Preparing maps, flux/time-series, dose-response, or forest plots
- Checking accessibility, resolution, and self-containment before submission

## What GCB rewards

1. **Mechanism-first main figures.** Lead with the driver-response relationship; relegate site maps and
   descriptive context to supporting figures unless they carry the argument.
2. **Visible uncertainty.** Confidence/credible ribbons, error bars, ensemble spread — uncertainty is
   part of the result, not optional decoration.
3. **A strong graphical abstract.** One concise figure linking an environmental **driver** to a
   biological **response**; it is the reader's first impression.
4. **Self-contained exhibits.** Each figure/table readable from its caption alone (units, n, sample,
   statistic, scale).
5. **Accessibility.** Colour-blind-safe palettes (`viridis`, Okabe-Ito), legible in grayscale; vector
   line art; adequate resolution (one rendering: 300 dpi colour / 600 dpi line art — 待核实).

## Tables
- Report effect sizes with intervals and units; define every symbol and abbreviation in the caption.
- Keep tables for precise numbers; move relationships and patterns into figures.

## Anti-patterns

- A graphical abstract that is a study-site map or phylogeny instead of the driver-response mechanism
- Main figures that describe the site rather than show the mechanism
- Plots with no uncertainty (point estimates only)
- Rainbow/jet colour maps; figures unreadable in grayscale or by colour-blind readers
- Captions that require the methods section to interpret the figure

## Output format

```
【Graphical abstract】shows driver → response mechanism? [Y/N]
【Main-figure story】mechanism-first sequence? [Y/N]
【Uncertainty shown】ribbons / bars / ensemble spread? [Y/N]
【Self-contained】each caption stands alone (units, n, stat)? [Y/N]
【Accessible】colour-blind-safe + grayscale-legible + resolution? [Y/N]
【Next】gcb-reporting-and-data-policy
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — plotting/mapping packages and palette tools
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — graphical-abstract requirement and figure specs
