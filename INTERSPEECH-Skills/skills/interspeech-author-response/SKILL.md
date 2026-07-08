---
name: interspeech-author-response
description: Use when INTERSPEECH reviews arrive on CMT and a rebuttal is due — triaging three-or-more speech reviewers with mixed science/engineering instincts, answering WER/MOS evidence doubts with material already in the 4-page record, keeping replies anonymous, and writing for the meta-reviewer who decides in June.
---

# INTERSPEECH Author Response

Interspeech added an author rebuttal to its historically response-free pipeline in
recent cycles; for 2026 the response window was reported as 24 April – 1 May, ahead
of the 5 June notification. Confirm the live mechanics (length cap, CMT form fields,
whether replies go to reviewers or only the area chair) before writing a word —
rebuttal formats at this venue are young and still moving.

## Know your audience mix

An Interspeech review set typically mixes reviewer species, because ISCA's areas
span science and engineering:

| Reviewer instinct | What they attacked | What convinces them |
|---|---|---|
| Speech engineer | Baselines stale, WER delta within noise | Point to the significance test or per-condition breakdown already in the paper |
| Speech scientist | No phonetic/error analysis, claims exceed perception data | Cite the analysis subsection; concede scope honestly |
| ML generalist | "Incremental over the arXiv version of X" | State the technical delta in one sentence; note what the 4-page record shows |
| Resource skeptic | Corpus license, split leakage, evaluation protocol | Quote the exact split/protocol line; name the license |

Answer each reviewer in their own dialect. A MOS-methodology objection answered with
more WER numbers reads as a dodge.

## The 4-page constraint shapes the rebuttal

Unlike venues with appendices, everything reviewable was on those four pages — so
"see appendix" is never available. Your levers are:

- **Locate**: most objections at Interspeech are density casualties; the answer is in
  the paper but compressed. Quote section and line.
- **Reframe**: restate what the 4 pages could not spell out — one derivation, one
  clarified protocol — briefly, as clarification, not as new content.
- **Concede and scope**: if the evidence truly is not there, say so and state what a
  camera-ready (or the next cycle) would add. Speech reviewers punish bluster more
  than gaps.

Whether new numbers are allowed in the response varies by cycle; if unverified,
assume tables of new results are unwelcome and offer them as camera-ready additions.

## Anonymity does not pause

The response is part of the double-anonymous record and the anonymity period runs
until decisions. No identity hints, no links to demo pages created after submission
under identifiable accounts, no "as our group showed at Interspeech 2024."

## Reply skeleton

One block per objection, ordered by decision weight:

```text
R1-Q2 (statistical validity of the 0.4 WER gain):
- The concern: gains may be within run-to-run variance.
- In the record: Table 2 reports mean±sd over 3 seeds; Sec 4.2 gives the
  bootstrap 95% CI on test-other, excluding zero.
- Clarification: the CI uses utterance-level resampling (1000 draws).
- Offered for camera-ready: add the matched-pairs test on test-clean.
```

Four to six lines each. The meta-reviewer will compress you anyway — pre-compress.

## Triage order under a one-week window

1. **Day 1**: read all reviews twice; tag each point evidence / clarity / scope /
   taste. Ignore taste unless the meta-reviewer could echo it.
2. **Days 2–3**: draft the evidence answers first — they decide acceptance at a
   venue where "not convincing" is the modal reject phrase.
3. **Day 4**: cross-reviewer consistency pass; contradictory replies to two
   reviewers are visible to the area chair on CMT.
4. **Day 5**: cut a third; verify the character/word cap; submit early. CMT under
   deadline load is not where you want to be at 23:58 AoE.

## What to skip

- Do not re-argue the venue ("this is more of an ICASSP concern") — the routing
  decision was yours at area selection.
- Do not promise a Long Paper resubmission as a fix for missing evidence.
- Do not thank at length; the cap is better spent on the CI you computed.
- Do not respond to score, only to content — scores at Interspeech shift through the
  meta-review, not through indignation.

## Pre-send checklist

- [ ] Every objection from every reviewer is acknowledged, even if only with one
      scoped sentence — silence on a point reads as concession.
- [ ] Each factual reply cites a section, table, or figure of the submitted PDF.
- [ ] No new result tables unless the live instructions explicitly permit them.
- [ ] Replies to different reviewers tell one consistent story.
- [ ] Zero identity signals: no lab names, grant codes, fresh links, or
      "our Interspeech 2024 system" phrasing.
- [ ] Word/character cap verified against the CMT form, not against habit.
- [ ] Someone outside the author list read it cold and could restate each
      objection from your answer alone.

## Emotional discipline, briefly

Interspeech reviews arrive compressed and sometimes blunt — three reviewers
covering a 4-page paper leave little space for pleasantries. The productive
reading: every blunt sentence is a compression artifact of a real concern.
Extract the concern, drop the tone, and never mirror bluntness back; the
meta-reviewer reads your temperament as evidence about the work's solidity.

## If there is no rebuttal this cycle

Rebuttal mechanics at Interspeech are recent and not guaranteed to recur. If the
current cycle runs without one, this skill still applies at two later moments:
the camera-ready revision memo (accepted papers), where reviewer concerns get
addressed in print, and the next-cycle revision plan (rejected papers), where
the same objection map drives the rewrite — see `interspeech-review-process`
for the triage lanes.

## Output format

```text
[Review set] R1/R2/R3(+) one-line objection map, tagged by type
[Decisive objection] <the one the meta-reviewer will weigh>
[Anchors] <section/table/figure of the 4-page record answering each point>
[Concessions] <honest gaps + camera-ready offers>
[Rebuttal draft] <numbered blocks per skeleton, within the live cap>
[Verify first] cap / new-results policy / who reads it — from the live CMT form
```

The 2026 window dates above came from secondary renderings and are flagged 待核实 in
`resources/official-source-map.md`; the official author pages control.
