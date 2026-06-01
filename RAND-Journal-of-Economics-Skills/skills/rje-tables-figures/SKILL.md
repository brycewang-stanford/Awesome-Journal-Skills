---
name: rje-tables-figures
description: Use to design tables and figures for a RAND Journal of Economics (RJE) industrial-organization manuscript — parameter, elasticity, markup, merger-simulation, and counterfactual-welfare exhibits — formatted under the RJE Style Guide (numbered sections, unnumbered subsections, flush-right equations) and disciplined by the hard page caps. Exhibit design, not estimation.
---

# Tables & Figures (rje-tables-figures)

## When to trigger

- Turning IO estimates into the article's main exhibits
- Deciding which tables stay in the 40-page main text and which go to the appendix
- Formatting exhibits and equations to the RJE Style Guide

## What RJE exhibits carry

As the **industrial-organization flagship**, RJE expects exhibits that communicate **market behavior and welfare**, not just regression output:

- **Demand / cost parameter tables** with standard errors and the estimation method noted.
- **Elasticity matrices** (own/cross-price) demonstrating sensible substitution.
- **Markup / marginal-cost tables** tying estimates to conduct.
- **Merger-simulation and counterfactual tables** reporting price, output, and **welfare (consumer/producer surplus)** changes, with the maintained assumptions stated in the note.
- **Reduced-form work:** clean event-study plots (leads and lags, confidence bands) and treatment-effect tables.

Each exhibit should be **self-contained**: a reader sees the market, the specification, the units, and the assumption set from the note alone.

## RJE Style Guide formatting

- **Sections numbered consecutively; subsections unnumbered** — match table/figure callouts to that scheme.
- **Equations numbered flush right**, with **(1a)/(1b)** for multi-part equations.
- Author-date references in notes (no page numbers, no issue numbers).
- Vector output (PDF/EPS) for print; keep figures legible in greyscale; avoid chartjunk.

## Page-cap discipline (hard)

Main text **<=40 pp**, total **<=50 pp**, double-spaced. Exhibits eat pages fast:

- Keep in the main text the **decisive** exhibits: headline estimates, the key elasticity/markup table, and the central counterfactual/welfare result.
- Move full parameter dumps, alternative specifications, and robustness exhibits to the **appendix** (within the <=10-page appendix+references budget).
- Do not offload core exhibits into supporting information, which RJE discourages and may decline.

## Anti-patterns

- A wall of parameter tables in the main text blowing the 40-page cap
- Counterfactual/welfare tables with no maintained-assumption note
- Elasticity matrices that imply implausible substitution, unexplained
- Numbered subsections or inline equation numbers (off RJE style)
- Low-resolution raster figures illegible in print/greyscale

## Output format

```
【Main-text exhibits】[headline estimates, key elasticity/markup, central counterfactual]
【Appendix exhibits】[full params, robustness, alt specs]
【Self-contained notes】units + specification + assumptions? [Y/N]
【Style】sections numbered/subsections not; eqns flush-right (1a)/(1b)? [Y/N]
【Page budget】main __/40, total __/50 — within cap? [Y/N]
【Next step】rje-writing-style
```
