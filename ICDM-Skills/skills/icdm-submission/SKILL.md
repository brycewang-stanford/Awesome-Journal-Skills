---
name: icdm-submission
description: Use when auditing an ICDM (IEEE International Conference on Data Mining) submission for readiness, covering Research-vs-Applied track choice and its anonymity regime, the triple-blind sweep, the 10-page IEEE all-inclusive cap, the single June deadline, in-paper artifact references, and the desk-level triggers that get an ICDM paper rejected without review.
---

# ICDM Submission

Run this audit twice: once a week before and once the day before the full-paper deadline
(2026: June 6, AoE — there was **no separate abstract deadline**). ICDM runs a
**single deadline**, not KDD-style cycles, so there is no next window this year — the
paper you upload in June is the paper that gets reviewed. Reopen the current **track**
call first; Research and Applied now differ on anonymity.

## Track and anonymity regime first

- **Research Track is triple-blind**; the **2026 Applied Track is single-blind**; the
  **Blue Sky Track** (CCC-sponsored) is a separate visionary lane. Pick the track before
  formatting, because it decides whether the paper must hide author identity at all.
- One paper, one track: do not submit the same work to Research and Applied at once.
- If the contribution is a deployed system with measured real-world impact, the Applied
  Track may fit better and its single-blind regime removes the anonymization burden — but
  confirm the current call's Applied scope before switching.

## The triple-blind sweep (Research Track)

ICDM's triple-blind tradition (since 2011) is stricter than double-blind: author *and*
referee identities are hidden, known only to the PC Co-Chairs, and author names are
revealed only after acceptance is finalized. Your obligation is to conceal identity
**throughout the whole paper**, not just the title block.

- No author names, affiliations, acknowledgements, funding/grant numbers, or ORCIDs.
- No "in our previous work [X], we..." phrasing that de-anonymizes by self-reference;
  cite your own prior papers in the third person.
- No identifying system names, internal dataset names, institutional URLs, or repository
  links that resolve to a named account.
- Scrub figures, plots, PDF metadata, and any embedded file paths.
- Preprints (ICDM 2026): do not upload or publicize the submission on arXiv or other platforms
  during review; a preprint posted before submission may stay up, but the PDF must not cite
  it in a way that reveals authorship.

## Submission-form extras

- Complete the **reproducibility checklist** in the submission system (required in 2026; the
  answers become part of the submission and reviewers weigh them).
- Select the track in the submission form (Research or Applied); there is no abstract-only
  registration step in 2026.

## The 10-page all-inclusive cap

The single hardest ICDM formatting fact: **10 pages in IEEE two-column format, including
the bibliography and any appendices.** There is no separate reference budget and no
separate appendix budget. Over-length papers are **rejected without review**.

```latex
% ICDM IEEE two-column setting (verify against the current track call)
\documentclass[conference]{IEEEtran}
% Everything below counts toward the 10-page cap: body, references, appendix.
% Do NOT shrink margins, fonts, or \baselineskip to reclaim space; IEEE
% proceedings checks and chairs detect a modified template.
% Plan the appendix as a first-class competitor for the same 10 pages as the body.
```

- Content, references, and appendix together must end by page 10; if it does not fit, cut
  scope or move detail to an external anonymized repository, never squeeze the template.
- Reference the code/data repository **inside the PDF**, anonymized: because ICDM
  traditionally offers no rebuttal, a repository not cited at submission is invisible to
  reviewers for the whole cycle.

## Desk-level and severity table

| Trigger | Track affected | Severity | Fixable after deadline? |
|---|---|---|---|
| Over 10 pages (incl. refs + appendix) | Both | Rejected without review | No |
| Identity leak in body, figure, metadata, or repo | Research | Triple-blind violation | No |
| Modified IEEE template | Both | Desk-level / chair flag | No |
| Same paper in Research and Applied | Both | Rejection of both | No |
| Repository link absent from PDF | Both | Not fatal, but unrepairable without rebuttal | No |
| Wrong track for the contribution type | Both | Hostile review, mis-fit | Only before deadline |

## Final-week sequence

1. Freeze the track choice and confirm the anonymity regime it implies.
2. Rebuild the PDF from a clean `IEEEtran` checkout; measure to the bottom of page 10 with
   references and appendix included.
3. Run the triple-blind sweep against the list above (Research Track): names, self-cites,
   system names, metadata, repo account.
4. Export a fresh anonymized repository with no git history and no institutional paths;
   cite it in the body.
5. Register the abstract early in the week; upload the paper with hours, not minutes, of
   AoE margin.

## Vignette: a paper that lost a page to its own bibliography

A graph-mining team writes a tight 9.5-page body and adds a two-page appendix of proofs,
forgetting that at ICDM the references (1.5 pages) and the appendix both live inside the
10-page cap. The compiled PDF is 12 pages — an automatic no-review reject. The fix is not
cosmetic: they promote one proof sketch to the body, move the full proof and extra tables
to the cited anonymized repository, and trim the related-work prose. The lesson: at ICDM,
budget the appendix and references *against the body* from the first outline, because
there is no separate allowance to grow into.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue icdm-skills   # from a clone of the AJS repository
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
[ICDM readiness] Ready / Needs fixes / Not ready
[Track x anonymity] Research(triple-blind) | Applied(single-blind) | Blue Sky
[Page check] <= 10 pages incl. refs + appendix: pass / fail
[Anonymity] triple-blind sweep clean / leaks found (Research only)
[Artifact visibility] repo cited in PDF: yes / no
[Fix order] <ordered fixes before the AoE deadline>
```
