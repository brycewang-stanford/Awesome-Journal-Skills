---
name: jhr-workflow
description: Use when deciding which jhr-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Journal of Human Resources (JHR) submission. Routes — it does not replace — the specialized skills.
---

# JHR Workflow Router (jhr-workflow)

## Overview

This is the router. It does not replace any specialized skill. It tells you **which jhr-* skill to use at the current stage** of a manuscript aimed at the *Journal of Human Resources*.

Default assumption: unless told otherwise, treat the target as JHR — a leading **empirical-microeconomics** journal founded in 1965, published by University of Wisconsin Press and housed at the UW-Madison Institute for Research on Poverty (IRP). It covers **labor, development, health, education, discrimination, and retirement** economics with a strong applied-micro, causal-identification, and **public-policy** orientation. Crucially, despite its name, JHR does **NOT** consider management or personnel ("HR management") research — and the nonrefundable submission fee is not returned for out-of-scope papers. The Editor is **Anna Aizer (Brown)** as of 2026-06-01; **Michael Lovenheim (Cornell)** becomes Editor on **2026-07-01** — re-verify on the live editorial-board page.

## When to trigger

- The user asks "what should I do next?"
- A draft is handed over and the current bottleneck needs diagnosing
- Work is ping-ponging between empirics, writing, and the response letter
- A JHR decision letter (desk reject or R&R) just arrived

## Routing table

| Current symptom | Next skill |
|---|---|
| Unsure the paper is even in scope (or it smells like "HR management") | `jhr-topic-selection` |
| Contribution relative to prior policy-relevant work is fuzzy | `jhr-literature-positioning` |
| Causal claim rests on OLS + controls | `jhr-identification-strategy` |
| Estimates exist but specs/sample/reconciliation are unsettled | `jhr-data-analysis` |
| The "why JHR / why now" framing is weak | `jhr-contribution-framing` |
| Tables are dense; exhibits not policy-legible | `jhr-tables-figures` |
| Prose buries the policy lesson | `jhr-writing-style` |
| Accepted-stage CC0 deposit, archive plan, DAS | `jhr-replication-and-data-policy` |
| Want to understand desk-reject / single-anonymous review | `jhr-review-process` |
| Ready to submit via msubmit.net; need a preflight | `jhr-submission` |
| Received an R&R; need a response-letter strategy | `jhr-rebuttal` |

## Default order

1. `jhr-topic-selection` 2. `jhr-literature-positioning` 3. `jhr-identification-strategy` 4. `jhr-data-analysis` 5. `jhr-contribution-framing` 6. `jhr-tables-figures` 7. `jhr-writing-style` 8. `jhr-replication-and-data-policy` 9. `jhr-review-process` 10. `jhr-submission` 11. `jhr-rebuttal`

> `jhr-writing-style` is a late polish — do not rewrite the intro before identification and reconciliation are settled.
