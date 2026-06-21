---
name: psychrev-workflow
description: Use when deciding which psychrev-* sub-skill to invoke next, or when sequencing a theory or formal-model manuscript from problem framing through masked-review revision for a Psychological Review submission. Routes — does not replace — the specialized skills.
---

# Psychological Review Theory Workflow (psychrev-workflow)

## Overview

This is the router. It does not replace any specialized skill — it tells you **which
psychrev-* skill to use at the current stage** of a Psychological Review manuscript.

Default assumption: unless the user says otherwise, treat the target as Psychological
Review — the American Psychological Association's flagship for **theoretical
contributions** in scientific psychology. Per its scope it "publishes articles that make
important theoretical contributions to any area of scientific psychology, including
systematic evaluation of alternative theories"; papers "mainly focused on surveys of the
literature, problems of method and design, or reports of empirical findings are not
appropriate" (apa.org/pubs/journals/rev, 检索于 2026-06；以官网为准). The deliverable is a
new **theory** or **formal/computational model**, or a major theoretical synthesis — built
with explicit assumptions, derived predictions, and stated scope. There is **no primary
empirical report**: data appear only to *motivate* or *constrain* the theory, never as the
contribution. If the empirical work is the point, route to a JEP-family journal,
Psychological Science, or a specialty venue — not Psychological Review.

Two register choices run through every stage. First, this is **theory**, so logical and
formal soundness plays the role statistics play at empirical journals. Second, this is
**APA**, so the prose is plain, precise, and mechanism-first; the vocabulary is *model*,
*assumption*, *prediction*, *parameter*, *scope* — not "study," "we found," "p < .05."

## When to trigger

- The user asks "what should I do next?" on a theory or modeling paper
- A draft arrives and you must locate its bottleneck (problem? model? derivations?)
- Work is thrashing between modeling, figure-building, and writing
- A Psychological Review decision letter has arrived and the work shifts to revision

## Routing table

| Current symptom                                                       | Next skill                    |
|----------------------------------------------------------------------|-------------------------------|
| Idea is vague; unsure there is a real theoretical problem (or it is empirical) | `psychrev-topic-selection`    |
| Have a problem but the model's assumptions/mechanisms are not built   | `psychrev-theory-construction`|
| Unsure which theories you extend or which rivals you must beat        | `psychrev-literature-positioning`|
| Model exists but predictions are not derived or confronted with data  | `psychrev-argument-development`|
| Theory over-claims; scope, identifiability, and limits are unstated   | `psychrev-boundary-conditions`|
| Model diagram or simulation-of-behavior figure is missing/unreadable  | `psychrev-conceptual-exhibits`|
| Cannot articulate the advance over the prior model                    | `psychrev-contribution-framing`|
| Prose reads like a literature review, not a theoretical argument      | `psychrev-writing-style`      |
| Ready to submit; need the Editorial Manager preflight                 | `psychrev-submission`         |
| Want to understand masked review and Theoretical Notes                 | `psychrev-review-process`     |
| Received a revise decision; need the response document                | `psychrev-rebuttal`           |

## Default order

1. `psychrev-topic-selection` — lock the theoretical problem and confirm it is not empirical
2. `psychrev-literature-positioning` — name the theories you extend and the rivals you must beat
3. `psychrev-theory-construction` — build assumptions, mechanisms, formal structure, derivations
4. `psychrev-argument-development` — derive predictions; confront existing data and rival models
5. `psychrev-boundary-conditions` — state scope, identifiability, and what the theory does NOT explain
6. `psychrev-conceptual-exhibits` — model diagrams + simulation-of-model-behavior figures
7. `psychrev-contribution-framing` — differentiate the advance over prior models
8. `psychrev-writing-style` — APA house style; mechanism-first prose (polish)
9. `psychrev-submission` — Editorial Manager preflight (incl. author's own model code if computational)
10. `psychrev-review-process` — understand masked review and the decision types
11. `psychrev-rebuttal` — after a revise-and-resubmit

> `psychrev-writing-style` is a **late-stage polish**. Do not polish prose before the
> derivations stand up (`psychrev-argument-development`) and the contribution is
> differentiated (`psychrev-contribution-framing`).

## Decision shortcuts

- "I have a striking phenomenon but no model" → `psychrev-topic-selection`
- "I don't know which existing model I'm beating" → `psychrev-literature-positioning`
- "My model has assumptions but no derived predictions" → `psychrev-argument-development`
- "A reviewer will ask whether the model is identifiable" → `psychrev-boundary-conditions`
- "Reviewers will ask 'how is this better than [prior model]?'" → `psychrev-contribution-framing`
- "My figures are boxes, no simulated behavior" → `psychrev-conceptual-exhibits`
- "It reads like a review essay" → `psychrev-writing-style`
- "I'm about to hit submit" → `psychrev-submission`
- "I got a major revision" → `psychrev-review-process` then `psychrev-rebuttal`

## Differences vs. sibling journals

- **Psychological Bulletin**: integrative **reviews** and **meta-analyses** — synthesizes
  evidence; does not advance a new formal theory. If your contribution is "the field, summarized,"
  it is Bulletin, not Review.
- **Behavioral and Brain Sciences (BBS)**: a **target article + open peer commentary** format
  for cross-disciplinary debate; not the APA single-author/team theory paper.
- **Trends in Cognitive Sciences**: short, invited **opinion/review** pieces; not original formal theory.
- **JEP family / Psychological Science**: **empirical** reports — where data *is* the contribution.

## Anti-patterns

- **Do not** skip `psychrev-literature-positioning` — reviewers first ask which model you beat.
- **Do not** let `psychrev-conceptual-exhibits` render a model before its behavior is derived.
- **Do not** let `psychrev-rebuttal` draft a response before the theory itself was revised.
- **Do not** treat Psychological Review as a venue for empirical reports; route data papers elsewhere.

> Volatile specifics (editor, exact length/abstract limits, portal URL, fees, APA edition,
> acceptance rate) change or could not be machine-verified — see
> `resources/official-source-map.md` and confirm on the official APA Psychological Review page.
