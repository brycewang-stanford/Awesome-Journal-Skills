---
name: issta-camera-ready
description: Use when preparing an accepted ISSTA paper for the ACM Digital Library camera-ready, covering de-anonymization, the final ACM sigconf layout without the review/anonymous options, ACM rights forms and DOI, metadata and CCS concepts, the artifact DOI and badge display, registration, and the in-person presentation obligation.
---

# ISSTA Camera Ready

Use this after acceptance (including after a successful Major Revision). Reopen the current ISSTA
camera-ready instructions, the ACM proceedings author kit, the rights-form email, and the artifact
badge instructions before advising authors — the mechanics and dates are cycle-specific.

## Camera-ready audit

- Convert the anonymous submission to the published version: restore the author block,
  affiliations, acknowledgements, and funding, and drop the `review` and `anonymous` template
  options so line numbers and the anonymized front matter disappear.
- Complete the ACM rights process. ACM assigns the rights form after acceptance; the resulting
  copyright/permission block, conference notice, and DOI must appear in the final PDF exactly as
  issued.
- Fill ACM metadata: title, author order and ORCIDs, the abstract, and CCS concept tags. These feed
  the ACM Digital Library record and are hard to correct after publication.
- Resolve the review and (if applicable) Major-Revision comments in the accepted text without
  changing the contribution beyond what was reviewed.
- Display artifact badges correctly: if the artifact earned Available/Functional/Reusable/Results
  Reproduced, place the awarded badges and the artifact DOI as the instructions specify, and make
  the Zenodo deposit public.
- Confirm registration and presentation: ISSTA is an in-person symposium and expects at least one
  author to register and present; verify the current policy rather than assuming remote is allowed.

## ACM sigconf reflow after de-anonymization

- Switching off `anonymous` and `review` changes the front matter and removes line numbers, which
  reflows the first page and can shift every subsequent break; recheck figure placement, table
  widths, and column balance across the whole paper.
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
| Repository link | Anonymized mirror or withheld | Public, licensed, DOI-archived (Zenodo) |
| Acknowledgements / funding | Absent | Restored |
| Self-citations | Third person | Natural first person where it reads better |

## Worked example: landing a reviewer-requested change

A reviewer asked that a scoping limitation move from a footnote into the technique section.
Camera-ready move: add one sentence to Section 3 stating the limitation, cross-reference it from the
threats-to-validity discussion, and verify the added lines did not push a full-width table onto a
new page — without weakening any claim the reviewers accepted.

## Hedged logistics

- Registration pricing, the exact rights-form mechanics, CCS metadata fields, and camera-ready dates
  change every cycle; confirm against the acceptance email and the current ACM proceedings
  instructions, not this file.

## Output format

```text
[Camera-ready status] Ready / Needs fixes / Blocked
[Final package] <PDF/source/ACM rights block/DOI/metadata/CCS>
[Artifact] <badges displayed / DOI / Zenodo public>
[Policy checks] <page/authors/registration/presentation>
[Reviewer-change map] <concern -> final edit>
[Remaining owner] <person -> task>
```
