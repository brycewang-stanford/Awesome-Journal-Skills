---
name: jcp-workflow
description: Use when deciding which jcp-* sub-skill to invoke next for a Journal of Consumer Psychology manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (jcp-workflow)

## Overview

This router sequences the twelve-skill stack for **Journal of Consumer Psychology (JCP)**. The journal's center of gravity is consumer psychology, judgment and decision-making, persuasion, emotion, identity, and consumption behavior. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Elsevier for the Society for Consumer Psychology; submission route to re-check live: Editorial Manager / Elsevier submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at JCP and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing JCP with nearby venues: Journal of Consumer Research, Journal of Marketing Research, Marketing Science, and Psychological Science.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `jcp-topic-selection` |
| the management-theory contribution is underdeveloped | `jcp-theory-development` |
| the contribution relative to adjacent journals is fuzzy | `jcp-literature-positioning` |
| methods and construct validity need alignment | `jcp-methods` |
| analysis design, estimation, or qualitative coding needs review | `jcp-data-analysis` |
| the theoretical contribution needs sharper positioning | `jcp-contribution-framing` |
| exhibits are hard to read or do not answer the question | `jcp-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `jcp-writing-style` |
| the paper is close to submission and needs a final preflight | `jcp-submission` |
| review-cycle expectations and revision choreography need planning | `jcp-review-process` |
| a decision letter or referee report needs a response plan | `jcp-rebuttal` |

## Default order

`jcp-workflow → jcp-topic-selection → jcp-theory-development → jcp-literature-positioning → jcp-methods → jcp-data-analysis → jcp-contribution-framing → jcp-tables-figures → jcp-writing-style → jcp-submission → jcp-review-process → jcp-rebuttal`

## Journal-specific lenses
- Scope lens: consumer psychology, judgment and decision-making, persuasion, emotion, identity, and consumption behavior.
- Field vocabulary to keep visible: consumer mechanism; experimental manipulation; psychological process; moderation logic; consumer welfare.
- Sibling boundary: Journal of Consumer Research, Journal of Marketing Research, Marketing Science, and Psychological Science.
- Writing standard: psychological mechanism evidence tied to consumer behavior and marketing theory.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating JCP as interchangeable with Journal of Consumer Research
- Treating JCP as interchangeable with Journal of Marketing Research
- Treating JCP as interchangeable with Marketing Science
- Using a generic top-five-economics or generic management template without the JCP audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Journal of Consumer Psychology
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one jcp-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
