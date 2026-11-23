---
name: cvpr-submission
description: Use when auditing a CVPR submission before the OpenReview deadline, covering paper registration, profile and enrollment requirements, submission and reciprocal-reviewer quotas, the 8-page limit including figures and tables, the mandatory LLM Usage Statement, anonymity and external-link bans, dual-submission attestations, reviewer-duty enrollment, and desk-reject triage.
---

# CVPR Submission

Run this audit in the two weeks before the CVPR paper deadline. All specifics below are
the CVPR 2027 cycle as re-read on 2026-11-24 (paper deadline November 16, 2026; CVPR 2026
values are marked as history); the next Program Chairs will rewrite details, so reopen
the current Author Guidelines and Dates pages at cvpr.thecvf.com before acting on any
number here.

## The three deadlines that catch people

CVPR staggers three hard cut-offs a week apart, and the first one is the one teams miss:

1. **Paper registration (abstract) + OpenReview profiles and enrollment** (Nov 10, 2026
   for CVPR 2027; Nov 6, 2025 in the 2026 cycle). Every listed author — including the
   advisor added "later" and the intern who wrote one module — needs a complete
   OpenReview profile and a completed author enrollment (which now includes the
   data-use and AI-processing consent) by this date. Authors cannot be added or removed
   afterwards; an incomplete coauthor is desk-reject exposure for the paper.
2. **Full paper** (Nov 16, 2026, AoE, fixed; Nov 13, 2025 in 2026). The PDF — including
   the mandatory **LLM Usage Statement** — lands here, and the author order becomes final.
3. **Supplementary material** (Nov 23, 2026, AoE; Nov 20, 2025 in 2026). One extra week —
   but only for the supplement; nothing in the main PDF can change after the paper
   deadline.

## Quotas (new for CVPR 2027)

- At most **25 submissions per author**; excess papers are desk-rejected from the highest
  paper IDs unless the author withdraws some first.
- At most **one submission per author on which no author is an eligible reciprocal
  reviewer** — someone with an accepted main-track paper (or full journal article) at a
  listed CV/ML/robotics/graphics/NLP venue by the abstract deadline, as shown on their
  OpenReview profile (import DBLP papers; a DBLP link alone does not count).

## Page discipline, CVPR flavor

The cap is **8 pages including figures and tables**, with extra pages permitted only for
cited references and the mandatory LLM Usage Statement. That "including figures" clause is what distinguishes CVPR budgeting
from text-limited venues: a half-page teaser figure, two qualitative grids, and three
result tables can consume four of your eight pages. Plan figures as page-budget line
items, not decorations, and treat any style-file edit, margin nudge, or font substitution
as a desk-reject trigger — over-length and mis-formatted papers are rejected without
review. Build from the official CVPR 2027 Submission Template
(`author-kit-CVPR2027-v1-latex.zip`, linked from the Author Guidelines; the kit also lives
at `github.com/cvpr-org/author-kit`), unmodified.

## The LLM Usage Statement (new for CVPR 2027)

Every submission must contain a section titled **"LLM Usage Statement"** after the main
text and before the references. It does not count toward the page limit, must stay
anonymous, and must (a) disclose any use of LLMs or other generative-AI tools in the
research or the writing — editing and grammar included; (b) name the tools, the affected
parts (text, figures, code, experiments, related work, ideation) and the extent; or (c)
state "No LLMs or generative AI tools were used in this work". A missing statement is a
desk reject; an incomplete one can mean desk rejection or an ethics referral. Disclosure
is not itself a review factor. If naming an in-house tool would break anonymity, describe
it generically and name it at camera-ready, where AI use moves to the Acknowledgements.

Related 2027 facts: conference-approved LLM tools in OpenReview process every submission
during review (no paper-level opt-out), and hidden prompt injection is a desk reject.

## The Compute Reporting Form (2026 only)

The 2026 cycle attached a Compute Reporting Form to every submission (Sections 1 and 5
mandatory, documented opt-out). The CVPR 2027 CFP and Author Guidelines do not mention
it; do not tell a 2027 team it is required unless the OpenReview form asks for it. Keep
the hardware and GPU-hour ledger anyway — reviewers still probe efficiency claims.

## Anonymity and the external-link ban

CVPR is double-blind with two venue-specific wrinkles. First, **arXiv posting is not an
anonymity violation** — you may have a preprint up, and reviewers are told not to hunt
for it. Second, **external links are banned when they expand content or subvert
review**: an anonymous-looking project page, a Google Drive of extra results, or a demo
URL can breach anonymity, the media embargo, or the length limit all at once. Everything
reviewers need must live in the PDF and the uploaded supplement.

