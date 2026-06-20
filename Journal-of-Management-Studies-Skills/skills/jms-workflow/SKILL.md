---
name: jms-workflow
description: Use when deciding which jms-* sub-skill to invoke next for a Journal of Management Studies manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (jms-workflow)

## Overview

This router sequences the twelve-skill stack for **Journal of Management Studies (JMS)**. The journal's center of gravity is management and organization studies, strategy, entrepreneurship, innovation, OB, and critical perspectives. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Wiley for the Society for the Advancement of Management Studies; submission route to re-check live: Wiley online submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at JMS and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing JMS with nearby venues: Journal of Management, Organization Studies, AMJ, AMR, and Strategic Management Journal.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `jms-topic-selection` |
| the management-theory contribution is underdeveloped | `jms-theory-development` |
| the contribution relative to adjacent journals is fuzzy | `jms-literature-positioning` |
| methods and construct validity need alignment | `jms-methods` |
| analysis design, estimation, or qualitative coding needs review | `jms-data-analysis` |
| the theoretical contribution needs sharper positioning | `jms-contribution-framing` |
| exhibits are hard to read or do not answer the question | `jms-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `jms-writing-style` |
| the paper is close to submission and needs a final preflight | `jms-submission` |
| review-cycle expectations and revision choreography need planning | `jms-review-process` |
| a decision letter or referee report needs a response plan | `jms-rebuttal` |

## Default order

`jms-workflow → jms-topic-selection → jms-theory-development → jms-literature-positioning → jms-methods → jms-data-analysis → jms-contribution-framing → jms-tables-figures → jms-writing-style → jms-submission → jms-review-process → jms-rebuttal`

## Journal-specific lenses
- Scope lens: management and organization studies, strategy, entrepreneurship, innovation, OB, and critical perspectives.
- Field vocabulary to keep visible: theoretical pluralism; organization studies; critical boundary; international management; phenomenon-driven contribution.
- Sibling boundary: Journal of Management, Organization Studies, AMJ, AMR, and Strategic Management Journal.
- Writing standard: conceptually rich management scholarship that makes theory travel beyond one setting.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating JMS as interchangeable with Journal of Management
- Treating JMS as interchangeable with Organization Studies
- Treating JMS as interchangeable with AMJ
- Using a generic top-five-economics or generic management template without the JMS audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Journal of Management Studies
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one jms-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
