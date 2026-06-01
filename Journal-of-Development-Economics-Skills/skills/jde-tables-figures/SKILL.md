---
name: jde-tables-figures
description: Use when designing the main exhibits for a Journal of Development Economics (JDE) manuscript — figure-forward presentation of treatment effects, heterogeneity, and event studies for development settings, with self-contained notes. Shapes exhibits; it does not run the estimation.
---

# Tables & Figures (jde-tables-figures)

## When to trigger

- The main result is a nine-column table no reader can parse
- A treatment effect or pre-trend would land harder as a figure
- Heterogeneity across subgroups is buried in interaction rows
- Notes under exhibits are too thin to stand alone for a referee

## The JDE exhibit bar

Development economics has moved toward **figure-forward** presentation, and JDE exhibits should make the headline result legible at a glance to a development economist skimming the paper. Principles:

- **Lead with a figure where the design allows it.** Event-study plots (DID), discontinuity plots (RDD), and treatment-effect-by-subgroup plots communicate a field result faster than a coefficient table. RCT main effects often read best as a clean coefficient plot with confidence intervals.
- **One main table, deep appendix.** Keep the main coefficient table tight (headline outcomes, the preferred specification, clustered SEs noted); push alternative specifications, balance, attrition, and robustness to the extensive online appendix.
- **Self-contained notes.** Each exhibit must state the sample, unit of observation, the level at which standard errors are clustered, the estimator, control set, and what the bars/bands represent — a referee should not have to hunt in the text.
- **Welfare-relevant scaling.** Where possible, scale axes and report effects in policy-comparable units (share of the poverty gap, standard deviations, cost per outcome) so magnitude is visible, not just significance.
- **Geography and maps.** When spatial variation drives the design (market access, program rollout, conflict), a map or spatial figure earns its place.

JDE accepts **any consistent formatting style at submission** (the journal's style is applied at the proof stage), so do not burn time on house-style table formatting before acceptance — spend it on clarity, correct clustering, and reproducibility. Every exhibit must be regenerable from the submitted code.

## Checklist

- [ ] Headline result presented as a figure where the design allows
- [ ] Main table limited to preferred specification + headline outcomes
- [ ] Clustering level and estimator stated in each note
- [ ] Confidence intervals / bands shown; no chartjunk (no 3D, minimal color)
- [ ] Effects scaled to welfare/policy-comparable units where possible
- [ ] Vector output (PDF/EPS) at print resolution
- [ ] Every exhibit reproducible from the master script

## Anti-patterns

- A dense table when one event-study or coefficient plot would carry the result
- Notes that omit the clustering level or sample definition
- Significance stars with no economically meaningful magnitude
- Polishing to Elsevier house style before acceptance (style is applied at proof stage)

## Output format

```
【Headline exhibit】figure type + what it shows
【Main table】outcomes + spec + clustering noted
【Appendix exhibits】[robustness, balance, attrition, ...]
【Scaling】effects in policy-comparable units? [Y/N]
【Reproducible from code?】[Y/N]
【Next step】jde-writing-style
```
