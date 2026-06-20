---
name: restat-workflow
description: Use when deciding which restat-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a The Review of Economics and Statistics (REStat) submission. Routes — it does not replace — the specialized skills.
---

# REStat Workflow Router (restat-workflow)

## Overview

This is the router. It tells you **which restat-* skill to use at the current stage** of a manuscript aimed at *The Review of Economics and Statistics* (REStat) — the venerable MIT Press journal **edited at the Harvard Kennedy School** (founded 1917/1919; current title since 1948). REStat publishes **applied economics and applied econometrics**: it rewards **credible causal identification, careful measurement, and quantitative evidence** across labor, public, development, trade, IO, health, environment, urban, and macro-empirics. It is **empirical-first** — a clean research design or a measurement advance is the contribution; theory interprets, it does not lead.

Operational tells that you are at REStat and not a sibling: REStat values **measurement and applied econometrics**, not pure methods development (that is *J. Econometrics*); it is **broad applied econ**, wider than a field journal but more specialized than AER. Submission is via **Editorial Express** with a nonrefundable **submission fee** (US$125; source map refreshed 2026-06-20); review is editor-managed peer review; accepted empirical papers must deposit data and code to the **REStat Harvard Dataverse** under the journal's **Data and Code Availability Policy**. Editors as of the 2026-06-20 refresh: Will Dobbie (Harvard) and Raymond Fisman (Boston U), co-chairs.

## When to trigger

- The user asks "what should I do next?"
- A draft needs its current bottleneck diagnosed
- Work is ping-ponging between identification, exhibits, framing, and the response letter
- A REStat decision letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Unsure the paper fits REStat vs AER / AEJ:Applied / J. Econometrics / a field journal | `restat-topic-selection` |
| Contribution vs. the closest prior work is fuzzy or undersold | `restat-literature-positioning` |
| Causal design / measurement strategy is the bottleneck | `restat-identification` |
| Theory is overgrown or absent; unclear how much model to carry | `restat-theory-model` |
| Headline estimate's stability under specs/sample/inference is untested | `restat-robustness` |
| Exhibits are dense; the main result is not legible in one table/figure | `restat-tables-figures` |
| The question + estimate do not land in the first paragraph | `restat-writing-style` |
| Need the Harvard Dataverse data/code package + README | `restat-replication-package` |
| Want to pre-empt the objections this design invites | `restat-referee-strategy` |
| Ready to submit via Editorial Express; need a preflight | `restat-submission` |
| Received an R&R; need a response-letter strategy | `restat-rebuttal` |

## Default order

1. `restat-topic-selection` — lock the applied question and REStat fit
2. `restat-literature-positioning` — stake the marginal contribution
3. `restat-identification` — make the causal design / measurement credible
4. `restat-theory-model` — right-size theory to interpret the estimate
5. `restat-robustness` — show the headline survives specs, sample, inference
6. `restat-tables-figures` — make the result legible in one exhibit
7. `restat-writing-style` — land question + estimate early (intro last)
8. `restat-replication-package` — assemble the Harvard Dataverse package
9. `restat-referee-strategy` — pre-empt design-specific objections
10. `restat-submission` — Editorial Express preflight
11. `restat-rebuttal` — after the R&R

> `restat-writing-style` is a late-stage polish; do not rewrite the intro before identification and robustness settle.

## Anti-patterns

- Deferring `restat-replication-package` until acceptance — REStat's Data and Code Availability Policy and Harvard Dataverse deposit are part of the path to publication, not an afterthought
- Letting `restat-tables-figures` polish exhibits while the identification is still moving
- Treating REStat like *J. Econometrics* (a new estimator is the contribution) or like AER (general-interest, agenda-setting scope) — REStat is broad **applied** econ with a **measurement** tradition

## Routing by paper archetype

REStat spans several applied archetypes, and the bottleneck differs. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| applied-micro causal design (DID / RD / IV) | heterogeneity-robust estimator + clean design | `restat-identification` |
| measurement / new data or index | construct validity + measurement-error discipline | `restat-identification` → `restat-robustness` |
| trade / IO / spatial (shift-share) | exposure-design inference + exogeneity of shares/shocks | `restat-identification` |
| structural-light applied | how much model to carry without becoming method-first | `restat-theory-model` |

## Worked routing example (illustrative)

A user says: "My DID on a staggered state policy estimates fine, but a referee says TWFE is biased and the measure of my outcome is noisy." That is two distinct REStat pushbacks — *heterogeneity-biased estimator* (owned by `restat-identification`, Branch DID) and *measurement error in the outcome* (a REStat-signature concern, addressed in `restat-identification` measurement + `restat-robustness`). Route to `restat-identification` first; only once the headline effect is stable under Callaway–Sant'Anna and an attenuation correction do you return to `restat-tables-figures` and `restat-rebuttal`.

## Minimal decision snippet

```
if decision_letter_arrived:        -> restat-rebuttal
elif ready_to_submit:              -> restat-submission
elif anticipating_referees:        -> restat-referee-strategy
elif need_data_code_package:       -> restat-replication-package
elif exhibits_dense:               -> restat-tables-figures
elif headline_not_robust:          -> restat-robustness
elif theory_mis-sized:             -> restat-theory-model
elif identification_or_measurement_shaky: -> restat-identification
elif contribution_fuzzy:           -> restat-literature-positioning
else:                              -> restat-topic-selection
```
