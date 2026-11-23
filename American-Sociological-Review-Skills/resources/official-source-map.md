# ASR Official Source Map

Primary source map for American Sociological Review (ASR)-specific facts encoded
in this pack. Official pages were re-checked on **2026-06-21**. Submission rules, fee and masthead
**re-verified 2026-11-24**: the Sage, ASA and Sage-PDF pages all refuse automated access from this
environment (HTTP 403 / Cloudflare, also via WebFetch), so the ASR Submission Guidelines (#1) were
re-read via search-engine rendering restricted to journals.sagepub.com and asanet.org, and the editorial
board (#5) via the Internet Archive snapshot of 2026-08-24. No changes found: 15,000-word cap including
text, references and footnotes (tables and figures excluded), 200-word abstract ceiling, 3,000-word
Comments/Replies, USD 25 fee with the ASA student-member waiver, anonymous peer review with a separate
title page, ASA Style Guide (7th ed., 2022), and the four UMass Amherst editors are all as recorded.

## Official submission and policy pages

| # | URL | What it verifies | Accessed |
|---|---|---|---|
| 1 | https://journals.sagepub.com/author-instructions/asr | ASR Submission Guidelines; Sage Track submission; anonymous manuscript and title-page separation; abstract and word limits (Articles ≤ 15,000 words including text, references and footnotes, excluding tables and figures; abstract 200 words or fewer; Comments/Replies under 3,000 words); USD 25 manuscript fee and ASA student-member waiver; formatting, style, ethics, and data-sharing requirements | 2026-06-21; re-verified 2026-11-24 via search-engine rendering (page returns 403) |
| 2 | https://www.asanet.org/publications/journals/american-sociological-review/ | ASR page at the American Sociological Association; flagship identity, ASA ownership, and SAGE publication context | 2026-06-21 |
| 3 | https://www.asanet.org/publications/journals/submission-information-for-asa-publications/ | ASA shared submission, ethics, and data-sharing norms for ASA journals | 2026-06-21 |
| 4 | https://www.sagepub.com/docs/default-source/msg/submission-guidelines_-american-sociological-review_-sage-journals.pdf | SAGE ASR submission-guidelines PDF fallback for the same author-instruction content | 2026-06-21 |
| 5 | https://journals.sagepub.com/editorial-board/asr | ASR editorial board / current editors masthead (Cort, Misra, Smith-Doerr, Tomaskovic-Devey) | 2026-06-22; re-verified 2026-11-24 via the Internet Archive snapshot https://web.archive.org/web/20260824142116/https://journals.sagepub.com/editorial-board/asr |
| 6 | https://www.umass.edu/social-sciences/news/asa-editors | UMass Amherst announcement of the 2024–2028 ASR editorial team (Joya Misra joining in 2026) | 2026-06-22 |

## Verified facts encoded in the pack

- **Publisher / owner:** ASR is the American Sociological Association flagship journal and is published by SAGE. (#1, #2)
- **Submission route:** Sage Track / ScholarOne at `mc.manuscriptcentral.com/asr`. (#1)
- **What ASR evaluates:** general-interest sociology, strong research designs/methods, broad sociological appeal, and theory development that transcends subfields. (#1)
- **Anonymous review files:** ASR manuscripts are peer-reviewed anonymously ("anonymous peer review"; the page does not use the term "double-blind"); authors upload an anonymous manuscript without title page plus a separate title page carrying institutional affiliations, acknowledgments, word count, and corresponding-author contact information. (#1)
- **Previously rejected papers:** ASR does not consider papers previously rejected at ASR. (#1)
- **Processing fee:** USD 25 non-refundable manuscript processing fee, paid through Sage Track; required for new manuscripts unless authored by ASA student members. (#1)
- **Article length:** Articles may not exceed 15,000 words including text, references, and footnotes, excluding tables and figures. (#1)
- **Comments/Replies:** capped at 3,000 words and uploaded directly in Sage Track. (#1)
- **Abstract:** upload abstract of 200 words or fewer; manuscript-preparation section describes 150-200 words and no author-identifying information. Use the stricter 200-word ceiling in submission checks. (#1)
- **Formatting:** double-spaced text, notes, and references; Times New Roman 12 point; at least 1-inch margins. (#1)
- **Self-citation / anonymity:** authors may cite their own work but must avoid wording that identifies them; dissertations, working drafts, and unpublished papers generally should not be self-cited in identifiable ways. (#1)
- **Style:** ASA Style Guide (7th ed., 2022); author-year citations in text with ASA-style notes and references. (#1)
- **Ethics:** simultaneous submission elsewhere while under ASR review is treated as unethical; previously published or forthcoming significant findings must be clearly identified. (#1)
- **Data sharing:** ASA Code of Ethics language expects sociologists to share data and documentation as part of a research plan and generally make data available after project completion or major publications, subject to proprietary/confidentiality limits. (#1, #3)

## Bounded live-check rules

- Do not encode a mandatory editor-verified replication package for ASR. The confirmed rule is ASA data-sharing ethics, not an AEA-style reproduction gate.
- **Current editors (verified 2026-06-22):** the **2024–2028** editorial team is **David Cort, Laurel Smith-Doerr, Donald Tomaskovic-Devey, and Joya Misra** (Misra joined in 2026), all at the **University of Massachusetts Amherst**. (#5, #6) Re-open the ASR/ASA masthead before naming the team in submission-ready advice, since offices rotate.
- **Processing fee (verified 2026-06-22):** **USD 25** non-refundable manuscript processing fee via Sage Track, **waived for ASA student members**. (#1) Re-check the amount/waiver wording immediately before submission; treat impact factor as volatile.

## UNVERIFIED / 待核实 (as of 2026-11-24)

- **In-manuscript declarations** (funding, conflict-of-interest, ethics/IRB approval, generative-AI use):
  the search-engine rendering of #1 did not surface ASR-specific wording on 2026-11-24, and the live page
  refuses automated access. Sibling Sage sociology journals require such statements, but do not assume
  ASR does; check the live Sage Track prompts before submission.
- **ScholarOne URL `mc.manuscriptcentral.com/asr`**: returns 403 to automated clients; the guidelines
  name "Sage Track" as the route. Re-open in a browser.
- **Fee waiver for revised (R&R) manuscripts**: an older ASA submission-information page (#3) says the
  fee is waived for R&Rs; not confirmed on the current Sage page.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "American Sociological Review",
  "verified": "2026-11-24",
  "rules": {
    "main_text_words_max": {"value": 15000, "source": "https://journals.sagepub.com/author-instructions/asr", "note": "ASR counts text, references and footnotes (tables and figures excluded); preflight's main-text count leaves out references and notes, so add them before comparing. Comments/Replies under 3,000 words"},
    "abstract_words_max": {"value": 200, "source": "https://journals.sagepub.com/author-instructions/asr", "note": "'200 words or fewer'; the preparation section describes 150-200 words with no author-identifying information"},
    "review_mode": {"value": "double-blind", "source": "https://journals.sagepub.com/author-instructions/asr", "note": "'anonymous peer review': anonymous manuscript without title page, identifying self-citation wording removed"},
    "separate_upload_statements": {"value": ["acknowledgments"], "source": "https://journals.sagepub.com/author-instructions/asr", "note": "separate title page carries institutional affiliations, acknowledgments, word count and corresponding-author contact"},
    "required_statements": {"value": [], "source": "https://journals.sagepub.com/author-instructions/asr", "note": "no in-manuscript statement confirmed on 2026-11-24; funding/COI/ethics/AI wording is listed as UNVERIFIED"},
    "submission_fee": {"value": "USD 25 non-refundable manuscript processing fee via Sage Track; waived for ASA student members", "source": "https://journals.sagepub.com/author-instructions/asr"},
    "portal": {"value": "Sage Track", "source": "https://journals.sagepub.com/author-instructions/asr"},
    "reference_style": {"value": "ASA Style Guide (7th ed., 2022), author-year citations", "source": "https://journals.sagepub.com/author-instructions/asr"},
    "file_format": {"value": "double-spaced text, notes and references; 12-point Times New Roman; margins at least 1 inch", "source": "https://journals.sagepub.com/author-instructions/asr"},
    "data_code_policy": {"value": "ASA Code of Ethics data sharing: data and documentation generally made available after completion or major publications, subject to proprietary/confidentiality limits; no editor-run replication check", "source": "https://journals.sagepub.com/author-instructions/asr"},
    "keywords_required": {"value": null, "note": "not stated in the renderings of the official page read on 2026-11-24"},
    "llm_policy": {"value": null, "note": "ASR-specific AI wording not surfaced on 2026-11-24 (page refuses automated access)"}
  }
}
```
