---
name: cell-submission
description: Use as the final preflight before submitting to Cell — a complete checklist across significance, narrative, Highlights/eTOC/Graphical Abstract, Summary, figures, STAR Methods, data, references, and required files. Bundles the checklist and cover-letter templates.
---

# Submission Preflight & Cover Letter (cell-submission)

## When to trigger

- The manuscript is "done" and you're about to upload to Editorial Manager.
- You want a single gate confirming every other cell-* skill's output landed.
- A revision is going back and you need to confirm nothing regressed.

## Master preflight checklist

### Significance & narrative
- [ ] Clears the complete-mechanistic-story bar (`cell-fit` rung ≥ 4, multiple converging lines).
- [ ] Single narrative arc (hypothesis → mechanism → significance); no parallel mini-stories.
- [ ] Title is declarative, names the actor + effect.

### Cell signature artifacts
- [ ] **Highlights**: 3–4 bullets, each ≤ 85 characters incl. spaces.
- [ ] **eTOC / In Brief blurb**: ~50 words, third person, lay language.
- [ ] **Graphical Abstract**: single panel, clear flow, minimal text, RGB, correct size.

### Summary & writing
- [ ] **Summary**: single paragraph ≤ ~150 words, mechanism named, ≥1 quantified result, no citations.
- [ ] Main text ~45,000 characters (incl. legends); display items within ~7–8.
- [ ] Results have claim-style subheadings; Discussion is interpretive, not a recap.

### Figures & display items
- [ ] Sized to 85 / 114 / 174 mm; min font ~6–7 pt; RGB.
- [ ] Data shown (points + n + replicate type); error bars defined; scale bars present.
- [ ] Colorblind-safe; legends stand alone (title + per-panel + statistics).
- [ ] Image integrity: uncropped key blots in supplement; source data retained.

### STAR Methods
- [ ] **Key Resources Table** complete (antibodies w/ Cat#+RRID; deposited data w/ accession; software w/ version).
- [ ] **Resource Availability** has all three subsections: Lead Contact / Materials Availability / Data and Code Availability.
- [ ] Experimental Model and Subject Details incl. ethics (IRB/IACUC, consent, authentication).
- [ ] Method Details reproducible; **Quantification and Statistical Analysis** consolidated.

### Data & code
- [ ] Data deposited; accession numbers/DOIs in hand; mirrored into KRT "Deposited Data."
- [ ] Code public + archived (Zenodo/Mendeley DOI).
- [ ] Three-bullet Data and Code Availability statement complete (data / code / additional).

### References
- [ ] Cell Press **author–date** in text; **alphabetical** reference list; full author lists.
- [ ] Every in-text "(Author, year)" resolves; a/b suffixes for same author/year.

### Required files & metadata
- [ ] Main text (Summary, Intro, Results, Discussion, STAR Methods, legends, references).
- [ ] Figures at required resolution + legends; Graphical Abstract file.
- [ ] Highlights and eTOC blurb files/fields.
- [ ] Supplemental Information (figures/tables/videos + captions).
- [ ] Cover letter (conceptual-advance + completeness forward).
- [ ] Authors, affiliations, ORCIDs, corresponding author, **Lead Contact**.
- [ ] CRediT author contributions; competing interests; funding.
- [ ] Suggested / opposed reviewers (if used).

## Final integrity sweep
- [ ] No over-claiming beyond the evidence (re-read Summary + Discussion).
- [ ] Every figure's n, replicate type, error bar, and test defined and consistent with QSA.
- [ ] All accession numbers/DOIs live and correct.
- [ ] Single-blind by default — do not anonymize unless double-blind requested. Confirm.

## What the desk editor is deciding

Submission goes through Cell Press Editorial Manager to an in-house scientific editor who makes the review-or-reject call before any referee sees the file. Two things they cannot recover later must be right at upload: the *conceptual advance* (does this reframe how the field thinks, not just add a data point) and the *completeness* (are the converging lines already in the manuscript, not promised in a rebuttal). The cover letter exists to state both in the editor's own vocabulary. Everything else in the preflight is hygiene; these two are the gate.

Do not open the cover letter with "Please find enclosed our manuscript." Open with the advance. A serviceable first sentence: *"We report that [actor] [mechanism], resolving the long-standing question of [gap] and establishing [principle] as a [broad consequence]."* Then one short paragraph naming the converging lines of evidence (genetics + biochemistry + in vivo, say), one sentence on why Cell's broad readership specifically, and — if relevant — a candid line on any concurrent related work so the editor is not surprised. Keep it to a page.

## Revision-specific gate

When a revised manuscript goes back, run the checklist again but add: every promised experiment from the response letter is now *in* the paper or explicitly justified as out of scope; every referee-driven change is reflected in both the text and the figures (a common regression is updating a panel but not its legend or the Quantification and Statistical Analysis block); the response letter and the manuscript agree on every number; and no new claim crept in during revision without new evidence. Version the figures so an old panel cannot ship by accident.

## Metadata traps specific to Cell Press

- The **Lead Contact** is a distinct required role from the corresponding author and must match the Resource Availability statement in STAR Methods exactly — a frequent mismatch.
- Cell uses **single-blind** review by default; do not strip author identity from the manuscript unless double-blind was explicitly requested, and confirm the current option on the portal.
- CRediT contributions, competing-interests, and funding statements must be present as structured fields, not only prose.
- Accession numbers and the Zenodo/Mendeley code DOI must appear identically in the KRT "Deposited Data" rows, the Data and Code Availability statement, and any Editorial Manager metadata field.

## Templates
- `templates/checklist.md` — copyable preflight checklist.
- `templates/cover_letter_template.md` — conceptual-advance cover-letter scaffold.

## Output format

```
【Blocking gaps】 [...]  (must fix before upload)
【Warnings】 [...]       (should fix)
【Files ready】 main / figures+legends / GA / Highlights+eTOC / SI / cover letter / metadata
【Verdict】 GO / NO-GO + the top 3 fixes
【Next】 submit | cell-rebuttal (after decision)
```

## Anti-patterns

- **Do not** upload before accession numbers/DOIs exist.
- **Do not** ship Highlights over 85 characters or an eTOC blurb in the first person.
- **Do not** submit a free-text Methods section instead of STAR Methods.
- **Do not** rely on memory; run the checklist top to bottom.

> Confirm all caps and required files against current Cell Press author guidelines before upload.
