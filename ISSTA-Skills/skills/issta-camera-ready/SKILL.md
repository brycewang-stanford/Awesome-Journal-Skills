---
name: issta-camera-ready
description: Use when preparing an accepted ISSTA paper for the PACMSE (ACM Digital Library) camera-ready, covering de-anonymization, the final ACM acmsmall layout without the review/anonymous options, ACM rights forms, the ACM OPEN/APC step and DOI, metadata and CCS concepts, the artifact DOI and badge display, and the registration and presentation requirements.
---

# ISSTA Camera Ready

Use this after acceptance (including after a successful Major Revision). ISSTA 2027 camera-ready is
due July 22, 2027 (AoE); papers appear in PACMSE, Issue ISSTA 2027. Reopen the current ISSTA
camera-ready instructions, the ACM author kit, the rights-form email, and the artifact
badge instructions before advising authors — the mechanics and dates are cycle-specific.

## Camera-ready audit

- Convert the anonymous submission to the published version: restore the author block,
  affiliations, acknowledgements, and funding, and drop the `review` and `anonymous` template
  options so line numbers and the anonymized front matter disappear.
- Complete the ACM rights process. ACM assigns the rights form after acceptance; the resulting
  copyright/permission block, conference notice, and DOI must appear in the final PDF exactly as
  issued.
- Settle open access: authors at an ACM OPEN institution pay no APC; otherwise an APC may apply
  (2027 amount to be announced; 2026 was US$250 ACM members / US$350 non-members, payable at
  camera-ready), with waivers available. The author list and title cannot differ from the
  submitted version.
- Fill ACM metadata: title, author order and ORCIDs, the abstract, and CCS concept tags. These feed
  the ACM Digital Library record and are hard to correct after publication.
- Resolve the review and (if applicable) Major-Revision comments in the accepted text without
  changing the contribution beyond what was reviewed.
- Display artifact badges correctly: if the artifact earned Available/Functional/Reusable, place
  the awarded badges and the artifact DOI as the instructions specify, make the archived deposit
  (Zenodo, FigShare or similar) public, and point the Data Availability section at its DOI.
- Confirm registration and presentation: the ISSTA 2027 pages (checked 2026-11-24) do not yet state
  the registration or presentation requirement for Singapore — verify the current policy rather
  than assuming either in-person or remote.

## ACM acmsmall reflow after de-anonymization

- Switching off `anonymous` and `review` changes the front matter and removes line numbers, which
  reflows the first page and can shift every subsequent break; recheck figure placement and table
  widths across the whole paper.
- The author block, affiliations, and acknowledgements consume space the anonymous version did not
  use; content that just fit at submission can overflow, so verify the page count against the final
  limit rather than assuming the accepted length still holds.
- Keep section, theorem, and listing numbering aligned with the reviewed version so the response
  record and any Major-Revision ledger stay traceable to the published text.

## De-anonymization sweep

| Item | Anonymous submission | Camera-ready |
|---|---|---|
| Author block | Removed | Restored with affiliations and ORCIDs |
| Tool / system name | Neutralized if it de-anonymized | Real name restored |
| Repository link | Anonymized mirror or withheld | Public, licensed, DOI-archived (e.g. Zenodo) |
| Acknowledgements / funding | Absent | Restored |
| Self-citations | Third person | Natural first person where it reads better |

## Worked example: landing a reviewer-requested change

A reviewer asked that a scoping limitation move from a footnote into the technique section.
Camera-ready move: add one sentence to Section 3 stating the limitation, cross-reference it from the
threats-to-validity discussion, and verify the added lines did not push a full-width table onto a
new page — without weakening any claim the reviewers accepted.

## Hedged logistics

- Registration pricing, the APC amount, the exact rights-form mechanics, CCS metadata fields, and
  camera-ready dates change every cycle; confirm against the acceptance email and the current ACM
  PACMSE instructions, not this file.

## Output format

```text
[Camera-ready status] Ready / Needs fixes / Blocked
[Final package] <PDF/source/ACM rights block/ACM OPEN or APC/DOI/metadata/CCS>
[Artifact] <badges displayed / DOI / archive public>
[Policy checks] <page/authors/registration/presentation>
[Reviewer-change map] <concern -> final edit>
[Remaining owner] <person -> task>
```
