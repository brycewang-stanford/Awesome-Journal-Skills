---
name: mathfin-workflow
description: Router for a Mathematical Finance (Wiley) manuscript — decides which mathfin sub-skill to use next across the theorem-first lifecycle, from problem selection through Wiley Research Exchange submission and revision. Use when orienting a financial-mathematics paper built on stochastic analysis and full proofs, or when unsure which stage is the current bottleneck.
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

## Stage gates with pass criteria

```text
gate 0->1  problem chosen      pass: conjectured theorem statable with explicit hypotheses
gate 1->2  positioned          pass: closest prior theorem named + delta sits on one axis
gate 2->3  proved              pass: no [gap] markers; every cited theorem's hypotheses checked
gate 3->4  framed              pass: each main theorem has a financial-payoff sentence
gate 4->5  numerics (optional) pass: every exhibit names the result it illustrates
gate 5->6  written             pass: theorem statements readable without their proofs
gate 6->7  packaged            pass: clean-checkout compile + data statement + classifications
```

A gate that will not close is the bottleneck; route to the owning skill instead of polishing
downstream sections.

## Symptom-to-skill routing

- "We have a model and simulations but no theorem" → mathfin-topic-selection (fit is at risk).
- "The proof uses a martingale property nobody verified" → mathfin-identification-strategy.
- "A colleague says this is just [known paper] in disguise" → mathfin-literature-positioning.
- "The introduction is all mathematics, no finance" → mathfin-contribution-framing.
- "The figures look like an empirical paper" → mathfin-tables-figures, then mathfin-data-analysis.
- "Notation drifts between main text and appendix" → mathfin-writing-style.
- "Referee 2 produced a counterexample" → mathfin-rebuttal, then back to mathfin-identification-strategy.

## Orientation heuristics for ambiguous stages

When a manuscript seems to sit between gates, locate it by its weakest artifact, not its
newest one: a polished introduction resting on an unchecked verification theorem is a gate-2
paper, and a complete proof set under an empirical-sounding abstract is a gate-3 paper. The
pipeline is re-entrant — a referee report or a discovered gap legitimately sends the project
back two or three gates, and re-running the later skills after such a regression is cheaper
than defending an internally inconsistent draft.

## Running proofs and prose in parallel

Theorem development and exposition need not be strictly serial. Once the assumption block is
frozen (gate 2), the introduction, model section, and statement skeletons can be drafted while
appendix proofs are still being verified — but prose must never claim more than the current
proof state supports. Mark unproved strengthenings as conjectures in the draft, and either
prove them or strip them before gate 6.

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
