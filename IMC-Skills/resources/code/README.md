# ACM IMC Replication-Package Code Adapter

This directory routes IMC authors to the repository-level shared tooling. It stays deliberately
thin: IMC-specific *policy* (the two-deadline One-Shot-Revision process, double-blind review, the
mandatory Ethics section, the artifact-availability declaration, dataset release) lives in the
skills and in [`../official-source-map.md`](../official-source-map.md); reusable *tooling* lives in
the shared kits so packs do not carry diverging copies.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — anonymous-review and public-release checks that transfer to any measurement replication
  package.
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free smoke checker for package layout.
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  and [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — generic pre-submission and response scaffolding; adapt the latter to the One-Shot-Revision
  resubmission in [`../../skills/imc-author-response/SKILL.md`](../../skills/imc-author-response/SKILL.md).

## Typical use for an IMC package

```bash
# Smoke-check the anonymized dataset/code artifact before the HotCRP upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/imc-artifact-staging
```

Treat the script as a layout smoke test only. Venue policy still comes from the current call and
the IMC skills for experiments, reproducibility, and artifact evaluation.

## IMC-specific checks the generic tooling cannot make

- **The artifact-availability declaration is honest and matches the archive.** IMC requires a
  full/partial/none declaration at submission; "available on request" is not availability, and a
  "none" needs a stated legitimate reason (proprietary/privacy). Accepted papers are shepherded
  to deliver what was promised (`../../skills/imc-reproducibility/SKILL.md`,
  `../../skills/imc-artifact-evaluation/SKILL.md`).
- **The Ethics section exists and is real.** IMC can reject a paper with no Ethics section. For
  human-subjects/user-data work, the IRB determination is documented (anonymized); for active
  measurement, the paper argues Belmont-style beneficence and a responsible-disclosure plan
  (`../../skills/imc-submission/SKILL.md`, `../../skills/imc-experiments/SKILL.md`).
- **Measurement provenance is pinned.** Record vantage points (locations, ASes, probe types),
  measurement dates and durations, tool versions, target lists with capture dates, and the
  network conditions — a measurement of a moving Internet cannot be re-run identically, so the
  captured data and its provenance *are* the reproducibility (`../../skills/imc-experiments/SKILL.md`).
- **Datasets are released with schema and documentation.** A Community Contribution Award-grade
  release has a documented schema, collection methodology, a license, and a DOI-issuing archive —
  public by the camera-ready deadline (`../../skills/imc-artifact-evaluation/SKILL.md`).
- **Double-blind extends to infrastructure.** Anonymize not only names and links but
  vantage-point and probe details that uniquely identify your group or testbed
  (`../../skills/imc-submission/SKILL.md`).

This is not the econometrics/Stata kit used by the journal packs in this repository, and IMC
evidence is not ML-leaderboard evidence: do not import DiD notebooks or benchmark-score framing
here.
