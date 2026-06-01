---
name: mathfin-workflow
description: Router for a Mathematical Finance (Wiley) manuscript — decides which mathfin sub-skill to use next across the theorem-first lifecycle, from problem selection through Wiley Research Exchange submission and revision. Use this first to orient a financial-mathematics paper built on stochastic analysis and proofs.
---

# Workflow Router (mathfin-workflow)

## When to trigger

- Starting a new financial-mathematics paper aimed at *Mathematical Finance* and unsure where to begin
- Mid-project and unsure which step is the current bottleneck (theorem? exposition? numerics?)
- Want a single map of the Mathematical Finance pipeline before diving in

## What Mathematical Finance rewards

*Mathematical Finance* (Wiley-Blackwell, affiliated with the **Bachelier Finance Society**) is a
**theory-first** venue. Submissions must be in a **mathematically rigorous style** and are
evaluated on **methodological novelty and contribution to financial modelling** — not on
empirical or data-driven finance. Papers must be **self-contained, including full proofs**;
detailed analysis belongs in an **Appendix**; numerical experiments are welcome **only** when
they support rigorous theoretical developments. Review is **single-blind**, screened first by
the Editor. This router keeps every step aligned to that bar.

## The pipeline (and which skill owns each step)

```text
mathfin-topic-selection          (is the problem novel + rigorously tractable?)
        ▼
mathfin-literature-positioning   (place the result against the stochastic-analysis frontier)
        ▼
mathfin-identification-strategy  (assumptions, theorems, proof architecture, generality)
        ▼
mathfin-contribution-framing     (state the methodological novelty for financial modelling)
        ▼
mathfin-data-analysis            (numerical experiments that SUPPORT the theory, if any)
        ▼
mathfin-tables-figures           (illustrative exhibits, separate files at revision)
        ▼
mathfin-writing-style            (rigorous exposition; results + intuition up front)
        ▼
mathfin-replication-and-data-policy (Data Availability Statement; reproducible code if any)
        ▼
mathfin-review-process           (single-blind editor → AE → referee path)
        ▼
mathfin-submission               (Research Exchange LaTeX preflight)
        ▼
mathfin-rebuttal                 (response-to-referees on revision)
```

## How to use the router

1. No theorem yet → `mathfin-topic-selection`.
2. Theorem exists but assumptions/proof are shaky → `mathfin-identification-strategy`.
3. Result is solid but the "so what for financial modelling" is unclear → `mathfin-contribution-framing`.
4. Adding numerics → `mathfin-data-analysis`, then `mathfin-tables-figures`.
5. Ready to write/polish → `mathfin-writing-style`.
6. Ready to submit → `mathfin-submission`; after a decision → `mathfin-rebuttal`.

## Output format

```
【Stage】topic / theory / framing / numerics / writing / submission / revision
【Bottleneck】one sentence
【Use next】mathfin-<skill>
【Why】how it clears the Mathematical Finance rigor bar
```
