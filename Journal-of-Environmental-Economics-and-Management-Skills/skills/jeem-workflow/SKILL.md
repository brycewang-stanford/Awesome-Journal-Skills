---
name: jeem-workflow
description: Use when deciding which jeem-* sub-skill to invoke next for a Journal of Environmental Economics and Management manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (jeem-workflow)

## Overview

This router sequences the twelve-skill stack for **Journal of Environmental Economics and Management (JEEM)**. The journal's center of gravity is environmental economics, resource economics, climate policy, regulation, valuation, and natural-resource management. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Elsevier; submission route to re-check live: Editorial Manager / Elsevier submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at JEEM and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing JEEM with nearby venues: Review of Environmental Economics and Policy, AEJ Economic Policy, Journal of Public Economics, and Nature Climate Change.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `jeem-topic-selection` |
| the contribution relative to adjacent journals is fuzzy | `jeem-literature-positioning` |
| causal or structural credibility is the bottleneck | `jeem-identification` |
| the model, mechanism, or conceptual frame is loose | `jeem-theory-model` |
| results may be specification-, sample-, or inference-sensitive | `jeem-robustness` |
| exhibits are hard to read or do not answer the question | `jeem-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `jeem-writing-style` |
| data, code, or computational documentation needs packaging | `jeem-replication-package` |
| likely objections should be anticipated before submission | `jeem-referee-strategy` |
| the paper is close to submission and needs a final preflight | `jeem-submission` |
| a decision letter or referee report needs a response plan | `jeem-rebuttal` |

## Default order

`jeem-workflow → jeem-topic-selection → jeem-literature-positioning → jeem-identification → jeem-theory-model → jeem-robustness → jeem-tables-figures → jeem-writing-style → jeem-replication-package → jeem-referee-strategy → jeem-submission → jeem-rebuttal`

## Journal-specific lenses
- Scope lens: environmental economics, resource economics, climate policy, regulation, valuation, and natural-resource management.
- Field vocabulary to keep visible: environmental externality; regulatory design; valuation evidence; climate adaptation; resource management.
- Sibling boundary: Review of Environmental Economics and Policy, AEJ Economic Policy, Journal of Public Economics, and Nature Climate Change.
- Writing standard: economic identification linked to environmental mechanisms and policy welfare.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating JEEM as interchangeable with Review of Environmental Economics and Policy
- Treating JEEM as interchangeable with AEJ Economic Policy
- Treating JEEM as interchangeable with Journal of Public Economics
- Using a generic top-five-economics or generic management template without the JEEM audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Journal of Environmental Economics and Management
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one jeem-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
