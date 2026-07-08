---
name: isca-review-process
description: Use when reasoning about how an ISCA submission is evaluated — the two-round review structure with December and February reviewer waves, what the combined rebuttal-and-revision window means for decisions, PC-meeting dynamics at a flagship architecture venue, and how to read the eventual outcome.
---

# ISCA Review Process

Knowing the pipeline changes author behavior at three points: how the paper is
written (for two waves of readers), how the February window is used (it permits
revision, not just argument), and how the decision is interpreted. The stage
structure below is the verified ISCA 2026 calendar; internal committee mechanics
are described as community-typical practice, labeled as such, because programs
rarely publish them.

## The 2026 pipeline as verified

| Stage | 2026 dates | Author-visible? |
|---|---|---|
| Abstract registration | Nov 10, 2025 | yes — HotCRP |
| Paper submission | Nov 17, 2025 | yes |
| Round 1 reviews written | due Dec 19, 2025 | no (delivered later) |
| Round 2 reviews written | due Feb 13, 2026 | no |
| Rebuttal + revision window | Feb 16 - Mar 6, 2026 | yes — the pack's pivot point |
| PC deliberation and decisions | after the window; exact 2026 date 待核实 | outcome only |
| Conference | Jun 27 - Jul 1, 2026, Raleigh | yes |

## What two rounds imply

A two-round structure typically means an early wave of reviews on every paper,
after which papers that remain viable receive additional expert reviews in the
second round. Two operational consequences for authors:

- **The paper must survive a first reading by a possibly non-specialist
  architect.** Round 1 breadth is why the introduction and motivation section
  carry so much weight (`isca-writing-style`): a paper that requires subarea
  fluency to appreciate may not reach the readers who have it.
- **Review counts differ across papers.** Receiving five or six reviews usually
  signals second-round attention; receiving few does not reliably signal
  anything. Do not decode fate from counts — the window that follows is the same
  either way.

## The combined rebuttal/revision window

The distinctive verified fact of the 2026 cycle: authors got a **three-week
window (Feb 16 - Mar 6)** described as a rebuttal/revision period — long enough
to run experiments and change the PDF, not merely to file 500 words of protest.
Venues design such windows so the committee can *conditionally* like a paper:
reviewers name concrete deficiencies, authors demonstrate the fix is real, and
the PC judges the demonstrated fix rather than a promise. Strategy and mechanics
for the author side live in `isca-author-response`; the process-level points:

- Reviews arriving at window-open are the *complete* input you will get; there
  is no later dialogue round to clarify misreadings. Everything must land in
  this window's artifacts.
- Reviewers reconvene (online discussion, then a PC meeting) with your response
  and any revision in front of them. The audience is the whole paper's
  discussion group, including reviewers who liked it and need ammunition to
  defend it.

## Inside the committee room (typical practice, not CFP text)

Flagship architecture PCs conventionally work discussion lists ordered by
average score, with each paper championed or buried in minutes of conversation.
Patterns worth internalizing:

- A paper without a **champion** — one reviewer willing to spend social capital —
  rarely survives discussion regardless of decent scores. Rebuttals should be
  written to arm the champion, not to defeat the detractor.
- **Expertise asymmetry is normal:** the most negative review is often the least
  expert. The committee usually knows this; a calm, factual response lets them
  discount it. An irritated response makes the room defend its colleague.
- **Methodology objections travel well** in the room ("the baseline is untuned"
  fits in one sentence); nuanced defenses do not. This is why methodology rigor
  up front (`isca-experiments`) is cheaper than any rebuttal.
- Conflicted members leave the room; your conflict declarations are what make
  that machinery work (`isca-submission`).

## Reading the outcome

```text
ACCEPT            -> isca-camera-ready + isca-artifact-evaluation immediately;
                     June presentation logistics.
ACCEPT-with-shepherd (if used) -> the shepherd's list is a contract; satisfy it
                     completely and visibly in the camera-ready.
REJECT, reviews engage the mechanism -> the idea was heard; fix the named
                     deficiencies and retarget (MICRO spring / HPCA summer)
                     with the reviews as a to-do list.
REJECT, reviews dispute the premise -> the community doesn't buy the problem;
                     more results won't help — reframe or re-venue
                     (isca-topic-selection).
REJECT, reviews are thin/confused   -> often a routing casualty; check whether
                     your abstract-step topics steered assignment badly before
                     blaming the idea.
```

Whether ISCA 2027 uses the same round structure, offers a revision phase at all,
or publishes different outcome categories is unverified — the 2027 CFP was not
posted at check time (待核实).

## Confidentiality and conduct

Submissions are confidential review material: do not publicize reviews, do not
contact suspected reviewers, and route irregularities (leaked identity, hostile
review, suspected conflict violation) to the program chairs through official
channels only. Public deadline-week complaints are read by exactly the community
that reviews your next five papers.

## Author-side calendar hooks

- At submission: file the five hardest anticipated objections with pre-computed
  answers (`isca-workflow` makes this a named role).
- Window-open minus one week: environment resurrection drill — the simulator
  tree, configs, and workloads must run (`isca-reproducibility`).
- Window-open: triage day (see `isca-author-response`); no experiments before
  triage completes.
- Decision day: run the outcome tree above within 48 hours while morale allows
  planning.

Calendar facts from `../../resources/official-source-map.md` (verified
2026-07-08); committee-mechanics paragraphs are labeled community practice and
should be re-weighed against any process description the 2027 chairs publish.
Whenever a live 2027 reviewer-instructions page appears, it supersedes every
"typical practice" paragraph in this file — update the source map first, then
this skill.
