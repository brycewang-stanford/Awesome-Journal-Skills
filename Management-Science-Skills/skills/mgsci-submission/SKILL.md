---
name: mgsci-submission
description: Use when running the final pre-submission preflight for a Management Science (INFORMS) manuscript — ScholarOne seven-step upload, double-anonymization, author-year house style, the $79 submission fee and waivers, the Data and Code Disclosure package and project-page URL, and conference-proceedings disclosure. It checks readiness to submit; it does not handle the post-decision response (mgsci-rebuttal).
---

# Pre-Submission Preflight (mgsci-submission)

## When to trigger

- "We're submitting this week" — the last check before hitting submit
- Unsure what ScholarOne requires, or which Department to select
- Need to confirm double-anonymization and the disclosure package are complete
- Verifying fee/waiver eligibility and the citation/format specs

> Always re-verify current limits, fees, and required files on the official Management Science submission guidelines and Code and Data Disclosure Policy pages before submitting — specifics change. As of 2026-06-01 the verified key specs are below.

## Verified Management Science specs (confirm current values)

- **Portal:** ScholarOne Manuscripts ("Manuscript Central") at **mc.manuscriptcentral.com/mnsc** via INFORMS PubsOnline; a **seven-step** upload workflow (type/title/abstract, file upload, keywords, authors/institutions, reviewers/editors, etc.).
- **Abstract / keywords:** abstract **250 words or less**; **3–5 keywords**.
- **Length:** **no formal limit at initial submission**, but the journal prefers **short, focused** papers; **invited revisions** must fit **47 pages double-spaced (25 lines/page)** or **32 pages 1.5-spaced (33 lines/page)**, 11-pt font, 1-inch margins, **online appendix excluded**.
- **Style:** **author-year (name–date)** in-text citations, e.g., (Norman 1977); alphabetical reference list; double- or 1.5-spaced, 11-pt, 1-inch margins; **PDF preferred**.
- **Review:** **double-anonymized**; a Department Editor runs the desk screen, so select the correct **Department** at submission.
- **Submission fee:** **USD $79** per original submission (effective Aug 1, 2025); **waived** for current **INFORMS members** at submission and for authors whose **primary affiliation is in a low-/lower-middle-income economy**; an **honor-based, no-justification waiver** is available; ability to pay is not visible to editors/reviewers. (A third-party aggregator lists $89; the official editorial states $79 — treated as authoritative.)
- **Data and Code Disclosure:** for accepted papers a **Data Editor verifies** data and code replicate all main-manuscript results **before publication**; supply the package and a **project-page URL** (AsPredicted / AsCollected — verify current platform) at submission. Verification adds ~17 days on average.

## Pre-submission checklist

### Double-anonymization

- [ ] Manuscript contains **no** author names, affiliations, acknowledgments, or funding
- [ ] Self-citations worded neutrally, not "our earlier work"
- [ ] File metadata/properties scrubbed; file names carry no identifiers
- [ ] Any **conference-proceedings** version disclosed in the cover letter and the proceedings paper **cited anonymously**

### Format & style

- [ ] Abstract ≤ 250 words; **3–5 keywords** supplied
- [ ] **Author-year** in-text citations; alphabetical INFORMS/journal-style reference list
- [ ] Double- or 1.5-spaced, **11-pt, 1-inch margins**; PDF
- [ ] Notation minimal and consistent; exhibits self-contained
- [ ] Main body short and focused (recall the invited-revision cap; appendix excluded)

### Department & ScholarOne (seven steps)

- [ ] Correct **Department / area** selected so the right Department Editor desk-screens it
- [ ] Article type, title, abstract, keywords entered
- [ ] Authors/institutions and ORCID current
- [ ] Suggested/non-conflicted reviewers proposed where requested
- [ ] Built PDF previewed before final submission

### Fee & disclosure

- [ ] Submission **fee ($79) paid or a waiver claimed** (INFORMS member / low-income economy / honor-based)
- [ ] **Data and Code Disclosure** package prepared: master script regenerates all main-text results, README, version-pinned environment, data sources
- [ ] **Project-page / pre-registration URL** supplied where applicable (verify platform)
- [ ] Author-contribution disclosure included

### References & consistency

- [ ] Every in-text citation appears in the reference list and vice versa
- [ ] Canonical works for the focal Department's conversation cited
- [ ] Proposition/hypothesis labels, notation, and exhibit numbers consistent throughout

## Anti-patterns

- Submitting with self-identifying language or an un-anonymized proceedings citation.
- Selecting the wrong Department so the paper routes to the wrong desk.
- Forgetting the fee/waiver step, or assuming the waiver needs justification (it does not).
- A disclosure package that does not actually regenerate the reported results.

## Output format

```
【Anonymization】pass / fix: [...]
【Format & style】author-year, 250-word abstract, 3–5 keywords, 11-pt: pass/fix
【Department & ScholarOne】department selected; seven steps complete: yes/no
【Fee/waiver】paid or waiver claimed: which one
【Disclosure】package regenerates main results; project URL supplied: yes/no
【Next step】await decision → mgsci-review-process; on R&R → mgsci-rebuttal
```

## Resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — analytical (Gurobi/CPLEX/JuMP, Mathematica) and empirical (Stata/R/Python, oTree/Prolific) tooling plus the disclosure-package recipe
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official INFORMS/Management Science URLs behind every verified fact (accessed 2026-06-01)
