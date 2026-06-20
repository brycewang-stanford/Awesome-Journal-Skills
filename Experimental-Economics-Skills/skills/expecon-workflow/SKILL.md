---
name: expecon-workflow
description: Use when deciding which expecon-* sub-skill to invoke next, or when sequencing manuscript work from design through rebuttal for an Experimental Economics (ExpEcon) submission. Routes — it does not replace — the specialized skills.
---

# ExpEcon Workflow Router (expecon-workflow)

## Overview

This is the router. It tells you **which expecon-* skill to use at the current stage** of a manuscript aimed at *Experimental Economics* — the **official journal of the Economic Science Association (ESA)** and the field's flagship for **experimental METHODS in economics**: lab experiments, lab-in-the-field, field experiments, market and game experiments, methodology of experimentation, and replications. The journal is defined by **method, not topic**. A clean public-goods design and a clean matching-market design compete in the same queue; what they share is craft.

Operational tells that you are at Experimental Economics and not a sibling: the journal moved from Springer to **Cambridge University Press in January 2025 (Vol. 28), fully open access (CC BY)** on behalf of the ESA (检索于 2026-06；以官网为准); submission runs through **Editorial Manager (editorialmanager.com/eec)** under **anonymous (double-blind) refereeing**, with **two editors** approving each accepted paper; **participant instructions must be supplied at submission**; and two hard gates dominate everything else — **real salient incentives** and the **ESA NO-DECEPTION norm**. A study that deceives participants is effectively a desk reject. Default assumption unless the user says otherwise: treat the target as Experimental Economics.

## When to trigger

- The user asks "what should I do next?" with an experiment aimed here
- A draft's binding constraint is unclear and is ping-ponging between design, analysis, exhibits, and the letter
- The team is weighing Experimental Economics against JEBO, GEB, AEJ: Micro, or JESA
- A decision letter arrived and the user must switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Unsure the question is a *method-defined* fit, or it reads as topic-first | `expecon-topic-selection` |
| Contribution vs. the experimental literature is fuzzy or oversold | `expecon-literature-positioning` |
| The behavioral/game-theoretic hypotheses being tested are loose | `expecon-theory-model` |
| Incentive compatibility, randomization, control, or the no-deception gate is shaky | `expecon-identification` |
| Power/MHT/comprehension/order effects/inference are the worry | `expecon-robustness` |
| Treatment-effect plots or tables are dense or mis-scaled | `expecon-tables-figures` |
| Prose buries the design; intro/abstract do not land | `expecon-writing-style` |
| z-Tree/oTree code, instructions, data deposit, or ESA repro prep | `expecon-replication-package` |
| Want to anticipate referee objections before submitting | `expecon-referee-strategy` |
| Ready to submit via Editorial Manager; need a preflight | `expecon-submission` |
| Received an R&R; need a response-letter strategy | `expecon-rebuttal` |

## Default order

1. `expecon-topic-selection` — confirm the method-defined fit and the cleanest treatment contrast
2. `expecon-literature-positioning` — stake the contribution vs. prior experiments
3. `expecon-theory-model` — pin the testable behavioral/game-theoretic hypotheses and predictions
4. `expecon-identification` — incentives, randomization, control, comprehension, **no-deception**
5. `expecon-robustness` — power/sample-size justification, MHT, order/learning, pooled-vs-session inference
6. `expecon-tables-figures` — treatment-comparison exhibits that carry the design
7. `expecon-writing-style` — make the design land (abstract + intro last)
8. `expecon-replication-package` — instructions + z-Tree/oTree code + data, ESA-compliant
9. `expecon-referee-strategy` — anticipate the experimentalist referee
10. `expecon-submission` — Editorial Manager preflight
11. `expecon-rebuttal` — after the R&R

> `expecon-writing-style` is late polish; do not rewrite the intro before design and analysis settle. Pre-registration (and any Registered Report intention) is decided at `expecon-topic-selection`/`expecon-identification`, never retrofitted.

## Anti-patterns

- Treating Experimental Economics like **JEBO** (broad behavioral, topic-defined, deception sometimes tolerated) — here method and the no-deception gate rule
- Treating it like **GEB** (a theory home where experiments are illustrative) or **AEJ: Micro** (where experiments support a broader applied/theory claim)
- Confusing it with **JESA**, the ESA's *other*, shorter-format journal — Experimental Economics is the ESA method flagship
- Polishing prose or exhibits while the treatment contrast or power justification is still moving
- Letting an appendix carry the comprehension checks, balance, or instructions the main text must establish

## Routing by paper archetype

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| Lab market / game experiment | clean treatment contrast + incentive-compatible payoffs | `expecon-identification` |
| Field / lab-in-the-field experiment | randomization integrity + attrition + ecological validity | `expecon-identification` → `expecon-robustness` |
| Methodology-of-experimentation paper | what existing designs get wrong + a demonstration | `expecon-topic-selection` → `expecon-theory-model` |
| Replication / Registered Report | fidelity to original protocol + pre-specified analysis + power | `expecon-topic-selection` → `expecon-robustness` |

## Worked routing example (illustrative)

A user says: "My ultimatum-game variant works, but a referee says the stranger-matching feedback might have misled subjects and the treatment effect could be a power artifact." Two distinct ExpEcon pushbacks — a possible **deception** concern (false feedback about other players) owned by `expecon-identification`, and **underpowering** owned by `expecon-robustness`. Resolve the deception gate first (it is binary and can sink the paper), then justify the sample (e.g., the design has 80% power to detect a 1.5-token gap at the session-clustered level, illustrative), then return to exhibits and the letter.

## Two gates that override the order

Most stages can be revisited out of sequence, but two checks dominate every route and should be confirmed before deep work on any skill:

- **No deception** — if any procedure deceives participants, no amount of analysis, framing, or robustness rescues the paper. Resolve at `expecon-identification` first; if it cannot be removed, the design must change.
- **Salient real incentives** — hypothetical or token stakes are not "incentivized" here. Confirm incentive compatibility for every elicited object before you optimize exhibits or prose.

A third, softer gate — **pre-registration / Registered Report intent** — is cheap before data collection and impossible to retrofit after. Decide it at `expecon-topic-selection`. When in doubt about where to enter, check these gates first; they reorder everything else.

## Output format

```text
【Target】Experimental Economics (ESA flagship; method-defined)
【Current bottleneck】fit / contribution / hypotheses / design / robustness / exhibits / style / package / submission / revision
【Next skill】<one expecon-* skill>
【Reason】why this is the binding constraint
【Gate check】incentives salient? no deception? instructions ready?
【Source check】official facts verified or marked 检索于 2026-06；以官网为准 / 待核实
```
