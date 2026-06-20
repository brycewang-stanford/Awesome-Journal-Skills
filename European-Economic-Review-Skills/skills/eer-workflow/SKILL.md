---
name: eer-workflow
description: Use when deciding which eer-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a European Economic Review (EER) submission. Routes — it does not replace — the specialized skills.
---

# EER Workflow Router (eer-workflow)

## Overview

This is the router. It tells you **which eer-* skill to use at the current stage** of a manuscript aimed at the *European Economic Review* (EER) — **Elsevier's** long-standing (founded 1969) **general-interest** European economics journal, hosted on ScienceDirect (ISSN 0014-2921). EER publishes **all fields of economics, theory and empirical** — macro, micro, labor, public, IO, international, finance, behavioral — and rewards papers of **broad interest** with a credible identification or theoretical contribution, not narrow field-specialist increments.

Default assumption: unless the user says otherwise, treat the target as EER. Operational tells that you are at EER and not a sibling or a field journal: submission is via **Editorial Manager** (`editorialmanager.com/eerev`); review is **single-anonymized** (single-blind — referees see author identities) (检索于 2026-06；以官网为准); there is a **non-refundable submission fee** (EUR 125 regular / EUR 100 PhD-student; Research4Life Group A waiver) (检索于 2026-06；以官网为准); accepted empirical/simulation/experimental papers must meet the **mandatory replication policy** (data, code, computational details before publication); house style is Elsevier-economics (structured abstract, JEL codes, keywords, research highlights, declaration of interest, **standard errors reported**). The "European" in the title is institutional history, not a scope restriction — topics need not be about Europe. Editors as of 2026 include Evi Pappa, David K. Levine, Stefania Garetto, Peter Rupert, Robert Sauer (检索于 2026-06；以官网为准). Re-verify volatile specifics on the official Elsevier/ScienceDirect pages.

## When to trigger

- The user asks "what should I do next?"
- A draft needs its current bottleneck diagnosed
- Work is ping-ponging between identification, theory, writing, and the response letter
- An EER decision letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Question feels narrow / field-specialist, not general-interest | `eer-topic-selection` |
| Contribution vs. the literature is fuzzy or oversold | `eer-literature-positioning` |
| Empirical causal design is shaky (OLS+controls, naive TWFE, weak IV) | `eer-identification` |
| A theory/model is needed or the existing one is loose | `eer-theory-model` |
| Results may not survive specification / sample / inference changes | `eer-robustness` |
| Exhibits are dense; significance asterisks dominate; no SEs | `eer-tables-figures` |
| Prose buries the idea; abstract/intro/highlights do not land | `eer-writing-style` |
| Data/code deposit, README, replication-policy prep | `eer-replication-package` |
| Want to anticipate referee objections before submitting | `eer-referee-strategy` |
| Ready to submit via Editorial Manager; need a preflight | `eer-submission` |
| Received an R&R; need a response-letter strategy | `eer-rebuttal` |

## Default order

1. `eer-topic-selection` — confirm the question is general-interest, not field-niche
2. `eer-literature-positioning` — stake the contribution vs. the frontier (incl. vs. JEEA/EJ)
3. `eer-identification` — make the empirical causal design credible
4. `eer-theory-model` — build/tighten the model or conceptual frame
5. `eer-robustness` — stress-test estimates to specs, samples, inference
6. `eer-tables-figures` — exhibits with SEs, no significance-star worship
7. `eer-writing-style` — make the idea land (abstract + intro + highlights last)
8. `eer-replication-package` — assemble the mandatory-replication-policy deposit
9. `eer-referee-strategy` — pre-empt the objections a single-blind referee will raise
10. `eer-submission` — Editorial Manager preflight (fee, format, declarations)
11. `eer-rebuttal` — after the R&R

> `eer-writing-style` is a late-stage polish; do not rewrite the intro before identification/theory settle. For a pure-theory paper, `eer-theory-model` precedes `eer-identification` (or replaces it).

## Anti-patterns

- Treating EER as a Europe-only or field journal — the bar is **general interest across all of economics**
- Polishing exhibits (`eer-tables-figures`) while the identification is still moving
- Deferring `eer-replication-package` until acceptance — assemble the deposit as you build results
- Forgetting the **non-refundable submission fee** and submitting an out-of-scope paper that desk-rejects
- Confusing EER with **JEEA** (the EEA's own flagship) or **The Economic Journal** (RES flagship)

## Routing by paper archetype

EER spans theory and many empirical fields; the bottleneck differs by archetype. Read the row, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| applied micro / labor / public causal design | staggered-DID or weak-IV credibility | `eer-identification` |
| macro / quantitative model | model discipline + mapping to data | `eer-theory-model` → `eer-robustness` |
| pure theory / micro-theory | sharpness + generality of the result | `eer-theory-model` |
| experiment / behavioral | pre-registration, balance, MHT, instructions | `eer-identification` → `eer-replication-package` |

## Worked routing example (illustrative)

A user says: "My labor paper uses event-study DID on a staggered minimum-wage rollout, but a referee says the parallel-trends story is thin and the result might be driven by one state." Two distinct EER pushbacks — *design credibility* (heterogeneity-robust DID, clean pre-trends) owned by `eer-identification`, and *fragility* (leave-one-state-out, alternative samples) owned by `eer-robustness`. Route to `eer-identification` first; once the event-study leads are flat and the modern estimator agrees (say the effect settles at -2.1% employment, s.e. 0.8, illustrative), move to `eer-robustness`, then `eer-tables-figures` and `eer-rebuttal`.

## Minimal decision snippet

```
if decision_letter_arrived:        -> eer-rebuttal
elif ready_to_submit:              -> eer-submission
elif anticipating_referees:        -> eer-referee-strategy
elif deposit_or_replication:       -> eer-replication-package
elif exhibits_or_significance:     -> eer-tables-figures
elif results_may_be_fragile:       -> eer-robustness
elif needs_model:                  -> eer-theory-model
elif identification_shaky:         -> eer-identification
elif claim_or_positioning_fuzzy:   -> eer-literature-positioning
else:                              -> eer-topic-selection
```
