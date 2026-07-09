# ASE Replication-Package Code Adapter

This directory routes ASE authors to the repository-level shared tooling. It stays deliberately
thin: ASE-specific *policy* (the Accept/Revision/Reject model, the early-rejection stage,
double-anonymous review, ACM artifact badging, the mandatory Data Availability Statement, dual
IEEE/ACM proceedings) lives in the skills and in
[`../official-source-map.md`](../official-source-map.md); reusable *tooling* lives in the shared
kits so packs do not carry diverging copies.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — anonymous-review and public-release checks that transfer to any SE replication package.
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free smoke checker for package layout.
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  and [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — generic pre-submission and response scaffolding; adapt the latter to the ASE rebuttal and the
  revision-round summary-of-changes in
  [`../../skills/ase-author-response/SKILL.md`](../../skills/ase-author-response/SKILL.md).

## Typical use for an ASE package

```bash
# Smoke-check the anonymized artifact before the HotCRP upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/ase-artifact-staging
```

Treat the script as a layout smoke test only. Venue policy still comes from the current
research-track call and the ASE skills for experiments, reproducibility, and artifact evaluation.

## ASE-specific checks the generic tooling cannot make

- **A Revision is criteria-bound, and the summary-of-changes is anonymous too.** ASE's Revision
  outcome commits reviewers to accept-in-principle against explicit criteria; the point-by-point
  summary-of-changes that answers them must stay double-anonymous — no author names, no revealed
  repository owner (`../../skills/ase-author-response/SKILL.md`).
- **The Data Availability Statement is mandatory and counts inside the 10 pages.** It sits after
  the Conclusions, describes what exists and where it will live, and must match what the anonymized
  archive actually contains; "available upon request" reads as a weakness
  (`../../skills/ase-reproducibility/SKILL.md`).
- **Tool provenance is pinned.** Automated-SE artifacts are usually *tools*: pin the exact commit,
  the subject-system versions and SHAs, the analysis configuration, seeds, and — for LLM-based
  components — model identifiers with dates and cached outputs, so a package reproduces rather than
  re-samples (`../../skills/ase-experiments/SKILL.md`).
- **Badge readiness targets Available and Reusable on a separate deadline.** A DOI-issuing archive
  (Zenodo / figshare / Software Heritage), an open license, and evaluator-proof reuse docs target
  the ACM Artifacts Available / Reusable badges shown on the paper's front page in *both* IEEE
  Xplore and the ACM DL (`../../skills/ase-artifact-evaluation/SKILL.md`).

This is not the econometrics/Stata kit used by the journal packs in this repository, and ASE
evidence is not ML-leaderboard evidence: do not import DiD notebooks or benchmark-score framing
here.
