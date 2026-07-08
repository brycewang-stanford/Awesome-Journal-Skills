---
name: soda-submission
description: Use when preparing or auditing a SODA (ACM-SIAM Symposium on Discrete Algorithms) submission — the no-page-limit full-version norm, the title-page abstract, 11-point single-column letter format, lightweight double-blind rules, HotCRP entry, and the July AoE deadline with its summary-rejection triggers.
---

# SODA Submission

Anchor cycle: SODA 2027, the ACM-SIAM Symposium on Discrete Algorithms in
Philadelphia, January 24-27, 2027, jointly sponsored by the SIAM Activity Group on
Discrete Mathematics and ACM SIGACT. Facts below were checked 2026-07-08 against the
SIAM SODA27 submission page (read via search rendering; `siam.org` refused direct
fetches) and `soda27.hotcrp.com`. The 2027 paper deadline is **July 9, 2026,
anywhere on Earth** — if you are reading this in early July 2026, the clock is
already inside the final week. Re-verify every number on the live SIAM page for any
later cycle.

## Submit the full version — SODA means it

SODA imposes **no page limit** and the CFP encourages authors to submit the full
version of the paper. This inverts the instinct trained by page-capped venues:

- Do not amputate proofs to look "conference-length." A SODA submission missing a
  proof invites the referee to assume the gap is real.
- The document still needs an act structure. Committee members triage hundreds of
  submissions; the ones they champion make the result and the technique graspable
  before page 5, with the complete proofs behind that front matter.
- The title page carries the title plus an abstract of one to two paragraphs
  summarizing the contributions — this abstract is the bidding surface for the PC,
  so it must state the theorem, the prior bound it beats, and the new idea.

## Format floor (2027 wording)

Typeset in 11-point or larger font, single column, single-spaced between lines with
ample spacing throughout, 1-inch margins on all sides, letter-size (8.5 x 11 inch)
paper. The CFP warns that a submission deviating from the guidelines "risks summary
rejection without consideration of its merits." A compliant skeleton:

```latex
\documentclass[11pt,letterpaper]{article}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsthm,thm-restate}
% Lightweight double-blind: omit \author entirely; keep all citations intact.
\title{Faster Algorithms for X via Y}
\date{}
\begin{document}
\maketitle
\begin{abstract}
One to two paragraphs: problem, prior bound, new bound, technique.
\end{abstract}
% Sections 1-3: result, technique overview, comparison to prior bounds.
% Remainder: full proofs. No page limit; completeness is expected.
\end{document}
```

## Lightweight double-blind, SODA flavor

The 2027 cycle uses what the CFP calls a fairly lightweight double-blind process.
The operational rules differ from heavyweight-anonymity venues and getting the
flavor wrong hurts in both directions:

| Rule | What it means in practice |
|---|---|
| No author names, affiliations, or emails on or in the submission | Delete the author block; scrub `\thanks`, grant lines, and PDF metadata |
| Dissemination stays free | Posting to arXiv, giving talks, and circulating drafts are all explicitly permitted |
| Important references must not be omitted or anonymized | Cite your own prior work normally, in third person — hiding it is the violation |
| Anonymity is best-effort, not forensic | Reviewers who recognize the arXiv version are not a policy problem; a signed PDF is |

Sweep before upload: `pdfinfo paper.pdf` for metadata, acknowledgements section
removed, self-references rewritten from "we showed in [7]" to "as shown in [7]."

## Prior and concurrent work constraints

Submissions must be original: not previously published and not simultaneously under
review at another conference with published proceedings or a journal. arXiv posting
does not count as prior publication. The dangerous overlap cases for an algorithms
group are ESA, ICALP, STOC, and FOCS windows — a paper still alive at one of these
when SODA's deadline closes is a dual submission (exact 2027 policy wording: 待核实
against the live CFP before relying on edge cases).

## HotCRP mechanics

- Site: `soda27.hotcrp.com`. Create the record days early; first-time HotCRP
  accounts, conflict-of-interest entry, and topic tagging consume an evening.
- The form's title and abstract must match the PDF's title page; the form abstract
  is what PC members see first while bidding.
- Declare conflicts against the PC honestly and completely — the algorithms
  community is small, and an undeclared advisor relationship is an integrity flag.
- Upload, then download the stored PDF and re-open it. Confirm the compile you
  intended is the compile they have.

## The final 48 hours, hour-ordered

AoE means the deadline passes only when July 9 ends at UTC-12 — but treating
that as slack is how groups discover HotCRP outages at the worst moment.

1. **T-48h:** freeze mathematics. Any theorem edit after this point requires
   re-running the drift check in `soda-reproducibility`.
2. **T-36h:** compile the candidate PDF; run the mechanical audits below.
3. **T-24h:** upload a complete draft to HotCRP. From here on, every improvement
   is a *re-upload*, never a first upload.
4. **T-12h:** least-involved coauthor reads title page + overview cold and
   states the headline bound back to you. Mismatch means the abstract fails.
5. **T-2h:** final re-upload; download the stored PDF; page through it.

Mechanical audit commands worth scripting once per group:

```bash
pdfinfo paper.pdf | grep -iE 'author|title|producer'   # metadata leaks
pdffonts paper.pdf | awk 'NR>2 && $5=="no"'            # unembedded fonts
pdftotext paper.pdf - | grep -inE 'full version|supplementary|anonym'
pdftotext paper.pdf - | grep -inE 'acknowledg|grant no|we thank'
```

Each grep hit is either a leftover from another venue's template or an
anonymity leak; both are five-minute fixes at T-36h and unfixable at T+1.

## Failure triage

| Failure | Consequence | Recoverable after July 9? |
|---|---|---|
| Missed AoE deadline | No submission; next stop STOC (November) or wait a year | No |
| Two-column or 10-point formatting | Summary-rejection risk per CFP | No |
| Author names in PDF or metadata | Double-blind violation, chair discretion | No |
| Key lemma unproved "for space" | Reviewers treat the result as unestablished | No — there was no space constraint to blame |
| Abstract oversells vs. theorem | Credibility damage during rebuttal | Partially, in the September response |

## Output format

```text
[SODA readiness] Ready / Needs fixes / Not ready
[Format audit] <font/column/margins/title-page findings>
[Anonymity audit] <names, metadata, self-citation phrasing>
[Completeness audit] <unproved claims, missing comparisons>
[HotCRP audit] <record, conflicts, form-PDF mismatches>
[Fix order] <ranked actions before the AoE cutoff>
```
