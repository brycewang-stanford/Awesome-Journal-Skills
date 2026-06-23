---
name: restud-workflow
description: Use when deciding which restud-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a The Review of Economic Studies (REStud) manuscript. Routes — does not replace — the specialized skills.
---

# REStud Workflow (restud-workflow)

## Overview

This is the router. It does not replace any specialized skill — it tells you which one to use next, and in what order.

Default assumption: unless the user names a different venue, the manuscript targets **The Review of Economic Studies (REStud)** — a top-5 general-interest journal (OUP, for the Review of Economic Studies Ltd; founded **1933** to advance **theoretical and applied** economics equally, especially by younger economists). REStud prizes a *clean, original contribution* — a new model, a new identification strategy, or a striking new empirical fact — presented rigorously and economically. It is not a finance-only stack, not a theory-only stack, and not a working-paper repository.

## REStud-specific anchors (carry these through every stage)

- **Identity:** founded 1933, theory and applied weighted equally; home of the **REStud Tour** (former May Meetings, annual since 1989) for promising young economists — calibrate ambition to that bar.
- **Submission:** **Editorial Express** portal, **USD 250 fee** (reduced **USD 150** if every author is a student / within 6 years of PhD / in a low-or-middle-income economy; rate effective 1 June 2026), **double-anonymous** review, **Harvard author-date** references, JEL codes, **~45-page** limit; editors desk-reject ~20–23% before refereeing.
- **Replication:** the **Data Editor (Miklós Koren)** runs an **AEA DCAS** pre-publication reproducibility check; packages deposit at **Zenodo**.
- **Editors (2026):** Joint Managing Editors include Jan De Loecker, Antonio Penta, Jakub Steiner (verify the full current roster).

## When to Use

- The user asks "what should I work on next?"
- The user dumps a draft and you must decide where the bottleneck is
- The user is rotating between theory, empirics, writing, and revision and loses track of the stage
- A referee report has arrived and the work mode must switch from drafting to rebuttal
- The user is preparing a job-market paper for the REStud "May Meetings" / Tour pipeline and wants the manuscript at REStud standard

## Routing Map

| Current symptom                                                          | Next skill                     |
|--------------------------------------------------------------------------|--------------------------------|
| Idea is fuzzy; the one-sentence contribution will not compress           | `restud-topic-selection`       |
| Related-work positioning is thin; closest papers not confronted          | `restud-literature-positioning`|
| Empirical design is the bottleneck (DID / IV / RDD / RCT / structural)   | `restud-identification`        |
| The paper is theory or has a model whose proofs need an online appendix  | `restud-theory-model`          |
| Main results exist but referee-anticipating checks are missing or fragile| `restud-robustness`            |
| Tables are oversized / footnote-bloated; figures do not carry the result | `restud-tables-figures`        |
| Prose is bloated; abstract over length; contribution buried              | `restud-writing-style`         |
| Preparing the data/code deposit or auditing reproducibility              | `restud-replication-package`   |
| Want to anticipate who referees and what they will demand                | `restud-referee-strategy`      |
| Final preflight before clicking submit (format, length, anonymity)       | `restud-submission`            |
| A referee report / R&R arrived and a response letter is needed           | `restud-rebuttal`              |

## Default Sequence

For a typical REStud-track manuscript, prefer this order:

1. `restud-topic-selection` — fix the one-sentence original contribution *before* anything else
2. `restud-literature-positioning` — locate the contribution against the closest 3–5 papers
3. `restud-identification` — for empirical papers, stress-test the design; if it fails here, no later skill saves the paper
4. `restud-theory-model` — for theory papers (or empirical papers with a model), build the model and route proofs to the online appendix
5. `restud-robustness` — anticipate the checks the demanding median REStud referee will require
6. `restud-tables-figures` — finalize exhibits so each one carries a result
7. `restud-writing-style` — only now polish prose, abstract, and introduction
8. `restud-replication-package` — assemble the deposit while results are fresh in code
9. `restud-referee-strategy` — map the likely referee pool and pre-empt objections
10. `restud-submission` — final preflight: length, anonymity, format, files
11. `restud-rebuttal` — after review, revise the manuscript first, then write the letter

> `restud-identification` and `restud-theory-model` are **parallel branches**: empirical papers lean on the first, theory papers on the second, and many REStud papers (theory-with-empirics) need both. `restud-writing-style` is a **late polish** — do not run it before the contribution and design are stable.

## Decision Cues

If the user says...

- *"I have data but no story"* → `restud-topic-selection`
- *"My closest paper is in QJE 2022 and I don't know what I add"* → `restud-literature-positioning`
- *"My DiD has staggered treatment and TWFE"* → `restud-identification`
- *"My model has a proposition but no proof section"* → `restud-theory-model`
- *"A referee will say the result is driven by X"* → `restud-robustness`
- *"My table 3 has 14 columns"* → `restud-tables-figures`
- *"My intro is 5 pages and buries the contribution"* → `restud-writing-style`
- *"I got a conditional accept; I need the data deposit"* → `restud-replication-package`
- *"Who is going to referee this and what will they want?"* → `restud-referee-strategy`
- *"I'm submitting tomorrow"* → `restud-submission`
- *"I got an R&R with three reports"* → `restud-rebuttal`

## Differences vs. Other Top-5 Stacks

REStud overlaps heavily with AER / QJE / JPE / Econometrica in standards, but its center of gravity differs:

- vs **AER**: AER weights cross-subfield interest and policy salience; REStud equally welcomes a clean theoretical or methodological contribution with no policy hook, and is famously *friendly to young scholars* — the **REStud Tour / May Meetings** (annual since 1989) showcase graduating PhD job-market work.
- vs **Econometrica**: Econometrica tolerates very heavy formal machinery as the contribution itself; REStud wants the economics payoff of the theory to be legible.
- vs **JPE**: JPE has a price-theory / Chicago tilt; REStud is field-agnostic and European-rooted.

If the paper is finance-specific (JF / JFE / RFS) or theory so abstract it is really a math paper, a different stack fits better.

## Anti-Patterns

- Polishing prose (`restud-writing-style`) before the identification or model is stable
- Treating `restud-theory-model` as optional for an empirical paper that has a model — REStud referees check that the model's assumptions map to the empirics
- Assembling the replication package only after acceptance — REStud's **Data Editor (Miklós Koren) runs an AEA DCAS reproducibility check before publication** (Zenodo deposit), so it is part of the production timeline, not an afterthought
- Writing the rebuttal against the old draft instead of the revised manuscript
- Skipping `restud-referee-strategy` because "the design is obviously fine" — REStud referees are demanding and develop strong papers across rounds

## Handoff Contract

Whenever this skill is invoked, end with:

```text
NEXT SKILL: <restud-skill-name>
REASON: <one sentence>
INPUTS NEEDED: <artifacts the next skill needs>
```
