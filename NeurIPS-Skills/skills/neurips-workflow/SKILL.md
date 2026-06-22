---
name: neurips-workflow
description: Use when planning and sequencing a full NeurIPS manuscript workflow from topic and track selection through writing, the mandatory Paper Checklist, OpenReview submission, double-blind review, author response, decision, camera-ready, artifact release, and rerouting to the Datasets & Benchmarks track, a workshop, or MLRC/TMLR.
---

# NeurIPS Workflow

Use this skill as the router for the NeurIPS depth pack. It helps choose the next skill and stage
the work so a manuscript does not arrive at submission with hidden policy or evidence gaps.

NeurIPS is a conference, not a journal: it has no standing editor-in-chief and no article-processing
charge. The rotating leadership is the per-edition General Chairs and Program Chairs (2026 General
Chairs: Hsuan-Tien Lin and Razvan Pascanu, verified 2026-06-22), and the cost model is registration
fees, not APCs — proceedings are open-access on OpenReview. Conference organizers rotate yearly, so
re-check the current CFP and committees page rather than carrying a name forward.

## Stage map

1. Topic and track fit: use `neurips-topic-selection`.
2. Paper shaping: use `neurips-writing-style`, `neurips-related-work`, and `neurips-experiments`.
3. Artifact and supplement planning: use `neurips-artifact-evaluation`, `neurips-reproducibility`,
   and `neurips-supplementary`.
4. Final pre-submission audit: use `neurips-submission`.
5. Review diagnosis: use `neurips-review-process`.
6. Rebuttal and discussion: use `neurips-author-response`.
7. Acceptance and public release: use `neurips-camera-ready`.

## Operating principles

- Start official-source checks early; NeurIPS annual policies change.
- Keep track choice explicit. A main-track method paper, E&D paper, position paper, and MLRC paper
  are not interchangeable.
- Write the checklist in parallel with the paper rather than at the end.
- Maintain one evidence table mapping every central claim to proof, experiment, data, artifact, and
  limitation.
- Keep an anonymous review artifact and a de-anonymized public release artifact as separate states.

## Deadline ladder to schedule backward from

NeurIPS spreads its gates across the year, so plan backward from the abstract deadline, not the
full-paper deadline. The exact dates move every cycle; reopen the current CFP and Main Track Handbook
for the live calendar.

| Gate | What locks here | Skill to finish before it |
| --- | --- | --- |
| OpenReview profiles | every author needs an active, complete profile | `neurips-submission` |
| Abstract deadline | title, abstract, and author list freeze (order may change after) | `neurips-topic-selection`, `neurips-related-work` |
| Full-paper deadline | PDF, checklist, and code/data ZIP submitted together | `neurips-experiments`, `neurips-supplementary` |
| Reviews released | nothing changes; you read and triage | `neurips-review-process` |
| Author-response window | rebuttal through OpenReview, no new paper version | `neurips-author-response` |
| Decision | accept (spotlight/poster) or reject | `neurips-camera-ready` if accepted |
| Camera-ready | de-anonymize, finalize checklist, public artifacts | `neurips-camera-ready`, `neurips-artifact-evaluation` |

## Track-fork early warning

Decide the track before drafting, because the Datasets & Benchmarks track, Position Papers track, and
MLRC/TMLR reproducibility route each have a distinct call, checklist emphasis, and review rubric. A
dataset paper forced into the main track, or a reproduction study that belongs in MLRC, wastes a full
cycle. If `neurips-topic-selection` flags a fork, resolve it before any other stage.

## Worked vignette: where this router intervenes

A team has strong benchmark wins for a new retrieval method but no mechanism analysis and a thin
limitations paragraph. The router routes them to `neurips-experiments` (add ablations and error
analysis) and `neurips-writing-style` (calibrate the claim and the limitations) before
`neurips-submission`, rather than letting a leaderboard-only paper reach OpenReview where reviewers
predictably ask for the missing mechanism.

## Output format

```text
[Current stage] topic / drafting / pre-submission / review / rebuttal / camera-ready / reroute
[Next skill] <one NeurIPS skill>
[Official source to open] <CFP/handbook/template/OpenReview/checklist>
[Blocking gap] <policy/evidence/artifact/writing>
[Next action] <concrete task>
```

