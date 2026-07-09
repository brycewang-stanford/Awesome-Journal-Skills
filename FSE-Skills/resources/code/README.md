# ESEC/FSE Replication-Package Code Adapter

This directory routes FSE authors to the repository-level shared tooling. It stays deliberately
thin: FSE-specific *policy* (the journal-style PACMSE process, double-anonymous "heavy" review,
ACM badging, data availability) lives in the skills and in
[`../official-source-map.md`](../official-source-map.md); reusable *tooling* lives in the shared
kits so packs do not carry diverging copies.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — anonymous-review and public-release checks that transfer to any SE replication package.
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free smoke checker for package layout.
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  and [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — generic pre-submission and response scaffolding; adapt the latter to the Major Revision
  response letter in [`../../skills/fse-author-response/SKILL.md`](../../skills/fse-author-response/SKILL.md).

## Typical use for an FSE package

```bash
# Smoke-check the anonymized artifact before the HotCRP upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/fse-artifact-staging
```

Treat the script as a layout smoke test only. Venue policy still comes from the current
research-papers call and the FSE skills for experiments, reproducibility, and artifact
evaluation.

## FSE-specific checks the generic tooling cannot make

- **The response letter is anonymous too.** FSE's "heavy" double-anonymity extends into the
  Major Revision round: the letter that answers reviewers must not name authors, institutions,
  or reveal a repository owner (`../../skills/fse-author-response/SKILL.md`).
- **A Data Availability statement exists and is honest.** It matches what the anonymized archive
  actually contains; "available upon request" is a scored weakness, not a neutral placeholder
  (`../../skills/fse-reproducibility/SKILL.md`).
- **Empirical provenance is pinned.** For mining or LLM studies, record repository SHAs, the
  corpus extraction date, model identifiers with dates, and cache raw model outputs — a package
  that needs live API calls re-samples rather than reproduces
  (`../../skills/fse-experiments/SKILL.md`).
- **Badge readiness is a post-acceptance task.** A DOI-issuing archive (Zenodo/figshare/Software
  Heritage), an open license, and evaluator-proof reuse docs target the ACM
  Available/Functional/Reusable/Reproduced badges after acceptance, on the artifact track's own
  deadline (`../../skills/fse-artifact-evaluation/SKILL.md`).

This is not the econometrics/Stata kit used by the journal packs in this repository, and FSE
evidence is not ML-leaderboard evidence: do not import DiD notebooks or benchmark-score framing
here.
