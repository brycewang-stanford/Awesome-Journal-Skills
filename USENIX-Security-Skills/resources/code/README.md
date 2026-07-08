# USENIX Security Reproducibility Code Adapter

This directory routes USENIX Security authors to the repository-level conference methods
kit. It is deliberately thin: USENIX Security-specific *policy* lives in the skills and in
`../official-source-map.md`; reusable *tooling* lives in the shared kit so that many
conference packs do not carry many diverging copies.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Typical use for a USENIX Security artifact

```bash
# Smoke-check the artifact package before submitting to Phase-1/Phase-2 evaluation
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/usenixsec-artifact-staging
```

Use the script as package hygiene only — it does not judge venue policy.

## USENIX Security-specific expectations the generic kit will not check

On top of the smoke checker, verify by hand (or with the skills) the things that are
distinctively USENIX Security:

- The paper contains everything needed to **evaluate** the work; the artifact contains
  everything needed to **redo** it. Reviewers are not obliged to run the artifact during
  review, so nothing decision-critical may live only there
  (see `../../skills/usenixsec-supplementary/SKILL.md`).
- The **Open Science appendix** must name resolvable artifact locations (anonymous mirror
  at submission, permanent/DOI-backed archive at camera-ready), and Phase-1 availability
  verification is a **condition of acceptance**
  (see `../../skills/usenixsec-artifact-evaluation/SKILL.md`).
- **Security artifacts carry hazards the generic checker ignores:** exploit/scanner code
  must target a bundled testbed, never the live internet; document the blast radius;
  ship a scaled-down run that reproduces the trend in under an hour alongside the full
  campaign (see `../../skills/usenixsec-reproducibility/SKILL.md`).
- The package must stay **double-blind end to end** at submission: no git history, author
  metadata, tracker URLs, institutional paths, or named-org repository links.
- **Withheld artifacts need a justification and a substitute procedure** — released
  aggregation code where raw data is sensitive, instruments where transcripts are
  human-subjects material.

This is not the economics/Stata kit used by the journal packs in this repository; do not
import DiD/IV/RDD tooling here.
