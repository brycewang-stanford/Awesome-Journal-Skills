---
name: corl-review-process
description: Use when reasoning about how CoRL reviews a paper — the OpenReview double-anonymous pipeline, reviewer/AC/SAC hierarchy, rubric scoring with weak accept as the acceptance threshold, the first-round rejection gate before rebuttal, the reviewer-AC discussion window, decision meetings, and public reviews for accepted papers.
---

# CoRL Review Process

Model the pipeline correctly and author effort lands where it can still change the
outcome. Everything here reflects the CoRL 2026 process as documented on corl.org
(Instruction for Reviewers / Reviews / Rebuttal pages) and OpenReview, read
2026-07-08; CoRL adjusts its process year to year, so treat this as one cycle's
mechanics.

## The pipeline, stage by stage

| Stage | Who acts | Author leverage |
|---|---|---|
| Submission + abstract registration | Authors | Full — see `corl-submission` |
| Assignment (keywords, bidding, conflicts) | ACs, OpenReview matching | Indirect, via keyword choice |
| Reviewing (June–early Aug 2026) | 3-ish reviewers per paper + AC | None; do rebuttal prep instead |
| Reviews released + first-round gate | Program committee | None at the gate itself |
| One-page rebuttal (due Aug 11, 2026 AoE) | Authors | **Highest-leverage moment** |
| Reviewer–AC discussion (Aug 12–19, 2026) | Reviewers, ACs | Indirect, through the rebuttal |
| SAC–AC meetings, then SACs–PCs meeting | ACs, SACs, Program Chairs | None |
| Decision + (for accepted papers) public reviews | Program Chairs | None |

Three structural facts to internalize:

1. **A three-tier committee.** Reviewers report to Area Chairs, who report to
   Senior Area Chairs; decisions are finalized in dedicated SAC–AC meetings plus a
   final SACs–PCs meeting. Your rebuttal's real audience includes the AC and SAC
   who will represent your paper in rooms you never see.
2. **A first-round rejection gate.** In the 2026 process, a paper that receives no
   score of weak accept or above — from any reviewer or the AC — is a candidate
   for rejection **without rebuttal**. Initial impressions are therefore not
   provisional at CoRL; the paper must earn at least one advocate on first read.
3. **Accepted papers publish their reviews.** Reviews and rebuttals of accepted
   papers are made publicly available. The exchange is part of the paper's
   permanent record, which disciplines both sides' tone.

## Scoring culture

The 2026 reviewer instructions direct reviewers to score against a rubric rather
than against their batch, with **weak accept reported as the acceptance-threshold
score** in the review form's terms. Practical consequences for authors:

- A profile of one enthusiastic accept plus several borderlines is viable — the
  gate needs *one* weak-accept-or-above, and discussion can move borderlines.
- Reviewer confidence is reported separately and ACs are told to weigh it; a
  low-confidence negative review is explicitly contestable in the rebuttal, in
  factual and polite terms.
- Reviewers are told to keep weaknesses specific and constructive and to write
  reviews that can stand alone if the paper never reaches rebuttal — meaning the
  written text, not just the score, is what the AC audits at the gate.

## What CoRL reviewers probe first

The reviewer pool is the robot-learning community itself, and its recurring
checks are learning-specific (details in `corl-experiments`):

- Evaluation breadth: number of tasks, objects/scenes, seeds, and episodes per
  policy — single-configuration results draw immediate skepticism.
- Baseline recency: comparison against current robot-learning methods, not only
  classical controllers or two-generation-old learning baselines.
- Sim-vs-real honesty: whether claims scoped as "real-world" rest on real-robot
  evaluations, and whether the transfer gap is measured or hand-waved.
- The mandatory Limitations section: reviewers read it and cross-check that the
  failure modes it admits match what the video shows.

## Reading a review packet

```text
Triage grid — fill within 24h of reviews arriving:
R1  score: __  confidence: __  gate-relevant (>= weak accept)? __
R2  score: __  confidence: __  gate-relevant? __
R3  score: __  confidence: __  gate-relevant? __
AC  (if scored/commented): __

If NO gate-relevant score exists:
  -> paper is a first-round rejection candidate; expect no rebuttal round.
  -> pivot to the resubmission branch (corl-topic-selection, corl-workflow).
If at least one exists:
  -> rebuttal is live (corl-author-response); rank concerns by which
     scores they block, not by which are easiest to answer.
```

## Confidentiality and process hygiene

- Reviewers must keep papers inside OpenReview and use them only for reviewing;
  suspected breaches go to the AC, not to public channels.
- Conflicts (institutional, advisor–advisee, recent collaboration, personal) are
  reassignment triggers — authors should declare them exhaustively on the form, as
  a missed conflict discovered late destabilizes an otherwise sound decision.
- Do not contact reviewers or guess identities; the discussion window is mediated
  entirely through OpenReview.

## Calibrating expectations

- CoRL is small and selective by design (a few hundred papers per year in recent
  volumes, versus thousands at ML mega-conferences); per-paper acceptance rates
  for 2026 are 待核实 until the cycle closes — do not quote a number to a team.
- Between rebuttal close (Aug 11) and decisions (September 2026, exact date
  待核实) there is genuine multi-layer deliberation; silence in that window
  carries no signal either way.
- Reviewer quality varies with pool load in a fast-growing field; the appeal path
  for a factually broken review is a calm note to the AC via OpenReview during the
  discussion window, not after decisions.

Re-verify the live process pages before advising on any cycle:
https://www.corl.org/contributions/instruction-for-reviewers and
https://www.corl.org/contributions/instruction-for-reviews (2026 URLs; year-sites
rotate).
