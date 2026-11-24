---
name: atc-submission
description: Use when auditing an ATC (ACM SIGOPS Annual Technical Conference, formerly USENIX ATC) submission for HotCRP readiness — first two pages that survive the round-one read, the two-column 12/6-page budget with appendices inside it, the two-submissions-per-author cap, the double-blind anonymity sweep, ACM Open Access publication, and desk-reject triage before the 19 January 2027 AoE cutoff.
---

# ATC Submission

Run this audit before uploading to the ATC 2027 HotCRP site (`atc27.hotcrp.com`). ATC is the **ACM
SIGOPS Annual Technical Conference** — the continuation of the retired **USENIX ATC** (USENIX ended
it after ATC '25) — and it is still re-deciding its rules each year. For **ATC 2027 (Rennes, 28 June
– 1 July 2027)** the submission deadline is **19 January 2027, AoE, no extensions**. Every number
below was read from the ATC 2027 SIGOPS call on 2026-11-24 (direct fetch; see
`resources/official-source-map.md`); treat it as a one-cycle snapshot and reopen the live call
first.

## Round one reads your first two pages

ATC 2027 reviews in two rounds, and the **first round is based on the first two pages** of the
paper. Reviewers can open the rest but are not obliged to. Round one rejects a paper when it is
clear that:

- it is not relevant to ATC (the main contribution is not systems);
- the problem is not clearly motivated;
- the main idea or chief insight is hard to understand;
- the contribution is too small or incremental over the state of the art;
- the paper does not place itself properly against related work;
- the evaluation is not rigorous (weak or inappropriate baselines, wrong workloads).

So the abstract and introduction must answer all six on their own — make the introduction
self-contained. (ATC 2026 used a separate two-page extended abstract for this; ATC 2027 does not
ask for one.)

## Format and page budget

- **PDF**, A4 or US letter; text and figures inside a **178 × 229 mm (7 × 9 in)** block; **two
  columns** 8 mm apart; **10-point** Times Roman (or similar) on 12-point leading; numbered pages;
  hyperlinked references. The call recommends `\documentclass[sigplan,10pt]{acmart}` (the ACM SIGPLAN
  LaTeX or Word template), with the copyright block suppressed and page numbers printed.
- **Page budget:** **long papers ≤ 12 pages, short papers ≤ 6 pages**, excluding references but
  **including all text, figures, tables, footnotes, and appendices**. An optional appendix (algorithm
  details, proofs, code snippets) must fit *inside* the limit — a change from ATC 2026, where
  appendices sat outside it.
- Violations may be desk-rejected with no extension to fix them; upload an early draft to check.
- Reviewers are **not required** to read supplementary material; nothing that decides acceptance may
  live only there (see `atc-supplementary`).

## Two submissions per author

New in 2027: each author may appear on **at most 2** ATC 2027 submissions, whatever the length or
track, regardless of email or affiliation. After the deadline the PC chairs check, and a violation
may get **every** submission listing that author desk-rejected. The author list cannot change after
submission. Reconcile the group's ledger before anyone registers a paper.

## Double-blind sweep

ATC review is **double-blind**. Put the **paper ID** from registration on the first page instead of
names; do not identify yourself or your institution explicitly or by implication; if your system's
name is already public (arXiv, tech report, talk, social media — all explicitly permitted), use an
**anonymized name**; cite your own work in the third person, never "reference removed"; for a
concurrent related submission, cite an anonymized version, discuss the relation, and email the PC
chairs a copy. **Operational Systems Track** papers may identify the organization behind the system
when anonymization is impractical (ask the chairs if unsure).

```bash
# Mechanical pass on the submission PDF and any anonymized artifact archive
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'github\.com/[a-z0-9-]+|gitlab|zenodo\.org/record|acknowledg|grant|our (prior|previous) (system|work)' | head
unzip -l artifact.zip | grep -Ei '\.git/|\.DS_Store|/home/|/Users/|hostname' | head
grep -rniE 'university|@[a-z0-9.]+\.edu|cluster [a-z0-9-]+|internal-|corp\.' artifact/ --include='*.md' --include='*.sh' | head
```

The systems-specific leaks: a system named after your group or product, a cluster hostname in a log
or config, a `git remote` inside a zipped repo, an acknowledgments/funding line, and "our system X"
self-citation. Mirror any linked repository behind a blind service before upload.

## Policies to clear on the form

- **Resubmissions:** a paper under submission elsewhere may not be submitted. For a previously
  rejected paper, upload the prior-submission information and an anonymized summary of changes
  (aim for one page); reviewers see it only after writing their reviews.
- **Prior work:** extensions of your own work must state the difference; workshop versions are fine
  if the ATC paper adds significant content.
- **Generative AI:** AI may help with editing and framing, but papers produced entirely or
  substantively by generative AI must not be submitted; all text must reflect the authors' thoughts.
- **Conflicts:** declare institutional (2 years), advisor, collaborator (2 years) and family
  conflicts; former interns list supervisors, not the whole company. PC chairs do not submit.

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| First two pages do not stand alone | Round-one failure | Rewrite abstract + intro so scope, motivation, idea, delta, positioning, and evidence all appear by page 2 |
| Body plus appendix over the 12/6-page budget | Desk-reject-grade | Cut, or move peripheral material to the artifact — the appendix no longer absorbs overflow |
| An author on three or more submissions | Desk-reject for all that author's papers | Decide which two papers that author stays on before submission |
| Format altered (margins, column width, shrunk font) | Desk-reject ground | Recompile with the recommended `acmart` setup; recover space editorially |
| Identity leak in PDF, artifact, system name, or self-citation | Anonymity violation | Re-anonymize, re-host, scrub metadata, third-person self-cites |
| Same work under review elsewhere | Not permitted | Withdraw one venue before submitting |
| Claims with no runnable evidence | Scored weakness | Add the anonymized artifact and a claim-to-experiment map |

## Final-week order of operations

1. Freeze the system and results early; prose can churn, the measurements cannot.
2. Read the first two pages cold, as a round-one reviewer, and check all six round-one criteria.
3. Run the double-blind checks on the **final** PDF and the **final** artifact archive — not drafts.
4. Fill every HotCRP field — track, topics, conflicts, resubmission summary — a day early; the
   author list is frozen once submitted.
5. Target **19 January 2027, AoE**, not local midnight (the HotCRP `/deadlines` page was still
   empty on 2026-11-24 — confirm the clock there).
6. Re-download the uploaded PDF and read it cold to confirm it is the file you meant.

## Reverify each cycle

- The deadline, the round-one page window ("may involve more pages" if submissions surge), and the
  author cap.
- The page budget and whether appendices count (they do in 2027, did not in 2026).
- The Operational Systems Track rules, the artifact-evaluation call (2027 version not yet published),
  and the AI policy.
- ACM Open Access / APC terms and waivers.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue atc-skills   # from a clone of the AJS repository
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
[ATC submission status] ready / blocked / needs work
[First two pages] stand alone against all six round-one criteria? yes/no
[Format] pages used (body+appendix / refs), acmart sigplan 10pt compliance
[Author cap] every author on at most 2 ATC 2027 submissions? yes/no
[Anonymity] clean / leaks: <where>
[Artifact] anonymized runnable package linked? claim-to-experiment map present?
[Fix queue] <ordered, with owners and dates before the 19 January 2027 AoE cutoff>
```
