---
name: icdm-camera-ready
description: Use when preparing the ICDM (IEEE International Conference on Data Mining) camera-ready after acceptance - IEEE final formatting and eCopyright, de-anonymizing a triple-blind paper, handling an Accept-as-Short outcome by compressing to short-paper length, registering for in-person presentation, and getting the paper into IEEE Xplore.
---

# ICDM Camera-Ready

Turn an accepted ICDM paper into the published IEEE version. Three things make ICDM's
camera-ready distinctive: you **de-anonymize** a paper written triple-blind, you may need to
**compress to short-paper length** if the outcome was Accept-as-Short, and publication runs
through **IEEE** (eCopyright, IEEE Xplore) with a mandatory in-person presentation. Verify every
deadline and the exact short-paper page length on the current call — these are 待核实.

## De-anonymize deliberately

The triple-blind submission hid your identity everywhere; camera-ready is where it comes back.

- Restore author names, affiliations, and ORCIDs in the IEEE author block.
- Restore acknowledgements and funding/grant numbers.
- Rewrite third-person self-citations to first person where natural ("we previously showed").
- De-anonymize the cited repository: point it at the real, named project and add the README
  acknowledgements you stripped for review.

## Handle Accept-as-Short

If the notification said "accepted as a short paper," the camera-ready is a compression job, not
a formatting job:

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
  2. Fit the final page limit (regular vs short; short length is 待核实).
  3. Run the IEEE PDF validation/eXpress check if required for the proceedings.
  4. Complete IEEE eCopyright / electronic copyright transfer.
  5. Add author block, acknowledgements, funding, ORCIDs, de-anonymized repo link.
  6. Register at least one author for in-person presentation (required to appear).
  7. Upload by the camera-ready deadline; confirm the Xplore-bound final PDF.
```

## Presentation and publication

- At least one author must register and **present in person** in Shenyang for the paper to be
  included in the proceedings and program.
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
[Outcome] Accept (regular) / Accept-as-Short
[De-anonymized] names / acks / funding / self-cites / repo link: complete / gaps
[Length] within regular or short page limit (short = 待核实): pass / over
[IEEE steps] template / eCopyright / PDF check / registration: done / pending
[Presentation] in-person author registered: yes / no
[Final read] whole PDF proofed as the Xplore version of record: yes / no
```
