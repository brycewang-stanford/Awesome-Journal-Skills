# EuroSys Systems-Evaluation Code Adapter

This directory adapts the repo-level ML-conference reproducibility kit for EuroSys use.
The shared kit is generic experiment/artifact scaffolding — not an econometrics library
and not a substitute for the sysartifacts process described in
[`../../skills/eurosys-artifact-evaluation/SKILL.md`](../../skills/eurosys-artifact-evaluation/SKILL.md).

## Shared kit entry points

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

```bash
# Smoke-check a EuroSys artifact directory before AEC submission
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/eurosys-artifact
```

## What the generic kit cannot check for EuroSys

Run these by hand; they are venue-specific:

1. **Badge mapping** — does the package match the badge set you declared (Available needs
   a DOI archive, Functional needs the claims-to-commands map, Reproduced needs full-run
   scripts sized for AEC hardware)? See the current sysartifacts call.
2. **Hardware honesty** — the kit cannot know that your p99 numbers need a specific NIC
   or NUMA layout; the README must declare the floor and expected deviations.
3. **Double-blind state** — at submission time the mirror must be anonymized (history
   stripped, hostnames scrubbed); the kit does not scan for lab-identifying strings.
4. **Provenance ledger coverage** — every figure regenerable from raw logs with one
   command, per [`../../skills/eurosys-reproducibility/SKILL.md`](../../skills/eurosys-reproducibility/SKILL.md).

Policy always comes from [`../official-source-map.md`](../official-source-map.md) and the
live round pages, never from tooling defaults.
