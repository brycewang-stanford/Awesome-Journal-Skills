# PPoPP Replication-Package Code Adapter

This directory routes PPoPP authors to the repository-level shared tooling. It stays deliberately
thin: PPoPP-specific *policy* (the double-blind review, the single rebuttal, the CGO-shared
artifact badges, the twin correctness+scalability bar) lives in the skills and in
[`../official-source-map.md`](../official-source-map.md); reusable *tooling* lives in the shared
kits so packs do not carry diverging copies.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — anonymous-review and public-release checks that transfer to any replication package.
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free smoke checker for package layout.
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  and [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — generic pre-submission and response scaffolding; adapt the latter to the short PPoPP rebuttal in
  [`../../skills/ppopp-author-response/SKILL.md`](../../skills/ppopp-author-response/SKILL.md).

## Typical use for a PPoPP package

```bash
# Smoke-check the anonymized artifact before the HotCRP upload (review-time)
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/ppopp-artifact-staging
```

Treat the script as a layout smoke test only. Venue policy still comes from the current
research-papers call and the PPoPP skills for experiments, reproducibility, and artifact
evaluation.

## PPoPP-specific checks the generic tooling cannot make

- **Correctness *and* scalability, not one or the other.** A replication package must reproduce the
  **scaling trend** (a core/thread sweep that regenerates the paper's curve) and ship the harness
  that supports the **correctness argument** (a model-checker or race-detector configuration), not
  just a single throughput number
  (`../../skills/ppopp-experiments/SKILL.md`).
- **The trend must survive a different machine.** Because PPoPP's artifact evaluators run on their
  own hardware, ship a **scaled-down configuration** whose curve shape matches the paper, state the
  **minimum configuration** on which the claim holds, and state the **tolerance** for "reproduced"
  (`../../skills/ppopp-reproducibility/SKILL.md`).
- **Parallel non-determinism is pinned.** Record exact CPU/GPU/topology, thread pinning/affinity,
  NUMA placement, seeds, warm-up, and frequency-scaling policy at run time — none of it can be
  reconstructed after the machine is released
  (`../../skills/ppopp-reproducibility/SKILL.md`).
- **Badge readiness is a post-acceptance task with PPoPP's own badge set.** Target **Functional or
  Reusable** plus **Results Reproduced** (PPoPP does **not** award "Results Replicated"), and secure
  the publisher-granted **Available** badge by depositing to a DOI-issuing archive
  (Zenodo/figshare/Software Heritage) — on the AE track's own, post-acceptance deadline
  (`../../skills/ppopp-artifact-evaluation/SKILL.md`).
- **Double-blind at review time.** The review-time package hides named machines/clusters, SLURM
  accounts, grant numbers, and personal-repo owners; de-anonymization happens only at camera-ready
  (`../../skills/ppopp-submission/SKILL.md`, `../../skills/ppopp-camera-ready/SKILL.md`).

This is not the econometrics/Stata kit used by the journal packs in this repository, and PPoPP
evidence is not ML-leaderboard evidence: do not import DiD notebooks or benchmark-score framing
here — import speedup curves, core sweeps, and correctness arguments.
