---
name: icra-submission
description: Use when auditing an ICRA paper for upload — PaperPlaza account and metadata, the 6-page-plus-2-reference-page limit, IEEE two-column template compliance, the double-anonymous rule introduced in the 2026 cycle, video-attachment specs (180 s, 20 MB), dual-submission conflicts with RA-L, and return-without-review triggers.
---

# ICRA Submission

Final-gate audit for a direct ICRA conference submission on PaperPlaza
(`ras.papercept.net`), the RAS submission system used across ICRA, IROS, and RA-L.
Everything here is anchored to the verified ICRA 2026 cycle; the numbers move, so
open the current year's "call for papers" page before trusting any of them.

## Hard limits (2026-cycle values — reverify each year)

| Check | 2026 rule | Consequence if violated |
|---|---|---|
| Page count at submission | 6 pages of content + up to 2 pages containing only references | Returned without review |
| Format | IEEE two-column conference template (RAS PaperPlaza support page templates), PDF only | Compliance failure at upload |
| Anonymity | Double-anonymous: no authors/affiliations in the PDF; full author list entered in PaperPlaza metadata | Administrative rejection |
| Video attachment | ≤ 180 seconds, ≤ 20 MB, one of mpeg/mp4/mpg | Rejected by the upload form |
| Video timing | Only inside the posted windows (2026: Aug 5–Sep 9 and Sep 17–22) | No video on record, no late path |
| Deadline | Sep 15, 2025, 23:59 **Pacific** (not AoE) | Closed portal |

The Pacific-time detail is a live trap: authors calibrated to AoE deadlines at ML
conferences lose up to five hours.

## The 2026 anonymity turn

Through ICRA 2025, review was single-blind — author names printed on page one.
The 2026 cycle switched to double-anonymous. Concretely:

- Strip the author block, affiliations, and identifying acknowledgements/grant
  numbers from the PDF; keep the full, final author list in PaperPlaza metadata
  (it cannot be extended casually later — treat the metadata list as binding).
- Rewrite platform tells: "our previously developed XYZ-Arm [12]" becomes "the
  XYZ-Arm [12]" with third-person citation.
- Blur or crop lab-identifying scenery in figures *and in the video attachment* —
  posters on the wall, safety vests with logos, institute door signs.
- Anonymize linked material: a GitHub URL with a lab organization name is an
  identity leak. Use an anonymized mirror or omit the link at submission.
- Because the policy is one cycle old, confirm it still holds for the target year
  before de-anonymizing or re-anonymizing anything.

## PaperPlaza mechanics worth knowing in advance

- Every author needs a PaperPlaza PIN; collecting PINs from six co-authors on
  deadline night is a known time sink — do it the week the site opens.
- The system runs its own PDF compliance test (fonts embedded, page size, page
  count); a failing PDF can be re-uploaded until the deadline, so test early.
- Keywords/session topics are chosen from a fixed RAS taxonomy and steer which
  Associate Editor sees the paper — pick the two or three closest, not the
  broadest.
- The submission confirmation email is the only receipt; archive it.

## PDF craft the compliance checker enforces

- Fonts must be embedded — the usual failures are figures exported from
  MATLAB/matplotlib with Type 3 or missing fonts; regenerate with embedded
  TrueType/Type 1 before deadline week.
- US Letter page size per the IEEE template; a European A4 build fails quietly.
- Vector figures where possible: reviewers zoom into plots of contact forces
  and trajectories, and rasterized 300-dpi exports turn to mush at 400%.
- Keep the final PDF a sane size — a 60 MB paper full of uncompressed photos
  strains the system and the reviewers' patience even where no hard cap bites.

## Dual-submission and the RA-L boundary

The same manuscript may not be simultaneously under review at ICRA and anywhere
else — including RA-L, arXiv exempted (a preprint is allowed; check the current
policy text for wording). The clean patterns:

- ICRA reject in January → revise → RA-L in February. Legal and common.
- RA-L accept in autumn → transfer within the posted window for conference
  presentation. Legal; this is the designed pathway.
- Same PDF to ICRA (September) and RA-L (October) "to hedge": dual submission,
  discoverable trivially since both run on PaperPlaza infrastructure with
  overlapping editorial boards.

## Metadata fields that outlive the deadline

Three PaperPlaza fields have consequences authors rarely anticipate:

- **Author list**: feeds the eventual IEEE Xplore record; a co-author omitted
  "to add later" creates an authorship dispute vector, not a placeholder.
- **Keywords**: route the paper to an Editor's area and its reviewer pool —
  effectively the only reviewer-selection influence authors get (see
  `icra-review-process`).
- **Abstract**: printed in the program and reviewer-bidding views; a stale
  abstract that diverges from the PDF makes bidding reviewers feel misled.

## Return-without-review triage

```text
severity ▲
  │ 7-page content body ............... certain return, no repair after deadline
  │ author names on page 1 (2026+) .... administrative reject
  │ template swapped for ML style ..... compliance flag, likely return
  │ references interleaved so page 7
  │   contains prose ................... counts against content limit — fix now
  │ video 200 s / 25 MB ............... attachment refused; trim or re-encode
  │ acknowledgements naming the grant
  │   and PI .......................... anonymity leak; delete for review
  ▼ metadata abstract ≠ PDF abstract ... sloppiness signal to the AE; sync them
```

## Pre-upload sequence (final 48 hours)

1. Regenerate the PDF from a clean clone of the paper repo; confirm the IEEE
   template class file is untouched.
2. Run the page split check: content ends on or before page 6; pages 7-8 contain
   nothing but the bibliography.
3. Anonymity sweep: PDF metadata (`pdfinfo`), acknowledgements, self-citations,
   figure backgrounds, video frames, embedded links.
4. Play the video attachment start to finish on a machine without the lab
   codecs; verify duration, size, and that captions carry no names.
5. Enter/verify PaperPlaza metadata: authors, keywords, abstract synced to PDF.
6. Upload paper and video; pass the compliance check; archive the confirmation.

## Output format

```text
[ICRA upload verdict] go / fix-first / no-go
[Page audit] content <n>/6, reference pages <n>/2
[Anonymity audit] pass / leaks: <list>
[Video audit] <s>s / <MB>MB / format / window date ok?
[Metadata audit] authors final? keywords chosen? abstract synced?
[Dual-submission] clear / conflict: <venue>
[Deadline math] <local time> vs 23:59 Pacific = <hours remaining>
```
