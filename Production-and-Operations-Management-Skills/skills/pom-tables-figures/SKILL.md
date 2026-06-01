---
name: pom-tables-figures
description: Use when designing the exhibits for a Production and Operations Management (POM) manuscript — result tables, comparative-statics and sensitivity plots, model schematics, empirical tables, simulation plots — and deciding what stays in the 32-page main paper vs. the online e-companion. Designs exhibits; it does not run the analysis (pom-data-analysis).
---

# Tables & Figures (pom-tables-figures)

## When to trigger

- Exhibits are cluttered, off house style, or not self-explanatory
- You are over the 32-page cap and must decide what moves to the e-companion
- A reviewer cannot follow the contribution from the table/figure sequence

## The POM exhibit budget: main paper vs. e-companion

POM's **32-page** limit *counts* tables, figures, appendices, and references (1.5 spacing, 11-pt). Treat exhibits as a scarce budget: only the displays that carry the core operational insight belong in the main paper; full proofs, large parameter grids, extended robustness, and supplementary tables go to the **unlimited online e-companion**. Number e-companion exhibits distinctly (e.g., EC.1, Table EC.2) and cross-reference them stably from the main text.

## Match the exhibit to the method track

- **Analytical/modeling:** a model schematic (decision timeline, information structure); a comparative-statics or sensitivity figure showing how the optimal policy moves with cost, lead time, or competition; a table of structural results. Lead with the *managerial* reading of the curve, not just its monotonicity.
- **Empirical OM:** a descriptive/summary table; the main results table with effect sizes and standard errors; robustness columns. Put units in decision-relevant terms (cost, fill rate, days).
- **Behavioral OM:** treatment-by-condition means with error bars; manipulation-check evidence.
- **Operations data science:** validation/performance tables plus a figure showing the **operational gain** (e.g., cost or service improvement from predict-then-optimize), not just accuracy.
- **Simulation:** plots with confidence intervals across sensitivity ranges.

## Make every exhibit decision-legible

- Title and note each exhibit with its **decision implication**, not only the statistical or mathematical object.
- State operational units explicitly.
- Ensure a Department Editor can grasp the contribution from the first one or two exhibits.
- Avoid duplicating main-paper content in appendices or the e-companion.

## Checklist

- [ ] Core insight exhibits in the main paper; depth in the e-companion
- [ ] Exhibits counted against the 32-page budget
- [ ] Operational units and decision implications labeled
- [ ] E-companion exhibits numbered (EC.*) and cross-referenced stably
- [ ] No duplication between main paper, appendix, and e-companion

## Output format

```
【Exhibit】table / figure / schematic / appendix item
【Purpose】mechanism / result / robustness / implication / method detail
【Placement】main paper / e-companion (EC.*)
【Problem】readability / page budget / missing units
【Revision】specific design change
【Next step】pom-writing-style
```
