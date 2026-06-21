---
name: proghg-workflow
description: Use when deciding which proghg-* sub-skill to invoke next, or when sequencing a review essay, theoretical intervention, or progress report from topic through revision for a Progress in Human Geography (PiHG) manuscript. Routes — it does not replace — the specialized skills.
---

# PiHG Workflow Router (proghg-workflow)

## Overview

This is the router. It tells you **which proghg-* skill to use at the current stage** of a **review essay, theoretical/conceptual intervention, or progress report** aimed at *Progress in Human Geography* (PiHG) — **SAGE's** flagship **review and state-of-the-art** journal in human geography, founded **1977** (检索于 2026-06；以官网为准). PiHG does **not** publish original empirical studies or detailed cases. It publishes **critical, theoretically-informed reviews** of current philosophical, conceptual, theoretical, topical, methodological, ethical, and political debates, plus the famous **commissioned progress reports** that survey the development of subfields (economic, urban, political, cultural, feminist, development, more-than-human geographies). So the lifecycle is not "design → identify → estimate → defend"; it is **scope a synthesis-worthy debate → enter via commission or submission → read the subfield critically → impose a conceptual organizing argument → engage traditions fairly and reflexively → land the PiHG voice → clear SAGE peer review → revise.**

Default assumption: unless the user says otherwise, treat the target as PiHG and the artefact as a **critical review / conceptual intervention**, not a primary-research paper. Operational tells that you are at PiHG and not a sibling: the work **appraises and reframes a body of scholarship** rather than reporting its own findings; **PiHG explicitly does not publish empirical results or detailed case studies** (检索于 2026-06；以官网为准); there is **no identification strategy and no replication package of your own data** (you read others' work critically); the contribution is a **conceptual argument about a subfield's trajectory** — where it is and where it should go — not a new estimate. If the user actually has original data and results, they want a primary-research outlet (Annals of the AAG, Transactions of the IBG, an empirical area journal), not PiHG — say so.

## When to trigger

- The user asks "what should I do next?" on a review essay, theory piece, or progress report
- A draft reads like a literature summary and needs a conceptual argument
- Work is ping-ponging between coverage, framing, balance, and the intake route
- A PiHG editor/referee letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Unsure the debate is review-worthy / conceptually significant enough for PiHG | `proghg-topic-selection` |
| Need to pitch a review, or you are writing a commissioned progress report | `proghg-proposal-and-commissioning` |
| Reading is unsystematic; you fear missing a tradition or key intervention | `proghg-literature-synthesis` |
| Draft is a list of works, not an argument about the subfield's development | `proghg-organizing-framework` |
| Coverage vs. selectivity, or fairness across theoretical traditions, feels off | `proghg-comprehensiveness-and-balance` |
| Need a debate-mapping table or a conceptual figure | `proghg-tables-figures` |
| Prose is dense/jargon-heavy; a geographer outside the subfield can't follow | `proghg-writing-style` |
| Documenting scholarly apparatus, positionality, or a search account | `proghg-transparency-and-reproducibility` |
| Working with the editors on a commissioned report vs. a submitted review | `proghg-editor-strategy` |
| Ready to submit via SAGE ScholarOne; need a preflight | `proghg-submission` |
| Received editor/referee feedback on the review | `proghg-revision` |

## Default order

1. `proghg-topic-selection` — confirm the debate is PiHG-scale (significant, contested, needs critical synthesis)
2. `proghg-proposal-and-commissioning` — the commissioned-report vs. submitted-review intake route
3. `proghg-literature-synthesis` — read the subfield critically (coverage discipline across traditions)
4. `proghg-organizing-framework` — impose the conceptual argument / spine
5. `proghg-comprehensiveness-and-balance` — fairness, reflexivity, even-handed traditions
6. `proghg-tables-figures` — debate-mapping tables and the conceptual figure
7. `proghg-writing-style` — the authoritative-yet-accessible PiHG voice (abstract + intro last)
8. `proghg-transparency-and-reproducibility` — scholarly apparatus, positionality, search account
9. `proghg-editor-strategy` — commissioned report vs. submitted review; what referees of a review check
10. `proghg-submission` — SAGE ScholarOne preflight
11. `proghg-revision` — after the editor/referee letter

> `proghg-writing-style` is a late-stage polish; do not rewrite the intro before the conceptual argument and coverage settle. The **route comes early** — a progress report is commissioned and short, a review is submitted and longer, so `proghg-proposal-and-commissioning` precedes the heavy reading.

## Anti-patterns

- Submitting an empirical paper or a detailed case study — PiHG **does not publish empirical results** (检索于 2026-06；以官网为准)
- Treating the review as an annotated bibliography (no conceptual argument) — the cardinal PiHG failure
- Using the author's own line of work as the review's center of gravity (self-promotion)
- Importing primary-research instincts: there is no "identification" or "replication package" of your own — you **read others' work critically**
- Confusing PiHG with **Annals of the AAG** (primary research, four areas), **Transactions of the IBG** (primary + some review), or **Antipode** (radical geography)

## Routing by article archetype

A PiHG piece is not one thing; the bottleneck differs by type. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| commissioned progress report (annual subfield survey, short) | scope discipline within a tight word limit | `proghg-proposal-and-commissioning` |
| major review essay (submitted, broad subfield) | scope is large; needs a conceptual spine | `proghg-organizing-framework` |
| theoretical / conceptual intervention | the argument about where the field should go | `proghg-organizing-framework` |
| emerging-debate review (young, fast-moving) | is it significant/mature enough for PiHG yet? | `proghg-topic-selection` |

## Minimal decision snippet

```
if editor_or_referee_letter:        -> proghg-revision
elif ready_to_submit:               -> proghg-submission
elif apparatus_or_positionality:    -> proghg-transparency-and-reproducibility
elif prose_dense_or_inaccessible:   -> proghg-writing-style
elif need_tables_or_figures:        -> proghg-tables-figures
elif coverage_or_fairness_off:      -> proghg-comprehensiveness-and-balance
elif reads_like_a_list:             -> proghg-organizing-framework
elif reading_unsystematic:          -> proghg-literature-synthesis
elif route_not_chosen:              -> proghg-proposal-and-commissioning
else:                               -> proghg-topic-selection
```
