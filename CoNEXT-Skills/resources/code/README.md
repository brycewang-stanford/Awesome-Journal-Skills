# ACM CoNEXT Replication-Package Code Adapter

This directory routes CoNEXT authors to the repository-level shared tooling. It stays deliberately
thin: CoNEXT-specific *policy* (the two-cycle PACMNET process, double-anonymous review, the one-shot
major revision, the reproducibility committee and optional ACM badges) lives in the skills and in
[`../official-source-map.md`](../official-source-map.md); reusable *tooling* lives in the shared
kits so packs do not carry diverging copies.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — anonymous-review and public-release checks that transfer to any networking replication package.
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free smoke checker for package layout.
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  and [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — generic pre-submission and response scaffolding; adapt the latter to the one-shot major-revision
  response letter in [`../../skills/conext-author-response/SKILL.md`](../../skills/conext-author-response/SKILL.md).

## Typical use for a CoNEXT package

```bash
# Smoke-check the anonymized artifact before the HotCRP upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/conext-artifact-staging
```

Treat the script as a layout smoke test only. Venue policy still comes from the current CoNEXT CFP
and the CoNEXT skills for experiments, reproducibility, and artifact evaluation.

## CoNEXT-specific checks the generic tooling cannot make

- **The response letter is anonymous too.** CoNEXT's double-anonymity extends into the one-shot
  major-revision round: the letter that answers the "minimum necessary changes" must not name
  authors, institutions, testbeds, or reveal a repository owner
  (`../../skills/conext-author-response/SKILL.md`).
- **Trace and config provenance is pinned.** For measurement or systems studies, record capture
  vantage points and dates, anonymization of IPs/identifiers, switch/NIC firmware and OS versions,
  and testbed topology — a package that cannot rebuild the environment re-runs a different
  experiment rather than reproducing yours (`../../skills/conext-experiments/SKILL.md`).
- **Badge opt-in is a submission-time task, not a post-acceptance one.** Eligibility for the
  optional ACM reproducibility badges requires **opting in before the paper submission deadline**;
  the one-page artifact description then goes to the reproducibility committee within a week of
  acceptance (`../../skills/conext-artifact-evaluation/SKILL.md`).
- **A DOI-issuing archive backs the availability claim.** Zenodo/figshare/Software Heritage with an
  open license and evaluator-proof reuse docs target the ACM Available/Functional/Reusable badges;
  "available upon request" is a scored weakness, not a neutral placeholder
  (`../../skills/conext-reproducibility/SKILL.md`).

This is not the econometrics/Stata kit used by the journal packs in this repository, and CoNEXT
evidence is not ML-leaderboard evidence: do not import DiD notebooks or benchmark-score framing
here. CoNEXT evidence is testbeds, deployments, and reproducible measurement.
