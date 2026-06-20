---
name: imfer-workflow
description: Use when deciding which imfer-* sub-skill to invoke next, or when sequencing manuscript work from topic through rebuttal for an IMF Economic Review (IMFER) submission. Routes — it does not replace — the specialized skills.
---

# IMFER Workflow Router (imfer-workflow)

## Overview

This is the router. It tells you **which imfer-* skill to use at the current stage** of a manuscript aimed at *IMF Economic Review* (IMFER) — the **International Monetary Fund's flagship scholarly journal**, published by **Palgrave Macmillan / Springer Nature** for the IMF, and the successor to *IMF Staff Papers*. IMFER's center of gravity is **international macroeconomics and finance with strong policy relevance**: exchange rates and capital flows, global imbalances, financial crises and contagion, sovereign debt, monetary and fiscal policy in open economies, IMF-program-relevant questions, and international spillovers. A distinctive pipeline is the **Jacques Polak Annual Research Conference (ARC)**, whose papers often appear as IMFER special issues.

Operational tells you are at IMFER and not a sibling or generic field journal: the audience is **part academic, part policy/institutional** — a referee reads as both a frontier researcher and someone who could brief an IMF mission; review is **double-blind** (anonymize the main file); house style is the **Chicago Manual of Style** with American spelling; the abstract is italicized and **JEL codes** are required. Editor-in-chief as of 2026: **Jesús Fernández-Villaverde** (检索于 2026-06；以官网为准). Re-verify volatile specifics on the Springer Nature IMFER pages.

## When to trigger

- The user asks "what should I do next?" on an IMFER-bound paper
- A draft needs its current bottleneck diagnosed (fit, design, theory, evidence, exhibits, style, submission)
- Work is ping-ponging between identification, the model, robustness, and the policy framing
- An IMFER decision letter arrived and the user must switch into revision mode
- The team is weighing IMFER against JIE, JIMF, JMCB, or *Economic Policy*

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Question feels narrow / not clearly international-macro with policy relevance | `imfer-topic-selection` |
| Contribution vs. JIE / JIMF / the IMF research frontier is fuzzy | `imfer-literature-positioning` |
| Cross-country causal design or policy-surprise identification is shaky | `imfer-identification` |
| The open-economy model / mechanism is loose or disconnected from the data | `imfer-theory-model` |
| Results may be specification-, sample-, or country-composition-sensitive | `imfer-robustness` |
| Exhibits are dense; significance asterisks still present; country coverage opaque | `imfer-tables-figures` |
| Prose buries the policy implication; abstract/intro do not land for a mixed audience | `imfer-writing-style` |
| Data, restricted IMF/central-bank paths, and code need packaging | `imfer-replication-package` |
| Likely objections should be war-gamed before submission | `imfer-referee-strategy` |
| Ready to submit via Editorial Manager; need a preflight | `imfer-submission` |
| An R&R arrived; need a response-letter strategy | `imfer-rebuttal` |

## Default order

1. `imfer-topic-selection` — lock the international-macro question with a policy hook
2. `imfer-literature-positioning` — stake the contribution vs. JIE/JIMF and the IMF frontier
3. `imfer-identification` — cross-country / high-frequency / crisis-event identification
4. `imfer-theory-model` — open-economy model that disciplines or interprets the estimate
5. `imfer-robustness` — specification, sample, and country-composition stability
6. `imfer-tables-figures` — exhibits with transparent country coverage, no asterisks
7. `imfer-writing-style` — make the idea land for the dual academic/policy audience (intro last)
8. `imfer-replication-package` — assemble the data/code package with restricted-data paths
9. `imfer-referee-strategy` — anticipate the dual-referee objections
10. `imfer-submission` — Editorial Manager double-blind preflight
11. `imfer-rebuttal` — after the R&R

> `imfer-writing-style` is a late polish; do not rewrite the intro before identification, the model, and robustness settle.

## Routing by paper archetype

IMFER spans several international-macro branches; the binding constraint differs by archetype.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| cross-country panel (capital flows, debt, crises) | country composition + spillover identification | `imfer-identification` → `imfer-robustness` |
| high-frequency policy-surprise (monetary/FX, spillovers) | clean surprise series + exclusion | `imfer-identification` |
| open-economy DSGE / international-finance model | parameter identification + counterfactual validity | `imfer-theory-model` → `imfer-identification` |
| crisis event study / narrative | event windows + confounding macro shocks | `imfer-identification` → `imfer-robustness` |
| ARC / special-issue invited paper | sharpening the policy contribution to the issue theme | `imfer-topic-selection` → `imfer-literature-positioning` |

## Worked routing example (illustrative)

A user says: "My cross-country panel shows capital-flow controls dampen crisis risk, but a referee says the result is driven by a handful of Asian economies and the controls are endogenous to the crisis." That is two distinct IMFER pushbacks — *country-composition fragility* (owned by `imfer-robustness`) and *policy endogeneity* (owned by `imfer-identification`). Route to identification first to defend the design, then to robustness to show the effect survives dropping the Asian bloc; only once the coefficient is stable do you return to `imfer-tables-figures` and `imfer-rebuttal`.

## Anti-patterns

- Treating IMFER like JIE (pure international trade/finance theory-and-empirics, less policy framing) or JIMF (broader, faster, less selective)
- Polishing prose before identification, the model, and robustness are stable
- Letting the online appendix carry a claim the main text must establish
- Forgetting the **policy "so what"** — a clean estimate with no IMF-relevant implication reads as the wrong journal
- Leaving author-identifying traces in a double-blind main file

## Minimal decision snippet

```
if decision_letter_arrived:          -> imfer-rebuttal
elif ready_to_submit:                -> imfer-submission
elif anticipating_referees:          -> imfer-referee-strategy
elif data_code_packaging:            -> imfer-replication-package
elif exhibits_or_significance:       -> imfer-tables-figures
elif results_fragile:                -> imfer-robustness
elif model_loose:                    -> imfer-theory-model
elif identification_shaky:           -> imfer-identification
elif claim_or_positioning_fuzzy:     -> imfer-contribution / imfer-literature-positioning
else:                                -> imfer-topic-selection
```
