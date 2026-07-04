---
name: pnas-submission
description: Use as the final preflight before submitting to PNAS — a complete checklist across significance, track, Significance Statement, abstract, classification + keywords, figures, statistics, data, references, and required files. Bundles a checklist and a PNAS cover-letter template. Emits GO/NO-GO.
---

# Submission Preflight (pnas-submission)

## When to trigger

- The manuscript is "done" and you're about to upload.
- You want a single gate that confirms every other pnas-* skill's output landed.
- A revision is going back and you need to confirm nothing regressed.

## Master preflight checklist

### Significance & venue
- [ ] Clears the broad-significance / high-quality bar (`pnas-fit` rung ≥ 2–3, cross-division reader passes).
- [ ] PNAS is the right venue (not better at a field journal or Science/Nature).
- [ ] Title is declarative, specific, parseable by a non-specialist.

### Submission track
- [ ] Track chosen: ☐ Direct ☐ Contributed (NAS member) (`pnas-track`).
- [ ] If Contributed: member within annual quota; ≥2 independent reviewers secured; reviews + author responses ready to submit.
- [ ] If Direct: suggested editors/reviewers prepared for the cover letter.

### Significance Statement & abstract
- [ ] Significance Statement ≤ 120 words, for a non-specialist, distinct from the abstract.
- [ ] Abstract ≤ ~250 words, single paragraph, no subheadings/citations, ≥1 quantified result.

### Structure, classification & length
- [ ] PNAS order: Title / authors / Significance / Abstract / Intro / Results / Discussion / **Materials and Methods (in-text)** / refs.
- [ ] Classification chosen: major division (Biological / Physical / Social Sciences) + minor subject area.
- [ ] Keywords provided (≤ ~5).
- [ ] Package within length/page budget; extended material in SI Appendix.

### Figures & display items
- [ ] Within page/item allowance; sized to 9 / 11.4 / 18 cm; fonts ≥ ~6–8 pt.
- [ ] Data shown (points + n); error bars defined; scale bars present.
- [ ] Colorblind-safe; RGB/CMYK handled; uncropped key blots + source data retained.

### Statistics & reproducibility
- [ ] Each claim: effect size + CI + n + test + assumptions.
- [ ] Biological vs technical replication clear; sample-size rationale stated.
- [ ] Randomization/blinding reported or justified; multiplicity controlled.
- [ ] Analysis code public + archived (DOI).

### Data, materials, ethics
- [ ] Data deposited with accession numbers/DOIs (no "on request" for primary data).
- [ ] Data Availability Statement drafted and compliant.
- [ ] Materials/reagent sharing plan; ethics approvals (IRB/IACUC/permits) as needed.

### References
- [ ] PNAS numbered style, ordered by appearance, single numbered list.
- [ ] Full author lists; journal abbreviations; all in-text numbers resolve.

### Required files & metadata
- [ ] Main text (title, Significance Statement, abstract, body, Materials and Methods, refs).
- [ ] Figures at required resolution + figure legends; tables.
- [ ] SI Appendix (extended methods, supporting figs/tables, supplementary text); Datasets if any.
- [ ] Cover letter (significance + track + suggested editor/reviewers if Direct).
- [ ] Author list, affiliations, ORCIDs, corresponding author.
- [ ] Author contributions, competing interests, funding statements.
- [ ] Classification + keywords entered in the submission system.

## Final integrity sweep

- [ ] No over-claiming beyond the evidence (re-read the Significance Statement, abstract, and last paragraph).
- [ ] Significance Statement is genuinely broader/plainer than the abstract — not a duplicate.
- [ ] Every figure's n, error bar, and test are defined in its legend.
- [ ] All accession numbers/DOIs are live and correct.

## Templates

- `templates/checklist.md` — copyable preflight checklist.
- `templates/cover_letter_template.md` — PNAS cover-letter scaffold (significance + track + suggested editor/reviewers).

## Track-specific preflight, side by side

The three PNAS tracks fail preflight for different reasons — check the one you chose:

- **Direct Submission:** the editor is assigned by PNAS, so the cover letter must argue broad significance and name suggested editors/reviewers. Blocker: no suggested editor in a field where the paper is cross-divisional.
- **Contributed:** an NAS member communicates their own paper, secures ≥2 independent reviewers, and submits their reviews plus author responses. Blockers: member over the annual quota; reviewers not demonstrably independent; review file missing.
- **Prearranged Editor:** an NAS member is lined up to handle a Direct submission before upload. Blocker: the editor arrangement is claimed but not confirmed in the cover letter.

## Cover-letter significance paragraph: before / after

The cover letter's opening is the editor's first read of your general-significance case.

- **Before:** "Please consider our manuscript, which reports new results on system X of interest to specialists in the field."
- **After:** "We report that system X resolves a question debated across two PNAS divisions: [one-sentence broad claim]. Because the result [general implication], it will interest readers well beyond the immediate subfield — which is why we submit to PNAS rather than a specialist journal."

The revision states the cross-division stake, ties it to the Significance Statement, and justifies the venue choice — exactly what a handling editor triages on.

## Output format

```
【Track】 Direct / Contributed (+ eligibility confirmed)
【Blocking gaps】 [...]  (must fix before upload)
【Warnings】 [...]       (should fix)
【Files ready】 main / figures+legends / SI Appendix / cover letter / metadata
【Verdict】 GO / NO-GO + the top 3 fixes
【Next】 submit | pnas-rebuttal (after decision)
```

## Anti-patterns

- **Do not** upload before accession numbers/DOIs exist.
- **Do not** submit without the Significance Statement and Classification.
- **Do not** let the Significance Statement duplicate the abstract.
- **Do not** rely on memory; run the checklist top to bottom.
