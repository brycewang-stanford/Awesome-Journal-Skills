---
name: ppsych-tables-figures
description: Use when building exhibits for a Perspectives on Psychological Science (PoPS) piece — the conceptual/framework figure, who-found-what summary tables, and (for meta-science) practice-prevalence or replication exhibits. Designs review/synthesis exhibits in APA style; it does not produce original-experiment result tables (a PoPS review reports no new study of its own).
---

# Tables & Figures for a PoPS Piece (ppsych-tables-figures)

## When to trigger

- The synthesis is done and a cross-area reader needs to *see* the field at a glance
- A controversy or a body of effects would be clearer as a table than as prose
- The organizing framework would land better as a diagram (often the signature exhibit)
- For meta-science: prevalence of a practice, or a replication landscape, needs a figure
- You are tempted to paste an experiment's result table — but this is a perspective, not a primary paper

## The exhibit types a PoPS piece actually uses

PoPS exhibits **summarize or conceptualize across the literature**; they do not present the author's own experiment. The workhorses:

| Exhibit | Purpose | Design notes |
|---------|---------|--------------|
| **Conceptual / framework figure** | render the organizing spine — taxonomy tree, theory diagram, the reframe | usually the piece's signature exhibit; restate-able from memory by a non-specialist |
| **Who-found-what summary table** | one row per study/area: construct, design, sample, finding (direction + magnitude), credibility note | rows ordered by framework cells, not chronology; only comparable constructs share a column |
| **Practice-prevalence / meta-science exhibit** | bar/trend of how common a practice is; replication-outcome landscape; power distribution | only when the underlying coding is systematic and reproducible |
| **Forest / meta-analytic plot** | pooled effect with uncertainty | only when estimates are commensurable and you are doing a real meta-analysis |

## Building a credible summary table

- **Compare like with like.** Group studies that measure the *same construct*; never put non-comparable constructs in one magnitude column.
- **Carry uncertainty and credibility.** A finding column without effect sizes / CIs and a credibility note invites "but how good is that study?" — answer it in the table.
- **Self-contained APA captions.** A PoPS exhibit is read on its own by an outsider; the note states what the table shows, the unit, how to read a row, and the source studies (APA table/figure conventions).
- **Source every cell.** Each entry traces to a paper in the evidence matrix; an unsourced number in a field-shaping piece is indefensible.

## The conceptual figure is PoPS's signature

Because the readership is cross-area, the **framework figure carries disproportionate weight**: it is what a psychologist from another area remembers and reuses. Invest in one diagram that renders the spine cleanly — a taxonomy tree, a theory flow, or the reframe — so a reader who recalls nothing else can reconstruct the argument. Design for legibility in the published format and confirm current figure specs and color policy on the author pages (检索于 2026-06；以官网为准).

## Meta-science exhibits: show the practice, not a vibe

A reform argument lands when the reader *sees* the prevalence:

- A bar/trend of preregistration, open-data, or replication rates over time makes "the field is changing" concrete.
- A funnel plot or p-curve makes a publication-bias claim auditable rather than rhetorical.
- Every such exhibit must come from the **documented, reproducible coding** in `ppsych-literature-synthesis` — a prevalence figure with an undisclosed sampling frame is the very opacity reform opposes. Note the sampling frame and coding rules in the caption, and deposit the data/code (see `ppsych-transparency-and-reproducibility`).

## Reproduced vs. re-drawn figures

When a figure from a reviewed paper is central, prefer a **re-drawn synthesis figure** (your own panel placing several studies on common axes) over copying one paper's exhibit — it serves the argument and avoids consensus-by-accident. If you reproduce an original figure, attribute it and secure any permission SAGE requires (检索于 2026-06；以官网为准).

## Checklist

- [ ] Each exhibit synthesizes/conceptualizes across studies (no original-experiment result output)
- [ ] Summary-table rows ordered by framework cells; only comparable constructs share a column
- [ ] Finding columns carry effect sizes/CIs and a credibility note, not bare claims
- [ ] The conceptual figure renders the spine and is restate-able from memory by a non-specialist
- [ ] Any meta-science/forest exhibit pools only commensurable estimates; sampling frame disclosed
- [ ] Captions/notes are self-contained and APA-styled (what / unit / how to read / sources)
- [ ] Every cell sources to a paper in the evidence matrix; meta-science data/code depositable
- [ ] Figure specs / color policy / permissions confirmed against current SAGE author pages (volatile)

## Anti-patterns

- Pasting a regression/ANOVA table of the author's *own* new study — a perspective reports no new results
- A who-found-what table that pools incomparable constructs into one magnitude column
- A prevalence figure or forest plot with an undisclosed, unreproducible sampling frame
- Finding columns with no effect size or credibility note
- A decorative figure that does not encode the framework — wasting the signature exhibit
- Exhibits whose captions need the body text to be intelligible (fails the cross-area reader)

## Output format

```text
【Exhibit set】<list: conceptual figure / summary tables / prevalence / forest>
【Conceptual figure】renders the spine; restate-able from memory? Y/N
【Summary table】rows by framework cell; comparable constructs only; effect sizes + credibility? Y/N
【Meta-science exhibit】sampling frame disclosed; coding reproducible? Y/N · N/A
【Forest plot】pools only commensurable estimates (or omitted)? Y/N · N/A
【Sourcing】every cell traces to the evidence matrix? Y/N
【APA/specs/permissions】captions APA; specs + permissions confirmed on SAGE pages? Y/N · 待核实
【Next step】→ ppsych-writing-style (weave exhibits into the synthesis prose)
```
