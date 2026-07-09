---
name: ase-camera-ready
description: Use when preparing the ASE (IEEE/ACM Automated Software Engineering) camera-ready after acceptance or a successful revision, covering systematic de-anonymization, the extra content page, the mandatory Data Availability finalization, the correct IEEE/ACM template and metadata, permanentized artifact links, and dual IEEE-Xplore/ACM-DL production checks.
---

# ASE Camera-Ready

Deliver the final version after an Accept or a met Revision. ASE camera-ready has three jobs that
trip authors up: **de-anonymize systematically**, **spend the extra content page well**, and pass
**dual production checks** — because the paper is indexed in **both IEEE Xplore and the ACM Digital
Library**, the metadata and template must satisfy the sponsoring publisher's pipeline. Every
requirement below is a one-cycle snapshot; reopen the current camera-ready instructions first.

## Systematic de-anonymization

Reverse every anonymization introduced for double-anonymous review — and only those:

```text
[Authors]      real names, affiliations, ORCID, and corresponding-author info restored.
[Tool]         real tool name restored consistently throughout (it was anonymized at submission).
[Repository]   Data Availability link points to the real, permanent archive (not the anon service).
[Self-cites]   third-person self-citations relaxed to normal form where appropriate.
[Acks]         funding, grants, and collaborators added (absent from the anonymized submission).
[Metadata]     PDF author/producer fields set correctly; no residual "Anonymous".
```

Do a final `pdfinfo` / `pdftotext` pass to confirm no leftover "Anonymous" and no *new* leak (a
funding line that should not be there, a wrong affiliation).

## Spend the extra content page

Accepted ASE papers are typically allowed **one additional content page** for revisions. Use it to
**incorporate review feedback** — the new baseline, the requested ablation, the clarified construct,
the strengthened threats — not to pad. If you received a Revision, the extra page is where the
criteria you met become visible in the final paper.

## Finalize the Data Availability Statement

- The statement moves from an **anonymized** link to the **permanent, DOI-archived** location.
- Confirm the archive is public and the DOI resolves; deposit in Zenodo / figshare / Software
  Heritage before submitting camera-ready if you have not already.
- Keep it after the Conclusions and within the (now +1) page budget.

## Template and metadata (IEEE/ACM dual)

- Use the **mandated camera-ready template** — for ASE 2026 the ACM `acmart` (switch out the
  `review`/`anonymous` options for the final class options the instructions specify). Because ASE is
  dual IEEE/ACM sponsored, the required template and the rights/metadata step can differ per
  edition; **confirm which publisher's pipeline this edition uses** and follow that kit.
- Complete the **rights/copyright** step (the e-rights form) and paste the correct rights block into
  the paper.
- Fill **indexing metadata** (title, authors, abstract, CCS concepts / keywords) accurately — this
  feeds both IEEE Xplore and the ACM DL records; mismatches cause production delays.
- Embed all fonts; check figures render and that the PDF passes the publisher's automated checker
  (e.g., an IEEE PDF eXpress-style or ACM validation step, per the edition's instructions).

## If your paper earned an artifact badge

- Ensure the **badge** is reflected per the instructions so it appears on the front page in both
  proceedings surfaces (see `ase-artifact-evaluation`).
- The badged artifact's DOI should match the Data Availability Statement.

## Camera-ready checklist

```text
[De-anon]     authors/affiliations/tool/repo/acks restored; no leftover "Anonymous"; no new leak
[Extra page]  review feedback incorporated (not padding); met revision criteria visible
[Data Avail]  permanent DOI archive, resolves, after Conclusions, within budget
[Template]    correct edition template/class options; rights block pasted
[Metadata]    title/authors/abstract/keywords/CCS accurate for IEEE Xplore + ACM DL
[Production]  fonts embedded; figures render; passes the publisher's PDF checker
[Badge]       artifact badge reflected if earned; DOI matches Data Availability
```

## Output format

```text
[Camera-ready status] ready / blocked
[De-anonymization] complete? residual "Anonymous" or new leak?
[Extra page] feedback incorporated / revision criteria visible?
[Data Availability] permanent DOI resolves, within budget?
[Template + rights] correct template, rights block, accurate metadata for both proceedings?
[Fix queue] <ordered, before the camera-ready deadline>
```
