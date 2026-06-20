---
name: jams-workflow
description: Use when deciding which jams-* sub-skill to invoke next for a Journal of the Academy of Marketing Science manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (jams-workflow)

## Overview

This router sequences the twelve-skill stack for **Journal of the Academy of Marketing Science (JAMS)**. The journal's center of gravity is marketing strategy, consumer behavior, channels, branding, innovation, and marketing theory. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Springer for the Academy of Marketing Science; submission route to re-check live: Springer Nature submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at JAMS and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing JAMS with nearby venues: Journal of Marketing, Journal of Marketing Research, Marketing Science, and Journal of Consumer Research.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `jams-topic-selection` |
| the management-theory contribution is underdeveloped | `jams-theory-development` |
| the contribution relative to adjacent journals is fuzzy | `jams-literature-positioning` |
| methods and construct validity need alignment | `jams-methods` |
| analysis design, estimation, or qualitative coding needs review | `jams-data-analysis` |
| the theoretical contribution needs sharper positioning | `jams-contribution-framing` |
| exhibits are hard to read or do not answer the question | `jams-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `jams-writing-style` |
| the paper is close to submission and needs a final preflight | `jams-submission` |
| review-cycle expectations and revision choreography need planning | `jams-review-process` |
| a decision letter or referee report needs a response plan | `jams-rebuttal` |

## Default order

`jams-workflow → jams-topic-selection → jams-theory-development → jams-literature-positioning → jams-methods → jams-data-analysis → jams-contribution-framing → jams-tables-figures → jams-writing-style → jams-submission → jams-review-process → jams-rebuttal`

## Journal-specific lenses
- Scope lens: marketing strategy, consumer behavior, channels, branding, innovation, and marketing theory.
- Field vocabulary to keep visible: marketing strategy; customer response; brand mechanism; managerial relevance; marketing theory.
- Sibling boundary: Journal of Marketing, Journal of Marketing Research, Marketing Science, and Journal of Consumer Research.
- Writing standard: marketing scholarship with clear managerial implications and theory contribution.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating JAMS as interchangeable with Journal of Marketing
- Treating JAMS as interchangeable with Journal of Marketing Research
- Treating JAMS as interchangeable with Marketing Science
- Using a generic top-five-economics or generic management template without the JAMS audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Journal of the Academy of Marketing Science
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one jams-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
