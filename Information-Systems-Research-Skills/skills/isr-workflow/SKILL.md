---
name: isr-workflow
description: Use when deciding which isr-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for an Information Systems Research (ISR) manuscript. Routes — it does not replace — the specialized skills. Knows ISR's sociotechnical, intradisciplinary mission and its co-equal behavioral and analytical genres.
---

# Information Systems Research Workflow (isr-workflow)

## Overview

This is the router. It does not replace any specialized skill; it tells you **which isr-* skill to use right now** for your Information Systems Research (ISR) manuscript.

Default assumption: unless the user says otherwise, treat the target as ISR — the INFORMS quarterly at the intersection of technology, organizations, economics, and society, and a member of the IS field's **Senior Scholars' Basket of Eight**. ISR's identity is deliberately **sociotechnical and intradisciplinary**: it is receptive to the design, management, use, valuation, and impacts of IT across multiple levels of analysis (individuals, groups, firms, networks, societies, nations), and it houses **both** rigorous behavioral/empirical research **and** analytical economic, econometric, and design-science modeling as **co-equal** first-class genres. The recurring editorial question is not only "is the method sound?" but "does this **bridge IS silos** and advance our intradisciplinary understanding of the sociotechnical?"

> Editorial team context: Suprateek Sarker (University of Virginia, McIntire) is the current Editor-in-Chief; his inaugural editorial appeared in ISR 34(1):1-4 on February 27, 2023. The 2025 multimethod-research framework editorial (ISR 36(2)) formalizes guidance for combining qualitative, quantitative, analytical, and design-science methods. Re-check the current masthead and policies at pubsonline.informs.org/journal/isre before submission.

## When to trigger

- "What should I do next?" with a half-built ISR manuscript
- You have an analytical model or a dataset but no clear sociotechnical, intradisciplinary story
- A reviewer/SE pushes on "contribution to IS" or "this is single-paradigm" and you are unsure which stage is the bottleneck
- You received an ISR decision letter and need to switch into response mode
- You keep bouncing between modeling/analysis, theory, and writing without a plan

## Routing table

| Current symptom                                                          | Next skill                   |
|--------------------------------------------------------------------------|------------------------------|
| Idea is vague; unsure it fits ISR's sociotechnical/intradisciplinary bar | `isr-topic-selection`        |
| Mechanism is thin (behavioral hypotheses or analytical propositions)     | `isr-theory-development`     |
| Front end reads as single-silo; does not bridge IS conversations         | `isr-literature-positioning` |
| Design/genre may not match the question (behavioral vs analytical vs DSR) | `isr-methods`               |
| Have data/model; unsure about identification, validity, or proof rigor   | `isr-data-analysis`          |
| Results exist but the "contribution to IS" is thin or single-paradigm    | `isr-contribution-framing`   |
| Exhibits cluttered, off INFORMS style, or proofs crowding the main text  | `isr-tables-figures`         |
| Prose is jargon-heavy, passive, or buries the argument                   | `isr-writing-style`          |
| Ready to submit; need the ScholarOne preflight + contribution statement  | `isr-submission`             |
| Want to understand how ISR's SE/AE review works before/after submit      | `isr-review-process`         |
| Received an R&R; need to plan and draft the response                     | `isr-rebuttal`               |

## Default order

1. `isr-topic-selection` — lock a sociotechnical question with ISR fit (vs MISQ/JMIS/MS)
2. `isr-theory-development` — build the mechanism (behavioral hypotheses **or** analytical propositions)
3. `isr-literature-positioning` — bridge IS silos; state the intradisciplinary conversation you join
4. `isr-methods` — match the genre (behavioral empirical / analytical-economic / design-science / multimethod)
5. `isr-data-analysis` — identification and validity (empirical) or proof discipline (analytical)
6. `isr-contribution-framing` — turn results into an explicit contribution to IS (drafts the ~500-word statement)
7. `isr-tables-figures` — finalize exhibits; push proofs/measurement to the electronic companion
8. `isr-writing-style` — full-manuscript prose polish
9. `isr-submission` — ScholarOne preflight (anonymization, contribution statement, editor/reviewer nominations)
10. `isr-review-process` — set expectations for the SE-led, fit-gated process
11. `isr-rebuttal` — after an R&R, plan revisions then draft the response

> `isr-tables-figures` and `isr-writing-style` are **late-stage polish**. Do not invoke them while the contribution or identification/proof is still unsettled.

## Difference vs. MISQ / JMIS / Management Science stacks

- **ISR**: sociotechnical and **intradisciplinary**; behavioral **and** analytical/design-science as co-equal genres under one cover; INFORMS (OR/economics lineage); 32-page text / 38-page total cap; SE/AE routing with an EIC fit gate.
- **MISQ**: sister Basket-of-Eight journal with a stronger **design-science genre identity** and its own theory/method conventions — different house norms.
- **JMIS**: Basket-of-Eight; overlapping scope but distinct editorial conventions.
- **Management Science**: also INFORMS, but a broader management/OR journal (and the one that charges the $79 original-submission fee) — not IS-specific.

## Anti-patterns

- **Do not** skip `isr-theory-development` and jump to estimation/derivation — ISR rejects atheoretical phenomenon-mining.
- **Do not** let `isr-tables-figures` beautify exhibits before the model and contribution are settled.
- **Do not** treat a single-paradigm result as automatically ISR-fit — the journal prizes intradisciplinary, silo-bridging work.
- **Do not** let `isr-writing-style` substitute for a real contribution to IS — polish cannot rescue thin theory or a non-identified design.
