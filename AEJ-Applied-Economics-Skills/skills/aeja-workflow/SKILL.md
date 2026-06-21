---
name: aeja-workflow
description: Use when deciding which aeja-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for an American Economic Journal: Applied Economics (AEJ: Applied) submission. Routes — it does not replace — the specialized skills.
---

# AEJ: Applied Workflow Router (aeja-workflow)

## Overview

This is the router. It tells you **which aeja-* skill to use at the current stage** of a manuscript aimed at the *American Economic Journal: Applied Economics* (AEJ: Applied) — the **American Economic Association's** quarterly journal for **empirical applied microeconomics with credible causal identification**: labor, development, health, education, public, urban, environmental, and household finance. AEJ: Applied is **empirical-first**: a clean research design carrying a substantive economic question, with theory used to *interpret and structure* rather than to lead.

Default assumption: unless the user says otherwise, treat the target as AEJ: Applied. Operational tells that you are at AEJ: Applied and not a sibling: review is **single-blind** (author identities are visible to referees); submission is via the **AEA ScholarOne system** with fee tiers by AEA membership and country-income status; **JEL codes and a 100-word abstract** are required; and the signature stable differentiator is the **AEA Data and Code Availability Policy** — administered by the **AEA Data Editor (Lars Vilhuber)**, accepted papers deposit data + code to the **AEA Data and Code Repository on openICPSR**, and the package is checked for reproducibility before publication. On 2026-06-20 the editor page listed **Raymond Fisman** (Boston University) as Editor, with coeditors Leah Boustan, Marika Cabral, Peter Hull, Xavier Jaravel, and Nicholas Ryan. Check live AEA pages for fees and editors before submission-week advice.

## When to trigger

- The user asks "what should I do next?"
- A draft needs its current bottleneck diagnosed
- Work is ping-ponging between identification, framing, writing, and the response letter
- An AEJ: Applied decision letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Unsure the paper fits AEJ: Applied vs AER / AEJ: Policy / a field journal | `aeja-topic-selection` |
| Contribution vs. the literature is fuzzy or undersold | `aeja-literature-positioning` |
| Causal design rests on OLS+controls, TWFE on staggered timing, or a weak IV | `aeja-identification` |
| A model is needed to interpret estimates or structure a mechanism | `aeja-theory-model` |
| Results not shown robust to specification, sample, inference | `aeja-robustness` |
| Exhibits are dense; main result not legible in one table/figure | `aeja-tables-figures` |
| Prose buries the design; abstract/intro do not land | `aeja-writing-style` |
| Data/code deposit, README, openICPSR prep for the AEA Data Editor | `aeja-replication-package` |
| Want to anticipate referee objections before submitting | `aeja-referee-strategy` |
| Ready to submit via the AEA portal; need a preflight | `aeja-submission` |
| Received an R&R; need a response-letter strategy | `aeja-rebuttal` |

## Default order

1. `aeja-topic-selection` — lock the applied-micro question and venue fit
2. `aeja-literature-positioning` — stake the marginal contribution
3. `aeja-identification` — make the data-to-causal-estimate mapping credible
4. `aeja-theory-model` — add only the theory that interprets/structures the estimate
5. `aeja-robustness` — show the headline survives specification, sample, inference
6. `aeja-tables-figures` — make the main result legible in one exhibit
7. `aeja-writing-style` — make the design and estimate land (abstract + intro last)
8. `aeja-replication-package` — assemble the openICPSR package for the AEA Data Editor
9. `aeja-referee-strategy` — pre-empt the objections this design invites
10. `aeja-submission` — AEA portal preflight (single-blind front matter, JEL, fee)
11. `aeja-rebuttal` — after the R&R

> `aeja-writing-style` is a late-stage polish; do not rewrite the intro before identification and robustness settle.

## Anti-patterns

- Treating the replication package as an acceptance-time chore — at AEA the Data Editor verifies reproducibility **before** publication, so build it as you go (`aeja-replication-package`)
- Polishing exhibits (`aeja-tables-figures`) while the identification or headline estimate is still moving
- Framing the paper as a policy question (that drifts toward AEJ: Policy) or as broad general-interest (that belongs at AER) instead of method/identification-driven applied micro

## Routing by paper archetype

AEJ: Applied spans several applied-micro designs, and the first bottleneck differs by design. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| field experiment / RCT (own data) | pre-registration, balance, attrition, estimand | `aeja-identification` → `aeja-robustness` |
| quasi-experiment (DID / event study) | staggered-timing bias, parallel-trends credibility | `aeja-identification` |
| regression discontinuity | density manipulation, bandwidth, bias-corrected CIs | `aeja-identification` → `aeja-robustness` |
| IV / shift-share | first-stage strength, exclusion, exposure design | `aeja-identification` |
| descriptive / measurement with a clean question | framing the contribution without a causal overclaim | `aeja-topic-selection` → `aeja-literature-positioning` |

## Worked routing example (illustrative)

A user says: "My event study on a staggered state policy looks fine, but a referee says the two-way fixed-effects estimate is contaminated and the parallel-trends story is thin." That is two AEJ: Applied pushbacks — *negative-weighting / contaminating already-treated comparisons under staggered timing* and *pre-trend credibility* — both owned by `aeja-identification`, with the robustness presentation in `aeja-robustness`. Route there first; only once the heterogeneity-robust estimate is stable (say it settles at a 3.1pp effect, s.e. 0.9, illustrative) do you return to `aeja-tables-figures` and `aeja-rebuttal` to present and defend it.

## Minimal decision snippet

```
if decision_letter_arrived:        -> aeja-rebuttal
elif ready_to_submit:              -> aeja-submission
elif anticipating_referees:        -> aeja-referee-strategy
elif building_replication_package: -> aeja-replication-package
elif intro_or_abstract_weak:       -> aeja-writing-style
elif exhibits_dense:               -> aeja-tables-figures
elif results_not_robust:           -> aeja-robustness
elif needs_model_to_interpret:     -> aeja-theory-model
elif identification_shaky:         -> aeja-identification
elif contribution_fuzzy:           -> aeja-literature-positioning
else:                              -> aeja-topic-selection
```
