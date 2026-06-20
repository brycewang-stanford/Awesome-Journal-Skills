---
name: wber-workflow
description: Use when deciding which wber-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a The World Bank Economic Review (WBER) submission. Routes — it does not replace — the specialized skills.
---

# WBER Workflow Router (wber-workflow)

## Overview

This is the router. It tells you **which wber-* skill to use at the current stage** of a manuscript aimed at *The World Bank Economic Review* (WBER) — the **rigorous empirical development-economics** journal published by **Oxford University Press for the World Bank** (founded 1986, quarterly). WBER prizes two things at once: **credible identification** AND **clear development-policy relevance** for a World Bank / policymaker audience. A paper that nails one and ignores the other is the classic WBER misfire.

Default assumption: unless the user says otherwise, treat the target as WBER. Operational tells that you are at WBER and not a sibling: the journal **requires public release of all data and code as a condition of publication** (it is, by repute, the only development *field* journal that does this routinely); review is **single-anonymized** (referees blind, author names on the title page); there is a **40-page total cap** including everything; and WBER welcomes **short-format policy-relevant papers** alongside full articles. Editors as of 2026: **Eric Edmonds and Nina Pavcnik (Dartmouth)** (检索于 2026-06；以官网为准). Re-verify volatile specifics on the OUP WBER pages.

## When to trigger

- The user asks "what should I do next?" on a development-economics manuscript
- A draft's binding constraint (fit, identification, policy framing, exhibits, package) is unclear
- Work is ping-ponging between design, framing, evidence, and the response letter
- A WBER decision letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Question is interesting but not clearly *development* + *policy-relevant* | `wber-topic-selection` |
| Contribution vs. JDE / World Development / the Research Observer is fuzzy | `wber-literature-positioning` |
| Causal design (RCT/DiD/RD/IV) credibility is the bottleneck | `wber-identification` |
| A development model is needed to interpret or to run a counterfactual | `wber-theory-model` |
| Results may be specification-, sample-, or inference-sensitive | `wber-robustness` |
| Exhibits are dense; significance asterisks still present | `wber-tables-figures` |
| Prose buries the policy "so what"; intro/abstract do not land | `wber-writing-style` |
| Data + code deposit, README, DOI link, restricted-data path | `wber-replication-package` |
| Want to anticipate referee objections before submitting | `wber-referee-strategy` |
| Ready to submit via ScholarOne; need a preflight | `wber-submission` |
| Received an R&R; need a response-letter strategy | `wber-rebuttal` |

## Default order

1. `wber-topic-selection` — lock a development question with policy stakes
2. `wber-literature-positioning` — stake the contribution; rule out sibling venues
3. `wber-identification` — make the causal design credible
4. `wber-theory-model` — only if interpretation or counterfactual needs a model
5. `wber-robustness` — threat-by-threat, not an appendix dump
6. `wber-tables-figures` — exhibits a policymaker can read; no asterisks
7. `wber-writing-style` — make the policy contribution land (abstract + intro last)
8. `wber-replication-package` — assemble the data + code deposit with a DOI
9. `wber-referee-strategy` — pre-empt the predictable objections
10. `wber-submission` — ScholarOne preflight (40-page cap, single-anon title page)
11. `wber-rebuttal` — after the R&R

> `wber-writing-style` is a late polish; do not rewrite the intro before identification and the policy frame settle. `wber-theory-model` is conditional — a clean reduced-form evaluation often needs no formal model.

## Anti-patterns

- Treating WBER as interchangeable with the **Journal of Development Economics** (the rigorous-dev-econ *field* journal — equally demanding on method but less insistent on a World Bank policy hook)
- Treating WBER as **World Development** (interdisciplinary, broader on qualitative/mixed methods)
- Routing a **survey or literature overview** to WBER — that belongs at the **World Bank Research Observer** (not refereed; Editorial-Board reviewed)
- Polishing prose before design, contribution, and the evidence hierarchy are stable
- Letting the appendix carry claims the main 40 pages must establish

## Routing by paper archetype

WBER spans several development archetypes, and the binding constraint differs. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| program/impact evaluation (RCT or quasi-experiment) | estimand + external validity / scaling | `wber-identification` |
| policy-reform DiD / RD around a developing-country reform | staggered-DiD bias or RD manipulation | `wber-identification` |
| measurement / poverty / inequality using LSMS/DHS/admin data | data construction transparency + reproducibility | `wber-replication-package` → `wber-robustness` |
| development model + structural counterfactual | what identifies parameters; policy-invariance | `wber-theory-model` → `wber-identification` |
| short-format policy note | sharp single result + tight framing | `wber-topic-selection` → `wber-writing-style` |

## Worked routing example (illustrative)

A user says: "My RCT of a school-grants program in three districts estimates a clean ITT, but a referee says it reads like a project report and isn't general enough for WBER." That is two distinct WBER pushbacks — *policy/general-interest framing* (owned by `wber-topic-selection` + `wber-literature-positioning`) and *external validity / scaling* (owned by `wber-identification`). Route to positioning first to reframe the evaluation as evidence on a *mechanism* of interest to development policy, then to `wber-identification` to argue what the three-district LATE implies for scale-up (general-equilibrium, fiscal cost). Only once the framing and external-validity story hold do you return to exhibits and the rebuttal.

## Minimal decision snippet

```
if decision_letter_arrived:          -> wber-rebuttal
elif ready_to_submit:                -> wber-submission
elif anticipating_referees:          -> wber-referee-strategy
elif data_code_deposit:              -> wber-replication-package
elif exhibits_or_significance:       -> wber-tables-figures
elif results_fragile:                -> wber-robustness
elif need_model_for_counterfactual:  -> wber-theory-model
elif identification_shaky:           -> wber-identification
elif contribution_or_fit_fuzzy:      -> wber-literature-positioning / wber-topic-selection
else:                                -> wber-topic-selection
```
