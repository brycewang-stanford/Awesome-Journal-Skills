---
name: eurosys-submission
description: Use when auditing a EuroSys submission before a HotCRP upload — abstract registration versus full-paper gates, the 12-page technical-content budget with free references, the SIGPLAN (acmart sigplan review/anonymous) template and text block, the three-papers-per-author-per-round cap, double-blind hygiene, the arXiv title/system-name rule, and the AI-use disclosure that ACM's authorship policy requires.
---

# EuroSys Submission

Run this audit before touching the round's HotCRP instance. Anchors below are the
EuroSys 2027 cycle as re-verified on 2026-11-24 from `2027.eurosys.org/cfp.html` and the
`eurosys27-spring` / `eurosys27-fall` HotCRP sites. EuroSys reissues its CFP per
edition and per round, so the live CFP always outranks this file.

## The two gates of a round

Each EuroSys round opens with abstract registration one week before the paper
deadline. Registration is where the title, abstract, author list, topics, and
conflicts become fixed inputs to reviewer assignment; the paper upload a week later
only swaps in the PDF.

| 2027 fall round item | Value (re-verified 2026-11-24) |
|---|---|
| Abstract registration | September 17, 2026, AoE |
| Full paper | September 24, 2026, AoE |
| Portal | `eurosys27-fall.hotcrp.com` |
| Reviews / author responses due | January 6 / January 8, 2027 |
| Notification | January 29, 2027 |
| Camera-ready | March 5, 2027 |

Both EuroSys 2027 rounds have closed (spring: papers May 14, 2026; fall: papers
September 24, 2026). As of 2026-11-24 no EuroSys 2028 call is published, so a new
paper's next gate has no official date yet — re-open the EuroSys site rather than
projecting the 2027 calendar forward.

## Length and layout rules

- **12 pages of technical content, maximum.** References ride free — as many pages
  as needed. Do not starve the bibliography to rescue a figure.
- Paper size A4 or US letter, with every character and figure inside a
  **178 x 229 mm (7 x 9 in) block**, two columns separated by at least 8 mm.
- Text, figures and captions at **≥10-point** font on **≥12-point** leading; figures
  readable in grayscale; pages numbered.
- The CFP encourages the **SIGPLAN** LaTeX or MS Word templates. In LaTeX that is
  `acmart` with the `sigplan` option, in review mode:

```latex
\documentclass[sigplan,twocolumn,review,anonymous]{acmart}
% Use the paper ID issued at abstract registration, not author names:
\acmSubmissionID{123}
```

- **At most three submissions per author per round**; a paper that pushes an author
  over the cap may be rejected without review.
- **Supplementary material** (proofs, additional results) may be uploaded as a
  separate file, but reading it is optional for reviewers — the paper must stand alone.

## Anonymity as EuroSys defines it

The standard asked for is a good-faith effort, judged by whether identity leaks
"explicitly or by implication":

- No names, affiliations, acknowledgments, or grant IDs anywhere in the PDF.
- Third-person self-citation; never "as we showed in [7]".
- Scrub PDF metadata and embedded file properties before upload.
- If the paper describes a deployment only your organization runs, abstract the
  operator without inventing data.
- Linked repositories must be anonymized mirrors, not lab GitHub accounts.
- Related work of yours that is **under review elsewhere** is cited anonymously, its
  difference explained, and a copy emailed to the PC chairs.
- An arXiv version, tech report, talk or social-media post is fine, but the submission
  must use a **substantially different title and system/tool name**.
- A prior or concurrent **workshop paper** on the topic is uploaded in the submission
  form with a short explanation of the new material.

## Pre-upload checklist

| Check | Pass condition |
|---|---|
| Abstract registered on time | HotCRP entry exists before the abstract gate |
| Page budget | ≤ 12 pages before the references begin |
| Text block | Nothing outside 178 x 229 mm; column gap ≥ 8 mm |
| Template mode | `review,anonymous` options active; paper ID on page 1 |
| Identity sweep | Metadata, acknowledgments, self-citations, repo links clean |
| Dual submission | Not concurrently under review at another archival venue |
| Resubmission legality | Not rejected at the immediately preceding EuroSys cycle |
| Author cap | No author on more than three submissions this round |
| AI disclosure | Any use of AI tools fully disclosed in the submission (ACM authorship policy) |
| Topics and conflicts | Complete in HotCRP, since assignment runs off them |

That resubmission row is EuroSys-specific: a paper not accepted in one cycle is not
eligible for the immediately following cycle — in practice it returns no earlier than
the same round of the next edition, so confirm the manuscript's
EuroSys history before registering it (see `eurosys-review-process`).

## Habits imported from other venues that break here

- **From USENIX venues:** expecting a single-column submission format or an
  appendix allowance — EuroSys reviews in the two-column ACM layout, and extra
  material goes in a separate supplementary file that reviewers may skip.
- **From NeurIPS-style venues:** expecting a checklist to carry the
  reproducibility story — EuroSys has no checklist ritual; the evidence
  discipline lives in the paper and the artifact instead.
- **From journals:** expecting to update the manuscript during review —
  between the paper gate and notification the PDF is frozen; plan the
  submission as final, not as an opening bid.
- **From single-deadline conferences:** treating the abstract gate as
  optional paperwork — at EuroSys it fixes reviewer bidding inputs, and a
  sloppy registered abstract buys mismatched reviewers.

## HotCRP field audit

The PDF is half the submission; the form is the other half.

- Title and abstract in HotCRP must match the PDF exactly — divergence
  confuses bidding and looks careless at PC time.
- Topic selections drive assignment within a broad PC; choose the two or
  three that name the paper's jury, not every topic it touches.
- Conflicts: declare per the CFP's definition, comprehensively, once —
  chairs audit both missing and padded conflict lists.
- Author list completeness at registration matters even though reviewers
  never see it: it is the basis of conflict screening.
- Any round-specific questions (artifact intent, ethics statements, AI-use
  disclosure, workshop-paper upload) get real answers, not placeholders.

## Last-72-hours order of operations

1. Freeze the evaluation numbers; regenerate every plot from the frozen data.
2. Rebuild with the review-mode template and re-check the page count — review mode
   and camera mode paginate differently.
3. Run the identity sweep on the final PDF, not on an earlier draft.
4. Register the abstract early; HotCRP lets you refine the PDF until the paper gate.
5. Re-open the CFP once more: EuroSys rounds occasionally adjust rules mid-cycle.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue eurosys-skills   # from a clone of the AJS repository
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
[EuroSys gate] next open round per the live CFP (both 2027 rounds closed as of 2026-11-24)
[Readiness] upload-ready / fixable / blocked
[Format findings] <page budget / text block / template / paper ID>
[Anonymity findings] <leak locations or clean>
[Policy findings] <dual submission / resubmission ban / conflicts>
[Ordered fixes] <what to do before the abstract and paper gates>
```
