---
name: jmgmt-workflow
description: Use when deciding which jmgmt-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Journal of Management (JOM) submission. Routes — it does not replace — the specialized skills.
---

# JOM Workflow Router (jmgmt-workflow)

## Overview

This is the router. It tells you **which jmgmt-* skill to use at the current stage** of a manuscript aimed at the *Journal of Management* (JOM) — the **Southern Management Association's** general-management flagship, published by **SAGE**. JOM spans organizational behavior, human resource management, strategic management, entrepreneurship, and research methods (plus related industrial/organizational psychology). It rewards a clear **theoretical contribution** paired with **rigorous method**, and — uniquely among the field's top journals — it runs a celebrated **review-article and meta-analysis tradition**: invited and unsolicited Review Issues appear biannually (January and July).

Default assumption: unless the user says otherwise, treat the target as JOM. Operational tells that you are at JOM and not a sibling or a generic top journal: a **hard 50-page limit** that includes *everything* (text, notes, references, tables, figures); a **15-word title** and **250-word abstract** cap entered in the portal; **masked (double-blind) review** enforced by an **anonymized data transparency table** that discloses overlap with the authors' other papers; **APA (7th) style**; and a real appetite for **systematic reviews / meta-analyses** as standalone contributions. Editor-in-Chief: **Cynthia E. Devers (Virginia Tech)** (检索于 2026-06；以官网为准). Re-verify volatile specifics on the SAGE JOM author-instructions page.

## When to trigger

- The user asks "what should I do next?" on a JOM manuscript
- A draft needs its current bottleneck diagnosed
- Work is ping-ponging between theory, design, analysis, framing, and the response letter
- A JOM decision letter arrived and the user needs to switch into revision mode
- The team is deciding between an empirical paper and a review/meta-analysis route

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Scope/fit uncertain, or empirical-vs-review path undecided | `jmgmt-topic-selection` |
| Hypotheses are bald predictions; mechanism/boundaries thin | `jmgmt-theory-development` |
| Contribution vs. adjacent journals (AMJ/SMJ/JMS) is fuzzy | `jmgmt-literature-positioning` |
| Design, construct validity, CMB, or endogeneity need work | `jmgmt-methods` |
| SEM/HLM/regression/meta-analysis estimation needs review | `jmgmt-data-analysis` |
| The "what new theory do we learn?" statement is missing | `jmgmt-contribution-framing` |
| Exhibits dense; correlation table / path model unclear | `jmgmt-tables-figures` |
| Intro/abstract miss the JOM voice; over 50 pages | `jmgmt-writing-style` |
| Ready to submit; need a SAGE/ScholarOne preflight | `jmgmt-submission` |
| Want masked-review timeline / desk-reject odds | `jmgmt-review-process` |
| Received an R&R; need a response-letter strategy | `jmgmt-rebuttal` |

## Default order

1. `jmgmt-topic-selection` — lock the question and the empirical-vs-review path
2. `jmgmt-theory-development` — build the mechanism and a priori hypotheses (or the review's organizing framework)
3. `jmgmt-literature-positioning` — stake the contribution vs. AMJ/SMJ/JMS/Org Science
4. `jmgmt-methods` — match design to theory; CMB, endogeneity, levels, measurement
5. `jmgmt-data-analysis` — SEM/HLM/regression or meta-analytic estimation
6. `jmgmt-contribution-framing` — the theoretical-contribution statement and discussion
7. `jmgmt-tables-figures` — correlation table, path/model figure, forest plots
8. `jmgmt-writing-style` — make the idea land; enforce the 50-page limit (abstract last)
9. `jmgmt-submission` — SAGE/ScholarOne preflight + data transparency table
10. `jmgmt-review-process` — calibrate masked-review expectations
11. `jmgmt-rebuttal` — after the R&R

> `jmgmt-writing-style` is a late-stage polish; do not rewrite the intro before theory, design, and analysis settle. The 50-page guillotine often forces cuts after the contribution is fixed, not before.

## Routing by paper archetype

JOM publishes several distinct article types, and the binding constraint differs by type. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| Micro empirical (OB/HR, survey/experiment) | construct validity + common-method bias + multilevel structure | `jmgmt-methods` |
| Macro empirical (strategy/entrepreneurship, archival panel) | endogeneity / identification + the theory it tests | `jmgmt-theory-development` → `jmgmt-methods` |
| Meta-analysis | coding protocol, artifact corrections, theory the synthesis advances | `jmgmt-data-analysis` (then `jmgmt-contribution-framing`) |
| Narrative / systematic review (for a Review Issue) | the organizing framework and forward agenda, not new data | `jmgmt-theory-development` → `jmgmt-contribution-framing` |

## Worked routing example (illustrative)

A user says: "My HR survey shows abusive supervision predicts turnover intention, but a reviewer says it's single-source cross-sectional and the theory is just labeled 'social exchange.'" That is two JOM pushbacks — *common-method bias / causal-design weakness* (owned by `jmgmt-methods`) and *theory invoked by name but not used* (owned by `jmgmt-theory-development`). Route to theory first to specify the exchange mechanism and a boundary, then to methods to add a time-lagged or multi-source wave; only once both settle do `jmgmt-data-analysis` (re-run the SEM) and `jmgmt-tables-figures` follow.

## Anti-patterns

- Treating JOM as interchangeable with **AMJ** (the AOM empirical flagship), **SMJ** (strategy-only), **JMS** (Wiley/European, more pluralist/qualitative), or **Organization Science** — JOM is the SMA general-management outlet that *also* runs strong reviews and meta-analyses
- Polishing prose before the theory, design, and evidence hierarchy are stable
- Forgetting the **data transparency table** and the **50-page** guillotine until the night before submission
- Submitting a meta-analysis with no theoretical advance — JOM wants synthesis that *moves theory*, not a coefficient census

## Minimal decision snippet

```
if decision_letter_arrived:        -> jmgmt-rebuttal
elif ready_to_submit:              -> jmgmt-submission
elif exhibits_unclear:             -> jmgmt-tables-figures
elif over_50pp_or_intro_flat:      -> jmgmt-writing-style
elif estimation_or_meta:           -> jmgmt-data-analysis
elif design_or_cmb_or_endog:       -> jmgmt-methods
elif theory_thin:                  -> jmgmt-theory-development
elif contribution_fuzzy:           -> jmgmt-contribution-framing / jmgmt-literature-positioning
else:                              -> jmgmt-topic-selection
```
