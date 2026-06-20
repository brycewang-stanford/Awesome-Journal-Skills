---
name: joe-workflow
description: Use when deciding which joe-* sub-skill to invoke next, or when sequencing a Journal of Econometrics (JoE) manuscript from methodological topic selection through revision rebuttal. Routes — it does not replace — the specialized skills.
---

# Journal of Econometrics Workflow Router (joe-workflow)

## Overview

This is the router. It tells you **which joe-* skill to use at the current stage** of a manuscript aimed at the *Journal of Econometrics* (JoE). Default assumption unless the user says otherwise: the target is JoE — an **Elsevier** journal (founded 1973) for **substantive econometric methodology**, covering identification, estimation, testing, decision, and prediction problems in economic research, plus applications of econometric techniques. The center of gravity is a **new estimator, test, identification result, or asymptotic theory**, defended with proofs and **Monte Carlo evidence**; purely empirical work without a methodological advance is typically out of scope.

Operational tells you are at JoE and not a sibling: current official pages split portal guidance
(ScienceDirect/new-submission links to **Editorial Manager**; JoE Google Sites and the
resubmission flow still reference **Editorial Express**), a **USD $75 nonrefundable fee** for new
submissions and resubmissions over one year, a **250-word** abstract, **single-anonymized** review
by a minimum of two referees after editor screening, Elsevier source-file rules plus Editorial
Express resubmission PDF norms, and three tracks: **Regular, Annals, and Themed Issues**.
Co-Editors-in-Chief: **Michael Jansson (UC Berkeley)** and **Aureo de Paula (UCL)**. Re-verify
volatile specifics (portal routing, editors, open themed calls) on the official pages.

## When to trigger

- The user asks "what should I do next?"
- A draft needs its current bottleneck diagnosed
- Work is ping-ponging between theory, simulation, illustration, and writing
- A JoE decision letter arrived and revision mode is needed

## Routing table

| Current symptom | Next skill |
|---|---|
| Idea feels incremental / "is this a real methodological contribution?" | `joe-topic-selection` |
| Contribution relative to the econometrics literature is fuzzy | `joe-literature-positioning` |
| Assumptions / regularity conditions / asymptotics not nailed down | `joe-identification-strategy` |
| Monte Carlo design or empirical illustration is thin | `joe-data-analysis` |
| The "why this matters to econometrics" framing is weak | `joe-contribution-framing` |
| Theorem/Monte-Carlo tables and figures are unclear | `joe-tables-figures` |
| Prose buries the result; proofs are hard to follow | `joe-writing-style` |
| Code/data archive and data-citation norms unclear | `joe-replication-and-data-policy` |
| Need to understand single-anonymized review / track choice | `joe-review-process` |
| Ready to submit; need live portal and file preflight | `joe-submission` |
| Received a revision request; need a response strategy | `joe-rebuttal` |

## Default order

1. `joe-topic-selection` — confirm a genuine methodological gap
2. `joe-literature-positioning` — stake the contribution against the frontier
3. `joe-identification-strategy` — assumptions, theorems, asymptotics, proof plan
4. `joe-data-analysis` — Monte Carlo design + empirical illustration
5. `joe-contribution-framing` — articulate the general lesson for econometrics
6. `joe-tables-figures` — size/power tables and theory-illustrating figures
7. `joe-writing-style` — make proofs legible; abstract + intro last
8. `joe-replication-and-data-policy` — assemble code/data per Elsevier norms
9. `joe-review-process` — pick the track; anticipate referees
10. `joe-submission` — live portal preflight (incl. fee/file proof)
11. `joe-rebuttal` — after the revision request

> `joe-writing-style` is a late polish. Do not rewrite the intro before the theorems and Monte Carlo are settled — the claims will change.

## Anti-patterns

- **Do not** skip `joe-literature-positioning` — referees judge the methodological novelty first
- **Do not** polish exhibits while a key regularity condition is still unproven
- **Do not** let `joe-rebuttal` draft a response before the revised manuscript exists
- **Do not** route a purely empirical paper here — without a methods advance it is out of scope
