---
name: mathfin-tables-figures
description: Use when preparing figures, numerical tables, theorem maps, appendix exhibits, and algorithm displays for a Mathematical Finance manuscript, ensuring every exhibit supports a rigorous result rather than acting as stand-alone empirical evidence.
---

# Tables & Figures (mathfin-tables-figures)

## When to trigger

- A numerical section needs figures or tables
- A proof-heavy manuscript needs diagrams, assumption maps, or appendix organization
- Exhibits risk looking like empirical finance rather than theorem support

## Exhibit rules

Every exhibit should answer: which theorem, proposition, algorithm, or modelling
insight does this support?

1. **Tie figures to formal results.** A convergence plot should cite the theorem or
   rate it illustrates.
2. **Report numerical settings.** Grid, time step, paths, tolerance, truncation,
   seed, and software version belong in the caption or appendix.
3. **Keep tables small.** Use them for parameter values, convergence rates,
   boundary comparisons, or sensitivity to assumptions.
4. **Move detail to appendices.** The author guidelines encourage detailed
   mathematical analysis in appendices; use them for long derivations and
   extended numerical diagnostics.
5. **Avoid empirical-style claims.** A calibration illustration does not establish
   an empirical result unless the paper is designed for that, which this venue
   generally is not.

## Good exhibits

- Error decay against the proven rate
- Free-boundary shape implied by an optimal stopping theorem
- Sensitivity of a pricing formula to parameters with financial meaning
- Algorithm pseudocode paired with convergence conditions
- Assumption dependency diagram for a complex theorem

## Output format

```text
[Exhibit] figure / table / algorithm / appendix
[Formal result supported] theorem/proposition/lemma
[Numerical details needed] ...
[Caption claim] ...
[Next step] mathfin-writing-style
```
