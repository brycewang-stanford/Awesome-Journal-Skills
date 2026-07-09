---
name: sigcomm-submission
description: Use when running the final pre-upload audit of an ACM SIGCOMM submission — the abstract-registration-then-paper sequence on the SIGCOMM HotCRP site, the AoE deadline clock, the 12 single-spaced pre-reference pages including figures and tables, double-blind anonymization, ACM acmart formatting, and the research-versus-experience track choice.
---

# SIGCOMM Submission

SIGCOMM gives you one main-track deadline a year, so this audit is unforgiving by design.
Reopen the current CFP, submission page, and the HotCRP `/deadlines` clock before trusting
any number below; the 2026 figures are a dated snapshot.

## Register the abstract, then upload the paper

SIGCOMM 2026 opened abstract registration on **January 30, 2026** and full-paper upload on
**February 6, 2026**, both **Anywhere on Earth**. The abstract step is a gate, not a
courtesy: no registered abstract, no paper a week later. Register the title, author list,
conflicts, and topics even at 60% confidence — a registered abstract can be abandoned, an
unregistered one cannot be resurrected once the clock closes. Because there is no second
gate this cycle, treat the AoE cutoff as the true horizon and convert each coauthor's local
time from the HotCRP page rather than memory.

## Pick the track before you audit the format

The two lanes are judged by different contracts, and choosing wrong wastes the whole year:

- **Research track** — a networking-stack mechanism or architecture judged on novelty,
  design insight, and evaluation depth.
- **Experience track** — an operational or deployment result judged on generalizable
  lessons from real operation; a research-novelty rubric will undervalue it, and a product
  narrative dressed as research will fail the novelty bar.

## Format audit

| Item | SIGCOMM 2026 rule | Audit action on the compiled PDF |
|---|---|---|
| Body | ≤ 12 single-spaced pages **before references**, including figures and tables | Count pages up to the references; over-length is not reviewed |
| References | as many pages as needed, outside the cap | Confirm nothing load-bearing hides there |
| Appendices | optional, after references, outside the cap | Body must stand without them (a shepherd later judges necessity) |
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
reviewer profile you want, not maximal coverage. Enter the full author list at abstract time
for conflict computation even though the PDF stays blind, and declare conflicts by the
site's definitions — completely and no wider than defined.

## Final sequence

1. T-8 days: HotCRP account, abstract fields drafted, conflicts entered, track chosen.
2. T-7 (Jan 30): abstract registered; topics and track locked deliberately.
3. T-2: content freeze; format and blindness audits on the near-final PDF.
4. T-1: coauthor sign-off; HotCRP title/abstract verbatim-match the PDF.
5. T-0 (Feb 6, AoE): upload, mark the submission complete, then re-download and read the
   uploaded bytes — the submitted file, not the local copy, is what reviewers see.

## Output format

```text
[Clock] HotCRP site + AoE cutoffs confirmed from /deadlines
[Track] research / experience — matches the evidence
[Format] 12-page pre-reference / template / references / appendix — pass or blocker
[Blindness] mechanical findings + human-pass verdict
[HotCRP fields] title/abstract verbatim match, topics, conflicts — cleared or flagged
[Blockers] ordered, with owner and time cost
```
