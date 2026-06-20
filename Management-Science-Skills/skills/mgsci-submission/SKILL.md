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

> Always re-verify current limits, fees, and required files on the official Management Science submission guidelines and Code and Data Disclosure Policy pages before submitting — specifics change. As of 2026-06-20 the verified key specs are below.

## Verified Management Science specs (confirm current values)

- **Portal:** ScholarOne Manuscripts ("Manuscript Central") at **mc.manuscriptcentral.com/mnsc** via INFORMS PubsOnline; a **seven-step** upload workflow (type/title/abstract, file upload, keywords, authors/institutions, reviewers/editors, details/comments, review/submit).
- **Abstract / keywords:** abstract **250 words or less**; **3–5 keywords**.
- **Length:** **no formal limit at initial submission**, but the journal prefers **short, focused** papers; **invited revisions** must fit **47 pages double-spaced (25 lines/page)** or **32 pages 1.5-spaced (33 lines/page)**, 11-pt font, 1-inch margins, **online appendix excluded**.
- **Style:** **author-year (name–date)** in-text citations, e.g., (Norman 1977); alphabetical reference list; double- or 1.5-spaced, 11-pt, 1-inch margins; **PDF preferred**.
- **Review:** **double-anonymous**; a Department Editor and possibly an Associate Editor first screen fit and merit, so select the correct **Department** at submission.
- **Submission fee:** **USD $79** per original submission (effective Aug 1, 2025); **waived** for current **INFORMS members** at submission and for authors whose **primary affiliation is in a low-/lower-middle-income country**; an **honor-based, no-justification waiver** is available; ability to pay is not visible to the editorial decision hierarchy.
- **Code and Data Disclosure:** policy effective **June 1, 2019** and revised **April 20, 2026**; authors provide an **AsCollected project-page URL** at submission. Accepted numerical/computational papers must provide data, programs, and other details sufficient to permit replication before production, or an approved alternative disclosure plan for proprietary/sensitive data.

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
- [ ] Five appropriate, non-conflicted reviewers proposed
- [ ] Three appropriate, non-conflicted Associate Editors proposed, plus any Guest AE rationale if used
- [ ] Built PDF previewed before final submission

### Fee & disclosure

- [ ] Submission **fee ($79) paid or a waiver claimed** (INFORMS member / low-income economy / honor-based)
- [ ] **Code and Data Disclosure** package prepared: master script regenerates main-text results where applicable, README, version-pinned environment, data sources, and alternative disclosure plan for proprietary/sensitive data if needed
- [ ] **AsCollected project-page URL** supplied
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
【Disclosure】package or approved disclosure plan ready; AsCollected URL supplied: yes/no
【Next step】await decision → mgsci-review-process; on R&R → mgsci-rebuttal
```

## Resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — analytical (Gurobi/CPLEX/JuMP, Mathematica) and empirical (Stata/R/Python, oTree/Prolific) tooling plus the disclosure-package recipe
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official INFORMS/Management Science URLs behind current process facts (accessed 2026-06-20)
