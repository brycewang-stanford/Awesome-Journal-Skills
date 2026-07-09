---
name: atc-camera-ready
description: Use when preparing the ATC (ACM SIGOPS Annual Technical Conference, formerly USENIX ATC) camera-ready after a conditional accept — de-anonymizing systematically, folding in the shepherd's required revisions, permanentizing artifact links, completing ACM Open Access metadata and the transition APC, and passing production checks for the November Hong Kong proceedings.
---

# ATC Camera-Ready

Use this after a **conditional accept**. Final acceptance is gated by the **shepherd**, so the
camera-ready is not just formatting — it must **fold in every required revision** and pass the
shepherd's sign-off, then satisfy **ACM Open Access** production. ATC 2026 publishes in the **ACM
Digital Library** (a change from the old USENIX proceedings model), so the metadata and cost steps
are new relative to pre-2026 USENIX ATC.

## Satisfy the shepherd first

- Treat the shepherd's required-revisions list as **binding for acceptance**. Fold each change into
  the camera-ready and keep the description-of-changes (see `atc-author-response`) in sync with what
  actually landed.
- Do not use the de-anonymization pass to quietly re-expand scope; the shepherd is checking that the
  paper the PC accepted is the paper being published.
- Get explicit shepherd sign-off before treating the paper as final.

## Systematic de-anonymization

The submission was double-blind; the camera-ready is not. Reverse every anonymization deliberately:

```text
[Authors]     add the author list, affiliations, and ORCIDs
[Self-cites]  restore first-person references where accurate ("our earlier system X [12]")
[System name] restore the real system/product name if you used a neutral placeholder
[Artifact]    swap anonymized/blind-mirror links for the public, DOI-issuing archive
[Acks]        add acknowledgments and funding/grant lines held out for blind review
[Metadata]    set real PDF author/title metadata (it was scrubbed for submission)
```

Cross-check: search the final PDF for leftover placeholders ("Anonymous," "System-X-anon," blind
URLs) — a stray one is the classic camera-ready miss.

## Format and production

- Keep the **two-column** format (178 × 229 mm text block, 10pt) and the page budget; the
  camera-ready may allow the same or a slightly extended limit — **confirm the exact camera-ready
  page allowance on the call** (待核实).
- Which template file the SIGOPS edition mandates (the USENIX template vs. ACM `acmart`/equivalent)
  is **待核实** — verify before recompiling, since ACM production checks depend on it.
- Embed all fonts, check figure resolution and color-blind legibility, and confirm the PDF passes
  the venue's automated production/format checker.

## ACM Open Access metadata and cost

ATC 2026 papers publish under **ACM Open Access**:

- Complete the **ACM rights/e-rights form**, author and affiliation metadata, ACM CCS concepts,
  keywords, and the abstract as it will index in the ACM DL.
- Budget for the **transition APC** — subsidized for 2026 (reported around US$250 for ACM/SIG
  members and US$350 for non-members); confirm the current figure, member split, and any waiver on
  the ACM/SIGOPS terms.
- Ensure the **artifact links are permanent** (DOI-issuing archive), since the published paper cites
  them and the AEC badges attach to this version (see `atc-artifact-evaluation`).

## Presentation and legacy-media note

USENIX ATC historically posted **free proceedings, slides, and talk videos**; under ACM Open Access
the proceedings are openly available via the ACM DL, and the conference is in **Hong Kong, 15-18
November 2026**. Confirm the current slides/video policy and the presenter requirement (at least one
author presents) on the venue page.

## Pre-submission checklist

```text
[Shepherd]    all required revisions folded in and signed off? yes/no
[De-anon]     authors, affiliations, self-cites, system name, acks, artifact links restored?
[Leftovers]   no "Anonymous"/blind-URL/placeholder strings in the final PDF?
[Format]      two-column template, page allowance, embedded fonts, production checker passed?
[ACM OA]      rights form, metadata, CCS/keywords complete? APC handled?
[Artifact]    permanent DOI link cited; badges attached to this version?
```

## Output format

```text
[Camera-ready status] ready / blocked on shepherd / blocked on production
[Shepherd] required revisions folded + signed off? yes/no
[De-anonymization] complete and leftover-free? gaps: <where>
[ACM Open Access] rights form, metadata, APC done? artifact DOI permanent?
[Fix queue] <ordered, with the camera-ready deadline>
```
