---
name: neurips-workflow
description: Use when planning a NeurIPS manuscript workflow from topic selection through submission, review, author response, decision, camera-ready, artifact release, and possible rerouting.
---

# NeurIPS Workflow

Use this skill as the router for the NeurIPS depth pack. It helps choose the next skill and stage
the work so a manuscript does not arrive at submission with hidden policy or evidence gaps.

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

## Output format

```text
[Current stage] topic / drafting / pre-submission / review / rebuttal / camera-ready / reroute
[Next skill] <one NeurIPS skill>
[Official source to open] <CFP/handbook/template/OpenReview/checklist>
[Blocking gap] <policy/evidence/artifact/writing>
[Next action] <concrete task>
```

