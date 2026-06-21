---
name: aeri-workflow
description: Use when deciding which aeri-* sub-skill to invoke next, or when sequencing work on a short-format manuscript from topic selection through the conditional-accept response for an American Economic Review: Insights (AER: Insights) submission. Routes — it does not replace — the specialized skills.
---

# AER: Insights Workflow Router (aeri-workflow)

## Overview

This is the router. It tells you **which aeri-* skill to use at the current stage** of a manuscript aimed at *American Economic Review: Insights* (AER: Insights) — the AEA's **short-format**, general-interest journal (founded 2019) for papers built around **ONE clear, important, well-executed idea**, empirical, theoretical, or methodological. The bar is **AER-level importance compressed into a short paper**. AER: Insights is the short sibling of the *American Economic Review* (long, multi-result, flagship) and is general-interest, unlike the field-oriented full papers of the *AEJ* family.

Default assumption: unless the user says otherwise, treat the target as AER: Insights. The two operational tells that you are at AER: Insights and not AER or an AEJ: (1) a **hard length cap** — main text **≤7,000 words with no exhibits, minus 200 words per exhibit, maximum five exhibits**, abstract **≤100 words** — papers over the cap are returned unreviewed; (2) a **single insight** must carry the whole paper, with everything secondary pushed to the online Supplemental Appendix. Process tells: AEA **single-blind** review that is **fast and decisive — no traditional revise-and-resubmit; first decisions are conditional accept or reject**, and conditional accepts (usually an 8-week window) are normally **not** sent back to referees. Editor as of 2026: **Matthew Gentzkow** (lead editor beginning January 2024; founding editor Amy Finkelstein). Live-check volatile specifics on the official AEA pages.

## When to trigger

- The user asks "what should I do next?"
- A draft is over the word/exhibit cap or is sprawling into multiple results
- Work is ping-ponging between the core result, framing, exhibits, and the response letter
- An AER: Insights decision letter (conditional accept or reject) arrived

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Paper has several results / no single crisp insight; fit to short format unclear | `aeri-topic-selection` |
| Contribution vs. the closest published work is fuzzy or oversold | `aeri-literature-positioning` |
| The causal or parameter identification is shaky | `aeri-identification` |
| A model is present but bloated, or unclear what it must minimally show | `aeri-theory-model` |
| Robustness is sprawling; unclear what stays in-text vs. appendix | `aeri-robustness` |
| Over the five-exhibit budget; exhibits are dense or carry significance asterisks | `aeri-tables-figures` |
| Prose buries the result; abstract/intro do not lead with it; over word cap | `aeri-writing-style` |
| Data/code deposit, README, or AEA Data Editor prep | `aeri-replication-package` |
| Want to understand the fast review / conditional-accept-vs-reject odds | `aeri-referee-strategy` |
| Ready to submit via the AEA portal; need a preflight | `aeri-submission` |
| Received a conditional accept; need a short, decisive response | `aeri-rebuttal` |

## Default order

1. `aeri-topic-selection` — confirm ONE crisp, important, well-identified insight that stands alone
2. `aeri-literature-positioning` — stake the contribution in one or two paragraphs
3. `aeri-identification` — make the design or parameter identification clean and self-contained
4. `aeri-theory-model` — keep only the model the single insight requires
5. `aeri-robustness` — the few in-text checks that matter; rest to the appendix
6. `aeri-tables-figures` — at most five exhibits, no significance asterisks
7. `aeri-writing-style` — lead with the result; enforce the word budget (abstract + intro last)
8. `aeri-replication-package` — assemble the AEA-compliant data/code package
9. `aeri-referee-strategy` — calibrate expectations for the fast, decisive process
10. `aeri-submission` — AEA portal preflight (word count + exhibit count)
11. `aeri-rebuttal` — after the conditional accept

> `aeri-writing-style` is a late-stage polish, but the word cap is a constraint from day one — track it throughout, not at the end.

## Anti-patterns

- Treating AER: Insights like a short AER: keeping a second and third result instead of cutting to one
- Letting `aeri-tables-figures` polish a sixth exhibit that should not exist
- Skipping `aeri-replication-package` until acceptance — the AEA Data Editor checks **before** publication
- Planning for a multi-round R&R that AER: Insights does not offer

## Routing by paper archetype

The single insight differs by archetype; enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| one clean causal estimate (DiD / RDD / IV / experiment) | is the design credible AND is it a single headline number? | `aeri-topic-selection` → `aeri-identification` |
| a sharp theoretical result / impossibility | is the model minimal and the result surprising? | `aeri-theory-model` |
| a methodological point with one application | does the method change a substantive answer in few pages? | `aeri-identification` → `aeri-robustness` |
| a striking new fact / measurement | is the fact important enough to stand alone, and robust? | `aeri-topic-selection` → `aeri-robustness` |

## Worked routing example (illustrative)

A user says: "My field experiment has a clean main effect, but I also estimated three heterogeneity splits and a structural extension, and the draft is 9,500 words." That is the canonical AER: Insights problem — *one good insight buried under a multi-result, over-cap paper*. Route first to `aeri-topic-selection` to confirm the single headline effect is the paper, then `aeri-robustness` and `aeri-tables-figures` to move the heterogeneity and the structural extension to the Supplemental Appendix, then `aeri-writing-style` to land the draft under the 7,000-word (minus exhibits) cap.

## Minimal decision snippet

```
if decision_letter_arrived:          -> aeri-rebuttal
elif ready_to_submit:                -> aeri-submission
elif over_cap_or_too_many_exhibits:  -> aeri-tables-figures / aeri-writing-style
elif robustness_sprawling:           -> aeri-robustness
elif model_bloated:                  -> aeri-theory-model
elif identification_shaky:           -> aeri-identification
elif contribution_fuzzy:             -> aeri-literature-positioning
else:                                -> aeri-topic-selection
```
