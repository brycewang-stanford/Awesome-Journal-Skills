---
name: jel-workflow
description: Use when deciding which jel-* sub-skill to invoke next, or when sequencing a survey/review article from topic selection through revision for a Journal of Economic Literature (JEL) submission. Routes — it does not replace — the specialized skills.
---

# JEL Workflow Router (jel-workflow)

## Overview

This is the router. It tells you **which jel-* skill to use at the current stage** of a **survey or review article** aimed at the *Journal of Economic Literature* (JEL) — the **American Economic Association's** survey-of-record journal (founded 1969). JEL does **not** publish original empirical research. It publishes commissioned and peer-reviewed **syntheses of bodies of economic research**, book reviews, and maintains the **JEL classification system**. So the lifecycle is not "design → identify → estimate → defend"; it is **scope a synthesis-worthy field → propose it → read the whole literature → impose an organizing framework → synthesize comprehensively and even-handedly → land the JEL voice → submit and revise.**

Default assumption: unless the user says otherwise, treat the target as JEL and the artefact as a **survey**, not a primary-research paper. Operational tells that you are at JEL and not a sibling: the work **reviews other people's results** rather than reporting your own; the natural first step is a **~10-page proposal emailed to the editor** before a full draft (检索于 2026-06；以官网为准); there is **no identification strategy and no replication package of your own data** (you instead appraise the studies you cover); the contribution is an **analytical map of a field**, not a new estimate. If the user actually has original results, they want a primary-research journal (e.g. AER, QE), not JEL — say so.

## When to trigger

- The user asks "what should I do next?" on a survey/review
- A survey draft reads like an annotated bibliography and needs a spine
- Work is ping-ponging between coverage, framing, balance, and the proposal
- A JEL editor/referee letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Unsure the field is mature/important enough to survey for JEL | `jel-topic-selection` |
| Need to pitch the survey to the editor before writing it | `jel-proposal-and-commissioning` |
| Reading is unsystematic; citation gaps likely | `jel-literature-synthesis` |
| Draft is a list of papers, not an argument about the field | `jel-organizing-framework` |
| Coverage vs. selectivity, or fairness across schools, feels off | `jel-comprehensiveness-and-balance` |
| Need who-found-what tables or a conceptual figure | `jel-tables-figures` |
| Prose is dense/jargon-laden; non-specialist can't follow | `jel-writing-style` |
| Assigning JEL codes, or relating the survey to the JEL taxonomy | `jel-classification-system` |
| Negotiating scope or handling referees of a survey | `jel-editor-strategy` |
| Ready to submit/propose via the AEA portal; need a preflight | `jel-submission` |
| Received editor/referee feedback on the survey | `jel-revision` |

## Default order

1. `jel-topic-selection` — confirm the field is JEL-scale (mature, important, needs synthesis)
2. `jel-proposal-and-commissioning` — pitch a ~10-page proposal before drafting
3. `jel-literature-synthesis` — gather and read the literature systematically
4. `jel-organizing-framework` — impose the analytical spine
5. `jel-comprehensiveness-and-balance` — completeness, fairness, even-handed controversies
6. `jel-tables-figures` — summary tables and conceptual figures
7. `jel-writing-style` — the authoritative-yet-accessible JEL voice (abstract + intro last)
8. `jel-classification-system` — assign JEL codes; situate the survey in the taxonomy
9. `jel-editor-strategy` — scope negotiation and referee expectations
10. `jel-submission` — AEA portal preflight (proposal or full paper)
11. `jel-revision` — after the editor/referee letter

> `jel-writing-style` is a late-stage polish; do not rewrite the intro before the organizing framework and coverage settle. The **proposal comes early** — much of JEL is invited or proposal-first, so `jel-proposal-and-commissioning` precedes the heavy reading.

## Anti-patterns

- Writing the full survey before sending a proposal — JEL prefers a ~10-page sketch first (检索于 2026-06；以官网为准)
- Treating the survey as an annotated bibliography (no framework) — the named JEL failure mode
- Using the author's own line of work as the survey's center of gravity (self-promotion)
- Importing primary-research instincts: there is no "identification" or "replication package" — you **appraise** others' designs, you do not run your own
- Confusing JEL with JEP (shorter, non-technical, broad audience) or with Annual Review of Economics

## Routing by survey archetype

A "survey" is not one thing; the bottleneck differs by type. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| field-defining synthesis (broad subfield) | scope is enormous; needs a taxonomy | `jel-organizing-framework` |
| methods/tool survey (e.g. an estimator family) | accessibility to non-specialists; worked intuition | `jel-writing-style` |
| empirical-evidence stock-take (what is the consensus?) | comprehensiveness + even-handed weighing of conflicting results | `jel-comprehensiveness-and-balance` |
| emerging-area review (young, fast-moving) | is it mature enough for JEL yet? | `jel-topic-selection` |

## Minimal decision snippet

```
if editor_or_referee_letter:        -> jel-revision
elif ready_to_submit_or_propose:    -> jel-submission
elif codes_or_taxonomy:             -> jel-classification-system
elif prose_dense_or_inaccessible:   -> jel-writing-style
elif need_tables_or_figures:        -> jel-tables-figures
elif coverage_or_fairness_off:      -> jel-comprehensiveness-and-balance
elif reads_like_a_list:             -> jel-organizing-framework
elif reading_unsystematic:          -> jel-literature-synthesis
elif no_proposal_yet:               -> jel-proposal-and-commissioning
else:                               -> jel-topic-selection
```
