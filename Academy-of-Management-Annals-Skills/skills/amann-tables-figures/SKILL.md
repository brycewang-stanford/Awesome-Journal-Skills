---
name: amann-tables-figures
description: Use when building exhibits for an Academy of Management Annals (Annals) review — the signature framework figure, who-studied-what synthesis tables, and search/coverage exhibits that summarize across a literature. Designs review exhibits; it does not produce original-estimate regression tables (an Annals review reports no new data of its own).
---

# Tables & Figures for a Review (amann-tables-figures)

## When to trigger

- The synthesis is done and the reader needs to *see* the field at a glance
- The organizing framework would land far better as a diagram than as prose
- A fragmented literature would be clearer as a synthesis table than as paragraphs
- You are tempted to paste a regression table — but this is a review, not a primary paper

## The exhibit types an Annals review actually uses

Annals exhibits **summarize and reorganize across the literature**; they never present the author's own estimation. The workhorses:

| Exhibit | Purpose | Design notes |
|---------|---------|--------------|
| **Framework figure** | render the organizing spine — typology grid, process model, multi-level architecture | this is usually the review's *signature* exhibit; it should be restate-able from memory and carry the "new way of seeing the field" |
| **Who-studied-what synthesis table** | one row per study (or per stream): construct, theory base, method/context, finding, your appraisal | rows ordered by the framework's cells, not chronology; columns let the reader compare *comparable* work |
| **Search / coverage exhibit** | a PRISMA-style flow, a search-terms table, or a publications-over-time chart | documents the systematic process from `amann-literature-synthesis` and pre-empts "why did you omit X?" |
| **Agenda / gap matrix** | the framework's empty cells laid out as the future-research agenda | turns the generativity of the framework into a concrete, visible roadmap |

## Building credible synthesis exhibits

- **The framework figure must do conceptual work.** It should *be* the contribution rendered visually — readers should be able to reconstruct the review's argument from it. A decorative diagram that merely lists topics fails.
- **Compare like with like.** In a synthesis table, group studies that theorize the *same* construct; never put incommensurable constructs in one column (the exhibit version of the pooling error from `amann-literature-synthesis`).
- **Carry an appraisal column.** A finding column without a credibility/method note invites "but how good is that study?" — answer it in the table (links to `amann-evidence-standards`).
- **Self-contained captions.** An Annals exhibit is read on its own; the caption states what it shows, the unit, how to read a row, and the source studies.
- **Source every cell.** Each entry traces to a paper in the coding matrix; an unsourced number in a review is indefensible.

## Meta-analysis and bibliometric caution

If you assemble effect sizes into a quantitative synthesis (forest plot, meta-regression) or a co-citation map, you are doing meta-analysis or bibliometrics, with all their assumptions — comparable constructs, independence, publication-bias diagnostics, weighting. Do this only where the literature genuinely supports it; a spurious pooled magnitude or an over-interpreted co-citation cluster is less honest than a qualitative synthesis table. Annals readers include the methodologists who would catch invalid pooling.

## Checklist

- [ ] Each exhibit synthesizes across studies (no original-estimate regression output of the author's own)
- [ ] A framework figure renders the spine and carries the "new way of seeing the field"; restate-able from memory
- [ ] Synthesis-table rows ordered by the framework's cells; only comparable constructs share a column
- [ ] Finding columns carry an appraisal/method note, not bare claims
- [ ] A search/coverage exhibit documents the systematic process (PRISMA-style or terms table)
- [ ] Any meta-analytic or bibliometric exhibit pools only commensurable work; diagnostics noted
- [ ] Captions are self-contained (what / unit / how to read a row / sources)
- [ ] Every cell sources to a paper in the coding matrix
- [ ] An agenda/gap exhibit makes the future-research roadmap visible

## Anti-patterns

- Pasting a regression table of the author's *own* new estimates — a review reports no new results
- A framework figure that merely lists topics instead of encoding the integrative argument
- A synthesis table that pools incommensurable constructs into one column
- A forest plot or co-citation map implying structure the literature does not support
- Finding columns with no appraisal note (every reader then asks "is that study any good?")
- Exhibits whose captions require the body text to be intelligible

## Output format

```text
【Exhibit set】<framework figure / synthesis tables / coverage exhibit / agenda matrix>
【Framework figure】encodes the spine + "new way of seeing"; restate-able from memory? Y/N
【Synthesis table】rows by framework cell; comparable constructs only? Y/N
【Appraisal column】present for every finding? Y/N
【Coverage exhibit】documents the systematic search (PRISMA-style)? Y/N
【Meta/bibliometric】pools only commensurable work (or omitted)? Y/N
【Sourcing】every cell traces to the coding matrix? Y/N
【Next skill】→ amann-writing-style (weave exhibits into the synthesis prose)
```
