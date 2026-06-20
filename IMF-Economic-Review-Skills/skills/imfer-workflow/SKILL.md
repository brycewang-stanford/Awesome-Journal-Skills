---
name: imfer-workflow
description: Use when deciding which imfer-* sub-skill to invoke next for a IMF Economic Review manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (imfer-workflow)

## Overview

This router sequences the twelve-skill stack for **IMF Economic Review (IMFER)**. The journal's center of gravity is international macroeconomics, finance, development, policy, exchange rates, sovereign risk, and IMF-relevant evidence. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Springer Nature for the International Monetary Fund; submission route to re-check live: Springer Nature submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at IMFER and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing IMFER with nearby venues: Journal of International Economics, JIMF, JMCB, and Economic Policy.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `imfer-topic-selection` |
| the contribution relative to adjacent journals is fuzzy | `imfer-literature-positioning` |
| causal or structural credibility is the bottleneck | `imfer-identification` |
| the model, mechanism, or conceptual frame is loose | `imfer-theory-model` |
| results may be specification-, sample-, or inference-sensitive | `imfer-robustness` |
| exhibits are hard to read or do not answer the question | `imfer-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `imfer-writing-style` |
| data, code, or computational documentation needs packaging | `imfer-replication-package` |
| likely objections should be anticipated before submission | `imfer-referee-strategy` |
| the paper is close to submission and needs a final preflight | `imfer-submission` |
| a decision letter or referee report needs a response plan | `imfer-rebuttal` |

## Default order

`imfer-workflow → imfer-topic-selection → imfer-literature-positioning → imfer-identification → imfer-theory-model → imfer-robustness → imfer-tables-figures → imfer-writing-style → imfer-replication-package → imfer-referee-strategy → imfer-submission → imfer-rebuttal`

## Journal-specific lenses
- Scope lens: international macroeconomics, finance, development, policy, exchange rates, sovereign risk, and IMF-relevant evidence.
- Field vocabulary to keep visible: international macro; sovereign risk; capital-flow policy; IMF policy audience; macro-financial stability.
- Sibling boundary: Journal of International Economics, JIMF, JMCB, and Economic Policy.
- Writing standard: policy-facing international macro evidence with transparent country coverage and model assumptions.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating IMFER as interchangeable with Journal of International Economics
- Treating IMFER as interchangeable with JIMF
- Treating IMFER as interchangeable with JMCB
- Using a generic top-five-economics or generic management template without the IMFER audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】IMF Economic Review
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one imfer-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
