---
name: cikm-review-process
description: Use when reasoning about CIKM peer review — the EasyChair pipeline (double-blind for Full/Short, single-blind for Applied/Resource/Demo), the mixed IR/data-mining/knowledge-management reviewer pool, per-track evaluation criteria, the ACM Peer Review Policy including the no-AI-written-reviews rule, notification timing, and what actually moves borderline decisions.
---

# CIKM Review Process

CIKM review runs on EasyChair — double-blind for the Full and Short Research tracks,
single-blind for Applied Research, Resource and Demo — inside the ACM Peer Review
Policy, and — its defining feature — in front of a reviewer pool drawn from three
communities at once. Verified 2026 mechanics (source map, re-verified 2026-11-24):
bidding May 26 - June 2, primary review June 2 - 30, reviewer discussion June 30 -
July 10, SPC meta-reviews July 10 - 20, PC chairs' decision meeting July 20 - August 5,
notification August 7; referees are explicitly barred from using AI systems to write
reviews; and the published schedule has **no author-response step** — plan without one.

## The blended-pool effect

A CIKM paper is typically read by people whose default standards differ:

| Reviewer's home lane | What they instinctively grade | Complaint they file most |
|---|---|---|
| Information retrieval | Evaluation design, baselines, metric discipline | "Baselines are stale / significance untested" |
| Data mining | Mechanism novelty, scalability, ablation logic | "Delta over the nearest KDD-line method unclear" |
| KM / databases | Data model, integration cost, system realism | "Would not survive real schema/scale/noise" |

The practical consequence: a paper optimized for one lane can draw its harshest
review from another. Write the submission so each lane finds its own checklist
satisfied — a defensible evaluation, an isolated mechanism, *and* a credible data
story — or explicitly scope the claim to the lanes it serves. This is also why the
reviewer-pool breadth rewards two-lane papers (see `cikm-topic-selection`): they
give more of the panel a reason to champion.

## Per-track criteria shift

The five tracks are judged against different success definitions. Full Research is
graded on novelty plus evidence depth; Short Research on the sharpness of a single
finding, not breadth; Applied Research on the credibility of deployment evidence
(launch, data release) and transferable lessons; Resource on documentation,
licensing, and likely reuse; Demonstration on what a visitor can actually do with
the prototype. Reviewing a submission against the wrong track's bar — the most
common self-review error — produces both false confidence and false alarm.

## What moves a borderline

- **A champion, not an average.** With three lanes in the room, a decided advocate
  who says "my community needs this" outweighs a slightly higher mean score.
- **Unanswered lane-specific objections sink.** A mining reviewer's unaddressed
  scalability question reads as a gap even if both IR reviewers scored high.
- **Compliance is upstream of merit.** The 2026 desk-reject set — missed reviewer
  nomination, undeclared public version, budget or anonymity violations, missing
  GenAI disclosure — removes papers before any lane weighs in.
- **Chairs calibrate across tracks.** Meta-decisions reconcile the lanes; a review
  that misread the track's bar can be discounted at that level, which is why a
  polite confidential-comments note on track fit (where the form allows one)
  is occasionally decisive.

## Timeline realism for the live cycle

Between the June close and the August 7 notification there is no author-visible
activity by default. Do not read silence as signal; do not email chairs for status;
do use the window as `cikm-workflow` Mode A prescribes (artifact readiness,
camera-ready pre-drafting). If a response phase is announced mid-cycle, it will be
short — pre-agree within the team who drafts and who signs off.

## Reading a CIKM review packet

When reviews arrive, decode them by lane before reacting:

```text
For each review:
  1. Identify the lane from the vocabulary
     ("nDCG/baselines/collections" → IR; "novelty/ablation/scale" → mining;
      "schema/provenance/real data" → KM-DB)
  2. Separate lane-standard demands (must answer) from
     lane-mismatch complaints (may be a track/framing misread)
  3. Rank objections by whether a chair would treat them as blocking:
     correctness > missing decisive evidence > positioning > polish
```

Two panel patterns worth recognizing. **Split-by-lane scores** (one lane high, one
low) usually mean the paper is legible to only part of the panel — a framing
problem more than an evidence problem, fixable at the next venue with
`cikm-writing-style`. **Uniform middling scores** usually mean the contribution
is understood and judged thin — an evidence problem no rewrite fixes.

## Confidentiality and integrity boundaries

The ACM Peer Review Policy governs both directions. Authors must not attempt
reviewer identification, contact reviewers, or publicize review text with intent
to pressure; reviewers must keep submissions confidential and — a 2026-explicit
rule — must not have AI systems write their reviews. If a review appears
AI-generated or plainly template-pasted, the recourse is a factual, unemotional
note to the program chairs, not a public thread. Chairs can and do recalibrate
around a defective review; they cannot around an author who breached process.

## After the decision

Accepted papers move to `cikm-camera-ready` with an August 23 camera-ready gate —
sixteen days after notification, one of the tightest turnarounds in the family, and
the same day as the author-registration deadline.
Rejected papers should mine the tri-lane reviews for routing information: lane-
specific objections point to the venue whose community wrote them, which is exactly
the input `cikm-workflow`'s fallback ring consumes.

## Scale realities

CIKM is one of the largest venues in its family — its proceedings run to many
hundreds of papers across tracks (exact counts per edition: check the ACM DL
record; 2026 statistics 待核实) — which shapes review dynamics in ways small
selective venues do not: reviewer load is high, so the first page carries even more of the
verdict (`cikm-writing-style`); topical match between paper and reviewer is
looser than at a single-community venue, which is why the abstract's
lane-vocabulary steers bidding; and per-track sub-committees (applied, resource,
demo) apply genuinely different rubrics rather than one program committee's
taste. Acceptance statistics for the current cycle were not verifiable
(待核实) — do not quote a rate to calibrate hopes; calibrate on whether each
lane's blocking question has an answer inside the PDF.

## Output format

```text
[Stage] pre-notification / notified-accept / notified-reject / response-window(if any)
[Lane read] IR / mining / KM-DB — likely stance of each on this paper
[Sharpest objection] <the one unanswered question most able to sink it>
[Compliance state] clean / at-risk (which trigger)
[Next move] <single highest-leverage action given the stage>
```
