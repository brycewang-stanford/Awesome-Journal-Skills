---
name: sigcomm-review-process
description: Use when explaining or planning around ACM SIGCOMM peer review — double-blind HotCRP reviewing, the early-reject cut for consensus rejections, the rebuttal for discussion-phase papers, the shepherd-run one-shot revision that ends in accept or reject only, shepherding of accepted papers, and how the outcome space shapes author strategy.
---

# SIGCOMM Review Process

Use this to reason about review-stage strategy. Reopen the current CFP and submission page
before making process claims; the mechanisms below are the SIGCOMM 2026 rendering and can
change per edition.

## The outcome space is wider than accept/reject

SIGCOMM layers several author-facing stages, and reading which one you are in drives every
subsequent move:

- **Early reject.** Submissions with a consensus to reject are notified before the formal
  date, so authors can redirect the work to another venue sooner. It is a courtesy, not a
  soft accept; there is no reply that reopens it.
- **Rebuttal.** Papers that advance to the discussion phase receive reviews and a chance to
  respond. This is the moment to correct factual errors and answer the decision-critical
  objection — not to relitigate taste.
- **One-shot revision.** A small set of papers get a merits summary plus a required-changes
  list, resubmit about a month later, and are re-reviewed **by the same reviewers where
  possible under a PC shepherd**. The name is literal: the revised paper can only be
  **accepted or rejected**, so the issue list is a contract, not a suggestion.
- **Accept (with shepherding).** Accepted papers may be assigned a shepherd who confirms the
  reviews are addressed through camera-ready and approves whether any appendix is necessary.

## What reviewers weigh

| Review dimension | What raises it | What sinks it |
|---|---|---|
| Contribution | A networking mechanism or architecture that generalizes | A single-site tuning win with no transferable idea |
| Evaluation realism | Testbed, trace, or deployment evidence with reported tails | Simulation-only or mean-only results for a fabric claim |
| Baselines | Comparisons against the strongest deployed alternative | Straw-man baselines the mechanism is built to beat |
| Measurement rigor | Documented workload, topology, run counts, variance | Percentiles with no replication or unstated conditions |
| Clarity | A stated design principle the paper defends | A behavior described but no invariant named |

## Who reviews here

The PC mixes networking-systems builders, measurement researchers, and theory-leaning
networking people; expect at least one reviewer to interrogate the evaluation setup line by
line and another to ask whether the mechanism generalizes beyond the tested topology. Because
SIGCOMM is the broad flagship, a paper is often read against the strongest prior work in its
exact subarea, so a missing state-of-the-art baseline is caught rather than skimmed past.

## Stage-by-stage realism

- **Reviews:** triage by what the discussion and the eventual shepherd would weigh, not by
  reviewer tone; one unresolved evaluation-realism objection outweighs several style notes.
- **Rebuttal:** short and precise beats exhaustive; answer the objection that decides the
  paper and concede what cannot be fixed now.
- **Revision:** treat the required-changes list as the grading rubric; a revision that
  addresses adjacent points but dodges a listed issue is the recognizable one-shot failure.
- **Shepherding:** the shepherd is an ally who signs off the final version, including
  appendix necessity — engage early through HotCRP comments rather than surfacing surprises
  at the camera-ready deadline.

## Output format

```text
[Current stage] submitted / reviews / rebuttal / revision / decision / camera-ready
[Outcome class] early reject / rebuttal / one-shot revision / accept-with-shepherd
[Decision actors] <reviewers / discussion / shepherd / chairs>
[Likely leverage] <contribution / evaluation realism / baselines / measurement / clarity>
[Forbidden moves] <identity leak / new unsupported results / dodging the issue list>
[Next response move] <one action>
```
