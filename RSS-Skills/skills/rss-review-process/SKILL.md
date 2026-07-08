---
name: rss-review-process
description: Use when explaining or strategizing around RSS (Robotics: Science and Systems) peer review — the double-blind OpenReview pipeline, the two-stage design where only above-threshold papers earn a one-page rebuttal, the Area Chair meeting that sets decisions, and what single-track selectivity does to reviewer expectations.
---

# RSS Review Process

Model how an RSS decision actually gets made. The mechanics below are the verified
2026 design (roboticsconference.org/reviewps/, checked 2026-07-08); the two-stage
structure itself is cycle policy, so confirm it survives before relying on it.

## The 2026 pipeline

```text
OpenReview submission (double-blind)
        │
   first review round
        │
   threshold gate ── below ──▶ reject (no rebuttal opportunity)
        │ above
   invited one-page rebuttal (due 2026-04-03 AoE)
        │
   Area Chair reads rebuttal
        │  (forwards to reviewers only if extra feedback is needed)
   Area Chair meeting ──▶ decisions (2026-04-27 AoE)
```

Two properties distinguish this from ML-conference discussion phases:

- **The rebuttal is earned, not granted.** Papers below the first-round threshold are
  decided without author input. Consequence: the submission itself must pre-answer
  foreseeable objections; there may be no second chance (`rss-writing-style`).
- **The audience of the rebuttal is the AC.** Reviewers may never see it. Write for
  the person running the meeting, not for a back-and-forth thread
  (`rss-author-response`).

## What single-track selectivity does to reviewing

Every accepted paper takes a slot in front of the whole conference, so the operative
question in the AC meeting is closer to "must the field hear this?" than "is this
sound?" Soundness is necessary, not sufficient. Practical consequences:

| Review dynamic | Cause | Author counter-move |
|---|---|---|
| High bar for "so what" | One program, finite slots | Lead with the claim's consequence for other subfields |
| Deep methodological reads | Specialized, smaller reviewer pool | State assumptions and protocol precisely; vagueness gets caught |
| Skepticism toward demo-style evidence | Science-first venue identity | Attribute failures, isolate mechanisms, report all trials |
| Low tolerance for padding | 8-page ceiling framed as ceiling | Cut aggressively; length is not a proxy for rigor here |

## Reading a borderline packet

- Separate *correctness* objections (a flaw in the claim or protocol) from *scope*
  objections (the claim is narrower than sold) from *significance* doubts (sound but
  not slot-worthy). Only the first two are rebuttal-addressable with existing
  evidence; the third is won or lost in the submission's framing.
- A lone enthusiastic review does not carry a paper through an AC meeting; a lone
  unanswered correctness objection can sink one. Triage accordingly.
- Decisions emerge from a synchronous meeting, so the AC's summary understanding is
  the decision artifact. Everything you write should compress well into two sentences
  an AC might say aloud.

## Timeline anatomy (2026 verified dates)

| Date (AoE) | Event | Author-side implication |
|---|---|---|
| Jan 30 | Papers in | Last word for below-threshold papers |
| Feb-Mar | First round (release date 待核实) | Do not plan around an assumed date |
| Apr 3 | Invited rebuttals due | Short notice — pre-draft objection answers |
| Apr 3-27 | AC digestion + meeting | No author-visible activity; silence is normal |
| Apr 27 | Decisions | ~11 weeks before the July conference |

The compressed April-to-July runway is a distinctive RSS pressure: camera-ready,
travel authorization, and artifact release all share eleven weeks.

## Calibrating expectations by venue contrast

- Unlike venues with universal author-response phases, RSS's threshold gate means
  a silent April is itself information — but never certain information, since
  invitation lists are confidential.
- Unlike rolling-review journals, there is no revise-and-resubmit: the meeting
  outputs accept or reject, and the improvement loop runs through the next venue
  slot (`rss-workflow`).
- Scores, forms, and thresholds are internal; public acceptance statistics were
  not verified for 2026 (待核实) — do not quote community folklore rates as fact.

## Confidentiality and conduct

- Reviewer identities, scores, and thresholds are confidential; do not attempt
  identification or out-of-band contact.
- Notification wording in 2026 covered "paper and demo acceptance" even though the
  CFP had no demo-paper category — treat demo mechanics as 待核实 rather than
  inferring a track.

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
[Stage] under review / rebuttal invited / no rebuttal / AC meeting pending / decided
[Objection triage] correctness: <...> | scope: <...> | significance: <...>
[AC-compressible summary] <two sentences the AC could say in the meeting>
[Rebuttal leverage] high / low / none (below threshold)
[Next move] <one action>
```
