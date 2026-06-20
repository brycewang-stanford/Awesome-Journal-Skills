---
name: jleo-workflow
description: Use when deciding which jleo-* sub-skill to invoke next for a Journal of Law, Economics, and Organization manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (jleo-workflow)

## Overview

This router sequences the twelve-skill stack for **Journal of Law, Economics, and Organization (JLEO)**. The journal's center of gravity is law, economics, and organization with emphasis on contracts, institutions, governance, and organizational design. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Oxford University Press; submission route to re-check live: OUP submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at JLEO and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing JLEO with nearby venues: Journal of Law and Economics, Journal of Legal Studies, Organization Science, and American Law and Economics Review.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `jleo-topic-selection` |
| the contribution relative to adjacent journals is fuzzy | `jleo-literature-positioning` |
| causal or structural credibility is the bottleneck | `jleo-identification` |
| the model, mechanism, or conceptual frame is loose | `jleo-theory-model` |
| results may be specification-, sample-, or inference-sensitive | `jleo-robustness` |
| exhibits are hard to read or do not answer the question | `jleo-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `jleo-writing-style` |
| data, code, or computational documentation needs packaging | `jleo-replication-package` |
| likely objections should be anticipated before submission | `jleo-referee-strategy` |
| the paper is close to submission and needs a final preflight | `jleo-submission` |
| a decision letter or referee report needs a response plan | `jleo-rebuttal` |

## Default order

`jleo-workflow → jleo-topic-selection → jleo-literature-positioning → jleo-identification → jleo-theory-model → jleo-robustness → jleo-tables-figures → jleo-writing-style → jleo-replication-package → jleo-referee-strategy → jleo-submission → jleo-rebuttal`

## Journal-specific lenses
- Scope lens: law, economics, and organization with emphasis on contracts, institutions, governance, and organizational design.
- Field vocabulary to keep visible: organizational governance; contracting institution; legal-economic mechanism; agency problem; institutional design.
- Sibling boundary: Journal of Law and Economics, Journal of Legal Studies, Organization Science, and American Law and Economics Review.
- Writing standard: institutional-economics argument that integrates legal rules, governance, and organizational mechanisms.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating JLEO as interchangeable with Journal of Law and Economics
- Treating JLEO as interchangeable with Journal of Legal Studies
- Treating JLEO as interchangeable with Organization Science
- Using a generic top-five-economics or generic management template without the JLEO audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Journal of Law, Economics, and Organization
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one jleo-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
