---
name: jle-workflow
description: Use when deciding which jle-* sub-skill to invoke next for a The Journal of Law and Economics manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (jle-workflow)

## Overview

This router sequences the twelve-skill stack for **The Journal of Law and Economics (JLE)**. The journal's center of gravity is law and economics, regulation, property rights, contracts, liability, antitrust, and legal institutions. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: University of Chicago Press; submission route to re-check live: Chicago Journals online submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at JLE and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing JLE with nearby venues: Journal of Legal Studies, JLEO, American Law and Economics Review, and Journal of Public Economics.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `jle-topic-selection` |
| the contribution relative to adjacent journals is fuzzy | `jle-literature-positioning` |
| causal or structural credibility is the bottleneck | `jle-identification` |
| the model, mechanism, or conceptual frame is loose | `jle-theory-model` |
| results may be specification-, sample-, or inference-sensitive | `jle-robustness` |
| exhibits are hard to read or do not answer the question | `jle-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `jle-writing-style` |
| data, code, or computational documentation needs packaging | `jle-replication-package` |
| likely objections should be anticipated before submission | `jle-referee-strategy` |
| the paper is close to submission and needs a final preflight | `jle-submission` |
| a decision letter or referee report needs a response plan | `jle-rebuttal` |

## Default order

`jle-workflow → jle-topic-selection → jle-literature-positioning → jle-identification → jle-theory-model → jle-robustness → jle-tables-figures → jle-writing-style → jle-replication-package → jle-referee-strategy → jle-submission → jle-rebuttal`

## Journal-specific lenses
- Scope lens: law and economics, regulation, property rights, contracts, liability, antitrust, and legal institutions.
- Field vocabulary to keep visible: legal rule variation; institutional doctrine; contracting friction; regulatory incidence; court or statute design.
- Sibling boundary: Journal of Legal Studies, JLEO, American Law and Economics Review, and Journal of Public Economics.
- Writing standard: economics-first legal analysis that respects doctrine, timing, and institutional assignment.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating JLE as interchangeable with Journal of Legal Studies
- Treating JLE as interchangeable with JLEO
- Treating JLE as interchangeable with American Law and Economics Review
- Using a generic top-five-economics or generic management template without the JLE audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】The Journal of Law and Economics
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one jle-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
