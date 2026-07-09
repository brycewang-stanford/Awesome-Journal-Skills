---
name: mobisys-camera-ready
description: Use when preparing an accepted MobiSys paper for the ACM Digital Library camera-ready — de-anonymization, the ACM double-column final layout and 12-page budget, ACM rights and CCS metadata, delivering any results promised in the rebuttal, coordinating the three artifact badges, registration, and the June in-person talk and demo in Cambridge.
---

# MobiSys Camera Ready

Use this after acceptance. Reopen the current camera-ready instructions, the ACM rights form,
the registration page, and the decision email before advising authors — dates and forms are
cycle-specific.

## Camera-ready audit

- Convert the anonymous submission to the public ACM version: author names, affiliations,
  acknowledgements, funding, and de-anonymized code/data links.
- Apply the current ACM double-column template and page budget. MobiSys 2026 kept a **12-page
  body including figures and tables**; references and appendices sit outside the cap — confirm
  the final-version rule against the current instructions.
- Deliver every result **promised in the rebuttal**; a promised camera-ready experiment that
  never appears is a credibility failure the AC may notice.
- Complete ACM rights, the CCS concepts/keywords metadata, title/abstract/author-order
  metadata, and the bibliography.
- Coordinate the three artifact badges so passing badges are printed on the paper and recorded
  in the ACM DL (`mobisys-artifact-evaluation`).
- Confirm registration and the June in-person obligation; MobiSys expects at least one author
  to present.

## What changes between the reviewed and final version

| Element | Reviewed (anonymous) | Camera-ready (ACM) |
|---|---|---|
| Author block | Stripped | Restored with affiliations |
| Repository links | Anonymized placeholder | Public, licensed, archival |
| Screenshots / demo media | Blurred / de-identified | Restored, subject to vendor NDA |
| Rebuttal promises | Pending | Delivered in body/appendix |
| Metadata | Minimal | ACM rights + CCS concepts |

## De-anonymization sweep

- Restore the author block, acknowledgements, grants, and any contribution statements the
  anonymous version stripped.
- Replace anonymized repository placeholders with the public, licensed, archival artifact and
  test every link from a logged-out browser.
- Un-blur screenshots and demo media, and restore device/vendor names where they were hidden
  for review — while respecting any vendor NDA on hardware details.

## ACM double-column reflow

- Switching the template from anonymous to final mode changes spacing; recheck every page
  break, figure placement, and wide device-table width after the flip.
- Adding the author block, acknowledgements, and funding lines can push the body over budget;
  confirm the 12 pages still hold rather than assuming.
- Keep figure, table, and section numbering identical to the reviewed version so the review and
  rebuttal record remain traceable to the final text.

## Worked example: integrating a promised result

The rebuttal promised a fifth-device measurement to answer a generalization concern.
Camera-ready move: add the device to the multi-device table and one sentence of interpretation,
regenerate the figure from the artifact so numbers match, and note the device in App. A's
provenance table — without restructuring the accepted contribution.

## Camera-ready readiness

```text
Final-package checklist:
  PDF: ACM double-column, 12-page body confirmed, numbering unchanged
  metadata: ACM rights, CCS concepts, author order, abstract
  promises: every rebuttal-promised result delivered
  artifacts: badges coordinated, repo de-anonymized and archival
  logistics: registration done, June presenter and demo assigned
```

## Hedged logistics

- Registration pricing, ACM rights/OA mechanics, and exact camera-ready dates change every
  cycle; confirm against the decision email and current instructions.

## Output format

```text
[Camera-ready status] Ready / Needs fixes / Blocked
[Final package] <PDF/metadata/ACM rights/artifacts>
[Policy checks] <page/authors/presentation/registration/badges>
[Promise delivery] <rebuttal promise -> final edit>
[Remaining owner] <person -> task>
```
