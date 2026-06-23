---
name: smj-workflow
description: Use when deciding which smj-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Strategic Management Journal (SMJ) manuscript. Routes — it does not replace — the specialized skills.
---

# Strategic Management Journal Workflow (smj-workflow)

## Overview

This is the router. It does not do the work of any specialized skill — it tells you **which smj-* skill to use right now** given where your manuscript stands.

Default assumption: unless you say otherwise, the target is the **Strategic Management Journal (SMJ)** — the flagship strategy journal published by Wiley for the Strategic Management Society (SMS), founded 1980 and led by four **Co-Editors** (current slate, pinned 2026-06-23: Agarwal, Benner, Gaba, and Silverman; roster rotates, so verify the live SMS masthead). SMJ wants a clear contribution to **strategy theory** (firm performance, competitive advantage) backed by rigorous, identification-aware empirics. It is highly selective (third-party estimates ~7% acceptance — UNVERIFIED), uses **double-blind** review, and requires **two abstracts** (research summary + managerial summary, ≤125 words each), **five keywords**, and **APA** references within a ~40-page budget. Generic "management" framing and unaddressed endogeneity are the two fastest paths to rejection. If the paper's engine is entrepreneurship or internationalization, the SMS siblings **SEJ** or **GSJ** may fit better than SMJ.

## When to trigger

- "What should I do next?" on an SMJ-targeted paper
- You have a draft and need to find the binding constraint
- You keep bouncing between theory, methods, and writing without a plan
- You received SMJ reviewer comments and need to switch into revision mode

## Routing table

| Current symptom                                                        | Next skill                  |
|------------------------------------------------------------------------|-----------------------------|
| Idea is vague; unsure it is a *strategy* question (performance / advantage) | `smj-topic-selection`       |
| Hypotheses are atheoretical or read as "predictions," not theory       | `smj-theory-development`    |
| Lit review is a list; no positioning against the strategy conversation | `smj-literature-positioning`|
| Design unclear: sample, unit of analysis, measures, identification     | `smj-methods`               |
| Performance regression with no endogeneity / reverse-causality fix     | `smj-data-analysis`         |
| Reviewers may ask "so what for strategy?"; contribution is thin        | `smj-contribution-framing`  |
| Too many tables; exhibits not self-contained; no path/effect figure    | `smj-tables-figures`        |
| Prose is jargon-heavy, hedged, or buries the argument                  | `smj-writing-style`         |
| Ready to submit; need preflight (dual abstracts, 5 keywords, APA, format) | `smj-submission`            |
| Want to understand the review timeline / action-editor process         | `smj-review-process`        |
| Received an R&R; need a response strategy and letter                    | `smj-rebuttal`              |

## Default order

1. `smj-topic-selection` — lock the strategy question (performance / competitive advantage)
2. `smj-theory-development` — build the theoretical mechanism and hypotheses
3. `smj-literature-positioning` — position against the live strategy conversation
4. `smj-methods` — sample, unit of analysis, measures, identification design
5. `smj-data-analysis` — estimate, and explicitly defeat endogeneity / selection / reverse causality
6. `smj-contribution-framing` — sharpen the contribution to strategy theory
7. `smj-tables-figures` — finalize self-contained exhibits
8. `smj-writing-style` — full-draft polish (do this late)
9. `smj-submission` — preflight (dual abstracts, 5 keywords, APA, page budget, anonymization)
10. `smj-review-process` — understand what happens after submission (Co-Editor screen → action editor)
11. `smj-rebuttal` — after the R&R decision

> `smj-writing-style` is a **late-stage polish**. Do not polish prose while the identification strategy or the theoretical contribution is still unsettled.

## Decision heuristics

- "I have data but no strategy story" → `smj-topic-selection`
- "My hypotheses are just signed correlations" → `smj-theory-development`
- "My intro never names whose conversation I'm joining" → `smj-literature-positioning`
- "My DV is firm performance and my X is a strategic choice" → `smj-data-analysis` (selection into the choice is the #1 threat)
- "A reviewer could say 'this is management, not strategy'" → `smj-contribution-framing`
- "I have nine tables" → `smj-tables-figures`
- "I submit tomorrow" → `smj-submission`
- "I got a Major Revision" → `smj-review-process` then `smj-rebuttal`

## Differences vs. AMJ / ASQ / AMR stacks

If the paper's center of gravity is general organizational behavior, HRM, or micro-OB, the [Academy of Management Journal](https://github.com/brycewang-stanford/amj-skills) stack fits better. If the contribution is purely conceptual with no data, use an [AMR](https://github.com/brycewang-stanford/amr-skills) theory-only stack. SMJ's distinctive bar: the dependent construct should connect to **firm performance or competitive advantage**, and the empirics must survive an **endogeneity** interrogation.

## Anti-patterns

- **Do not** skip `smj-theory-development` and jump to estimation — SMJ reviewers read theory first.
- **Do not** let `smj-tables-figures` polish exhibits before the identification strategy holds.
- **Do not** let `smj-rebuttal` draft a response letter before you have actually revised the manuscript.
- **Do not** treat this as a generic management workflow; every stage must reconnect to strategy.
- **Do not** forget SMJ's dual-abstract / 5-keyword / APA requirements until submission day, or route an SEJ/GSJ-shaped paper to SMJ.

## Templates & resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — SMJ scope, Co-Editors, dual-abstract/keyword/reference rules, and the SMS journal family
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — strategy data sources and analysis packages across the pipeline
