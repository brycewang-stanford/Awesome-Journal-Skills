---
name: rof-tables-figures
description: Use when designing Review of Finance tables and figures under the 60-page total cap, including empirical-finance exhibits, theory figures, robustness tables, data-description tables, and replication-friendly notes.
---

# Review of Finance Tables And Figures

Use this when exhibits are too dense, under-explained, or wasting the 60-page budget. At RoF
exhibits are not free space: the hard 60-page cap explicitly counts appendices, bibliography,
figures, and tables, so every exhibit must earn its place and be self-contained for a
top-three-standard referee.

## When to trigger

- The main table has too many columns and buries the headline result.
- Figures lack confidence bands, units, or self-contained notes.
- The manuscript is near or over 60 pages and exhibits are part of why.

## Exhibit rules

- Lead with one clean headline exhibit a reader grasps in seconds; keep the main paper focused
  on exhibits that carry the finance contribution or address likely top-three-standard
  objections.
- Use table notes to document sample, period, variable construction, fixed effects,
  clustering, controls, units, and economic magnitude — a referee should read the exhibit
  without hunting through the text.
- Prefer figures where a relationship is visual: event-time cumulative returns, sorted
  portfolios, factor loadings. Show confidence bands; avoid chartjunk; use vector output
  (PDF/EPS).
- Move mechanical robustness grids to the supplementary replication package rather than padding
  in-paper exhibits, keeping the main identification logic self-contained.
- For theory papers, use figures to clarify comparative statics or equilibrium regions, not to
  decorate algebra; keep proofs compact so they do not eat the page budget.
- Respect the formatting baseline (at least 12-point font, at least 1.5 line spacing) and
  re-check that appendices, bibliography, figures, and tables still fit the 60-page cap.

## Anti-patterns

- A nine-column kitchen-sink table as the main result.
- Figures with no units, no bands, or notes that require the body text to interpret.
- Letting appendix tables and the bibliography silently push the paper past 60 pages.

## Output format

```text
[Exhibit status] keep / compress / move / delete
[Finance role] <main result, identification, mechanism, robustness, or theory>
[Missing note] <sample, variables, controls, SEs, units, or data source>
[Page-budget action] <specific cut or move>
```
