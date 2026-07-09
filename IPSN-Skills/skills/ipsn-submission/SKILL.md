---
name: ipsn-submission
description: Use when auditing an IPSN-lineage submission for HotCRP readiness, covering the IP-vs-SPOTS track choice, the ACM Primary Article Template and ≤12-page inclusive budget, the double-blind sweep for hardware/deployment papers, dataset/artifact links, and desk-reject triage — routed to the current successor (SenSys) call because IPSN no longer runs standalone.
---

# IPSN Submission

Run this audit before uploading. IPSN research papers were **double-blind**, on the **ACM Primary
Article Template**, **≤12 pages** inclusive of everything, submitted through **HotCRP** — and split
into the **IP** and **SPOTS** tracks. IPSN merged into **SenSys (Embedded AI and Sensing Systems)**
from 2025-2026, so reopen the current SenSys call first: the numbers below are the IPSN 2024 (23rd,
Hong Kong) snapshot read on 2026-07-09 (see `resources/official-source-map.md`) and the successor may
differ (SenSys 2026 posted full 12 / short 6 pages).

## Pick the track before the PDF

- **IP track** (Information Processing): algorithms, estimation, signal processing, inference,
  learning, localization. Reviewed by method reviewers who check soundness, baselines, and whether
  the information-processing claim holds.
- **SPOTS track** (Sensor Platforms, Tools and Design Methods): hardware, embedded software, tools,
  measurement, deployments. Reviewed for reusability, measured design trade-offs, and real-system
  evidence.

A mis-tracked paper draws the wrong reviewers and loses on the wrong axis. Confirm whether the
successor keeps this split or uses a single track with categories (待核实).

## Format and page budget

- **ACM Primary Article Template**, unmodified, two-column, **9 pt** (IPSN 2024). This is a compact
  two-column budget — not FSE's generous single-column journal budget; do not carry that habit over.
- **Page budget (verify per cycle):** IPSN 2024 posted **≤12 pages inclusive** of figures, tables,
  and references — there is no separate reference allowance. SenSys 2026 posted **12** (full) / **6**
  (short). Everything a reviewer must read to judge the paper lives inside the budget.
- Margins, font, and column layout are fixed by the template; editorial compression, not template
  tampering, recovers space.

## Double-blind sweep (hardware papers leak in unusual places)

IPSN is **double-blind**. Sensor-systems papers leak identity through hardware and deployment
artifacts more than software papers do:

```bash
# Mechanical pass on the submission PDF and any anonymized artifact archive
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'github\.com/[a-z0-9-]+|gitlab|zenodo\.org/record|doi\.org|acknowledg|grant|university|@[a-z0-9.]+\.edu' | head
unzip -l artifact.zip | grep -Ei '\.git/|\.DS_Store|/home/|/Users/|firmware.*owner' | head
```

The IPSN-specific leaks to hunt by eye:

- **Board photos and PCB silkscreen** showing a lab logo, university name, or a distinctive bench.
- **Oscilloscope / logic-analyzer screenshots** with a captured hostname or lab watermark.
- **Testbed and building names** ("our 4th-floor CS testbed", a named bridge or campus) that
  identify the institution.
- **Firmware repo owners, dataset DOIs, and IEEE DataPort links** that resolve to an author.
- **Deployment site coordinates or photos** that pinpoint an author's city or institution.

Re-host datasets and firmware behind an anonymizing archive before upload, and blur or crop
identifying hardware imagery.

## Dataset and artifact at submission

- Provide an **anonymized** dataset/firmware link or archive, and state what will be released after
  acceptance. IPSN's artifact and Best Research Artifact culture makes a missing release story a
  scored weakness, not a neutral choice.
- Log **energy/latency measurement conditions** and **ground truth** now; these cannot be
  reconstructed at review time.

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Main text over the page budget | Desk-reject-grade | Cut or move to the artifact; there is no separate reference allowance in the 12-page inclusive budget |
| Template altered (margins, shrunk font, single-column) | Named desk-reject ground | Recompile clean on the ACM template, recover space editorially |
| Identity leak in PDF, board photo, testbed name, or dataset link | Anonymity violation (desk-reject risk) | Re-anonymize imagery and re-host artifacts; scrub PDF metadata |
| Wrong track (platform paper in IP, or estimator in SPOTS) | Reviewer mismatch | Re-file under the matching track before the deadline |
| No dataset/firmware release story | Scored against the paper | Add an anonymized package + a release statement |
| Same work under review elsewhere | Dual-submission exposure | Withdraw one venue; verify the current concurrent-submission wording |

## Final-week order of operations

1. Confirm the **live successor (SenSys) call**, its deadline, and whether the track split survives.
2. Freeze the body early; measurements and figures can be re-plotted, the argument cannot.
3. Register title/abstract/authors/conflicts and pick the track before the cutoff.
4. Build the anonymized dataset/firmware package and place its link and release statement in the paper.
5. Run the mechanical anonymity checks on the *final* PDF and archive, plus an eyes-on pass over
   every board photo, scope screenshot, and testbed name.
6. Fill every HotCRP field — topic tags matching your track, conflicts for every coauthor's
   institution and recent collaborators — a day early.
7. Re-download the uploaded PDF and read it cold.

## Reverify each cycle

- That the venue is the current SenSys edition at CPS-IoT Week (IPSN does not run standalone).
- Track structure (IP/SPOTS vs single track), the page budget, and the ACM template revision.
- Rebuttal mechanics, dual-submission wording, artifact/award timing, and any AI-disclosure rule —
  all cycle-volatile.

## Output format

```text
[IPSN/SenSys submission status] ready / blocked / needs work
[Track] IP / SPOTS (or successor category), matches the primary novelty? yes/no
[Format] pages used, ACM template compliance (two-column 9 pt)
[Anonymity] clean / leaks: <PDF metadata | board photo | testbed name | dataset link>
[Dataset/artifact] anonymized link present? release statement present?
[Fix queue] <ordered, with owners and dates before the AoE cutoff>
```
