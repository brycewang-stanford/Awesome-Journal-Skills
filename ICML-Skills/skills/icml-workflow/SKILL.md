---
name: icml-workflow
description: Use when planning an ICML manuscript workflow from topic selection through drafting, submission, review, author response, camera-ready, PMLR publication, public artifacts, and rerouting.
---

# ICML Workflow

Use this as the router for the ICML depth pack. It chooses the next skill and keeps policy,
evidence, artifact, and public-record risks visible.

## Stage map

1. Fit and track: `icml-topic-selection`.
2. Drafting: `icml-writing-style`, `icml-related-work`, `icml-experiments`.
3. Artifact and supplement: `icml-artifact-evaluation`, `icml-reproducibility`, `icml-supplementary`.
4. Pre-submission audit: `icml-submission`.
5. Review diagnosis: `icml-review-process`.
6. Rebuttal and discussion: `icml-author-response`.
7. Accepted-paper work: `icml-camera-ready`.

## Working principles

- Start with the current ICML official pages, not last year's memory.
- Maintain a table mapping claims to main-paper evidence, appendix evidence, code/data, and
  limitations.
- Keep anonymous review artifacts and public release artifacts as separate states.
- Treat reciprocal reviewing, reviewer LLM policy, impact statements, lay summaries, and public
  original-submission release as first-class workflow items.
- Decide early whether a paper is really an ICML main-track paper or better suited to a position
  paper, workshop, NeurIPS, ICLR, AISTATS, TMLR, JMLR, or a domain venue.

## Output format

```text
[Current stage] fit / drafting / pre-submission / review / response / camera-ready / reroute
[Next skill] <ICML skill>
[Official source to open] <CFP/Author Instructions/FAQ/OpenReview/LLM policy>
[Blocking gap] <policy/evidence/artifact/writing/public-record>
[Next action] <concrete task>
```

