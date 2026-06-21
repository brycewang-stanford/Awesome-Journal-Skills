---
name: jmr-submission
description: Use when running the final pre-submission preflight for a Journal of Marketing Research (JMR) manuscript — ScholarOne portal, double-anonymization, the 50-page page limit, the 'W'-prefixed Web Appendix PDF, the title-page Data Availability Statement, AMA formatting, and AI/ethics declarations. Checks readiness to submit; jmr-rebuttal handles the post-decision response.
---

# Pre-Submission Preflight (jmr-submission)

## When to trigger

- "We're submitting this week" — the last check before hitting submit
- Unsure what ScholarOne requires (anonymized manuscript, title page, Web Appendix PDF)
- Verifying the print paper meets the 50-page limit and AMA formatting
- Confirming double-anonymization and the Data Availability Statement

> Always re-verify current limits and required files on the SAGE author instructions and the AMA submission-guidelines page before submitting — specifics change, and the masthead is mid-handover (see below). As of 2026-06-01 the verified key specs are below.

## Verified JMR/AMA specs (confirm current values)

- **Portal**: ScholarOne / Manuscript Central at **mc.manuscriptcentral.com/ama_jmr**; questions to jmr@ama.org.
- **Length**: **50-page maximum**, properly formatted and **inclusive** of title, abstract, keywords, text, footnotes, references, tables, figures, and print appendices. The **Web Appendix does NOT count** toward the 50 pages. JMR uses a **page** limit, not a word cap.
- **Formatting**: 12-point Times New Roman (or 12-point LaTeX font), double-spaced (tables/references may be single-spaced), 1-inch margins; **no page/line numbers, no headers/footers**.
- **Abstract**: **200 words max, third person.** Title **≤ 25 words**; up to **8 keywords**.
- **Review**: **double-anonymized**; **two independent reviews** are required to reach a Revise or Accept decision; initial editorial evaluation may **desk-reject** out-of-scope or non-conforming papers.
- **Statistics**: empirical papers must report **exact p-values (three digits), standard errors, and effect sizes**; AMA number style (no leading zero, ≤ 3 decimals).
- **Web Appendix**: a **single separate PDF**, excluded from the page limit, with tables/figures labeled **'W'-prefixed** ("Table W1", "Figure W1").
- **Transparency**: AMA Research Transparency Policy; a **Data Availability Statement is required on the title page**; be ready to share code, instruments, and materials on request and to provide data/materials before final acceptance.
- **Integrity & AI**: every submission is screened with **iThenticate**; any **AI-generated content must be disclosed** in the main document and Acknowledgments.
- **Fees**: the SAGE MRJ page states **"There are no fees payable to submit or publish in this journal"** for the standard route; optional Sage Choice open access is available, and the SAGE 2026 Choice price list records JMR's 2026 OA APC as **USD 5,780 / GBP 4,238.474**. Recheck the annual SAGE price list before quoting fees.
- **Editor transition**: Rebecca Hamilton (Georgetown) is EIC through 30 June 2026; Raphael Thomadsen's incoming team (WashU, 2026–2029) has processed new manuscripts since 1 April 2026.

## Pre-submission checklist (summary; full version in templates/checklist.md)

### Anonymization (double-anonymized)
- [ ] Manuscript file has **no** author names, affiliations, or acknowledgments
- [ ] Self-citations worded neutrally ("prior research (Author 2020)"), not "our earlier work"
- [ ] Title page (separate) holds authors, affiliations, contact, funding, **Data Availability Statement**
- [ ] File metadata and file names scrubbed of identity

### Format & length
- [ ] Print paper **≤ 50 pages** (everything except the Web Appendix counts)
- [ ] 12-pt Times New Roman, double-spaced, 1-inch margins, no page/line numbers or headers/footers
- [ ] Abstract ≤ 200 words, third person; title ≤ 25 words; ≤ 8 keywords
- [ ] AMA author-year citations; exact p-values, SEs, effect sizes in all tables

### Web Appendix & files
- [ ] Web Appendix as a **single separate PDF**, exhibits **'W'-prefixed**
- [ ] Anonymized main document; separate title page with all identifiers + DAS
- [ ] Cover letter (fit, contribution, not under review elsewhere)

### Declarations & ethics
- [ ] **Data Availability Statement** on the title page
- [ ] **AI-generated content disclosed** in the main document and Acknowledgments
- [ ] IRB/human-subjects approval where applicable; no concurrent submission
- [ ] iThenticate-clean (paraphrase, quote, and cite properly)

## ScholarOne operation notes

- Create/keep your author account and ORCID current; select the article type and the keywords/domain so the manuscript routes to an appropriate **Coeditor / Associate Editor** by domain.
- Upload the anonymized main document, the title page, and the Web Appendix PDF in the designated slots; preview the built PDF before final submission.

## Anti-patterns

- Letting the print paper exceed 50 pages by forgetting tables/figures/references count.
- Web Appendix not a single PDF, or exhibits not 'W'-prefixed.
- Missing the title-page Data Availability Statement, or undisclosed AI use.
- Asterisk/threshold statistics instead of exact p-values, SEs, and effect sizes.

## Output format

```text
[Anonymization] pass / fix
[Format & length] <=50pp, AMA format, abstract<=200 (3rd person): pass/fix
[Web Appendix] single PDF, W-prefixed: pass/fix
[Declarations] DAS on title page / AI disclosure / IRB: complete?
[Files] main doc / title page / Web Appendix / cover letter: ready?
[Next step] await decision → jmr-review-process; on R&R → jmr-rebuttal
```

## Resources

- [`templates/checklist.md`](templates/checklist.md) — full pre-submission self-check (anonymization / format / 50-page limit / Web Appendix / declarations / references / portal)
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — behavioral and modeling tools, and the Web Appendix / replication workflow
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AMA/SAGE URLs behind every verified fact (accessed 2026-06-01)
