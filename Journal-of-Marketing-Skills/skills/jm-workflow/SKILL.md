---
name: jm-workflow
description: Use when deciding which jm-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Journal of Marketing (JM) manuscript. Routes — it does not replace — the specialized skills.
---

# Journal of Marketing Workflow (jm-workflow)

## Overview

This is the router. It does not replace any specialized skill; it tells you **which jm-* skill to use right now** for your Journal of Marketing manuscript.

Default assumption: unless the user says otherwise, treat the target as JM — the American Marketing Association's (AMA) premier *general-audience* marketing journal, published by SAGE on the AMA's behalf. JM's mission is to develop and disseminate knowledge about **real-world marketing questions** useful to scholars, educators, managers, policy makers, consumers, and other societal stakeholders. Its gatekeeping criterion is publishing "the most impactful, thought-leading **substantive** research in the marketing discipline." The non-negotiable bar: a **substantive insight** into an important marketing question, with genuine **managerial, policy, or societal relevance** — not methodological novelty for its own sake. JM is methodologically "big tent" (experiments, field studies, surveys, interviews, observational, and secondary data) and actively promotes **empirics-first** research grounded in real-world phenomena.

> Editorial team: Editor in Chief Jan-Benedict E.M. Steenkamp (UNC Kenan-Flagler); Coeditors Marc Fischer (Cologne), Kelly L. Haws (Vanderbilt), Maura L. Scott (Arizona State), Rebecca J. Slotegraaf (Indiana). Verify the live masthead on the AMA editorial-leadership page before naming conflicts or suggesting opposed reviewers.

## When to trigger

- "What should I do next?" with a half-built JM manuscript
- You have results but the managerial/societal "so what" is thin
- A reviewer/editor questions whether the contribution is *substantive* or merely a new-context replication
- You received a JM decision letter (R&R or reject) and need to switch into response mode
- You keep bouncing between phenomenon, theory, method, and writing without a plan

## Routing table

| Current symptom                                                          | Next skill                  |
|--------------------------------------------------------------------------|-----------------------------|
| Idea is vague; not sure it is substantive or JM-fit (vs. JMR / Mktg Sci) | `jm-topic-selection`        |
| Phenomenon is real but the conceptual logic is underdeveloped            | `jm-theory-development`     |
| Front end reads as gap-spotting; substantive conversation not engaged    | `jm-literature-positioning` |
| Design may not match the question (causality, field realism, level)      | `jm-methods`                |
| Have data; unsure about identification, exact-statistic reporting, replication | `jm-data-analysis`     |
| Results exist but managerial/policy/societal relevance is thin           | `jm-contribution-framing`   |
| Tables/figures cluttered or lack a managerial takeaway                   | `jm-tables-figures`         |
| Prose buries the substantive argument; off AMA house style               | `jm-writing-style`          |
| Ready to submit; need the ScholarOne (Sage Track) preflight              | `jm-submission`             |
| Want to understand how JM double-anonymized review works                 | `jm-review-process`         |
| Received an R&R; need to plan and draft the response                     | `jm-rebuttal`               |

## Default order

1. `jm-topic-selection` — lock a substantive, managerially relevant question with JM fit
2. `jm-theory-development` — build conceptual logic grounded in the real-world phenomenon
3. `jm-literature-positioning` — engage the substantive conversation; avoid new-context incrementalism
4. `jm-methods` — match design (experiment / field / survey / secondary / qualitative) to the question
5. `jm-data-analysis` — identification, exact p-values/SEs/effect sizes, JM Dataverse replication
6. `jm-contribution-framing` — turn results into a substantive + managerial/policy/societal contribution
7. `jm-tables-figures` — finalize exhibits with managerial takeaways in AMA style
8. `jm-writing-style` — full-manuscript prose polish (front-loaded substantive argument)
9. `jm-submission` — ScholarOne (Sage Track) preflight (anonymization, 50-page format, files)
10. `jm-review-process` — set expectations for double-anonymized, multi-round review
11. `jm-rebuttal` — after an R&R, plan revisions then draft the response letter

> `jm-tables-figures` and `jm-writing-style` are **late-stage polish**. Do not invoke them while the substantive contribution or identification is still unsettled.

## Decision shortcuts

- "I have a finding but no managerial story" → `jm-topic-selection` then `jm-contribution-framing`
- "My intro says 'no one has studied X in this context'" → `jm-literature-positioning`
- "Reviewer says it's a new-context replication" → `jm-contribution-framing` (substantive novelty)
- "My paper is mostly a clever model" → reconsider fit (Marketing Science / JMR), then `jm-topic-selection`
- "I reported p < .05" → `jm-data-analysis` (exact p-values, SEs, effect sizes)
- "Conditional acceptance — what do I deposit?" → `jm-submission` / `jm-data-analysis` (JM Dataverse packet)
- "Got an R&R" → `jm-review-process` then `jm-rebuttal`

## Difference vs. JMR / Marketing Science / JCR stacks

- **JM**: substantive insight into real-world marketing questions *with managerial/policy/societal relevance*; "big tent" empirics-first; AMA/SAGE; 50-page inclusive limit; ScholarOne at mc.manuscriptcentral.com/ama_jm.
- **JMR** (AMA/SAGE sister journal): methods-forward empirical rigor — measurement, models, methods; route quant-methods-driven work here.
- **Marketing Science** (INFORMS): analytical, game-theoretic, and structural modeling — route modeling-for-its-own-sake here.
- **JCR** (Oxford UP / ACR): interdisciplinary consumer-behavior theory.

If your paper centers on a modeling/methods advance rather than a substantive marketing insight, JM is the wrong venue.

## Anti-patterns

- **Do not** skip `jm-contribution-framing` — JM rejects work with no managerial/societal relevance.
- **Do not** dress up a new-context replication as a contribution.
- **Do not** let complex analysis substitute for an important, substantive question.
- **Do not** let `jm-rebuttal` draft a response letter before the manuscript is actually revised.
