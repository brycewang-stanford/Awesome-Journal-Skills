---
name: etp-workflow
description: Use when deciding which etp-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for an Entrepreneurship Theory and Practice (ETP) submission.
Routes — it does not replace — the specialized skills.
---

# ETP Workflow Router (etp-workflow)

## Overview

This is the router. It tells you **which etp-* skill to use at the current stage** of a manuscript aimed at *Entrepreneurship Theory and Practice* (ETP) — the **theory-and-practice flagship** of entrepreneurship research, published by **SAGE on behalf of Baylor University** and the **official journal of USASBE** (United States Association for Small Business and Entrepreneurship).
ETP rewards papers that **build entrepreneurship theory** — opportunity, effectuation, bricolage, entrepreneurial identity, cognition, family business, social/sustainable entrepreneurship — *and* draw out implications for practice, on the back of rigorous empirics (quantitative, qualitative, or mixed).

Default assumption: unless the user says otherwise, treat the target as ETP.
Operational tells that you are at ETP and not a sibling: review is **double-anonymized** (scrub author identity, not just the title page); the contribution is judged on **theoretical advance AND a defensible "implications for practice" section**; Original Articles run **≤40 pages double-spaced, 12pt Times New Roman, 1-inch margins** (Research Briefs ≤20 pages); references are **APA**; submission is via **ScholarOne Manuscripts** at mc.manuscriptcentral.com/ETP.
Johan Wiklund is listed as executive editor (待核实 — confirm the masthead at submission).
Re-verify volatile specifics on the SAGE author-instructions page (检索于 2026-06；以官网为准).

## When to trigger

- The user asks "what should I do next?" on an ETP-bound paper
- A draft needs its current bottleneck diagnosed
- Work is ping-ponging between theory, design, evidence, framing, and the response letter
- An ETP decision letter (usually R&R) arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Question is interesting but not clearly *entrepreneurship*, or outlet fit is uncertain | `etp-topic-selection` |
| The theoretical contribution is thin / "could be about any firm" | `etp-theory-development` |
| Contribution vs. JBV / SEJ / AMJ is fuzzy or the gap is undersold | `etp-literature-positioning` |
| Design can't observe the venturing process; selection/survival worries | `etp-methods` |
| Estimation, endpoints, event-history, or qualitative coding need work | `etp-data-analysis` |
| The "so what for theory AND practice" claim is not sharp | `etp-contribution-framing` |
| Exhibits dense; significance asterisks; figures don't show the mechanism | `etp-tables-figures` |
| Prose buries the idea; intro/abstract don't land the ETP voice | `etp-writing-style` |
| Ready to submit via ScholarOne; need a preflight + double-anonymization scrub | `etp-submission` |
| Want referee timeline / desk-reject odds / R&R norms | `etp-review-process` |
| Received an R&R; need a response-letter strategy | `etp-rebuttal` |

## Default order

1. `etp-topic-selection` — lock an entrepreneurship-central question
2. `etp-theory-development` — build the entrepreneurial mechanism (opportunity / effectuation / identity / family)
3. `etp-literature-positioning` — stake the gap vs. the entrepreneurship frontier
4. `etp-methods` — design that survives selection/survivorship and observes the process
5. `etp-data-analysis` — estimation / event-history / SEM / qualitative rigor
6. `etp-contribution-framing` — sharpen the theory + practice claim
7. `etp-tables-figures` — exhibits and a mechanism figure, no asterisk theater
8. `etp-writing-style` — make the idea land (abstract + intro last)
9. `etp-submission` — ScholarOne preflight + double-anonymization
10. `etp-review-process` — calibrate the developmental R&R
11. `etp-rebuttal` — after the decision letter

> `etp-writing-style` is a late-stage polish; do not rewrite the intro before theory, design, and evidence settle. The "implications for practice" section is a *contribution*, not boilerplate — sharpen it during framing, not the night before.

## Routing by paper archetype

ETP spans several research traditions, and the binding constraint differs by archetype. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| Inductive / qualitative process (opportunity, identity, sensemaking) | Process theory + trustworthiness, not a method label | `etp-theory-development` → `etp-methods` |
| Large-N archival venture panel (founding, growth, exit, financing) | Selection into founding + survivorship + endogeneity | `etp-methods` → `etp-data-analysis` |
| Experiment / cognition (effectuation, decision-making) | Construct anchored to a venture primitive; estimand | `etp-theory-development` → `etp-methods` |
| Family business / social-sustainable entrepreneurship | Why the family/social mechanism is *theory*, not context | `etp-theory-development` → `etp-literature-positioning` |
| Conceptual / theory paper | A genuinely new construct or reconciliation, not a review | `etp-theory-development` → `etp-contribution-framing` |
| Meta-analysis / replication | Boundary conditions and what *new theory* the synthesis yields | `etp-literature-positioning` → `etp-data-analysis` |

## Worked routing example (illustrative)

A user says: "My panel of nascent ventures shows that founder prior failure predicts faster pivoting, but a reviewer says it's just survivor bias and that the result 'isn't really about entrepreneurship theory.'" That is two distinct ETP pushbacks — a *design* threat (the nascent panel silently drops ventures that died before pivoting, owned by `etp-methods` → `etp-data-analysis` for an event-history fix) and a *theory* threat (the mechanism reads as generic learning, owned by `etp-theory-development`, which must tie pivoting to an entrepreneurial primitive like experiential learning under Knightian uncertainty).
Route to theory first to secure the entrepreneurial mechanism, then to methods to defend the sample; only once both settle do you return to `etp-contribution-framing` and `etp-rebuttal`.

## Anti-patterns

- Treating ETP like JBV (which welcomes a wider methodological/narrative range) or SEJ (strategy-of-entrepreneurship), or like AMJ (general management) — ETP wants entrepreneurship theory *with practice implications*
- Polishing prose before theory, design, and the evidence hierarchy are stable
- Treating "implications for practice" as a throwaway paragraph rather than part of the contribution
- Forgetting that review is double-anonymized — leaving author tells in the file
- Letting the appendix carry claims the main 40-page text must establish

## Minimal decision snippet

```
if decision_letter_arrived:          -> etp-rebuttal
elif ready_to_submit:                -> etp-submission
elif exhibits_or_significance:       -> etp-tables-figures
elif estimation_or_coding:           -> etp-data-analysis
elif design_or_selection:            -> etp-methods
elif claim_or_positioning_fuzzy:     -> etp-contribution-framing / etp-literature-positioning
elif mechanism_not_entrepreneurial:  -> etp-theory-development
else:                                -> etp-topic-selection
```
