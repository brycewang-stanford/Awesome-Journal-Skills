---
name: jeem-workflow
description: Use when deciding which jeem-* sub-skill to invoke next, or when sequencing manuscript work from scoping through rebuttal for a Journal of Environmental Economics and Management (JEEM) submission. Routes — it does not replace — the specialized skills.
---

# JEEM Workflow Router (jeem-workflow)

## Overview

This is the router. It tells you **which jeem-* skill to use at the current stage** of a manuscript aimed at the *Journal of Environmental Economics and Management* (JEEM) — the flagship field journal in **environmental and resource economics**, published by **Elsevier** (ScienceDirect, ISSN 0095-0696), six issues a year. JEEM rewards papers where a real environmental or resource problem — pollution and climate, energy, natural-resource depletion, ecosystem services, environmental regulation, or the **value of a nonmarket good** — is attacked with credible economics: a causal design exploiting policy variation, a tractable resource/pollution-control model, or a revealed- or stated-preference valuation that pins down a welfare-relevant parameter.

Operational tells that you are at JEEM and not a sibling: it is a **field** journal (the environmental mechanism must carry the paper, not be window-dressing on a generic applied-micro result); **nonmarket valuation** (hedonics, travel cost, contingent valuation, discrete-choice experiments) is a first-class branch here in a way it is not at the general-interest journals; there is a **submission fee** and the paper may be **desk-rejected for scope or style non-compliance before review**; submission is via **Elsevier Editorial Manager**; JEEM has a long-standing **data-availability / replication** expectation. Editors as of 2026: **Roger von Haefen and Andreas Lange** (检索于 2026-06；以官网为准). Re-verify volatile specifics on the official ScienceDirect pages.

## When to trigger

- The user asks "what should I do next?" on a JEEM-bound paper
- A draft needs its current bottleneck diagnosed
- Work is ping-ponging between design, the environmental mechanism, exhibits, and the response letter
- A JEEM decision letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Scope/fit uncertain; is the environmental angle load-bearing? | `jeem-topic-selection` |
| Contribution vs. JAERE / JPubE / Ecological Economics is fuzzy | `jeem-literature-positioning` |
| Causal design (regulation DiD, permit-market, RD, weather/pollution IV) or valuation identification is shaky | `jeem-identification` |
| A resource/pollution-control or dynamic model needs sharpening | `jeem-theory-model` |
| Results may be specification-, sample-, spatial-, or inference-sensitive | `jeem-robustness` |
| Exhibits (maps, event-study plots, WTP distributions) do not answer the question | `jeem-tables-figures` |
| Intro/abstract miss the JEEM voice; mechanism→policy link is buried | `jeem-writing-style` |
| Data/code deposit, monitoring/satellite/admin data documentation | `jeem-replication-package` |
| Likely referee objections should be pre-empted | `jeem-referee-strategy` |
| Close to submission; need the Editorial Manager + fee + scope preflight | `jeem-submission` |
| A decision letter / referee report needs a response plan | `jeem-rebuttal` |

## Default order

1. `jeem-topic-selection` — lock the environmental/resource question and its policy stakes
2. `jeem-literature-positioning` — stake the contribution against the field and the siblings
3. `jeem-identification` — causal design or valuation identification
4. `jeem-theory-model` — resource/pollution-control or dynamic model where one is needed
5. `jeem-robustness` — specification, spatial, and inference stress tests
6. `jeem-tables-figures` — exhibits that show the environmental signal
7. `jeem-writing-style` — make the mechanism→welfare→policy chain land (intro last)
8. `jeem-replication-package` — assemble the data/code deposit (incl. restricted-data paths)
9. `jeem-referee-strategy` — anticipate the environmental-economics referee
10. `jeem-submission` — Editorial Manager preflight + fee + scope gate
11. `jeem-rebuttal` — after the decision letter

> `jeem-writing-style` is a late-stage polish; do not rewrite the intro before identification and the environmental mechanism settle.

## Routing by paper archetype

JEEM spans distinct branches, and the binding constraint differs by branch. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| environmental-policy causal design (regulation DiD, cap-and-trade, RD in standards) | staggered-DiD credibility / permit-market confounders | `jeem-identification` |
| revealed-preference valuation (hedonics, travel cost) | spatial sorting, omitted amenities, market definition | `jeem-identification` → `jeem-robustness` |
| stated-preference valuation (CV, discrete-choice experiments) | survey design, hypothetical bias, scope sensitivity | `jeem-identification` → `jeem-replication-package` |
| resource/pollution-control theory model | the model must generate a testable or policy-relevant comparative static | `jeem-theory-model` |
| climate / weather IV / damage estimation | exogeneity of weather shocks, adaptation, spatial SEs | `jeem-identification` → `jeem-robustness` |

## Anti-patterns

- Treating JEEM as interchangeable with **JAERE** (AERE's own journal — the sibling it is most confused with), **AEJ: Economic Policy**, **Journal of Public Economics**, **Ecological Economics**, or **Resource and Energy Economics**
- A generic applied-micro result with environment bolted on (it will read as a JPubE or AEJ paper that lost its way)
- Polishing prose before the environmental mechanism and identification are stable
- Skipping `jeem-replication-package` until acceptance — the data-availability expectation bites earlier
- Quoting fees/editors/limits as permanent when the source map marks them volatile

## Worked routing example (illustrative)

A user says: "My paper estimates that a county air-quality regulation raised house prices, but a referee says my hedonic could be picking up neighborhood sorting and my standard errors ignore spatial correlation." That is two distinct JEEM pushbacks — a **valuation-identification** threat (sorting / omitted amenities owned by `jeem-identification`) and an **inference** threat (spatial dependence owned by `jeem-robustness`). Route to identification first to defend the amenity capitalization claim, then to robustness for Conley/spatial SEs; only once the capitalization estimate is stable do you return to `jeem-tables-figures` to map it and `jeem-rebuttal` to defend it.

## Minimal decision snippet

```
if decision_letter_arrived:           -> jeem-rebuttal
elif ready_to_submit:                 -> jeem-submission
elif anticipating_referees:           -> jeem-referee-strategy
elif data_code_packaging:             -> jeem-replication-package
elif exhibits_unclear:                -> jeem-tables-figures
elif results_fragile:                 -> jeem-robustness
elif model_needs_work:                -> jeem-theory-model
elif identification_or_valuation:     -> jeem-identification
elif contribution_fuzzy:              -> jeem-literature-positioning
else:                                 -> jeem-topic-selection
```
