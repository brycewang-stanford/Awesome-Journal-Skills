---
name: hri-camera-ready
description: Use when preparing the camera-ready of an accepted ACM/IEEE HRI paper — de-anonymizing systematically, completing ACM+IEEE dual-publication metadata (CCS concepts, ORCID, rights/eRights form), delivering every rebuttal promise within the 8-page budget, finalizing the video and de-anonymized archive, and passing production checks.
---

# HRI Camera-Ready

Acceptance is not the finish line — the camera-ready is where a double-blind paper becomes a
public, dual-published ACM+IEEE record, and where every promise you made in the rebuttal comes due.
HRI papers appear in **both the ACM Digital Library and IEEE Xplore**, so the metadata and rights
work is real. This skill runs the de-anonymization, the ACM metadata, the promised changes, and the
production checks. Timing for the HRI 2026 cycle: camera-ready ~9-12 Jan 2026 (**待核实** exact date;
see `resources/official-source-map.md`).

## De-anonymize systematically

Double-blind is over; reverse every anonymization deliberately, and do not miss one:

- **Author block** — real names, affiliations, and emails in the `acmart` author fields.
- **Self-citations** — convert third-person "prior work [X]" back to natural phrasing where
  appropriate; ensure your own cited work is complete.
- **Acknowledgments** — restore funding sources, grant numbers, and thanks.
- **Materials, code, and data archive** — swap the anonymized review archive for the **de-anonymized
  public archive** with a DOI (see `hri-artifact-evaluation`); update the link in the paper.
- **Video** — replace the review-only anonymized cut with the intended public version **only if
  participants consented** to public video; otherwise keep the de-identified cut and say so.

Then read the paper cold once more for any remaining "anonymized for review" placeholder.

## Deliver every rebuttal promise

Reviewers accepted the paper partly on what you promised. Within the **8-page** budget (incl.
figures, excl. references):

- Make each promised change — the reframed claim, the added analysis or effect size, the foregrounded
  Wizard-of-Oz disclosure, the added citation, the clarified figure.
- If the edition assigned a **shepherd / conditional acceptance**, make the required changes and get
  the shepherd's sign-off before submitting (**待核实** whether the cycle uses this).
- Do not quietly add new claims the reviewers never saw; camera-ready is for fulfilling promises and
  polishing, not re-scoping.

## ACM + IEEE metadata and rights

HRI's dual publication means both publishers' metadata must be right:

- **Rights / eRights form** — complete the ACM rights process; the resulting **rights block, DOI, and
  conference citation** must appear on the first page exactly as issued. Because papers also go to
  IEEE Xplore, follow any IEEE copyright/PDF-eXpress step the author kit specifies (**待核实** per
  cycle whether a separate IEEE step applies).
- **CCS concepts** — add the ACM Computing Classification System concepts for your paper.
- **Author keywords** — the index terms readers and search will use.
- **ORCID** — register/attach ORCIDs for authors as the metadata requires.
- **Title/author metadata** in the PDF must match the submission-system record exactly.

## Finalize the video and supplement

- Provide the **final video figure** at the required format/size (**待核实** limits per cycle), now
  with correct attribution if public use was consented.
- Ensure supplementary materials and the artifact archive are the final, de-anonymized versions and
  are referenced correctly from the paper (see `hri-supplementary`).

## Production checks

- **Compile clean** against the required `acmart` (and any IEEE) specification; fix every LaTeX/font
  warning that affects the PDF.
- **Embed all fonts**; verify figures are legible in grayscale and at print size.
- **Check the page count** — the body (incl. figures) must still fit **8 pages** after adding names,
  acknowledgments, and rights block; these additions often push a tight paper over.
- **Validate the PDF** against any portal checker (e.g., PDF eXpress if IEEE requires it) and re-open
  the final upload cold.
- **Verify links** — the DOI archive and any URLs resolve and point to the public, permanent versions.

## Common camera-ready failures

- Leftover **anonymization** (a "[anonymized]" acknowledgment, a review-only archive link).
- **Over length** after the author block, acknowledgments, and rights block are added.
- **Missing CCS concepts / ORCID / keywords** the metadata requires.
- **Rights block or DOI** absent or not matching the issued text.
- **Video** or archive still the anonymized review version, or an unconsented public video.
- A **rebuttal promise** silently dropped.

## Reverify each cycle

- The exact camera-ready date and whether a separate IEEE (Xplore/PDF-eXpress) step applies.
- The required `acmart` revision, CCS/ORCID/keyword fields, and video format limits.
- Whether shepherding/conditional acceptance applies to your paper.

## Output format

```text
[De-anonymization] authors/affiliations/acks/self-cites/archive/video all restored? leftover anon: <where>
[Rebuttal promises] each delivered within 8 pages? shepherd signed off (if any)?
[ACM+IEEE metadata] rights block + DOI · CCS concepts · keywords · ORCID · IEEE step (if req.)
[Video/supplement] final format · de-anonymized · consent-appropriate · referenced
[Production] clean compile · fonts embedded · page count ≤ 8 (body) · PDF checker passed
[Fix queue] <ordered, before the camera-ready deadline>
```
