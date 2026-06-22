---
name: ijoc-workflow
description: Use when deciding which ijoc-* sub-skill to invoke next, or when sequencing a manuscript from idea through rebuttal for an INFORMS Journal on Computing (IJOC) submission. Routes — it does not replace — the specialized skills.
---

# IJOC Workflow Router (ijoc-workflow)

## Overview

This is the router. It tells you **which ijoc-* skill to use at the current stage** of a manuscript aimed at the *INFORMS Journal on Computing* (IJOC) — the INFORMS journal at the **intersection of operations research / management science and computer science**. IJOC judges a paper on its **computational and/or methodological advance**: algorithm design and analysis, exact and heuristic optimization, integer/stochastic/robust programming, simulation, computational probability, machine learning for OR, data-science methodology, and the software/computational tooling that makes OR work. A clever application alone does not clear the bar; the *computing* must be the contribution.

Operational tells that you are at IJOC and not a sibling: the author **selects one of the journal's 10 technical areas** at submission via **ScholarOne** (mc.manuscriptcentral.com/ijoc); the **Area Editor desk-rejects roughly 40%** of submissions and the **associate editor's identity is never disclosed** to authors; review is **single-blind** (reviewers see author names); and IJOC runs a **distinctive reproducibility regime** — accepted papers deposit code/data in the **IJOC Software and Data Repository on GitHub** (the INFORMSJoC organization), which snapshots a tagged release and mints a **separate code DOI (`…​.cd`)** alongside the article DOI. Editor-in-chief: **David L. Woodruff** (UC Davis), succeeding Alice E. Smith (whose term ended 2025-12-31); confirmed via INFORMS (检索于 2026-06-22；以官网为准). Re-verify volatile specifics on the official INFORMS pages.

## When to trigger

- The user asks "what should I do next?" on an IJOC-bound paper
- A draft's binding constraint (scope fit, algorithmic claim, experiments, exhibits, deposit) needs naming
- Work is ping-ponging between method design, computational experiments, framing, and the response letter
- An IJOC decision letter arrived and the user must switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Unsure the paper is computing-first or which of the 10 areas fits | `ijoc-topic-selection` |
| The algorithm/model is described but its formulation, correctness, or guarantees are loose | `ijoc-theory-development` |
| Contribution vs. OR/MS and CS prior art is fuzzy or oversold | `ijoc-literature-positioning` |
| Method choice, baselines, or experimental protocol are not pinned down | `ijoc-methods` |
| Computational experiments need instances, fair tuning, timing, and statistics | `ijoc-data-analysis` |
| The "what is new computationally" sentence is not sharp | `ijoc-contribution-framing` |
| Performance profiles / runtime-vs-size plots are dense or misleading | `ijoc-tables-figures` |
| Prose buries the method; abstract/intro do not land the advance | `ijoc-writing-style` |
| Page limit, LaTeX template, area choice, GitHub deposit prep | `ijoc-submission` |
| Want to understand AE/AE-blind timeline, desk-reject odds, or sibling transfer | `ijoc-review-process` |
| Received an R&R; need a response-letter and re-experiment plan | `ijoc-rebuttal` |

## Default order

1. `ijoc-topic-selection` — confirm computing-first scope and the right area
2. `ijoc-theory-development` — formulate the algorithm/model; state correctness/complexity
3. `ijoc-literature-positioning` — stake the advance vs. OR/MS and CS frontiers
4. `ijoc-methods` — method choice, baselines, experimental design
5. `ijoc-data-analysis` — instances, tuning, timing, statistical comparison, scaling
6. `ijoc-contribution-framing` — sharpen the one-sentence computational claim
7. `ijoc-tables-figures` — performance profiles and scaling plots
8. `ijoc-writing-style` — make the advance land (abstract + intro last)
9. `ijoc-submission` — page limit, template, area, GitHub deposit preflight
10. `ijoc-review-process` — calibrate the AE-blind cycle; consider sibling fit
11. `ijoc-rebuttal` — after the R&R

> `ijoc-writing-style` is a late polish; do not rewrite the intro before the algorithm and experiments settle.

## Anti-patterns

- Treating IJOC like *Operations Research* (broad OR theory) or *Management Science* (broad MS) — IJOC wants the computing/methodology to be the news
- Confusing it with *Mathematical Programming Computation* (pure computational MP) or *INFORMS Journal on Optimization* (optimization theory) — IJOC is the OR↔computing interface across simulation, ML, probability, and tooling, not optimization alone
- Polishing exhibits or prose while the algorithm or its experiments are still moving
- Deferring the GitHub code/data deposit to "after acceptance" — design reproducibility in from the start
- Submitting to the wrong technical area and inviting a fast Area-Editor desk reject

## Routing by paper archetype

IJOC spans distinct computing archetypes; the binding constraint differs by archetype. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| exact algorithm / new formulation (B&C, decomposition) | correctness + complexity + benchmark instances | `ijoc-theory-development` → `ijoc-data-analysis` |
| (meta)heuristic / matheuristic | fair tuning, baselines, statistical wins not luck | `ijoc-methods` → `ijoc-data-analysis` |
| ML-for-OR / learning-to-optimize | generalization claim + OR baseline + reproducibility | `ijoc-methods` → `ijoc-data-analysis` |
| simulation / computational probability | DGP, seeds, variance reduction, validation | `ijoc-methods` → `ijoc-data-analysis` |
| software / computational tooling | what is the methodological news beyond the tool | `ijoc-contribution-framing` → `ijoc-submission` |

## Worked routing example (illustrative)

A user says: "My branch-and-cut solver beats the commercial baseline on my instances, but a referee says the win could be tuning and the instance set is cherry-picked." That is two IJOC pushbacks — *unfair experimental comparison* and *non-representative benchmark* — both owned by `ijoc-data-analysis`, with the formulation/cut-validity defense in `ijoc-theory-development`. Route to `ijoc-data-analysis` first: re-run on standard library instances (e.g., MIPLIB-class), tune both solvers on a disjoint set, report a performance profile and a Wilcoxon test, and disclose hardware and time limits. Only once the win survives do you return to `ijoc-tables-figures` and `ijoc-rebuttal`.

## Minimal decision snippet

```
if decision_letter_arrived:        -> ijoc-rebuttal
elif ready_to_submit:              -> ijoc-submission
elif exhibits_or_profiles:         -> ijoc-tables-figures
elif experiments_or_benchmarks:    -> ijoc-data-analysis
elif method_or_baselines:          -> ijoc-methods
elif formulation_or_guarantees:    -> ijoc-theory-development
elif claim_or_positioning_fuzzy:   -> ijoc-contribution-framing / ijoc-literature-positioning
else:                              -> ijoc-topic-selection
```
