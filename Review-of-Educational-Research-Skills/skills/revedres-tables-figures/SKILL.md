---
name: revedres-tables-figures
description: Use when designing the PRISMA flow diagram, forest/funnel plots, and coding/evidence tables for a Review of Educational Research (RER) review or meta-analysis. Builds exhibits that carry the synthesis; it does not run the analyses (revedres-comprehensiveness-and-balance) or settle reproducibility of the underlying data (revedres-transparency-and-reproducibility).
---

# Tables & Figures (revedres-tables-figures)

## When to trigger

- The synthesis is settled and you need exhibits that prove and carry it
- A draft describes the search in prose with no PRISMA diagram
- A meta-analysis has results but no forest plot or bias figure
- Tables list studies without making them comparable to a reader

## Exhibits an RER review is expected to carry

A review's exhibits are not decoration — they are how a reader audits your search and reads your synthesis at a glance. Build the right ones for the review type.

| Exhibit | Required for | What it must show |
|---|---|---|
| **PRISMA flow diagram** | systematic reviews & meta-analyses | identification → screening → eligibility → included, with counts and exclusion reasons that reconcile |
| **Study characteristics table** | all review types | per-study: sample/context, design, measures, key result, risk-of-bias rating |
| **Forest plot** | meta-analysis | each effect with CI, weight, and the pooled estimate; subgroup panels for moderators |
| **Funnel plot (+ Egger/trim-fill)** | meta-analysis | publication-bias diagnostics, not asserted in prose |
| **Coding / evidence-map table** | narrative & critical syntheses | studies arranged by the framework's cells, so the spine is visible |
| **Conceptual figure** | critical/integrative syntheses | the organizing model or taxonomy as a diagram |

## Design rules so exhibits do real work

1. **The PRISMA numbers must reconcile.** Identified − duplicates − screened-out − full-text-excluded = included. Reviewers add them up; a mismatch undermines the whole review.
2. **Compare only commensurable estimates.** A study-characteristics table that mixes incompatible outcomes invites false "the literature finds…" claims; group by construct and note the metric.
3. **Carry credibility in the table.** Every finding/effect column needs a risk-of-bias rating beside it so emphasis is visibly credibility-weighted, not count-weighted.
4. **The forest plot is the result.** Order it by the moderator that matters (so heterogeneity is visible), show weights, and place the pooled diamond with its CI and prediction interval where useful.
5. **The conceptual figure should be re-buildable from memory.** If a reader cannot redraw your framework after one look, it is too busy.
6. **APA 7 formatting.** Number, title, and note each table/figure per APA 7th; figures legible in greyscale; alt-text/notes where required.

## Matching the exhibit set to the review type

Do not build a forest plot for a conceptual synthesis or skip the PRISMA flow for a systematic review — the expected set differs:

- **Meta-analysis:** PRISMA flow + study-characteristics table (with effect sizes and risk-of-bias) + forest plot + publication-bias figure are all effectively mandatory. A subgroup forest or meta-regression figure carries the moderator story.
- **Systematic review (narrative):** PRISMA flow + a study-characteristics table + an evidence-map table organized by the framework's cells; a forest plot is inappropriate if effects are not pooled.
- **Critical / conceptual synthesis:** a conceptual figure of the framework is the centerpiece; an evidence-map or comparison table shows how the literature populates it. No PRISMA flow is required if the synthesis is explicitly non-systematic, but the search logic must still be described.

The exhibits should let a skim-reader reconstruct the search, the corpus, and the synthesis without reading the prose — that is the test of a good RER exhibit set.

## Checklist

- [ ] PRISMA flow diagram present (systematic/meta) and its counts reconcile exactly
- [ ] Study-characteristics table: sample, design, measure, result, risk-of-bias per study
- [ ] Forest plot ordered by a meaningful moderator; weights + pooled estimate + CI shown
- [ ] Publication-bias figure (funnel/Egger/trim-fill) included for meta-analyses
- [ ] Narrative/critical review has an evidence-map table arranged by the framework's cells
- [ ] A conceptual figure renders the organizing model (for integrative syntheses)
- [ ] Only commensurable outcomes are tabled together; metric noted per group
- [ ] Tables/figures formatted to APA 7; legible in greyscale; embedded in the Word manuscript

## Anti-patterns

- No PRISMA diagram, or one whose numbers do not add up
- A study table that mixes incompatible outcomes into one comparison
- A forest plot with no weights, no pooled estimate, or arbitrary study order
- Asserting "no publication bias" in prose with no funnel/Egger/trim-fill figure
- A conceptual figure so cluttered it cannot be redrawn from memory
- Finding columns with no adjacent quality rating, so weak and strong studies look equal
- Pasting original-regression output of the author's *own* data — RER reviews synthesize, not report new estimates

## Output format

```
【Review type】systematic | meta-analysis | critical-integrative
【PRISMA】flow diagram present; counts reconcile? Y/N
【Study table】sample/design/measure/result/RoB per study? Y/N
【Forest plot】ordered by moderator; weights + pooled CI? Y/N (meta)
【Bias figure】funnel/Egger/trim-fill included? Y/N (meta)
【Evidence map】arranged by framework cells? Y/N (narrative/critical)
【Conceptual figure】model/taxonomy diagram present + re-drawable? Y/N
【APA 7】numbering, titles, notes, greyscale legibility checked? Y/N
【Next step】→ revedres-writing-style (write the synthesizing RER voice; abstract + intro last)
```
