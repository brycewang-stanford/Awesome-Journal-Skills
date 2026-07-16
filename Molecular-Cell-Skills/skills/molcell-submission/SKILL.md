---
name: molcell-submission
description: Use as the final preflight before submitting to Molecular Cell — a complete checklist across mechanism, single-mechanism arc, length budget, figures, STAR Methods, data deposition, numbered references, front-matter artifacts, and required files. Bundles the checklist and cover-letter templates.
---

# Submission Preflight & Cover Letter (molcell-submission)

## When to trigger

- The manuscript is "done" and you're about to upload to Editorial Manager.
- You want a single gate confirming every other molcell-* skill's output landed.
- A revision is going back and you need to confirm nothing regressed.

## Master preflight checklist

### Mechanism & narrative
- [ ] Clears the deep-mechanism bar (`molcell-fit` rung ≥ 3; orthogonal validation; physiological relevance).
- [ ] Single-mechanism arc (question → mechanism → physiological consequence); no technique catalog.
- [ ] Separation-of-function / point-mutant evidence ties the mechanism to the phenotype.
- [ ] Title is declarative, names the molecular actor + molecular action.

### Length & structure
- [ ] Main text ~7,000 words incl. main figure legends (or ~4,000 for a Short Article); confirm live cap.
- [ ] Display items within ~7; extras in Supplemental Information.
- [ ] Results have molecular-claim subheadings; Discussion interpretive (model + excluded alternative), not a recap.

### Front-matter artifacts
- [ ] **Highlights**: 3–4 bullets, each ≤ 85 characters incl. spaces.
- [ ] **eTOC / In Brief blurb**: ~50 words, third person, accessible language.
- [ ] **Graphical Abstract**: single panel, clear flow, minimal text, RGB, correct size.
- [ ] **Summary**: single paragraph (~150 words), mechanism named, ≥1 quantified result, no citations.

### Figures & display items
- [ ] Sized to 85 / 114 / 174 mm; min font ~6–7 pt; RGB.
- [ ] Data shown (points + n + replicate type); error bars defined; primary data (gels/traces/maps) shown.
- [ ] Blot integrity: uncropped key blots in supplement; source scans retained; splices disclosed.
- [ ] Structures: resolution/FSC/refinement reported; contacts supported by density.
- [ ] Genomics: normalization + replicate metric stated; colorblind-safe throughout.

### STAR Methods
- [ ] **Key Resources Table** complete (antibodies w/ Cat#+RRID; plasmids/oligos/purified proteins; deposited data w/ accession; software w/ version).
- [ ] **Resource Availability**: Lead Contact / Materials Availability / Data and Code Availability.
- [ ] Experimental Model and Subject Details incl. ethics (IRB/IACUC, consent, authentication, mycoplasma).
- [ ] Method Details reproducible (purification/reconstitution/pipelines); **Quantification and Statistical Analysis** consolidated.

### Data & code
- [ ] Data deposited (GEO/PDB+EMDB/PRIDE); accession numbers/DOIs in hand; mirrored into KRT "Deposited Data."
- [ ] Structures deposited with maps/structure factors; code public + archived (Zenodo/Mendeley DOI).
- [ ] Data and Code Availability statement complete (data / code / additional).

### References
- [ ] Cell Press **numbered** superscript in text, in order of first appearance.
- [ ] Reference list numbered by appearance; full author lists; abbreviated journal names.
- [ ] Every superscript resolves to one entry; no uncited entries; single merged list incl. STAR Methods.

### Required files & metadata
- [ ] Main text (Summary, Intro, Results, Discussion, STAR Methods, legends, references).
- [ ] Figures at required resolution + legends; Graphical Abstract file.
- [ ] Highlights and eTOC blurb files/fields.
- [ ] Supplemental Information (figures/tables/videos + captions).
- [ ] Cover letter (mechanistic-advance forward).
- [ ] Authors, affiliations, ORCIDs, corresponding author, **Lead Contact**.
- [ ] CRediT author contributions; competing interests; funding.
- [ ] Suggested / opposed reviewers (if used).

## Final integrity sweep
- [ ] No over-interpretation beyond the evidence (re-read Summary + Discussion + structure claims).
- [ ] Every figure's n, replicate type, error bar, and test defined and consistent with QSA.
- [ ] All accession numbers/DOIs live and correct; structure map-model fit matches the deposited entry.
- [ ] Single-blind by default — do not anonymize unless double-blind requested. Confirm on the portal.

## What the desk editor is deciding

Submission goes through Cell Press Editorial Manager to an in-house scientific editor who makes the review-or-reject call before any referee sees the file. Two things they cannot recover later must be right at upload: the *mechanistic depth* (is the molecular event proven, or only proposed) and the *orthogonal validation* (are the independent lines already in the manuscript, not promised in a rebuttal). The cover letter exists to state both in the editor's vocabulary. Everything else in the preflight is hygiene; these two are the gate.

Do not open the cover letter with "Please find enclosed our manuscript." Open with the mechanism. A serviceable first sentence: *"We show that [molecular actor] [molecular action] by [mechanistic detail], resolving how [process] is controlled and why [physiological outcome] depends on it."* Then one short paragraph naming the orthogonal lines of evidence (e.g., structure + reconstitution + separation-of-function genetics), one sentence on why Molecular Cell's mechanism-focused readership specifically, and — if relevant — a candid line on concurrent related work. Keep it to a page.

## Revision-specific gate

When a revised manuscript goes back, run the checklist again but add: every promised experiment from the response letter is now *in* the paper or explicitly justified as out of scope; every referee-driven change is reflected in both text and figures (a common regression is updating a panel but not its legend or the QSA block); the response letter and the manuscript agree on every number; no new mechanistic claim crept in without new evidence; and any re-processed structure/genomics matches the deposited entry. Version figures so an old panel cannot ship by accident.

## Metadata traps specific to Cell Press
- The **Lead Contact** is a distinct required role from the corresponding author and must match the Resource Availability statement exactly.
- Molecular Cell uses **single-blind** review by default; do not strip author identity unless double-blind was explicitly requested — confirm the current option on the portal.
- CRediT contributions, competing-interests, and funding statements must be structured fields, not only prose.
- Accession numbers and the Zenodo/Mendeley code DOI must appear identically in the KRT "Deposited Data" rows, the Data and Code Availability statement, and any Editorial Manager metadata field.

## Templates
- `templates/checklist.md` — copyable preflight checklist.
- `templates/manuscript_template.md` — Molecular Cell manuscript skeleton (STAR Methods, KRT, eTOC blurb, Highlights, cover-letter scaffold).

## Output format

```
【Blocking gaps】 [...]  (must fix before upload)
【Warnings】 [...]       (should fix)
【Files ready】 main / figures+legends / GA / Highlights+eTOC / SI / cover letter / metadata
【Verdict】 GO / NO-GO + the top 3 fixes
【Next】 submit | molcell-rebuttal (after decision)
```

## Anti-patterns

- **Do not** upload before accession numbers/DOIs (and deposited structures) exist.
- **Do not** ship Highlights over 85 characters or an eTOC blurb in the first person.
- **Do not** submit a free-text Methods section instead of STAR Methods.
- **Do not** leave author–date citations unconverted — Molecular Cell is numbered.
- **Do not** rely on memory; run the checklist top to bottom.

> Confirm all caps and required files against the current Molecular Cell information-for-authors page before upload.
