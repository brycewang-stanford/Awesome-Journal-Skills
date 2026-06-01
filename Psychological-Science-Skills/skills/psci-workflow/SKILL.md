---
name: psci-workflow
description: Use as the entry point for any Psychological Science manuscript. Routes to the right sub-skill based on lifecycle stage and manuscript type (Research Article, Registered Report Stage 1/2, Registered Report with Existing Data, Commentary), and flags the journal's tight word format and open-science requirements. It dispatches; it does not draft content.
---

# Psychological Science Workflow Router (psci-workflow)

The orchestrator for a Psychological Science submission. The journal's two defining constraints are a
**very tight word format** and **strong open-science requirements** — the router makes sure both are
handled from the start, then sends the user to the matching skill.

## When to trigger

- Starting a new Psychological Science paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Choosing among manuscript types
- Returning with a decision letter (route to `psci-rebuttal`)

## First question: manuscript type

| Situation | Type | Route note |
|-----------|------|-----------|
| Completed empirical study | **Research Article** | main pipeline below; mind the 2,000-word format |
| Prospective design, no results yet | **Registered Report (Stage 1)** | go to `psci-study-design` + `psci-review-process` early |
| Stage-1 accepted, now have results | **Registered Report (Stage 2)** | `psci-data-analysis` → `psci-writing-style` |
| Confirmatory test on existing data | **Registered Report with Existing Data** | `psci-study-design` (declare data provenance) |
| Short critique/reply to a published paper | **Commentary / Reply** (≤ 1,000 words) | `psci-literature-positioning` |

> Short Reports and standalone Preregistered Direct Replications are **no longer accepted** — fit your
> replication/extension into a Research Article or a Registered Report.

## Routing map (stage → skill)

```text
Idea / fit?                       → psci-topic-selection
Where does it sit in the field?   → psci-literature-positioning
Theory + hypotheses?              → psci-theory-and-hypotheses
Design / power / preregistration? → psci-study-design
Analysis sound + disclosed?       → psci-data-analysis
Exhibits (APA, embedded)?         → psci-tables-figures
Fits the word format?             → psci-writing-style
Open data/materials + statement?  → psci-open-science-and-transparency
How will it be judged?            → psci-review-process
Ready to submit?                  → psci-submission
Got an R&R / decision?            → psci-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-and-hypotheses → study-design → data-analysis →
tables-figures → writing-style → open-science-and-transparency → review-process → submission → rebuttal`

For Registered Reports, the Stage 1 package (theory + design + analysis plan) is reviewed **before**
data — pull `study-design` and `review-process` forward.

## Anti-patterns

- Writing long, then trying to cut to 2,000 words — design for the format from the start
- Treating open data/materials as optional (they are required; exemptions are case-by-case and graded)
- Forgetting the Research Transparency Statement (it sits between Intro and Methods)
- Choosing a Registered Report after results exist

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Type】Research Article / Registered Report S1 / S2 / RR-Existing-Data / Commentary
【Route to】psci-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — preregistration, repositories, power, effect-size tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Psychological Science URLs behind every fact in this pack
