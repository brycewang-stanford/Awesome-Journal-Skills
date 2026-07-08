# SODA Verification Code Adapter

SODA is a theorem-led venue: there is no artifact track and no reproducibility
checklist. The computational objects a SODA author actually ships are (a)
machine-checked proof steps with certificates and (b) optional illustration
experiments — see [`../../skills/soda-artifact-evaluation/SKILL.md`](../../skills/soda-artifact-evaluation/SKILL.md)
and [`../../skills/soda-experiments/SKILL.md`](../../skills/soda-experiments/SKILL.md).
For those, the repo's shared ML-conference kit is reusable as a *packaging* smoke
check even though SODA has no checklist to satisfy:

## Shared kit (packaging checks only)

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

```bash
# Smoke-check an anonymity-safe verification archive before linking it:
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/verification-archive
```

## What the generic kit cannot check (SODA-specific, do by hand)

1. **Certificate sufficiency** — that `check.py` succeeding actually implies the
   lemma (the reduction must be argued in the paper, not the README).
2. **Determinism** — rerun the whole check twice from a clean clone; any
   nondeterminism in a proof-supporting computation is a correctness bug.
3. **Anonymity of the hosting** — the archive URL must not name an author or
   lab (lightweight double-blind still covers linked material at submission).
4. **Claim-class labels on experiments** — illustration / evidence / motivation,
   per `soda-experiments`; no script can classify intent.

If the experiments are the contribution, stop packaging for SODA and route to
ALENEX's artifact evaluation instead (`../official-source-map.md`, source 7).
