---
name: arsoc-tables-figures
description: Use when building exhibits for an Annual Review of Sociology (ARSoc) review — summary "who-found-what" tables, the conceptual/framework figure, and meta-evidence exhibits that synthesize across studies. Designs review exhibits; it does not produce original-estimate regression tables (an ARSoc review reports no new estimates of its own) or write prose (arsoc-writing-style).
---

# Tables & Figures for a Review (arsoc-tables-figures)

## When to trigger

- The synthesis is done and a cross-subfield reader needs to *see* the area at a glance
- A debate or a body of findings would be clearer as a table than as prose
- The organizing framework would land better as a diagram
- You are tempted to paste a regression table — but this is a review, not a primary paper

## The three exhibit types an ARSoc review actually uses

ARSoc exhibits **summarize across the literature**; they do not present the author's own estimation. The workhorses:

| Exhibit | Purpose | Design notes |
|---------|---------|--------------|
| **Who-found-what summary table** | one row per study (or per design class): question/claim, method/mode, sample, finding, tradition, credibility note | rows ordered by the framework's cells, not chronology; columns let the reader compare *comparable* objects |
| **Conceptual / framework figure** | render the organizing spine — taxonomy tree, mechanism/process diagram, levels-of-analysis map, the simple model | this is often the review's signature exhibit; it should be restate-able from memory by a non-specialist |
| **Meta-evidence exhibit** | a forest-style plot, a timeline of a debate, a coverage/citation map | use only when the estimates are *commensurable*; otherwise it manufactures false consensus |

## Building a credible summary table

- **Compare like with like.** Group studies that address the *same object*; never put non-comparable claims or estimands in one column (the cross-study pooling error from `arsoc-comprehensiveness-and-balance`).
- **Carry the mode and the credibility.** Sociology mixes ethnography, surveys, computational analysis, and theory; a method/mode column plus a credibility note lets the reader weigh a row without re-reading the study.
- **Self-contained captions.** An ARSoc exhibit is read on its own by a cross-subfield sociologist; the caption states what the table shows, the unit, how to read a row, and the source studies.
- **Source every cell.** Each entry traces to a study in the evidence matrix; an unsourced claim in a review of record is indefensible.

## The conceptual figure is ARSoc's signature

Because the readership spans subfields, the **framework figure carries disproportionate weight**: it is what a sociologist from another area remembers and reuses (and what gets reproduced in syllabi). Invest in one diagram that renders the spine cleanly — a taxonomy tree, a mechanism flow, or a levels-of-analysis map — so a reader who recalls nothing else can reconstruct the subfield's structure from it. Annual Reviews production supports full-color figures; design for legibility in the published format and confirm current figure specs on the author pages (检索于 2026-06；以官网为准).

## Meta-analysis caution

If you assemble effect sizes into a quantitative synthesis (forest plot, meta-regression), you are doing a *meta-analysis*, with its assumptions — comparable estimands, publication-bias diagnostics, weighting. Sociology's qualitative and theoretical strands rarely reduce to a pooled effect size; do this only where the literature genuinely supports it, and never pool incommensurable findings. ARSoc readers include the methodologists who would catch invalid pooling. If you do run a meta-analysis, its data and code must be reproducible (see `arsoc-transparency-and-reproducibility`).

## Reproduced vs. re-drawn figures

When a figure from a reviewed study is central, prefer a **re-drawn synthesis figure** (your own panel placing several studies on common axes) over copying one study's exhibit — it serves the review's argument and avoids consensus-by-accident. If you reproduce an original figure, attribute it and secure any permission Annual Reviews requires (检索于 2026-06；以官网为准).

## Checklist

- [ ] Each exhibit synthesizes across studies (no original-estimate regression output)
- [ ] Summary-table rows ordered by framework cells; only comparable objects share a column
- [ ] A method/mode column and a credibility note accompany each finding
- [ ] The conceptual figure renders the spine and is restate-able from memory by a non-specialist
- [ ] Any meta-evidence plot pools only commensurable estimates; bias diagnostics noted
- [ ] Captions are self-contained (what / unit / how to read a row / sources)
- [ ] Every cell sources to a study in the evidence matrix
- [ ] Figure specs / permissions confirmed against current Annual Reviews author pages (volatile)

## Anti-patterns

- Pasting a regression table of the author's *own* new estimates — a review reports no new results
- A who-found-what table that pools incomparable claims into one column
- A forest plot implying a pooled consensus the literature does not support (or pooling qualitative work into effect sizes)
- Finding columns with no method/credibility note (every reader then asks "is that study any good?")
- A decorative figure that does not encode the framework — wasting the review's signature exhibit
- Exhibits whose captions require the body text to be intelligible (fails the cross-subfield reader)

## Output format

```text
【Exhibit set】<list: summary tables / conceptual figure / meta-evidence>
【Summary table】rows by framework cell; comparable objects only? Y/N
【Mode + credibility column】present for every finding? Y/N
【Conceptual figure】renders the spine; restate-able from memory? Y/N
【Meta-evidence】pools only commensurable estimates (or omitted)? Y/N
【Sourcing】every cell traces to the evidence matrix? Y/N
【Specs/permissions】confirmed on Annual Reviews author pages? Y/N · 待核实
【Next step】→ arsoc-writing-style (weave exhibits into the synthesis prose)
```
