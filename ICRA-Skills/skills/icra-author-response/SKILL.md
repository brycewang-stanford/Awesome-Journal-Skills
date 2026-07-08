---
name: icra-author-response
description: Use when responding to ICRA reviews in the channels that actually exist — turning decision-day reviewer comments into a disciplined camera-ready revision, writing the revise-and-resubmit response letter on the RA-L pathway, or converting an ICRA reject into a targeted IROS or RA-L resubmission — since classic ICRA offers no rebuttal.
---

# ICRA Author Response

At most conferences "author response" means a rebuttal window. Classic ICRA has
none (verify the current cycle — see `icra-review-process`): reviews arrive
together with the January decision. Author response at ICRA therefore happens in
three real channels, each with its own craft: the **camera-ready revision** after
acceptance, the **RA-L response letter** if the work travels the journal
pathway, and the **resubmission memo** after a reject. Doing these well is a
skill; pretending a rebuttal exists is a planning error.

## Channel 1: the camera-ready revision (accepted papers)

Reviewer comments on an accepted ICRA paper are advisory — no one re-checks
compliance — but ignoring them is shortsighted: reviewers are your first
readers, their confusions predict everyone else's, and the same people may
review the journal extension.

Triage each comment:

| Comment type | Action in camera-ready | Budget guard |
|---|---|---|
| Factual/math error caught | fix unconditionally | always fits |
| Ambiguity that misled a reviewer | rewrite the passage | high priority |
| Missing reference | add it | cheap |
| "Add experiment X" | usually defer to journal version; add only if data exists | 8-page total final limit |
| Stylistic taste | your call | lowest |
| Requests contradicting each other | pick one, note the tension in limitations | — |

Remember the geometry: submissions ran 6 content + 2 reference pages, while the
2026 final limit was 8 pages *total including references* — additions compete
with your bibliography. Never silently change claims: if a fix weakens a number,
the number changes and the text stays honest.

## Channel 2: the RA-L response letter (journal pathway)

Work routed through RA-L (see `icra-topic-selection`) can receive a revise
decision, and here a real response letter exists with journal norms:

```text
Response structure per point:
  R1.3 (reviewer text quoted verbatim, trimmed fairly)
  > Response: <direct answer first — yes/no/agree/disagree>
  > Change: Sec. III-B, para 2 rewritten; Table II adds the n=15
  >         wrist-mounted condition; Fig. 4 caption now states 1× speed.
  > (If disagreeing) Evidence: <measurement, citation, or derivation —
  >         never volume of prose>
```

- Answer every point, including the painful ones; a skipped point reads as
  concession or evasion.
- Lead with agreement where genuine — robotics reviewers respond well to "the
  reviewer is right; trials with the deformable set were added" because added
  hardware evidence is costly and shows commitment.
- Keep the letter's tone flat and technical; the AE reads it as a signal of
  whether a second round will converge.
- Respect the clock: RA-L revisions run on a fixed schedule within its
  ~6-month publish-or-reject envelope; start hardware reruns the day the
  decision lands, not after the letter is drafted.

## Channel 3: the resubmission memo (rejected papers)

A January ICRA reject reaches March IROS or same-week RA-L only through
disciplined conversion. Write an internal memo, not a grievance:

1. Extract every substantive objection; deduplicate across reviewers.
2. Classify: evidence gap / clarity failure / novelty challenge / scope
   mismatch (the categories predict different fixes).
3. For each, decide: fix with new data, fix with rewriting, or consciously
   accept the risk — with an owner and a date.
4. Diff the venue: what IROS or RA-L reviewers will additionally expect (RA-L
   reviewers, for instance, read with journal-permanence standards; a "promising
   demo" framing must mature into a validated-claim framing).
5. Reviewer-pool overlap is high across ICRA/IROS/RA-L — assume at least one
   repeat reader who will check whether their objection was addressed.

## Tone calibration (robotics reviewers, specifically)

- Reviewers here are practitioners; "in a real deployment this would not
  matter" arguments fail unless backed by deployment data they can see.
- Concede hardware limits plainly — "the F/T sensor saturates at 50 N, so
  higher-load trials were not possible" — rather than reframing constraints as
  choices; the community respects physical honesty.
- Avoid ML-rebuttal reflexes (citing three new preprints, promising a camera-
  ready appendix): ICRA has no appendix, and the channels above run on data
  and page-anchored edits, not citation volume.

## Discipline common to all three channels

- **Quote before answering.** Restating a comment in your own words invites the
  accusation of answering a strawman.
- **Evidence outranks assertion.** One added table row beats three paragraphs
  of explanation; in robotics, one new uncut video clip beats both.
- **Track everything.** Keep a comment → action → location ledger; it becomes
  the camera-ready cover note, the RA-L response letter skeleton, or the
  resubmission changelog respectively.
- **Never fabricate agility.** "We have added extensive new experiments" backed
  by nothing is checkable and fatal with overlapping reviewer pools.

## Ledger template

```text
| # | Reviewer point (quoted) | Class | Action | Where | Status |
|---|-------------------------|-------|--------|-------|--------|
| R2.1 | "success criterion never defined" | clarity | verbatim criterion added | Sec V-A | done |
| R1.4 | "compare against MPC baseline" | evidence | n=20 MPC trials run | Tab III | data 6/12 |
| R3.2 | "extend to deformables" | scope | deferred; limitation stated | Sec VII | done |
```

## Output format

```text
[Channel] camera-ready / RA-L letter / resubmission memo
[Comment ledger] <n> points: fix-now <n> / defer-stated <n> / risk-accepted <n>
[Evidence adds] <new trials/tables/clips committed, with dates>
[Page impact] fits final limit? <y/n + what moves>
[Repeat-reviewer check] objections addressed verbatim-quotably: y/n
[Deadline] <channel deadline and working backward date>
```
