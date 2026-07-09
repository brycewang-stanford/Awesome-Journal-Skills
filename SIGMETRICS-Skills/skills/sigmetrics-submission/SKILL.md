---
name: sigmetrics-submission
description: Use when auditing an ACM SIGMETRICS submission for HotCRP readiness, covering the choice among the three rolling deadlines (summer/fall/winter), the separate abstract-registration step, the 20-page single-column acmsmall budget plus unlimited references, double-anonymous review (and the Operational Systems Track exception), track selection, POMACS publication, and desk-reject triage before the AoE cutoff.
---

# SIGMETRICS Submission

Run this audit before uploading to the per-deadline SIGMETRICS HotCRP site. SIGMETRICS research
papers are published as **journal articles in POMACS** (Proceedings of the ACM on Measurement and
Analysis of Computing Systems), submitted on a **three-deadlines-per-year rolling model**, so the
submission is judged like a journal manuscript that also earns a conference slot. Every number
below was read from the SIGMETRICS 2026/2027 calls on 2026-07-09 via search renderings (see
`resources/official-source-map.md`); treat them as a one-cycle snapshot and reopen the live call
first.

## Choose the deadline first

SIGMETRICS has **three deadlines a year** — summer, fall, winter — each on its own HotCRP site.
This is the biggest departure from a single-annual-deadline conference:

- Every deadline feeds the same POMACS journal; there is no "main" deadline.
- Papers accepted from the **summer and fall** deadlines appear in POMACS **before** the
  conference; a winter acceptance publishes in the following issue. Pick the deadline whose
  notification and publication timing fits your goals (graduation, a job-market cycle, the
  conference you want to present at).
- 2026-cycle dates (verify per cycle): **Summer** abstract Jul 22 / paper Jul 29 2025;
  **Fall** abstract Oct 7 / paper Oct 14 2025; **Winter** abstract Jan 6 / paper Jan 13 2026. All
  23:59 **AoE**, hard. The live next target as of 2026-07-09 is the **SIGMETRICS 2027** summer
  round (abstract Jul 3, 2026; paper deadline 待核实).

## The two-step deadline

Each deadline separates **abstract registration** from **paper submission**, both AoE:

- **Abstract registration** locks title, abstract, authors, conflicts, and **track** roughly a
  week early. Miss it and the system will not accept the PDF later.
- **Paper submission** uploads the anonymized PDF a week after. Register with the *real* title and
  abstract — the abstract drives reviewer bidding.

## Track selection

Select the track that matches your evidence on the submission site:

- **Theory** (stochastic processes, queueing, scheduling, caching theory, algorithms, control).
- **Measurement & Applied Modeling** (principled measurement/simulation of real systems —
  networking, distributed systems, architecture, cloud, edge/IoT, HPC).
- **Learning** (ML/AI algorithm design and analysis, or learning *for* systems, with guarantees).
- **Operational Systems Track** (deployed systems in significant real-world use).

Pick **one** track; a second only for genuinely interdisciplinary work. The full track set/count
is cycle-volatile (**待核实**).

## Format and page budget

- **ACM `acmsmall`** single-column template, unmodified. This is the journal (POMACS) format, not a
  two-column conference style.
- **Page budget (verify per cycle):** SIGMETRICS 2026 posts **up to 20 pages** of technical content
  including all tables and figures, **plus unlimited pages for references**. No changes to margins,
  spacing, or font sizes from the style files.
- Editorial compression, not template tampering, is how you recover space. A proof-heavy paper that
  only fits by shrinking the model description is over-scoped for the body — move derivations to an
  appendix (still within the reviewed pages unless the call says otherwise).

## Double-anonymous sweep

SIGMETRICS runs **double-anonymous** ("double-blind") review: make a good-faith effort to
anonymize; do not identify yourself explicitly or by implication.

```bash
# Mechanical pass on the submission PDF and any anonymized artifact archive
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'github\.com/[a-z0-9-]+|our (system|prior) work|acknowledg|grant|university of' | head
unzip -l artifact.zip | grep -Ei '\.git/|\.DS_Store|/home/|/Users/' | head
```

The SIGMETRICS-specific leaks: a system named after your group, a trace whose provenance names your
institution, a self-citation phrased in the first person, a cluster path in a simulation script.
**Exception:** the **Operational Systems Track** may reveal the deploying organization or the
deployed system where needed — confirm which track's rules apply before scrubbing.

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Technical content over 20 pages | Desk-reject-grade | Cut or move to an appendix; references are unlimited but do not absorb body text |
| Two-column or non-acmsmall template | Named desk-reject ground | Recompile in single-column acmsmall |
| Identity leak in PDF, plots, or code (non-Operational track) | Anonymity violation | Re-anonymize and re-host; scrub PDF metadata |
| Abstract not registered by the earlier date | No submission slot exists | Nothing fixes this post-AoE — calendar it now |
| Wrong track selected | Poor reviewer match | Fix at registration; a second track only if truly interdisciplinary |
| Same paper under review elsewhere (incl. a paper in one-shot revision here) | Simultaneous-submission violation | Withdraw one; a paper under one-shot revision counts as under submission |

## Final-week order of operations

1. Choose the deadline and confirm its abstract and paper dates on the current HotCRP site.
2. Freeze the model/theorem and the evaluation early; references can churn, the argument cannot.
3. Register title/abstract/authors/conflicts/track before the registration cutoff.
4. Build the anonymized artifact (model, seeded simulator, trace scripts) and reference it.
5. Run the mechanical anonymity checks on the *final* PDF and archive, not drafts.
6. Re-download the uploaded PDF and read it cold to confirm it is the file you meant.

## Reverify each cycle

- The three deadline dates and abstract-vs-paper offsets (they move every cycle).
- The page budget and which acmsmall revision is required.
- The track list and each track's anonymity policy (Operational Systems differs).
- Whether an artifact/reproducibility track runs and its timing.

## Output format

```text
[SIGMETRICS submission status] ready / blocked / needs work
[Deadline] summer / fall / winter <cycle> — abstract + paper dates confirmed?
[Registration] title/abstract/authors/conflicts/track locked by the earlier deadline? yes/no
[Format] pages used (body), acmsmall single-column compliance
[Anonymity] clean / leaks: <where> (note Operational-track exception if applicable)
[Fix queue] <ordered, with owners and dates before the AoE cutoff>
```
