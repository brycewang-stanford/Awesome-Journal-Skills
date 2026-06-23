---
name: amj-submission
description: Use when running the final pre-submission preflight for an Academy of Management Journal (AMJ) manuscript — ScholarOne portal, anonymization for double-blind review, AOM house-style formatting, files, and ethics declarations. Checks readiness to submit; it does not handle the post-decision response (amj-rebuttal).
---

# Pre-Submission Preflight (amj-submission)

## When to trigger

- "We're submitting this week" — the last check before hitting submit
- Unsure what ScholarOne requires (anonymized manuscript, title page, cover materials)
- Need to confirm double-blind anonymization is complete
- Verifying the manuscript matches current AMJ/AOM formatting requirements

> Always re-verify current limits and required files on the official AMJ submission page and the AOM Style Guide before submitting — specifics change. As of 2026-05-30 the verified key specs are below.

## Verified AMJ/AOM specs (confirm current values)

- **Length:** full manuscripts have a **40-page maximum for the main body**, which *includes* text, references, and appendices but *excludes* tables and figures. (AOM uses a **page** limit, not a word cap.)
- **Formatting:** double-spaced throughout (including references and notes), **Times New Roman 12-point**, **1-inch margins** on all sides, pages numbered consecutively.
- **Abstract:** no more than **200 words**.
- **Keywords:** **three** keywords supplied at submission.
- **Submission portal:** ScholarOne Manuscripts at **mc.manuscriptcentral.com/AMJ**.
- **Review:** blind review; desk review typically takes ~1-2 weeks, and AMJ targets developmental feedback to authors within roughly **60 days**. Authors who submit are expected to reciprocate by reviewing for AMJ when asked.
- **Style:** APA conventions per the AMJ Style Guide for Authors (citations, reference list, headings, tables).
- **Integrity:** manuscripts are screened with **iThenticate**; no simultaneous submission; any preprint posted online must be **removed during the review period**.
- **Fees:** AOM charges **no submission fee** and **no author-paid APC**. AMJ is subscription-published, and AOM **does not support Gold (author-funded) open access**; the only open-access route is **Green OA (self-archiving)**, where authors may post the accepted (pre-copyedited) manuscript and the Version of Record may be made open only after a **12-month embargo**, at no fee (verified on the AOM open-access page 2026-06-23). Re-verify on the AOM/AMJ open-access page before submission, as policy may change.
- **AI disclosure:** any use of AI tools must be disclosed in the **cover letter** and the **acknowledgements**, with confirmation that you have read the AOM AI policy; AI cannot be listed as an author.

## Pre-submission checklist

### Anonymization (double-blind)

- [ ] Manuscript file contains **no** author names, affiliations, or acknowledgments
- [ ] Self-citations are worded neutrally ("prior research (Author, 2020)"), not "our earlier work"
- [ ] Acknowledgments, funding, and author bios live on a **separate title page**, not in the manuscript
- [ ] File metadata/properties scrubbed of author identity
- [ ] File names contain no author or institution identifiers

### Format (verify against the current AOM Style Guide)

- [ ] Title page (separate): title, authors, affiliations, contact, acknowledgments, funding
- [ ] Abstract ≤ 200 words; **three** keywords supplied
- [ ] AOM/APA-style citations and reference list, alphabetized and complete
- [ ] Headings follow the AOM hierarchy; **double-spaced, Times New Roman 12-pt, 1-inch margins**
- [ ] Tables and figures placed/numbered as the portal requires; each self-contained
- [ ] Main body **≤ 40 pages** (text + references + appendices; tables/figures excluded)

### Files for ScholarOne

- [ ] Anonymized main document (manuscript + tables + figures, or as the portal specifies)
- [ ] Separate title page with all identifying information
- [ ] Cover letter to the editor (concise: fit, contribution, not under review elsewhere)
- [ ] Any required supplementary/online appendix files
- [ ] High-resolution figure files if requested separately

### Declarations & ethics

- [ ] Human-subjects/IRB approval stated where applicable (separate from anonymized text)
- [ ] Data-availability/transparency statement as required by current policy
- [ ] No concurrent submission; prior conference/working-paper versions disclosed in the cover letter
- [ ] **AI use disclosed** in the cover letter and acknowledgements per the AOM AI policy (AI is never an author)
- [ ] Conflicts of interest and funding disclosed on the title page
- [ ] Authorship and contribution roles agreed by all authors

### References & consistency

- [ ] Every in-text citation appears in the reference list and vice versa
- [ ] Canonical theory works for the focal domain are cited (a frequent reviewer check)
- [ ] Hypothesis labels, construct names, and table/figure numbers are consistent throughout

## ScholarOne operation notes

- AMJ submits through ScholarOne Manuscripts at **mc.manuscriptcentral.com/AMJ**; create/keep your author account and ORCID current.
- Select the correct article type and the most fitting division/keywords so the manuscript routes to an appropriate action editor.
- You may be asked to suggest qualified, non-conflicted reviewers — propose people in the focal conversation without recent co-authorship.
- Upload anonymized files and the title page in the slots the system designates; preview the built PDF before final submission.

## Anti-patterns

- Submitting with self-identifying language ("in our 2019 study") intact.
- Acknowledgments/funding left inside the anonymized manuscript.
- Reference list in a non-AOM default style straight from the reference manager.
- Missing data-availability/ethics statement, or undisclosed AI use, where the policy requires one.
- Inconsistent hypothesis labels or table numbers between text and exhibits.
- Letting the main body exceed the 40-page limit by forgetting that references and appendices count toward it.

## Output format

```
【Anonymization】pass / fix: [...]
【Format vs. AOM guide】pass / fix: [...]
【Files ready】manuscript / title page / cover letter / supplements: yes/no
【Declarations】IRB / data availability / disclosures: complete? [...]
【References】citations↔list reconciled; canonical theory cited: yes/no
【Article type & division】selected ...
【Next step】await decision → amj-review-process; on R&R → amj-rebuttal
```

## Resources

- [`templates/manuscript_template.md`](templates/manuscript_template.md) — full AMJ manuscript skeleton (title page, abstract ≤200 words, three keywords, theory & hypotheses, methods, results, discussion, references) with verified AOM format specs
- The full pre-submission self-check (anonymization / format / files / declarations / references / portal) is inline above in this skill
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — management-research data sources and analysis software (Mplus / R lavaan / HLM / Stata / SPSS PROCESS)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AOM/AMJ URLs behind every verified fact in this pack (accessed 2026-05-30)
