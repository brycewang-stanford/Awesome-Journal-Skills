---
name: humrel-workflow
description: Use when deciding which humrel-* sub-skill to invoke next, or when sequencing manuscript work from topic through rebuttal for a Human Relations (HR) submission. Routes — it does not replace — the specialized skills.
---

# Human Relations Workflow Router (humrel-workflow)

## Overview

This is the router. It tells you **which humrel-* skill to use at the current stage** of a manuscript aimed at *Human Relations* (HR) — the long-established **interdisciplinary social-science journal of work, organization, and management**, published by **SAGE for the Tavistock Institute of Human Relations** (founded 1947, monthly). HR draws on organization studies, sociology, psychology, and critical perspectives, and its stated aim is "to advance our understanding of social relationships at and around work through theoretical development and empirical investigation." It treats qualitative, critical, quantitative, and mixed-methods work as equally first-class — what is non-negotiable is **a unique and substantive theoretical contribution** anchored in the *relational, social* nature of work.

Operational tells that you are at HR and not a sibling: review is **double-anonymous**, so the manuscript must be fully anonymized (no author names, no links to external sites); the total length cap is **13,000 words including everything** (检索于 2026-06；以官网为准); referencing is **SAGE Harvard** (author-date); submission is through **ScholarOne / ManuscriptCentral** (mc.manuscriptcentral.com/hr). HR runs an **editorial scoping screen** before full review — "suitable data are a necessary but not sufficient feature to get to full peer review" — so the contribution and fit must be legible up front. Co-Editors-in-Chief are **Smriti Anand and Penny Dick** (检索于 2026-06；以官网为准).

## When to trigger

- The user asks "what should I do next?" on an HR-targeted manuscript
- A draft needs its current bottleneck diagnosed
- Work is ping-ponging between theory, fieldwork/data, framing, writing, and the response letter
- An HR decision letter arrived and the user needs to switch into revision mode
- The team is weighing HR against Organization Studies, JMS, AMJ, or Organization

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Scope/audience fit uncertain; "is this an HR paper?" | `humrel-topic-selection` |
| Theory is thin, box-and-arrow, or under-engaged with social theory | `humrel-theory-development` |
| Contribution vs. adjacent conversations/journals is fuzzy | `humrel-literature-positioning` |
| Design choice and rigor (qual/critical/quant/mixed) unsettled | `humrel-methods` |
| Coding, estimation, or data-to-theory link is opaque | `humrel-data-analysis` |
| The "so what" / theoretical claim is not sharp | `humrel-contribution-framing` |
| Exhibits (data-structure table, models) hard to read | `humrel-tables-figures` |
| Prose flat; intro/abstract miss the reflexive HR register | `humrel-writing-style` |
| Anonymization, 13k cap, SAGE Harvard, portal preflight | `humrel-submission` |
| Want to calibrate scoping-screen odds / timeline / transfer | `humrel-review-process` |
| Received an R&R; need a response-letter strategy | `humrel-rebuttal` |

## Default order

1. `humrel-topic-selection` — lock the work-and-society question and HR fit
2. `humrel-theory-development` — build the social-theoretical engine
3. `humrel-literature-positioning` — stake the contribution vs. the conversation
4. `humrel-methods` — design (qual / critical / quant / mixed) with rigor
5. `humrel-data-analysis` — make the evidence-to-theory link transparent
6. `humrel-contribution-framing` — sharpen the one-sentence theoretical claim
7. `humrel-tables-figures` — exhibits that carry, not decorate
8. `humrel-writing-style` — the reflexive HR voice (intro + abstract last)
9. `humrel-submission` — anonymized ScholarOne preflight
10. `humrel-review-process` — calibrate the scoping screen and developmental review
11. `humrel-rebuttal` — after the R&R

> `humrel-writing-style` is a late polish; do not rewrite the intro before the theory and evidence settle.

## Anti-patterns

- Treating HR as interchangeable with Organization Studies (EGOS), JMS, AMJ (US hypothesis-testing), or Organization (critical-only) — see the archetype table
- Sending a paper whose contribution is empirical-only ("we found X") with no theoretical advance — fails the scoping screen
- Polishing prose before theory, design, and the evidence hierarchy are stable
- Leaving author-identifying traces (acknowledgements, self-cites in first person, live URLs) in a double-anonymous submission
- Letting an appendix carry claims the 13k main text must establish

## Routing by paper archetype

HR spans several traditions, and the binding constraint differs by archetype. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| Ethnographic / qualitative process study | data-to-theory transparency + theoretical payoff | `humrel-theory-development` → `humrel-data-analysis` |
| Critical / reflexive (power, identity, discourse) | sharpening the critique into a *travelling* contribution | `humrel-literature-positioning` → `humrel-contribution-framing` |
| Quantitative / survey / multilevel | construct validity + theorizing beyond the coefficient | `humrel-methods` → `humrel-data-analysis` |
| Mixed-methods | integration logic (why both, what each adds) | `humrel-methods` |
| Theory paper (no new data) | novelty + reach vs. existing organizational theory | `humrel-theory-development` |

## Worked routing example (illustrative)

A user says: "My ethnography of platform couriers is rich, but a reviewer says it reads as 'a vivid case with thin theory' and feels closer to *Work, Employment and Society* than HR." That is two HR pushbacks — *the data-to-theory ladder is invisible* (owned by `humrel-data-analysis`) and *the contribution is empirical not theoretical* (owned by `humrel-contribution-framing`, scoped against siblings in `humrel-literature-positioning`). Route to theory and data first; only once the courier case yields a named, generative mechanism about control and identity at work — not just a labour-process description — do you return to `humrel-writing-style` and `humrel-rebuttal`.

## Minimal decision snippet

```
if decision_letter_arrived:          -> humrel-rebuttal
elif ready_to_submit:                -> humrel-submission
elif exhibits_unclear:               -> humrel-tables-figures
elif evidence_to_theory_opaque:      -> humrel-data-analysis
elif design_or_rigor_unsettled:      -> humrel-methods
elif claim_or_positioning_fuzzy:     -> humrel-contribution-framing / humrel-literature-positioning
elif theory_thin:                    -> humrel-theory-development
else:                                -> humrel-topic-selection
```
