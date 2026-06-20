---
name: jimf-workflow
description: Use when deciding which jimf-* sub-skill to invoke next, or when sequencing a Journal of International Money and Finance (JIMF) manuscript from topic through rebuttal. Routes — it does not replace — the specialized skills.
---

# JIMF Workflow Router (jimf-workflow)

## Overview

This is the router. It tells you **which jimf-* skill to use at the current stage** of a manuscript aimed at the *Journal of International Money and Finance* (JIMF) — Elsevier's field journal (ISSN 0261-5606; online 1873-0639; founded 1982) for **international monetary and financial economics**. The center of gravity is exchange rates, capital flows, the global financial cycle, cross-border banking, sovereign debt and risk, currency crises, and monetary-policy spillovers — i.e. *open-economy macro-finance with an asset-pricing and identification spine*. JIMF rewards a paper that takes a cross-country or high-frequency international design and answers a question a central banker, an IMF/BIS economist, or an international-finance professor would recognize as first-order.

The defining workflow tell: JIMF is an **Elsevier journal on Editorial Manager**, not a society journal. There is no membership gate, no submission fee for a standard paper (open-access APC only if the author chooses gold OA — 待核实), single-anonymized review is the Elsevier default (待核实 — confirm on the live Guide for Authors), and abstracts run **≤250 words** with required Highlights and CRediT author statements. Re-verify volatile specifics (editor names, exact APC, blinding) on the official ScienceDirect/Elsevier pages — access checked 2026-06.

## When to trigger

- The user asks "what should I do next?" on a JIMF-bound paper
- A draft's binding constraint (fit, identification, exhibits, prose, response letter) is unclear
- Work is ping-ponging between data/design, framing, exhibits, and the rebuttal
- The team is comparing JIMF with siblings (JIE, JME, JMCB, JFE) and needs to confirm fit

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Scope/outlet fit uncertain; might be a JIE/JME/JMCB paper | `jimf-topic-selection` |
| Contribution vs. the international-finance frontier is fuzzy | `jimf-literature-positioning` |
| The causal or structural credibility is the bottleneck | `jimf-identification` |
| Cross-country/high-frequency sample, measurement, or panel design is fragile | `jimf-empirical-design` |
| Results may be specification-, sample-, regime-, or inference-sensitive | `jimf-robustness` |
| Exhibits are dense or do not answer the question | `jimf-tables-figures` |
| Online appendix is too thin or sprawling; data/code deposit unclear | `jimf-internet-appendix` |
| Intro/abstract/Highlights miss the JIMF voice | `jimf-writing-style` |
| Close to submission; need an Editorial Manager preflight | `jimf-submission` |
| Likely referee objections should be pre-empted | `jimf-referee-strategy` |
| A decision letter arrived and needs a response plan | `jimf-rebuttal` |

## Default order

`jimf-topic-selection → jimf-literature-positioning → jimf-identification → jimf-empirical-design → jimf-robustness → jimf-tables-figures → jimf-internet-appendix → jimf-writing-style → jimf-submission → jimf-referee-strategy → jimf-rebuttal`

> `jimf-writing-style` is late-stage polish: do not rewrite the intro before identification, the cross-country design, and the robustness layer settle. `jimf-internet-appendix` runs in parallel with exhibits, not after acceptance — JIMF referees check the appendix.

## Routing by paper archetype

JIMF papers cluster into four archetypes; the first bottleneck differs by archetype, so enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| High-frequency identification (FX / policy-surprise event study, intraday) | event-window construction + surprise measurement | `jimf-identification` → `jimf-empirical-design` |
| Cross-country panel (capital flows, credit, GFCy exposure) | comparability + within-country vs. cross-country variation | `jimf-empirical-design` → `jimf-identification` |
| Policy / institutional natural experiment (capital controls, FXI, regime switch) | a clean control group + endogenous-policy concern | `jimf-identification` |
| Open-economy model + estimation (UIP deviations, term premia, sovereign default) | what data feature identifies each parameter | `jimf-identification` → `jimf-robustness` |

## Worked routing example (illustrative)

A user says: "My event study finds the dollar appreciates after Fed surprises, but a referee says my surprise measure is contaminated by the information channel and my country sample is unbalanced." Two distinct JIMF pushbacks — *surprise identification* (owned by `jimf-identification`, separating the pure monetary shock from the central-bank information shock) and *panel comparability* (owned by `jimf-empirical-design`, the unbalanced cross-country sample). Route to `jimf-identification` first; only once the cleaned surprise series is defended do you return to `jimf-empirical-design`, then `jimf-robustness` to show the dollar response survives sample and window choices.

## Stage gates (advance only when the gate is cleared)

Each handoff has a gate; do not advance a paper past a gate it has not cleared, and route back if a later stage exposes an earlier weakness.

| Gate | Cleared when |
|------|--------------|
| topic → positioning | the international margin is load-bearing, not decorative |
| positioning → identification | the contribution is one sentence against a named frontier program |
| identification → design | the global confounder (GFCy / common US shock) is addressed |
| design → robustness | measures, country set, and frequency are declared and defended |
| robustness → exhibits | the result survives dropping the obvious episode and the US |
| exhibits → appendix | the headline international effect is findable in seconds |
| appendix → style | the body is self-contained; the deposit traces to every number |
| style → submission | the abstract (≤250w), Highlights, and JEL land for a policy reader |

## Minimal decision snippet

```
if decision_letter_arrived:          -> jimf-rebuttal
elif ready_to_submit:                -> jimf-submission
elif anticipating_objections:        -> jimf-referee-strategy
elif intro_or_abstract_weak:         -> jimf-writing-style
elif appendix_or_deposit_unclear:    -> jimf-internet-appendix
elif exhibits_dense:                 -> jimf-tables-figures
elif result_fragile:                 -> jimf-robustness
elif data_or_measurement_shaky:      -> jimf-empirical-design
elif identification_shaky:           -> jimf-identification
elif contribution_fuzzy:             -> jimf-literature-positioning
else:                                -> jimf-topic-selection
```

## Anti-patterns

- Treating JIMF as interchangeable with **Journal of International Economics** (real trade + real open-economy macro), **JME** (domestic monetary/business-cycle), **JMCB** (domestic money/banking), or **JFE** (corporate/asset-pricing without the international margin)
- Polishing prose before the design, contribution, and evidence hierarchy are stable
- Letting the online appendix carry a claim the main text must establish
- Quoting volatile process facts (editor, APC, blinding) as permanent rather than marking 检索于 2026-06；以官网为准
- Submitting an applied-finance paper with no international/open-economy margin — JIMF's reason to exist

## Output format

```text
【Target】Journal of International Money and Finance (Elsevier)
【Archetype】high-frequency / cross-country panel / policy experiment / open-economy model
【Current bottleneck】fit / contribution / identification / design / robustness / exhibits / appendix / style / submission / revision
【Next skill】<one jimf-* skill>
【Reason】why this is the binding constraint now
【Source check】official facts verified or marked 待核实 / 检索于 2026-06
```
