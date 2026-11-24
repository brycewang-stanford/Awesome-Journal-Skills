---
name: mobisys-camera-ready
description: Use when preparing an accepted MobiSys paper for the ACM Digital Library camera-ready — clearing the anonymous shepherd, finalizing author metadata, the ACM double-column final layout and 12-page budget, ACM rights and CCS metadata, delivering any results promised in the rebuttal, coordinating the three artifact badges, registration, the ACM Open/APC step, the one-page public review, and the June in-person talk in Ho Chi Minh City.
---

# MobiSys Camera Ready

Use this after acceptance. Reopen the current camera-ready instructions, the ACM rights form,
the registration page, and the decision email before advising authors — dates and forms are
cycle-specific. MobiSys 2027 (re-verified 2026-11-24): camera-ready due **April 14, 2027**;
conference **June 21–25, 2027, Ho Chi Minh City, Vietnam**.

## Camera-ready audit

- Clear the **anonymous shepherd** first: every MobiSys 2027 acceptance is conditional, and the
  shepherd may request additional evaluation results, not only editorial changes.
- Finalize author metadata: the submission already carried names and affiliations (review is
  single-blind since 2026), so check spelling, order, ORCID and affiliations against HotCRP and
  the ACM rights form, and add acknowledgements, funding, and public code/data links.
- Apply the ACM double-column template and page budget. MobiSys 2027 caps submissions at a
  **12-page body including figures and tables**; references and appendices sit outside the cap
  — the final-version page allowance is 待核实, confirm it against the camera-ready instructions.
- Deliver every result **promised in the rebuttal**; a promised camera-ready experiment that
  never appears is a credibility failure the AC may notice.
- Complete ACM rights, the CCS concepts/keywords metadata, title/abstract/author-order
  metadata, and the bibliography.
- Coordinate the three artifact badges so passing badges are printed on the paper and recorded
  in the ACM DL (`mobisys-artifact-evaluation`).
- Settle the **APC**: authors whose institutions are not in ACM Open pay $500 (ACM/SIG members)
  or $750 (non-members) in 2027.
- Expect a **one-page public review** of the paper, written by a TPC member, to appear on the
  website and in the proceedings; pitch-video requirements are still to be announced.
- Confirm registration and the June in-person obligation: at least one author registers at a
  **non-student rate** and presents in person.

## What changes between the reviewed and final version

| Element | Reviewed (single-blind) | Camera-ready (ACM) |
|---|---|---|
| Author block | Present | Verified against HotCRP and ACM rights metadata |
| Acknowledgements / funding | Optional at review | Complete |
| Repository links | Review-time links | Public, licensed, archival (DOI) |
| Rebuttal promises / shepherd requests | Pending | Delivered in body/appendix |
| Metadata | Minimal | ACM rights + CCS concepts |

## Author-metadata sweep

- Verify the author block, acknowledgements, grants, and any contribution statements; the
  author list itself was frozen at the submission deadline.
- Replace review-time repository links with the public, licensed, archival artifact and test
  every link from a logged-out browser.
- Check screenshots and demo media for participant privacy and any vendor NDA on hardware
  details.

## ACM double-column reflow

- Switching the template from review to final mode changes spacing; recheck every page
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
  artifacts: badges coordinated, repo public and archival
  shepherd: sign-off received; APC settled or ACM Open confirmed
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
