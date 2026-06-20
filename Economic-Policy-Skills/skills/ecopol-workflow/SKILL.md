---
name: ecopol-workflow
description: Use when deciding which ecopol-* sub-skill to invoke next, or when sequencing manuscript work from topic pitch through post-panel revision for an Economic Policy (EP) manuscript. Routes — it does not replace — the specialized skills.
---

# Economic Policy Workflow Router (ecopol-workflow)

## Overview

This is the router. It tells you **which ecopol-* skill to use at the current stage** of a paper aimed at *Economic Policy* — the CEPR / CESifo / Sciences Po (Fondation Nationale des Sciences Politiques) policy-economics journal published by **Oxford University Press**. EP's identity is European, policy-first, and *accessible*: rigorous analysis of a current policy question written so that economists **and** policymakers can read it, with the heavy machinery pushed to an appendix.

What makes EP unlike any sibling is its lifecycle. EP does **not** run standard anonymous refereeing. Papers are selected by the **Managing Editor / Panel**, presented at the journal's **biannual conference (summer and winter)**, where **two invited discussants** debate each paper from an academic *and* a policy angle and act as the referees. The final paper is published **together with the discussants' comments and a summary of the panel discussion**, within ~6 months of presentation (检索于 2026-06；以官网为准). Since the 2025 relaunch as *Economic Policy: Papers on European and Global Issues*, the journal is **online-only and commissioned** — "all articles are invited by the Managing Editor"; **unsolicited submissions are not accepted** (检索于 2026-06；以官网为准). Treat `ecopol-submission` as the *pitch / commissioning + camera-ready* route, not an open portal.

Default assumption: unless the user says otherwise, the target is EP and the bottleneck is "will the Panel want this, and will it survive two discussants in front of a policy audience?"

## When to trigger

- The user asks "what should I do next?" on an EP-bound paper
- A draft's current bottleneck (fit, framing, evidence, exhibits, prose) needs diagnosing
- Work is ping-ponging between the policy question, the identification, the writing, and the discussant-proofing
- A commissioning invitation or a post-panel revision request arrived and the user must switch modes

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Not clearly a timely, important policy question the Panel would commission | `ecopol-topic-selection` |
| Contribution vs. the policy debate / adjacent journals is fuzzy | `ecopol-literature-positioning` |
| Causal or structural credibility is the binding constraint | `ecopol-identification` |
| The mechanism / model that organizes the policy logic is loose | `ecopol-theory-model` |
| Results may be specification-, sample-, or inference-fragile | `ecopol-robustness` |
| Exhibits are too technical for a policy reader or don't carry the message | `ecopol-tables-figures` |
| Main text reads like a tech report, not accessible policy prose | `ecopol-writing-style` |
| Data / code package and verification material need assembling | `ecopol-replication-package` |
| Need to anticipate the two discussants and the panel debate | `ecopol-referee-strategy` |
| Camera-ready / commissioning logistics need a final check | `ecopol-submission` |
| A post-panel / discussant revision request needs a response plan | `ecopol-rebuttal` |

## Default order

1. `ecopol-topic-selection` — lock a timely, Panel-worthy policy question
2. `ecopol-literature-positioning` — stake the contribution to the live policy debate
3. `ecopol-identification` — make the data-to-policy-claim mapping credible
4. `ecopol-theory-model` — the minimal model that disciplines the policy logic
5. `ecopol-robustness` — pre-empt the discussants' fragility tests
6. `ecopol-tables-figures` — exhibits a minister could read
7. `ecopol-writing-style` — accessible main text, technical appendix (do this late)
8. `ecopol-replication-package` — verification-ready data + code
9. `ecopol-referee-strategy` — war-game the two discussants + panel
10. `ecopol-submission` — commissioning / camera-ready preflight
11. `ecopol-rebuttal` — revise after the panel and discussant comments

> `ecopol-writing-style` is late polish; do not rewrite the intro before the identification and the headline policy number settle.

## Routing by paper archetype

The discussant duo and panel debate hit different papers at different seams. Read the archetype, enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| empirical causal evaluation of a policy | staggered-DID / weak-IV credibility under a hostile discussant | `ecopol-identification` |
| structural / quantitative policy model | what identifies parameters + counterfactual policy-invariance | `ecopol-theory-model` → `ecopol-identification` |
| macro / fiscal / monetary policy analysis | timeliness + the central policy number's robustness | `ecopol-topic-selection` → `ecopol-robustness` |
| cross-country / EU-institutional study | comparability of data + the "so what for European policy" | `ecopol-literature-positioning` |

## Worked routing example (illustrative)

A user says: "We were invited to present a paper on an EU minimum-wage directive at the winter conference; one likely discussant is a labor economist, the other sits in a finance ministry." That is the EP-specific bottleneck — *survive two discussants from two worlds*. The labor discussant will press identification (`ecopol-identification`) and robustness (`ecopol-robustness`); the ministry discussant will press the headline magnitude, the welfare/cost framing, and whether a non-economist can read it (`ecopol-tables-figures`, `ecopol-writing-style`). Route to `ecopol-referee-strategy` to map both personas, then to the two technical skills they will probe.

## Anti-patterns

- Treating EP like a journal with an open submission portal and anonymous referees — it is commissioned, panel-reviewed, with **named** discussants
- Polishing prose before identification and the central policy number are stable
- Confusing EP with **AEJ: Economic Policy** (AEA, anonymous refereeing, more technical), **Brookings Papers** (the US panel analogue), or **Journal of Public Economics** (field journal, no panel)
- Letting the technical appendix carry a claim the accessible main text must make to a policymaker

## Minimal decision snippet

```
if post_panel_revision:            -> ecopol-rebuttal
elif commissioned_camera_ready:    -> ecopol-submission
elif facing_the_two_discussants:   -> ecopol-referee-strategy
elif exhibits_too_technical:       -> ecopol-tables-figures
elif results_fragile:              -> ecopol-robustness
elif identification_shaky:         -> ecopol-identification
elif model_loose:                  -> ecopol-theory-model
elif contribution_fuzzy:           -> ecopol-literature-positioning
else:                              -> ecopol-topic-selection
```
