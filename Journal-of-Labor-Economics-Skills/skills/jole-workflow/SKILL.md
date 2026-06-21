---
name: jole-workflow
description: Use when deciding which jole-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Journal of Labor Economics (JOLE) submission. Routes — it does not replace — the specialized skills.
---

# JOLE Workflow Router (jole-workflow)

## Overview

This is the router. It does not replace any specialized skill. It tells you **which jole-* skill to use at the current stage** of a manuscript aimed at the *Journal of Labor Economics*.

Default assumption: unless the user says otherwise, treat the target as JOLE — a general-interest, peer-reviewed **quarterly** in labor economics, published by the **University of Chicago Press** for the **Society of Labor Economists (SOLE)**. JOLE takes both theoretical and applied/empirical labor work (wages and earnings, employment, human capital and education, labor supply and demand, family economics, discrimination, unions, migration, institutions and policy). Operational tells that you are at JOLE and not a sibling journal: **Editor-in-Chief Peter Kuhn**, a **non-refundable submission fee** ($100 SOLE members / $175 non-members since July 1, 2018; decisions withheld until paid), **single-blind** review via **Editorial Manager** (so the manuscript is **NOT** anonymized — a title page names all co-authors), a **100-word abstract**, a **~20,000-word** soft cap counting each full-page table/figure as 500 words, **Chicago author-date** references ordered in-text chronologically then alphabetically, and deposit to the **JOLE Dataverse Repository** under the AER data policy. Before upload, live-check the portal path, fee prompts, editor conflicts, and data-policy wording from the official source map.

## When to trigger

- The user asks "what should I do next?"
- The user hands over a draft and needs the current bottleneck diagnosed
- Work is ping-ponging between empirics, framing, writing, and response letters
- A JOLE decision letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom                                                        | Next skill                          |
|------------------------------------------------------------------------|-------------------------------------|
| Question feels narrow / "so what for labor?" unclear                   | `jole-topic-selection`              |
| Contribution relative to the labor literature is fuzzy or undersold    | `jole-literature-positioning`       |
| Empirics rest on OLS + controls; causal claim is undefended            | `jole-identification-strategy`      |
| Estimation, sample construction, or robustness needs labor norms       | `jole-data-analysis`                |
| The "what's new for labor economics" pitch is not framed               | `jole-contribution-framing`         |
| Exhibits are dense and blow the 500-words-per-page budget              | `jole-tables-figures`               |
| Prose buries the idea; 100-word abstract / intro do not land           | `jole-writing-style`                |
| Accepted-stage data/code deposit to the JOLE Dataverse                 | `jole-replication-and-data-policy`  |
| Want to understand single-blind review, fee, and referee expectations  | `jole-review-process`               |
| Ready to submit via Editorial Manager; need a preflight checklist       | `jole-submission`                   |
| Received an R&R; need a response-letter strategy                       | `jole-rebuttal`                     |

## Default order

1. `jole-topic-selection` — lock a labor question that matters broadly
2. `jole-literature-positioning` — stake the contribution against the labor frontier
3. `jole-identification-strategy` — make the causal design credible
4. `jole-data-analysis` — execute estimation and robustness to labor norms
5. `jole-contribution-framing` — articulate what is new for labor economics
6. `jole-tables-figures` — finalize exhibits within the word economy
7. `jole-writing-style` — polish prose, the 100-word abstract, author-date cites (last)
8. `jole-replication-and-data-policy` — assemble the JOLE Dataverse deposit
9. `jole-review-process` — understand the single-blind process and pre-empt referees
10. `jole-submission` — Editorial Manager preflight (fee, title page, non-anonymized)
11. `jole-rebuttal` — after the R&R

> `jole-writing-style` is a late-stage polish. Do not rewrite the intro before identification is settled — the argument will change.

## Decision shortcuts

- "I have data but no labor angle" → `jole-topic-selection`
- "I don't know who I'm building on in labor" → `jole-literature-positioning`
- "My DID is TWFE on staggered minimum-wage timing" → `jole-identification-strategy`
- "My AKM firm effects may have limited-mobility bias" → `jole-data-analysis`
- "My result has no clear lesson for labor" → `jole-contribution-framing`
- "My main table has 12 columns and eats my word count" → `jole-tables-figures`
- "My abstract is 220 words" → `jole-writing-style`
- "Editor wants data and code on the Dataverse" → `jole-replication-and-data-policy`
- "Do I pay the fee, and is it double-blind?" → `jole-review-process`
- "Submitting tomorrow on Editorial Manager" → `jole-submission`
- "Got the referee reports" → `jole-rebuttal`

## Anti-patterns

- **Do not** anonymize the manuscript — JOLE is single-blind; that is `jole-submission`'s job to enforce
- **Do not** let `jole-tables-figures` polish exhibits while identification is still shaky
- **Do not** skip `jole-literature-positioning` and jump to identification — referees judge the labor contribution first
- **Do not** let `jole-rebuttal` draft a response letter before the revised manuscript exists
- **Do not** forget the submission fee blocks the decision — budget for it (see `jole-review-process`)
