# ICSE Replication-Package Code Adapter

This directory routes ICSE authors to the repository-level shared tooling. It
stays thin on purpose: ICSE-specific *policy* (open science, badging,
page-model placement) lives in the skills and in
[`../official-source-map.md`](../official-source-map.md); reusable *tooling*
lives in the shared kits so conference packs do not carry diverging copies.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — anonymous-review and public-release checks that transfer directly to SE
  replication packages.
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free smoke checker for package layout.
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  and [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — generic pre-submission and response scaffolding; adapt the latter to the
  Major Revision ledger in `../../skills/icse-author-response/SKILL.md`.

## Typical use for an ICSE package

```bash
# Smoke-check the anonymized replication package before the HotCRP upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/icse-replication-staging
```

## ICSE-specific checks the generic tooling cannot make

- **Everything decision-critical is inside the 10 pages** — the package is
  evidence, not overflow (see `../../skills/icse-supplementary/SKILL.md`).
- **The Data Availability section exists after the Conclusion** and matches
  what the package actually contains (`../../skills/icse-reproducibility/SKILL.md`).
- **Mining provenance is pinned** — repo SHAs, corpus extraction date, and the
  extracted dataset archived, not just the queries.
- **LLM evidence is cached** — raw model responses stored, model identifiers
  versioned and dated; a package requiring live API calls cannot reproduce,
  only re-sample.
- **Badge-readiness** — DOI-issuing archive, open license, reuse docs — is a
  post-acceptance January deadline, not a submission one
  (`../../skills/icse-artifact-evaluation/SKILL.md`).

This is not the econometrics/Stata kit used by the journal packs in this
repository, and SE evidence is not ML-leaderboard evidence: do not import DiD
notebooks or benchmark-score framing here.
