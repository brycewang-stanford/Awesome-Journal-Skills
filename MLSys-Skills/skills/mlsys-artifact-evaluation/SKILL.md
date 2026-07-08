---
name: mlsys-artifact-evaluation
description: Use when packaging an accepted MLSys paper's code, configs, and measurement scripts for the venue's post-acceptance artifact evaluation, targeting the Availability, Functional, and Reproducible badges, writing the Artifact Appendix, handling hardware that AE reviewers cannot access, and answering anonymous evaluator questions.
---

# MLSys Artifact Evaluation

Use this after acceptance, when deciding whether and how to enter MLSys artifact
evaluation. AE is one of this venue's defining institutions: a separate committee
evaluates how well artifacts support the paper's claims and awards badges. In the 2026
cycle (verified 2026-07-08): submission of artifact abstract, paper PDF, and Artifact
Appendix to a dedicated AE site by March 8; evaluation window March 8 - April 8;
badges for **Availability**, **Functional**, and **Reproducible**; anonymous
reviewer-author interaction during evaluation; and a small number of Distinguished
Artifact Awards for exceptional packages. Reopen the current Call for Artifact
Evaluations before relying on any of these mechanics.

## Badge strategy — decide the target first

| Badge | What evaluators check | Typical cost to authors |
|---|---|---|
| Availability | Artifact is publicly and permanently retrievable (public GitHub-style link expected in the appendix) | Hours: license, public repo, archival snapshot |
| Functional | The artifact runs: documented, complete relative to the paper, exercisable end-to-end | Days: install path, smoke test, small-scale example |
| Reproducible | Evaluators regenerate the paper's key results following your instructions | Weeks: automation, hardware plan, tolerance definitions |

Claim badges honestly. Requesting Reproducible when the headline table needs a cluster
the committee cannot access converts a friendly process into a failed one; requesting
only Availability+Functional with a clear statement of why is respected.

## The hardware problem — MLSys AE's hardest part

Most MLSys results are performance results on specific hardware. Solve this explicitly
in the appendix rather than hoping:

- **Tier the claims.** Separate results reproducible on one commodity GPU (or CPU) from
  results needing an 8-GPU node from results needing a cluster. Ask for the Reproducible
  badge on the tiers evaluators can actually run.
- **Scale-down targets.** Provide a reduced configuration (smaller model, shorter trace)
  whose *trend* matches the paper — and state the expected numbers for that reduced
  configuration, since evaluators cannot compare against a table they cannot reproduce.
- **Relative, not absolute, tolerances.** Performance varies across machines; define
  success as "speedup over the included baseline within ±15%" rather than absolute
  throughput.
- If you can offer supervised access to your hardware, check whether the current AE call
  permits it; do not assume.

## Package skeleton evaluators expect

```dockerfile
# Dockerfile — pin the system layer, not just Python
FROM nvidia/cuda:12.4.1-devel-ubuntu22.04
RUN apt-get update && apt-get install -y git python3.11 python3-pip
COPY requirements.lock /w/requirements.lock          # exact versions, hash-pinned
RUN pip install --no-cache-dir -r /w/requirements.lock
COPY . /w
WORKDIR /w
# One command per claim tier:
#   make smoke        (<10 min, any GPU)   -> Functional
#   make table3       (~1 h, 1x A100/H100) -> Reproducible tier 1
#   make fig6-scaled  (reduced trace, expected: 1.5-1.7x over baseline)
CMD ["make", "smoke"]
```

- README with: claims-to-commands map, hardware/time requirements per command, and a
  "what should I see" block for every command.
- All baselines included at the versions and configurations used in the paper — a
  package that reproduces your system but not the comparison reproduces nothing.
- Logged outputs from your own runs, so evaluators can diff behavior before burning
  GPU-hours.
- Traces, datasets, or generators for the workloads; if a workload is proprietary,
  ship a synthetic surrogate and label the substitution honestly.

## Artifact Appendix skeleton

The appendix is the evaluator's map; in 2026 it was submitted with the artifact abstract
and paper PDF to the AE site. Whatever template the current call mandates, cover:

```text
A.1 Abstract           what the artifact contains, one paragraph
A.2 Claims supported   paper claim -> command -> expected output -> tolerance
A.3 Requirements       hardware (per tier), software, disk, network access,
                       time-to-first-result and time-to-full-reproduction
A.4 Setup              container build or install path; offline fallback for
                       anything fetched from the network at build time
A.5 Experiment map     make targets / scripts per figure and table number
A.6 Known deviations   results that vary by hardware and by how much;
                       proprietary workloads replaced by surrogates
A.7 Reusability        how to point the artifact at new models/workloads —
                       this is what separates award-level artifacts
```

Write A.3 pessimistically: an evaluator who discovers an undeclared 200GB download or
a hidden internet dependency mid-window will not restart with goodwill.

## During the evaluation window

- Interaction is anonymous and mediated; respond within a day — the window is
  finite (one month in 2026) and a stuck evaluator is a failed badge.
- Treat every evaluator failure as a packaging bug to fix and re-push, not a user error
  to explain away; committees typically allow artifact updates during evaluation.
- Keep one author on call who can debug environment issues; the most common failure
  mode is driver/container mismatch on the evaluator's machine, not your code.

## Why bother

Badges appear with the paper and signal to this community — where results are routinely
questioned as hardware-specific — that a third party ran your code. The Distinguished
Artifact Award exists because MLSys treats the artifact as part of the scholarship, and
a badged artifact keeps producing citations after the conference ends.

## Cycle-volatility warnings

- Badge names, the AE site, deadlines, and whether AE remains post-acceptance-optional
  are all per-cycle decisions; the 2026 mechanics above are anchors to verify.
- The Artifact Appendix template, if one is mandated, comes from the current AE call.

## Output format

```text
[Badges targeted] availability / +functional / +reproducible (per claim tier)
[Claim tiers] <claim -> hardware needed -> reproducible by AE? >
[Package status] <docker/README/baselines/workloads/logged-outputs>
[Scale-down plan] <reduced configs + expected numbers>
[On-call owner] <person for the evaluation window>
[Gaps before AE deadline] <ordered list>
```
