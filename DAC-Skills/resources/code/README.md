# DAC Replication-Package Code Adapter

This directory routes DAC authors to the repository-level shared tooling. It stays deliberately thin:
DAC-specific *policy* (double-blind review, the 6+1 budget, ACM-DL archival, the Research-vs-
Engineering track split, and the fact that DAC runs **no standing artifact-badging track**) lives in
the skills and in [`../official-source-map.md`](../official-source-map.md); reusable *tooling* lives
in the shared kits so packs do not carry diverging copies.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — anonymous-review and public-release checks that transfer to any replication package; read them
  through the EDA lens below (benchmarks/PDK/flow versions, not ML leaderboards).
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free smoke checker for package layout.
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  and [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — generic pre-submission scaffolding; adapt the latter only when you **reroute a rejected DAC paper
  to a journal (TCAD/TODAES)**, since DAC itself has historically had no author-response letter
  ([`../../skills/dac-author-response/SKILL.md`](../../skills/dac-author-response/SKILL.md)).

## Typical use for a DAC package

```bash
# Smoke-check the anonymized artifact before the Softconf upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/dac-artifact-staging
```

Treat the script as a layout smoke test only. Venue policy still comes from the current Call for
Contributions and the DAC skills for experiments, reproducibility, and (badge-free) artifact
packaging.

## DAC-specific checks the generic tooling cannot make

- **QoR claims trace to a benchmark run.** Every headline number (PPA, wirelength, WNS/TNS, coverage,
  runtime) maps to a script + the exact benchmark release (ISPD/EPFL/ISCAS/ITC/TAU/CircuitNet) that
  produces it ([`../../skills/dac-experiments/SKILL.md`](../../skills/dac-experiments/SKILL.md)).
- **Flow and technology are disclosed.** Tool versions (OpenROAD/ABC/Yosys or a commercial flow) and
  the PDK/standard-cell library are named; QoR is meaningless without the technology context
  ([`../../skills/dac-reproducibility/SKILL.md`](../../skills/dac-reproducibility/SKILL.md)).
- **Stochastic flows report seeds and variance.** For simulated-annealing/RL-based placement,
  routing, or partitioning, fixed seeds and multi-run spread — not a single lucky run.
- **ML-for-EDA splits are disjoint by design.** Train and test on **different** designs/netlists, and
  evaluate on unseen technology nodes; a leaked design invalidates the result.
- **Double-blind extends to the artifact.** At review time the linked repo/dataset is anonymized —
  no author/lab names, no personal GitHub, no cluster paths, no vendor-flow fingerprints — and
  reviewers are not obligated to open it ([`../../skills/dac-submission/SKILL.md`](../../skills/dac-submission/SKILL.md)).
- **No badge to chase.** DAC has historically run **no artifact-evaluation/badging track** (**待核实**
  per cycle); package for reviewer credibility and community reuse (DOI-archived, licensed) rather
  than an ACM badge ([`../../skills/dac-artifact-evaluation/SKILL.md`](../../skills/dac-artifact-evaluation/SKILL.md)).

This is not the econometrics/Stata kit used by the journal packs in this repository, and DAC evidence
is not empirical-SE or ML-leaderboard evidence: do not import DiD notebooks or accuracy-on-a-proxy
framing here. DAC evidence is measured design quality on recognized circuits.
