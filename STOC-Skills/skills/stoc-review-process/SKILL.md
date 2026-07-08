---
name: stoc-review-process
description: Use when reasoning about how a STOC (ACM Symposium on Theory of Computing) submission is evaluated — the SIGACT program-committee model with external subreviewers, HotCRP mechanics, double-blind conflicts, the November-to-February decision arc, and what best-paper designation and rejection each actually mean.
---

# STOC Review Process

Model for the anchor cycle: STOC 2026 submissions went to HotCRP
(`stoc26.hotcrp.com`) by November 4, 2025, and decisions were emailed on or
before February 1, 2026 — a roughly thirteen-week arc with no author-visible
intermediate stage announced in the CFP (checked 2026-07-08). The PC chair was
Artur Czumaj (University of Warwick); chairs and committees are reconstituted
every year by SIGACT, so treat all names as one-cycle facts.

## Who actually reads the paper

STOC uses the classical theory model, not the ML area-chair pyramid:

- A single program committee of several dozen theoreticians covers the whole
  field; each paper is assigned to a handful of PC members.
- PC members widely delegate detailed proof-reading to **external subreviewers**
  — often the postdoc or specialist closest to the sub-area. In practice the
  most technically engaged report on your paper is frequently written by someone
  not on the PC at all.
- The PC member then argues the paper's case (or its dismissal) in HotCRP
  discussion and, for contested papers, at the (physical or virtual) PC meeting.
  Papers near the boundary live or die on whether *one* PC member is willing to
  champion them against the accept-rate arithmetic.

Consequences for authors: write the overview for the cross-area PC member, the
proofs for the specialist subreviewer, and the first page for the five-minute
skim that decides how much attention the rest receives.

## What the committee optimizes

STOC self-defines as the SIGACT flagship for the theory of computation, and its
committee heuristics follow:

| Evaluation axis | The question in the PC discussion |
|---|---|
| Correctness | Has anyone verified the central argument? Any unresolved doubts sink the paper |
| Significance | Does this change what the field knows — barrier broken, problem closed, model clarified? |
| Breadth of interest | Can a non-specialist on the PC see why it matters? (STOC's distinguishing axis vs. specialized venues) |
| Novelty of technique | Will the machinery be reused by others? |
| Presentation | Could the committee actually follow the guaranteed-read pages? |

Note what is absent: no experiments axis, no artifact axis, no checklist score.
And note the STOC-specific weight on breadth — a technically flawless result
whose interest is confined to one subcommunity is precisely the paper that gets
"strong work, better suited to <specialized venue>" at STOC.

## Timeline anatomy (2026 cycle)

```text
Nov 1, 2025   opt-in LLM pre-submission feedback upload (experiment; authors-only output)
Nov 4, 2025   submission deadline, 4:59pm EST (not AoE)
Nov-Jan       assignment -> subreviews -> PC discussion on HotCRP
              possible chair-mediated author queries (custom, not guaranteed)
<= Feb 1, 2026  accept/reject notification by email
Mar 31, 2026  camera-ready (AoE) + full version public on arXiv/ECCC
Jun 22-26, 2026  conference (Salt Lake City; TheoryFest program)
```

No rebuttal round existed in this arc; `stoc-author-response` covers what to do
instead. Reviews are typically released with the decision, at varying levels of
detail.

## Double-blind mechanics, HotCRP flavor

- STOC 2026 was double-blind: reviewers were not shown author identities, and
  submissions had to avoid revealing them. Conflicts are declared on HotCRP by
  authors against PC members; incomplete conflict declaration is an integrity
  issue, not an oversight.
- Subreviewer anonymity runs the other way too — you will likely never learn
  who verified your proofs. Do not fish for reviewer identity on social media
  or at the conference; theory is a small community and this is remembered.

## Where author leverage exists (and doesn't)

Because the process has no author-visible stages between upload and decision,
all leverage is front-loaded:

- **Bid-stage leverage:** the HotCRP-form abstract and topic selections decide
  which PC members bid; a mis-scoped abstract routes the paper to reviewers
  who will judge it by the wrong sub-area's standards.
- **Assignment leverage:** honest, complete conflict declaration protects the
  paper from a forced late reassignment to a less suitable reviewer.
- **Champion leverage:** the technical overview is written for the PC member
  who must defend the paper in discussion; give that person the three
  sentences they will repeat in the meeting.
- **No leverage:** contacting reviewers, lobbying the chair, or updating the
  preprint with "response to reviews" mid-cycle. None of these reach the
  decision; the last can violate anonymity rules.

## Outcomes and their meanings

- **Accept.** All accepted papers get talks under the TheoryFest program. The PC
  may additionally designate up to four **Best Papers** (chosen by the PC subset
  without submissions), and all-student-author papers compete automatically for
  the **Danny Lewin Best Student Paper Award** (SIGACT prize pages, checked
  2026-07-08).
- **Reject.** At a venue accepting a modest fraction of submissions (exact rate
  per cycle: 待核实), rejection frequently reads "true and correct, but not
  STOC-scale." The reviews distinguish which axis failed — correctness doubts
  demand repair; significance doubts demand either a stronger result or a
  better-matched venue (`stoc-topic-selection`); breadth doubts often just mean
  SODA/CCC/ITCS was the right first stop.
- Rejected papers commonly resurface at the next FOCS with visible
  improvements; the reviewing pools overlap heavily, and committees notice both
  improvement and its absence (`stoc-workflow` plans this cycle).

## Cycle-volatility warnings

- PC chair, committee, meeting format, review-form wording, and any feedback
  experiments are re-decided annually; the LLM-feedback program was explicitly
  labeled an experiment for 2026 (待核实 for future cycles).
- Double-blind is recent at STOC and its detailed rules (preprint interaction,
  conflict granularity) may be refined; re-read the live CFP each fall.

## Output format

```text
[Stage] pre-submission / under review / decided
[Reader model] <PC-member story vs subreviewer-proof story both present?>
[Committee axes at risk] correctness / significance / breadth / technique / presentation
[Timeline expectation] <next event and date, from the live cycle>
[If rejected] <axis that failed -> repair, re-scope, or re-route>
```
