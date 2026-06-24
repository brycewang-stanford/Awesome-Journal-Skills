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

## Exhibit pushback patterns and the INFORMS-style fix

| Referee remark on an exhibit | What it flags | Venue-specific fix |
|------------------------------|---------------|--------------------|
| "Computational study lacks benchmarks" | no recognized baseline column | add a column for the closest prior method and a strong solver on standard instances |
| "Cannot tell what 'best' means" | undefined win marking | caption defines the metric and tie-breaking; bold/mark honestly |
| "Results not reproducible from the table" | missing units/time-limit/hardware | state units, time limit, termination, hardware, and the producing configuration |
| "Means hide variability" | bare means for stochastic output | error bars / confidence intervals on every random-output figure |
| "Theorem numbers don't match the text" | label drift | single numbering scheme via `amsthm`; reference by number everywhere |
| "Scaling claim unsupported" | linear-axis time plot | log-log size-vs-time plot or a performance profile across the instance set |

These are the exhibit-level versions of the two flags that sink OR computational
sections: *no benchmarks* and *structure-not-connected-to-application*. Because
Operations Research is the INFORMS flagship demanding **both** theorem-grade rigor and a
credible computational study, the comparison table and the performance profile carry as
much referee weight as the theorem environments.

## Worked exhibit pair (illustrative numbers)

A paper proves a 1.5-approximation and validates it. Two exhibits do the persuading:

Comparison table — `Method × {assumption, factor, complexity}`:

| Method | Assumption | Factor | Complexity |
|--------|-----------|--------|------------|
| Prior (Author year) | bounded ratios | 2.0 | O(n²) |
| This paper | general weights | 1.5 | O(n² log n) |

Computational table — `Instance set × {mean gap %, time (s), solver baseline}`, e.g.
TSPLIB-derived instances showing 1.8% mean gap vs. 31% for the heuristic baseline at a
600 s limit on stated hardware, with the proved 50% bound never violated. The figure
pairs them: a log-log scaling plot with confidence-interval bands over 30 seeds. The
table corroborates the theorem's bound; the plot shows it holds as size grows.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Operations Research is predominantly analytical / optimization / stochastic modeling; use the chain below only for its empirical/causal papers — modeling, optimization, and simulation are outside this causal-inference toolchain.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
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
