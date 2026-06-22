---
name: icml-workflow
description: Use when planning or sequencing an ICML manuscript workflow end to end - from topic selection and drafting through OpenReview submission, double-blind review, author response, camera-ready, PMLR publication, public original-submission release, and rerouting decisions. Use when you need the next ICML skill, the official page to reopen, or the blocking gap for the current stage.
---

# ICML Workflow

Use this as the router for the ICML depth pack. It chooses the next skill and keeps policy,
evidence, artifact, and public-record risks visible.

ICML is a conference, not a journal: it has no standing editor-in-chief and no article-processing
charge. The rotating leadership is the per-edition General Chair and Program Chairs (2026 General
Chair: Tong Zhang; Program Chairs: Dudik, Jaggi, Agarwal, Li, verified 2026-06-22), and the cost
model is registration fees, not APCs — PMLR proceedings are open-access with no author fee.
Conference organizers rotate yearly, so re-check the current CFP and committees page rather than
carrying a name forward.

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

## Deadline cadence (verify against the current CFP)

ICML runs an abstract deadline before the full-paper deadline, and the 2026 cycle freezes the author
list at the abstract stage. Treat the cadence as: abstract and author list locked, then full PDF and
supplement, then reviews, then the response window, then one discussion round, then decisions, then
camera-ready and the PMLR-bound proceedings. Never hard-code the exact dates here; reopen the current
year's CFP because they move annually.

## Stage-to-risk router

| Stage | Dominant ICML risk | First skill to open |
| --- | --- | --- |
| Fit | Wrong track (main vs Position Papers) | `icml-topic-selection` |
| Drafting | Claim outruns evidence in 8 pages | `icml-writing-style`, `icml-experiments` |
| Pre-submission | Anonymity or page-limit desk reject | `icml-submission` |
| Response | One-round rebuttal misallocated | `icml-author-response` |
| Accepted | Public-record exposure on OpenReview | `icml-camera-ready` |

## Worked routing pass

A team has an adaptive-optimizer paper with a convergence proof and ImageNet-scale benchmarks. The
router sends them first to topic selection (confirm main-track, not Position Papers), then to
experiments and writing-style for the tuned-baseline and compute-disclosure gaps, then to submission
for the OpenReview and format-checker audit. Each handoff records the official page to reopen so the
plan never relies on last year's remembered rules. After decisions, an accepted paper flows to
camera-ready with its public-record state in mind, while a rejected one loops back to topic selection
or reroute, carrying the reviewer-quotable issue into the next venue choice.

## Output format

```text
[Current stage] fit / drafting / pre-submission / review / response / camera-ready / reroute
[Next skill] <ICML skill>
[Official source to open] <CFP/Author Instructions/FAQ/OpenReview/LLM policy>
[Blocking gap] <policy/evidence/artifact/writing/public-record>
[Next action] <concrete task>
```

