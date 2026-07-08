# NSDI Reproducibility Code Adapter

This directory routes NSDI authors to the repository-wide ML/systems conference
reproducibility kit and records what that generic kit cannot check for a
networked-systems submission. It is deliberately not a copy of the economics
(Stata/DiD/IV/RDD) tooling used by the journal packs.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

```bash
# Smoke-check the artifact tree you intend to submit for badge evaluation
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/nsdi-artifact
```

## What the generic kit cannot verify for NSDI

The smoke checker inspects package hygiene (manifests, seeds, scripts). An NSDI
artifact lives or dies on things it cannot see:

- **Topology and hardware assumptions** — node counts, NIC speeds, RTTs, and switch
  configs that the paper's numbers depend on, and a documented downscaled variant for
  evaluators without a testbed.
- **Trace availability and licensing** — whether the workloads behind the headline
  figures can legally ship, and what the synthetic substitute preserves
  (`nsdi-reproducibility`).
- **Time-sensitive behavior** — congestion, failover, and tail-latency results vary
  with background load; the artifact needs expected-variance notes, not just
  expected-output files.
- **Community Award eligibility** — code/data must be public by the final-papers
  deadline to compete (`nsdi-artifact-evaluation`).

Venue policy always comes from [`../official-source-map.md`](../official-source-map.md)
and the live pages it points to, not from this adapter.
