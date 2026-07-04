---
name: geb-workflow
description: Use when deciding which geb-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Games and Economic Behavior (GEB) submission. Routes — it does not replace — the specialized skills.
---

# GEB Workflow Router (geb-workflow)

## Overview

This is the router. It does not replace any specialized skill. It tells you **which geb-* skill to use at the current stage** of a manuscript aimed at *Games and Economic Behavior* (GEB).

Default assumption: unless the user says otherwise, treat the target as GEB — the leading specialist **game-theory** journal, published by Elsevier and an official journal of the **Game Theory Society** (founded 1989 by Ehud Kalai; chief editor Hervé Moulin since 2021). GEB judges work on whether it **advances the frontiers of game theory and its applications** — theory, mechanism design, behavioral, and experiments — not general-economics interest alone. Its process is distinctive: the chief editor assigns each paper to one of **seven Editors** (your publicly known "Editor in Charge"), who routes it to an **anonymous Advisory Editor** and anonymous referees. About **one-third of submissions are desk-rejected** and only **~15%** are eventually published. Re-verify volatile specifics (chief editor, the seven Editors, abstract cap, fees) on the official Guide for Authors; several are marked 待核实 in the source map.

## When to trigger

- The user asks "what should I do next?"
- The user hands over a draft and needs the current bottleneck diagnosed
- Work is ping-ponging between theory, experiment, writing, and response letters
- A GEB decision letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom                                                          | Next skill                          |
|--------------------------------------------------------------------------|-------------------------------------|
| Result feels incremental / unclear it advances game theory itself        | `geb-topic-selection`               |
| Relation to the game-theory literature is fuzzy or undersold             | `geb-literature-positioning`        |
| The "so what for game theory" sentence is missing                        | `geb-contribution-framing`          |
| Proofs are opaque, or assumptions/generality are under-examined          | `geb-identification-strategy`       |
| Experimental data / numerical examples need analysis or are under-powered| `geb-data-analysis`                 |
| Game trees, payoff matrices, or result tables are unclear                | `geb-tables-figures`                |
| Prose buries the model; abstract is over 250 words                       | `geb-writing-style`                 |
| Need a data/code-sharing plan (encouraged, not required at GEB)          | `geb-replication-and-data-policy`   |
| Want to understand the Editor-in-Charge review path before submitting    | `geb-review-process`                |
| Ready to submit via Editorial Manager; need a preflight + cover letter   | `geb-submission`                    |
| Received an R&R; need a response-letter strategy                         | `geb-rebuttal`                      |

## Default order

1. `geb-topic-selection` — confirm the result advances game theory itself
2. `geb-literature-positioning` — locate it against the game-theory frontier
3. `geb-contribution-framing` — state the one-sentence contribution to the field
4. `geb-identification-strategy` — assumptions, results, proof exposition, generality
5. `geb-data-analysis` — experimental analysis / verified numerical examples
6. `geb-tables-figures` — game trees, payoff matrices, clean result exhibits
7. `geb-writing-style` — land the model for a general game-theory reader (abstract ≤250 words)
8. `geb-replication-and-data-policy` — optional but recommended sharing plan
9. `geb-review-process` — understand the Editor-in-Charge path
10. `geb-submission` — Editorial Manager preflight + conference-version cover letter
11. `geb-rebuttal` — after the R&R

> `geb-writing-style` is a late-stage polish. Do not rewrite the introduction before the theorems and assumptions are settled — the statements will change.

## Stage log

Keep this log with the manuscript and update it after each working pass; the **first unresolved line is your route**:

```text
GEB stage log  (✓ = settled, ? = open — first ? wins)
contribution  one-line advance to game theory written out verbatim ..... [?]
positioning   nearest frontier papers named + what you generalize ...... [?]
results       theorems stated, assumptions listed, proofs readable ..... [?]
evidence      experiment powered / numerical examples verified ......... [?]
exhibits      game trees and payoff matrices self-contained ............ [?]
prose         abstract ≤250 words; model reachable within intro ........ [?]
sharing       data/code plan drafted (encouraged, not required) ........ [?]
process       Editor-in-Charge path + desk-reject risks reviewed ....... [?]
submit        Editorial Manager preflight; conference version flagged .. [?]
--- decision letter in hand? ignore every line above → geb-rebuttal ---
```

- "Is this big enough for GEB?" → `geb-topic-selection`
- "Who am I building on / generalizing?" → `geb-literature-positioning`
- "My proof is correct but unreadable" → `geb-identification-strategy`
- "My experiment may be under-powered" → `geb-data-analysis`
- "My abstract is 320 words" → `geb-writing-style`
- "There's a conference version of this paper" → `geb-submission`
- "Who actually decides on my paper?" → `geb-review-process`
- "I got a revise-and-resubmit" → `geb-rebuttal`

## Anti-patterns

- **Do not** skip `geb-contribution-framing` and submit a technically-correct result with no stated advance to game theory — desk-reject risk
- **Do not** polish exhibits while the main theorem's assumptions are still moving
- **Do not** treat GEB like a general-economics top-5: the bar is advancing **game theory**, not broad policy interest
- **Do not** let `geb-rebuttal` draft a response letter before the revised manuscript exists
