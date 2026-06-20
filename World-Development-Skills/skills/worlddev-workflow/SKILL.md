---
name: worlddev-workflow
description: Use when deciding which worlddev-* sub-skill to invoke next for a World Development manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (worlddev-workflow)

## Overview

This router sequences the twelve-skill stack for **World Development (World Development)**. The journal's center of gravity is development studies and development economics across poverty, institutions, sustainability, and policy implementation. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Elsevier; submission route to re-check live: Editorial Manager / Elsevier submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at World Development and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing World Development with nearby venues: Journal of Development Economics, World Bank Economic Review, Economic Development and Cultural Change, and World Development Perspectives.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `worlddev-topic-selection` |
| the contribution relative to adjacent journals is fuzzy | `worlddev-literature-positioning` |
| causal or structural credibility is the bottleneck | `worlddev-identification` |
| the model, mechanism, or conceptual frame is loose | `worlddev-theory-model` |
| results may be specification-, sample-, or inference-sensitive | `worlddev-robustness` |
| exhibits are hard to read or do not answer the question | `worlddev-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `worlddev-writing-style` |
| data, code, or computational documentation needs packaging | `worlddev-replication-package` |
| likely objections should be anticipated before submission | `worlddev-referee-strategy` |
| the paper is close to submission and needs a final preflight | `worlddev-submission` |
| a decision letter or referee report needs a response plan | `worlddev-rebuttal` |

## Default order

`worlddev-workflow → worlddev-topic-selection → worlddev-literature-positioning → worlddev-identification → worlddev-theory-model → worlddev-robustness → worlddev-tables-figures → worlddev-writing-style → worlddev-replication-package → worlddev-referee-strategy → worlddev-submission → worlddev-rebuttal`

## Journal-specific lenses
- Scope lens: development studies and development economics across poverty, institutions, sustainability, and policy implementation.
- Field vocabulary to keep visible: development intervention; local institution; poverty mechanism; implementation constraint; global-south relevance.
- Sibling boundary: Journal of Development Economics, World Bank Economic Review, Economic Development and Cultural Change, and World Development Perspectives.
- Writing standard: development evidence that connects identification to implementation, equity, and institutions.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating World Development as interchangeable with Journal of Development Economics
- Treating World Development as interchangeable with World Bank Economic Review
- Treating World Development as interchangeable with Economic Development and Cultural Change
- Using a generic top-five-economics or generic management template without the World Development audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】World Development
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one worlddev-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
