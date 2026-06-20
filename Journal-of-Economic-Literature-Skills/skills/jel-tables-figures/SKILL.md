---
name: jel-tables-figures
description: Use when building exhibits for a Journal of Economic Literature (JEL) survey — summary "who-found-what" tables, conceptual/framework figures, and meta-evidence exhibits that synthesize across studies. Designs survey exhibits; it does not produce original-estimate regression tables (a JEL survey reports no new estimates of its own).
---

# Tables & Figures for a Survey (jel-tables-figures)

## When to trigger

- The synthesis is done and the reader needs to *see* the field at a glance
- A controversy or a body of estimates would be clearer as a table than as prose
- The organizing framework would land better as a diagram
- You are tempted to paste a regression table — but this is a survey, not a primary paper

## The three exhibit types a JEL survey actually uses

JEL exhibits **summarize across the literature**; they do not present the author's own estimation. The workhorses:

| Exhibit | Purpose | Design notes |
|---------|---------|--------------|
| **Who-found-what summary table** | one row per study (or per design class): question/estimand, method, sample, finding (direction + magnitude), credibility note | rows ordered by the framework's cells, not chronology; columns let the reader compare *comparable* objects |
| **Conceptual / framework figure** | render the organizing spine — taxonomy tree, mechanism diagram, the simple unifying model | this is often the survey's signature exhibit; it should be restate-able from memory |
| **Meta-evidence exhibit** | a forest-style plot or funnel of effect sizes, a timeline of methods, a coverage map | use only when the estimates are *commensurable*; otherwise it manufactures false consensus |

## Building a credible summary table

- **Compare like with like.** Group studies that estimate the *same object*; never put non-comparable estimands in one magnitude column (the cross-study version of the pooling error from `jel-literature-synthesis`).
- **Carry uncertainty and credibility.** A finding column without a credibility/identification note invites a referee to ask "but how good is that study?" — answer it in the table.
- **Self-contained captions.** A JEL exhibit is read on its own; the caption states what the table shows, the unit, and how to read a row, and points to the source studies.
- **Source every cell.** Each entry traces to a paper in the evidence matrix; a survey table with an unsourced number is indefensible.

## Meta-analysis caution

If you assemble effect sizes into a quantitative synthesis (forest plot, meta-regression), you are doing a *meta-analysis*, with all its assumptions — comparable estimands, publication-bias diagnostics, weighting. Only do this where the literature genuinely supports it; otherwise a qualitative who-found-what table is more honest than a spurious pooled number. JEL readers include the methodologists who would catch an invalid pooling.

## Reproduced vs. re-drawn figures

When a figure from a surveyed paper is central, prefer a **re-drawn synthesis figure** (your own panel that places several studies on common axes) over copying one paper's exhibit. A re-drawn figure serves the survey's argument and avoids the consensus-by-accident of reprinting whichever paper had the prettiest chart; if you do reproduce an original figure, attribute it and secure any permission the AEA style guide requires.

## Checklist

- [ ] Each exhibit synthesizes across studies (no original-estimate regression output)
- [ ] Summary-table rows ordered by the framework's cells; only comparable estimands share a column
- [ ] Finding columns carry a credibility/identification note, not bare point estimates
- [ ] The conceptual figure renders the organizing spine and is restate-able from memory
- [ ] Any meta-evidence plot pools only commensurable estimates; bias diagnostics noted
- [ ] Captions are self-contained (what / unit / how to read a row / sources)
- [ ] Every cell sources to a paper in the evidence matrix
- [ ] Exhibits are placed where the argument needs them, sized for readability in print

## Anti-patterns

- Pasting a regression table of the author's *own* new estimates — a survey reports no new results
- A who-found-what table that pools incomparable estimands into one magnitude column
- A forest plot implying a pooled consensus the literature does not support
- Finding columns with no credibility note (every reader then asks "is that study any good?")
- Decorative figures that do not encode the framework
- Exhibits whose captions require the body text to be intelligible

## Output format

```
【Exhibit set】<list: summary tables / conceptual figure / meta-evidence>
【Summary table】rows by framework cell; comparable estimands only? Y/N
【Credibility column】present for every finding? Y/N
【Conceptual figure】renders the spine; restate-able from memory? Y/N
【Meta-evidence】pools only commensurable estimates (or omitted)? Y/N
【Sourcing】every cell traces to the evidence matrix? Y/N
【Next step】→ jel-writing-style (weave exhibits into the synthesis prose)
```
