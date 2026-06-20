---
name: hrm-workflow
description: Use when deciding which hrm-* sub-skill to invoke next for a Human Resource Management manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (hrm-workflow)

## Overview

This router sequences the twelve-skill stack for **Human Resource Management (HRM)**. The journal's center of gravity is human resource management, talent, compensation, employment systems, workforce analytics, and HR strategy. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Wiley; submission route to re-check live: Wiley online submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at HRM and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing HRM with nearby venues: Personnel Psychology, Journal of Management, Human Relations, and Academy of Management Journal.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `hrm-topic-selection` |
| the management-theory contribution is underdeveloped | `hrm-theory-development` |
| the contribution relative to adjacent journals is fuzzy | `hrm-literature-positioning` |
| methods and construct validity need alignment | `hrm-methods` |
| analysis design, estimation, or qualitative coding needs review | `hrm-data-analysis` |
| the theoretical contribution needs sharper positioning | `hrm-contribution-framing` |
| exhibits are hard to read or do not answer the question | `hrm-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `hrm-writing-style` |
| the paper is close to submission and needs a final preflight | `hrm-submission` |
| review-cycle expectations and revision choreography need planning | `hrm-review-process` |
| a decision letter or referee report needs a response plan | `hrm-rebuttal` |

## Default order

`hrm-workflow → hrm-topic-selection → hrm-theory-development → hrm-literature-positioning → hrm-methods → hrm-data-analysis → hrm-contribution-framing → hrm-tables-figures → hrm-writing-style → hrm-submission → hrm-review-process → hrm-rebuttal`

## Journal-specific lenses
- Scope lens: human resource management, talent, compensation, employment systems, workforce analytics, and HR strategy.
- Field vocabulary to keep visible: HR system; talent architecture; employment relation; workforce analytics; strategic HR.
- Sibling boundary: Personnel Psychology, Journal of Management, Human Relations, and Academy of Management Journal.
- Writing standard: HR scholarship that connects people practices to organizational mechanisms and outcomes.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating HRM as interchangeable with Personnel Psychology
- Treating HRM as interchangeable with Journal of Management
- Treating HRM as interchangeable with Human Relations
- Using a generic top-five-economics or generic management template without the HRM audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Human Resource Management
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one hrm-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
