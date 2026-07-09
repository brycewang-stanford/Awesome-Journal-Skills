# IEEE ICSME Replication-Package Code Adapter

This directory routes ICSME authors to the repository-level shared tooling. It stays deliberately
thin: ICSME-specific *policy* (the single-round double-anonymous IEEE process, the early-decision
cut, ROSE-Festival IEEE badges, mining provenance) lives in the skills and in
[`../official-source-map.md`](../official-source-map.md); reusable *tooling* lives in the shared kits
so packs do not carry diverging copies.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — anonymous-review and public-release checks that transfer to any SE replication package.
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free smoke checker for package layout.
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  and [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — generic pre-submission and response scaffolding; adapt the latter to the single-round
  author-response rebuttal in [`../../skills/icsme-author-response/SKILL.md`](../../skills/icsme-author-response/SKILL.md).

## Typical use for an ICSME package

```bash
# Smoke-check the anonymized artifact before the EasyChair upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/icsme-artifact-staging
```

Treat the script as a layout smoke test only. Venue policy still comes from the current
research-papers call and the ICSME skills for experiments, reproducibility, and artifact evaluation.

## ICSME-specific checks the generic tooling cannot make

- **The evidence must be complete on submission.** ICSME has **no Major Revision round**: a missing
  analysis cannot be added later, so the artifact and paper must already support every scored claim
  (`../../skills/icsme-experiments/SKILL.md`, `../../skills/icsme-review-process/SKILL.md`).
- **Mining provenance is pinned.** For evolution studies, record repository SHAs, the corpus
  extraction date and time window, inclusion/exclusion criteria, and fork/duplicate/bot handling; a
  package that only ships the query re-samples rather than reproduces
  (`../../skills/icsme-experiments/SKILL.md`).
- **Anonymity includes your own systems.** Double-anonymity extends to not naming your own subject
  system or public org as the mined corpus if that reveals authorship
  (`../../skills/icsme-submission/SKILL.md`).
- **A data-availability statement exists and is honest.** It matches the anonymized archive;
  "available upon request" is a scored weakness under ROSE norms, not a neutral placeholder
  (`../../skills/icsme-reproducibility/SKILL.md`).
- **Badge readiness targets the IEEE scheme.** A DOI-issuing archive (Zenodo/figshare/Software
  Heritage), an open license, and evaluator-proof reuse docs target the IEEE **Open Research Object**
  and **Research Object Reviewed** badges in the Joint Artifact Evaluation Track and ROSE Festival —
  after acceptance, on a deadline shared with SCAM and VISSOFT
  (`../../skills/icsme-artifact-evaluation/SKILL.md`). Do **not** target ACM badge names here.

This is not the econometrics/Stata kit used by the journal packs in this repository, and ICSME
evidence is not ML-leaderboard evidence: do not import DiD notebooks or benchmark-score framing here.
