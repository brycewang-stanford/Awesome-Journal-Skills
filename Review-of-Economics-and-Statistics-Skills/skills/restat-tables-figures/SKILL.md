---
name: restat-tables-figures
description: Use when building or revising the exhibits of a The Review of Economics and Statistics (REStat) manuscript so the main result is legible in one table or figure in AEA/REStat house style. Designs publication-grade exhibits; it does not run the underlying estimation.
---

# Tables & Figures (restat-tables-figures)

## When to trigger

- The main result is buried across several dense tables instead of one clear exhibit
- Tables lack self-contained notes (a reader must hunt the text for the spec)
- Figures are decorative rather than load-bearing, or omit uncertainty
- You are preparing exhibits for the online appendix vs the main paper

## The REStat exhibit bar

A REStat reader should grasp the **headline estimate from one main exhibit** — a table or, increasingly, an event-study / RD / coefficient-stability figure with a confidence band. REStat follows **standard economics house style**: significance **stars are permitted**, but **standard errors are expected in parentheses** and the exhibit must stand on its own. Every table and figure carries a **self-contained note** stating the sample, the specification, the unit of observation, the inference (clustering level), and what the reader should take away. The main paper is **self-contained**; supporting detail goes to the **online appendix (≤20 pages; source map refreshed 2026-06-20)**.

## Exhibit design rules

| Element | REStat-compliant practice |
|---------|---------------------------|
| Headline result | One main table or one figure a reader can read in 30 seconds |
| Standard errors | In parentheses below coefficients; clustering stated in the note |
| Significance | Stars allowed, but never *instead* of SEs; report the SE always |
| Notes | Self-contained: sample, spec, unit, N, inference, source |
| Figures | Load-bearing (event study with leads, RD plot, coefficient stability) with CIs/bands |
| Decimals | Consistent, sensible precision; no spurious digits |
| Appendix | Robustness and construction detail → online appendix (≤20 pp); main paper self-contained |
| Reproducibility | Every number traces to a script in the Harvard Dataverse package (`restat-replication-package`) |

## Which exhibit for which design

- **DID / event study:** an event-study plot with leads and lags and a confidence band is often the single most persuasive exhibit — flat pre-trends visible at a glance.
- **RD:** a binned scatter with the fitted polynomials and the discontinuity, plus the estimate table with bandwidth/robust CIs.
- **IV / shift-share:** a first-stage table or figure alongside the structural estimate; do not hide a weak first stage.
- **Measurement papers:** a validation figure (new measure vs benchmark) earns its place as a main exhibit.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). REStat is applied econometrics/empirical micro — the home of careful identification; DiD/IV/RDD with weak-IV-robust CIs.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] The headline estimate is legible from ONE main exhibit
- [ ] Standard errors in parentheses; clustering level stated in the note
- [ ] Stars (if used) accompany, never replace, standard errors
- [ ] Every table/figure note is self-contained (sample, spec, unit, N, inference, source)
- [ ] Figures are load-bearing and carry uncertainty (CIs / bands)
- [ ] Main paper self-contained; supporting exhibits moved to online appendix (≤20 pp)
- [ ] Every reported number is reproducible from the deposited code

## Anti-patterns

- A wall of coefficients with no single readable headline exhibit
- Stars with no standard errors (REStat expects the SE shown)
- Table notes that force the reader back into the text to learn the specification
- Decorative figures without confidence bands or a clear takeaway
- Overstuffed main paper that should have pushed detail to the online appendix
- Exhibit numbers that do not match what the deposited script regenerates

## Worked vignette: one figure carrying the paper (illustrative)

A staggered-DID paper had its main result spread over three tables: a TWFE column, a Callaway–Sant'Anna
column, and a robustness table. A REStat editor wanted to see the identification at a glance. The fix
collapsed the headline into a **single event-study figure** — event-time on the x-axis, the estimated effect
with a 95% confidence band on the y-axis, leads visibly flat and centered on zero, lags showing the dynamic
effect. The accompanying table kept only the pooled post estimate with its SE and clustering note. A reader
now sees parallel-trends support and the effect in one exhibit; the three old tables moved to the online
appendix. Self-contained note states sample, estimator, unit, N, and clustering — nothing to hunt for in the text.

## Output format

```
【Headline exhibit】Table/Figure [n]: [what it shows in one line]
【SE + inference】SEs in parentheses; clustering at [level]; stars: [used/not]
【Figure load-bearing?】[event-study / RD plot / validation / coef-stability] with CIs? [Y/N]
【Notes self-contained?】sample/spec/unit/N/inference/source present? [Y/N]
【Main vs appendix】main exhibits: [...]; online appendix (≤20pp): [...]
【Reproducible?】each number ← script in Dataverse package? [Y/N]
【Next step】restat-writing-style
```
