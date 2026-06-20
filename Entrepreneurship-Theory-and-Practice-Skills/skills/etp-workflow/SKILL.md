---
name: etp-workflow
description: Use when deciding which etp-* sub-skill to invoke next for a Entrepreneurship Theory and Practice manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (etp-workflow)

## Overview

This router sequences the twelve-skill stack for **Entrepreneurship Theory and Practice (ETP)**. The journal's center of gravity is entrepreneurship theory, new ventures, founder teams, entrepreneurial finance, ecosystems, and family business. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: SAGE for Baylor University; submission route to re-check live: SAGE / ScholarOne submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at ETP and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing ETP with nearby venues: Journal of Business Venturing, Strategic Entrepreneurship Journal, Research Policy, and Academy of Management Journal.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `etp-topic-selection` |
| the management-theory contribution is underdeveloped | `etp-theory-development` |
| the contribution relative to adjacent journals is fuzzy | `etp-literature-positioning` |
| methods and construct validity need alignment | `etp-methods` |
| analysis design, estimation, or qualitative coding needs review | `etp-data-analysis` |
| the theoretical contribution needs sharper positioning | `etp-contribution-framing` |
| exhibits are hard to read or do not answer the question | `etp-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `etp-writing-style` |
| the paper is close to submission and needs a final preflight | `etp-submission` |
| review-cycle expectations and revision choreography need planning | `etp-review-process` |
| a decision letter or referee report needs a response plan | `etp-rebuttal` |

## Default order

`etp-workflow → etp-topic-selection → etp-theory-development → etp-literature-positioning → etp-methods → etp-data-analysis → etp-contribution-framing → etp-tables-figures → etp-writing-style → etp-submission → etp-review-process → etp-rebuttal`

## Journal-specific lenses
- Scope lens: entrepreneurship theory, new ventures, founder teams, entrepreneurial finance, ecosystems, and family business.
- Field vocabulary to keep visible: venture formation; founder team; entrepreneurial ecosystem; opportunity process; startup finance.
- Sibling boundary: Journal of Business Venturing, Strategic Entrepreneurship Journal, Research Policy, and Academy of Management Journal.
- Writing standard: entrepreneurship theory with credible venture-level evidence and boundary conditions.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating ETP as interchangeable with Journal of Business Venturing
- Treating ETP as interchangeable with Strategic Entrepreneurship Journal
- Treating ETP as interchangeable with Research Policy
- Using a generic top-five-economics or generic management template without the ETP audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Entrepreneurship Theory and Practice
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one etp-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
