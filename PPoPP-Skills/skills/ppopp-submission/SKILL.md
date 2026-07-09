---
name: ppopp-submission
description: Use when auditing a PPoPP research-paper submission for HotCRP readiness, covering the two-column acmart sigplan template, the 10-page text+figures budget with unlimited references, the 100-400 word abstract, double-blind anonymity for parallel-systems work, conflict declaration against the PC and External Review Committee, and desk-reject triage before the AoE cutoff.
---

# PPoPP Submission

Run this audit before uploading to the PPoPP HotCRP site (PPoPP 2027's summer round used
`ppopp27-summer.hotcrp.com`). PPoPP is the ACM SIGPLAN Symposium on Principles and Practice of
Parallel Programming; its submissions are conference papers in the **two-column `acmart`
`sigplan`** format, not journal manuscripts. Every number below was read from the PPoPP 2026/2027
calls on 2026-07-09 via search renderings (see `resources/official-source-map.md`); treat them as a
one-cycle snapshot and reopen the live call first.

## Abstract and registration

- Submit **electronically** with an **abstract of 100–400 words**, full author contact info, and
  the complete author/affiliation list (no "et al." in the author field).
- In recent editions the abstract and the full paper share a single deadline (PPoPP 2026:
  1 September 2025; PPoPP 2027 summer round: 3 August 2026, AoE). Whether a year adds a separate
  earlier abstract-registration date, or a second (fall) round, is cycle-volatile — 待核实.
- Write the real abstract, not a placeholder: it drives reviewer bidding and TPMS matching, and a
  parallel-programming abstract that hides the actual system or workload gets mismatched reviewers.

## Format and page budget

- **Two-column ACM Conference Format**: the `acmart` document class in the `sigplan` proceedings
  mode, via `ppopp-acmart-sigplanproc-template.tex`. This is the SIGPLAN two-column look — **not**
  PLDI's single-column review style and **not** an IEEE box.
- **Page budget:** **10 pages** of text and figures. **References are excluded and unlimited** —
  include the full author list for every citation (no "et al."). There is no separate unlimited
  appendix inside the reviewed budget; anything reviewers must read to judge the paper lives in the
  10 pages (see `ppopp-supplementary` for what may move to the artifact).
- The PDF must be **printable on both A4 and US-letter** paper. Papers that exceed the length,
  deviate from the template, or arrive late are rejected — this is stated, not discretionary.
- Margins, font, and column geometry are fixed by `acmart`; recover space by cutting, not by
  shrinking the template.

## Double-blind sweep

PPoPP review is **double-blind**. Parallel-systems papers leak identity through the machine and the
code more than through the prose:

```bash
# Mechanical pass on the submission PDF and any anonymized artifact archive
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'github\.com/[a-z0-9-]+|gitlab|zenodo\.org/record|acknowledg|grant|cluster|supercomputer' | head
unzip -l artifact.zip 2>/dev/null | grep -Ei '\.git/|/home/|/scratch/|/users/|\.slurm' | head
grep -rniE 'our (system|runtime|library)|named after|@[a-z0-9.]*\.edu' artifact/ --include='*.md' 2>/dev/null | head
```

The PPoPP-specific leaks: a runtime or library named after your group; a **named cluster or
supercomputer** ("runs on <Center> <Machine>") that identifies the institution; SLURM job scripts
with a user/account; a results repo on a personal GitHub; and acknowledgements/grant numbers left
in the review PDF. Describe hardware by its architecture ("a 2-socket 64-core AMD EPYC node,
8-channel DDR5, an NVIDIA H100") rather than by a facility name during review.

## Conflicts against PC and ERC

- Declare conflicts against **both** the Program Committee **and** the **External/Extended Review
  Committee (ERC)** — PPoPP uses both pools, and a missed ERC conflict is a common late failure.
- Include every coauthor's institution and recent collaborators; reviewer matching may run through
  **TPMS**, so an accurate topic/COI declaration directly changes who reads you.

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Body over 10 pages (text+figures) | Stated reject ground | Cut or move to artifact; references do not absorb body text |
| Single-column / wrong template | Format-deviation reject | Recompile with `acmart` `sigplan` two-column |
| "et al." in the paper's author field or citations | Requirement violation | Spell out all authors |
| Named cluster/user/grant reveals identity | Anonymity break | Re-describe hardware architecturally; scrub scripts and metadata |
| Missing ERC conflicts | Review-integrity risk | Declare against PC and ERC before the deadline |
| Abstract missing or outside 100–400 words | Submission-form error | Fix in HotCRP before upload closes |
| Same result under review at PLDI/CGO/SC | Dual-submission exposure | Withdraw one; verify current concurrent-submission wording |

## Final-week order of operations

1. Freeze the claim and the scalability figures early; the numbers are the paper.
2. Fill the abstract (100–400 words), author list, topics, and PC+ERC conflicts a day early.
3. Confirm the PDF is two-column `acmart` `sigplan`, ≤10 pages text+figures, A4/US-letter clean.
4. Run the mechanical double-blind checks on the **final** PDF and the **final** artifact archive.
5. Re-describe every machine architecturally; remove facility names, SLURM accounts, grant numbers.
6. Re-download the uploaded PDF and read it cold to confirm it is the file you meant.

## Reverify each cycle

- The number of submission rounds (the 2027 "summer" HotCRP suggests a possible split — 待核实).
- The exact page budget and which `acmart` revision is required.
- Artifact-track timing and badge set, dual-submission wording, and any AI-disclosure rule.

## Output format

```text
[PPoPP submission status] ready / blocked / needs work
[Abstract] 100-400 words present? topics/COI set?
[Format] pages used (text+figs / refs), two-column acmart sigplan? A4+letter?
[Anonymity] clean / leaks: <named machine | user | grant | repo>
[Conflicts] PC + ERC declared? yes/no
[Fix queue] <ordered, with owners and dates before the AoE cutoff>
```
