---
name: cav-submission
description: Use when auditing a CAV (Computer Aided Verification) submission for portal readiness, covering the four submission categories (Regular / Short Tool / Short Application / Industrial Experience & Case Studies), the LNCS page limits, the per-category anonymization matrix, the artifact-intent declaration, and desk-reject triage before the AoE paper deadline.
---

# CAV Submission

Run this audit before uploading to the CAV submission portal. CAV research papers are published
open access as **Springer LNCS chapters**, and the submission is judged by a two-stage review, so
the category you pick, the LNCS format, and the anonymization rule for that category all have to be
right before the deadline. Every number below was read from the CAV 2026 Call for Papers on
2026-07-09 via search renderings of the `i-cav.org` URLs (see
`resources/official-source-map.md`); treat them as a one-cycle snapshot and reopen the live CFP
first.

## Pick the right category first

CAV 2026 solicits **four** categories, and the category sets both the page limit and the anonymity
rule:

| Category | Page limit (LNCS, excl. refs + appendix) | Anonymized? | Fits |
|---|---|---|---|
| Regular Paper | 18 pages | **Yes** (double-blind) | A new technique/algorithm with a formal contribution |
| Short Tool Paper | 10 pages | **No** | A usable, downloadable verification tool on standard benchmarks |
| Short Application Paper | 10 pages | **Yes** (double-blind) | Applying verification to a concrete problem/system |
| Industrial Experience Report & Case Study | 10 pages | **No** | A real-world/industrial verification experience |

The anonymization split is unusual and cycle-volatile — **verify it on the current CFP**. The
logic: a tool paper that hid its tool's name would be unreviewable, so tool and industrial papers
are not anonymized; regular and application papers are.

## Format and page budget

- **LNCS `llncs` document class**, single column, unmodified. This is the Springer path — do not
  carry an ACM `acmart` or an IEEEtran double-column habit across from a sibling venue.
- **Page limits exclude references and appendices.** A clearly marked appendix is allowed, but
  **reviewers are not obliged to read it** — so nothing that decides acceptance may live only in the
  appendix (see `cav-supplementary`).
- Margins, font, and spacing are fixed by `llncs`; recover space by editing, not by tampering with
  the template.

## Double-blind sweep (Regular and Application papers)

For the anonymized categories, CAV runs double-blind review, and verification papers leak identity
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
**tool and industrial papers**, this sweep does not apply — the tool's identity is expected.

## Artifact intent at submission time

CAV asks authors to **declare artifact intent at submission** — whether you plan to submit an
artifact to the AEC if the paper is accepted — and this information is **shared with reviewers**.
Decide early: an artifact-backed claim reads as stronger. Artifact evaluation itself is
post-notification, invited, and **not** a condition of acceptance (see `cav-artifact-evaluation`).

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Wrong category (tool work filed as Regular, or vice versa) | Mis-routed review | Re-file in the correct category before the deadline; the page limit and anonymity change |
| Main text over the page limit | Desk-reject-grade | Cut or move to the (optional-to-read) appendix; refs/appendix do not absorb body text |
| Non-LNCS template or altered `llncs` | Format violation | Recompile clean in `llncs`, recover space editorially |
| Identity leak in an anonymized (Regular/Application) paper | Anonymity violation | Re-anonymize PDF, tool name, and artifact; re-host |
| Anonymized a Tool/Industrial paper by mistake | Reviewability problem | These are not double-blind — restore tool identity |
| No artifact-intent declaration | Missing signal to reviewers | Set it in the portal; decide the AEC plan now |
| Same work under review elsewhere | Dual-submission exposure | Withdraw one venue; verify the current concurrent-submission wording |

## Final-week order of operations

1. Confirm the **category** and its page limit and anonymity rule against the live CFP.
2. Freeze the body early; the theorem/algorithm and the benchmark table are the argument.
3. Build the artifact and, for anonymized categories, its anonymized copy; set artifact intent.
4. Run the mechanical anonymity sweep on the *final* PDF and archive (anonymized categories only).
5. Fill every portal field — category, topics, conflicts for every co-author's institution — a day
   early; late conflicts are the classic midnight failure.
6. Confirm the portal (EasyChair or HotCRP — **verify the live link**) and re-download the uploaded
   PDF to confirm it is the file you meant.

## Reverify each cycle

- Whether a separate abstract/registration deadline precedes the paper deadline (**待核实** for
  2026; only the paper deadline was confirmed).
- The per-category page limits, the anonymization matrix, and which LNCS template revision is
  required.
- The submission portal (EasyChair vs. HotCRP), two-stage-review mechanics, and dual-submission
  wording — all cycle-volatile.

## Output format

```text
[CAV submission status] ready / blocked / needs work
[Category] Regular / Short Tool / Short Application / Industrial — matches the contribution? yes/no
[Format] pages used (body), LNCS llncs compliance
[Anonymity] required for this category? yes/no -> clean / leaks: <where>
[Artifact intent] declared? AEC plan noted?
[Fix queue] <ordered, with owners and dates before the AoE cutoff>
```
