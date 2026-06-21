---
name: revedres-workflow
description: Use when deciding which revedres-* sub-skill to invoke next, or when sequencing a systematic review, meta-analysis, or critical integrative synthesis from question-scoping through revision for a Review of Educational Research (RER) manuscript. Routes — it does not replace — the specialized skills.
---

# RER Workflow Router (revedres-workflow)

## Overview

This is the router. It tells you **which revedres-* skill to use at the current stage** of a **review article** aimed at the *Review of Educational Research* (RER) — the **American Educational Research Association's (AERA)** review journal of record, published by **SAGE** (founded 1931). RER publishes **comprehensive, critical, integrative reviews of research bearing on education** — systematic reviews, meta-analyses, and conceptual/critical syntheses — and **does not publish original empirical research** unless it is incorporated in a broader integrative review.

The decisive fact that shapes everything: **unlike Annual Reviews, RER reviews are SUBMITTED and peer-reviewed, not invited.** There is no commissioning editor handing you a slot. So the rigor of the **review itself** is the contribution — a documented systematic search and PRISMA flow, transparent inclusion/exclusion, reliable double-coding, defensible meta-analytic models (or a principled narrative synthesis), risk-of-bias and sensitivity analysis, and an **organizing framework that advances theory or policy** rather than tallying studies. The lifecycle is therefore: **scope a synthesis-worthy question → write and (where applicable) preregister a protocol → search and screen systematically to a PRISMA flow → impose a conceptual framework → demonstrate comprehensiveness, code reliably, and probe robustness → make transparency/reproducibility provable → write in RER's masked APA-7 voice → submit and revise.**

Default assumption: unless the user says otherwise, treat the target as RER and the artefact as a **review** (systematic / meta-analytic / critical-integrative), not a primary-research paper. Operational tells that you are at RER and not a sibling: the work **synthesizes other people's studies** rather than reporting your own; the natural early step is a **protocol/PROSPERO registration**, not an IRB-approved data collection; there is **no identification strategy of your own** (you appraise the designs of the studies you include). If the user has original empirical results, they want *American Educational Research Journal* (AERJ) or *AERA Open*, not RER — say so.

## When to trigger

- The user asks "what should I do next?" on a review/meta-analysis
- A review draft reads like an annotated bibliography and needs an analytic spine
- Work is ping-ponging between search, screening, coding, and framing
- An RER editor/reviewer letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Unsure the question is synthesis-worthy / RER-scale | `revedres-topic-selection` |
| Need a protocol, scope, and (where applicable) preregistration before searching | `revedres-proposal-and-commissioning` |
| Search/screening is unsystematic; PRISMA flow not built | `revedres-literature-synthesis` |
| Corpus is a pile of studies, not an argument about the field | `revedres-organizing-framework` |
| Coverage, risk-of-bias, or robustness feels thin | `revedres-comprehensiveness-and-balance` |
| Need a PRISMA flow, forest plot, or evidence/coding table | `revedres-tables-figures` |
| Prose summarizes study-by-study; reads narrow or jargon-heavy | `revedres-writing-style` |
| Coding reliability, open materials, reproducible meta-analysis to settle | `revedres-transparency-and-reproducibility` |
| Negotiating scope or handling reviewers of a review | `revedres-editor-strategy` |
| Ready to submit via Manuscript Central; need a preflight | `revedres-submission` |
| Received editor/reviewer feedback on the review | `revedres-revision` |

## Default order

1. `revedres-topic-selection` — confirm the question is RER-scale (important, mature enough, needs synthesis)
2. `revedres-proposal-and-commissioning` — protocol + (where applicable) PROSPERO/PRISMA-P preregistration
3. `revedres-literature-synthesis` — systematic search, screening, PRISMA flow, data extraction
4. `revedres-organizing-framework` — impose the conceptual spine that advances theory/policy
5. `revedres-comprehensiveness-and-balance` — exhaustiveness, risk-of-bias, heterogeneity, sensitivity
6. `revedres-tables-figures` — PRISMA flow, forest/funnel plots, coding and evidence tables
7. `revedres-writing-style` — the synthesizing RER voice in APA 7 (abstract + intro last)
8. `revedres-transparency-and-reproducibility` — coding reliability, open data/code, MARS/PRISMA reporting
9. `revedres-editor-strategy` — scope negotiation and reviewer expectations
10. `revedres-submission` — Manuscript Central preflight (masking, APA 7, 150-word abstract)
11. `revedres-revision` — after the editor/reviewer letter

> `revedres-writing-style` is a late-stage polish; do not rewrite the intro before the organizing framework and the corpus settle. The **protocol comes early** — a credible systematic review fixes its search and inclusion rules *before* screening, so `revedres-proposal-and-commissioning` precedes the heavy reading.

## Anti-patterns

- Searching and screening with no written protocol, then back-fitting inclusion rules to a convenient set — reviewers read this as a fishing expedition
- Treating the review as an annotated bibliography (no framework) — the named RER failure mode
- Vote-counting significant vs. non-significant studies instead of weighing by effect size, design quality, and estimand
- Importing primary-research instincts: there is no "identification" or "replication package" of your own data — you **appraise** the included studies and report **your** synthesis's reproducibility
- Confusing RER with AERJ / *AERA Open* (primary research), *Educational Researcher* (short commentary/policy), *Review of Research in Education* (commissioned thematic volumes), or *Psychological Bulletin* (psychology reviews)

## Routing by review archetype

A "review" is not one thing; the bottleneck differs by type. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| meta-analysis (pooled effect sizes) | comparability of estimands + a defensible model and heterogeneity story | `revedres-comprehensiveness-and-balance` |
| systematic review (PRISMA, qualitative synthesis) | a complete, documented search and reliable screening | `revedres-literature-synthesis` |
| critical/conceptual synthesis | the organizing framework that reframes the field | `revedres-organizing-framework` |
| emerging-area review (young, fast-moving) | is the literature mature enough for RER yet? | `revedres-topic-selection` |

## Minimal decision snippet

```
if editor_or_reviewer_letter:        -> revedres-revision
elif ready_to_submit:                -> revedres-submission
elif coding_or_reproducibility:      -> revedres-transparency-and-reproducibility
elif prose_summarizes_not_synth:     -> revedres-writing-style
elif need_prisma_or_forest_plot:     -> revedres-tables-figures
elif coverage_rob_or_robustness:     -> revedres-comprehensiveness-and-balance
elif reads_like_a_list:              -> revedres-organizing-framework
elif search_unsystematic:            -> revedres-literature-synthesis
elif no_protocol_yet:                -> revedres-proposal-and-commissioning
else:                                -> revedres-topic-selection
```
