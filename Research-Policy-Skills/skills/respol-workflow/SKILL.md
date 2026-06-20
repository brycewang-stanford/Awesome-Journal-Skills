---
name: respol-workflow
description: Use when deciding which respol-* sub-skill to invoke next, or when sequencing manuscript work from topic through rebuttal for a Research Policy (RP) submission. Routes — it does not replace — the specialized skills.
---

# Research Policy Workflow Router (respol-workflow)

## Overview

This is the router. It names **which respol-* skill to use at the current stage** of a manuscript aimed at *Research Policy* (RP) — Elsevier's flagship journal of **innovation studies** and science, technology & innovation (STI) policy. RP's center of gravity is the economics, management, and sociology of innovation: R&D and technological change, national/regional/sectoral innovation systems, science and technology policy, entrepreneurship and technology management, university-industry links, and intellectual property. It is deeply **interdisciplinary** and carries the SPRU/Freeman-Nelson-Pavitt heritage; a paper earns space by advancing innovation-studies understanding, usually with a policy or managerial implication.

Default assumption: unless the user says otherwise, treat the target as RP. Operational tells that you are at RP and not a sibling: the contribution is to **innovation theory or evidence**, not to a generic strategy or economics conversation; methods are pluralist (econometrics, **bibliometrics/patent analysis**, surveys, case studies, mixed methods) and no single technique is privileged; review is **double-blind**; the desk-screen rejects papers whose literature is "almost entirely economics or management journals" as out of scope (检索于 2026-06；以官网为准). Article types include full articles (~8,000–10,000 words incl. notes/refs/tables) and shorter Research Notes (~3,000–5,000 words) — verify on the guide for authors.

## When to trigger

- The user asks "what should I do next?" on an RP-bound manuscript
- A draft's current bottleneck is unclear and needs diagnosis
- Work is ping-ponging between framing, theory, design, evidence, exhibits, and the response letter
- An RP decision letter arrived and the user must switch into revision mode
- The team is debating RP vs. a sibling (Industrial and Corporate Change, Technovation, JPIM, SMJ)

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Scope/audience/outlet fit uncertain; risk of "out of scope" desk reject | `respol-topic-selection` |
| The innovation-studies conceptual contribution is thin or borrowed | `respol-theory-development` |
| Contribution vs. the innovation-studies frontier is fuzzy or mis-cited | `respol-literature-positioning` |
| Identification / measurement / design (patent, survey, case, mixed) is shaky | `respol-methods` |
| Estimation, bibliometric construction, coding, or robustness needs work | `respol-data-analysis` |
| The one-sentence "so what for innovation studies + policy" does not land | `respol-contribution-framing` |
| Exhibits are dense or do not carry the mechanism | `respol-tables-figures` |
| Prose buries the idea; intro/abstract miss the RP voice | `respol-writing-style` |
| Ready to submit; need a preflight + data/code statement | `respol-submission` |
| Want referee timeline / desk-reject odds / Research Note option | `respol-review-process` |
| Received an R&R; need a response-letter strategy | `respol-rebuttal` |

## Default order

1. `respol-topic-selection` — lock an innovation-studies question RP owns
2. `respol-theory-development` — build the mechanism / conceptual frame
3. `respol-literature-positioning` — stake the gap against the RP/SPRU canon
4. `respol-methods` — design and measurement appropriate to the claim
5. `respol-data-analysis` — estimation / bibliometric build / coding + robustness
6. `respol-contribution-framing` — sharpen the "so what + policy/managerial" claim
7. `respol-tables-figures` — exhibits that carry the mechanism
8. `respol-writing-style` — make the idea land (intro/abstract last)
9. `respol-submission` — Editorial Manager preflight + data/code statement
10. `respol-review-process` — calibrate expectations; consider Research Note
11. `respol-rebuttal` — after the R&R

> `respol-writing-style` is a late polish; do not rewrite the intro before theory, design, and evidence settle.

## Routing by paper archetype

RP spans several research traditions, and the binding constraint differs by tradition. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| Patent / bibliometric quantitative | construct validity of the indicator + endogeneity | `respol-methods` → `respol-data-analysis` |
| Policy-evaluation / causal (R&D subsidy, mission programs) | identification (DID/IV/RDD) + policy-invariance of mechanism | `respol-methods` |
| Survey on innovation behavior (firm/CIS-style) | measurement, common-method bias, generalizability | `respol-methods` → `respol-data-analysis` |
| Qualitative / case study of an innovation system | theoretical generalization + boundary conditions | `respol-theory-development` |
| Mixed-methods (cases + patents/survey) | integration logic, not two papers stapled together | `respol-theory-development` → `respol-methods` |
| Conceptual / typology of innovation systems | novelty vs. the SPRU canon; falsifiability | `respol-literature-positioning` |

## Worked routing example (illustrative)

A user says: "My patent-based paper on regional knowledge spillovers estimates fine, but a referee says the citation measure is endogenous and that the paper reads like an economics-of-geography paper, not innovation studies." That is two distinct RP pushbacks — an *indicator/identification* problem owned by `respol-methods` and `respol-data-analysis`, and a *positioning/scope* problem owned by `respol-literature-positioning`. Route to methods first to defend the patent-citation measure (e.g., self-citation correction, examiner vs. applicant citations), then to positioning to re-anchor the contribution in the innovation-systems literature so it reads as RP, not JEG.

## Anti-patterns

- Treating RP as interchangeable with SMJ (strategy), Management Science (general management science), Industrial and Corporate Change, Technovation, or JPIM
- Polishing prose before theory, design, and the evidence hierarchy are stable
- Skipping `respol-topic-selection` and submitting a paper whose lit base is "all econ/management" — the classic out-of-scope desk reject
- Letting the appendix carry a claim the main text must establish

## Minimal decision snippet

```
if decision_letter_arrived:         -> respol-rebuttal
elif ready_to_submit:               -> respol-submission
elif exhibits_unclear:              -> respol-tables-figures
elif claim_or_so_what_fuzzy:        -> respol-contribution-framing
elif estimation_or_indicator:       -> respol-data-analysis
elif design_or_measurement_shaky:   -> respol-methods
elif theory_thin:                   -> respol-theory-development
elif positioning_or_scope_fuzzy:    -> respol-literature-positioning / respol-topic-selection
else:                               -> respol-topic-selection
```
