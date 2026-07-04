---
name: qje-workflow
description: Use when deciding which qje-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Quarterly Journal of Economics (QJE) submission. Routes — it does not replace — the specialized skills.
---

# QJE Workflow Router (qje-workflow)

## Overview

This is the router. It does not replace any specialized skill. It tells you **which qje-* skill to use at the current stage** of a manuscript aimed at the *Quarterly Journal of Economics*.

Default assumption: unless the user says otherwise, treat the target as QJE — the oldest English-language economics journal (founded 1886, published by Oxford University Press for the **Harvard** Department of Economics), a top-5 general-interest journal that rewards a **big conceptual idea backed by clean, credible empirics**. Its five Harvard-based Editors (Barro, Katz, Nunn, Shleifer, Stantcheva as of 2024) desk-decide in roughly **two weeks** — the fastest at desk among the top-5 — and desk-reject the majority; unconditional acceptance is only **~1-4%**. There is **no submission fee**; initial submission is a **single PDF via Editorial Express** under **double-blind** review. Re-verify volatile specifics (current editors, fee, deposit policy) on the official journal page before relying on them.

## When to trigger

- The user asks "what should I do next?"
- The user hands over a draft and needs the current bottleneck diagnosed
- Work is ping-ponging between empirics, theory, writing, and response letters
- A QJE decision letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom                                                      | Next skill                   |
|----------------------------------------------------------------------|------------------------------|
| Idea feels small / "so what?" unclear / not obviously top-5 material | `qje-topic-selection`        |
| Contribution relative to the literature is fuzzy or undersold        | `qje-literature-positioning` |
| Empirics rest on OLS + controls; causal claim is undefended          | `qje-identification`         |
| Reduced-form result has no conceptual frame / no model               | `qje-theory-model`           |
| Main result exists but robustness / appendix is thin                 | `qje-robustness`             |
| Tables are dense; paper is not figure-forward enough                 | `qje-tables-figures`         |
| Prose buries the idea; abstract/intro do not land the "big question" | `qje-writing-style`          |
| Accepted-stage data/code deposit, or pre-empting referee replication | `qje-replication-package`    |
| Want to anticipate referee objections before submitting              | `qje-referee-strategy`       |
| Ready to submit via Editorial Express; need a preflight checklist    | `qje-submission`             |
| Received an R&R; need a response-letter strategy                     | `qje-rebuttal`               |

## Default order

1. `qje-topic-selection` — lock the big question + the conceptual takeaway
2. `qje-literature-positioning` — stake the contribution against the frontier
3. `qje-identification` — make the causal design bulletproof
4. `qje-theory-model` — give the result a conceptual frame / model
5. `qje-robustness` — build the extensive appendix QJE expects
6. `qje-tables-figures` — finalize figure-forward main exhibits
7. `qje-writing-style` — make the prose land the idea (abstract + intro last)
8. `qje-replication-package` — assemble the deposit (also revisit at acceptance)
9. `qje-referee-strategy` — war-game referee objections pre-submission
10. `qje-submission` — Editorial Express preflight
11. `qje-rebuttal` — after the R&R

> `qje-writing-style` is a late-stage polish. Do not rewrite the intro before the identification is settled — the argument will change.

## Pipeline status check

Fill this in before asking "what next?" — work top-down and take the **first NO** as the route.

```text
QJE PIPELINE STATUS — first NO wins
Big question answerable in one sentence a non-specialist cares about?  NO -> qje-topic-selection
Delta vs. the frontier papers named, not just cited?                   NO -> qje-literature-positioning
Causal design survives the toughest referee attack you can imagine?    NO -> qje-identification
Headline coefficient has a conceptual frame or model behind it?        NO -> qje-theory-model
Online appendix already covers the checks referees will demand?        NO -> qje-robustness
Main exhibits figure-forward; no table past ~6 columns?                NO -> qje-tables-figures
Abstract states question, design, and magnitude in plain prose?        NO -> qje-writing-style
QJE Dataverse deposit (data + code) assembled and re-runnable?         NO -> qje-replication-package
Referee objections war-gamed and pre-empted in the draft?              NO -> qje-referee-strategy
Single anonymized PDF ready for Editorial Express (no fee due)?        NO -> qje-submission
Decision letter with an R&R in hand?                                   YES -> qje-rebuttal
```

## Decision shortcuts

- "I have data but no big idea" → `qje-topic-selection`
- "I don't know who I'm building on or beating" → `qje-literature-positioning`
- "My DID is TWFE on staggered timing" → `qje-identification`
- "My result is a coefficient with no story" → `qje-theory-model`
- "A referee will ask for X robustness" → `qje-robustness`
- "My main table has 9 columns" → `qje-tables-figures`
- "The abstract doesn't state the finding" → `qje-writing-style`
- "Editor wants data and code" → `qje-replication-package`
- "Submitting tomorrow" → `qje-submission`
- "Got three referee reports" → `qje-rebuttal`

## Differences vs. other top-5 stacks

If the paper is methods-first (a new estimator, an asymptotic theorem) it belongs at *Econometrica*; if it is a structural-IO or macro-quantitative paper leading with a calibrated model, *JPE* or *Econometrica* may fit better. QJE's comparative advantage is the **big empirical-micro question with a clean natural experiment and a broad lesson** (labor, public, development, behavioral, economic history, political economy) — the lineage runs from Akerlof's "Market for 'Lemons'" (QJE 1970) and Mankiw–Romer–Weil (QJE 1992) to Chetty–Hendren–Kline–Saez on mobility (QJE 2014). When in doubt, ask whether a smart non-specialist would care about the *answer*, not the *technique*. Operational tells that you are at QJE and not a sibling: no submission fee, one PDF via Editorial Express, double-blind review, ~2-week desk decisions, deposit to the **QJE Dataverse** (not openICPSR).

## Anti-patterns

- **Do not** skip `qje-literature-positioning` and jump to identification — QJE referees judge the contribution first
- **Do not** let `qje-tables-figures` polish exhibits while the identification is still shaky
- **Do not** let `qje-rebuttal` draft a response letter before the revised manuscript exists
- **Do not** treat `qje-robustness` as optional — a thin online appendix reads as an incomplete paper here
