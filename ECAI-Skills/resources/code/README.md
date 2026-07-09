# ECAI Reproducibility / Supplementary Code Adapter

This directory routes ECAI authors to the repository-level shared tooling. It stays deliberately
thin: ECAI-specific *policy* (the FAIA vs IJCAI-proceedings regime, double-blind review, the
two-deadline flow, PAIS routing, open-access proceedings) lives in the skills and in
[`../official-source-map.md`](../official-source-map.md); reusable *tooling* lives in the shared
kits so packs do not carry diverging copies.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — anonymous-review and public-release checks that transfer to any AI supplementary package.
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free smoke checker for package layout.
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  and [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — generic pre-submission and response scaffolding; adapt the latter to the single ECAI rebuttal
  window in [`../../skills/ecai-author-response/SKILL.md`](../../skills/ecai-author-response/SKILL.md).

## Typical use for an ECAI package

```bash
# Smoke-check the anonymized supplementary package before the paper deadline
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/ecai-supplementary-staging
```

Treat the script as a layout smoke test only. Venue policy still comes from the current call and
the ECAI skills for experiments, reproducibility, and supplementary material.

## ECAI-specific checks the generic tooling cannot make

- **The page budget is tight and hard.** The reviewed claim must be supported inside **7 pages**
  of body (references are the only overflow: 1 page standalone, 2 pages in IJCAI-ECAI 2026). A
  supplementary package holds proofs, extra tables, and code — it must not carry material a
  reviewer needs to *judge* the paper (`../../skills/ecai-supplementary/SKILL.md`).
- **Double-blind extends to the package.** Anonymize the supplementary archive, repository
  owners, dataset acknowledgements, and any tool named after your group; ECAI review is
  double-blind and the summary-reject phase can catch a de-anonymizing leak early
  (`../../skills/ecai-submission/SKILL.md`).
- **Formal contributions ship proofs, not just code.** Much of ECAI is KR, planning,
  argumentation, and theory — the "artifact" is often a **complete proof appendix** and a
  reference implementation, not an ML leaderboard. Match the package to the contribution shape
  (`../../skills/ecai-reproducibility/SKILL.md`, `../../skills/ecai-experiments/SKILL.md`).
- **No ACM/IEEE badge scheme applies.** ECAI/FAIA has **no ACM artifact-badging pipeline**; the
  reproducibility story is carried by the paper and its supplement, evaluated by the same
  reviewers, not by a separate badge committee (`../../skills/ecai-artifact-evaluation/SKILL.md`).
- **Provenance is pinned for empirical work.** For learning or mining studies, record dataset
  versions, seeds, model identifiers with dates, and cache raw outputs — a package needing live
  API calls re-samples rather than reproduces (`../../skills/ecai-experiments/SKILL.md`).

This is not the econometrics/Stata kit used by the journal packs in this repository, and ECAI
evidence is not ML-leaderboard-only evidence: do not import DiD notebooks or a single-benchmark
score framing here.
