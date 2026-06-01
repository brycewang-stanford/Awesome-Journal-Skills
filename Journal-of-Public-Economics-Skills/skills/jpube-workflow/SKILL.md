---
name: jpube-workflow
description: Use when deciding which jpube-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Journal of Public Economics (JPubE) submission. Routes — it does not replace — the specialized skills.
---

# JPubE Workflow Router (jpube-workflow)

## Overview

This is the router. It does not replace any specialized skill. It tells you **which jpube-* skill to use at the current stage** of a manuscript aimed at the *Journal of Public Economics* (JPubE).

Default assumption: unless the user says otherwise, treat the target as JPubE — Elsevier's flagship field journal in **public economics / public finance**, founded in **1972 by Tony Atkinson** and edited by Co-Editors-in-Chief **John N. Friedman (Brown)** and **Wojciech Kopczuk (Columbia)**. The journal covers the economic role of government — taxation, public expenditure, social insurance, redistribution, externalities, public goods, and fiscal policy — applying modern theory and quantitative methods to policy questions of interest to an international readership. Operational tells you are at JPubE and not a free top-5 generalist: a **US$165 submission fee** (US$82.50 for students; waived for Elsevier article-transfer submissions), submission via **Editorial Manager**, **single anonymized** review with a minimum of two reviewers, a **250-word abstract cap**, **author-date** references, an optional **SSRN preprint**, and **one appeal per submission**. Re-verify volatile specifics on the official Guide for Authors.

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
| Need to assemble data/code per the Elsevier framework | `jpube-replication-and-data-policy` |
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
8. `jpube-replication-and-data-policy` — Elsevier research-data framework
9. `jpube-review-process` — understand the single-anonymized timeline
10. `jpube-submission` — Editorial Manager preflight + fee
11. `jpube-rebuttal` — after the R&R

> `jpube-writing-style` is a late-stage polish. Do not rewrite the intro before identification is settled.

## Anti-patterns

- **Do not** skip framing and jump to identification — JPubE referees judge the public-finance contribution first
- **Do not** budget zero for the **US$165** fee (it is real, unlike many free generalist journals) unless you are transferring within Elsevier
- **Do not** let `jpube-rebuttal` draft a letter before the revised manuscript exists, and do not waste the single allowed appeal on a weak case
