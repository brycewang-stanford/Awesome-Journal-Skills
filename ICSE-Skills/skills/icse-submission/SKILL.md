---
name: icse-submission
description: Use when auditing an ICSE research-track submission for HotCRP readiness, covering the mandatory abstract deadline, the 10-page-plus-2-reference-page IEEE format, double-anonymous rules, the open-science Data Availability section, supplementary uploads, and desk-reject triage before the AoE cutoff.
---

# ICSE Submission

Run this audit before touching the submit button on the ICSE HotCRP site. Every
number below was read from the ICSE 2027 Research Track pages on 2026-07-08 (via
search renderings of the official `conf.researchr.org` URLs — see
`resources/official-source-map.md`); treat them as one cycle's snapshot and reopen
the live call before acting.

## The 2027-cycle mechanics

- **Two deadlines, both AoE (23:59:59, UTC-12).** The abstract deadline
  (June 23, 2026) is *mandatory* — no abstract in HotCRP by that date, no paper
  submission a week later (June 30, 2026). ICSE uses the abstract for bidding
  and PC assignment, so a placeholder abstract that drifts from the final paper
  quietly damages your reviewer match.
- **10 + 2 page format.** Main text ≤ 10 pages *inclusive of all figures, tables,
  and appendices*; up to 2 additional pages may contain **only references**.
  There is no unlimited appendix: anything reviewers must see lives inside the 10.
- **IEEE conference template, unmodified.** Title in 24pt, body in 10pt —
  `\documentclass[10pt,conference]{IEEEtran}`, without `compsoc` options. The
  call states that spacing/font alterations can mean desk rejection without review.
- **Submission site:** `icse2027.hotcrp.com`, one HotCRP instance per track.

## Double-anonymous sweep

ICSE reviews double-anonymously: the submission may not reveal author identity,
and your own prior work is cited in the third person. Because SE papers lean on
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
- If you cannot share, add a short **Data Availability** section after the
  Conclusion explaining why (industrial confidentiality, human-subjects limits).
- Sharing is not formally mandatory for acceptance — but the Verifiability and
  Transparency criterion is one of the four scored criteria, so an empty
  availability story is a scored weakness, not a neutral choice.

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Main text spills to page 11 | Desk-reject-grade | Cut content or move it to the artifact; the 2 extra pages are references-only |
| Template tampering (margins, 9.5pt body) | Explicitly named desk-reject ground | Recompile clean; recover space editorially |
| Identity leak in PDF or supplement | Anonymity violation | Re-anonymize and re-host; check PDF metadata too |
| Abstract not registered by June 23 | No submission slot exists | Nothing fixes this after AoE — calendar it now |
| No availability statement, no artifact | Scored against verifiability | Add Data Availability section + anonymized package |
| Same study under review elsewhere | Dual-submission exposure | Withdraw one venue first; verify the current policy wording |

## Final-week order of operations

1. Freeze the 10-page body early; references can churn, the body cannot.
2. Register the abstract well before June 23 with the *real* title and abstract.
3. Build the anonymized replication package and place its link in the paper.
4. Run the mechanical anonymity checks on the final PDF, not a draft.
5. Fill every HotCRP field (topics, conflicts, coauthors with correct emails)
   a day early — conflicts entered late are the classic AoE-midnight failure.
6. Re-download your submission from HotCRP and read it cold, checking that the
   PDF that uploaded is the PDF you meant.

## What the form asks that the paper does not

HotCRP topic selections drive which PC members bid on you. Choose topics that
match your *evidence*, not your ambitions: a paper tagged "machine learning for
SE" plus "human factors" gets one reviewer from each pool, and the mismatched
one writes the low score. Declare conflicts for every coauthor's institution
and recent collaborators; ICSE PCs are large, and an undeclared conflict found
later is a chair-level problem.

## IEEEtran traps that surface at upload

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
  cycles; 2027 posts one).
- Page budget and template (10+2 and IEEEtran were the 2027 numbers).
- Supplementary handling, AI-use disclosure rules, and dual-submission wording
  — all 待核实 per cycle; none should be assumed stable.

## Output format

```text
[ICSE submission status] ready / blocked / needs work
[Format] pages used (main/refs), template compliance
[Anonymity] clean / leaks: <where>
[Open science] artifact link present? availability statement present?
[HotCRP] abstract registered, topics, conflicts, coauthors
[Fix queue] <ordered, with owners and dates before June 30 AoE>
```
