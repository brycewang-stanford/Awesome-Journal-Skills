---
name: msom-workflow
description: Use when deciding which msom-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Manufacturing & Service Operations Management (M&SOM) manuscript. Routes — it does not replace — the specialized skills.
---

# Manufacturing & Service Operations Management Workflow (msom-workflow)

## Overview

This is the router. It does not replace any specialized skill; it tells you **which msom-* skill to use right now** for your M&SOM manuscript.

Default assumption: unless the user says otherwise, treat the target as M&SOM — the premier operations-management journal, published by INFORMS and sponsored by the MSOM Society, founded 1999 and published quarterly. M&SOM covers the **design, procurement, production, delivery, and recovery of goods and services**. The non-negotiable gate: an **operations decision or problem must be central to the contribution**, executed at top-tier rigor — whether the work is **analytical/stochastic** (optimization, queueing, stochastic models, game theory, revenue management) or **empirical OM / data-driven analytics**. A strong analytics, marketing, or finance-flavored paper is routinely desk-screened if the OM core is not the primary contribution. Submissions are routed by author-chosen **Department** (six of them) and two preferred Department Editors, so "fit" means matching the right department, not a generalist pool.

> Editorial team: Georgia Perakis (MIT Sloan) is listed as Editor-in-Chief on the 2026-06-20 M&SOM home and editorial-board pages; INFORMS announced that her final term expires 31 December 2026 and that the search committee aims to propose a successor by 1 July 2026. The M&SOM home page lists 2024 Impact Factor 4.2 and five-year Impact Factor 6.6. Check the masthead and editorial-board page before relying on current editor names.

## When to trigger

- "What should I do next?" with a half-built M&SOM manuscript
- You have a model or dataset but the operations decision is not yet the centerpiece
- A reviewer/DE pushes on "where is the operations contribution?" and you are unsure which stage is the bottleneck
- You received an M&SOM decision letter (R&R or reject) and need to switch into response mode
- You keep bouncing between model, analysis, and writing without a plan

## Routing table

| Current symptom                                                          | Next skill                   |
|--------------------------------------------------------------------------|------------------------------|
| Idea is vague; not sure an operations decision is central or M&SOM-fit   | `msom-topic-selection`       |
| Model/hypotheses lack a crisp operational mechanism or tradeoff          | `msom-theory-development`    |
| Front end reads as a gap; the OM conversation is not engaged             | `msom-literature-positioning`|
| Method/identification may not match the operations problem               | `msom-methods`               |
| Have proofs/numerics or data; unsure about rigor, replicability          | `msom-data-analysis`         |
| Results exist but the "managerial/operational so-what" is thin           | `msom-contribution-framing`  |
| Exhibits cluttered, off INFORMS style, or not self-explanatory           | `msom-tables-figures`        |
| Prose buries the operations insight; too much notation up front          | `msom-writing-style`         |
| Ready to submit; need the ScholarOne + department-routing preflight      | `msom-submission`            |
| Want to understand double-anonymous review and department routing        | `msom-review-process`        |
| Received an R&R; need to plan and draft the response                     | `msom-rebuttal`              |

## Default order

1. `msom-topic-selection` — lock an operations decision that is central and M&SOM-fit
2. `msom-theory-development` — build the model / operational mechanism and its tradeoff
3. `msom-literature-positioning` — engage the OM conversation and the right department
4. `msom-methods` — match the analytical/empirical method to the operations problem
5. `msom-data-analysis` — proofs, numerical studies, estimation, identification, replicability
6. `msom-contribution-framing` — turn results into an operational/managerial insight
7. `msom-tables-figures` — finalize exhibits in INFORMS house style
8. `msom-writing-style` — front-load the insight; control notation; structured abstract
9. `msom-submission` — ScholarOne preflight, anonymization, department routing
10. `msom-review-process` — set expectations for double-anonymous, department-routed review
11. `msom-rebuttal` — after an R&R, plan revisions then draft the response letter

> `msom-tables-figures` and `msom-writing-style` are **late-stage polish**. Do not invoke them while the model or identification is still unsettled.

## Difference vs. other OR/OM and management stacks

- **M&SOM**: an operations decision is central; analytical *or* empirical; INFORMS double-anonymous; 32-page typeset cap; ScholarOne at mc.manuscriptcentral.com/msom; author-routed departments.
- **Management Science (INFORMS)**: broader OR/management scope and an OM department, but not OM-exclusive; its author-facing fee policy differs from M&SOM's submission-guideline page.
- **Operations Research**: methodological OR contributions where the *method* can be the contribution; M&SOM insists the *operations problem* is.
- **POM (Production & Operations Management)**: overlapping OM scope, different society (POMS) and house style.

If an operations decision is not the centerpiece, M&SOM is the wrong venue.

## Router output snapshot

```
【Stage detected】topic / theory / positioning / methods / analysis / framing / exhibits / writing / submission / review / rebuttal
【Operations lever central?】yes / reshape (→ topic-selection)
【Lane】analytical / empirical
【Next skill】msom-...
【Live-check items】page cap, departments, masthead → author guidelines
```

## Anti-patterns

- **Do not** skip `msom-topic-selection` — a paper whose OM core is only a backdrop is desk-screened.
- **Do not** let `msom-tables-figures` beautify exhibits before the model/identification is settled.
- **Do not** let `msom-rebuttal` draft a response before you have actually revised the manuscript.
- **Do not** treat `msom-writing-style` as a substitute for a real operations contribution.
