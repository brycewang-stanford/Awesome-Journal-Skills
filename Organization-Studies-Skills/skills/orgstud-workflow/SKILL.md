---
name: orgstud-workflow
description: Use when deciding which orgstud-* sub-skill to invoke next for a Organization Studies manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (orgstud-workflow)

## Overview

This router sequences the twelve-skill stack for **Organization Studies (OS)**. The journal's center of gravity is organization theory, institutional theory, critical management, qualitative research, and process studies. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: SAGE for EGOS; submission route to re-check live: SAGE / ScholarOne submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at OS and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing OS with nearby venues: Administrative Science Quarterly, Organization Science, Journal of Management Studies, and Academy of Management Review.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `orgstud-topic-selection` |
| the management-theory contribution is underdeveloped | `orgstud-theory-development` |
| the contribution relative to adjacent journals is fuzzy | `orgstud-literature-positioning` |
| methods and construct validity need alignment | `orgstud-methods` |
| analysis design, estimation, or qualitative coding needs review | `orgstud-data-analysis` |
| the theoretical contribution needs sharper positioning | `orgstud-contribution-framing` |
| exhibits are hard to read or do not answer the question | `orgstud-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `orgstud-writing-style` |
| the paper is close to submission and needs a final preflight | `orgstud-submission` |
| review-cycle expectations and revision choreography need planning | `orgstud-review-process` |
| a decision letter or referee report needs a response plan | `orgstud-rebuttal` |

## Default order

`orgstud-workflow → orgstud-topic-selection → orgstud-theory-development → orgstud-literature-positioning → orgstud-methods → orgstud-data-analysis → orgstud-contribution-framing → orgstud-tables-figures → orgstud-writing-style → orgstud-submission → orgstud-review-process → orgstud-rebuttal`

## Journal-specific lenses
- Scope lens: organization theory, institutional theory, critical management, qualitative research, and process studies.
- Field vocabulary to keep visible: institutional process; qualitative depth; organization theory; critical reflexivity; process temporality.
- Sibling boundary: Administrative Science Quarterly, Organization Science, Journal of Management Studies, and Academy of Management Review.
- Writing standard: organization-theory argument with careful positioning, reflexivity, and evidence-theory fit.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating OS as interchangeable with Administrative Science Quarterly
- Treating OS as interchangeable with Organization Science
- Treating OS as interchangeable with Journal of Management Studies
- Using a generic top-five-economics or generic management template without the OS audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Organization Studies
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one orgstud-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
