---
name: icdm-camera-ready
description: Use when preparing the ICDM (IEEE International Conference on Data Mining) camera-ready after acceptance - IEEE final formatting and eCopyright, de-anonymizing a triple-blind paper, handling a Regular/Short designation (both ten pages in 2026), registering for in-person presentation, and getting the paper into IEEE Xplore.
---

# ICDM Camera-Ready

Turn an accepted ICDM paper into the published IEEE version. Three things make ICDM's
camera-ready distinctive: you **de-anonymize** a paper written triple-blind, you check whether
the Regular/Short designation changes the page limit, and publication runs through **IEEE**
(PDF eXpress, copyright, IEEE Xplore) with a mandatory in-person presentation and a poster. In
ICDM 2026 the camera-ready was due **September 9, 2026** (AoE; the Applied Track call said
September 16), at **most 10 pages including references and appendices** for every accepted
paper (re-verified 2026-11-24). Verify every deadline on the current call.

## De-anonymize deliberately

The triple-blind submission hid your identity everywhere; camera-ready is where it comes back.

- Restore author names, affiliations, and ORCIDs in the IEEE author block.
- Restore acknowledgements and funding/grant numbers.
- Rewrite third-person self-citations to first person where natural ("we previously showed").
- De-anonymize the cited repository: point it at the real, named project and add the README
  acknowledgements you stripped for review.

## Handle a Short designation

In ICDM 2026 papers were designated Regular or Short after acceptance "with limits of ten pages",
and the camera-ready instructions capped every paper at 10 pages — so a Short designation did
**not** force compression. Earlier editions did shorten short papers; if the current call gives
Short papers fewer pages, the camera-ready becomes a compression job, not a formatting job:

| Keep in the short body | Move to the repository / cut |
|---|---|
| The named mechanism and its statement | Full proofs, extended derivations |
| The single strongest experiment | Secondary experiments and extra datasets |
| The core discovery-validity argument | Long protocol detail, ablation appendices |
| A pruned related-work contrast | Padding, background everyone knows |

Use the compression map you prepared during `icdm-supplementary`; the mechanism must survive at
short length, with overflow cited in the (now de-anonymized) repository.

## IEEE production steps

```text
Camera-ready checklist (verify order/deadlines on the current call):
  1. Recompile in the IEEE two-column template WITHOUT the anonymous/review options.
  2. Fit the final page limit (10 pages all-inclusive for Regular and Short in 2026).
  3. Run IEEE PDF eXpress (2026 Conference ID 70242X) via the ICDM author kit.
  4. Complete the IEEE copyright transfer in the author kit.
  5. Add author block, acknowledgements, funding, ORCIDs, de-anonymized repo link.
  6. Register at least one author for in-person presentation (required to appear).
  7. Upload by the camera-ready deadline; confirm the Xplore-bound final PDF.
  8. Submit the e-poster (required for every accepted paper; 2026 deadline October 12).
```

## Presentation and publication

- At least one author must register and **present in person** for the paper to be included in
  the proceedings and program; in 2026, authors unable to attend joined a designated online
  session with a recorded presentation as backup. Every accepted paper also presents a poster
  (printed by the conference in 2026).
- Accepted papers are published by IEEE and indexed on **IEEE Xplore** and dblp; the camera-ready
  is the version of record, so proofread it as final.

## Vignette: a de-anonymization that leaked the wrong way

A team rushed camera-ready and left one figure's caption reading "results from the anonymized
system," while restoring author names in the header — an inconsistent half-de-anonymization that
looked careless in the published record. The fix is a single pass: sweep every "anonymous,"
"our system (name withheld)," and third-person self-citation, restore the real names and the real
repository link, then recompile without the review options and re-read the whole PDF once as the
permanent Xplore version.

## Output format

```text
[Outcome] Accept, designated Regular / Short
[De-anonymized] names / acks / funding / self-cites / repo link: complete / gaps
[Length] within the current limit (10 pages all-inclusive in 2026): pass / over
[IEEE steps] template / eCopyright / PDF check / registration: done / pending
[Presentation] in-person author registered: yes / no
[Final read] whole PDF proofed as the Xplore version of record: yes / no
```
