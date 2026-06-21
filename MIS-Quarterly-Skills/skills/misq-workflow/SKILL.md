---
name: misq-workflow
description: Use when deciding which misq-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through revision for a MIS Quarterly (MISQ) manuscript. Routes — it does not replace — the specialized skills, and it first helps you name which of the four IS research traditions (behavioral, design science, economics, organizational) your paper lives in.
---

# MIS Quarterly Workflow (misq-workflow)

## Overview

This is the router. It does not replace any specialized skill; it tells you **which misq-* skill to use right now** for your MIS Quarterly manuscript.

Default assumption: unless the user says otherwise, treat the target as **MIS Quarterly (MISQ)** — a leading information systems journal published by the MIS Research Center (MISRC), Carlson School of Management, University of Minnesota, and an official journal of the Association for Information Systems (AIS). It appears quarterly (March, June, September, December). MISQ is deliberately **pluralistic across four IS research traditions — behavioral, design science, economics, and organizational** — and rewards a rigorous theory contribution within any of them, including cross-tradition blends. So the first routing question is not "is the method sound?" but **"which tradition is this paper, and did the author pick the matching manuscript category?"**

> Editorial team and policies change: Susan A. (Sue) Brown (University of Arizona, Eller College of Management) is the 14th Editor-in-Chief (term began Jan 1, 2024; exact end date 待核实); verify the current masthead and the category page-limit table at misq.umn.edu. Treat any acceptance-rate or impact-factor figure as 待核实.

## When to trigger

- "What should I do next?" with a half-built MISQ manuscript
- You are unsure which IS tradition (and therefore which category/contribution mode) the paper belongs to
- You have built an IT artifact but no clear design-science evaluation or theory story
- A Senior Editor or reviewer pushes on contribution, transparency, or genre fit
- You received a MISQ decision (major/minor revision or reject) and need to switch into response mode

## Routing table

| Current symptom                                                              | Next skill                    |
|------------------------------------------------------------------------------|-------------------------------|
| Idea is vague; unsure of the tradition or whether it is a MISQ-fit IS question | `misq-topic-selection`        |
| Mechanism/design-theory/hypotheses are descriptive, not derived              | `misq-theory-development`     |
| Front end reads as gap-spotting; the IS conversation is not engaged          | `misq-literature-positioning` |
| Design/artifact-evaluation may not match the question or tradition           | `misq-methods`                |
| Have data/artifact output; unsure about validity, identification, evaluation | `misq-data-analysis`          |
| Results exist but the "so what for IS theory/practice" is thin               | `misq-contribution-framing`   |
| Tables/figures cluttered, off style, or eating the page limit                | `misq-tables-figures`         |
| Prose is jargon-heavy or buries the argument; APA-7/MISQ style off           | `misq-writing-style`          |
| Ready to submit; need the ScholarOne + transparency-commitment preflight     | `misq-submission`             |
| Want to understand the SE/AE double-anonymous process before/after submit    | `misq-review-process`         |
| Received a revision decision; need to plan and draft the response            | `misq-rebuttal`               |

## Default order

1. `misq-topic-selection` — name the tradition; lock an IS question and the matching category
2. `misq-theory-development` — build the mechanism / design theory and derive testable claims
3. `misq-literature-positioning` — join the IS conversation; engage canonical IS work
4. `misq-methods` — match design or build-and-evaluate strategy to the question and tradition
5. `misq-data-analysis` — validity, identification, or artifact evaluation done right
6. `misq-contribution-framing` — make the contribution explicit for IS theory and practice
7. `misq-tables-figures` — finalize exhibits within the page limit (which counts everything)
8. `misq-writing-style` — APA-7 / MISQ-style prose polish
9. `misq-submission` — ScholarOne preflight + pluralistic transparency commitment
10. `misq-review-process` — set expectations for the SE/AE double-anonymous process
11. `misq-rebuttal` — after a revision invite, plan revisions then draft the response

> `misq-tables-figures` and `misq-writing-style` are **late-stage polish**. Do not invoke them while the tradition, contribution, or identification/evaluation is still unsettled.

## Decision shortcuts

- "I built a tool/model but have no theory story" → `misq-topic-selection` then `misq-theory-development` (design-science track)
- "My intro says 'no one has studied X'" → `misq-literature-positioning`
- "Single-source, single-wave, self-report survey" → `misq-data-analysis` (common-method bias)
- "Archival IT event; treatment may be endogenous" → `misq-methods` then `misq-data-analysis`
- "Over the page limit / lots of supplementary files" → `misq-tables-figures` then `misq-submission`
- "Got a major revision with an SE letter" → `misq-review-process` then `misq-rebuttal`

## Anti-patterns

- **Do not** treat MISQ as a single-paradigm journal — picking the wrong category/tradition is a fit problem before it is a quality problem.
- **Do not** let `misq-tables-figures` beautify exhibits before the contribution and evaluation are settled.
- **Do not** plan supplementary appendices to dodge the page limit — supplementary materials are discouraged and the limit counts everything.
- **Do not** let `misq-rebuttal` draft a response before the manuscript is actually revised.
