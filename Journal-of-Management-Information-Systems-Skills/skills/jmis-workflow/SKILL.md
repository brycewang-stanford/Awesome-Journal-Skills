---
name: jmis-workflow
description: Use when deciding which jmis-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Journal of Management Information Systems (JMIS) submission. Routes — it does not replace — the specialized skills. Knows JMIS's management-and-economics-of-IS identity and its email-to-EIC, double-anonymized process.
---

# JMIS Workflow Router (jmis-workflow)

## Overview

This is the router. It tells you **which jmis-* skill to use at the current stage** of a manuscript aimed at the *Journal of Management Information Systems* (JMIS) — the Taylor & Francis (Routledge) quarterly founded in 1984 and edited since its founding by **Vladimir Zwass** (Fairleigh Dickinson University). JMIS is one of the IS field's "Senior Scholars' basket" top journals, but it has a distinctive center of gravity: the **management and economics of information systems and technology** — IS strategy and IT business value, e-commerce and digital platforms, IT economics, decision support and business analytics, the economics of security and privacy, and the managerial use of emerging technology. Methodologically it is broad: econometrics on firm/platform data, surveys, experiments, analytical/design-science modeling, and data science.

Default assumption: unless the user says otherwise, treat the target as JMIS. Operational tells that you are at JMIS and not a sibling: submission is **by email to the Editor-in-Chief at jmis@fdu.edu** (subject line "JMIS Submission"), *not* through a ScholarOne or Taylor & Francis portal; review is **double-anonymized**; references use **numbered bracketed citations [9] with an alphabetized list** (an IEEE-like numbering, unlike the author-date style of MISQ/ISR); the complete manuscript is capped at **≤50 pages**; the abstract is **≤150 words with no citations**. (检索于 2026-06；以官网为准.)

## When to trigger

- The user asks "what should I do next?" with a half-built JMIS manuscript
- A draft's current bottleneck — fit, mechanism, identification, exhibits, prose, submission — needs diagnosing
- Work is ping-ponging between framing, estimation/modeling, writing, and the response letter
- A JMIS decision letter arrived and the user needs to switch into revision mode
- The team is unsure whether the paper belongs at JMIS versus MISQ, ISR, JAIS, or Management Science

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Question not clearly an IS-management/economics problem; outlet fit uncertain | `jmis-topic-selection` |
| The IT-value / platform / economic mechanism is thin or descriptive | `jmis-theory-development` |
| Contribution vs. MISQ/ISR/JAIS and the IS literature is fuzzy | `jmis-literature-positioning` |
| Research design or construct validity does not match the claim | `jmis-methods` |
| Estimation, identification, SEM, or analytics modeling needs work | `jmis-data-analysis` |
| Results exist but the "so what for IS management" is implicit | `jmis-contribution-framing` |
| Exhibits are dense, mislabeled, or do not answer the question | `jmis-tables-figures` |
| Prose buries the argument; abstract/intro do not land | `jmis-writing-style` |
| Ready to email the EIC; need an anonymization + format preflight | `jmis-submission` |
| Want to understand the EIC-led, double-anonymized timeline / desk-reject odds | `jmis-review-process` |
| Received an R&R; need a response-letter strategy | `jmis-rebuttal` |

## Default order

1. `jmis-topic-selection` — lock an IS-management/economics question with JMIS fit
2. `jmis-theory-development` — build the IT-value / platform / economic mechanism
3. `jmis-literature-positioning` — stake the contribution vs. the basket and reference disciplines
4. `jmis-methods` — match design to claim (econometrics / survey / experiment / analytical / design-science)
5. `jmis-data-analysis` — identification, construct validity, estimation, analytics
6. `jmis-contribution-framing` — turn results into an explicit IS contribution
7. `jmis-tables-figures` — exhibits that carry the argument
8. `jmis-writing-style` — make the idea land (abstract + intro last)
9. `jmis-submission` — anonymization + ≤50pp + numbered-reference preflight, then email the EIC
10. `jmis-review-process` — calibrate expectations for the EIC-led process
11. `jmis-rebuttal` — after the R&R

> `jmis-tables-figures` and `jmis-writing-style` are **late-stage polish**. Do not rewrite the intro before the mechanism and identification settle.

## Routing by paper archetype

JMIS spans several research styles, and the binding constraint differs by style. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| IT-business-value / firm econometrics | endogeneity of IT investment; identifying variation | `jmis-methods` → `jmis-data-analysis` |
| digital platform / e-commerce empirics | network effects, two-sidedness, selection on platform data | `jmis-theory-development` → `jmis-data-analysis` |
| behavioral survey / experiment (IS adoption, security) | construct validity, common-method bias, manipulation realism | `jmis-methods` |
| analytical / economic modeling of IS | the economic mechanism and signed comparative statics | `jmis-theory-development` |
| design-science / data-science artifact | utility evaluation vs. credible baselines, managerial relevance | `jmis-methods` → `jmis-data-analysis` |

## Difference vs. MISQ / ISR / JAIS / Management Science

- **JMIS**: management **and economics** of IS/technology; email-to-EIC submission; double-anonymized; numbered bracketed references; ≤50pp. Distinctive economics-of-IS and e-commerce/platform emphasis (Zwass's IJEC lineage).
- **MISQ**: basket sibling with a stronger **design-science genre identity** and theory/method conventions; ScholarOne; author-date style — different house norms.
- **ISR**: INFORMS quarterly, **sociotechnical and intradisciplinary**, behavioral and analytical co-equal; ScholarOne; mandatory ~500-word contribution statement.
- **JAIS**: AIS flagship, broad IS theory; AIS e-Library submission.
- **Management Science**: INFORMS, broad management/OR (not IS-specific); charges a submission fee.

## Anti-patterns

- Treating JMIS as interchangeable with MISQ or ISR — it has its own scope (economics of IS), process (email to EIC), and citation style (numbered brackets)
- Submitting through a Taylor & Francis / ScholarOne portal because the journal is T&F-published — JMIS intake is the EIC's email
- Forgetting the **≤50-page** ceiling and trying to offload core claims to an online appendix
- Letting `jmis-tables-figures`/`jmis-writing-style` polish exhibits while the mechanism or identification is still moving
- Quoting an editor, fee, or limit not in `resources/official-source-map.md` without marking it 待核实

## Output format

```text
【Target】Journal of Management Information Systems (JMIS)
【Current bottleneck】fit / mechanism / positioning / design / evidence / exhibits / style / submission / revision
【Archetype】IT-value / platform / behavioral / analytical / design-science
【Next skill】<one jmis-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实 (检索于 2026-06)
```
