---
name: jcr-submission
description: Use when running the final pre-submission preflight for a Journal of Consumer Research (JCR) manuscript — ScholarOne portal, anonymization for double-anonymized review, the 60-page cap, the 200-word abstract, the 300-word Consumer Relevance and Contribution Statement, the Step-6 Data Collection Statement, Chicago/Word formatting, and the transparency apparatus. Checks readiness to submit; it does not handle the post-decision response (jcr-rebuttal).
---

# Pre-Submission Preflight (jcr-submission)

## When to trigger

- "We're submitting this week" — the last check before hitting submit
- Unsure what ScholarOne requires (anonymized manuscript, statements, files)
- Need to confirm double-anonymized anonymization is complete
- Verifying the manuscript matches current JCR formatting and transparency rules

> Always re-verify current limits and required files on consumerresearcher.com and the OUP JCR instructions before submitting — specifics change. As of 2026-06-01 (manuscript-preparation and research-ethics rules re-verified 2026-11-24) the verified key specs are below.

## Verified JCR specs (confirm current values)

- **Length:** manuscript may not exceed **60 double-spaced pages**, inclusive of **title, abstract, main text (with tables and figures embedded), appendices, and references**. (A page cap, not a word cap; exhibits count.)
- **Web appendix:** supplementary materials up to **40 MB**, distinct from a manuscript appendix and **excluded** from the 60-page cap — use it for overflow stimuli, instruments, and extra studies.
- **Abstract:** ≤ **200 words**, followed in the manuscript by **three to six keywords** in a separate paragraph.
- **Consumer Relevance and Contribution Statement:** ≤ **300 words**, required for new submissions (distinct from the abstract).
- **Format:** upload in **Word, Rich Text, or PDF** (LaTeX users upload a PDF); file ≤ 40 MB; US letter, 1-inch margins, 12-pt Times New Roman, double-spaced and left-justified, no page numbers, headers, footers, or line numbers; no separate title page (title goes in the manuscript file). JCR style guide, and for matters not covered, the **Chicago Manual of Style** (title capitalization, author-date references).
- **Submission portal:** ScholarOne Manuscripts (ManuscriptCentral) at **mc.manuscriptcentral.com/jconres**.
- **Review:** **double-anonymized**; remove all identifying information; self-citation allowed only if the cited work is publicly available.
- **Fees:** **no submission or publication fee**; only optional open-access licensing and color-print charges (OUP lists **$600 per figure** for print colour; black-and-white print is free).
- **Data and Materials Availability Statement (revised policy, September 24, 2026):** **every** submission, including the original one, carries a single-paragraph statement before the references saying where the (anonymized) data, stimuli, measures, protocols and code are, or why they cannot be shared; JCR by default expects anonymized data to be available to the review team and, after acceptance, to readers (preferably via a third-party repository such as Dataverse).
- **AI use:** disclose Gen-AI use per the OUP policy and the JCR AI Use and Disclosure Policy — at Step 6 **and** in the relevant manuscript section (e.g., methods, acknowledgments); grammar/spelling/formatting help and literature identification need no disclosure.
- **Formats (since Jan 1, 2025):** standard empirical paper, plus **Registered Reports** and **Brief Commentaries** — select the correct type.

## Pre-submission checklist

### Anonymization (double-anonymized)

- [ ] Manuscript contains **no** author names, affiliations, author notes, or acknowledgments
- [ ] Identifying **URLs** removed; field sites/institutions described generically ("a large public university")
- [ ] Self-citations worded neutrally and only to publicly available work
- [ ] File metadata/properties and file names scrubbed of author/institution identity

### Required statements & format

- [ ] **Abstract ≤ 200 words**, matching the ScholarOne entry, followed by **3–6 keywords**
- [ ] **Consumer Relevance and Contribution Statement ≤ 300 words**, distinct from the abstract
- [ ] Manuscript **≤ 60 double-spaced pages** including title, abstract, text, embedded tables/figures, appendices, and references
- [ ] Overflow stimuli/instruments/extra studies moved to the **web appendix (≤ 40 MB)**
- [ ] **Chicago**-style title capitalization and author-date references; Word, RTF, or PDF file ≤ 40 MB

### Research transparency (JCR-specific)

- [ ] **Step-6 Data Collection Statement** prepared (where/when/who collected and analyzed the data, where stored) — hidden from reviewers, published if accepted
- [ ] **Data and Materials Availability Statement** in the manuscript (before the references) with anonymized links to data, stimuli, measures, protocols and code — or the reason they cannot be shared; links open without an access request
- [ ] **Statistical/programming replication code** provided (or a written description for proprietary code)
- [ ] Plan to **retain data ≥ 7 years** after publication; consulted the "Research Method Transparency Guidelines and Reporting Requirements"

### Files & declarations

- [ ] Anonymized main manuscript (with embedded exhibits as the portal specifies)
- [ ] Web appendix / supplementary file
- [ ] Confidential cover letter (suggest up to three current associate editors; disclose conflicts of interest)
- [ ] Author note (incl. acknowledgments, funding, AI-use disclosure) entered at Step 6, not in the manuscript
- [ ] Human-subjects/IRB approval stated where applicable; conflicts and funding disclosed off the anonymized text
- [ ] Correct article type selected (standard / Registered Report / Brief Commentary)

### References & consistency

- [ ] Every in-text citation appears in the reference list and vice versa
- [ ] Construct names, hypothesis labels, and study/table/figure numbers consistent throughout

## ScholarOne operation notes

- Submit through ScholarOne at **mc.manuscriptcentral.com/jconres**; keep your author account and ORCID current.
- Complete the **Step-6 Data Collection Statement** in the portal; it is hidden from reviewers but published if accepted.
- Upload anonymized files and the web appendix in the designated slots; preview the built PDF before final submission.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue jcr-skills   # from a clone of the AJS repository
```

It reports, with a location for each finding:

- this venue's machine-readable limits, review mode and required statements, when the venue has a
  rules block (`--list-venues`);
- citations ↔ references;
- table and figure numbering, cross-references and standard-error notes;
- abstract numbers traced to the tables;
- placeholders and tracked changes.

With the Research Toolkit pack installed, `rt-submission-readiness` runs the same check as stage 0
of the full pre-submission pipeline (scorecard → referee panel → polish → cover letter). Anything
it lists as *not checked* still needs the manual items below.

## Anti-patterns

- Letting embedded tables/figures push the manuscript over 60 pages (they count).
- Treating the Consumer Relevance and Contribution Statement as a copy of the abstract.
- Skipping or deferring the Step-6 Data Collection Statement.
- APA-style references in a Chicago journal.
- Identifying language ("in our 2019 study") or named field sites breaking anonymization.

## Output format

```
【Anonymization】pass / fix: [...]
【Statements】abstract ≤200; Consumer Relevance ≤300: ready?
【Length】≤60 pp incl. embedded exhibits; overflow → web appendix (≤40 MB)
【Transparency】Data Collection Statement + repository + code: complete?
【Format】Word; Chicago title-case + author-date
【Article type】standard / Registered Report / Brief Commentary
【Next step】await decision → jcr-review-process; on R&R → jcr-rebuttal
```

## Resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — participant sourcing (Prolific/CloudResearch/Qualtrics), analysis (R/PROCESS/spotlight), CCT tools (NVivo/ATLAS.ti), and JCR-approved repositories
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JCR/OUP URLs behind every verified fact in this pack (accessed 2026-06-01)
