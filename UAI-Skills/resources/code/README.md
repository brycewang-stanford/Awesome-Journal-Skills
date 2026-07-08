# UAI Reproducibility Code Adapter

This directory routes UAI authors to the repository-level ML conference methods kit.
It is deliberately thin: UAI-specific *policy* lives in the skills and in
`../official-source-map.md`; reusable *tooling* lives in the shared kit so that twelve
conference packs do not carry twelve diverging copies.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Typical use for a UAI supplement

```bash
# Smoke-check the anonymous archive before it goes into the 50 MB supplementary ZIP
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/uai-supplement-staging
```

## UAI-specific expectations the generic kit will not check

The smoke checker validates package hygiene, not venue policy. On top of it, verify by
hand (or with the skills) the things that are distinctively UAI:

- The supplement is **optional reading** for reviewers — nothing decision-critical may
  exist only in the ZIP (see `../../skills/uai-supplementary/SKILL.md`).
- Appendices belong **inside the single submission PDF**, not in the archive
  (2026 rule; reverify each cycle).
- Inference artifacts should expose diagnostics — seeds plus R-hat/ESS for samplers,
  ELBO traces and restart rules for variational methods, coverage computation for
  interval methods (see `../../skills/uai-reproducibility/SKILL.md`).
- The archive must stay double-blind end to end: no git history, notebook author
  fields, tracker URLs, or home-directory paths.

This is not the economics/Stata kit used by the journal packs in this repository; do
not import DiD/IV/RDD tooling here.
