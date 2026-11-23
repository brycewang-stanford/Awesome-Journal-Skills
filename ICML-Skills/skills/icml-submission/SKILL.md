---
name: icml-submission
description: Use when auditing an ICML main-track submission for OpenReview, LaTeX formatting, 8-page body, anonymity, supplementary material, impact statement, dual submission, concurrent ICML submissions, reciprocal reviewing, and LLM/prompt-injection policy compliance.
---

# ICML Submission

Use this for a final ICML submission audit. ICML rules are annual; reopen the current CFP, Author
Instructions, OpenReview group, style files, example paper, FAQ, and LLM-review policy before giving
submission-ready advice.

## Submission checks

- Confirm the target is a main-track paper, not workshop, tutorial, expo, or Journal-to-Conference,
  and pick the right contribution type. In ICML 2027, position papers go through the main track as
  the "Position Papers" contribution type rather than a separate call.
- Verify OpenReview account readiness for all authors before the relevant deadline (suggested by
  January 8, 2027). ICML 2027 requires title, full author list, and complete abstract by the January
  14, 2027 abstract deadline and freezes the author list after it; full papers are due January 22,
  2027 AoE.
- Check quotas: no author on more than 20 submissions, one eligible reciprocal reviewer named per
  submission (at most 6 submissions each), and self-rankings filed by authors with multiple
  submissions.
- Check that the PDF uses the current ICML LaTeX style (`icml2027.zip`). ICML 2027 provides no
  support for non-LaTeX typesetting.
- Enforce the current main-body limit. The 2027 submission body limit is 8 pages, followed by
  references, the impact statement, and appendices in the same PDF.
- Check the 50MB PDF file-size limit and all required OpenReview fields.
- Confirm double-blind compliance in the paper, appendices, supplementary manuscripts, code/data
  ZIPs, anonymous repositories, filenames, metadata, acknowledgments, grant numbers, and links.
- Include the impact statement (before References) and the AI Disclosure Statement (end of paper);
  neither counts toward the page limit, and ICML 2027 requires both in every submission.

## ICML-specific desk-reject risks

- Main body over the page limit.
- Non-anonymized paper, appendix, code, data, repository, or supplementary manuscript.
- Missing or late abstract/full-paper submission.
- Dual submission to another archival venue at the full-paper deadline.
- Prompt injection or review-manipulation text.
- Template modifications that create unfair space.
- Reciprocal reviewer or LLM-review policy violations tied to the paper.

## Concurrent ICML submissions

Treat related submissions by overlapping author sets as prior work. If a reasonable reviewer would
expect the related paper in the related-work section, cite it anonymously, explain the difference,
and include the anonymized PDF in supplementary material.

## Pre-deadline audit sequence

Run these in order, because each later check assumes the earlier one passed.

| Order | Check | Pass condition |
| --- | --- | --- |
| 1 | Track | Main-track paper with the right contribution type, not workshop |
| 2 | LaTeX style | Current ICML template, unmodified margins |
| 3 | Page limit | Body within the 2027 8-page limit, references and appendices after |
| 4 | Anonymity | No author, repo, path, grant, or link leak in PDF or supplement |
| 5 | OpenReview fields | Code URL, contribution type, reciprocal reviewer, impact and AI Disclosure statements complete |
| 6 | Dual submission | No archival overlap at the full-paper deadline |

## Worked vignette: auditing the optimizer submission

The adaptive-optimizer paper passes track and style, but the body runs long once the proof sketch is
inlined; the fix is moving the full proof to the same-PDF appendix and keeping only the theorem in the
body. The anonymous code ZIP still contains a cluster username in a launch script, a desk-reject risk,
so it is scrubbed before upload. Re-verify the page limit, file-size cap, and policy labels against
the current CFP.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue icml-skills   # from a clone of the AJS repository
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
[Submission readiness] Ready / Needs fixes / Not ready
[Track] Main / position / workshop / other
[Blocking ICML checks] <OpenReview/LaTeX/page limit/anonymity/supplement/impact/dual-submission>
[Concurrent-submission risk] none / cite anonymously / reroute or withdraw
[Highest desk-reject risk] <one issue>
[Fix list] <ordered fixes before submission>
```

