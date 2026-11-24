---
name: sigcomm-submission
description: Use when running the final pre-upload audit of an ACM SIGCOMM submission — the single February deadline on the SIGCOMM HotCRP site, the 12 single-spaced pre-reference pages including figures and tables, the 200-word abstract and author-block page counts, double-blind anonymization, ACM acmart formatting, the submission-form fields (track, ethics, reciprocal reviewer, ORCID), and the research-versus-experience track choice.
---

# SIGCOMM Submission

SIGCOMM gives you one main-track deadline a year, so this audit is unforgiving by design.
Reopen the current CFP, submission page, and the HotCRP `/deadlines` clock before trusting
any number below; the SIGCOMM 2027 figures are a dated snapshot (re-verified 2026-11-24).

## One hard deadline — read the clock on HotCRP

SIGCOMM 2027 publishes **one** paper deadline, **February 2, 2027**, "a hard deadline and no
extensions will be given". Unlike SIGCOMM 2026 (abstracts January 30, papers February 6, 2026,
AoE), the 2027 pages announce no separate abstract-registration date and no time zone; the
`sigcomm27.hotcrp.com` site was not yet open on 2026-11-24. When it opens, read its
`/deadlines` page for the exact cutoff and any registration step, and convert each coauthor's
local time from that page rather than memory. Start the HotCRP record early anyway: the form
asks for the track, topics, an ethics description, PC conflicts, ORCIDs and a named
**reciprocal reviewer** (an author, normally holding a PhD, who may be asked to review as many
papers as they submitted). Each author may appear on at most **eight** submissions across both
tracks; surplus papers are desk-rejected.

## Pick the track before you audit the format

The two lanes are judged by different contracts, and choosing wrong wastes the whole year:

- **Research track** — a networking-stack mechanism or architecture judged on novelty,
  design insight, and evaluation depth.
- **Experience track** — insights from deploying or operating a design, judged in 2027 on the
  **depth of the lessons learned**, not on the size or duration of the deployment; the title
  must begin with **"Experience:"** and the track is declared on the form. A product narrative
  without supported lessons fails this bar.

Either way, SIGCOMM 2027 adds a **general-accessibility** test: the PC will reject a paper
whose motivation or approach most networking researchers would not understand.

## Format audit

| Item | SIGCOMM 2027 rule | Audit action on the compiled PDF |
|---|---|---|
| Body | ≤ 12 single-spaced pages **before references**, including figures and tables | Count pages up to the references; over-length is not reviewed |
| References | as many pages as needed, outside the cap | Confirm nothing load-bearing hides there |
| Appendices | optional, after references, outside the cap; reviewers need not read them | Body must stand without them; no main-body claim may depend on an appendix experiment |
| Author block | "Paper #N, 12 pages body, 14 pages total"-style line under the title | Fill in the HotCRP number and the real counts |
| Abstract | no more than 200 words | Count words; paste the same text into HotCRP |
| Layout | Letter, two-column, 10-point or larger, at most 55 lines per column, numbered pages | Run Banal (the HotCRP checker) before upload |
| File | PDF only, under 15 MB | Embed fonts; check legibility of plot labels |
| Template | ACM `acmart.cls` (or ACM Word), unmodified | Diff class options against the distributed file |
| Track | research / experience | Matches the evidence actually in the paper |

The page cap at SIGCOMM is figure pressure — figures and tables count against the 12 pages.
The remedy is content triage, never margin, spacing, or font surgery; the ACM production
path and reviewers both notice geometry games.

## Double-blind sweep

Author identity must be absent from the PDF text, plots, captions, metadata, and any linked
artifact or repository. Self-citations stay in the third person, and references are never
dropped to preserve anonymity. Measurement papers leak identity through the deployment more
than the byline: a "our production backbone" trace plus a topology detail and an author
count can triangulate to one operator, so neutralize to scale-descriptive language.
The SIGCOMM 2027 instructions make one exception: an **experience-track** paper may name the
company or system, but never the authors.

```text
# Mechanical pass on the exact upload candidate (adapt tool names as available)
pdftotext paper.pdf - | grep -niE '(acknowledg|funded by|grant no|@[a-z]+\.(edu|com))'
pdfinfo paper.pdf   | grep -iE 'author|creator'          # metadata identity leak
grep -rniE '(github\.com/[a-z0-9_-]+|/home/|/Users/)' *.tex figures/
# then a human pass: a non-author reads the PDF asking only "who wrote this?"
```

Mechanical passes catch strings; only a human catches implication.

## HotCRP fields are reviewed before the PDF

Title and abstract must match the PDF verbatim — drift confuses bidding and reads as
carelessness. Topic selections steer the paper toward a sub-community; choose for the
reviewer profile you want, not maximal coverage. Enter the full author list at registration time
for conflict computation even though the PDF stays blind, and declare conflicts by the
site's definitions — completely and no wider than defined.

## Final sequence

1. T-8 days: HotCRP account and record started once the site opens; ORCIDs collected;
   reciprocal reviewer named; conflicts entered; track chosen.
2. T-7: any registration step HotCRP announces completed; topics, ethics text and track
   locked deliberately.
3. T-2: content freeze; format (Banal), abstract-length and blindness audits on the
   near-final PDF.
4. T-1: coauthor sign-off; HotCRP title/abstract verbatim-match the PDF; author-block page
   counts correct.
5. T-0 (February 2, 2027, at the cutoff HotCRP states): upload, mark the submission complete,
   then re-download and read the uploaded bytes — the submitted file, not the local copy, is
   what reviewers see.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue sigcomm-skills   # from a clone of the AJS repository
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
[Clock] HotCRP site + cutoff and time zone confirmed from /deadlines
[Track] research / experience — matches the evidence
[Format] 12-page pre-reference / 200-word abstract / author block / template / 15 MB — pass or blocker
[Form] ORCIDs / reciprocal reviewer / ethics text / ≤8 papers per author — done or missing
[Blindness] mechanical findings + human-pass verdict
[HotCRP fields] title/abstract verbatim match, topics, conflicts — cleared or flagged
[Blockers] ordered, with owner and time cost
```
