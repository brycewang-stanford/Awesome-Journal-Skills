---
name: atc-submission
description: Use when auditing an ATC (ACM SIGOPS Annual Technical Conference, formerly USENIX ATC) submission for HotCRP readiness — the paired two-page extended abstract plus full paper, the two-column 12/6-page budget, the double-blind anonymity sweep, ACM Open Access publication, and desk-reject triage before the early-June AoE cutoff.
---

# ATC Submission

Run this audit before uploading to the ATC HotCRP site (`atc26.hotcrp.com`). ATC 2026 is the first
**ACM SIGOPS Annual Technical Conference** — the continuation of the former **USENIX ATC** — so the
process changed in the handover: a new **two-round, extended-abstract** review, a **June deadline**,
a **Hong Kong / November** conference, and **ACM Open Access** publication. Every number below was
read from the ATC 2026 SIGOPS call and the USENIX ATC '25 pages on 2026-07-09 via search renderings
(see `resources/official-source-map.md`); treat them as a one-cycle snapshot and reopen the live
call first.

## The paired upload (the thing authors miss)

ATC's first review round judges a **two-page extended abstract**, uploaded **together with the full
paper** in one HotCRP submission:

- The extended abstract gives the motivation and contribution and is **for review only — it is not
  published**.
- It must **stand on its own**: a round-one reviewer may read *only* the abstract, and a round-two
  reviewer may read *only* the paper. Neither may assume the other.
- A copy of the introduction can serve as the abstract **only if it fits two pages and reads
  self-contained** — usually it needs tightening, not just truncation.

If your submission has a strong paper but a weak, dependent abstract, you can be cut in round one
before anyone opens the PDF. Audit the abstract as hard as the paper.

## Format and page budget

- **Two-column** format: text block **178 × 229 mm (7 × 9 in)**, **10-point** Times Roman (or
  similar) on 12-point single-spaced leading, A4 or US letter. This is the classic USENIX systems
  layout; whether the SIGOPS edition mandates the USENIX template file or an ACM equivalent is
  **待核实** — confirm on the call.
- **Page budget:** **full papers ≤ 12 pages, short papers ≤ 6 pages**, excluding references and
  appendices but **including** all text, figures, tables, and footnotes.
- Reviewers are **not required** to read appendices; nothing that decides acceptance may live only
  in an appendix (see `atc-supplementary`).

## Double-blind sweep

ATC review is **double-blind**: reviewer and author identities are mutually concealed. Because
systems papers lean on code, testbeds, and system names, the leak surface is wide:

```bash
# Mechanical pass on the submission PDF and any anonymized artifact archive
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'github\.com/[a-z0-9-]+|gitlab|zenodo\.org/record|acknowledg|grant|our (prior|previous) (system|work)' | head
unzip -l artifact.zip | grep -Ei '\.git/|\.DS_Store|/home/|/Users/|hostname' | head
grep -rniE 'university|@[a-z0-9.]+\.edu|cluster [a-z0-9-]+|internal-|corp\.' artifact/ --include='*.md' --include='*.sh' | head
```

The systems-specific leaks: a system named after your group or product, a cluster hostname in a log
or config, a `git remote` inside a zipped repo, an acknowledgments/funding line, and citing your own
prior system as "our system X." Cite your own work in the **third person** and never write
"reference removed for blind review." Mirror any linked repository behind a blind service before
upload.

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| No extended abstract, or it does not stand alone | Round-one failure | Write/tighten a self-contained 2-page abstract; verify it reads without the paper |
| Main text over the 12/6-page budget | Desk-reject-grade | Cut or move to an appendix; references/appendices do not absorb body text |
| Format altered (margins, column width, shrunk font) | Desk-reject ground | Recompile to the two-column spec; recover space editorially |
| Identity leak in PDF, artifact, system name, or self-citation | Anonymity violation | Re-anonymize, re-host, scrub metadata, third-person self-cites |
| Same work under review elsewhere | Concurrent-submission exposure | Withdraw one venue; verify the current concurrent-submission wording |
| Claims with no runnable evidence | Scored weakness | Add the anonymized artifact and a claim-to-experiment map |

## Final-week order of operations

1. Freeze the system and results early; prose can churn, the measurements cannot.
2. Write the extended abstract last but audit it first — read it cold, without the paper, and check
   the problem, contribution, testbed, and result all land in two pages.
3. Run the double-blind checks on the **final** PDF, the **final** extended abstract, and the
   **final** artifact archive — not on drafts.
4. Fill every HotCRP field — topic tags that match your evidence, conflicts for every coauthor's
   institution and recent collaborators — a day early; late conflicts are the classic midnight
   failure.
5. Confirm the exact deadline day on the SIGOPS call (renderings disagree on **1 vs. 10 June 2026**
   — 待核实) and target AoE, not local midnight.
6. Re-download both uploaded PDFs and read them cold to confirm they are the files you meant.

## Reverify each cycle

- The exact June deadline day, the abstract/paper pairing rule, and whether the two-round model
  persists.
- The page budget and which template file (USENIX vs. ACM) is required (**待核实**).
- Whether the Deployed Systems / experience track is offered (**待核实**), the artifact-track timing,
  concurrent-submission wording, and any AI-disclosure rule.
- ACM Open Access / APC terms and waivers.

## Output format

```text
[ATC submission status] ready / blocked / needs work
[Extended abstract] present and self-standing? yes/no
[Format] pages used (body/refs), two-column template compliance
[Anonymity] clean / leaks: <where>
[Artifact] anonymized runnable package linked? claim-to-experiment map present?
[Fix queue] <ordered, with owners and dates before the early-June AoE cutoff>
```
