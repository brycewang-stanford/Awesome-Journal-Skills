---
name: cav-submission
description: Use when auditing a CAV (Computer Aided Verification) submission for portal readiness, covering the three CAV 2027 submission categories (Regular / Tool / Application-Industrial-Case Study), the LNCS page limits, the per-category anonymity rule, the mandatory tool-paper artifact and the artifact-intent declaration, the five-submissions-per-author cap, and desk-reject triage before the AoE paper deadline.
---

# CAV Submission

Run this audit before uploading to the CAV submission portal. CAV research papers are published
open access as **Springer LNCS chapters**, and the submission is judged by a two-stage review, so
the category you pick, the LNCS format, and the anonymization rule for that category all have to be
right before the deadline. Every number below was read from the CAV 2027 Call for Papers on
2026-11-24 by direct fetch of `https://conferences.i-cav.org/2027/cfp/` (see
`resources/official-source-map.md`); treat them as a one-cycle snapshot and reopen the live CFP
first. CAV changed its categories, page limits, anonymity split and tool-paper artifact rule
between 2026 and 2027 — do not reuse a CAV 2026 checklist.

## Pick the right category first

CAV 2027 solicits **three** categories, and the category sets the page limit, the anonymity
rule, and whether an artifact is mandatory:

| Category | Page limit (LNCS, excl. refs + appendix; camera-ready) | Anonymized? | Artifact | Fits |
|---|---|---|---|---|
| Regular Paper | 18 pages (20) | **Yes** (double-blind) | Invited after acceptance, non-conditional | A new technique/algorithm with a formal contribution |
| Tool Paper | 18 pages (20) | **No** (single-blind) | **Mandatory**, reviewed in parallel; needs at least Functional | A new tool or new tool version of wide interest, backed by refereed work |
| Application / Industrial Experience / Case Study Paper | 10 pages (12) | **No** (single-blind) | Encouraged, non-conditional | Applying or transferring verification to a real problem or industrial setting |

At most **5** submissions per author across all three categories. The anonymity split is unusual
and cycle-volatile (CAV 2026 still anonymized its Short Application Papers) — **verify it on the
current CFP**. The logic: a tool paper that hid its tool's name would be unreviewable.

## Format and page budget

- **LNCS `llncs` document class**, single column, unmodified. This is the Springer path — do not
  carry an ACM `acmart` or an IEEEtran double-column habit across from a sibling venue.
- **Page limits exclude references and appendices.** A clearly marked appendix is allowed, but
  **reviewers are not obliged to read it** — so nothing that decides acceptance may live only in the
  appendix (see `cav-supplementary`).
- Margins, font, and spacing are fixed by `llncs`; recover space by editing, not by tampering with
  the template.

## Double-blind sweep (Regular Papers)

For Regular Papers, CAV runs double-blind review (non-conforming submissions are rejected
without review), and verification papers leak identity
through **tool names, repositories, and benchmark artifacts**:

```bash
# Mechanical pass on an anonymized submission PDF and any artifact archive
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'github\.com/[a-z0-9-]+|gitlab|zenodo\.org|our (tool|solver|prover)|acknowledg|grant' | head
unzip -l artifact.zip | grep -Ei '\.git/|\.DS_Store|/home/|/Users/' | head
```

The verification-specific leaks: a solver named after your group, a benchmark path revealing a
cluster/username, a tool repository URL in the evaluation, and an acknowledgement of a grant that
identifies the lab. Re-host anonymized artifacts behind an anonymizing service *before* upload. For
**Tool and Application/Industrial/Case Study papers**, this sweep does not apply — they are
single-blind. CAV 2027 also strongly discourages posting to arXiv within 1 week around or 1 month
after the deadline.

## Artifact intent at submission time

CAV asks authors to **declare artifact intent at submission** — whether you plan to submit an
artifact — and this information is **shared with reviewers**. Decide early: an artifact-backed
claim reads as stronger. For Regular and Application papers, artifact evaluation is
post-notification, invited, and **not** a condition of acceptance. For **Tool Papers it is
mandatory**: register the artifact by 8 March 2027 and submit by 11 March 2027 (CAV 2027), and the
paper is accepted only if the artifact earns at least the Functional badge. An exemption must be
requested **at submission time** with reasons (see `cav-artifact-evaluation`).

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Wrong category (tool work filed as Regular, or vice versa) | Mis-routed review | Re-file in the correct category before the deadline; anonymity and the artifact obligation change |
| Tool Paper without an artifact plan or exemption request | Cannot be accepted | Plan the March artifact round now, or file the exemption request with the submission |
| More than 5 submissions by one author | Over the per-author cap | Withdraw down to 5 before the deadline |
| Main text over the page limit | Desk-reject-grade | Cut or move to the (optional-to-read) appendix; refs/appendix do not absorb body text |
| Non-LNCS template or altered `llncs` | Format violation | Recompile clean in `llncs`, recover space editorially |
| Identity leak in a Regular Paper | Rejected without review | Re-anonymize PDF, tool name, and artifact; re-host |
| Anonymized a Tool/Application paper by mistake | Reviewability problem | These are single-blind — restore tool identity |
| No artifact-intent declaration | Missing signal to reviewers | Set it in the portal; decide the AEC plan now |
| Same work under review elsewhere | Dual-submission exposure | Withdraw one venue; verify the current concurrent-submission wording |

## Final-week order of operations

1. Confirm the **category** and its page limit and anonymity rule against the live CFP.
2. Freeze the body early; the theorem/algorithm and the benchmark table are the argument.
3. Build the artifact (mandatory for Tool Papers) and, for Regular Papers, its anonymized copy;
   set artifact intent.
4. Run the mechanical anonymity sweep on the *final* PDF and archive (Regular Papers only).
5. Fill every portal field — category, topics, conflicts for every co-author's institution — a day
   early; late conflicts are the classic midnight failure.
6. Confirm the portal (CAV 2027: HotCRP; the CFP link was not yet posted on 2026-11-24 —
   **verify the live link**) and re-download the uploaded PDF to confirm it is the file you meant.

## Reverify each cycle

- Whether a separate abstract/registration deadline precedes the paper deadline (the CAV 2027
  CFP lists only "Full papers due", 20 January 2027).
- The category set, per-category page limits, the anonymity split, the tool-paper artifact rule,
  and which LNCS template revision is required — CAV changed all of these between 2026 and 2027.
- The HotCRP link, two-stage-review mechanics, and dual-submission wording — all cycle-volatile.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue cav-skills   # from a clone of the AJS repository
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
[CAV submission status] ready / blocked / needs work
[Category] Regular / Tool / Application-Industrial-Case Study — matches the contribution? yes/no
[Format] pages used (body), LNCS llncs compliance
[Anonymity] required for this category? yes/no -> clean / leaks: <where>
[Artifact intent] declared? Tool Paper: March artifact round or exemption request filed?
[Fix queue] <ordered, with owners and dates before the AoE cutoff>
```
