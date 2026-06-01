---
name: ijcai-submission
description: Use when auditing an IJCAI or IJCAI-ECAI main-track submission for Chairing Tool readiness, abstract and author-information deadlines, page limits, double-blind anonymity, supplementary files, reproducibility, resubmission information, author limits, dual-submission policy, and LLM-use policy.
---

# IJCAI Submission

Use this for an IJCAI main-track submission audit. Reopen the current conference CFP,
Author Kit, FAQ, reproducibility page, submission site, and conflict policy before giving
deadline-ready advice.

## Submission audit

- Confirm the target program: main track, one of the special tracks, Survey Track, or a
  non-main program. Track rules and deadlines can differ.
- Verify Chairing Tool account access, title, abstract, author details, ORCID status,
  author confirmations, keywords, conflicts, and any Primary Paper Initiative fee exposure.
- Apply the current author kit. IJCAI-ECAI 2026 main-track papers used a 9-page total limit:
  7 pages for body text, figures, and tables, plus up to 2 pages for references.
- Check that no acknowledgements or contribution statements appear in the anonymous review
  version, and that the optional ethics statement sits where current rules permit.
- Enforce double-blind anonymity in PDF content, metadata, filenames, supplement, code,
  paths, URLs, and resubmission files.
- Submit supplementary material and resubmission information by the full-paper deadline; do
  not rely on rebuttal-time uploads.
- Confirm the per-author submission limit, dual-submission policy, and last-12-month
  rejection disclosure before upload.
- Apply the current LLM-use policy. For IJCAI-ECAI 2026, style/language polishing was
  allowed, but LLM-written manuscript text was a desk-reject risk.

## Blocking risks

- Missing abstract registration or missing author information.
- Overlength PDF or template manipulation.
- Identity leakage in the paper, supplement, code, data, paths, or metadata.
- Missing required resubmission information for a recent rejected version.
- Concurrent formal archival submission.
- LLM-generated paper text, hallucinated references, or unsupported claims.

## Output format

```text
[IJCAI readiness] Ready / Needs fixes / Not ready
[Track] main / special / survey / other
[Blocking checks] <page/anonymity/authors/ORCID/supplement/resubmission/dual-submission/LLM>
[Highest desk-reject risk] <one issue>
[Fix order] <ordered fixes before submission>
```
