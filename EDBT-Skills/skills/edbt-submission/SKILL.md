---
name: edbt-submission
description: Use when auditing an EDBT research-track submission for Microsoft CMT readiness, covering the cycle choice, the paper shape (Regular / Experiments-&-Analysis / Vision), the OpenProceedings/host LaTeX template and per-shape page budget, the 12-month resubmission ban, reproducibility items, and desk-reject triage before the cycle deadline.
---

# EDBT Submission

Run this audit before uploading to **Microsoft CMT** for an EDBT cycle. EDBT is the European
database-systems flagship; its papers are published **open access on OpenProceedings.org** under a
**CC-BY-NC-ND** license, and it runs a **multiple-cycle rolling model** rather than one annual
deadline. Every number below was read from the EDBT/ICDT 2026 (Tampere) call and the EDBT 2022
research CFP on 2026-07-09 via search renderings (see `resources/official-source-map.md`); treat
them as a one-cycle snapshot and reopen the live call first.

## Pick the cycle and the paper shape first

Two decisions precede the audit, and both change the checklist:

- **Which cycle?** EDBT runs three submission/publication cycles a year (since 2022). A paper
  accepted in an earlier cycle presents at that year's conference; the last cycle rolls to the next
  edition. Choose the cycle your evidence is actually ready for — a rushed submission into an early
  cycle wastes a *revise* opportunity you could have earned with two more weeks of measurement.
  (EDBT 2027 cycle deadlines: 4 Feb 2026, 10 Jun 2026, 7 Oct 2026; cycle 3 is the live one as of
  2026-07-09.)
- **Which shape?** EDBT distinguishes **Regular** research papers, **Experiments & Analysis** papers
  (where the benchmarking/repeatability study *is* the contribution), and short **Vision** papers.
  The shape sets the page budget and what reviewers weigh — do not submit an Experiments & Analysis
  paper as a Regular one or vice versa.

## Format and page budget

- **Host/OpenProceedings LaTeX template**, unmodified. EDBT proceedings are produced by
  OpenProceedings, not ACM DL or IEEE Xplore — use the template the current host site ships, not an
  `acmart` or `IEEEtran` file carried over from a US venue.
- **Page budget (verify per cycle):** from the EDBT 2022 research CFP, **Regular** and **Experiments
  & Analysis** papers are **≤12 pages** plus **unlimited references**; **Vision** papers are **≤6
  pages** plus unlimited references. References do not count against the limit, but figures, tables,
  and appendices inside the body do. (**待核实** for the exact current-cycle numbers.)
- Margins, font size, and spacing are fixed by the template; editorial compression, not template
  tampering, is how you recover space.

## The resubmission-ban check (EDBT-specific)

EDBT enforces a **12-month resubmission ban**: work rejected or withdrawn from an EDBT track cannot
be resubmitted to any EDBT track **in the same paper format** for 12 months. Before you submit:

- Confirm this exact work has not been rejected/withdrawn from an EDBT track in the past year in the
  same format. A Regular paper reworked as a Vision paper is a different format — but do not guess
  the boundary; check the current wording.
- This is not a dual-submission rule (that is separate); it is EDBT's own re-entry cooldown, a
  direct consequence of the rolling-cycle model, where nothing stops rapid re-tries otherwise.

## Blind policy and identity

- Confirm on the current call whether reviewing is **single-blind or double-blind** (**待核实**;
  EDBT has historically used author-identified single-blind reviewing). If the cycle is
  double-blind, anonymize the PDF, the artifact, and any repository link:

```bash
# If the current cycle is double-blind, run before upload:
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'github\.com/[a-z0-9-]+|zenodo\.org/record|acknowledg|grant' | head
unzip -l artifact.zip | grep -Ei '\.git/|\.DS_Store|/home/|/Users/' | head
```

If the cycle is single-blind, skip anonymization but still scrub broken author metadata and stale
paths from the artifact.

## Reproducibility at submission time

EDBT's community values inspectable, reproducible work, and the published record is open access:

- Provide a **runnable artifact** or a clear availability statement: what exists, the workloads and
  dataset versions, the hardware/cluster configuration, and where the package will live.
- For an **Experiments & Analysis** paper this is not optional decoration — the repeatability of the
  measurements is the contribution, so the package and the paper must line up exactly.
- Pin dataset versions, query/workload provenance, and engine build/commit now; these cannot be
  reconstructed after the cycle closes.

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Body over the per-shape page budget | Desk-reject-grade | Cut or move to the artifact; references do not absorb body text |
| Wrong template (`acmart`/`IEEEtran` instead of the host/OpenProceedings style) | Format violation | Recompile in the correct template |
| Paper shape mismatched to contribution | Mis-routed review | Re-declare Regular / Experiments-&-Analysis / Vision correctly |
| Work under the 12-month EDBT ban in this format | Ineligible | Do not submit; wait out the cooldown or change format only if the rules allow |
| Double-blind cycle with identity leak | Anonymity violation | Re-anonymize PDF and artifact |
| No artifact / availability story | Scored against the paper (esp. Experiments & Analysis) | Add a runnable package or an explicit, justified exception |
| Same work under review elsewhere | Dual-submission exposure | Withdraw one venue; verify the concurrent-submission wording |

## Final-week order of operations

1. Freeze the body early; the argument and the measurements cannot churn late.
2. Confirm the cycle, the paper shape, and the resubmission-ban status against the live call.
3. Build the artifact and pin every workload, dataset version, and hardware detail.
4. Compile clean in the host/OpenProceedings template; check the per-shape page budget.
5. Fill every CMT field — subject areas that match your evidence, conflicts for every coauthor's
   institution and recent collaborators — a day early; late conflicts are the classic midnight
   failure.
6. Re-download the uploaded PDF and read it cold to confirm it is the file you meant.

## Reverify each cycle

- The number of cycles and the exact per-cycle deadline, author-feedback, and revision dates.
- The page budget and template revision per paper shape, and whether a short-paper category exists.
- Single- vs double-blind, the reproducibility/availability requirement, and any AI-disclosure rule
  — all cycle-volatile; none should be assumed stable.

## Output format

```text
[EDBT submission status] ready / blocked / needs work
[Cycle + shape] cycle N (<deadline>) / Regular | Experiments-&-Analysis | Vision
[Eligibility] resubmission-ban clear? yes/no
[Format] pages used (body), template compliance, per-shape budget met?
[Blind] policy this cycle + (if double-blind) anonymity clean/leaks
[Reproducibility] runnable artifact? provenance pinned?
[Fix queue] <ordered, with owners and dates before the cycle deadline>
```
