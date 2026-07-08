---
name: sosp-camera-ready
description: Use when preparing a SOSP camera-ready after acceptance, working with an assigned shepherd toward the final deadline, expanding from the 12-page submission to the 13-page final limit (14 with shepherd approval), de-anonymizing safely, adding artifact badges, and meeting ACM proceedings requirements.
---

# SOSP Camera-Ready

Use this between a SOSP acceptance notification and the final-version deadline. The
2026-cycle anchors (verified 2026-07-08 on the sosp26 HotCRP deadlines page and the
official author guidelines): notification July 3, 2026; camera-ready due August 28,
2026; final papers may use **13 pages of technical content**, and the shepherd may
approve **one additional page** for a 14-page maximum. References remain uncounted.
Proceedings are published in the ACM Digital Library.

## Shepherding is the center of this phase

Accepted SOSP papers are shepherded: a PC member is assigned to see the revision
through, and the shepherd's sign-off — including on the optional 14th page — gates the
camera-ready. Treat the shepherd as the PC's delegate, not as a copy editor.

- Within days of notification, send the shepherd a **revision plan**: every substantive
  reviewer concern, what will change in the text, and what will not change with a
  one-line reason. Get agreement on scope before rewriting.
- Batch questions; shepherds are volunteers working around their own deadlines.
- If you want the extra page, ask early with a concrete use ("the failure-model
  discussion Rev C requested needs ~0.7 pages"), not at upload time.
- Disagreements about a requested change go through the shepherd to the chairs; never
  silently skip an agreed item — shepherds diff drafts.

## The extra page is for reviewers' concerns

The jump from 12 submitted pages to 13 (or 14) exists so the discussion-phase concerns
can be addressed with substance. Spend it in priority order:

1. Clarifications the reviews showed were needed — misread invariants, buried
   assumptions, undefined workload details.
2. Evaluation context reviewers asked for that the submitted runs already support.
3. Honest-limitations text that the PC meeting surfaced.

Do not spend it on new claims: results that were never reviewed, added to the final
version, are how camera-ready papers acquire post-publication trouble.

## De-anonymization checklist

The submitted PDF carried a paper ID and scrubbed context; reversing that has sharp
edges:

| Restore | Watch out for |
|---|---|
| Author block, affiliations, emails | Order and spelling final — the DL metadata is generated from this |
| Acknowledgments and funding | Grant numbers your funder requires verbatim |
| Real system and organization names | Employer/legal approval for deployment details that were generalized for review |
| First-person references to your prior work | Rewrite the third-person camouflage so citations read naturally |
| Repository and artifact URLs | Point at the archival artifact (see `sosp-artifact-evaluation`), not a moving main branch |

```bash
# Confirm no review-phase debris survives in the final PDF
pdftotext final.pdf - | grep -inE 'paper ?#?[0-9]{2,4}|anonym|double.blind|under submission' | head
pdfinfo final.pdf | grep -iE '^(author|title)'   # metadata should now be real
```

## ACM proceedings mechanics

- The ACM rights form arrives per-paper by email after acceptance; the completed rights
  block text and DOI must be placed in the paper exactly as issued. The title and
  author list on the form must match the PDF character for character.
- ORCID and author-profile linkage happen through the ACM submission pipeline; make
  sure every co-author completes their part before the deadline, since one missing
  rights confirmation blocks the whole paper.
- Artifact badges earned through evaluation are rendered on the DL page and may be
  stamped on the paper; coordinate badge placement with the camera-ready timeline
  rather than re-opening the PDF after upload. Exact form names and TAPS/workflow
  details vary by year — 待核实 against the acceptance-email instructions rather than
  assumed from this file.

## Sequencing against artifact evaluation and the conference

August is crowded: the camera-ready, the artifact-evaluation window, and conference
logistics (registration, visas for the host country, talk preparation) all run in
parallel. Assign different owners to the shepherd thread and the AE thread — both are
interactive, deadline-bound conversations, and one person context-switching between
them drops messages. Book travel for the conference (Sep 29 - Oct 2, 2026 in Prague
for the 2026 edition) as soon as acceptance is firm; attendance and presentation
expectations for the current year are stated in acceptance materials, not guessed.

## Output format

```text
[Camera-ready stage] plan agreed / revising / shepherd review / uploaded
[Page budget] 13 base + 14th requested? granted? <use>
[Revision map] <reviewer concern -> change or agreed no-change>
[De-anonymization] complete / pending items
[ACM mechanics] rights form / metadata match / badges / ORCID
[Parallel threads] AE owner, travel, talk
```
