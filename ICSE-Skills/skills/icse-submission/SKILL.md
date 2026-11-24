---
name: icse-submission
description: Use when auditing an ICSE research-track submission for HotCRP readiness, covering the mandatory abstract deadline, the 10-page-plus-2-reference-page ACM format, reciprocal-reviewer nomination, double-anonymous rules, the open-science Data Availability section, supplementary uploads, and desk-reject triage before the AoE cutoff.
---

# ICSE Submission

Run this audit before touching the submit button on the ICSE HotCRP site. Every
number below was read from the ICSE 2028 Research Track call on 2026-11-24 (direct
fetch of the official `conf.researchr.org` pages — see
`resources/official-source-map.md`); treat them as one cycle's snapshot and reopen
the live call before acting.

## The 2028-cycle mechanics

- **Two deadlines, both AoE (23:59:59, UTC-12).** The abstract deadline
  (June 24, 2027) is *mandatory* — no abstract in HotCRP by that date, no paper
  submission a week later (July 1, 2027). ICSE 2028 has **no bidding phase**:
  assignments are generated automatically from expertise, subject areas and
  conflicts, so a placeholder abstract or a wrong area choice that drifts from
  the final paper quietly damages your reviewer match.
- **Reciprocal reviewer (new in 2028).** Each submission must nominate one
  qualified potential reviewer; area chairs decide whether the nominee joins
  the PC. Eligibility details are promised in the submission instructions
  (待核实).
- **10 + 2 page format.** Main text ≤ 10 pages *inclusive of all figures, tables,
  and appendices*; up to 2 additional pages may contain **only references**.
  There is no unlimited appendix: anything reviewers must see lives inside the 10.
- **ACM Primary Article Template, unmodified.** LaTeX users use `sigconf` with
  the `review` (line numbers) and `anonymous` options —
  `\documentclass[sigconf,review,anonymous]{acmart}`. ICSE 2027 used IEEEtran,
  so do not reuse last year's skeleton. The call states that spacing/font
  alterations can mean desk rejection without review.
- **Reference integrity.** Submissions are checked for hallucinated, fabricated
  or unverifiable references; confirmed cases are desk-rejected without review.
- **Generative AI.** AI cannot be an author; AI-generated content is disclosed
  in the Acknowledgements; Grammarly-style editing need not be disclosed.
- **Human participants.** You declare compliance with the ACM policy on
  research involving human participants when you submit.
- **Submission site:** a dedicated HotCRP site, "available soon" at check time
  (the 2027 site was `icse2027.hotcrp.com`; one HotCRP instance per track).

## Double-anonymous sweep

ICSE reviews double-anonymously: the submission may not reveal author identity,
your own prior work is cited in the third person, and company and institution
names are anonymized too (the 2028 Q&A). Preprints are allowed but must not
say the work is under submission to ICSE; the call recommends waiting until
after notification. Because SE papers lean on
tools and repositories, the leak surface is wider than the author block:

```bash
# Mechanical pass on the submission PDF and any supplementary archive
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'github\.com/[a-z0-9-]+|gitlab|zenodo\.org/record|acknowledg|grant' | head
unzip -l supplement.zip | grep -Ei '\.git/|\.DS_Store|/home/|/Users/' | head
grep -rn "university\|@.*\.edu" supplement/ --include='*.md' | head
```

The SE-specific leaks: a tool named after your lab, screenshots showing a
username, a replication link pointing at a personal GitHub, commit metadata
inside a zipped repository, and issue-tracker URLs in the evaluation section.
Re-host artifacts behind an anonymizing service before upload, not after.

## Open science at submission time

The research track is governed by the ICSE Open Science policy: sharing is the
expected default, and *non*-sharing is what needs justification. Concretely for
the submission:

- Provide anonymized links to data/repositories, or upload anonymized material
  through HotCRP's supplementary option.
- State in the paper how reviewers access the artifact. If you cannot share,
  explain why in both the submission form and the paper (industrial
  confidentiality, human-subjects limits); ICSE 2027 asked for a **Data
  Availability** section after the Conclusion, and the 2028 Open Science page
  is not yet posted (待核实), so keep that section.
- Sharing is not formally mandatory for acceptance — but the Verifiability and
  Transparency criterion is one of the five scored criteria and one reviewer
  checks any attached or linked artifact, so an empty
  availability story is a scored weakness, not a neutral choice.

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Main text spills to page 11 | Desk-reject-grade | Cut content or move it to the artifact; the 2 extra pages are references-only |
| Template tampering (margins, 9.5pt body) | Explicitly named desk-reject ground | Recompile clean; recover space editorially |
| Identity leak in PDF or supplement | Anonymity violation | Re-anonymize and re-host; check PDF metadata too |
| Abstract not registered by June 24 | No submission slot exists | Nothing fixes this after AoE — calendar it now |
| No reciprocal reviewer nominated | Incomplete submission | Agree the nominee with a qualified colleague before June |
| A cited work cannot be traced | Explicitly named desk-reject ground | Check every reference against DBLP/DOI before upload |
| No availability statement, no artifact | Scored against verifiability | Add Data Availability section + anonymized package |
| Same study under review elsewhere | Dual-submission exposure | Withdraw one venue first; verify the current policy wording |

## Final-week order of operations

1. Freeze the 10-page body early; references can churn, the body cannot.
2. Register the abstract well before June 24 with the *real* title, abstract,
   area choice, and reciprocal-reviewer nominee.
3. Build the anonymized replication package and place its link in the paper.
4. Run the mechanical anonymity checks on the final PDF, not a draft.
5. Fill every HotCRP field (topics, conflicts, coauthors with correct emails)
   a day early — conflicts entered late are the classic AoE-midnight failure.
6. Re-download your submission from HotCRP and read it cold, checking that the
   PDF that uploaded is the PDF you meant.

## What the form asks that the paper does not

The area and topic selections drive the automatic reviewer assignment (2028
has no bidding). Choose topics that match your *evidence*, not your ambitions: a paper tagged "machine learning for
SE" plus "human factors" gets one reviewer from each pool, and the mismatched
one writes the low score. Declare conflicts for every coauthor's institution
and recent collaborators; ICSE PCs are large, and an undeclared conflict found
later is a chair-level problem.

## Template traps that surface at upload

Three template failures recur in SE submissions specifically: bibliography
styles that silently exceed the reference pages when dblp entries carry long
venue strings (abbreviate via the `.bib`, not by shrinking the font);
`listings`/`minted` code blocks whose captured line widths overflow the
column and get "fixed" with negative `\hspace` — a tampering signal; and
figures exported from dashboards at screen resolution that balloon the PDF
and blur in print. Budget a compile-and-print test on the true template a
week out, because each of these costs hours exactly when you have none.

## Reverify each cycle

- Deadlines and whether the cycle count changes again (2025–2026 ran two
  cycles; 2027 and 2028 post one).
- Page budget and template (10+2 in both years; IEEEtran in 2027, ACM `sigconf`
  in 2028).
- Supplementary handling, reciprocal-reviewer rules, AI-use disclosure, and
  dual-submission wording — re-read per cycle; none should be assumed stable.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue icse-skills   # from a clone of the AJS repository
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
[ICSE submission status] ready / blocked / needs work
[Format] pages used (main/refs), template compliance
[Anonymity] clean / leaks: <where>
[Open science] artifact link present? availability statement present?
[HotCRP] abstract registered, area/topics, reciprocal reviewer, conflicts, coauthors
[Fix queue] <ordered, with owners and dates before July 1 AoE>
```
