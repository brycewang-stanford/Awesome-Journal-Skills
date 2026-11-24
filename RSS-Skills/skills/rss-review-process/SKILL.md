---
name: rss-review-process
description: Use when explaining or strategizing around RSS (Robotics: Science and Systems) peer review — the double-blind OpenReview pipeline, the RSS 2027 two-stage shepherding design (Extended Abstract, invited rebuttal, Extension Charter, final paper), signed reviews for accepted papers, and what single-track selectivity does to reviewer expectations.
---

# RSS Review Process

Model how an RSS decision actually gets made. The mechanics below are the verified
RSS 2027 design (Call for Papers, Author FAQ and Reviewer Guidelines at
roboticsconference.org, read directly on 2026-11-24); the two-stage shepherding
structure is new in 2027 and is cycle policy, so confirm it survives before relying on
it in a later edition.

## The RSS 2027 pipeline

```text
Stage 1: Extended Abstract on OpenReview (double-blind), due 2026-12-04 AoE
        │   (5 pages content + 1 page references; nothing beyond is reviewed)
   reviewers score Value of Hypothesis (1-4) + Feasibility of Conclusion (1-4)
        │
   Stage 1 decision 2027-02-05 ── reject (cascading filter)
        │ invited
   Metareview: required clarifications, evaluations, extensions
        │
   rebuttal (due 2027-02-12 AoE)
        │
   Stage 2 decision 2027-02-26 ── reject
        │ invited
   Extension Charter (AC-finalized roadmap)
        │
   final paper, 8 pages excl. references (2027-04-16) + supplement (2027-04-19)
        │
   Program Committee checks the Charter was followed ──▶ notification 2027-04-30
```

Three properties distinguish this from ML-conference discussion phases:

- **Stage 1 judges the hypothesis, not the results table.** Experiments may be
  preliminary; the problem, hypotheses and methodology must be complete. Weak
  hypotheses are filtered out early so ACs can spend effort on the rest.
- **The rebuttal is earned, and it shapes a contract.** Only invited papers respond to
  the Metareview, and the AC turns the response into the Extension Charter. Write it
  for the AC who will draft that Charter (`rss-author-response`).
- **Final acceptance asks "was the Charter executed?"** Negative results are not
  grounds for rejection if the hypothesis was rigorously tested and insights drawn.
- **Signed reviews.** Reviews of accepted papers are published with the reviewers' and
  chairs' names — expect careful, accountable reviewing.

## What single-track selectivity does to reviewing

Every accepted paper takes a slot in front of the whole conference, so the operative
question in the AC meeting is closer to "must the field hear this?" than "is this
sound?" Soundness is necessary, not sufficient. Practical consequences:

| Review dynamic | Cause | Author counter-move |
|---|---|---|
| High bar for "so what" | One program, finite slots | Lead with the claim's consequence for other subfields |
| Deep methodological reads | Specialized, smaller reviewer pool | State assumptions and protocol precisely; vagueness gets caught |
| Skepticism toward demo-style evidence | Science-first venue identity | Attribute failures, isolate mechanisms, report all trials |
| Low tolerance for padding | 5 + 1 Stage 1 limit, 8-page final ceiling | Cut aggressively; length is not a proxy for rigor here |

## Reading a borderline packet

- Separate *correctness* objections (a flaw in the claim or protocol) from *scope*
  objections (the claim is narrower than sold) from *significance* doubts (sound but
  not slot-worthy). The first two can be answered in the rebuttal or absorbed into the
  Extension Charter; the third is won or lost in the hypothesis framing.
- A lone enthusiastic review does not carry a paper through an AC meeting; a lone
  unanswered correctness objection can sink one. Triage accordingly.
- The AC's Metareview and Charter are the decision artifacts. Everything you write
  should compress well into two sentences an AC might put in them.

## Timeline anatomy (RSS 2027 verified dates)

| Date (AoE) | Event | Author-side implication |
|---|---|---|
| Dec 4, 2026 | Extended Abstract in | Last word for papers filtered at Stage 1 |
| Feb 5, 2027 | Stage 1 decision + Metareview | One week to respond |
| Feb 12, 2027 | Rebuttal due | Pre-draft answers to likely objections |
| Feb 26, 2027 | Stage 2 decision / Extension Charter | Seven weeks of execution begin |
| Apr 16 / Apr 19, 2027 | Final paper / supplement | Charter delivered, 8 pages + references |
| Apr 30, 2027 | Notification | ~10 weeks before the July 6–11 conference |

The compressed April-to-July runway is a distinctive RSS pressure: camera-ready (May 14,
2027), travel authorization, and artifact release all share it.

## Calibrating expectations by venue contrast

- Unlike venues with universal author-response phases, only papers invited at Stage 1
  rebut; a Stage 1 rejection on February 5 is final for the cycle.
- Unlike rolling-review journals, the revise step is bounded: one Charter, one final
  submission, then accept or reject.
- Scores and thresholds are internal; public acceptance statistics were not verified
  (待核实) — do not quote community folklore rates as fact.

## Confidentiality and conduct

- Reviewer identities stay confidential during review (they are published only with
  accepted papers' reviews); do not attempt identification or out-of-band contact.
- Reviewers are asked to flag hallucinated references and rule violations (such as
  anonymity breaches) to the AC; both lead to desk rejection.

## Who sits in the reviewer pool

- The pool spans planning, control, perception, learning, and mechanism design;
  topic matching at a smaller venue is tight, so expect at least one reviewer who
  has personally run experiments like yours — protocol hand-waving gets caught.
- Because the audience is the whole field, at least one review often comes from an
  *adjacent* subfield; jargon-dense writing loses exactly the vote the single-track
  format makes decisive.
- Area Chairs are established researchers appointed per edition; the AC's synthesis
  carries the meeting, which is why every skill in this pack optimizes for the
  AC-compressible summary.

## Output format

```text
[Stage] stage 1 review / rebuttal invited / stage 1 reject / charter execution / final review / decided
[Objection triage] correctness: <...> | scope: <...> | significance: <...>
[AC-compressible summary] <two sentences the AC could say in the meeting>
[Rebuttal leverage] high / low / none (not invited)
[Next move] <one action>
```
