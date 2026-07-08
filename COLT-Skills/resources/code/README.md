# COLT Numerical-Illustration Code Adapter

This directory adapts the repo-level ML-conference kit for COLT's reality: a
theory-first venue where most papers ship **no code at all**, and where the artifact
that matters is the proof appendix (see
[`../../skills/colt-artifact-evaluation/SKILL.md`](../../skills/colt-artifact-evaluation/SKILL.md)).
Use the shared kit only for the minority case — a paper carrying a numerical
illustration of a bound, separation, or phase transition.

## Shared Kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## COLT-specific usage notes

- Apply the kit's seed/replication discipline to illustration scripts, but skip its
  benchmark-oriented sections (baseline tuning budgets, dataset provenance) — they
  answer questions COLT does not ask.
- The 2026 cycle had no code-upload channel; during review, an illustration's
  procedure lives in the appendix as prose plus pseudocode, and any linked repository
  must be anonymized.
- Post-acceptance, release the (usually tiny) script publicly and link it from the
  arXiv version, since the PMLR PDF is frozen at camera-ready.

```bash
# Smoke-check a post-acceptance illustration package before releasing it:
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/colt-illustration-package
```

The script is a generic smoke check only. Venue policy comes from
[`../official-source-map.md`](../official-source-map.md), the live CFP, and the
`colt-experiments` / `colt-reproducibility` / `colt-supplementary` skills.
