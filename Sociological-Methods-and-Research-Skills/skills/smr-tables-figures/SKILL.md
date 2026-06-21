---
name: smr-tables-figures
description: Use when designing tables and figures for a Sociological Methods & Research (SMR) paper — self-contained simulation grids, method-comparison tables, diagnostic plots, and equation/notation exhibits in ASA-styled format. Designs exhibits; does not write prose or run analyses.
---

# SMR Tables and Figures

Use this to make exhibits carry the methodological argument. At SMR the central exhibits are usually
a **simulation results grid** and a **method-comparison table**, plus diagnostic figures — not the
descriptive-statistics tables of a substantive paper. Each must be readable without the surrounding
text and must let a reviewer audit the claim directly.

## The simulation results exhibit

This is the most-scrutinized table in a methods paper. Design rules:

- **One row per DGP cell, one column block per method** — or a small-multiples figure if the grid is
  large. The reader must compare methods *within* a cell at a glance.
- **Show the metric that matches the claim** (bias, RMSE, coverage, size, power) and report Monte Carlo
  standard error or replication count so the precision of the simulation is visible.
- **Mark the contribution cell** (where the incumbent breaks and the method holds) and the **boundary
  cell** (where the method degrades). Honesty about the boundary reads as rigor.
- Avoid burying the headline in a 40-row table; lead with a compact summary and put the full grid in an
  appendix if needed.

## Method-comparison and notation exhibits

- A **comparison table** of methods × properties (assumptions required, what each is robust to, cost)
  orients the reader before the results — a powerful, distinctly-methods-paper exhibit.
- **Notation must be consistent** between equations, tables, and figures; a symbol that means one thing
  in the theorem and another in the table is a credibility leak at a methods venue.
- Equations are exhibits too: number them, keep estimands and estimators visually distinct, and place
  assumptions near the result they support.

## Diagnostic figures

- For inference methods, a **coverage or size figure** across the difficulty parameter often
  communicates more than a table — show the nominal line and where each method departs from it.
- For estimators, **bias/RMSE curves** across sample size make the asymptotic story visible.
- Keep figures legible in grayscale where possible and ensure every figure is referenced and
  interpreted in the text.

## ASA and SAGE formatting discipline

- Follow **ASA style** for table titles, notes, and numbering (检索于 2026-06；以官网为准); put method
  abbreviations and Monte Carlo details in the table note so the exhibit is self-contained.
- Under **double-anonymized** review, exhibits must not deanonymize: no author-identifying file paths,
  software-account names, or "as in our earlier work" captions.
- Confirm figure/table file-format and resolution requirements on the live SAGE author page before
  final submission.

## Checklist

- [ ] The simulation grid compares methods within each cell at a glance.
- [ ] Metrics match the claim and Monte Carlo precision (SE or replication count) is shown.
- [ ] The contribution cell and the boundary cell are both visible.
- [ ] A method × property comparison table orients the reader.
- [ ] Notation is identical across equations, tables, and figures.
- [ ] Inference figures show the nominal line and each method's departure.
- [ ] Table notes make every exhibit self-contained; ASA style followed.
- [ ] No exhibit deanonymizes the authors.

## Anti-patterns

- **Wall-of-numbers grid**: a giant table with no marked headline cell.
- **Metric mismatch**: reporting bias when the claim is about coverage.
- **Notation drift**: symbols that change meaning between theorem and table.
- **Hidden Monte Carlo error**: results with no replication count or MCSE.
- **Deanonymizing captions**: "our package" or author file paths in exhibits.
- **Decorative descriptive tables**: substantive-paper exhibits crowding out the simulation grid.

## Output format

```text
[Exhibit status] self-contained / needs repair / not ready
[Core exhibits] <simulation grid / method-comparison table / coverage figure>
[Headline + boundary cells] <which cells make the point and the limit>
[Notation check] consistent / drift found where
[Anonymization check] clean / risk where
[Next SMR skill] smr-writing-style
```
