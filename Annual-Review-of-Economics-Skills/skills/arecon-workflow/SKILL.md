---
name: arecon-workflow
description: Use when deciding which arecon-* sub-skill to invoke next, or when sequencing an invited review article from topic through revision for an Annual Review of Economics (ARE) manuscript. Routes — it does not replace — the specialized skills.
---

# ARE Workflow Router (arecon-workflow)

## Overview

This is the router. It tells you **which arecon-* skill to use at the current stage** of an **invited review article** aimed at the *Annual Review of Economics* (ARE) — the **Annual Reviews** (nonprofit) survey series for economics, founded **2009**, published as an **annual volume** with a high impact factor (检索于 2026-06；11.4 in 2024, ~5th of 617 econ journals；以官网为准). ARE does **not** publish original empirical research. It publishes **authoritative, accessible review articles** that synthesize a field for specialists and adjacent economists. So the lifecycle is not "design → identify → estimate → defend"; it is **scope a synthesis-worthy field → secure the invitation → read the whole literature → impose an organizing framework → appraise the evidence fairly → land the ARE voice → clear the Annual Reviews production process → revise.**

Default assumption: unless the user says otherwise, treat the target as ARE and the artefact as an **invited review**, not a primary-research paper. Operational tells that you are at ARE and not a sibling: the work **reviews other people's results** rather than reporting its own; **unsolicited manuscripts are not accepted** — the **Editorial Committee commissions** topics and authors (you can suggest a topic, but you cannot self-submit a finished paper the way you would to a journal) (检索于 2026-06；以官网为准); there is **no identification strategy and no replication package of your own data** (you appraise the studies you cover); the contribution is an **analytical map of a field**, not a new estimate. If the user actually has original results, they want a primary-research journal (AER, QE, an AEJ), not ARE — say so.

## When to trigger

- The user asks "what should I do next?" on an invited review
- A review draft reads like an annotated bibliography and needs a spine
- Work is ping-ponging between coverage, framing, balance, and the invitation pitch
- An ARE editor/referee letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Unsure the field is mature/important enough to review for ARE | `arecon-topic-selection` |
| Need to get the topic in front of the Editorial Committee / accept an invitation | `arecon-proposal-framing` |
| Reading is unsystematic; citation gaps likely | `arecon-literature-synthesis` |
| Draft is a list of papers, not an argument about the field | `arecon-organizing-framework` |
| Conflicting findings; credibility of primary studies needs weighing | `arecon-evidence-standards` |
| Coverage, balance, or self-promotion concerns | `arecon-evidence-standards` (balance lens) |
| Need who-found-what tables or a conceptual framework figure | `arecon-tables-figures` |
| Prose is dense/jargon-laden; a non-specialist economist can't follow | `arecon-writing-style` |
| Working with the Annual Reviews production editor / Committee on scope | `arecon-editor-strategy` |
| Ready to deliver the commissioned draft; need a preflight | `arecon-submission` |
| Want to understand the Committee review cycle / timeline | `arecon-review-process` |
| Received editor/referee feedback on the review | `arecon-revision` |

## Default order

1. `arecon-topic-selection` — confirm the field is ARE-scale (mature, important, needs synthesis)
2. `arecon-proposal-framing` — get the topic to the Editorial Committee / shape the accepted invitation
3. `arecon-literature-synthesis` — gather and read the literature systematically
4. `arecon-organizing-framework` — impose the analytical spine
5. `arecon-evidence-standards` — appraise primary-study credibility; balance competing views
6. `arecon-tables-figures` — summary tables and the conceptual figure
7. `arecon-writing-style` — the authoritative-yet-accessible ARE voice (abstract + intro last)
8. `arecon-editor-strategy` — scope and the Committee/production relationship
9. `arecon-submission` — Annual Reviews delivery preflight
10. `arecon-review-process` — what the Committee review cycle looks like
11. `arecon-revision` — after the editor/referee letter

> `arecon-writing-style` is a late-stage polish; do not rewrite the intro before the organizing framework and evidence appraisal settle. The **invitation comes early** — ARE is commissioning-first, so `arecon-proposal-framing` precedes the heavy reading.

## Anti-patterns

- Treating ARE as a journal you submit to cold — it is **invitation-driven; unsolicited manuscripts are not accepted** (检索于 2026-06；以官网为准)
- Treating the review as an annotated bibliography (no framework) — the cardinal review-article failure
- Using the author's own line of work as the review's center of gravity (self-promotion)
- Importing primary-research instincts: there is no "identification" or "replication package" of your own — you **appraise** others' designs
- Confusing ARE with **JEL** (the AEA's in-depth survey of record, proposal/full-paper intake) or **JEP** (shorter, non-technical, broad audience), or with a **Handbook chapter**

## Routing by review archetype

A "review" is not one thing; the bottleneck differs by type. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| field-defining synthesis (broad subfield) | scope is enormous; needs a taxonomy | `arecon-organizing-framework` |
| methods/tool review (an estimator or modeling family) | accessibility to non-specialists; worked intuition | `arecon-writing-style` |
| empirical-evidence stocktake (what is the consensus?) | weighing conflicting results by credibility | `arecon-evidence-standards` |
| emerging-area review (young, fast-moving) | is it mature enough for an ARE volume yet? | `arecon-topic-selection` |

## Minimal decision snippet

```
if editor_or_referee_letter:        -> arecon-revision
elif ready_to_deliver_draft:        -> arecon-submission
elif prose_dense_or_inaccessible:   -> arecon-writing-style
elif need_tables_or_figures:        -> arecon-tables-figures
elif evidence_credibility_or_balance: -> arecon-evidence-standards
elif reads_like_a_list:             -> arecon-organizing-framework
elif reading_unsystematic:          -> arecon-literature-synthesis
elif no_invitation_yet:             -> arecon-proposal-framing
else:                               -> arecon-topic-selection
```
