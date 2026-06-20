---
name: jeea-workflow
description: Use when deciding which jeea-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Journal of the European Economic Association (JEEA) submission. Routes — it does not replace — the specialized skills.
---

# JEEA Workflow Router (jeea-workflow)

## Overview

This is the router. It tells you **which jeea-* skill to use at the current stage** of a manuscript aimed at the *Journal of the European Economic Association* (JEEA) — the **general-interest journal of the European Economic Association (EEA)**, published by **Oxford University Press (OUP)**. JEEA publishes high-quality economics across **all** fields — micro and macro theory, applied econometrics, applied micro, finance, development, public — and judges every paper at a **general-interest theory-and-empirics bar**, not a field-specialist one. A JEEA paper can be a clean empirical design **or** a disciplined theory/structural contribution; both must matter to a broad economics readership.

Default assumption: unless the user says otherwise, treat the target as JEEA. Operational tells that you are at JEEA and not a sibling (*The Economic Journal*, the *European Economic Review*) or a top-5: **EEA membership is required** for the submitting author to submit and resubmit; there is a **submission fee** (€100, effective Feb 1, 2026; waived if the submitting author and all coauthors are based in low- and middle-income countries); review is **single-blind**, managed by a co-editor with a **fast-decision target (≈8 weeks where possible)**; and the **JEEA Data Editor** runs a **mandatory replication check before formal acceptance** under the DCAS standard (endorsed since Feb 1, 2024), with replication packages posted to the **JEEA Zenodo community**. Source-map process facts were refreshed on 2026-06-20; live-check volatile specifics on the official EEA / OUP pages before a real upload.

## When to trigger

- The user asks "what should I do next?"
- A draft needs its current bottleneck diagnosed
- Work is ping-ponging between identification/theory, framing, writing, and the response letter
- A JEEA decision letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Question feels narrow / field-specialist, not clearly general-interest | `jeea-topic-selection` |
| Contribution vs. the frontier is fuzzy or undersold | `jeea-literature-positioning` |
| Empirical causal design or theory/structural identification is shaky | `jeea-identification` |
| A theory model needs sharper assumptions, results, or discipline | `jeea-theory-model` |
| Results may not survive specification / sample / inference perturbations | `jeea-robustness` |
| Exhibits are dense; significance asterisks still present | `jeea-tables-figures` |
| Prose buries the idea; abstract/intro do not land | `jeea-writing-style` |
| Data/code deposit, README, or JEEA Data Editor prep | `jeea-replication-package` |
| Want to anticipate referee objections / desk-reject odds / timeline | `jeea-referee-strategy` |
| Ready to submit via the EEA member-area flow; need a preflight | `jeea-submission` |
| Received an R&R; need a response-letter strategy | `jeea-rebuttal` |

## Default order

1. `jeea-topic-selection` — lock the general-interest question and confirm JEEA fit
2. `jeea-literature-positioning` — stake the contribution vs. the frontier
3. `jeea-identification` — credible empirical design or theory/structural identification
4. `jeea-theory-model` — make any model disciplined and its results legible
5. `jeea-robustness` — show the headline result is not fragile
6. `jeea-tables-figures` — exhibits without significance asterisks
7. `jeea-writing-style` — make the idea land (abstract + intro last)
8. `jeea-replication-package` — assemble the DCAS package for the JEEA Data Editor
9. `jeea-referee-strategy` — pre-empt objections; calibrate expectations
10. `jeea-submission` — EEA member-area submission preflight
11. `jeea-rebuttal` — after the R&R

> `jeea-writing-style` is a late-stage polish; do not rewrite the intro before identification/theory/robustness settle.

## Anti-patterns

- Skipping `jeea-replication-package` until acceptance — the JEEA Data Editor checks **before** formal acceptance, and empirical papers cannot be accepted until replication is verified
- Letting `jeea-tables-figures` polish exhibits while estimation or the model is still moving
- Treating JEEA like a field journal (selling depth in one subfield) instead of a general-interest outlet (selling a lesson that travels)

## Routing by paper archetype

JEEA spans theory and empirics, and the bottleneck differs by archetype. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| applied micro / development causal design | staggered-DID or weak-IV credibility | `jeea-identification` |
| micro / macro theory | assumptions, generality, and a sharp result | `jeea-theory-model` → `jeea-identification` (Branch C) |
| structural / quantitative | parameter identification + counterfactual validity | `jeea-identification` (Branch A) → `jeea-robustness` |
| finance / asset pricing | identification + factor-zoo / inference discipline | `jeea-identification` → `jeea-robustness` |

## Worked routing example (illustrative)

A user says: "My theory paper has a clean model, but a referee says the main proposition needs a more general environment and the empirical illustration uses naive TWFE." That is two distinct JEEA pushbacks — *the model is not as general as the claim* (owned by `jeea-theory-model`) and *the empirical design is biased under staggered timing* (owned by `jeea-identification` Branch B). Route to `jeea-theory-model` first to generalize the proposition, then to `jeea-identification` to re-estimate with a heterogeneity-robust estimator; only once both settle (say the headline elasticity stabilizes at 0.18, s.e. 0.04, illustrative) do you return to `jeea-tables-figures` and `jeea-rebuttal`.

## Minimal decision snippet

```
if decision_letter_arrived:        -> jeea-rebuttal
elif ready_to_submit:              -> jeea-submission
elif exhibits_or_significance:     -> jeea-tables-figures
elif results_look_fragile:         -> jeea-robustness
elif model_not_disciplined:        -> jeea-theory-model
elif identification_shaky:         -> jeea-identification
elif claim_or_positioning_fuzzy:   -> jeea-literature-positioning
else:                              -> jeea-topic-selection
```
