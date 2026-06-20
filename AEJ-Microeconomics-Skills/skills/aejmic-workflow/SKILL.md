---
name: aejmic-workflow
description: Use when deciding which aejmic-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for an American Economic Journal: Microeconomics (AEJ: Micro) submission. Routes — it does not replace — the specialized skills.
---

# AEJ: Micro Workflow Router (aejmic-workflow)

## Overview

This is the router. It tells you **which aejmic-* skill to use at the current stage** of a manuscript aimed at the *American Economic Journal: Microeconomics* (AEJ: Micro) — the **American Economic Association's** quarterly journal (founded 2009, one of four AEJs) for **microeconomic THEORY and its applications**: game theory, mechanism and market design, industrial-organization theory, contract theory, information economics, decision theory, behavioral theory, and theory-grounded experiments. AEJ: Micro is **theory-first** — it rewards a clean, general, well-motivated result, with structural/experimental applications welcome when the economics is the point.

Default assumption: unless the user says otherwise, treat the target as AEJ: Micro. Operational tells that you are at AEJ: Micro and not a sibling: it wants **broad micro interest + the AEA editorial process** (vs. specialist *JET* / *GEB* / *Theoretical Economics*); it is **less abstract/methodological** than *TE* or *Econometrica*; and it is **theory**, not empirical applied micro (that is *AEJ: Applied*). Process tells: **single-blind** review via the AEA submission system (author revealed to referees; referees anonymous), a **submission fee** (AEA member rate — volatile), JEL classification per AEA practice, and the **AEA Data and Code Availability Policy** for any paper with data, code, experiments, or numerical results. Re-verify volatile specifics on the official AEA pages (see `resources/official-source-map.md`).

## When to trigger

- The user asks "what should I do next?"
- A draft needs its current bottleneck diagnosed
- Work is ping-ponging between the model, the proofs, the framing, and the response letter
- An AEJ: Micro decision letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Unsure the question is broad-micro-interesting theory (not JET/TE/AEJ:Applied) | `aejmic-topic-selection` |
| Contribution vs. the closest existing result is fuzzy or oversold | `aejmic-literature-positioning` |
| The model, equilibrium concept, or proof architecture is the bottleneck | `aejmic-theory-model` |
| Unclear what makes the result tight / which assumption is doing the work | `aejmic-identification` |
| Extensions, edge cases, or (applied) robustness checks are missing | `aejmic-robustness` |
| Propositions, numerical examples, or experimental exhibits are messy | `aejmic-tables-figures` |
| Prose buries the result; abstract/intro do not land | `aejmic-writing-style` |
| Proof appendix, numerical/structural/experimental code deposit, README | `aejmic-replication-package` |
| Want to anticipate referee objections / calibrate desk-reject odds | `aejmic-referee-strategy` |
| Ready to submit via the AEA system; need a preflight | `aejmic-submission` |
| Received an R&R; need a response-letter strategy | `aejmic-rebuttal` |

## Default order

1. `aejmic-topic-selection` — lock a broad-interest microeconomic-theory question
2. `aejmic-literature-positioning` — stake the result against the closest theorem
3. `aejmic-theory-model` — **the central skill**: model, equilibrium concept, proof strategy
4. `aejmic-identification` — what makes the result tight / what identifies parameters
5. `aejmic-robustness` — extensions, edge cases, applied robustness
6. `aejmic-tables-figures` — propositions, numerical examples, experimental tables
7. `aejmic-writing-style` — make the result land (abstract + intro last)
8. `aejmic-replication-package` — proof appendix + code (AEA Data Editor)
9. `aejmic-referee-strategy` — pre-empt the objections theory referees raise
10. `aejmic-submission` — AEA system preflight (single-blind, JEL, fee)
11. `aejmic-rebuttal` — after the R&R

> `aejmic-writing-style` is a late-stage polish; do not rewrite the intro before the model and proofs settle.

## Anti-patterns

- Polishing prose or exhibits while the **model or main proof is still moving** — `aejmic-theory-model` must settle first
- Treating AEJ: Micro like *JET*/*GEB* (specialist, maximal generality) or *AEJ: Applied* (empirical) — wrong fit gate
- Deferring the **proof appendix** and any **numerical/experimental code** until acceptance — the AEA Data Editor checks before publication
- Reporting an applied result with significance asterisks instead of standard errors

## Routing by paper archetype

AEJ: Micro spans several branches; the bottleneck differs. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| pure theory (mechanism/game/decision) | equilibrium concept + proof strategy + generality | `aejmic-theory-model` |
| theory with structural estimation | parameter identification + counterfactual validity | `aejmic-identification` → `aejmic-theory-model` |
| theory-grounded experiment | design maps to the model's prediction; pre-registration | `aejmic-topic-selection` → `aejmic-identification` |
| IO theory / applied micro-theory | the mechanism's robustness to modeling choices | `aejmic-theory-model` → `aejmic-robustness` |

## Worked routing example (illustrative)

A user says: "My mechanism-design result is proved, but a referee says it hinges on a knife-edge tie-breaking assumption and asks whether it survives a continuum of types." That is two distinct AEJ: Micro pushbacks — *which assumption is doing the work* (owned by `aejmic-identification`) and *does the mechanism extend* (owned by `aejmic-robustness`), both anchored to `aejmic-theory-model`. Route to `aejmic-theory-model` to restate the proof under the relaxed assumption, then `aejmic-robustness` for the continuum extension; only once the proposition is stable do you return to `aejmic-tables-figures` and `aejmic-rebuttal`.

## Minimal decision snippet

```
if decision_letter_arrived:          -> aejmic-rebuttal
elif ready_to_submit:                -> aejmic-submission
elif anticipating_referees:          -> aejmic-referee-strategy
elif proof_appendix_or_code:         -> aejmic-replication-package
elif prose_or_intro:                 -> aejmic-writing-style
elif exhibits_or_examples:           -> aejmic-tables-figures
elif extensions_or_edge_cases:       -> aejmic-robustness
elif which_assumption_or_id:         -> aejmic-identification
elif model_or_proof_unsettled:       -> aejmic-theory-model
elif fit_or_positioning_fuzzy:       -> aejmic-topic-selection / aejmic-literature-positioning
else:                                -> aejmic-topic-selection
```
