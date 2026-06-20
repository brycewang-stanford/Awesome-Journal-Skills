---
name: jle-workflow
description: Use when deciding which jle-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a The Journal of Law and Economics (JLE) submission. Routes — it does not replace — the specialized skills.
---

# JLE Workflow Router (jle-workflow)

## Overview

This is the router. It tells you **which jle-* skill to use at the current stage** of a manuscript aimed at *The Journal of Law and Economics* (JLE) — the **University of Chicago Press** journal founded in 1958 that defined the field of **law and economics** (the Coase–Stigler–Director tradition). JLE rewards **credible economic analysis of law, regulation, and legal institutions**: antitrust and competition, regulation and its incidence, crime and deterrence, property and contract, corporate and securities law, litigation, intellectual property, and the political economy of law. The house sensibility is **Chicago price theory plus an institutional eye** — a real legal or regulatory question, a credible empirical design or a disciplined theoretical model, and respect for how the rule actually operates.

Default assumption: unless the user says otherwise, treat the target as JLE. Operational tells that you are at JLE and not a sibling: review is **single-blind** (the title page carries author names; referees stay anonymous) — so do *not* anonymize the manuscript; submission is via the **JLE Editorial Manager** site; a **US$100 submission fee** applies (beginning May 1, 2026; non-refundable; editorial review does not start until it is paid); the **data and replication policy** requires data, programs, and computation details to be available for replication **before publication**; house citation is **Chicago author-date**. Editors as of 2026: **Elliott Ash, Matthew Backus, Dennis W. Carlton, Dhammika Dharmapala, Thomas J. Miles, Sam Peltzman** (检索于 2026-06；以官网为准). Re-verify volatile specifics on journals.uchicago.edu/journals/jle.

## When to trigger

- The user asks "what should I do next?"
- A draft needs its current bottleneck diagnosed
- Work is ping-ponging between identification, framing, exhibits, and the response letter
- A JLE decision letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Unsure the paper fits JLE vs. Journal of Legal Studies / JLEO / ALER | `jle-topic-selection` |
| Contribution vs. the law-and-economics literature is fuzzy or undersold | `jle-literature-positioning` |
| Causal design rests on OLS+controls, TWFE on staggered law changes, or a weak IV | `jle-identification` |
| A model of the legal rule / deterrence / contracting is needed | `jle-theory-model` |
| Results not shown robust to specification, sample, inference, jurisdiction | `jle-robustness` |
| Exhibits dense; the legal-variation estimate not legible in one table/figure | `jle-tables-figures` |
| Prose buries the institution and the design; intro does not land | `jle-writing-style` |
| Data/code deposit for the pre-publication replication requirement | `jle-replication-package` |
| Want to anticipate referee objections before submitting | `jle-referee-strategy` |
| Ready to submit via Editorial Manager; need a preflight | `jle-submission` |
| Received an R&R; need a response-letter strategy | `jle-rebuttal` |

## Default order

1. `jle-topic-selection` — place the legal/regulatory question at JLE, not a sibling
2. `jle-literature-positioning` — stake the marginal contribution to law and economics
3. `jle-identification` — make the law-to-outcome causal mapping credible
4. `jle-theory-model` — add the price-theory / deterrence model that interprets the estimate
5. `jle-robustness` — show the headline survives specification, sample, jurisdiction, inference
6. `jle-tables-figures` — make the legal-variation result legible in one exhibit
7. `jle-writing-style` — make the institution and the design land (abstract + intro last)
8. `jle-replication-package` — assemble the data/code deposit for the pre-publication check
9. `jle-referee-strategy` — pre-empt the objections this design and field invite
10. `jle-submission` — Editorial Manager preflight (single-blind, fee, title page)
11. `jle-rebuttal` — after the R&R

> `jle-writing-style` is a late-stage polish; do not rewrite the intro before identification and robustness settle.

## Anti-patterns

- **Anonymizing the manuscript** — JLE is single-blind; the title page carries author names. Blinding is the wrong reflex here (it is correct at AEJ/JLEO, not JLE).
- Treating the replication deposit as an acceptance-day chore — the policy requires materials available **before publication**; build it as you go (`jle-replication-package`)
- Polishing exhibits (`jle-tables-figures`) while the identification or headline estimate is still moving
- Framing the paper as doctrinal legal scholarship (drifts toward *Journal of Legal Studies*) or as organizational/positive-political-economy (drifts toward *JLEO*) instead of Chicago-style law-and-economics

## Routing by paper archetype

JLE spans several law-and-economics designs, and the first bottleneck differs by archetype. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| law change / staggered statute adoption (DiD / event study) | negative-weighting under staggered timing; parallel trends across jurisdictions | `jle-identification` |
| court / judge / case-assignment design (IV or as-good-as-random) | random-assignment defense; monotonicity; exclusion | `jle-identification` |
| regulatory threshold / eligibility cutoff (RD) | density manipulation; bandwidth; bunching | `jle-identification` → `jle-robustness` |
| antitrust / enforcement event (merger, decree, entry) | event-window contamination; market definition; control markets | `jle-identification` → `jle-robustness` |
| theory of a legal rule / deterrence / liability | a model whose comparative statics are testable, not decorative | `jle-theory-model` |
| measurement of a legal/regulatory object (new index, hand-coded doctrine) | validity of the measure; framing the contribution without causal overclaim | `jle-topic-selection` → `jle-literature-positioning` |

## Worked routing example (illustrative)

A user says: "My event study on states adopting a tort-reform statute looks fine, but a referee says the two-way fixed-effects estimate is contaminated by already-reformed states and the parallel-trends story across jurisdictions is thin." That is two JLE pushbacks — *forbidden comparisons under staggered statute adoption* and *cross-jurisdiction pre-trend credibility* — both owned by `jle-identification`, with the presentation in `jle-robustness`. Route there first; only once the heterogeneity-robust estimate is stable (say liability claims fall 8% [s.e. 3], illustrative) do you return to `jle-tables-figures` and `jle-rebuttal` to present and defend it.

## Minimal decision snippet

```
if decision_letter_arrived:        -> jle-rebuttal
elif ready_to_submit:              -> jle-submission
elif anticipating_referees:        -> jle-referee-strategy
elif building_replication_package: -> jle-replication-package
elif intro_or_abstract_weak:       -> jle-writing-style
elif exhibits_dense:               -> jle-tables-figures
elif results_not_robust:           -> jle-robustness
elif needs_model_of_the_rule:      -> jle-theory-model
elif identification_shaky:         -> jle-identification
elif contribution_fuzzy:           -> jle-literature-positioning
else:                              -> jle-topic-selection
```
