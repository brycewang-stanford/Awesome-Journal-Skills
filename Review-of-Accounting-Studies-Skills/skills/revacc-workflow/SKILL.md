---
name: revacc-workflow
description: Use when deciding which revacc-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Review of Accounting Studies (RAST) submission. Routes — it does not replace — the specialized skills.
---

# RAST Workflow Router (revacc-workflow)

## Overview

This is the router. It tells you **which revacc-* skill to use at the current stage** of a manuscript aimed at *Review of Accounting Studies* (RAST) — the **Springer** top-tier accounting journal edited by Paul Fischer (待核实; 检索于 2026-06；以官网为准). RAST sits squarely in financial accounting and reporting: disclosure, earnings quality and management, valuation and capital markets, analysts and forecasting, audit, taxation, and the economic consequences of accounting. Crucially, RAST publishes **three method lanes side by side** — empirical archival, **analytical (modeling)**, and some experimental work — and is known for methodological rigor with a relatively fast, well-run process.

Default assumption: unless the user says otherwise, treat the target as RAST. Operational tells that you are at RAST and not a sibling or a generic top journal: submission runs through **Editorial Manager** (Springer), with a **submission fee of USD $500 payable within 7 days or the paper is withdrawn** (待核实; 检索于 2026-06); review is **double-blind**; the journal advertises **prompt turnaround and an explicit tradition of making an accept/reject decision on the first round for most manuscripts** (rather than many R&R cycles); abstracts run roughly **150–250 words** (待核实); and there is a recurring **RAST Conference** whose accepted papers feed a **conference issue** while all conference submissions are also considered for the regular journal. Re-verify volatile specifics on the official Springer page.

## When to trigger

- The user asks "what should I do next?" with a half-built RAST manuscript
- A draft's current bottleneck — fit, model, identification, evidence, exhibits, prose — is unclear
- Work is ping-ponging between modeling/estimation, framing, writing, and the response letter
- A RAST decision letter arrived (often a terse first-round accept/reject) and the user must decide whether to rebut, revise, or redirect

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Question feels generic, atheoretical, or not clearly financial-accounting | `revacc-topic-selection` |
| Predictions are bald associations; no friction/model; analytical paper lacks a clean equilibrium | `revacc-theory-development` |
| Contribution vs. TAR/JAR/JAE/CAR and the disclosure/earnings frontier is fuzzy | `revacc-literature-positioning` |
| Identification design (DiD, IV, RDD, event study) or analytical solution concept is shaky | `revacc-methods` |
| Estimation, clustering, construct measurement, robustness, or proxy validation need work | `revacc-data-analysis` |
| Results exist but the "so what for accounting" is thin | `revacc-contribution-framing` |
| Exhibits are dense, off house style, or do not answer the question | `revacc-tables-figures` |
| Prose buries the result; intro/abstract do not land | `revacc-writing-style` |
| Ready to submit via Editorial Manager; need a preflight and the fee/anonymization check | `revacc-submission` |
| Want to understand RAST's first-round-decision norm, conference path, or timeline | `revacc-review-process` |
| Received an R&R (rarer at RAST); need a response-letter strategy | `revacc-rebuttal` |

## Default order

1. `revacc-topic-selection` — lock a contribution-driven financial-accounting question with RAST fit
2. `revacc-theory-development` — build the friction/mechanism, or the analytical model and propositions
3. `revacc-literature-positioning` — stake the contribution vs. the accounting frontier and the siblings
4. `revacc-methods` — design identification (or fix model primitives) matched to the question
5. `revacc-data-analysis` — estimator, FE, clustering, construct validation, robustness
6. `revacc-contribution-framing` — turn results into an explicit accounting contribution
7. `revacc-tables-figures` — finalize main exhibits in accounting house style
8. `revacc-writing-style` — full-manuscript prose polish (abstract + intro last)
9. `revacc-submission` — Editorial Manager preflight (anonymization, fee, files)
10. `revacc-review-process` — calibrate expectations for the first-round-decision model
11. `revacc-rebuttal` — after an R&R, revise then draft the response

> `revacc-tables-figures` and `revacc-writing-style` are **late-stage polish**. Do not invoke them while identification, the model, or the contribution is still unsettled.

## Routing by paper archetype

RAST's three lanes have different first bottlenecks. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| empirical archival (disclosure/earnings/valuation event) | identification credibility + construct measurement | `revacc-methods` → `revacc-data-analysis` |
| analytical / disclosure model | minimal primitives, equilibrium, comparative statics with an accounting payoff | `revacc-theory-development` |
| analyst/forecasting capital-markets | proxy validity (I/B/E/S), confounding events, return-window choices | `revacc-data-analysis` |
| experimental (investor/auditor/manager) | construct manipulation, channel isolation, power | `revacc-theory-development` → `revacc-methods` |

## Difference vs. the AAA/Chicago/Elsevier family

- **RAST** is the **Springer** top accounting outlet that explicitly welcomes **both archival and analytical** work, with a fast first-round-decision culture and the RAST Conference path.
- **TAR** (The Accounting Review, AAA) is method-agnostic and contribution-first but archival-dominated; **JAR** (Chicago Booth/Wiley) prizes identification and posts a data-and-code package; **JAE** (Elsevier) leans economics-of-accounting with an archival house style and the JAE data archive; **CAR** (CPA Canada/Wiley) is broad and methodologically catholic. If your study is purely a methods demonstration with no accounting payoff, RAST is the wrong venue.

## Worked routing example (illustrative)

A user says: "My analytical disclosure model solves, but a referee says the equilibrium is not the *minimal* structure and the comparative static has no obvious accounting reading." That is two RAST-analytical pushbacks — *model not parsimonious* and *no accounting payoff* — both owned by `revacc-theory-development`, with positioning against the disclosure-theory frontier in `revacc-literature-positioning`. Route there first; only once the proposition is the leanest one that delivers an accounting-relevant comparative static do you move to `revacc-tables-figures` (for the equilibrium illustration) and `revacc-writing-style`.

## Anti-patterns

- Treating RAST as **archival-only** and shoehorning an analytical paper through an empirical chain (or vice versa)
- Treating RAST like TAR, JAR, JAE, or CAR — different owners, portals, data policies, and decision cultures
- Polishing prose or exhibits before identification, the model, and the contribution are stable
- Assuming many R&R rounds: RAST's first-round-decision norm raises the bar on the *initial* submission

## Output format

```text
【Target】Review of Accounting Studies (Springer)
【Lane】archival / analytical / experimental
【Current bottleneck】fit / model / identification / evidence / exhibits / style / submission / revision
【Next skill】<one revacc-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
