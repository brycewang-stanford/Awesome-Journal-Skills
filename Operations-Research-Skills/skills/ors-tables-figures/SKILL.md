---
name: ors-tables-figures
description: Use when building the exhibits for an Operations Research (OR) manuscript — theorem/assumption layout, comparison tables against prior work, computational-results tables, and convergence/scaling plots in INFORMS house style. Lays out exhibits; it does not generate the numbers (ors-data-analysis) or prove the results (ors-methods).
---

# Tables, Figures & Exhibits (ors-tables-figures)

## When to trigger

- The model, proofs, and computational results exist and must be displayed clearly.
- You need a clean comparison table separating your method from prior work.
- Reviewers should be able to read a result table without hunting through the text.

## Exhibits that carry an OR paper

Unlike empirical social-science papers built around correlation and regression tables,
*Operations Research* exhibits are about **structure, guarantees, and computation**:

- **Formal-statement layout:** number theorems, propositions, lemmas, and assumptions
  consistently (Theorem 1, Assumption 1) and reference them by number everywhere.
  Use the INFORMS LaTeX style files / `amsthm` so environments render uniformly.
- **Comparison table (prior work × properties):** rows = methods/papers, columns =
  {assumptions, strongest result, approximation factor, complexity/rate}. This is the
  single most persuasive OR exhibit for novelty.
- **Computational-results table:** instances/sizes × {optimality gap, time,
  iterations, baseline comparison}. Report units, time limits, and which configuration
  produced the row; bold or mark wins honestly.
- **Plots:** convergence curves, scaling (size vs. time, ideally log-log), performance
  profiles across instance sets, and for stochastic output **error bars / confidence
  intervals** — never bare means.

## INFORMS house-style notes

- **Format:** prepare for 1.5-spaced, 11-point, 1-inch-margin manuscript layout;
  submit as PDF (source LaTeX/Word on acceptance). Use the provided LaTeX style files.
- **Self-contained exhibits:** each table/figure has a complete caption (what, units,
  instance set, what "best" means) so it stands alone.
- **Notation consistency:** symbols in exhibits match the text exactly; define them in
  the caption or a notation table.
- **E-companion:** large result tables and ablations can go to the e-companion (which
  must not be longer than the manuscript); keep the headline exhibits in the main text.

## Vector tooling

Use TikZ/PGFPlots (or matplotlib exported to vector) for crisp figures; performance
profiles and log-log scaling plots reproduce well as vectors. Keep raw data/scripts in
the ORJournal repository so every exhibit regenerates.

## Anti-patterns

- A results table with no time limits, units, or hardware — irreproducible.
- Bare means for stochastic output with no confidence intervals.
- A comparison table that omits the closest competitor.
- Theorem/assumption numbers that drift between text and exhibits.
- Raster screenshots of plots instead of vector figures.

## Output format

```
【Formal statements】numbered consistently; INFORMS/amsthm style
【Comparison table】prior work × {assumptions, result, complexity}: drafted?
【Computational table】instances × {gap, time, baseline}; units/limits stated
【Plots】convergence / scaling / CIs present?
【House style】1.5-spaced, 11-pt; self-contained captions; e-companion split
【Next step】ors-writing-style
```
