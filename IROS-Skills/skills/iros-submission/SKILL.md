---
name: iros-submission
description: Use when auditing an IROS paper for the PaperPlaza upload — author PINs and metadata, the content-page limit with references counted in, IEEE two-column format, the 2026 double-anonymous rule, the 60-second/10 MB video attachment and its own deadline, dual-submission traps shared with ICRA and RA-L, and return-without-review triggers.
---

# IROS Submission

Final-gate audit for an IROS conference submission on PaperPlaza (`ras.papercept.net`), the shared RAS
system that also runs ICRA, CASE, and RA-L. Everything here is anchored to the verified IROS 2026 cycle;
the numbers move each edition because a new IEEE/RSJ committee resets them, so open the current
year-site's call-for-papers page before trusting any value below.

## Hard limits (2026-cycle values — reverify each year)

| Check | 2026 rule | Consequence if violated |
|---|---|---|
| Page count | Content-page limit with references and appendices counted *in* (2025 anchor: 6 + up to 2 paid) | Return without review or an unexpected page charge |
| Format | IEEE two-column conference template, PDF only, file up to 6 MB | Compliance failure at upload |
| Anonymity | Double-anonymous (2026): no authors/affiliations in the PDF; full list in PaperPlaza metadata | Administrative rejection |
| Video attachment | ≤ 60 seconds, ≤ 10 MB, mpg/mpeg/mp4 | Rejected by the upload form |
| Video deadline | Its own date, a few days after the paper (2026: March 5) | No video on record |
| Paper deadline | Per the CFP's stated zone — convert, do not assume AoE | Closed portal |

The tighter video envelope is an IROS signature: where ICRA allows 180 seconds and 20 MB, IROS 2026
allows only 60 seconds and 10 MB, so a video cut for ICRA must be re-edited, not just re-uploaded.

## The references-count-inside trap

IROS counts references (and any appendix) *within* the page budget. Authors arriving from ML venues
that advertise "N pages excluding references" routinely overrun. There is no separate supplementary PDF
either — so an argument that does not fit the body does not get an appendix to escape into. Budget the
bibliography as content from the first outline, not as free space.

## The 2026 anonymity posture

IROS carried a long single-blind tradition, but the 2026 cycle presents as double-anonymous. Concretely:

- Strip the author block, affiliations, and identifying acknowledgements/grant numbers from the PDF;
  keep the final author list in PaperPlaza metadata (treat it as binding, not a placeholder).
- Rewrite platform tells: "our previously built XYZ rover [9]" becomes "the XYZ rover [9]" cited in the
  third person.
- De-identify figures **and the video**: institute banners, lab door signs, logo'd safety vests, and
  building-specific scenery are all leaks.
- Anonymize links: a code URL carrying a lab organization name is an identity leak; use an anonymized
  mirror or omit it at review time.
- Because the policy departs from IROS habit, confirm it still holds for your target year before you
  de-anonymize or re-anonymize anything.

## PaperPlaza mechanics worth knowing early

- Every co-author needs a PaperPlaza PIN tied to a profile; gathering PINs from a large author list on
  deadline night is a known time sink — do it the week the site opens.
- The portal runs its own PDF compliance test (embedded fonts, page size, page count); a failing PDF can
  be re-uploaded until the deadline, so test days early, not hours early.
- Keywords come from a fixed RAS taxonomy and steer which Associate Editor and reviewer pool see the
  paper; pick the two or three closest, not the broadest.
- The confirmation email is the only receipt — archive it.

## Dual-submission and the RA-L boundary

The same manuscript may not be under review at IROS and elsewhere at once. Note the current-cycle shape:

- IROS 2026 has **no combined RA-L+IROS submission option**; do not try to submit "to both."
- The legitimate journal-to-conference route is a **published** RA-L (or T-RO, T-ASE, RAM) paper
  transferred for presentation during an eligibility window — a different mechanism from submitting.
- A preprint on arXiv is generally allowed; confirm the exact wording in the current CFP.

## Pre-upload sequence (final 48 hours)

```text
1. Rebuild the PDF from a clean clone; confirm the IEEE class file is untouched.
2. Page audit: content + references + appendix all fit the current budget; note any page charge.
3. Anonymity sweep: pdfinfo metadata, acknowledgements, self-citations, figure backgrounds,
   embedded links, and every video frame and caption.
4. Play the 60 s video end to end on a machine without lab codecs; verify duration, size, format.
5. Verify PaperPlaza metadata: authors + PINs, keywords, abstract synced to the PDF.
6. Upload paper and video; pass the compliance check; archive the confirmation email.
```

## Output format

```text
[IROS upload verdict] go / fix-first / no-go
[Page audit] content+refs <n>/<limit>, page charge? <y/n>
[Anonymity audit] pass / leaks: <list>
[Video audit] <s>s / <MB>MB / format / deadline ok?
[Metadata audit] PINs collected? keywords chosen? abstract synced?
[Dual-submission] clear / conflict: <venue>
[Deadline math] <local time> vs <CFP zone> = <hours remaining>
```
