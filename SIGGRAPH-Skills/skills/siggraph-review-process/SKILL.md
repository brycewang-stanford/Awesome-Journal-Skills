---
name: siggraph-review-process
description: Use to model the SIGGRAPH / SIGGRAPH Asia Technical Papers review pipeline and calibrate expectations, covering the single 6-point score scale, the primary/secondary/tertiary reviewer structure, the 1000-word rebuttal, the Technical Papers Committee meeting, conditional acceptance with second-stage verification, and the dual-track Journal-vs-Conference decision.
---

# SIGGRAPH Review Process

Understanding the SIGGRAPH pipeline tells you where author leverage exists and where it does not.
The process is a hybrid: a **conference clock** (one deadline, a short rebuttal, a committee
meeting that decides in one round) wrapped around a **journal outcome** (an ACM Transactions on
Graphics article, with a conditional-accept revision to reach the journal bar). Facts below trace
to the SIGGRAPH 2026 reviewer-instructions/ethics page (`resources/official-source-map.md`);
reconfirm per cycle.

## The pipeline

```text
Submission form (authors locked) -> full submission (PDF + supplemental video)
   -> assignment to a Technical Papers Committee member (primary) + secondary + external tertiary reviewers
   -> reviews written; authors see the full set
   -> rebuttal window (<=1000 words, text only)
   -> Technical Papers Committee meeting: conditional accept / reject, and track assignment
   -> [if conditional] second-stage review verifies the final version
   -> publication in the SIGGRAPH issue of ACM TOG (or the Conference Proceedings)
```

## One scale for everyone

All submissions — dual-track and Journal-only — are scored on a **single scale**: Strong Reject,
Reject, Borderline Reject, Borderline Accept, Accept, Strong Accept. There is **no separate journal
vs conference review**; the same reviews serve both possible outcomes, and the committee decides
the *track* afterward. Practically, this means you write one paper to the journal bar and let the
committee route it — you do not get to argue "but it's only a conference paper."

## Who reads your paper

- A **primary** (a Technical Papers Committee member) owns the paper, recruits reviewers, and
  presents it at the committee meeting.
- A **secondary** committee member and **external tertiary** reviewers provide additional expert
  reviews. Graphics reviewers are domain-deep and will *run the supplemental video* and scrutinize
  comparisons and timings.
- The **rebuttal** is read by these referees and folded into the committee discussion — the primary
  carries your paper's case into the room, so answer the objection the primary will have to defend.

## Where leverage exists

| Stage | Author leverage | Reality |
|---|---|---|
| Submission | High | The paper + results video are 95% of the outcome; write and shoot them to the journal bar |
| Rebuttal | Narrow but real | 1000 text-only words can flip a *factual* error, rarely a judgment |
| Committee meeting | None directly | The primary argues on your behalf; you are not in the room |
| Conditional accept | High | Deliver every required change; the second-stage reviewer can still hold the paper |
| Track assignment | Low | The committee decides Journal vs Conference; you cannot appeal the track |

## Conditional acceptance and the second stage

A SIGGRAPH accept is almost always **conditional**: the committee lists required changes, and a
committee member verifies in a **second reviewing process** that the final version is acceptable
and the changes were made. This is the journal-grade revision folded into a conference calendar —
treat the conditions as binding, not advisory (see `siggraph-author-response` and
`siggraph-camera-ready`).

## The dual-track decision

For a dual-track submission the committee chooses **Journal (TOG)** or **Conference** publication.
Reviewers are **less demanding about formal completeness, validation, and experimental
evaluation** when accepting to the **Conference** track — that track exists to publish riskier or
earlier-stage work. A Conference-track accept is a real acceptance and a real SIGGRAPH
presentation; it is published in the Conference Proceedings rather than the TOG issue. Do not read a
Conference-track outcome as a rejection of the idea.

## Calibrating outcomes

- SIGGRAPH acceptance has historically run in the **~20-30%** range across the whole program with
  **no fixed quota** — the number emerges from the committee, not a target. (SIGGRAPH 2025: >970
  submissions, 306 accepted; SIGGRAPH 2026: >1,120 submissions — exact 2026 accepts **待核实**.)
- A borderline paper is decided by the **video and the comparisons**, not by the rebuttal. Invest
  accordingly *before* submission.
- If rejected, the standard path is to revise using the reviews and target the *next* cycle
  (SIGGRAPH Asia after SIGGRAPH, or vice versa) — see `siggraph-workflow` and
  `siggraph-topic-selection`.

## Output format

```text
[Stage] pre-submission / awaiting reviews / rebuttal / post-decision / conditional
[Score read] where the pivotal reviewer sits on the 6-point scale
[Leverage] what this stage can and cannot change
[Rebuttal target] the factual error / specific question to address (if in window)
[If conditional] required changes -> plan -> second-stage risk
[Track expectation] dual-track (journal/conference) or journal-only
```
