---
name: jpube-workflow
description: Use when deciding which jpube-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Journal of Public Economics (JPubE) submission. Routes — it does not replace — the specialized skills.
---

# JPubE Workflow Router (jpube-workflow)

## Overview

This is the router. It does not replace any specialized skill. It tells you **which jpube-* skill to use at the current stage** of a manuscript aimed at the *Journal of Public Economics* (JPubE).

Default assumption: unless the user says otherwise, treat the target as JPubE — Elsevier's flagship field journal in **public economics / public finance**, founded in **1972 by Tony Atkinson** and currently edited by **Nathaniel Hendren (MIT)** and **Wojciech Kopczuk (Columbia)**. The journal covers the economic role of government — taxation, public expenditure, social insurance, redistribution, externalities, public goods, and fiscal policy — applying modern theory and quantitative methods to policy questions of interest to an international readership. Operational tells you are at JPubE and not a free top-5 generalist: a **US$165 submission fee** (US$82.50 for students; waived for Elsevier article-transfer submissions), submission via **Editorial Manager**, **single anonymized** review with a minimum of two reviewers, a **250-word abstract cap**, required highlights, **author-date** references, Elsevier **Option C** research-data routing, an optional **SSRN preprint**, and **one appeal per submission**. Live-check the official Guide for Authors before upload.

## When to trigger

- The user asks "what should I do next?"
- A draft is handed over and the current bottleneck needs diagnosing
- Work is ping-ponging between empirics, framing, writing, and response letters
- A JPubE decision letter arrived and the user needs revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Idea is not clearly a *public-economics* question / policy "so what?" unclear | `jpube-topic-selection` |
| The government-role contribution is fuzzy or undersold | `jpube-contribution-framing` |
| Placement against the public-finance literature is vague | `jpube-literature-positioning` |
| Causal claim rests on OLS + controls; no quasi-experiment | `jpube-identification-strategy` |
| Estimates exist but data handling / robustness is thin | `jpube-data-analysis` |
| Tables are dense; design is not figure-forward | `jpube-tables-figures` |
| Prose buries the policy lesson; abstract over 250 words | `jpube-writing-style` |
| Need to assemble data/code per Elsevier Option C | `jpube-replication-and-data-policy` |
| Want to understand the single-anonymized review timeline | `jpube-review-process` |
| Ready to submit via Editorial Manager; need a preflight + fee check | `jpube-submission` |
| Received an R&R / want to use the one appeal wisely | `jpube-rebuttal` |

## Default order

1. `jpube-topic-selection` — lock the public-economics question + policy stakes
2. `jpube-contribution-framing` — frame the government-role contribution
3. `jpube-literature-positioning` — stake it against the public-finance frontier
4. `jpube-identification-strategy` — make the quasi-experimental design credible
5. `jpube-data-analysis` — administrative-data handling, elasticities, robustness
6. `jpube-tables-figures` — finalize figure-forward exhibits
7. `jpube-writing-style` — land the policy lesson (250-word abstract last)
8. `jpube-replication-and-data-policy` — Elsevier Option C research-data route
9. `jpube-review-process` — understand the single-anonymized timeline
10. `jpube-submission` — Editorial Manager preflight + fee
11. `jpube-rebuttal` — after the R&R

> `jpube-writing-style` is a late-stage polish. Do not rewrite the intro before identification is settled.

## Stage-gate diagnostic

Each gate must hold before the next skill earns its turn. If a gate fails, route back rather than forward.

| Gate | Holds when | If it fails, route to |
|------|------------|------------------------|
| Fit | A government-role question with a welfare/policy stake | `jpube-topic-selection` |
| Contribution | One sentence ties an estimate to a policy lever | `jpube-contribution-framing` |
| Position | Two or three frontier papers and your delta named | `jpube-literature-positioning` |
| Identification | A policy-induced discontinuity, not OLS + controls | `jpube-identification-strategy` |
| Welfare mapping | Estimate converted to DWL / MVPF / sufficient stat | `jpube-data-analysis` |
| Form | 250-word abstract, author-date, editable source | `jpube-writing-style` / `jpube-submission` |

## Worked routing vignette (illustrative)

A user arrives with a clean event-study **DID = −0.06** on a benefit-reform take-up margin (illustrative) and asks "is it ready to submit?" The router does not jump to `jpube-submission`. It checks gates: identification holds (clean pre-trends), but the welfare-mapping gate fails — the −0.06 is never converted to a fiscal-externality or MVPF term. So the route is back to `jpube-data-analysis` (build the MVPF), then `jpube-contribution-framing` (state the policy payoff), and only then forward to writing and submission. The router's job is to catch the missing welfare step before the desk screen does.

```
【Current stage】topic / framing / position / identification / analysis / exhibits / writing / data / review / submit / rebuttal
【Failing gate】[name the first gate that does not hold]
【Route to】jpube-<skill>
【Blocked-on】welfare mapping / identification / fee / abstract / appeal-decision
```

## Anti-patterns

- **Do not** skip framing and jump to identification — JPubE referees judge the public-finance contribution first
- **Do not** budget zero for the **US$165** fee (it is real, unlike many free generalist journals) unless you are transferring within Elsevier
- **Do not** let `jpube-rebuttal` draft a letter before the revised manuscript exists, and do not waste the single allowed appeal on a weak case
