---
name: jmis-workflow
description: Use when deciding which jmis-* sub-skill to invoke next for a Journal of Management Information Systems manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (jmis-workflow)

## Overview

This router sequences the twelve-skill stack for **Journal of Management Information Systems (JMIS)**. The journal's center of gravity is information systems, digital transformation, platforms, analytics, IT governance, and organizational impacts of technology. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Taylor & Francis; submission route to re-check live: Taylor & Francis submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at JMIS and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing JMIS with nearby venues: MIS Quarterly, Information Systems Research, Journal of the AIS, and Management Science.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `jmis-topic-selection` |
| the management-theory contribution is underdeveloped | `jmis-theory-development` |
| the contribution relative to adjacent journals is fuzzy | `jmis-literature-positioning` |
| methods and construct validity need alignment | `jmis-methods` |
| analysis design, estimation, or qualitative coding needs review | `jmis-data-analysis` |
| the theoretical contribution needs sharper positioning | `jmis-contribution-framing` |
| exhibits are hard to read or do not answer the question | `jmis-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `jmis-writing-style` |
| the paper is close to submission and needs a final preflight | `jmis-submission` |
| review-cycle expectations and revision choreography need planning | `jmis-review-process` |
| a decision letter or referee report needs a response plan | `jmis-rebuttal` |

## Default order

`jmis-workflow → jmis-topic-selection → jmis-theory-development → jmis-literature-positioning → jmis-methods → jmis-data-analysis → jmis-contribution-framing → jmis-tables-figures → jmis-writing-style → jmis-submission → jmis-review-process → jmis-rebuttal`

## Journal-specific lenses
- Scope lens: information systems, digital transformation, platforms, analytics, IT governance, and organizational impacts of technology.
- Field vocabulary to keep visible: digital platform; IT governance; analytics adoption; information systems theory; organizational technology.
- Sibling boundary: MIS Quarterly, Information Systems Research, Journal of the AIS, and Management Science.
- Writing standard: IS scholarship that connects technology mechanisms to organizational and managerial outcomes.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating JMIS as interchangeable with MIS Quarterly
- Treating JMIS as interchangeable with Information Systems Research
- Treating JMIS as interchangeable with Journal of the AIS
- Using a generic top-five-economics or generic management template without the JMIS audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Journal of Management Information Systems
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one jmis-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
