---
name: icsme-submission
description: Use when auditing an IEEE ICSME research-track submission for EasyChair readiness, covering the abstract-then-paper two-step deadline, the IEEEtran two-column 10+2 page budget, double-anonymous review, the open-science data-availability expectation, and desk-reject triage before the AoE cutoff.
---

# ICSME Submission

Run this audit before uploading to the ICSME EasyChair site. ICSME research papers are IEEE
conference papers that publish in **IEEE Xplore**, judged in a **single double-anonymous round**.
Every number below was read from the ICSME 2026 research-papers call on 2026-07-09 via search
renderings of the `conf.researchr.org` and EasyChair URLs (see `resources/official-source-map.md`);
treat them as a one-cycle snapshot and reopen the live call first.

## The abstract-then-paper two-step

ICSME separates **abstract registration** from **full-paper upload**, and both are AoE:

- **Abstract** locks in title, abstract, authors, and topic areas about a week early (ICSME 2026:
  27 February 2026). New submissions are not accepted after this; only updates to registered ones.
- **Full paper** uploads the anonymized PDF (ICSME 2026: 6 March 2026).

Register with the *real* title and abstract, not a placeholder — the abstract drives reviewer
bidding on EasyChair, and a registered abstract that diverges from the final paper worsens your PC
match and can strand the submission if you miss the abstract cutoff.

## Format and page budget

- **IEEE two-column conference proceedings format**, `\documentclass[conference]{IEEEtran}` for
  LaTeX; Word users take the US-Letter IEEE template. This is the **IEEE path** — do not carry an
  ACM `acmart` single-column habit over from ICSE-adjacent ACM venues or from FSE.
- **Page budget (verify per cycle):** ICSME 2026 posts **10 pages** including all text, figures,
  tables, and appendices, **plus up to 2 pages containing references only**. There is no separate
  unlimited appendix — anything reviewers must read to judge the paper lives inside the 10 pages.
- Margins, font size, and column layout are fixed by IEEEtran; editorial compression, not template
  tampering, is how you recover space. A shrunk font or widened text block is a named desk-reject.

## Double-anonymous sweep

ICSME runs **double-anonymous** review: author identity must be hidden from reviewers. Because
maintenance/evolution papers lean on named subject systems, mined repositories, and tools, the
leak surface is wide:

```bash
# Mechanical pass on the submission PDF and any anonymized artifact archive
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'github\.com/[a-z0-9-]+|gitlab|zenodo\.org/record|acknowledg|grant' | head
unzip -l artifact.zip | grep -Ei '\.git/|\.DS_Store|/home/|/Users/' | head
grep -rni 'university\|@[a-z0-9.]*\.edu\|our (tool|group|lab)' artifact/ --include='*.md' | head
```

The ICSME-specific leaks: a study that names *your own* system as the subject, a mined corpus that
is obviously your public GitHub org, a tool named after your lab, commit metadata inside a zipped
repository, and a data-availability link pointing at a personal account. Refer to your own prior
maintenance studies in the third person, and re-host artifacts behind an anonymizing service
*before* upload.

## Open science at submission time

ICSME's ROSE-Festival culture makes open science the default expectation, even at review time:

- Provide an **anonymized** artifact link (or upload anonymized material) and a **data-availability
  statement** describing the mined corpus, subject systems, scripts, and where they will live after
  acceptance.
- Pin mining provenance now — repository SHAs, extraction dates, inclusion/exclusion criteria — and
  cache any LLM outputs; these cannot be reconstructed at review time.
- If confidentiality (an industrial legacy system, proprietary change history) blocks sharing, say
  so and why; a silent gap reads as a scored weakness, not a neutral choice.

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Main text over 10 pages (figures/appendices counted) | Desk-reject-grade | Cut or move to the artifact; the 2 reference pages do not absorb body text |
| Template altered (margins, shrunk font, wrong class) | Named desk-reject ground | Recompile clean IEEEtran conference, recover space editorially |
| Identity leak in PDF, artifact, subject-system choice, or tool name | Anonymity violation | Re-anonymize and re-host; scrub PDF metadata |
| Abstract not registered by the earlier date | No submission slot exists | Nothing fixes this post-AoE — calendar it now |
| No availability statement, no artifact | Scored against the paper under ROSE norms | Add the statement + an anonymized package |
| Same study under review elsewhere | Dual-submission exposure | Withdraw one venue; verify the current concurrent-submission wording |

## Final-week order of operations

1. Freeze the body early; references can churn, the argument cannot.
2. Register title/abstract/authors/topics on EasyChair well before the abstract cutoff.
3. Build the anonymized artifact and place its link and data-availability statement in the paper.
4. Run the mechanical anonymity checks on the *final* PDF and the *final* archive, not drafts.
5. Fill every EasyChair field — topics that match your evidence, conflicts for every coauthor's
   institution and recent collaborators — a day early; late conflicts are the classic failure.
6. Re-download the uploaded PDF and read it cold to confirm it is the file you meant.

## Reverify each cycle

- Whether the abstract-then-paper two-step and its exact dates hold.
- The page budget (10+2 in 2026) and which IEEEtran revision is required.
- Supplementary handling, the ROSE-Festival timing, dual-submission wording, and any AI-disclosure
  rule — all cycle-volatile; none should be assumed stable.

## Output format

```text
[ICSME submission status] ready / blocked / needs work
[Abstract step] title/abstract/authors/topics registered by the earlier deadline? yes/no
[Format] pages used (body/refs), IEEEtran conference compliance
[Anonymity] clean / leaks: <where, incl. subject-system and tool-name leaks>
[Open science] anonymized artifact link present? data-availability statement present?
[Fix queue] <ordered, with owners and dates before the AoE cutoff>
```
