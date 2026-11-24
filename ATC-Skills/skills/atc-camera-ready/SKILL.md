---
name: atc-camera-ready
description: Use when preparing the ATC (ACM SIGOPS Annual Technical Conference, formerly USENIX ATC) camera-ready after a conditional accept — de-anonymizing systematically, folding in the shepherd's required revisions, permanentizing artifact links, completing ACM Open Access metadata and any APC, and passing production checks by the 28 May 2027 camera-ready deadline for the Rennes proceedings.
---

# ATC Camera-Ready

Use this after a **conditional accept**. Final acceptance is gated by the **shepherd**, so the
camera-ready is not just formatting — it must **fold in every required revision** and pass the
shepherd's sign-off, then satisfy **ACM Open Access** production. For ATC 2027 (call re-verified
2026-11-24) notifications go out **27 April 2027** and camera-ready papers are due **28 May 2027**.
The SIGOPS editions publish in the **ACM Digital Library** (a change from the retired USENIX ATC
proceedings model), so the metadata and cost steps are new relative to USENIX ATC.

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

- Keep the **two-column** format (178 × 229 mm text block, 10pt) built with the ACM SIGPLAN
  template the call recommends (`\documentclass[sigplan,10pt]{acmart}`); switch off the
  submission-time tweaks (suppressed copyright block, anonymous mode) as the ACM author kit directs.
- The camera-ready page allowance is not stated on the 2027 call — **confirm it in the acceptance
  instructions** (待核实). Remember the submission limit counted appendices.
- Embed all fonts, check figure resolution and color-blind legibility, and confirm the PDF passes
  the venue's automated production/format checker.

## ACM Open Access metadata and cost

ATC papers publish under **ACM Open Access** (ACM went fully open access on 1 January 2026):

- Complete the **ACM rights/e-rights form**, author and affiliation metadata, ACM CCS concepts,
  keywords, and the abstract as it will index in the ACM DL.
- Check whether an **APC** applies: none if your institution is in **ACM Open**, otherwise an APC
  unless you qualify for a (rare) waiver. The ATC 2027 call quotes no rate; ACM's subsidized 2027
  rates as stated on other ACM-sponsored 2027 calls are **$500** (ACM/SIG members) and **$750**
  (non-members). (Figures of about US$250 / US$350 for 2026 circulated in secondary renderings and
  were never confirmed on an official page — do not quote them.)
- Ensure the **artifact links are permanent** (DOI-issuing archive), since the published paper cites
  them and the AEC badges attach to this version (see `atc-artifact-evaluation`).

## Presentation and legacy-media note

USENIX ATC historically posted **free proceedings, slides, and talk videos**; under ACM Open Access
the proceedings are openly available via the ACM DL, all accepted papers go online before the
conference, and ATC 2027 meets in **Rennes, France, 28 June – 1 July 2027**. Every accepted paper is
presented **orally and/or as a poster** (not all get an oral slot), and **one author must attend**.
Papers of particular merit are forwarded to **ACM TOCS** and **CACM Research Highlights**.

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
