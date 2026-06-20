---
name: jbes-workflow
description: Use when deciding which jbes-* sub-skill to invoke next, or when sequencing methods-paper work from topic selection through rebuttal for a Journal of Business & Economic Statistics (JBES) submission. Routes — it does not replace — the specialized skills.
---

# JBES Workflow Router (jbes-workflow)

## Overview

This is the router. It does not replace any specialized skill. It tells you **which jbes-* skill to use at the current stage** of a manuscript aimed at the *Journal of Business & Economic Statistics*.

Default assumption: unless the user says otherwise, treat the target as JBES — a methodological econometrics-and-statistics journal published by **Taylor & Francis on behalf of the American Statistical Association (ASA)**. JBES's defining demand is **methods-with-empirics**: a new or improved statistical/econometric method (machine-learning and data-science adaptations and computational improvements explicitly welcomed) that has **clear empirical relevance** and usually a **substantive empirical application**. Pure theory without empirical motivation, or pure applications without methodological novelty, are off-scope. The journal runs on a **rotating Joint Editor model with no single Editor-in-Chief**; current Joint Editors are **Yingying Fan**, **Michael Kolesár**, and **Dacheng Xiu** per the official T&F search snippet. Submission-only details still require opening the live T&F author instructions.

## When to trigger

- The user asks "what should I do next?" on a methods manuscript
- The user hands over a draft and needs the current bottleneck diagnosed
- Work is ping-ponging between theory, simulations, the application, and writing
- A JBES decision letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Unsure the method is novel enough, or it has no empirical relevance / application | `jbes-topic-selection` |
| Contribution vs. prior econometrics/statistics methods is fuzzy | `jbes-literature-positioning` |
| The "what's new and why it matters" claim is not crisp | `jbes-contribution-framing` |
| Regularity conditions / asymptotics / Monte Carlo design are the bottleneck | `jbes-identification-strategy` |
| The empirical application or simulation evidence is thin | `jbes-data-analysis` |
| Simulation tables are dense; size/power not legible | `jbes-tables-figures` |
| Prose buries the method or theorem statements are unclear | `jbes-writing-style` |
| Data/code supplement and data availability statement not assembled | `jbes-replication-and-data-policy` |
| Want to understand peer review / discussion-paper handling here | `jbes-review-process` |
| Ready to submit; need a preflight checklist | `jbes-submission` |
| Received an R&R; need a response-letter strategy | `jbes-rebuttal` |

## Default order

1. `jbes-topic-selection` — confirm method novelty + empirical relevance fit
2. `jbes-literature-positioning` — stake the method against prior art
3. `jbes-contribution-framing` — sharpen the one-sentence methodological contribution
4. `jbes-identification-strategy` — assumptions, asymptotics, Monte Carlo design
5. `jbes-data-analysis` — Monte Carlo evidence + the substantive application
6. `jbes-tables-figures` — make size/power/coverage legible
7. `jbes-writing-style` — polish prose, theorem statements, abstract (late stage)
8. `jbes-replication-and-data-policy` — assemble the reproducible supplement
9. `jbes-review-process` — understand the multi-Co-Editor review path
10. `jbes-submission` — preflight
11. `jbes-rebuttal` — after the R&R

> `jbes-writing-style` is a late-stage polish. Do not rewrite the introduction before the theory and simulation evidence are settled.

## Differences vs. economics / pure-statistics stacks

A **pure economics finding** with no methodological novelty fits a general-interest economics journal better; **pure theorem-proving with no empirical motivation** fits a theoretical statistics journal better. JBES sits in between, and because it is **ASA-owned** it follows ASA editorial/ethics and data-sharing policy rather than the AEA Data Editor / mandatory-pre-publication-replication regime. Operational tells you are at JBES: methods-with-empirics scope, multi-Co-Editor model, ASA supplementary-material expectation, Open Select hybrid OA, and a discussion-paper tradition.

## Worked vignette: routing one manuscript end-to-end

A hypothetical JBES manuscript — a dependence-robust forecast-comparison test on FRED-MD inflation (path **illustrative**) — moves through the stack as follows. The author runs `jbes-topic-selection` (novelty + a real macro application → in-scope), then `jbes-literature-positioning`, then `jbes-contribution-framing` (a HAC-robust test fixing over-rejection). When the limiting null is the bottleneck, route to `jbes-identification-strategy`; when simulation and application are thin, `jbes-data-analysis`; then `jbes-tables-figures`, late-stage `jbes-writing-style`, the supplement, review, and submission. An R&R routes to `jbes-rebuttal`, which re-dispatches into the same skills.

## Routing as a decision block

```
【Stage】topic / positioning / framing / method / evidence / exhibits / prose / supplement / submit / rebuttal
【Symptom】the current bottleneck in one phrase
【Route to】the single jbes-* skill that owns it
【Scope gate】novelty AND empirical relevance present? [Y/N] — if N, topic-selection first
【Live-T&F preflight needed】submission-only fact could change route? [Y/N]
【Next】the skill to invoke now
```

Calibration anchor (hedged): the spine is **methods-with-empirics** — a method with no application is
desk-rejected, and exhibits wait until the asymptotics settle. Submission-specific rules are live-page
preflight items.

## Anti-patterns

- **Do not** skip `jbes-topic-selection` — a method with no empirical relevance is desk-rejected as off-scope
- **Do not** polish exhibits while the asymptotic theory is still unsettled
- **Do not** treat the empirical application as optional — at JBES it is part of scope
- **Do not** let `jbes-rebuttal` draft a response letter before the revised manuscript exists
