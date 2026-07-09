---
name: aamas-review-process
description: Use when explaining or planning around AAMAS peer review, covering OpenReview review release, the double-blind rebuttal on preliminary reviews, area-chair discussion, the mixed game-theory, MARL, and systems reviewer pool, the public posting of reviews and decisions, and how acceptance criteria weigh the interaction contribution.
---

# AAMAS Review Process

Use this to reason about review-stage strategy. Reopen the current CFP, OpenReview group,
author and reviewer instructions, and the code of conduct before making process claims; AAMAS
review specifics move between editions.

## Process model

- AAMAS runs submission and review on OpenReview under the IFAAMAS namespace in recent cycles.
- Reviewers evaluate technical correctness, the significance of the interaction contribution,
  the reality and rigor of the multiagent evaluation, clarity, reproducibility, and fit with
  agents-and-multiagent-systems scope.
- A rebuttal lets authors respond to preliminary reviews before the final decision; area chairs
  then synthesize.
- Accepted papers and their reviews are published, so the review record is durable and public.
- The most useful rebuttal gives the area chair a clean rationale for acceptance, not a
  point-by-point defense of every comment.

## Who reviews here

- The pool mixes game theorists, multiagent-RL researchers, mechanism-design and social-choice
  specialists, and systems-minded reviewers; expect at least one to read the game definition and
  solution concept line by line.
- Because AAMAS is specialized, a paper is likely to meet a reviewer who works on exactly its
  subarea, so a vague equilibrium claim or an under-specified opponent set gets caught rather
  than skimmed.
- Borderline interaction papers usually fail on one of three edges: the result turns out to be
  single-agent in disguise, the solution concept is never pinned down, or the multiagent
  evaluation is thin (self-play only, no seeds, no held-out opponents).

## Scoring leverage table

| Review dimension | What raises it | What sinks it |
|---|---|---|
| Correctness | A stated game, a named solution concept, and a body-level proof sketch | Hidden information structure; an equilibrium asserted but never defined |
| Significance | A finding that only exists because agents interact | An incremental single-agent gain wearing a multiagent label |
| Empirical support | Experiments that probe strategy: held-out opponents, deviation tests | Self-play-only curves disconnected from the claim |
| Clarity | One notation source and a legible game description | Notation and payoff conventions that shift between sections |

## Stage-by-stage realism

- Initial reviews: triage by what the area chair would weigh, not by reviewer tone.
- Rebuttal: windows are short; an early, precise reply anchored in submitted evidence beats a
  late exhaustive one.
- Decision: the area chair synthesizes, and one unanswered correctness or interaction-reality
  objection outweighs several resolved clarity complaints.
- Public record: assume the reviews and your rebuttal will be visible with the paper, and keep
  the exchange professional and concrete.

## Output format

```text
[Current stage] submitted / reviews / rebuttal / decision / camera-ready
[Decision actors] <reviewers / area chair / program chairs>
[Likely leverage] <correctness / interaction-reality / significance / experiments / clarity>
[Forbidden moves] <identity leak / new results / revised-paper upload if disallowed>
[Next response move] <one action>
```
