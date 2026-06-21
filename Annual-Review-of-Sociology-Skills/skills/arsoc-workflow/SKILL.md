---
name: arsoc-workflow
description: Use when deciding which arsoc-* sub-skill to invoke next, or when sequencing an invited review article from topic through revision for an Annual Review of Sociology (ARSoc) manuscript. Routes — it does not replace — the specialized skills.
---

# ARSoc Workflow Router (arsoc-workflow)

## Overview

This is the router. It tells you **which arsoc-* skill to use at the current stage** of an **invited review article** aimed at the *Annual Review of Sociology* (ARSoc) — the **Annual Reviews** (nonprofit) sociology survey series, founded **1975**, published as an **annual volume** with the discipline's highest impact factor (检索于 2026-06；2024 JIF ≈ 9, ranked 1st of 219 in Sociology；以官网为准). ARSoc does **not** publish original empirical research. It publishes **authoritative, accessible review articles** that synthesize a sociology subfield — stratification, culture, organizations, networks, race/ethnicity, gender, demography, political and economic sociology — for sociologists across the discipline. So the lifecycle is not "design → identify → estimate → defend"; it is **scope a synthesis-worthy subfield → secure the commission → read the whole literature → impose an organizing framework → cover comprehensively and even-handedly → land the ARSoc voice → clear the Annual Reviews process → revise.**

Default assumption: unless the user says otherwise, treat the target as ARSoc and the artefact as an **invited review**, not a primary-research paper. Operational tells that you are at ARSoc and not a sibling: the work **reviews other scholars' results** rather than reporting its own; **unsolicited finished manuscripts are not accepted** — the **Editorial Committee commissions** topics and authors (you can suggest a topic, but you cannot self-submit a finished paper the way you would to ASR or AJS) (检索于 2026-06；以官网为准); there is **no identification strategy and no replication package of your own data** (you appraise the studies you cover); the contribution is an **analytical map of a subfield** ending in a research agenda, not a new finding. If the user actually has original data and results, they want a primary-research journal (ASR, AJS, *Sociological Science*, *Demography*), not ARSoc — say so.

## When to trigger

- The user asks "what should I do next?" on an invited review
- A review draft reads like an annotated bibliography and needs a spine
- Work is ping-ponging between coverage, framing, balance, and the topic pitch
- An ARSoc editor/Committee letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Unsure the subfield is mature/important enough to review for ARSoc | `arsoc-topic-selection` |
| Need to get the topic in front of the Editorial Committee / accept an invitation | `arsoc-proposal-and-commissioning` |
| Reading is unsystematic; citation gaps likely | `arsoc-literature-synthesis` |
| Draft is a list of studies, not an argument about the subfield | `arsoc-organizing-framework` |
| Coverage vs. selectivity, or fairness across theoretical schools, feels off | `arsoc-comprehensiveness-and-balance` |
| Need who-found-what tables or the conceptual framework figure | `arsoc-tables-figures` |
| Prose is dense/jargon-laden; a sociologist outside the subfield can't follow | `arsoc-writing-style` |
| Documenting the coverage account, or a meta-analysis the review reports | `arsoc-transparency-and-reproducibility` |
| Working with the Editorial Committee on scope / the annual-volume timeline | `arsoc-editor-strategy` |
| Ready to deliver the commissioned draft; need a preflight | `arsoc-submission` |
| Received editor/Committee feedback on the review | `arsoc-revision` |

## Default order

1. `arsoc-topic-selection` — confirm the subfield is ARSoc-scale (mature, important, needs synthesis)
2. `arsoc-proposal-and-commissioning` — get the topic to the Editorial Committee / shape the invitation
3. `arsoc-literature-synthesis` — gather and read the literature systematically (coverage discipline)
4. `arsoc-organizing-framework` — impose the analytical spine
5. `arsoc-comprehensiveness-and-balance` — completeness, fairness, even-handed treatment of schools
6. `arsoc-tables-figures` — who-found-what tables and the conceptual figure
7. `arsoc-writing-style` — the authoritative-yet-accessible ARSoc voice (abstract + intro last)
8. `arsoc-transparency-and-reproducibility` — coverage account + any meta-analytic data/code
9. `arsoc-editor-strategy` — scope and the Committee/production relationship + volume clock
10. `arsoc-submission` — Annual Reviews delivery preflight
11. `arsoc-revision` — after the editor/Committee letter

> `arsoc-writing-style` is a late-stage polish; do not rewrite the intro before the framework and coverage settle. The **commission comes early** — ARSoc is commissioning-first, so `arsoc-proposal-and-commissioning` precedes the heavy reading.

## Anti-patterns

- Treating ARSoc as a journal you submit to cold — it is **commissioning-driven; unsolicited manuscripts are not accepted** (检索于 2026-06；以官网为准)
- Treating the review as an annotated bibliography (no framework) — the cardinal review-article failure
- Using the author's own line of work as the review's center of gravity (self-promotion)
- Importing primary-research instincts: there is no "identification" or "replication package" of your own — you **appraise** others' designs
- Confusing ARSoc with **ASR / AJS** (sociology's primary-research flagships), **Sociological Theory** (theory development, not survey), or the sister series **Annual Review of Psychology / Economics**

## Routing by review archetype

A "review" is not one thing; the bottleneck differs by type. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| subfield-defining synthesis (broad area) | scope is enormous; needs a taxonomy | `arsoc-organizing-framework` |
| concept/process review (e.g. a mechanism or construct) | accessibility across subfields; clear definitions | `arsoc-writing-style` |
| empirical-evidence stocktake (what is the consensus?) | weighing conflicting findings; even-handed schools | `arsoc-comprehensiveness-and-balance` |
| emerging-area review (young, fast-moving) | is it mature enough for an ARSoc volume yet? | `arsoc-topic-selection` |

## Minimal decision snippet

```
if editor_or_committee_letter:        -> arsoc-revision
elif ready_to_deliver_draft:          -> arsoc-submission
elif coverage_account_or_meta:        -> arsoc-transparency-and-reproducibility
elif prose_dense_or_inaccessible:     -> arsoc-writing-style
elif need_tables_or_figures:          -> arsoc-tables-figures
elif coverage_or_fairness_off:        -> arsoc-comprehensiveness-and-balance
elif reads_like_a_list:               -> arsoc-organizing-framework
elif reading_unsystematic:            -> arsoc-literature-synthesis
elif no_commission_yet:               -> arsoc-proposal-and-commissioning
else:                                 -> arsoc-topic-selection
```
