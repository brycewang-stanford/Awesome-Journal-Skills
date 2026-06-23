---
name: pnasnexus-submission
description: Use as the final preflight before submitting to PNAS Nexus — a complete checklist across fit, open access/APC/license, article type & length, Significance Statement, abstract, classification, figures, statistics, data/code, references, and required files. Covers the PNAS-transfer case and bundles a checklist and cover-letter template. Emits GO/NO-GO.
---

# Submission Preflight (pnasnexus-submission)

## When to trigger

- The manuscript is "done" and you're about to upload via the submission portal (pnasnexus.msubmit.net).
- You want a single gate that confirms every other pnasnexus-* skill's output landed.
- You are completing a **transfer from PNAS** and need to confirm nothing is missing.
- A revision is going back and you need to confirm nothing regressed.

## Master preflight checklist

### Fit & venue
- [ ] Clears the broad, cross-disciplinary significance bar (`pnasnexus-fit`); a reader from another division would care.
- [ ] PNAS Nexus is the right venue (not better at flagship PNAS or a field journal).
- [ ] If transferring from PNAS: decline was about **fit/priority, not soundness**; prior reviews attached.
- [ ] Title is declarative, specific, parseable by a non-specialist.

### Open access, APC & license
- [ ] Confirmed gold OA; **APC figure obtained live from the OUP calculator** (category + corresponding-author region) — not from memory (`pnasnexus-openaccess`).
- [ ] Waiver/discount checked (LMIC waiver/discount, Read & Publish, membership, discretionary).
- [ ] License chosen: ☐ CC BY 4.0 ☐ CC BY-NC 4.0 — **CC BY if a funder mandate applies**.
- [ ] Funder open-access requirements (license + deposit) satisfied.
- [ ] (Reminder) no Direct/Contributed track — standard editor-assigned review.

### Article type, structure & length
- [ ] Article type chosen: ☐ Research Report ☐ Brief Report ☐ Registered Report (S1/S2) ☐ Perspective ☐ Review.
- [ ] Within the page budget for that type (Research Report: 6 pp preferred / **12 max**); captions, legends, abstract, and Significance Statement counted.
- [ ] Order: Title / authors / Significance / Abstract / Intro / Results / Discussion / **Materials and Methods (in main text)** / back matter.
- [ ] Materials and Methods present in the **main text** (not solely in SI).
- [ ] Classification chosen: research area (Biological-Health-Medical / Physical-Engineering / Social-Political) + subcategory.

### Significance Statement & abstract
- [ ] Significance Statement **50–120 words** (Research Reports / Stage 2 Registered Reports), for a broad audience, distinct from the abstract.
- [ ] Abstract ≤ 250 words, **single paragraph, no headings**, ≥1 quantified result.

### Figures & display items
- [ ] Within the graphical-element budget (~4 for a 6-pp Research Report; secondary items → SI).
- [ ] Sized to journal column widths; fonts legible at print size.
- [ ] Data shown (points + n); error bars defined; scale bars present.
- [ ] Colorblind-safe; color used where it helps (OA, online); **raw unprocessed images retained**.

### Statistics & reproducibility
- [ ] Each claim: effect size + CI + n + test + assumptions.
- [ ] Biological vs technical replication clear; sample-size rationale stated.
- [ ] Randomization/blinding reported or justified; multiplicity controlled.
- [ ] Analysis code + scripts public and archived (DOI).

### Data, code, materials, ethics
- [ ] Data, code, materials, and protocols deposited in a **public repository** with accession numbers/DOIs (mandatory upon publication; no "on request" only for primary data).
- [ ] Data and Code Availability Statement drafted and compliant; datasets/software cited with the `[dataset]` tag.
- [ ] Materials/reagent sharing plan; ethics approvals (IRB/IACUC/permits) as needed.

### References
- [ ] **Any readable style accepted at submission** — but the list is consistent, complete, and fully resolvable; DOIs added.
- [ ] Data/software cited as formal references with the `[dataset]` tag.

### Required files & metadata
- [ ] Main text (title, Significance Statement, abstract, body, Materials and Methods, references).
- [ ] Figures at required resolution + figure legends; tables.
- [ ] Supporting Information (extended methods, supporting figs/tables, supplementary text); Datasets if any.
- [ ] Cover letter (advance + broad significance; article type; transfer note if applicable).
- [ ] Author list, affiliations, ORCIDs, corresponding author (drives APC/waiver eligibility — set deliberately).
- [ ] Author contributions, competing interests, funding statements.
- [ ] Classification + keywords entered in the submission system.

## Final integrity sweep

- [ ] No over-claiming beyond the evidence (re-read the Significance Statement, abstract, and last paragraph).
- [ ] Significance Statement is genuinely broader/plainer than the abstract — not a duplicate — and within 50–120 words.
- [ ] Every figure's n, error bar, and test are defined in its legend.
- [ ] All accession numbers/DOIs are live and correct.

## Templates

- `templates/checklist.md` — copyable preflight checklist.
- `templates/cover_letter_template.md` — PNAS Nexus cover-letter scaffold (significance + article type + transfer note + suggested reviewers).

## Output format

```
【Article type】 Research Report / Brief Report / Registered Report / Perspective / Review
【OA/APC/license】 APC confirmed-live; waiver path; license (CC BY / CC BY-NC); funder-compliant?
【Transfer from PNAS?】 N/A | yes (reviews attached; decline was fit/priority)
【Blocking gaps】 [...]  (must fix before upload)
【Warnings】 [...]       (should fix)
【Files ready】 main / figures+legends / SI / cover letter / metadata
【Verdict】 GO / NO-GO + the top 3 fixes
【Next】 submit | pnasnexus-rebuttal (after decision)
```

## Anti-patterns

- **Do not** upload before the APC, waiver eligibility, and license are settled (`pnasnexus-openaccess`).
- **Do not** upload before data/code are deposited with accession numbers/DOIs.
- **Do not** submit without the Significance Statement (50–120 words) and the classification.
- **Do not** let the Significance Statement duplicate the abstract.
- **Do not** put Materials and Methods only in Supporting Information.
- **Do not** rely on memory; run the checklist top to bottom.
