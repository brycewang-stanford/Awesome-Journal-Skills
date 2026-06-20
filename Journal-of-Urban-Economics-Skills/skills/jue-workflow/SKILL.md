---
name: jue-workflow
description: Use when deciding which jue-* sub-skill to invoke next for a Journal of Urban Economics manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (jue-workflow)

## Overview

This router sequences the twelve-skill stack for **Journal of Urban Economics (JUE)**. The journal's center of gravity is urban economics, spatial equilibrium, housing, transport, local public finance, and neighborhood sorting. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Elsevier; submission route to re-check live: Editorial Manager / Elsevier submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at JUE and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing JUE with nearby venues: Journal of Public Economics, Journal of Economic Geography, Regional Science and Urban Economics, and AEJ Applied.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `jue-topic-selection` |
| the contribution relative to adjacent journals is fuzzy | `jue-literature-positioning` |
| causal or structural credibility is the bottleneck | `jue-identification` |
| the model, mechanism, or conceptual frame is loose | `jue-theory-model` |
| results may be specification-, sample-, or inference-sensitive | `jue-robustness` |
| exhibits are hard to read or do not answer the question | `jue-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `jue-writing-style` |
| data, code, or computational documentation needs packaging | `jue-replication-package` |
| likely objections should be anticipated before submission | `jue-referee-strategy` |
| the paper is close to submission and needs a final preflight | `jue-submission` |
| a decision letter or referee report needs a response plan | `jue-rebuttal` |

## Default order

`jue-workflow → jue-topic-selection → jue-literature-positioning → jue-identification → jue-theory-model → jue-robustness → jue-tables-figures → jue-writing-style → jue-replication-package → jue-referee-strategy → jue-submission → jue-rebuttal`

## Journal-specific lenses
- Scope lens: urban economics, spatial equilibrium, housing, transport, local public finance, and neighborhood sorting.
- Field vocabulary to keep visible: spatial equilibrium; housing supply; commuting margin; local public goods; neighborhood sorting.
- Sibling boundary: Journal of Public Economics, Journal of Economic Geography, Regional Science and Urban Economics, and AEJ Applied.
- Writing standard: spatially grounded evidence with clear maps, mechanisms, and equilibrium caveats.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating JUE as interchangeable with Journal of Public Economics
- Treating JUE as interchangeable with Journal of Economic Geography
- Treating JUE as interchangeable with Regional Science and Urban Economics
- Using a generic top-five-economics or generic management template without the JUE audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Journal of Urban Economics
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one jue-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
