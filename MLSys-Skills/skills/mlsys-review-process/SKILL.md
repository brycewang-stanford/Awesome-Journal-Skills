---
name: mlsys-review-process
description: Use when reasoning about how MLSys peer review works, covering the OpenReview workflow, the mixed ML-and-systems reviewer pool and how each half scores differently, the compressed response window, industrial-track review expectations, decision dynamics, and what the post-acceptance artifact stage means for review strategy.
---

# MLSys Review Process

Use this to model what happens to a Conference on Machine Learning and Systems submission
between upload and decision. Mechanics below are 2026-cycle anchors (verified 2026-07-08);
the venue is young and still redesigns its process — 2026 alone added an entire track —
so reopen the current CFP and OpenReview group before strategic decisions.

## The pipeline (2026 anchors)

- Submission via OpenReview (`MLSys.org/2026/Conference` group) by October 30, 2025.
- Double-blind review; arXiv posting allowed in parallel.
- Reviews released January 12, 2026; author responses due January 16; notifications
  January 25-26. There is no long discussion phase to rescue a paper — the response is
  a single, short shot (see `mlsys-author-response`).
- Accepted papers publish on proceedings.mlsys.org; artifact evaluation follows as a
  separate, optional, badge-awarding stage (March 8 - April 8 in 2026).

## Who reviews here — the two-culture pool

MLSys program committees deliberately mix ML researchers with systems, architecture, and
compiler people. The same paper is read through two different quality lenses:

| Dimension | ML-culture reviewer asks | Systems-culture reviewer asks |
|---|---|---|
| Contribution | Is the idea new relative to the ML literature? | Is there a reusable mechanism/abstraction, or just engineering? |
| Evidence | Are comparisons fair, seeds varied, quality preserved? | Is the workload realistic? Where are the bottleneck analysis and tails? |
| Skepticism trigger | Accuracy deltas without significance | "Up to Nx" speedups without workload context |
| Appendix habits | May check math and extra ablations | Rarely reads it; judges the 10 pages |

A submission that satisfies only one culture gets a split review set, and split reviews
at a single-shot-response venue are dangerous: you have four days to convert one side.
Write for both from the start — name the mechanism (systems lens) *and* show quality is
preserved under the optimization (ML lens).

## What decisions actually turn on

- **Workload representativeness** is the most common fatal objection: a system evaluated
  only on microbenchmarks or toy models loses both cultures at once.
- **Baseline strength**: comparing against an untuned or outdated system is treated as
  invalidating, not just weakening, the result — the field's baselines (serving engines,
  compilers, training frameworks) improve monthly.
- **Claim-evidence scope match**: a general claim ("for transformer inference") tested on
  one model family gets scoped down by reviewers if the authors did not scope it first.
- **Honesty signals**: reported non-wins, stated tradeoffs, and cost accounting raise
  trust scores disproportionately at this venue.
- **Industrial-track papers** are judged on different axes: scale realism, design
  methodology depth, and benchmark detail — explicitly not novelty (2026 track rules).
  A research-track-style novelty defense in an industrial-track response misses the
  actual bar, and vice versa; know which rubric your reviewers were given.
- **The appendix asymmetry**: since reviewers are not obliged to read the separate
  appendix, an objection already answered there is still a live objection — the review
  process treats the 10 pages as the paper, and responses must quote the appendix
  material into the reply rather than pointing at it indignantly.

## Reading a review packet

```text
Triage grid for an MLSys review set:
  R1 (systems): workload not representative        -> decision-critical, answerable
  R2 (ML):      missing significance on Table 2     -> decision-critical, cheap to fix
  R3 (systems): "wish you compared against X"       -> check X's publication date vs
                                                       your deadline; if after, say so
  All:          writing nits                        -> batch into two lines
Rank by (decision impact) x (answerability in 4 days); ignore tone.
```

Meta-review synthesis rewards responses that resolve the *shared* objection across
reviewers; three reviewers independently doubting the baseline is one problem, not three.

## Reading scores and reviewer signals

- A short review with a middling score from a systems reviewer usually means "plausible
  but I don't trust the evaluation" — the response should add measurement, not prose.
- A long, detailed negative review is often the most convertible: the reviewer engaged
  deeply enough to change their mind if the specific objections close.
- Confidence scores matter more here than at mega-conferences: with small, topically
  close panels, a high-confidence negative reviewer who is factually wrong is the
  highest-priority target, because the meta-reviewer will otherwise defer to them.
- Watch for the culture split masquerading as disagreement: R1 (ML) at accept and R3
  (systems) at reject with non-overlapping objections is not noise — it means the paper
  currently serves one audience. Say explicitly in the response how each culture's
  concern is met.
- Do not read tone as signal; systems-review bluntness ("this evaluation is not
  credible") is genre convention, not a verdict on the idea.

## Confidentiality and conduct

- Submissions are confidential to the review process; reviewers must not use or share
  them. Authors likewise must not fish for reviewer identities or contact PC members
  about their paper outside the platform.
- The double-blind-plus-arXiv model means a reviewer may recognize your preprint;
  policy treats good-faith anonymization by authors as the requirement, not reviewer
  ignorance. Do not exploit this by advertising the arXiv version at reviewers.

## After the decision

- Rejected: MLSys reviews are unusually actionable (workload, baseline, and measurement
  gaps are concrete); the annual-cycle question is whether to strengthen for next MLSys
  or reroute to a systems venue with a nearer deadline — see `mlsys-topic-selection`.
- Accepted: review strategy hands off to camera-ready reconciliation and the artifact
  stage, where a different committee re-examines your evidence in executable form.

## Cycle-volatility warnings

- Response-window length, discussion mechanics, reviewer-volunteer expectations for
  authors, and any AI-use policy in reviewing were not verifiable for 2026 beyond the
  dates above (待核实) — confirm on the live pages.
- Acceptance-rate folklore changes yearly and is omitted here deliberately.

## Output format

```text
[Stage] pre-submission / under review / response / decided
[Review-set shape] <systems vs ML objections, split or aligned>
[Decision-critical objection] <the one the meta-review will weigh>
[Response leverage] <answerable in window? with what evidence>
[Conduct checks] <anonymity/contact/confidentiality risks>
[Next move] <one action>
```
