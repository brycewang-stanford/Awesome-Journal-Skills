---
name: aamas-workflow
description: Use when planning an AAMAS project timeline from venue fit through abstract, full-paper or extended-abstract upload, supplementary material, the double-blind rebuttal, decision, IFAAMAS camera-ready, registration, and presentation, with track-specific deadlines and backward-planning offsets for a game-theory-plus-experiments paper.
---

# AAMAS Workflow

Use this as the project-management skill for an AAMAS submission. Replace every date with the
current official timetable and work backward from the OpenReview cutoffs.

AAMAS is a conference owned by IFAAMAS, not a journal: it has no editor-in-chief and no
article-processing charge. Each edition is run by rotating General and Program Chairs, the cost
model is registration, and accepted papers are published open-access by IFAAMAS. Re-check the
current CFP and organization page rather than carrying names or dates forward - as of 2026-07-09
the live target is AAMAS 2027, whose full timetable was not yet confirmable.

## Milestones

- Venue fit: confirm the contribution is genuinely about interacting agents and choose the track
  (main full paper, extended abstract, AAAI, JAAMAS, Blue Sky, Demo, Competitions).
- Evidence lock: freeze the game, agent objectives, theorems, opponent sets, experiments, and
  supplement contents.
- Abstract deadline: submit the short plain-text abstract, authors, and keywords (main track's
  abstract is due before the paper).
- Paper deadline: upload the double-blind PDF and OpenReview fields.
- Supplement deadline: upload the anonymized zip within the size cap.
- Rebuttal window: respond to preliminary reviews with anonymous, evidence-anchored text; no new
  results.
- Decision: archive reviews, rebuttal, and the submitted version (all become public).
- Acceptance: prepare the IFAAMAS camera-ready, register, plan the in-person presentation, and
  release the public artifact.

## Backward plan from the paper deadline

| Weeks out (heuristic) | Game-theory-plus-experiments milestone |
|---|---|
| 8+ | Game defined, solution concept fixed, theorems proved |
| 6 | Self-play and opponent sets designed against each claim |
| 4 | Population runs complete, seeds logged |
| 3 | Full draft in AAMAS two-column format |
| 2 | Internal mock review by a game-theory-minded reader |
| 1 | Anonymity sweep, supplement assembly, deviation-test check |
| 0 | Abstract then paper on OpenReview; supplement by its own cutoff |

These offsets are planning heuristics only - anchor each to the current official timetable, and
remember the AAAI, JAAMAS, and Blue Sky tracks have *different* deadlines.

## Failure modes by stage

- Theory or the game still moving at week 3 forces last-minute definition edits nobody has
  re-verified - the classic AAMAS correctness reject in the making.
- Leaving format conversion to the final week surfaces two-column overflow of game figures late.
- Skipping the mock review forfeits the only chance to hear "this is really single-agent" from a
  friend instead of a reviewer.
- Building the supplement under deadline pressure is how anonymity leaks and missing opponent
  sets ship.

## Coordination notes

- Assign one named owner for the anonymity sweep and another for the opponent/seed logging;
  shared ownership is how both slip.
- Archive the exact submitted PDF, supplement, and any deviation-test harness, since rebuttal
  replies must quote them precisely and the record goes public.

## Output format

```text
[Current stage] idea / experiments / writing / abstract / submission / supplement / rebuttal / accepted
[Track + next deadline] <track and date/source, or unknown>
[Critical path] <three tasks that determine readiness>
[Risk register] <page / anonymity / interaction evidence / supplement / presentation>
[Owner map] <task -> person or role>
```
