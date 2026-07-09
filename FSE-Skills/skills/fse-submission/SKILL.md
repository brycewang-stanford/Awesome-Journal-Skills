---
name: fse-submission
description: Use when auditing an ESEC/FSE research-track submission for HotCRP readiness, covering the mandatory paper-registration step, the ACM Primary Article Template page budget, double-anonymous "heavy" anonymity, the open-science Data Availability statement, PACMSE publication, and desk-reject triage before the AoE cutoff.
---

# FSE Submission

Run this audit before uploading to the FSE HotCRP site. FSE research papers are published as
**journal articles in PACMSE** (Proceedings of the ACM on Software Engineering), so the
submission is judged like a journal manuscript that also earns a conference slot. Every number
below was read from the FSE 2026/2027 research-papers calls on 2026-07-09 via search renderings
of the `conf.researchr.org` URLs (see `resources/official-source-map.md`); treat them as a
one-cycle snapshot and reopen the live call first.

## The two-step deadline

FSE separates **paper registration** from **paper submission**, and both are AoE:

- **Registration** locks in title, abstract, authors, and conflicts a week early (FSE 2026:
  4 September 2025). Miss it and the system will not accept the PDF later.
- **Submission** uploads the anonymized PDF (FSE 2026: 11 September 2025). FSE 2027's single
  research deadline is 2 October 2026.

Register with the *real* title and abstract, not a placeholder — the abstract drives reviewer
bidding, and a registered abstract that diverges from the final paper quietly worsens your PC
match.

## Format and page budget

- **ACM Primary Article Template**, unmodified, in the single-column review format. This is the
  ACM path, not IEEE — do not carry an IEEEtran habit over from a sibling venue.
- **Page budget (verify per cycle):** FSE 2027 posts **≤18 pages** for all text and figures plus
  **4 pages** for references only. There is no separate unlimited appendix; anything reviewers
  must read to judge the paper lives inside the budget.
- Margins, font size, and spacing are fixed by the template; editorial compression, not template
  tampering, is how you recover space.

## Double-anonymous "heavy" sweep

FSE runs **heavy** double-anonymous review: anonymity is preserved through *all* reviewing and
discussion, and even a later Major Revision response letter must stay anonymous. Because SE papers
lean on tools, repositories, and mined data, the leak surface is wide:

```bash
# Mechanical pass on the submission PDF and any anonymized artifact archive
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'github\.com/[a-z0-9-]+|gitlab|zenodo\.org/record|acknowledg|grant' | head
unzip -l artifact.zip | grep -Ei '\.git/|\.DS_Store|/home/|/Users/' | head
grep -rni 'university\|@[a-z0-9.]*\.edu\|our (tool|group|lab)' artifact/ --include='*.md' | head
```

The SE-specific leaks: a tool named after your lab, a screenshot showing a username, a data-
availability link pointing at a personal GitHub, commit metadata inside a zipped repository, and
issue-tracker URLs in the evaluation. Re-host artifacts behind an anonymizing service *before*
upload.

## Open science at submission time

FSE expects sharing by default under an open-science policy. Concretely for the submission:

- Provide an **anonymized** artifact link or upload anonymized material, and add a **Data
  Availability** statement describing what exists and where it will live after acceptance.
- If you genuinely cannot share (industrial confidentiality, human-subjects limits), say so and
  why — a missing availability story reads as a scored weakness, not a neutral choice.
- Cache LLM outputs and pin mining provenance now; these cannot be reconstructed at review time.

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Main text over the page budget | Desk-reject-grade | Cut or move to the artifact; reference pages do not absorb body text |
| Template altered (margins, shrunk font) | Named desk-reject ground | Recompile clean, recover space editorially |
| Identity leak in PDF, artifact, or tool name | Anonymity violation | Re-anonymize and re-host; scrub PDF metadata |
| Abstract/paper not registered by the earlier date | No submission slot exists | Nothing fixes this post-AoE — calendar it now |
| No availability statement, no artifact | Scored against the paper | Add the statement + an anonymized package |
| Same study under review elsewhere | Dual-submission exposure | Withdraw one venue; verify the current concurrent-submission wording |

## Final-week order of operations

1. Freeze the body early; references can churn, the argument cannot.
2. Register title/abstract/authors/conflicts well before the registration cutoff.
3. Build the anonymized artifact and place its link and Data Availability statement in the paper.
4. Run the mechanical anonymity checks on the *final* PDF and the *final* archive, not drafts.
5. Fill every HotCRP field — topics that match your evidence, conflicts for every coauthor's
   institution and recent collaborators — a day early; late conflicts are the classic midnight
   failure.
6. Re-download the uploaded PDF and read it cold to confirm it is the file you meant.

## Reverify each cycle

- Whether the year runs one deadline or two (FSE 2024 used two; 2025-2027 post one).
- The page budget and which ACM template revision is required.
- Supplementary handling, artifact-track timing, dual-submission wording, and any AI-disclosure
  rule — all cycle-volatile; none should be assumed stable.

## Output format

```text
[FSE submission status] ready / blocked / needs work
[Registration] title/abstract/authors/conflicts locked by the earlier deadline? yes/no
[Format] pages used (body/refs), ACM template compliance
[Anonymity] clean / leaks: <where>
[Open science] artifact link present? Data Availability statement present?
[Fix queue] <ordered, with owners and dates before the AoE cutoff>
```
