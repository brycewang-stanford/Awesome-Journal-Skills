---
name: jais-workflow
description: Use when deciding which jais-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Journal of the Association for Information Systems (JAIS) manuscript. Routes — it does not replace — the specialized skills, and it first helps you name which of JAIS's seven manuscript categories your paper belongs in.
---

# JAIS Workflow Router (jais-workflow)

## Overview

This is the router. It does not replace any specialized skill; it tells you **which jais-* skill to use right now** for your manuscript aimed at the *Journal of the Association for Information Systems* (JAIS).

Default assumption: unless the user says otherwise, treat the target as JAIS — the **flagship journal of the Association for Information Systems (AIS)**, a Senior Scholars' Basket member that publishes "the highest quality scholarship in the field of information systems." JAIS's identity is **theory-forward and methodologically plural**: it is "inclusive in topics, level and unit of analysis, theory, method and philosophical and research approach" and "encourages theory based multi- or inter-disciplinary research" (about page, 检索于 2026-06；以官网为准). The defining tell of JAIS versus its siblings is that **theory is a first-class contribution in its own right** — JAIS runs a standalone **Theory** category for "original theory" alongside empirical Research Articles, design research, and literature reviews.

So the first routing question is not "is the method sound?" but **"which of the seven JAIS categories is this, and does the contribution match that category's bar?"** The seven categories (each with its own Senior Editor) are: **Research Articles**, **Theory**, **Literature Reviews**, **Research Perspectives**, **Foundational Research on Novel Digital Phenomena**, **Editorials**, and **Policy and Impact** (检索于 2026-06；以官网为准).

> Editorial team and policies change: Monideepa Tarafdar is Editor-in-Chief (effective Sept 1, 2024). Treat the masthead, category SEs, and any impact-factor figure as 待核实 and re-verify at aisel.aisnet.org/jais.

## When to trigger

- "What should I do next?" with a half-built JAIS manuscript
- You are unsure which of the seven JAIS categories (and therefore which contribution bar) the paper fits
- You have a conceptual/theory paper and are unsure whether JAIS or MISQ/ISR is the home
- A Senior Editor or reviewer pushes on theory contribution, fit, or methodological transparency
- A JAIS decision letter arrived and you need to switch into revision/response mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Idea is vague; unsure of the category or whether it is a JAIS-fit IS question | `jais-topic-selection` |
| The theoretical engine (new construct, framework, mechanism) is underbuilt | `jais-theory-development` |
| Front end reads as gap-spotting; the IS conversation is not engaged | `jais-literature-positioning` |
| Method (behavioral / econometric / design-science / qualitative) may not fit the claim | `jais-methods` |
| Have data or artifact output; unsure about validity, identification, or evaluation | `jais-data-analysis` |
| Results exist but the "contribution to IS theory" is thin or generic | `jais-contribution-framing` |
| Tables/figures cluttered, off APA style, or the body is not standalone | `jais-tables-figures` |
| Prose is jargon-heavy or buries the argument; APA-6 / JAIS style off | `jais-writing-style` |
| Ready to submit; need the ManuscriptCentral + double-blind + matrix preflight | `jais-submission` |
| Want to understand JAIS's developmental, SE-led review before/after submit | `jais-review-process` |
| Received a revision decision; need to plan and draft the response | `jais-rebuttal` |

## Default order

1. `jais-topic-selection` — name the category; lock an IS question that JAIS would want
2. `jais-theory-development` — build the original theory / framework / mechanism
3. `jais-literature-positioning` — join the IS conversation across disciplines
4. `jais-methods` — match the design (behavioral / econometric / design-science / qualitative) to the claim
5. `jais-data-analysis` — validity, identification, or artifact evaluation done right
6. `jais-contribution-framing` — make the theoretical contribution explicit
7. `jais-tables-figures` — finalize exhibits in a standalone, APA-styled body
8. `jais-writing-style` — APA-6 / JAIS prose polish (abstract + intro last)
9. `jais-submission` — ManuscriptCentral preflight (double-blind, matrix, cover letter)
10. `jais-review-process` — set expectations for the developmental, SE-led process
11. `jais-rebuttal` — after a revision invite, revise then draft the response

> `jais-tables-figures` and `jais-writing-style` are **late-stage polish**. Do not invoke them while the category, theory, or identification/evaluation is still unsettled.

## Routing by paper archetype

JAIS is plural, and the binding constraint differs by archetype. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| pure theory / conceptual (Theory category) | a genuinely *new* construct or framework, not a relabeled import | `jais-theory-development` |
| behavioral empirical (survey/experiment) | construct validity + common-method bias; SEM measurement model | `jais-methods` → `jais-data-analysis` |
| econometric / economics-of-IS | a credible identification strategy for the IS effect | `jais-methods` → `jais-data-analysis` |
| design science (artifact) | design principles + a real evaluation, not "we built it" | `jais-theory-development` → `jais-methods` |
| literature review (structured / theory-elaborating) | a method for the review + a forward-looking theoretical payoff | `jais-methods` → `jais-contribution-framing` |
| foundational / novel digital phenomenon | disciplined description that yields new or pre-theoretical insight | `jais-topic-selection` → `jais-theory-development` |

## Difference vs. MISQ / ISR / JMIS / Management Science

- **JAIS**: the AIS's own flagship; the most explicit "theory and method as contributions in their own right" stance — a standalone Theory category, developmental reviewing, methodological/philosophical pluralism. Double-blind; APA 6th; ManuscriptCentral; Green OA, no APC.
- **MISQ**: sister Basket journal with a stronger **design-science genre identity**, a strict page-limit-counts-everything rule, and a pluralistic transparency commitment uploaded at submission.
- **ISR**: INFORMS quarterly, sociotechnical and **intradisciplinary**, behavioral and analytical co-equal; 32/38-page caps; a required ~500-word contribution statement.
- **JMIS**: Basket journal with a more applied-systems/economic-modeling tilt and its own conventions.
- **Management Science**: broad INFORMS management/OR journal (charges a submission fee) — not IS-specific.

## Anti-patterns

- Treating JAIS as interchangeable with MISQ or ISR — the standalone **Theory** category and pluralism are the differentiators.
- Sending an atheoretical phenomenon-mining paper to JAIS — theory (or a pre-theoretical insight, in the Foundational category) is the price of entry.
- Letting `jais-tables-figures` beautify exhibits before the theory and evidence are settled.
- Polishing prose before the category, contribution, and evidence hierarchy are stable.
- Quoting a fee, editor, or word limit as permanent when the source map marks it volatile.

## Output format

```text
【Target】Journal of the Association for Information Systems (JAIS)
【Category】Research Article / Theory / Literature Review / Research Perspectives / Foundational / Editorial / Policy and Impact
【Current bottleneck】fit / theory / positioning / method / evidence / contribution / exhibits / style / submission / revision
【Next skill】<one jais-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
