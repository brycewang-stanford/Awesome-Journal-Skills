---
name: jms-workflow
description: Use when deciding which jms-* sub-skill to invoke next, or when sequencing manuscript work from topic through rebuttal for a Journal of Management Studies (JMS) submission. Routes — it does not replace — the specialized skills.
---

# JMS Workflow Router (jms-workflow)

## Overview

This is the router. It tells you **which jms-* skill to use at the current stage** of a manuscript aimed at the *Journal of Management Studies* (JMS) — the **Society for the Advancement of Management Studies (SAMS)** journal published by **Wiley**, an internationally oriented, European-rooted outlet for management and organization studies: strategy, organization theory, entrepreneurship, innovation, OB, and the broader study of management. JMS's defining trait is **methodological pluralism**: it publishes strong quantitative *and* strong qualitative / interpretive / process / theory-building work, plus **Point–CounterPoint** debates and **JMS Says** essays. What earns space is a genuine **theoretical contribution** engaged with an organizational phenomenon — the "so what for management theory and practice."

Default assumption: unless the user says otherwise, treat the target as JMS. Tells that you are at JMS and not a sibling: **double-blind review** with full anonymisation; **Harvard author-date** referencing; a typical length of **10,000–13,000 words inclusive of tables/figures/references**; submission via **ScholarOne (mc.manuscriptcentral.com/jmstudies)**; editorial office at **Durham University**; and a house culture that treats a rigorous qualitative case or process study as first-class rather than second-best. Mark volatile specifics `(检索于 2026-06；以官网为准)`.

## When to trigger

- The user asks "what should I do next?" on a JMS-bound paper
- A draft needs its current bottleneck diagnosed
- Work is ping-ponging between theory, design, evidence, framing, writing, and the response letter
- A JMS decision letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Topic feels narrow / not clearly a management-theory question | `jms-topic-selection` |
| The theoretical mechanism / propositions are thin or borrowed | `jms-theory-development` |
| Contribution vs. the conversation is fuzzy or oversold | `jms-literature-positioning` |
| Design (qual/quant/multi-method) does not fit the theory | `jms-methods` |
| Estimation, coding, or trustworthiness of the analysis is weak | `jms-data-analysis` |
| The "so what for theory & practice" is not sharp | `jms-contribution-framing` |
| Tables/figures (or a data structure / process figure) are dense | `jms-tables-figures` |
| Prose buries the idea; abstract/intro do not land | `jms-writing-style` |
| Anonymisation, Harvard refs, word count, portal preflight | `jms-submission` |
| Want to understand the developmental review timeline / desk-reject odds | `jms-review-process` |
| Received an R&R; need a response-letter strategy | `jms-rebuttal` |

## Default order

1. `jms-topic-selection` — lock a phenomenon-grounded management question
2. `jms-theory-development` — build the mechanism / propositions (or hypotheses)
3. `jms-literature-positioning` — stake the contribution to a live conversation
4. `jms-methods` — match design to the question (qual / quant / multi-method)
5. `jms-data-analysis` — estimation or qualitative trustworthiness
6. `jms-contribution-framing` — sharpen the "so what for theory & practice"
7. `jms-tables-figures` — exhibits, data tables, process / data-structure figures
8. `jms-writing-style` — make the idea land (abstract + intro last)
9. `jms-submission` — ScholarOne preflight (anonymisation, Harvard, word count)
10. `jms-review-process` — calibrate the developmental, multi-round culture
11. `jms-rebuttal` — after the R&R

> `jms-writing-style` is a late-stage polish; do not rewrite the intro before the theory and evidence settle. For qualitative work, theory and data co-evolve, so cycle 2↔4↔5 more than once.

## Routing by paper archetype

JMS spans four archetypes, and the binding constraint differs by archetype. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| qualitative / grounded theory-building (cases, ethnography) | data-to-construct transparency + theoretical model from data | `jms-theory-development` → `jms-methods` |
| process / longitudinal (how things unfold over time) | temporal bracketing, mechanism, narrative-to-theory | `jms-theory-development` → `jms-data-analysis` |
| quantitative hypothesis-testing (survey / archival) | endogeneity, CMB, a non-bald mechanism | `jms-methods` → `jms-data-analysis` |
| Point–CounterPoint / review essay / JMS Says | a contestable claim + a conversation worth moving | `jms-contribution-framing` → `jms-literature-positioning` |

## Worked routing example (illustrative)

A user says: "My inductive study of how family firms professionalise is rich, but a reviewer says the contribution is 'a nice description, not theory,' and the data structure is hard to follow." That is two JMS pushbacks — *no abstracted theoretical model* and *opaque data-to-theory chain* — owned by `jms-theory-development` (abstract the first-order codes into second-order themes and aggregate dimensions, then a process model) and `jms-tables-figures` (a Gioia-style data-structure figure plus a representative-quotes table). Route to theory first; only once the emergent model is crisp do you return to exhibits and `jms-contribution-framing`.

## Anti-patterns

- Treating JMS like **AMJ** (US hypothetico-deductive default), **Organization Studies** (more EGOS / process-theoretical), **Journal of Management** (SMA, US general/meta-analytic), or **SMJ** (strategy-economics) — JMS is the SAMS pluralist outlet that genuinely welcomes strong qualitative work
- Polishing prose before the theoretical contribution and evidence hierarchy are stable
- Forcing a qualitative study into a hypotheses-and-controls template, or judging it by quant criteria
- Letting an online appendix carry claims the 13,000-word main text must establish

## Output format

```text
【Target】Journal of Management Studies (JMS)
【Archetype】qualitative / process / quantitative / Point-CounterPoint
【Current bottleneck】topic / theory / positioning / design / evidence / framing / exhibits / style / submission / revision
【Next skill】<one jms-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
