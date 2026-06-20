---
name: wber-workflow
description: Use when deciding which wber-* sub-skill to invoke next for a The World Bank Economic Review manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (wber-workflow)

## Overview

This router sequences the twelve-skill stack for **The World Bank Economic Review (WBER)**. The journal's center of gravity is policy-relevant development economics, impact evaluation, institutions, trade, labor, agriculture, and poverty. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Oxford University Press for the World Bank; submission route to re-check live: OUP / ScholarOne submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at WBER and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing WBER with nearby venues: Journal of Development Economics, World Development, Economic Development and Cultural Change, and AEJ Applied.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `wber-topic-selection` |
| the contribution relative to adjacent journals is fuzzy | `wber-literature-positioning` |
| causal or structural credibility is the bottleneck | `wber-identification` |
| the model, mechanism, or conceptual frame is loose | `wber-theory-model` |
| results may be specification-, sample-, or inference-sensitive | `wber-robustness` |
| exhibits are hard to read or do not answer the question | `wber-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `wber-writing-style` |
| data, code, or computational documentation needs packaging | `wber-replication-package` |
| likely objections should be anticipated before submission | `wber-referee-strategy` |
| the paper is close to submission and needs a final preflight | `wber-submission` |
| a decision letter or referee report needs a response plan | `wber-rebuttal` |

## Default order

`wber-workflow → wber-topic-selection → wber-literature-positioning → wber-identification → wber-theory-model → wber-robustness → wber-tables-figures → wber-writing-style → wber-replication-package → wber-referee-strategy → wber-submission → wber-rebuttal`

## Journal-specific lenses
- Scope lens: policy-relevant development economics, impact evaluation, institutions, trade, labor, agriculture, and poverty.
- Field vocabulary to keep visible: policy counterfactual; program evaluation; World Bank audience; developing-country data; implementation margin.
- Sibling boundary: Journal of Development Economics, World Development, Economic Development and Cultural Change, and AEJ Applied.
- Writing standard: development-policy evidence with transparent data construction and actionable interpretation.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating WBER as interchangeable with Journal of Development Economics
- Treating WBER as interchangeable with World Development
- Treating WBER as interchangeable with Economic Development and Cultural Change
- Using a generic top-five-economics or generic management template without the WBER audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】The World Bank Economic Review
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one wber-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
