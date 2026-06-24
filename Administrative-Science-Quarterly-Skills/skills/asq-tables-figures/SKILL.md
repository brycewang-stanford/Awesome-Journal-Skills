---
name: asq-tables-figures
description: Use when building and refining exhibits for an Administrative Science Quarterly (ASQ) manuscript — qualitative data structures and data-to-theory tables, process models, and quantitative tables. Designs exhibits; it does not run the analysis behind them.
---

# Tables & Figures (asq-tables-figures)

## When to trigger

- Your exhibits are dense, generic, or do not reveal the data structure
- Qualitative: you have quotes but no data-to-theory table or process model figure
- Quantitative: tables are over-stuffed or hide the result that matters
- Reviewers cannot reconstruct how your data became theory from the exhibits

## Principle: exhibits do theoretical work

At ASQ, exhibits are part of the *argument*, not decoration. A reader should be able to grasp the contribution from the figures and tables alone. Build them in tandem with `asq-data-analysis`.

## Qualitative exhibits

- **Data structure figure.** Show first-order codes → second-order themes → aggregate dimensions (Gioia-style), or an equivalent cross-case/process display. This is often the single most scrutinized exhibit in an inductive ASQ paper.
- **Data-to-theory table.** Columns: theoretical construct/dimension → representative quotes/evidence (proof quotes) → analytic note. This makes the inference auditable.
- **Process model figure.** For process theory, a clean phase/feedback diagram with arrows that mean something (sequence, transformation, feedback), labeled with your constructs.
- **Case/site table.** Comparative table of cases on key dimensions (for multiple-case designs).
- **Power quotes** live in the body; **proof quotes** live in tables — keep the body readable.

## Quantitative exhibits

- **Descriptives & correlations** table (means, SD, correlations) — standard and complete.
- **Main regression table.** Build models cumulatively (baseline → controls → focal effects → interactions). Avoid wall-to-wall columns; show the models that test the theory.
- **Interaction plots.** Plot significant moderations; a marginal-effects/simple-slopes figure beats a coefficient alone.
- **Robustness** can be summarized compactly or moved to an appendix; the body shows the result that matters.

## Craft standards (both)

- Each exhibit is self-contained: title, units, notes, significance conventions, and source defined in the note.
- Figures are clean and legible in grayscale; no chart-junk; consistent fonts and labels.
- Number and reference every exhibit in text; the text *interprets*, it does not merely repeat the table.
- Keep exhibits **anonymized** for ASQ's double-blind review (no author-revealing site names or acknowledgments in figure sources).
- Follow **APA style** for citations in notes (ASQ adopted APA in January 2025), with SAGE table conventions; manuscripts go in via ScholarOne (Word or PDF, 12-pt Times New Roman, double-spaced). Exhibits count toward length, and ASQ rewards "high intellectual value per page" — keep the whole manuscript near the suggested **35–45 pages of text** (over-long files are unsubmitted before review). Verify current details at journals.sagepub.com/author-instructions/asq.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). ASQ wants a clean causal or well-identified observational design behind an organizational-theory contribution; reduced-form estimation fits the chain below, interpretive work does not.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Qual: data-structure figure present and faithful to the coding
- [ ] Qual: data-to-theory / evidence table lets a reader audit the inference
- [ ] Qual: process model figure (if process theory) with meaningful arrows
- [ ] Quant: descriptives + correlations table complete
- [ ] Quant: main table built cumulatively; interactions plotted
- [ ] Every exhibit is self-contained (title, notes, units, significance key)
- [ ] Text interprets exhibits rather than restating them
- [ ] Formatting matches current ASQ/SAGE guidelines (verify on official page)

## Anti-patterns

- A "wall of coefficients" table where the key result is buried among dozens of columns
- Qualitative papers with quotes but no data-structure figure or evidence table
- Process figures whose arrows have no defined meaning
- Exhibits that require the body text to be interpretable (not self-contained)
- Chart-junk, illegible grayscale, inconsistent decimals/labels
- Reporting interaction coefficients without a plot

## Output format

```
【Exhibit list】figures + tables planned
【Data-to-theory exhibit】present? (qual) / cumulative main table? (quant)
【Process model】present? (if process theory)
【Self-containment】all notes/units/keys complete?
【Formatting】matches ASQ/SAGE guidelines (verify)
【Next step】asq-writing-style
```
