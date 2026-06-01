---
name: ors-workflow
description: Use as the router for an Operations Research (OR) manuscript — given where you are in the OR/MS modeling-to-submission lifecycle, it names the next ors-* skill to invoke. Routes; it does not itself formulate models (ors-theory-development), prove results (ors-methods), or run computational studies (ors-data-analysis).
---

# Workflow Router (ors-workflow)

## When to trigger

- You are starting an *Operations Research* manuscript and want the right order of operations.
- You finished one stage (e.g., the optimization model is formulated) and ask "what next?"
- You received a decision letter from the handling Area Editor and need to route to revision.

## What Operations Research expects

*Operations Research* is the flagship methodology journal of **INFORMS**. It prizes
mathematically rigorous OR/MS contributions — optimization, stochastic/probabilistic
models, simulation, decision analysis — with **provable results** (theorems and
proofs) alongside increasingly data-driven and applied work. Methodological novelty
and rigor are valued over purely empirical work. The lifecycle below reflects OR's
distinctive norms: an **equation-free introduction**, a **mandatory contribution
statement** (since 1 June 2023, in the cover letter, fewer than 500 words),
**area-editor routing** at submission, **soft double-anonymous** review, and the
**ORJournal GitHub** code/data reproducibility workflow.

## Default order

```text
ors-topic-selection      (is the problem an OR/MS methodological contribution? right area?)
        ▼
ors-theory-development   (formulate the model; state assumptions, theorems, propositions)
        ▼
ors-literature-positioning (place against the OR canon; what is genuinely new?)
        ▼
ors-methods              (proof technique / algorithm design / simulation protocol)
        ▼
ors-data-analysis        (computational study, reproducible experiments, instances)
        ▼
ors-contribution-framing (the <500-word contribution statement + significance)
        ▼
ors-tables-figures       (theorem layout, computational tables, convergence plots)
        ▼
ors-writing-style        (equation-free intro, INFORMS author-year house style) — polish
        ▼
ors-submission           (Author Portal/ScholarOne preflight; area, AEs, reviewers)
        ▼
ors-review-process       (soft double-anonymous; reading the decision)
        ▼
ors-rebuttal             (point-by-point response; reproducibility review)
```

## Routing table

| You are here | Go to |
|--------------|-------|
| Have a problem, unsure it fits OR vs. MS/M&SOM/INFORMS J. Comp. | `ors-topic-selection` |
| Need to formulate the model / state results | `ors-theory-development` |
| Reviewers will ask "what is new vs. prior work" | `ors-literature-positioning` |
| Need a proof strategy or algorithm guarantee | `ors-methods` |
| Have a model and need a computational study | `ors-data-analysis` |
| Writing the contribution statement / discussion | `ors-contribution-framing` |
| Building exhibits | `ors-tables-figures` |
| Final language polish, intro has equations | `ors-writing-style` |
| About to submit | `ors-submission` |
| Decision letter arrived | `ors-review-process` → `ors-rebuttal` |

## Output format

```
【Where you are】...
【Next skill】ors-...
【Why】... (OR-specific reason)
```
