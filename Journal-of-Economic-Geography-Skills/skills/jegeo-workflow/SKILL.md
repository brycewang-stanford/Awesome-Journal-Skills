---
name: jegeo-workflow
description: Use when deciding which jegeo-* sub-skill to invoke next for a Journal of Economic Geography manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (jegeo-workflow)

## Overview

This router sequences the twelve-skill stack for **Journal of Economic Geography (JEG)**. The journal's center of gravity is economic geography, spatial economics, regional development, innovation clusters, trade, and place-based policy. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Oxford University Press; submission route to re-check live: OUP / ScholarOne submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at JEG and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing JEG with nearby venues: Journal of Urban Economics, Regional Studies, Economic Geography, and Journal of International Economics.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `jegeo-topic-selection` |
| the contribution relative to adjacent journals is fuzzy | `jegeo-literature-positioning` |
| causal or structural credibility is the bottleneck | `jegeo-identification` |
| the model, mechanism, or conceptual frame is loose | `jegeo-theory-model` |
| results may be specification-, sample-, or inference-sensitive | `jegeo-robustness` |
| exhibits are hard to read or do not answer the question | `jegeo-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `jegeo-writing-style` |
| data, code, or computational documentation needs packaging | `jegeo-replication-package` |
| likely objections should be anticipated before submission | `jegeo-referee-strategy` |
| the paper is close to submission and needs a final preflight | `jegeo-submission` |
| a decision letter or referee report needs a response plan | `jegeo-rebuttal` |

## Default order

`jegeo-workflow → jegeo-topic-selection → jegeo-literature-positioning → jegeo-identification → jegeo-theory-model → jegeo-robustness → jegeo-tables-figures → jegeo-writing-style → jegeo-replication-package → jegeo-referee-strategy → jegeo-submission → jegeo-rebuttal`

## Journal-specific lenses
- Scope lens: economic geography, spatial economics, regional development, innovation clusters, trade, and place-based policy.
- Field vocabulary to keep visible: spatial clustering; regional divergence; place-based policy; network geography; innovation ecosystem.
- Sibling boundary: Journal of Urban Economics, Regional Studies, Economic Geography, and Journal of International Economics.
- Writing standard: spatial economic argument that combines maps, mechanisms, and regional theory.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating JEG as interchangeable with Journal of Urban Economics
- Treating JEG as interchangeable with Regional Studies
- Treating JEG as interchangeable with Economic Geography
- Using a generic top-five-economics or generic management template without the JEG audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Journal of Economic Geography
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one jegeo-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
