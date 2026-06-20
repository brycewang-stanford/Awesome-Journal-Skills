---
name: ecj-workflow
description: Use when deciding which ecj-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a The Economic Journal (EJ) submission. Routes — it does not replace — the specialized skills.
---

# EJ Workflow Router (ecj-workflow)

## Overview

This is the router. It does not replace any specialized skill. It tells you **which ecj-* skill to use given where you are right now** in a manuscript aimed at *The Economic Journal* (EJ) — the **Royal Economic Society's** flagship general-interest journal, founded **1891** and published by **Oxford University Press**. EJ publishes across **all fields of economics**, theory and applied alike, for a **broad international readership**, and prizes work that is **technically well-crafted, makes a substantial contribution, and is of broad interest to economists at large**. Its house personality is **breadth of relevance plus clear exposition** — a sharp idea legible to a generalist beats a narrow result only specialists can read.

Default assumption: unless the user says otherwise, treat the target as EJ. Operational tells that you are at EJ and not a sibling: submission is through the **Editorial Express** portal (not ScholarOne); review is **single-blind** (referees are anonymous to authors; authors are *not* anonymized); there is an explicit **short-paper option in the AER:Insights style (<6,000 words, 5 exhibits)** alongside full-length articles; and accepted empirical, experimental, and numerical papers go through an **EJ Data Editor reproducibility check** with the replication package deposited to **Zenodo** or another trusted repository. Editor-in-chief as of the 2026-06-20 source refresh: **Francesco Lippi**; Data Editor: **Damian Clarke**. Re-verify volatile fees, charges, and rosters on the official OUP/RES pages.

## When to trigger

- The user asks "what should I do next?" on an EJ-targeted paper
- A draft is handed over and the current bottleneck is unclear
- Work is bouncing between modeling, empirics, and writing with no clear order
- An EJ decision letter (reject / R&R) has arrived and the user needs to switch into response mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Idea is narrow / not clearly of broad interest to economists at large | `ecj-topic-selection` |
| Lit review reads as a list; contribution not framed for a general audience | `ecj-literature-positioning` |
| Empirics are OLS + controls; causal claim not defended | `ecj-identification` |
| A reduced-form result has no model / mechanism behind it | `ecj-theory-model` |
| Theory/structural model present but its discipline is unclear | `ecj-theory-model` |
| Main result rests on a single specification | `ecj-robustness` |
| Tables overloaded; figures not carrying the economic story | `ecj-tables-figures` |
| Prose buries the idea; a generalist cannot follow the argument | `ecj-writing-style` |
| Accepted/near-accept; need a DCAS package for the EJ Data Editor / Zenodo | `ecj-replication-package` |
| Want to anticipate the breadth/identification objections a referee will raise | `ecj-referee-strategy` |
| Ready to submit via Editorial Express; need a single-blind preflight | `ecj-submission` |
| Received an R&R; need the response-letter strategy | `ecj-rebuttal` |

## Default order

1. `ecj-topic-selection` — lock a question of broad interest, and decide full-length vs. short paper
2. `ecj-literature-positioning` — situate the contribution for a general-interest readership
3. `ecj-identification` — make the causal/empirical claim credible
4. `ecj-theory-model` — the model or mechanism that gives the result its economic meaning
5. `ecj-robustness` — kill the alternative explanations a referee will float
6. `ecj-tables-figures` — finalize exhibits so each carries economic content
7. `ecj-writing-style` — make the idea land for a generalist (intro/abstract last)
8. `ecj-referee-strategy` — pre-mortem the report you expect, patch holes
9. `ecj-replication-package` — assemble data/code to DCAS standard for the EJ Data Editor
10. `ecj-submission` — Editorial Express preflight (single-blind, JEL, short-paper option)
11. `ecj-rebuttal` — after the R&R lands

> `ecj-writing-style` is a **late polish** stage; do not rewrite the intro before identification and the model settle. At EJ, *exposition is part of the contribution* — budget real time for it, but after the substance is sound.

## Decision heuristics

- "I have a clean causal effect but only specialists would care" → `ecj-topic-selection` (broaden the framing or rescope)
- "My result is sharp and self-contained but short" → `ecj-topic-selection` then `ecj-submission` (consider the short-paper route)
- "My intro cites everyone but never says what economics learns" → `ecj-literature-positioning`
- "DID uses TWFE with staggered timing and I haven't addressed heterogeneity bias" → `ecj-identification`
- "All my evidence is one regression" → `ecj-robustness`
- "A non-specialist reader gets lost by page 3" → `ecj-writing-style`
- "Submitting tomorrow" → `ecj-submission`
- "Got referee reports" → `ecj-rebuttal`

## Differences vs. JEEA / EER / top-5 stacks

EJ is a leading general-interest journal just below the top-5, with a distinct taste:

- **EJ**: the RES flagship, long history, breadth of relevance + clear exposition; theory and applied both core; an explicit short-paper option. A generalist must be able to read it.
- **JEEA** (EEA): European general-interest flagship; comparably broad, sometimes more selective/methodological in tilt.
- **EER**: European general-interest, often more field-specialized in practice; faster turnaround perception.
- **Top-5 (AER/QJE/JPE/Econometrica/REStud)**: a notch higher on novelty/importance; EJ welcomes substantial, broadly interesting work that may not clear that bar but is excellent and general.

If the paper is purely methodological/econometric, **The Econometrics Journal** (also RES) may fit better. If it is a narrow field contribution a generalist would skip, reconsider framing in `ecj-topic-selection` before targeting EJ.

## Anti-patterns

- **Do not** target EJ with a narrow result no generalist would finish — breadth of interest is a stated bar
- **Do not** waste effort anonymizing the manuscript — EJ review is **single-blind**, so author identity is expected
- **Do not** let `ecj-tables-figures` polish exhibits while the identification is still contested
- **Do not** let `ecj-rebuttal` draft a response letter before the manuscript itself has been revised
- **Do not** defer reproducible code to post-accept; the EJ Data Editor verifies the package before final publication
