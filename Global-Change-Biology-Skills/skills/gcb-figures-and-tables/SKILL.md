---
name: gcb-figures-and-tables
description: Use when building figures, tables, and the mandatory graphical abstract for a Global Change Biology (GCB) manuscript. GCB rewards mechanism-first, self-contained, accessible exhibits and requires a graphical abstract depicting the driver-to-response link. Guides exhibit design; it does not invent data.
---

# Figures & Tables (gcb-figures-and-tables)

In GCB, exhibits carry the **mechanism**. The strongest papers show a clear **driver → biological
response** relationship in the main figures, with uncertainty visible. GCB also **requires a graphical
abstract** that depicts the mechanistic link (not a site map or phylogeny). Verify current figure specs
on the live guidelines page before submission.

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
   line art; live-check the current resolution and file-format specifications.

## Tables
- Report effect sizes with intervals and units; define every symbol and abbreviation in the caption.
- Keep tables for precise numbers; move relationships and patterns into figures.

## Exhibit-by-exhibit expectations

Different exhibit types carry different burdens at GCB. Use this as a per-panel design contract before
you finalize the figure set.

| Exhibit | Carries | Must show | Common reject note |
|---------|---------|-----------|--------------------|
| Graphical abstract | The driver → response link | A causal arrow from environmental driver to biological response | A site map or phylogeny standing in for mechanism |
| Flux / time-series panel | Trend and its uncertainty | Confidence ribbon and the sampling unit | A bare line with no spread |
| Map | Spatial pattern | Colour-blind-safe ramp, scale bar, projection | Rainbow ramp, no scale, undefined extent |
| Dose-response | Mechanism shape | Fitted curve with interval and the data | Curve drawn through points with no band |
| Forest plot (synthesis) | Pooled effect + heterogeneity | Per-study and pooled effect with CIs | Pooled diamond only, studies hidden |

## Worked micro-example (illustrative)

A remote-sensing study of carbon flux wants one mechanistic main figure. A site map of the eddy-covariance
towers is supporting material, not the lead. The lead panel plots gross primary productivity against
growing-season temperature with a fitted ribbon: GPP rises then saturates near an illustrative 22 C, with
the ensemble spread shaded. The caption states n = 18 site-years (illustrative), the statistic, the units
(g C m^-2 d^-1), and reads alone. The graphical abstract distils this to a single arrow: warming →
productivity saturation → weakening land carbon sink. Numbers illustrative.

## Reviewer pushback on exhibits and the fix

- "Figure 1 is a map; where is the mechanism?" → promote the driver-response panel to lead; demote the
  map to supporting information.
- "Point estimates only" → add ribbons, error bars, or ensemble spread so uncertainty is visible.
- "Unreadable in grayscale / rainbow map" → switch to `viridis` or Okabe-Ito and verify grayscale
  legibility.
- "Caption not self-contained" → add n, units, statistic, and scale so the exhibit stands without the
  methods.

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
