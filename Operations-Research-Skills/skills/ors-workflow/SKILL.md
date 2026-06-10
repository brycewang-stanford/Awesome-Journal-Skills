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

## The OR value arc the router protects

Every stage exists to keep one chain intact — the arc an *Operations Research* area
editor mentally traces when deciding fate: **model → analysis → algorithm →
computational study → decision insight**. A manuscript that breaks any link routes to a
referee complaint downstream. The router's job is to surface the weak link early.

| Arc link | Owning skill | Snaps when... | Area-editor reads it as |
|----------|--------------|---------------|--------------------------|
| Model | `ors-theory-development` | object too general to prove or too narrow to matter | "no theorem-grade core" |
| Analysis | `ors-methods` | a proof gap or unestablished rate | "rigor not at OR's bar" |
| Algorithm | `ors-methods` | a guarantee-free heuristic carries the paper | "INFORMS J. Comp., not OR" |
| Computational study | `ors-data-analysis` | benchmarks/baselines missing | "claims not corroborated" |
| Decision insight | `ors-contribution-framing` | structure never reaches the application | "elegant but no OR payoff" |

Operations Research is the **INFORMS flagship**: it wants both a theorem-grade result
*and* a credible computational/decision study. M&SOM, POM, or *Journal of Operations
Management* would route an empirical-OM survey through a different door; OR will not.
Whenever a stage is "done," ask whether its arc link can survive the next referee.

## Methodology-area vs. application-area routing

A second routing axis OR authors miss: every submission carries a **methodology**
identity (optimization / stochastic / simulation / game-theory / ML-for-OR) *and* an
**application** flavor (revenue management, healthcare, logistics). The editorial area
is chosen on the **methodology**, not the application headline — a revenue-management
paper whose engine is a queueing analysis routes to Stochastic Models, not a
"pricing" bucket. Misreading this axis is the most common re-route cause; resolve it in
`ors-topic-selection` before formulating.

## Worked routing vignette (illustrative)

A team has a stochastic-inventory control problem, a proved threshold-policy optimality
result, and an approximation algorithm with a claimed 1.5-factor guarantee (numbers
illustrative). Router trace: they *think* they are ready for `ors-submission`, but the
arc shows the **computational-study link is empty** — no benchmark instances, no solver
baseline. Route order corrected to `ors-data-analysis` first, then `ors-tables-figures`
for a performance-profile plot, then `ors-contribution-framing` to tie the threshold
structure to the decision payoff, *then* `ors-submission`. Skipping straight to submit
would have drawn a "computational study lacks benchmarks" desk-stage flag.

## Output format

```
【Where you are】...
【Arc link at risk】model / analysis / algorithm / comp-study / insight
【Next skill】ors-...
【Why】... (OR-specific reason)
```