```bash
# Mechanical sweep on the final build, ten minutes before upload
pdftotext paper.pdf - | grep -nEi 'github\.com|drive\.google|project page|our (prior|previous) work' | head
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'     # identity in metadata
grep -rn 'vspace\|\\addtolength\|geometry' main.tex        # style-tampering tells
pdftotext paper.pdf - | awk 'END{print NR" lines extracted"}'   # sanity: text present, not raster
```

## Dual submission and the media embargo

By submitting you attest that no substantially similar paper (20 percent or more
overlap) is under review at another conference, workshop or journal **during the defined
review period** (Nov 16, 2026 – Feb 22, 2027 for CVPR 2027; Nov 13, 2025 – Feb 20, 2026
in the 2026 cycle). Verified carve-outs: a "publication" is a peer-reviewed work **longer
than four pages** (excluding references), so shorter prior papers do not trigger the
rule; arXiv preprints, technical reports and GitHub documents are not publications. Separately, papers under
review are embargoed from proactive media discussion until acceptance — a violation can
remove the paper from the proceedings. A journalist writing about your arXiv preprint
without your involvement is not a violation; you pitching the story is.

## Reviewer duty is part of submitting

All authors are added to the reviewer pool unless exempted in advance. This is not
symbolic: papers authored by a reviewer who blows review deadlines, files highly
irresponsible reviews, or uploads submissions to an external LLM can be
**desk-rejected wholesale**. Before the deadline, decide which
coauthors will absorb December–January reviewing load and calendar it.

## Desk-reject triage

| Finding | Severity | Recoverable? |
|---|---|---|
| Coauthor without a complete OpenReview profile/enrollment at abstract deadline | Desk reject | Only before Nov 10, 2026 |
| More than 25 papers, or >1 paper without an eligible reciprocal reviewer | Desk reject (highest IDs) | Withdraw by the PCs' deadline |
| Page 9 contains anything besides references and the LLM Usage Statement | Rejected without review | Only before the paper deadline |
| LLM Usage Statement missing | Desk reject | Add it before the paper deadline |
| Prompt injection or fabricated citation | Desk reject + possible sanctions | Remove before upload |
| Style file modified / margins compressed | Rejected without review | Fix and rebuild |
| Identity leak (metadata, acknowledgements, linked repo) | Desk reject | Sweep before upload |
| External link expanding content | Policy violation | Delete; move content into supplement |
| Same work under review elsewhere in the window | Administrative rejection | Withdraw one venue first |
| Assigned coauthor review never delivered (January) | All their papers at risk | Deliver the reviews |

## OpenReview form fields worth drafting early

The PDF gets the rehearsals; the form causes the midnight surprises. Draft these a day
ahead: the abstract field (verbatim from the PDF — reviewers bid on it), subject areas
(chosen for reviewer routing, not maximal coverage), conflicts (every coauthor's
domain conflicts, checked against the institution list), and the author order (frozen —
post-deadline author changes are a chairs-level exception, not an edit).

## Final 72 hours, in order

1. Freeze the 8-page body; late edits go to the supplement queue, not the PDF.
2. Rebuild from a clean checkout of the official kit and verify no local style patches
   leaked in.
3. Run the mechanical sweep above; treat every hit as a blocker.
4. Complete the OpenReview form fields a full day early and confirm the LLM Usage
   Statement is in the PDF; the abstract field must match the PDF verbatim because
   reviewers bid on it.
5. Upload, re-download, and read your own submission cold — including checking that
   figures render at print zoom, since reviewers judge qualitative results visually.

## Reverify each cycle

- All three deadlines and whether abstract registration exists in the current cycle.
- The page cap and whether references-only extra pages still apply.
- LLM Usage Statement wording and placement; whether any compute form returns.
- Submission and reciprocal-reviewer quotas and the eligible-venue list.
- Dual-submission window definition and the >4-page publication definition.
- Supplementary size/format caps (none stated for 2027 — 待核实).

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue cvpr-skills   # from a clone of the AJS repository
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
[CVPR submission] ready / blocked / at-risk
[Profiles] all coauthors valid on OpenReview: yes/no
[Format] pages used (of 8 incl. figures/tables) · refs + LLM statement overflow only
[LLM Usage Statement] present, anonymous, complete: yes/no
[Quotas] ≤25 per author; reciprocal-reviewer eligibility on every paper: yes/no
[Anonymity/links] clean / violations: <list>
[Duty plan] reviewing coauthors named: yes/no
[Fix queue] <ordered blockers>
```
