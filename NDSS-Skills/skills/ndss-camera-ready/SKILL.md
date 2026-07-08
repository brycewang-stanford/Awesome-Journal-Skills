---
name: ndss-camera-ready
description: Use when converting an accepted NDSS paper into the final open-access version — satisfying Minor/Major Revision conditions, de-anonymizing, restoring disclosure specifics, adding earned artifact badges, and meeting the Internet Society proceedings and camera-ready requirements by the January deadline.
---

# NDSS Camera-Ready

Acceptance at NDSS produces a paper the *whole world* reads for free: proceedings and talk
videos are open access under the Internet Society, with no reader paywall and authors free
to self-post. The camera-ready is therefore a public artifact, not an archival formality —
and for many papers it must first discharge a revision condition. The 2027 camera-ready
deadline is January 6, 2027 (CFP, checked 2026-07-08).

## First, clear the decision's conditions

| Decision | Precondition to camera-ready |
| --- | --- |
| Accept | None — proceed to the checklist |
| Minor Revision | Make exactly the requested changes; a shepherd or the chairs confirm they are satisfactory |
| Major Revision (now accepted) | The re-review already judged the revision-task list fulfilled; carry those changes into the final version faithfully — do not quietly walk any of them back |

Treat any shepherd or revision-task list as binding text. Diff your final PDF against the
committed changes item by item; a reviewer who wrote a task will look for it in the
published paper, and its absence is the failure mode that follows a paper into print.

## De-anonymize deliberately

Submission was double-blind; the camera-ready reverses it, and reversal is where mistakes
enter:

- Add authors, affiliations, ORCIDs, and acknowledgments/funding in the template's fields.
- Restore the disclosure specifics that anonymity forced you to blur: real vendor names,
  CVE identifiers, advisory URLs, coordinated-disclosure dates. The open-access paper is
  part of the public disclosure record — get these exact.
- Replace anonymized artifact links with the archival DOI (see `ndss-artifact-evaluation`).
- Restore internal system/tool names, cited correctly.
- Verify every reference now that self-citation can be first-person and complete.

## Add earned artifact badges

If artifact evaluation passed, place the earned badges (Available / Functional / Reproduced)
on the first page using the provided badge style (`ndssbadges.sty` in the 2026 tooling) and
add the 2-page artifact appendix. Badges you did not earn do not appear — the committee's
report is the source of truth, not your ambition.

## Final production checklist

```text
[ ] Revision/shepherd conditions all discharged (item-by-item diff)
[ ] Current NDSS camera-ready template; body still within the limit after de-anon growth
[ ] Authors, affiliations, ORCIDs, acknowledgments, funding present and correct
[ ] Disclosure specifics restored and accurate (vendors, CVEs, dates, advisories)
[ ] Ethics Considerations section retained and consistent with the published claims
[ ] Artifact badges placed (if earned) + 2-page artifact appendix added
[ ] References complete; DOIs where available; self-citations de-anonymized
[ ] Fonts embedded; PDF compiles clean on another machine; metadata now correct
[ ] Copyright/publication forms submitted per Internet Society instructions
[ ] Presenter identified; Seoul registration and travel underway (visas!)
```

## The open-access consequence

Because there is no paywall between your paper and the field, two things follow. First,
errors are permanent and public — the timeline, the vendor name, the availability
statement will be read by the affected vendors and by future citers. Second, self-archiving
is explicitly permitted, so post the camera-ready on your own pages and repositories once
proceedings publish; there is no embargo to wait out.

## Present in Seoul

NDSS 2027 meets in Seoul, 22-26 March 2027 — the venue's first move off its long San Diego
February footing. Confirm attendance/presentation requirements on the current logistics
page (registration opened October 2026), and plan the talk for a room that will read the
free paper afterward: lead with the adversary and the finding, not the related work.

## Output format

```text
[Conditions] revision/shepherd items — each discharged? outstanding listed
[De-anonymization] authors / disclosure specifics / artifact link / tool names — done or gaps
[Badges] earned set placed? artifact appendix added?
[Production] checklist failures blocking submission
[Logistics] presenter, registration, visa lead time
```
