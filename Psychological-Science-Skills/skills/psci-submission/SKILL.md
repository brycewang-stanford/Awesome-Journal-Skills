---
name: psci-submission
description: Use when running the final pre-submission preflight for Psychological Science via Manuscript Central — word-format compliance, the 150-word structured abstract, APA 7th-edition style, anonymization, the Research Transparency Statement, and open data/materials with DOIs. Final checks; it does not draft content.
---

# Submission Preflight (psci-submission)

The last check before submitting through **Manuscript Central** (`mc.manuscriptcentral.com/psci`).
Two things sink Psychological Science submissions most often: **busting the word format** and **missing
open-science compliance**. Verify volatile specifics (format numbers, policy wording, editor) on the
official page first.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure what the format and open-science requirements demand
- Confirming the abstract, anonymization, Transparency Statement, and deposits are in order

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** Association for Psychological Science (APS) / SAGE.
- **Portal:** **Manuscript Central**, `mc.manuscriptcentral.com/psci`.
- **Review:** anonymized — keep author identity out of the manuscript and repository links.
- **Word format (Research Article):** **Introduction + Discussion + Footnotes + Acknowledgments +
  Appendices ≤ 2,000 words combined**; **Method + Results excluded** (typically ≤ ~2,500); ~**40
  references**.
- **Abstract:** **150 words**, stating **sample sizes, participant populations, and design limitations**.
- **Style:** **APA 7th edition**; **tables/figures embedded** in the text.
- **Open science (since 1 Jan 2024):** **open data + materials required** (justified case-by-case
  exemptions); **Research Transparency Statement** between Intro and Methods; **DOIs** for shared
  content; preregistration reported and weighed.
- **Types:** Research Article; Registered Reports (Stage 1/2); RR with Existing Data; Commentary (≤1,000).

## Preflight checklist

### Format & abstract
- [ ] Intro + Discussion (+ footnotes/acks/appendices) **≤ 2,000 words combined**
- [ ] Method + Results readable (≤ ~2,500 words)
- [ ] Abstract **150 words**: sample sizes + populations + design limitations
- [ ] ~40 references; APA 7th edition; tables/figures **embedded** near discussion

### Anonymization (for review)
- [ ] No author names/affiliations in the manuscript
- [ ] Repository / preregistration links **anonymized** (e.g., OSF anonymized view)
- [ ] Identifying file metadata stripped

### Open science
- [ ] **Open data** deposited + DOI + data dictionary (or justified exemption)
- [ ] **Open materials** deposited + DOI
- [ ] **Analysis scripts** deposited; reproduce in a fresh session
- [ ] **Research Transparency Statement** placed between Intro and Methods
- [ ] Preregistration linked; confirmatory/exploratory split consistent

### Stats & disclosure
- [ ] Effect sizes + confidence intervals for major results
- [ ] Sample-size justification (power analysis if appropriate)
- [ ] Full disclosure of exclusions, conditions, and measures

## Anti-patterns

- Submitting over the 2,000-word combined budget
- Abstract missing sample sizes/populations/limitations or over 150 words
- Tables/figures at the end instead of embedded
- Missing or non-anonymized open-science links during masked review
- No Research Transparency Statement

## Output format

```
【Format】Intro+Discussion ≤ 2,000? Method+Results ≤ ~2,500? [Y/N]
【Abstract】150 words + sample sizes + populations + limitations? [Y/N]
【APA 7th + embedded exhibits】[Y/N]
【Anonymized】manuscript + repo/prereg links + metadata? [Y/N]
【Open science】data + materials + scripts + DOIs + Transparency Statement? [Y/N]
【Stats】effect sizes + CIs + sample-size justification + disclosure? [Y/N]
【Next】await decision → psci-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — repositories, DOIs, `papaja`, power and effect-size tools
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Psychological Science URLs behind every fact in this pack
