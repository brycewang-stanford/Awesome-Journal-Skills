---
name: icde-author-response
description: Use when responding to IEEE ICDE reviews, whether drafting a rebuttal to reviewer concerns or preparing a revise-and-resubmit change document for an invited ICDE revision under the 4-week window, coordinating with area chairs, addressing systems-reviewer pushback on baselines and cost, and deciding what is feasible before the revision deadline.
---

# ICDE Author Response

Use this after ICDE reviews arrive. Reopen the current call's review-and-revision instructions
before drafting, because ICDE's outcome model — and whether a Revise & Resubmit exists this
edition — is edition-specific (待核实 for the current cycle).

## Two response genres

ICDE can hand you either of two response tasks; identify which one you have before writing.

1. **A rebuttal** to initial reviews (where the process offers one) — a short, factual reply
   that corrects errors and answers the decision-critical objection per reviewer.
2. **A revise-and-resubmit change document** — when the first reviewing phase returns
   **Revise & Resubmit** (ICDE 2026 model), you get roughly **four weeks** to make concrete
   changes, re-reviewed by the same reviewers before a final Accept/Reject.

## Triage (both genres)

- Answer concerns that affect correctness, novelty, evaluation soundness, or reproducibility
  first; cosmetic complaints last.
- Because ICDE is **single-blind**, you may cite your own prior work and name your system
  freely — there is no anonymity to protect in the reply.
- Anchor every answer to concrete evidence: a paper section, an added experiment, a disclosed
  cost, or a specific edit — not a promise.
- Correct factual misreadings before conceding anything; a reviewer who misread Figure 7
  should be pointed to the exact panel, courteously.

## The revision change document

For an invited revision, build a **requirement ledger** the same reviewers can check line by
line:

1. Extract every required and suggested change into a numbered list, tagged by reviewer.
2. For each, decide: done (point to the new text/figure), partially done (state the limit
   honestly), or infeasible in four weeks (say so and explain).
3. Write the change document so a reviewer can verify each item without hunting — quote the new
   sentence, name the new figure, give the section.
4. Do not smuggle in scope changes the reviewers did not ask for; an invited revision is judged
   against its list, and surprise additions read as evasion.

## Systems-reviewer pushback patterns

| Pushback | What it signals | ICDE-ready fix |
|---|---|---|
| "Baseline X is untuned" | The reviewer suspects an unfair comparison | Report the tuning budget you gave X, or re-run it tuned and show the new numbers |
| "Results are single-point" | No scale or variance shown | Add a scale curve and report variance across runs, not one median |
| "Cost of the mechanism is hidden" | The trade-off is not disclosed | Add the memory/bandwidth/latency cost table so the trade is legible |
| "Only synthetic workloads" | Doubt about real-world relevance | Add a real workload, or scope the claim to the regime you actually tested |
| "Prior system Y already does this" | Novelty challenge | Name the specific mechanism difference and, if possible, compare against Y directly |

## Feasibility discipline

- Before promising a demanded experiment, price it against the four-week window and your
  hardware access; a revision plan you cannot finish is worse than an honest partial.
- One decision-critical resolution per reviewer beats an exhaustive reply; the area chair reads
  for whether the central objection was actually answered.
- Reply and revise early — the window is short and same-reviewer re-review rewards clarity over
  volume.

## Output format

```text
[Genre] rebuttal / revise-and-resubmit change document
[Priority issue] <reviewer concern>
[Decision dimension] correctness / novelty / evaluation / reproducibility
[Draft response] <ICDE-ready text with evidence anchors>
[Requirement ledger] <numbered change -> done/partial/infeasible, per reviewer>
[Feasibility check] <fits the 4-week window? y/n + why>
```
