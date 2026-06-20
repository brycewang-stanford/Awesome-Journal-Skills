---
name: jams-workflow
description: Use when deciding which jams-* sub-skill to invoke next, or when sequencing manuscript work from question to rebuttal for a Journal of the Academy of Marketing Science (JAMS) submission. Routes — it does not replace — the specialized skills.
---

# JAMS Workflow Router (jams-workflow)

## Overview

This is the router. It tells you **which jams-* skill to use at the current stage** of a manuscript aimed at the *Journal of the Academy of Marketing Science* (JAMS) — the flagship journal of the **Academy of Marketing Science (AMS)**, published by **Springer** (ISSN 0092-0703 print / 1552-7824 online; bimonthly). JAMS is the broad **marketing-science** outlet: marketing strategy, B2B/industrial marketing, services, retailing, channels, sales, branding, innovation, the marketing–finance interface, and consumer behavior. Its defining tradition is **managerial relevance married to strong method** — every paper is expected to advance theory *and* tell a manager (or policy maker) something they can act on.

Default assumption: unless the user says otherwise, treat the target as JAMS. Operational tells that you are at JAMS and not a sibling: submission runs through **Springer Editorial Manager**; review is **double-anonymized** (fully blinded manuscript + separate title page with ORCID); the house citation style is **APA**; and the contribution test is explicitly **dual** — theory contribution *and* "what should a manager do." Co-Editors-in-Chief Stephanie M. Noble and Charles H. Noble (University of Tennessee, since June 2024) lead the journal (检索于 2026-06；以官网为准). Re-verify volatile specifics on the Springer journal page (link.springer.com/journal/11747).

## When to trigger

- The user asks "what should I do next?" on a JAMS-bound paper
- A draft needs its current bottleneck diagnosed
- Work is ping-ponging between framing, theory, design, evidence, exhibits, and the response letter
- A JAMS decision letter arrived and the user needs to switch into revision mode
- The team is unsure whether the paper belongs at JAMS vs. JM, JMR, Marketing Science, or JCR

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Scope/outlet fit uncertain; not clearly a broad marketing-science question | `jams-topic-selection` |
| The conceptual framework / mechanism is thin or borrowed | `jams-theory-development` |
| Contribution vs. the marketing literature is fuzzy or oversold | `jams-literature-positioning` |
| Construct validity, design, or identification need alignment to the claim | `jams-methods` |
| Estimation (SEM/PLS/HLM/regression/experiment/meta) needs work | `jams-data-analysis` |
| The theory **and** managerial "so what" are not both sharp | `jams-contribution-framing` |
| Exhibits are dense; tables do not answer the question | `jams-tables-figures` |
| Intro/abstract/prose bury the idea or miss the JAMS voice | `jams-writing-style` |
| Editorial Manager preflight: blinding, APA, files, statements | `jams-submission` |
| Want to understand the developmental review timeline / decisions | `jams-review-process` |
| Received an R&R; need a response-letter strategy | `jams-rebuttal` |

## Default order

1. `jams-topic-selection` — lock the broad, managerially consequential marketing question
2. `jams-theory-development` — build the conceptual framework and mechanism
3. `jams-literature-positioning` — stake the contribution against the marketing canon
4. `jams-methods` — match construct validity and design to the claim
5. `jams-data-analysis` — SEM/PLS/HLM/regression/experiment/meta, done right
6. `jams-contribution-framing` — the dual theory + managerial contribution
7. `jams-tables-figures` — exhibits that answer the question
8. `jams-writing-style` — make the idea land (abstract + intro last)
9. `jams-submission` — Editorial Manager preflight (blinding, APA, statements)
10. `jams-review-process` — calibrate the developmental-review timeline
11. `jams-rebuttal` — after the R&R

> `jams-writing-style` is late-stage polish; do not rewrite the intro before theory, design, and the managerial takeaway settle.

## Routing by paper archetype

JAMS spans several genres, and the binding constraint differs by genre. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| Survey + SEM/PLS (strategy, B2B, services) | construct validity, CMV, discriminant validity | `jams-methods` → `jams-data-analysis` |
| Secondary-data econometrics (scanner, CRM, finance interface) | causal identification / endogeneity | `jams-methods` (identification) → `jams-data-analysis` |
| Behavioral experiment | manipulation validity, mediation, mechanism | `jams-methods` → `jams-data-analysis` |
| Meta-analysis | sampling frame, coding reliability, moderators | `jams-methods` → `jams-data-analysis` |
| Conceptual / framework paper | a genuinely new framework, not a literature recap | `jams-theory-development` → `jams-contribution-framing` |

## Worked routing example (illustrative)

A user says: "My survey SEM fits well and all paths are significant, but a reviewer says the contribution is a new-context replication and the managerial implications are generic." That is two distinct JAMS pushbacks. The contribution challenge is owned by `jams-literature-positioning` (find the live gap) and `jams-contribution-framing` (state the dual contribution and defend against "incremental"); the generic-managerial-implication challenge is owned by `jams-contribution-framing` and `jams-writing-style` (rewrite the implications section with decisions and magnitudes). A good fit also routes through `jams-data-analysis` to make sure each path has a managerial magnitude to cite. Note what is *not* the bottleneck here: the measurement model already fits, so do not start by re-running the SEM.

## Minimal decision snippet

```
if decision_letter_arrived:          -> jams-rebuttal
elif ready_to_submit:                -> jams-submission
elif exhibits_unclear:               -> jams-tables-figures
elif estimation_or_validity:         -> jams-data-analysis / jams-methods
elif contribution_or_positioning:    -> jams-contribution-framing / jams-literature-positioning
elif theory_thin:                    -> jams-theory-development
else:                                -> jams-topic-selection
```

## Anti-patterns

- Treating JAMS as interchangeable with JM (AMA strategy outlet), JMR (methods/measurement), Marketing Science (analytical modeling), or JCR (consumer/interpretive)
- Polishing prose before the theory, design, and managerial takeaway are stable
- Skipping the managerial contribution and submitting a "theory only" paper — JAMS reviewers ask for both
- Letting `jams-tables-figures` polish exhibits while estimation is still moving
- Quoting volatile process facts (fees, limits, editors) as permanent rather than re-verifying

## Output format

```text
【Target】Journal of the Academy of Marketing Science (JAMS)
【Archetype】survey-SEM / secondary-data / experiment / meta-analysis / conceptual
【Current bottleneck】fit / theory / positioning / design / evidence / exhibits / style / submission / revision
【Next skill】<one jams-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实 / 检索于 2026-06
```
