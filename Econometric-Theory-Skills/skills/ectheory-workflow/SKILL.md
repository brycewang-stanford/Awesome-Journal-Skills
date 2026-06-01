---
name: ectheory-workflow
description: Use as the router for an Econometric Theory (ET) manuscript — decides which ectheory-* skill to invoke next across the theorem-proof lifecycle, from topic selection through single-anonymous review and rebuttal. Start here when unsure where you are.
---

# Workflow Router (ectheory-workflow)

## When to trigger

- Starting a new theorem-proof paper aimed at *Econometric Theory* (ET) and unsure which step comes first
- Mid-project and unsure whether the bottleneck is the assumptions, the proofs, the simulations, or the framing
- Deciding whether the paper is a full **Article** or a short **Miscellanea** (typically <20 pages, often ~15)
- About to submit and wanting the right preflight and review-process skills

## What ET is, in one paragraph

ET, published by **Cambridge University Press** and founded by **Peter C. B. Phillips**, publishes the
mathematical and statistical foundations of econometrics — asymptotic theory, probability-theoretic
methods, time series and nonstationarity, high-dimensional and non-standard environments. Papers are
**theorem-proof in style** with supporting lemmas, derivations, and often Monte Carlo or numerical
illustration. From **1 January 2026** three joint Editors-in-Chief (Guggenberger, Su, Sun) succeed
founding editor Phillips, with a program of invited papers with discussions and themed special issues.

## Default sequence

```text
ectheory-topic-selection         (is the result general + foundational enough?)
        ▼
ectheory-literature-positioning  (stake the theorem against the frontier)
        ▼
ectheory-identification-strategy (assumptions, regularity conditions, asymptotics, proof plan)
        ▼
ectheory-contribution-framing    (state the theorem so its generality is legible)
        ▼
ectheory-data-analysis           (Monte Carlo / numerical illustration, if any)
        ▼
ectheory-tables-figures          (simulation tables, limit-behavior plots, self-contained notes)
        ▼
ectheory-writing-style           (proof exposition, notation discipline, APA references)
        ▼
ectheory-replication-and-data-policy (reproducible computation + ET Supplementary Material file)
        ▼
ectheory-review-process          (war-game referee objections; single-anonymous reality)
        ▼
ectheory-submission              (ScholarOne single-PDF preflight; Article vs Miscellanea; 50-page ceiling)
        ▼
ectheory-rebuttal                (response strategy when the decision letter arrives)
```

## Routing heuristics

- Proof has a gap or an assumption feels ad hoc → `ectheory-identification-strategy`
- Result is correct but reads as narrow/incremental → `ectheory-topic-selection` + `ectheory-contribution-framing`
- Paper exceeds 50 pages → `ectheory-submission` (overflow to online Supplement) + `ectheory-tables-figures`
- Simulations unconvincing or non-reproducible → `ectheory-data-analysis` + `ectheory-replication-and-data-policy`
- Decision letter in hand → `ectheory-rebuttal`

## Output format

```
【Stage】topic / proof / framing / simulation / writing / submission / rebuttal
【Article type】Article or Miscellanea (and why)
【Bottleneck】one sentence
【Next skill】ectheory-...
```
