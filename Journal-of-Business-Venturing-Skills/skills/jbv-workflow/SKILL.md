---
name: jbv-workflow
description: Use when deciding which jbv-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Journal of Business Venturing (JBV) manuscript. Routes — it does not replace — the specialized skills.
---

# Journal of Business Venturing Workflow (jbv-workflow)

## Overview

This is the router. It does not replace any specialized skill; it tells you **which jbv-* skill to use right now** for your JBV manuscript.

Default assumption: unless the user says otherwise, treat the target as the **Journal of Business Venturing (JBV)** — an FT50 flagship in entrepreneurship and new venture creation, published by Elsevier (print ISSN 0883-9026, online ISSN 1873-2003). Current ScienceDirect metadata lists Sophie Bacq and Simon Parker as Co-Editors-in-Chief. JBV's defining bar is **phenomenon-driven**: a paper must illuminate the "entrepreneurial phenomenon in its myriad of forms" and advance theory about it. Entrepreneurship must be *central* to the contribution, not an incidental setting — this is what distinguishes JBV from general management journals that accept any well-identified organizational study. The journal is self-consciously **multidisciplinary** (grounded in economics, psychology, and sociology) and welcomes "theories, narratives, and interpretations," so reviewers ask "what new theory of entrepreneurship do we learn?" as insistently as "is the method sound?"

> Routing reality: manuscripts are routed through the current Co-EIC / area-editor structure. Review is **double-anonymized**. Verify the current masthead, Guide for Authors, APC, and metrics on ScienceDirect before author-facing advice.

## When to trigger

- "What should I do next?" with a half-built JBV manuscript
- You have venture data and a result but no clear entrepreneurship-theory story
- A reviewer or handling editor pushes on "is entrepreneurship really central?" and you are unsure which stage is the bottleneck
- You received a JBV decision letter (R&R or reject) and need to switch into response mode
- You keep bouncing between theory, method, and writing without a plan

## Routing table

| Current symptom                                                          | Next skill                  |
|--------------------------------------------------------------------------|-----------------------------|
| Idea is vague; unclear if entrepreneurship is central or JBV-fit         | `jbv-topic-selection`       |
| Mechanism is thin; no multidisciplinary theory of the phenomenon         | `jbv-theory-development`    |
| Front end reads as gap-spotting; the entrepreneurship conversation absent| `jbv-literature-positioning`|
| Design may not fit a venture-creation question (level, timing, selection)| `jbv-methods`               |
| Have data; unsure about survival/selection, attrition, endogeneity       | `jbv-data-analysis`         |
| Results exist but the "so what for entrepreneurship theory" is thin      | `jbv-contribution-framing`  |
| Tables/figures cluttered, off Elsevier style, or not self-explanatory    | `jbv-tables-figures`        |
| Prose buries the phenomenon; passive; jargon-heavy                       | `jbv-writing-style`         |
| Ready to submit; need the Editorial Manager preflight                    | `jbv-submission`            |
| Want to understand how JBV area-editor review works before/after submit  | `jbv-review-process`        |
| Received an R&R; need to plan and draft the response                     | `jbv-rebuttal`              |

## Default order

1. `jbv-topic-selection` — lock a phenomenon-driven question with JBV fit
2. `jbv-theory-development` — build a multidisciplinary mechanism; derive the argument
3. `jbv-literature-positioning` — engage the entrepreneurship conversation
4. `jbv-methods` — match design to the venture question (level, timing, selection)
5. `jbv-data-analysis` — survival/selection/panel, attrition, endogeneity, robustness
6. `jbv-contribution-framing` — turn results into a contribution to entrepreneurship theory
7. `jbv-tables-figures` — finalize main exhibits in Elsevier house style
8. `jbv-writing-style` — full-manuscript prose polish (phenomenon-forward, active voice)
9. `jbv-submission` — Editorial Manager preflight (anonymization, declarations, files)
10. `jbv-review-process` — set expectations for the area-editor / handling-editor, multi-round process
11. `jbv-rebuttal` — after an R&R, plan revisions then draft the response letter

> `jbv-tables-figures` and `jbv-writing-style` are **late-stage polish**. Do not invoke them while the entrepreneurial phenomenon, theory, or identification is still unsettled.

## Decision shortcuts

- "I have a finding but no entrepreneurship story" → `jbv-topic-selection` then `jbv-theory-development`
- "Reviewer says entrepreneurship is just the setting" → `jbv-topic-selection` / `jbv-contribution-framing`
- "My intro says 'no one has studied X in startups'" → `jbv-literature-positioning`
- "Venture-survival sample with heavy attrition" → `jbv-data-analysis`
- "Selection into founding may be endogenous" → `jbv-methods` then `jbv-data-analysis`
- "Submitting tomorrow" → `jbv-submission`
- "Got an R&R from a handling editor" → `jbv-review-process` then `jbv-rebuttal`

## Difference vs. general management / strategy stacks

- **JBV**: entrepreneurship/new venture creation must be central; multidisciplinary; welcomes narratives and interpretations; Elsevier Editorial Manager; double-anonymized; area-editor routing.
- **AMJ/AMR/ASQ/SMJ**: an entrepreneurship paper can fit those venues, but only JBV requires the *entrepreneurial phenomenon itself* to be the contribution. If entrepreneurship is incidental to your study, JBV is the wrong venue.

## Anti-patterns

- **Do not** treat entrepreneurship as a convenient empirical setting for a general theory.
- **Do not** let `jbv-tables-figures` beautify exhibits before the model and contribution settle.
- **Do not** let `jbv-rebuttal` draft a response before you have actually revised.
- **Do not** assume a single deductive template — JBV also rewards strong narrative/interpretive theorizing.

## Routing output

```
【Stage】topic | theory | positioning | methods | analysis | framing | exhibits | writing | submission | review
【Bottleneck】entrepreneurship central? mechanism? identification?
【Route】jbv-<skill>
```
