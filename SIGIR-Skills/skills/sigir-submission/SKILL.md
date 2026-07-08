---
name: sigir-submission
description: Use when auditing a SIGIR full or short paper before the deadline — the 9-page vs 4-page budgets with appendices counted inside, ACM sigconf anonymization, per-track OpenReview groups, the PC-member nomination duty, cross-track double-submission bans, AI-use disclosure, and desk-reject triage for the ACM SIGIR conference.
---

# SIGIR Submission

Run this audit before anything is uploaded to a SIGIR OpenReview group. SIGIR is a
multi-track venue where the same manuscript can be legal in one track and
desk-rejectable in another, so the audit starts with "which track is this PDF for?"
and only then checks format. Reopen the current edition's track page — every number
below is a 2026-cycle anchor (verified 2026-07-08, exact deadlines 待核实), not a rule.

## The two-format trap

SIGIR's full and short formats are not a long and a short version of the same bar.
A 4-page short paper is a complete argument about one focused finding; a 9-page full
paper is expected to carry a rounded evidence program (multiple collections, ablations,
significance tests, efficiency notes). The most common self-inflicted wound is
submitting a compressed full paper as a short paper — reviewers see missing evidence,
not admirable focus.

| Check | Full papers | Short papers |
|---|---|---|
| Page budget (2026) | ≤ 9 pages, references excluded | ≤ 4 pages, references excluded |
| Appendices | Count **inside** the budget (2025 wording: everything except references) | Same — no appendix escape hatch |
| Template | ACM Primary Article Template, LaTeX `sigconf` / Word Interim | Same |
| Review | Double-blind, fully anonymized | Double-blind, fully anonymized |
| OpenReview group | Main conference group | Separate Short Papers Track group |
| PC duty | One author nominated as PC member per submission | Confirm on the current track page |

The appendix rule is the sharpest edge on this table: unlike NeurIPS-style venues,
SIGIR gives you no unlimited appendix after the references. Proofs, prompt listings,
extra tables — either they fit in the budget or they move to the cited repository.

## Anonymization for IR papers specifically

Generic double-blind advice misses the leaks IR papers actually have:

- **The system name.** If your ranker is already public under the same name (arXiv,
  a leaderboard, a plugin for Anserini/PyTerrier), the name itself de-anonymizes.
  Rename for review or argue from the current policy page that preprints are allowed.
- **Leaderboard submissions.** MS MARCO / TREC-style leaderboards show team names and
  dates. Do not cite your own leaderboard row in a way that only the submitting team
  could.
- **Proprietary query logs.** "Queries sampled from our commercial search engine's
  logs in country X" can identify the company. Genericize the description, keep the
  statistics.
- **Self-citations** in third person; **repository links** anonymized (e.g., an
  anonymous.4open.science mirror); **PDF metadata** stripped.

## Policy gates (2026, source: submission-policies page)

- **Parallel submission = desk reject**, regardless of how the other venue decides.
- **Cross-track double submission inside SIGIR is banned** — e.g., the dataset you
  submit as a Resource paper cannot also be the novel contribution of your full paper.
  Decide which track owns each contribution before the abstract deadline.
- **Generative-AI use must be disclosed**; AI tools cannot be authors; SIGIR reserves
  automated compliance checks. Assume your PDF will be machine-screened.
- ACM authorship policy applies: the author list is expected to be stable and human.

## Desk-reject triage

| Trigger | Severity | Can it be fixed after the deadline? |
|---|---|---|
| Over budget (appendix counted in) | Desk reject | No |
| Wrong track's OpenReview group | Desk reject or forced withdrawal | Usually no |
| Identity leak (name, log, leaderboard) | Desk reject | No |
| Parallel submission discovered | Desk reject at any time | No |
| Same content in two SIGIR tracks | Both at risk | Only by withdrawing one first |
| Missing PC-member nomination | Chair follow-up / submission incomplete | Sometimes, briefly |
| No significance testing on close results | Review-stage damage | Only before the deadline |

## Final-week sequence for a retrieval paper

1. Freeze runs: regenerate every table from versioned run files (TREC-format
   `runs/*.trec`) so the PDF, repository, and any leaderboard entry agree.
2. Re-run the significance script last — copy-pasted p-values from stale runs are a
   classic reviewer catch when the numbers moved.
3. Compress into the page budget by demoting per-query analyses to the repository,
   not by shrinking floats or tampering with `sigconf` spacing.
4. Anonymity sweep: PDF metadata, acknowledgments, repo URL, system name, log
   provenance.
5. Upload to the **correct track group**, complete the AI-disclosure and PC-nomination
   fields, and verify the OpenReview abstract matches the PDF abstract.

```bash
# Pre-upload checks that catch the silent killers
pdfinfo paper.pdf | grep -iE "author|creator"        # metadata identity leak
grep -inE "acknowledg|our (system|engine|company)" *.tex  # textual leaks
grep -c "documentclass\[sigconf" main.tex             # right ACM class
pdftotext paper.pdf - | grep -icE "p ?[<=] ?0\.05|t-test|significan"  # stats present?
```

## Abstract-deadline gotchas

The abstract deadline (a week before the PDF in recent cycles) is a harder gate
than teams expect:

- Title, author list, and track are effectively frozen there; ACM authorship policy
  makes later author changes painful and cross-track moves are usually impossible.
- The abstract text should be the PDF's abstract, not a placeholder — reviewers bid
  on it, and a bait-and-switch abstract draws mismatched expertise.
- Conflicts-of-interest declarations and the PC-member nominee belong to this
  stage; chasing a nominee's consent during PDF week is a self-inflicted crisis.

## What this audit does not cover

Evidence quality lives in `sigir-experiments`; page-budget writing strategy in
`sigir-writing-style` and `sigir-supplementary`; track choice in
`sigir-topic-selection`. If the paper is a dataset or a replication, stop here and
re-route: Resources and Reproducibility have different budgets, different anonymity
regimes (Resources is single-anonymous), and different dates.

## Output format

```text
[SIGIR readiness] Ready / Needs fixes / Wrong track / Not ready
[Track + group] full / short + OpenReview group id
[Budget check] <pages used>/<budget>, appendix-inside-budget confirmed yes-no
[Anonymity risks] <system name / leaderboard / logs / metadata / links>
[Policy gates] parallel-submission, cross-track, AI-disclosure, PC-nomination status
[Fix order] <ordered blocking fixes>
[Reopen first] <current track page URL to re-verify dates and budgets>
```
