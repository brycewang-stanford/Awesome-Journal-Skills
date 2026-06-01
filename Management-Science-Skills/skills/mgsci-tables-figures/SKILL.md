---
name: mgsci-tables-figures
description: Use when building exhibits for a Management Science (INFORMS) manuscript — propositions and numerical-illustration figures for analytical papers, or result/identification tables and effect plots for empirical papers — keeping notation clean, exhibits self-contained, and the page budget tight for the invited-revision limit. It builds exhibits; it does not run the analysis (mgsci-data-analysis).
---

# Tables & Figures (mgsci-tables-figures)

## When to trigger

- Exhibits are cluttered, notation-heavy, or not self-explanatory
- A reviewer cannot read a result off a table/figure without hunting the text
- You are over the page budget and exhibits are bloated
- You need to present proofs/comparative statics or estimates in house style

Management Science prefers **short, focused** papers and warns that excessive length and **notation density slow review**. Every exhibit should earn its space and stand on its own.

## Analytical lane

- **Propositions/theorems** are numbered and stated cleanly in the text; defer long proofs to the appendix (which does **not** count toward the invited-revision page limit).
- **Comparative-statics figures** are where the managerial insight becomes visible — plot the optimal policy / equilibrium quantity against the key primitive, with axes, parameter values, and the takeaway labeled.
- **Notation tables** (a symbol glossary) help when the model is symbol-heavy; keep notation minimal and consistent throughout.
- Numerical-example tables should report the parameter ranges and confirm the qualitative result holds across them.

## Empirical lane

- **Descriptives / correlation table** with clear variable definitions.
- **Main results table:** coefficients with standard errors, the clustering noted, sample size, and fit; mark significance consistently.
- **Identification exhibits:** event-study plots, parallel-trends checks, first-stage strength, RDD continuity plots — the design's credibility shown, not just asserted.
- **Effect plots:** interaction/marginal-effect plots so the magnitude is readable; report practical magnitude, not only stars.

## House style and self-containment

- Use **author-year** style consistently in notes and captions.
- Each table/figure has a number, a descriptive title, and a note defining every symbol, abbreviation, and the SE/clustering — readable without the body text.
- Keep formatting to the journal's exhibit conventions; verify against current submission guidelines.

## Page budget discipline

Invited revisions must fit within **47 pages double-spaced (25 lines/page)** or **32 pages at 1.5 spacing (33 lines/page)**, 11-pt font, 1-inch margins — the **online appendix is excluded**. Move long proofs, secondary robustness tables, and extended derivations to the online appendix so the main exhibits stay essential.

## Anti-patterns

- A wall of nested notation no glossary explains.
- A results table the reader cannot interpret without the text.
- Interaction effects reported only as coefficients, never plotted.
- Padding the counted main body with exhibits that belong in the online appendix.

## Output format

```
【Lane】analytical / empirical
【Core exhibits】[list, each self-contained]
【Notation/definitions】glossary + table notes complete: yes/no
【Identification/comparative-statics shown】yes/no
【Page budget】main body within invited-revision limit; appendix offloaded: yes/no
【Next step】mgsci-writing-style
```
