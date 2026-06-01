---
name: jcr-workflow
description: Use when deciding which jcr-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Journal of Consumer Research (JCR) manuscript. Routes — it does not replace — the specialized skills.
---

# Journal of Consumer Research Workflow (jcr-workflow)

## Overview

This is the router. It does not replace any specialized skill; it tells you **which jcr-* skill to use right now** for your JCR manuscript.

Default assumption: unless the user says otherwise, treat the target as JCR — the multi-disciplinary flagship of consumer behavior research, founded 1974 and published by Oxford University Press for Journal of Consumer Research, Inc. JCR's overriding criterion is **advancing understanding of consumer behavior or the conduct of consumer research**. It is explicitly interdisciplinary — psychology, anthropology, sociology, economics, marketing, statistics, communication — and its identity is institutionalized by a Policy Board of ~11 sponsoring professional societies. The non-negotiable bar is a clear **conceptual contribution** that advances, deepens, or repudiates existing theory about consumption, backed by appropriate empirical evidence. Two flagship genres coexist under one masthead: rigorous **multi-study behavioral experiments** and interpretive **Consumer Culture Theory (CCT)** work — JCR is one of the few top journals where ethnography and lab experiments compete on equal footing.

> Editorial team changes: Oleg Urminsky (Chicago Booth) is Editor in Chief for the term Jan 1, 2025 – Dec 31, 2028; the active co-editor roster is time-sensitive (待核实) — verify the current masthead at consumerresearcher.com. As of Jan 1, 2025 JCR also considers **Registered Reports** and **Brief Commentaries** beyond the standard empirical paper.

## When to trigger

- "What should I do next?" with a half-built JCR manuscript
- You have a robust effect but no clear conceptual story about consumption
- A reviewer/editor pushes on "contribution to consumer theory" and you are unsure which stage is the real bottleneck
- You received a JCR decision letter (R&R or reject) and need to switch into response mode
- You keep bouncing between theory, studies, and writing without a plan

## Routing table

| Current symptom                                                            | Next skill                  |
|----------------------------------------------------------------------------|-----------------------------|
| Idea is vague; not sure it is a consumer-behavior question or JCR-fit       | `jcr-topic-selection`       |
| Effect is real but there is no psychological/sociocultural mechanism        | `jcr-theory-development`    |
| Front end reads as gap-spotting; the consumer-research conversation is thin | `jcr-literature-positioning`|
| Unsure whether to run experiments, CCT fieldwork, or a mixed design         | `jcr-methods`               |
| Have studies; unsure about process evidence, mediation, robustness          | `jcr-data-analysis`         |
| Results exist but the conceptual "so what for consumer theory" is thin      | `jcr-contribution-framing`  |
| Tables/figures cluttered, off house style, or not self-explanatory          | `jcr-tables-figures`        |
| Prose buries the consumer insight or is jargon-heavy                        | `jcr-writing-style`         |
| Ready to submit; need the ScholarOne preflight + transparency apparatus     | `jcr-submission`            |
| Want to understand how JCR review/decisions work before/after submit        | `jcr-review-process`        |
| Received an R&R; need to plan and draft the response                        | `jcr-rebuttal`              |

## Default order

1. `jcr-topic-selection` — lock a consumer-behavior question with JCR fit
2. `jcr-theory-development` — build the psychological/sociocultural mechanism
3. `jcr-literature-positioning` — join the consumer-research conversation across disciplines
4. `jcr-methods` — choose experiments vs. CCT vs. mixed; design multi-study evidence
5. `jcr-data-analysis` — process evidence, mediation/moderation, interpretive trustworthiness
6. `jcr-contribution-framing` — write the conceptual contribution + Consumer Relevance Statement
7. `jcr-tables-figures` — finalize exhibits (study tables, process figures, interaction plots)
8. `jcr-writing-style` — front-load the consumer insight; Chicago house style
9. `jcr-submission` — ScholarOne preflight, anonymization, Data Collection Statement
10. `jcr-review-process` — set expectations for the developmental, multi-round process
11. `jcr-rebuttal` — after an R&R, plan revisions then draft the response letter

> `jcr-tables-figures` and `jcr-writing-style` are **late-stage polish**. Do not invoke them while the conceptual contribution or process story is still unsettled.

## Decision shortcuts

- "I have a cool effect but no theory" → `jcr-topic-selection` then `jcr-theory-development`
- "My intro says 'no one has studied X'" (gap-spotting) → `jcr-literature-positioning`
- "Reviewers will want process evidence" → `jcr-data-analysis` (mediation/moderation)
- "Is this an experiments paper or a CCT paper?" → `jcr-methods`
- "Reviewer says contribution is incremental" → `jcr-contribution-framing`
- "Submitting next week" → `jcr-submission` (60-page cap, Data Collection Statement)
- "Got an R&R" → `jcr-review-process` then `jcr-rebuttal`

## Difference vs. JM / JCP / JMR stacks

- **JCR**: the conceptual, multi-disciplinary flagship of consumer **behavior**; bar is a theory contribution about consumption; experiments and CCT compete on equal footing; OUP; 60-double-spaced-page cap; ScholarOne at mc.manuscriptcentral.com/jconres.
- **JCP (Journal of Consumer Psychology)**: psychology-focused, typically tighter behavioral process work.
- **JMR / JM (AMA journals)**: broader marketing scope including modeling, strategy, and managerial relevance, not exclusively consumer behavior.

If your paper is a managerial-strategy or analytical-modeling marketing paper with no real consumer-theory advance, JCR is the wrong venue.

## Anti-patterns

- **Do not** skip `jcr-theory-development` — JCR rejects atheoretical "interesting effects."
- **Do not** let `jcr-tables-figures` beautify exhibits before the conceptual contribution is settled.
- **Do not** treat the Consumer Relevance and Contribution Statement as an afterthought — it is a JCR-specific gate handled in `jcr-contribution-framing` / `jcr-submission`.
- **Do not** let `jcr-writing-style` substitute polish for a real contribution to consumer theory.
