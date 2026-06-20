---
name: arecon-tables-figures
description: Use when building exhibits for an Annual Review of Economics (ARE) review — summary "who-found-what" tables, the conceptual/framework figure, and meta-evidence exhibits that synthesize across studies. Designs review exhibits; it does not produce original-estimate regression tables (an ARE review reports no new estimates of its own).
---

# Tables & Figures for a Review (arecon-tables-figures)

## When to trigger

- The synthesis is done and an adjacent-field reader needs to *see* the field at a glance
- A controversy or a body of estimates would be clearer as a table than as prose
- The organizing framework would land better as a diagram
- You are tempted to paste a regression table — but this is a review, not a primary paper

## The three exhibit types an ARE review actually uses

ARE exhibits **summarize across the literature**; they do not present the author's own estimation. The workhorses:

| Exhibit | Purpose | Design notes |
|---------|---------|--------------|
| **Who-found-what summary table** | one row per study (or per design class): question/estimand, method, sample, finding (direction + magnitude), credibility note | rows ordered by the framework's cells, not chronology; columns let the reader compare *comparable* objects |
| **Conceptual / framework figure** | render the organizing spine — taxonomy tree, mechanism diagram, the simple unifying model | this is often the review's signature exhibit; it should be restate-able from memory by a non-specialist |
| **Meta-evidence exhibit** | a forest-style plot, a timeline of methods, a coverage map | use only when the estimates are *commensurable*; otherwise it manufactures false consensus |

## Building a credible summary table

- **Compare like with like.** Group studies that estimate the *same object*; never put non-comparable estimands in one magnitude column (the cross-study pooling error from `arecon-evidence-standards`).
- **Carry uncertainty and credibility.** A finding column without a credibility/identification note invites the question "but how good is that study?" — answer it in the table.
- **Self-contained captions.** An ARE exhibit is read on its own by an outsider; the caption states what the table shows, the unit, how to read a row, and the source studies.
- **Source every cell.** Each entry traces to a paper in the evidence matrix; an unsourced number in a review of record is indefensible.

## The conceptual figure is ARE's signature

Because the readership is cross-field, the **framework figure carries disproportionate weight**: it is what an adjacent economist remembers and reuses. Invest in one diagram that renders the spine cleanly — a taxonomy tree, a mechanism flow, or the simple model — so a reader who recalls nothing else can reconstruct the field's structure from it. Annual Reviews production supports full-color figures; design for legibility in the published two-column format and confirm current figure specs on the author pages (检索于 2026-06；以官网为准).

## Meta-analysis caution

If you assemble effect sizes into a quantitative synthesis (forest plot, meta-regression), you are doing a *meta-analysis*, with its assumptions — comparable estimands, publication-bias diagnostics, weighting. Do this only where the literature genuinely supports it; otherwise a qualitative who-found-what table is more honest than a spurious pooled number. ARE readers include the methodologists who would catch invalid pooling. If you do run a meta-analysis, its data/code should be reproducible (see `arecon-submission`).

## Reproduced vs. re-drawn figures

When a figure from a reviewed paper is central, prefer a **re-drawn synthesis figure** (your own panel placing several studies on common axes) over copying one paper's exhibit — it serves the review's argument and avoids consensus-by-accident. If you reproduce an original figure, attribute it and secure any permission Annual Reviews requires (检索于 2026-06；以官网为准).

## Checklist

- [ ] Each exhibit synthesizes across studies (no original-estimate regression output)
- [ ] Summary-table rows ordered by framework cells; only comparable estimands share a column
- [ ] Finding columns carry a credibility/identification note, not bare point estimates
- [ ] The conceptual figure renders the spine and is restate-able from memory by a non-specialist
- [ ] Any meta-evidence plot pools only commensurable estimates; bias diagnostics noted
- [ ] Captions are self-contained (what / unit / how to read a row / sources)
- [ ] Every cell sources to a paper in the evidence matrix
- [ ] Figure specs / permissions confirmed against current Annual Reviews author pages (volatile)

## Anti-patterns

- Pasting a regression table of the author's *own* new estimates — a review reports no new results
- A who-found-what table that pools incomparable estimands into one magnitude column
- A forest plot implying a pooled consensus the literature does not support
- Finding columns with no credibility note (every reader then asks "is that study any good?")
- A decorative figure that does not encode the framework — wasting the review's signature exhibit
- Exhibits whose captions require the body text to be intelligible (fails the cross-field reader)

## Output format

```text
【Exhibit set】<list: summary tables / conceptual figure / meta-evidence>
【Summary table】rows by framework cell; comparable estimands only? Y/N
【Credibility column】present for every finding? Y/N
【Conceptual figure】renders the spine; restate-able from memory? Y/N
【Meta-evidence】pools only commensurable estimates (or omitted)? Y/N
【Sourcing】every cell traces to the evidence matrix? Y/N
【Specs/permissions】confirmed on Annual Reviews author pages? Y/N · 待核实
【Next step】→ arecon-writing-style (weave exhibits into the synthesis prose)
```
