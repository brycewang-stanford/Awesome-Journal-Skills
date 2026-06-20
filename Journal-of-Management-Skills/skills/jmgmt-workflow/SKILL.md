---
name: jmgmt-workflow
description: Use when deciding which jmgmt-* sub-skill to invoke next for a Journal of Management manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (jmgmt-workflow)

## Overview

This router sequences the twelve-skill stack for **Journal of Management (JOMgmt)**. The journal's center of gravity is management theory and empirical work across organizational behavior, strategy, HR, entrepreneurship, and research methods. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: SAGE for the Southern Management Association; submission route to re-check live: SAGE / ScholarOne submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at JOMgmt and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing JOMgmt with nearby venues: Academy of Management Journal, Strategic Management Journal, Organization Science, and Journal of Management Studies.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `jmgmt-topic-selection` |
| the management-theory contribution is underdeveloped | `jmgmt-theory-development` |
| the contribution relative to adjacent journals is fuzzy | `jmgmt-literature-positioning` |
| methods and construct validity need alignment | `jmgmt-methods` |
| analysis design, estimation, or qualitative coding needs review | `jmgmt-data-analysis` |
| the theoretical contribution needs sharper positioning | `jmgmt-contribution-framing` |
| exhibits are hard to read or do not answer the question | `jmgmt-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `jmgmt-writing-style` |
| the paper is close to submission and needs a final preflight | `jmgmt-submission` |
| review-cycle expectations and revision choreography need planning | `jmgmt-review-process` |
| a decision letter or referee report needs a response plan | `jmgmt-rebuttal` |

## Default order

`jmgmt-workflow → jmgmt-topic-selection → jmgmt-theory-development → jmgmt-literature-positioning → jmgmt-methods → jmgmt-data-analysis → jmgmt-contribution-framing → jmgmt-tables-figures → jmgmt-writing-style → jmgmt-submission → jmgmt-review-process → jmgmt-rebuttal`

## Journal-specific lenses
- Scope lens: management theory and empirical work across organizational behavior, strategy, HR, entrepreneurship, and research methods.
- Field vocabulary to keep visible: management theory contribution; multi-study design; construct validity; organizational mechanism; boundary conditions.
- Sibling boundary: Academy of Management Journal, Strategic Management Journal, Organization Science, and Journal of Management Studies.
- Writing standard: theory-driven management research with clean construct logic and robust empirical design.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating JOMgmt as interchangeable with Academy of Management Journal
- Treating JOMgmt as interchangeable with Strategic Management Journal
- Treating JOMgmt as interchangeable with Organization Science
- Using a generic top-five-economics or generic management template without the JOMgmt audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Journal of Management
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one jmgmt-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
