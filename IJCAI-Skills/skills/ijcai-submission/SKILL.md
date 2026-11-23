---
name: ijcai-submission
description: Use when auditing an IJCAI main-track submission for submission-site readiness, abstract and author-information deadlines, page limits, double-blind anonymity, supplementary files, reproducibility, resubmission information, author limits, dual-submission policy, and LLM-use policy.
---

# IJCAI Submission

Use this for an IJCAI main-track submission audit. Reopen the current conference CFP,
Author Kit, submission-process page, reproducibility page, submission site, and conflict policy before giving
deadline-ready advice.

## Submission audit

- Confirm the target program: main track, one of the special tracks, Survey Track, or a
  non-main program. Track rules and deadlines can differ.
- Verify submission-site account access (the IJCAI 2027 site was still "TBA" on 2026-11-23;
  2026 used Chairing Tool), title, abstract, author details, compulsory ORCID validation,
  author confirmations, up to 3 content-area keywords, conflicts, the reciprocal-reviewer
  designation, and any Primary Paper Initiative fee exposure (USD 100 per non-primary paper
  for IJCAI 2027).
- Apply the current author kit. IJCAI 2027 main-track papers use a 9-page total limit:
  7 pages for body text, figures, and tables, plus up to 2 pages for references.
- Check that no acknowledgements or contribution statements appear in the anonymous review
  version, and that the optional ethics statement sits where current rules permit.
- Enforce double-blind anonymity in PDF content, metadata, filenames, supplement, code,
  paths, URLs, and resubmission files.
- Submit supplementary material (IJCAI 2027: up to 50MB, PDF or ZIP, appendix due with the
  full paper) by the full-paper deadline; do not rely on rebuttal-time uploads.
- Confirm the per-author submission limit (IJCAI 2027: no more than 8 submissions per author
  across main and special tracks), the dual-submission policy, and whether a recent-rejection
  disclosure is still required (it was in 2026; the 2027 pages are silent) before upload.
- Apply the current LLM-use policy. For IJCAI 2027, LLMs may only polish text the authors
  wrote; LLM-generated new content is prohibited and prompt injection is forbidden.

## Blocking risks

- Missing abstract registration or missing author information.
- Overlength PDF or template manipulation.
- Identity leakage in the paper, supplement, code, data, paths, or metadata.
- Missing required resubmission information for a recent rejected version.
- Concurrent formal archival submission.
- LLM-generated paper text, hallucinated references, or unsupported claims.

## Desk-reject risk matrix

IJCAI screens a large submission volume and can reject on mechanical grounds before any
scientific review. Sort each risk by whether it is auto-fatal at intake.

| Risk | Severity | Pre-upload check |
| --- | --- | --- |
| Missing abstract registration | Fatal | Abstract filed by its earlier deadline |
| Overlength or template manipulation | Fatal | Page count and Author Kit style verified |
| Anonymity leak in PDF/metadata/code | Fatal | Names, URLs, filenames scrubbed |
| Missing resubmission file | Fatal | Anonymized rejected version attached |
| Concurrent archival submission | Fatal | No venue overlap during review |
| LLM-written manuscript text | High | Only policy-allowed polishing |

## Worked vignette: a multi-agent paper at intake

A multi-agent RL paper is ready scientifically but its anonymized PDF embeds the lab name in a
figure caption and its code ZIP keeps an institutional path. Both are anonymity leaks that can
desk-reject the paper before review. Fix order: scrub the caption and metadata, re-zip with
relative paths, confirm the page count, verify the abstract was registered on time, and confirm
no concurrent archival submission.

## Reviewer/chair pushback and the venue-specific fix

- "Exceeds the limit." Compress to the body limit and move overflow to the appendix; do not
  shrink margins, fonts, or spacing to fake compliance.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue ijcai-skills   # from a clone of the AJS repository
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

## Output format

```text
[IJCAI readiness] Ready / Needs fixes / Not ready
[Track] main / special / survey / other
[Blocking checks] <page/anonymity/authors/ORCID/supplement/resubmission/dual-submission/LLM>
[Highest desk-reject risk] <one issue>
[Fix order] <ordered fixes before submission>
```
