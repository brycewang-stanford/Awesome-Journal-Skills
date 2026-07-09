---
name: siggraph-camera-ready
description: Use when preparing the final version of a conditionally accepted SIGGRAPH / SIGGRAPH Asia Technical Paper for publication in ACM Transactions on Graphics, covering the second-stage committee verification, TOG journal metadata and DOI, ACM rights and CCS concepts, final results video and representative image, and permanent code/data links.
---

# SIGGRAPH Camera-Ready

A SIGGRAPH accept is a **conditional** accept: your paper is not done until a Technical Papers
Committee member has verified the final version in the **second reviewing process**. The output is
an **ACM Transactions on Graphics (TOG)** journal article (e.g., SIGGRAPH 2026 = TOG Vol. 45,
Issue 4), so the camera-ready is a journal production task, not a proceedings cleanup. Facts below
trace to `resources/official-source-map.md`; reconfirm the current TOG production checklist and
deadlines.

## Clear the conditions first

Conditional acceptance came with required changes. Before any production polish:

- Turn every condition from the decision and reviews into a concrete edit, and keep a change map
  the second-stage reviewer can follow.
- Re-run and re-render anything a condition touched — a corrected artifact means a **re-rendered
  video and re-generated figure**, not a caption edit.
- Do not smuggle in unrequested new results that could reopen the review; deliver the conditions,
  strengthen the writing, stop.

## TOG journal metadata and rights

Because the paper publishes as a TOG article, complete the journal apparatus:

- **ACM rights form** (eRights) — obtain the correct copyright/permission block and DOI, and paste
  the exact rights text and DOI into the paper.
- **ACM CCS concepts** and author keywords — required TOG metadata; pick concepts that match the
  contribution, not a generic list.
- **ACM Reference Format** citation and the correct **TOG volume/issue/article-number/month**;
  the article number replaces page ranges in the journal.
- **ORCIDs** and confirmed author order and affiliations — the author list was locked at the form
  deadline; only correct affiliation/spelling, not membership.

## Format and length at final

- Recompile against the **current `acmart` (>= 2.16)** class in the journal (`acmtog`) format the
  final version requires; do not modify the class file.
- The single-column journal layout differs from the review PDF — reflow figures and the teaser,
  check that no figure crosses the margin, and confirm all fonts embed.
- Journal-track final versions may relax the review page cap; confirm the current-cycle length
  policy and the figures-only-page rules before adding material.

## The final media are part of the publication

- **Representative image** — supply the high-resolution final still the program and DL will use.
- **Final supplemental video** — re-encode at the required resolution/codec; caption it; ensure it
  matches the accepted (revised) results, and that you hold rights to every frame.
- **Permanentize code/data links** — replace any review-time placeholder with a stable archive
  (Zenodo DOI or Software Heritage) so the published article's links do not rot; this also sets you
  up for the Graphics Replicability Stamp (see `siggraph-artifact-evaluation`).

## Production checklist

```text
[Conditions] every required change made and mapped for the second-stage reviewer? yes/no
[Class] acmart >=2.16, acmtog final format, unmodified .cls, fonts embedded
[Rights] ACM eRights done; DOI + rights block pasted; ACM Reference Format present
[Metadata] CCS concepts, keywords, ORCIDs, TOG vol/issue/article number correct
[Media] high-res representative image + final results video (rights cleared)
[Links] code/data on a permanent archive (DOI/Software Heritage), not a personal URL
[Proof] re-read the compiled journal PDF cold; watch the final video end to end
```

## Common camera-ready failures

- Treating conditional accept as unconditional and skipping a required change — the second-stage
  reviewer can hold the paper.
- Shipping a review-quality video with the journal article, or one that no longer matches the
  revised results.
- Missing or wrong TOG article number / rights block — a production-desk bounce.
- Un-embedded fonts or an outdated acmart class at final.
- Leaving a personal GitHub link that will break, instead of a DOI-bearing archive.

## Output format

```text
[Camera-ready status] ready / blocked
[Conditions cleared] yes/no + change map link
[TOG metadata] rights/DOI/CCS/article-number all set? yes/no
[Media] final image + video rights-cleared and results-consistent? yes/no
[Archive] permanent code/data DOI in place? yes/no
[Blocking items] <ordered>
```
