---
name: orgsci-workflow
description: Use when deciding which orgsci-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for an Organization Science manuscript. Routes — it does not replace — the specialized skills.
---

# Organization Science Workflow (orgsci-workflow)

## Overview

This is the router. It does not replace any specialized skill; it tells you **which orgsci-* skill to use right now** for your Organization Science manuscript.

Default assumption: unless told otherwise, treat the target as Organization Science — the interdisciplinary, theory-driven INFORMS journal about organizations (their processes, structures, technologies, identities, capabilities, forms, and performance) spanning **micro (individual/team) to macro (organizational/field/population)** levels. Its defining bar is **overall contribution**: the editorial statement holds that "theoretical novelty is neither necessary nor sufficient," and contributions may come from new theory, data, method, settings, mechanisms, or social-problem/grand-challenge relevance. It is methodologically eclectic, with a signature openness to **qualitative and inductive** work alongside quantitative, experimental, computational, and formal-analytical research; causal inference is valued but "not necessary and often impossible."

> Time-sensitive items: Lamar Pierce (Washington University in St. Louis) is Editor-in-Chief (oseic@wustl.edu); verify the masthead at pubsonline.informs.org/journal/orsc. A mandatory **<500-word contribution statement** in the cover letter has been required since June 1, 2023.

## When to trigger

- "What should I do next?" with a half-built Organization Science manuscript
- You have inductive field data or a model but no sharpened theoretical contribution
- A senior editor pushes on "what is the contribution to organization research?"
- You received a decision letter and need to switch into response mode
- You keep bouncing between theory, method, and writing without a plan

## Routing table

| Current symptom                                                          | Next skill                     |
|--------------------------------------------------------------------------|--------------------------------|
| Idea is vague; unsure it fits Organization Science (vs. ASQ/AMJ/Mgmt Sci)| `orgsci-topic-selection`       |
| Theory is thin; mechanism across levels not articulated                  | `orgsci-theory-development`    |
| Front end reads as gap-spotting; not joining an organization-theory conversation | `orgsci-literature-positioning`|
| Design (qualitative/quant/experiment/computational/formal) may not fit   | `orgsci-methods`               |
| Have data/model output; unsure how to analyze and report it credibly     | `orgsci-data-analysis`         |
| Results exist but the contribution statement is weak                     | `orgsci-contribution-framing`  |
| Tables/figures or a process model are cluttered or off house style       | `orgsci-tables-figures`        |
| Prose buries the argument; not in INFORMS author-date style              | `orgsci-writing-style`         |
| Ready to submit; need the ScholarOne + length-policy preflight           | `orgsci-submission`            |
| Want to understand the decentralized senior-editor review process        | `orgsci-review-process`        |
| Received an R&R; need to plan and draft the response                      | `orgsci-rebuttal`              |

## Default order

1. `orgsci-topic-selection` — lock a theory-driven question with Organization Science fit
2. `orgsci-theory-development` — build the cross-level mechanism / inductive grounded model
3. `orgsci-literature-positioning` — join an organization-theory conversation
4. `orgsci-methods` — match design to the question and level of analysis
5. `orgsci-data-analysis` — analyze and report transparently (including trustworthiness for qualitative work)
6. `orgsci-contribution-framing` — draft the mandatory <500-word contribution statement
7. `orgsci-tables-figures` — finalize exhibits / data structure / process model
8. `orgsci-writing-style` — prose polish in INFORMS author-date style
9. `orgsci-submission` — ScholarOne preflight (anonymization, ~50-page norm, separate appendix)
10. `orgsci-review-process` — set expectations for the decentralized senior-editor process
11. `orgsci-rebuttal` — after an R&R, plan revisions then draft the response letter

> `orgsci-tables-figures` and `orgsci-writing-style` are **late-stage polish**. Do not invoke them while the theoretical contribution is still unsettled.

## Decision shortcuts

- "I have rich field data but no theory yet" → `orgsci-topic-selection` then `orgsci-theory-development`
- "My intro says 'no one has studied X'" → `orgsci-literature-positioning`
- "An editor said 'interesting but not enough contribution'" → `orgsci-contribution-framing`
- "Reviewer wants causal identification I cannot get" → `orgsci-methods` then `orgsci-data-analysis` (mechanism + design logic over identification)
- "Submitting next week" → `orgsci-submission`
- "Got an R&R from one senior editor and two reviewers" → `orgsci-review-process` then `orgsci-rebuttal`

## Difference vs. ASQ / AMJ / Management Science stacks

- **Organization Science**: interdisciplinary, theory-driven organizations research, micro to macro; eclectic methods with a qualitative/inductive signature; overall contribution over novelty; decentralized senior-editor model; INFORMS / ScholarOne at mc.manuscriptcentral.com/orsc.
- **ASQ**: Cornell/SAGE; deep contextual/qualitative work and bold framing, but not the INFORMS venue.
- **AMJ**: AOM empirical journal; equal empirical + theoretical bar, page limit, AOM house style.
- **Management Science**: INFORMS sibling; departmental area-editor routing and a code-and-data disclosure mandate Organization Science does not impose.

## Anti-patterns

- **Do not** chase causal identification at the expense of the contribution — this venue does not require it.
- **Do not** skip the contribution statement; submissions without it are returned before review.
- **Do not** treat polish as a substitute for an organization-theory contribution.
