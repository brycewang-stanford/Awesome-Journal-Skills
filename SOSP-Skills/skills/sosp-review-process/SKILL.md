---
name: sosp-review-process
description: Use when reasoning about how a SOSP submission is evaluated — double-blind HotCRP reviewing, staged review rounds, PC-chair-audited conflicts, the pre-PC-meeting author response, the single-track PC meeting where every decision is argued live, notification, and shepherded acceptance outcomes.
---

# SOSP Review Process

Use this to model what happens to a SOSP paper between the April upload and the July
decision, and to time author-side actions to the phases that actually move outcomes.
Anchors below are from the 2026-cycle CFP and the `sosp26.hotcrp.com` schedule
(checked 2026-07-08): submission April 2026, author response ahead of the PC meeting,
notification **July 3, 2026**.

## The pipeline

| Phase | Who acts | What authors can do |
|---|---|---|
| Conflict screening (from abstract registration) | PC chairs audit declared conflicts, add or **remove** entries | Declare defensibly; chairs treat strategic conflicts as misconduct-adjacent |
| Early reviewing | A subset of the PC reads every paper | Nothing — the paper speaks alone |
| Later-round reviewing | Papers still alive draw additional, often more senior, reviews | Nothing; round structure and counts vary by year (待核实 per cycle) |
| Author response | Authors correct factual errors, answer posed questions | The one sanctioned intervention (see `sosp-author-response`) |
| PC meeting | Full committee discusses candidates live, single track | Nothing — but the response was written for this room |
| Decision + shepherd assignment | Chairs notify July 3; accepted papers get a shepherding PC member | Camera-ready planning begins (see `sosp-camera-ready`) |

Two structural facts do most of the explanatory work. First, reviewing is **staged**:
a paper that reads as unsound in the first pass never reaches the reviewers most
likely to appreciate a subtle contribution, so the opening pages must survive a
skeptical fast read (see `sosp-writing-style`). Second, decisions are made **in a
meeting**, not by score averaging: one convinced advocate who can defend the paper
against live objections beats four mildly positive scores.

## Reading SOSP reviews

Systems reviews concentrate their weight in predictable places:

- **Soundness attacks** ("the evaluation doesn't isolate the claimed mechanism",
  "this workload can't show the tail behavior claimed") are the score-drivers.
  Address these first in any response.
- **Positioning complaints** ("how is this different from X at OSDI two years ago")
  signal a related-work gap the meeting will replay (see `sosp-related-work`).
- **Taste judgments** ("incremental", "not SOSP-worthy") rarely change through
  argument; they change when an advocate reframes the paper's principle at the
  meeting — which your response can quietly arm with one crisp sentence.

```text
Post-review triage sheet (fill before drafting anything)

For each review R1..Rn:
  overall lean:        champion / positive / neutral / negative / kill
  score-driving issue: <one sentence>
  type:                factual error | missed content | posed question | judgment
  response-eligible?:  yes (types 1-3) / no (type 4)
Meeting risk:          <the objection an advocate could not answer alone>
```

## Confidentiality and integrity edges

- Reviews and PC discussion are confidential; reviewers are anonymous forever, and
  guessing at reviewer identity in the response reads badly (reviews are anonymous
  in both directions).
- Double-blind holds until notification. Do not advertise the submission where PC
  members will see it; the CFP's anonymization duty does not lapse after upload.
- HotCRP is the channel of record. Deadline-adjacent questions go to the PC chairs
  through it, not to PC members you happen to know — that is a conflict violation
  in a culture that audits conflicts.

## Calibrating expectations

SOSP is a low-acceptance venue where most submissions are competent; rejections
routinely carry reviews that would be accepts elsewhere. Per-year submission counts
and acceptance rates are published with each program (待核实 for 2026 until the
program appears; cross-check `dl.acm.org/conference/sosp` and dblp for history).
Practical consequences of the meeting-centric model:

1. A rejected paper with one strong champion review is often a revise-and-retarget
   candidate for the next systems deadline, not a redesign candidate.
2. Reviews written for the meeting compress; a terse negative review may encode a
   long live discussion. Mine every sentence — each one survived an argument.
3. Because SOSP and its sibling OSDI both now run annually, the cost of a rejection
   is measured in months, not years (see `sosp-workflow` for the retargeting map).

## Output format

```text
[Phase] where the paper sits in the pipeline now
[Review map] per-review lean + score-driving issue + response eligibility
[Meeting risk] the one live objection to defuse
[Action] respond / wait / prepare retarget
[Integrity check] anonymity holds? all contact via HotCRP?
```
