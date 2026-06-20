---
name: jue-workflow
description: Use when deciding which jue-* sub-skill to invoke next, or when sequencing manuscript work from topic through rebuttal for a Journal of Urban Economics (JUE) submission. Routes — it does not replace — the specialized skills.
---

# JUE Workflow Router (jue-workflow)

## Overview

This is the router. It tells you **which jue-* skill to use at the current stage** of a manuscript aimed at the *Journal of Urban Economics* (JUE) — the **Elsevier** field flagship for urban & regional economics, founded in 1974 by Edwin Mills and described as "the premier journal in the field." JUE rewards papers whose question is genuinely **spatial**: agglomeration economies, housing supply & real estate, local labor markets, commuting & transportation, land use & zoning, local public finance & Tiebout sorting, neighborhood effects, spatial sorting, urban growth, and place-based policy. The bar is a **credible spatial identification** married to a **clear urban mechanism** — not just a national-level result run on geographic data.

Operational tells that you are at JUE and not a sibling: single-anonymized (single-blind) review via **Editorial Manager**; a **US$100 nonrefundable submission fee** paid during submission (检索于 2026-06；以官网为准); a **mandatory replication policy** (data + code deposited to a major repository at acceptance, before publication); a short-paper track, **JUE: Insights** (≤6,000 words, ≤5 exhibits); co-editors-in-chief **Nathaniel Baum-Snow (Toronto)** and **Kristian Behrens (UQÀM)** (检索于 2026-06；以官网为准). Re-verify volatile specifics on the official Elsevier/ScienceDirect pages.

## When to trigger

- The user asks "what should I do next?" on a JUE-bound paper
- A draft needs its current spatial-economics bottleneck diagnosed
- Work is ping-ponging between framing, identification, exhibits (maps!), and the response letter
- A JUE decision letter arrived and the user must switch into revision mode
- The team is deciding between JUE and a sibling (RSUE, JREconomics, JEG, JPubE)

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Question is not clearly *spatial* / fit with JUE vs a sibling is uncertain | `jue-topic-selection` |
| Contribution vs. the urban-econ frontier is fuzzy or undersold | `jue-literature-positioning` |
| The spatial causal design (boundary RD, shift-share, place-based DiD) is shaky | `jue-identification` |
| The mechanism needs a spatial-equilibrium or sorting model to interpret | `jue-theory-model` |
| Results may be spatial-autocorrelation-, sorting-, or sample-sensitive | `jue-robustness` |
| Exhibits are dense; the paper has no map; spatial pattern is invisible | `jue-tables-figures` |
| Prose buries the spatial mechanism; intro/abstract do not land | `jue-writing-style` |
| Geocoded/restricted data deposit, README, repository prep | `jue-replication-package` |
| Likely referee objections should be anticipated before submission | `jue-referee-strategy` |
| Ready to submit via Editorial Manager; need a preflight | `jue-submission` |
| An R&R arrived; need a response-letter strategy | `jue-rebuttal` |

## Default order

`jue-topic-selection → jue-literature-positioning → jue-identification → jue-theory-model → jue-robustness → jue-tables-figures → jue-writing-style → jue-replication-package → jue-referee-strategy → jue-submission → jue-rebuttal`

> `jue-writing-style` is late-stage polish — do not rewrite the intro before identification and the spatial mechanism settle. Start `jue-replication-package` early if data is geocoded or restricted; the deposit is harder than it looks.

## Routing by paper archetype

JUE spans several spatial sub-fields and the binding constraint differs by archetype. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| housing supply / real estate prices | spatial sorting & supply-elasticity identification | `jue-identification` |
| agglomeration / productivity | reverse causality + Bartik/historical-IV exogeneity | `jue-identification` |
| place-based policy evaluation | boundary discontinuity or DiD with spatial spillovers (SUTVA) | `jue-identification` → `jue-robustness` |
| neighborhood effects / mobility | selection into neighborhoods; MTO-style design | `jue-identification` |
| quantitative spatial model (QSM) | what data identifies the structural parameters | `jue-theory-model` |
| transportation / commuting | network endogeneity; market-access measurement | `jue-identification` |

## How JUE differs from its siblings (keep this straight while routing)

- **RSUE** (Regional Science & Urban Economics, Elsevier) — leans more methodological / regional-science; JUE leads with the economics, not the spatial method.
- **Journal of Regional Science** — broader regional-science scope; JUE is the urban-economics field flagship.
- **JEG** (Journal of Economic Geography, OUP) — economic-geography framing (clusters, evolutionary geography), non-Elsevier; JUE is spatial-equilibrium urban economics.
- **JPubE** (Journal of Public Economics) — the tax/spending design leads; at JUE the spatial reallocation and capitalization lead.
- **AEJ: Applied** — rewards the causal design alone; JUE additionally requires a load-bearing urban mechanism.

## Anti-patterns

- Treating JUE as interchangeable with **RSUE** (more methods/regional-science), **Journal of Regional Science**, **JEG** (econ-geography, OUP), or **JPubE** (a place-based result is not automatically a public-finance paper)
- Polishing exhibits or prose while the spatial identification is still moving
- Deferring the replication folder to acceptance when the data is geocoded/restricted
- A national-level result dressed in geographic data with no urban mechanism

## Worked routing example (illustrative)

A user says: "My paper shows a new rail line raised nearby house prices, but a referee says the price jump could be sorting of richer households into the corridor, and the control areas may be contaminated by displaced demand." That is two distinct JUE pushbacks — *spatial sorting/selection* and *SUTVA/spillover contamination of controls* — both owned by `jue-identification` (design) and `jue-robustness` (spatial-spillover sensitivity, donut controls). Route to `jue-identification` first; only once the capitalization estimate is defended (say it settles at 4.5%, illustrative) return to `jue-tables-figures` for the map and `jue-rebuttal`.

## Two cross-cutting threads to keep alive throughout

- **Spatial inference** is not a single stage — it surfaces in `jue-identification` (Conley/spatial-cluster SEs), `jue-robustness` (cutoff sensitivity), and `jue-tables-figures` (reporting). Do not treat it as a one-time fix.
- **The replication path** for geocoded/restricted data touches `jue-topic-selection` (feasibility), `jue-replication-package` (deposit), and `jue-submission` (cover-letter exemption). Decide it early, not at acceptance.

## Minimal decision snippet

```
if decision_letter_arrived:          -> jue-rebuttal
elif ready_to_submit:                -> jue-submission
elif anticipating_referees:          -> jue-referee-strategy
elif data_is_geocoded_or_restricted: -> jue-replication-package
elif exhibits_have_no_map:           -> jue-tables-figures
elif spatial_robustness_open:        -> jue-robustness
elif need_spatial_model:             -> jue-theory-model
elif identification_shaky:           -> jue-identification
elif claim_or_positioning_fuzzy:     -> jue-literature-positioning
else:                                -> jue-topic-selection
```
