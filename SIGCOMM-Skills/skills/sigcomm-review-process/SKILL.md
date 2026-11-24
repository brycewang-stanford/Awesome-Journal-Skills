---
name: sigcomm-review-process
description: Use when explaining or planning around ACM SIGCOMM peer review — double-blind HotCRP reviewing, SIGCOMM 2027's collaborative reviewing with a single consensus review and no rebuttal or one-shot revision, the three decisions (conference accept with shepherd, CCR accept, reject), reciprocal reviewers, the general-accessibility test, and how the SIGCOMM 2026 early-reject/rebuttal/one-shot pipeline differed.
---

# SIGCOMM Review Process

Use this to reason about review-stage strategy. Reopen the current CFP and submission page
before making process claims; the mechanisms below are the SIGCOMM 2027 rendering
(re-verified 2026-11-24), and SIGCOMM changes its review model between editions — 2027 changed
it substantially.

## SIGCOMM 2027: collaborative reviewing, three decisions, no reply window

- **Collaborative reviewing.** The reviewers of a paper are in conversation from the start,
  asking each other questions and airing disagreements before anyone commits to a verdict.
  After the PC decides, they write **one relatively short consensus review** — closer to a PC
  summary than a set of detailed individual reviews.
- **No rebuttals or one-shot revisions.** Nothing the author writes after submission changes
  the decision; the paper has to answer the predictable objections itself.
- **Reciprocal reviewers.** Each submission names an author willing to review (normally a PhD
  holder); these external reviewers widen the pool and may be asked to review as many papers
  as their own submissions.
- **General accessibility is a criterion.** The PC will reject papers whose motivation or
  approach most SIGCOMM attendees would not understand.
- **Three decisions:**
  - **Accepted into the SIGCOMM conference** — every such paper gets a shepherd, owes a video,
    and is presented in person at a small-scale discussion session; a subset is also chosen for
    a plenary talk (chosen to spark discussion, explicitly not a quality tier).
  - **Accepted into CCR** — rejected from the conference but offered publication as a regular
    Computer Communication Review research article; authors may decline and resubmit elsewhere.
  - **Rejected** from both.

## SIGCOMM 2026 (history): the layered pipeline

The 2026 edition used a different outcome space; keep it in mind when reading older advice:

- **Early reject** for consensus rejections, notified before the formal date.
- **Rebuttal** for papers that advanced to the discussion phase.
- **One-shot revision** for a small set of papers: a merits summary plus required changes,
  resubmitted about a month later under a PC shepherd, re-reviewed by the same reviewers where
  possible, ending in **accept or reject only**.
- **Accept (with shepherding)**, the shepherd approving any appendix's necessity.

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

- **Before submission (2027):** the only author-controlled stage. Every objection you can
  foresee — evaluation realism, a missing baseline, generalization — is answered in the body or
  not at all.
- **Consensus review:** read it as the PC's decision rationale; one unresolved
  evaluation-realism point outweighs several style notes when planning the next submission.
- **CCR offer:** a real publication decision, not a consolation prize — weigh it against a
  resubmission elsewhere.
- **Shepherding:** the shepherd is an ally who signs off the final version, including appendix
  necessity — engage early through HotCRP comments rather than surfacing surprises at the
  camera-ready deadline.
- **Rebuttal / revision (2026 model only):** short and precise beats exhaustive; treat a
  required-changes list as the grading rubric.

## Output format

```text
[Current stage] submitted / under collaborative review / decision / CCR choice / camera-ready
[Outcome class] conference accept (shepherd) / CCR accept / reject — 2026 model: early reject / rebuttal / one-shot revision
[Decision actors] <reviewers / discussion / shepherd / chairs>
[Likely leverage] <contribution / evaluation realism / baselines / measurement / clarity>
[Forbidden moves] <identity leak / new unsupported results / dodging the issue list>
[Next response move] <one action>
```
