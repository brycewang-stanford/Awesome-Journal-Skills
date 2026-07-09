---
name: sigcomm-reproducibility
description: Use when strengthening the reproducibility evidence of an ACM SIGCOMM paper — topology and testbed ledgers, traffic workload and trace provenance, configuration and version pinning, tail-percentile run counts and variance, legal data-release decisions, and consistency between the paper's claims and the artifact that backs them.
---

# SIGCOMM Reproducibility

Use this before submission and again before the artifact deadline. SIGCOMM's culture treats a
result as a claim a stranger should be able to rebuild; reproducibility here is largely about
whether the **network conditions** behind a number are recorded well enough to recreate.
Reopen the current Call for Artifacts to confirm the process for this edition.

## Evidence map

- Map each reported number to a rebuildable location: a script, a logged run, a config, and
  the figure it feeds.
- For every measurement, record the **topology** (physical or emulated), the **traffic**
  (workload generator or trace, with provenance), the **configuration** (every parameter),
  and the **environment** (kernel, NIC, switch firmware, data-plane toolchain).
- For any stochastic result, report the **run count**, the seed or workload driver, and the
  variance behind each percentile — a lone 99th-percentile number with no replication is not
  reproducible.
- Decide early what can legally ship: production traces and topologies often cannot, so plan a
  substitute with matching statistical character rather than discovering the block at the
  deadline.
- Keep the paper and the artifact consistent; a figure the artifact cannot regenerate is a
  reproducibility gap reviewers and the AEC both notice.

## The four ledgers

| Ledger | What it records | Failure it prevents |
|---|---|---|
| Topology | Nodes, links, capacities, buffer sizes, emulation vs. hardware | "Which topology produced Figure 6?" |
| Traffic | Workload distribution or trace, provenance, which figure used it | Numbers that cannot be tied to an input |
| Configuration | Every parameter and its value per experiment | Silent knob changes between runs |
| Run | Seeds, replication counts, timestamps, variance | Percentiles with no reproducible basis |

Maintaining these while you run is cheap; reconstructing them after the deadline is
error-prone and often impossible.

## Degrees of reproducibility

```text
Turnkey     : one command rebuilds each figure from logged runs on a documented setup
Scripted    : scripts exist but need hardware, private data, or documented manual steps
Descriptive : prose detailed enough that a competent networker could rebuild the pipeline
Fragile     : results depend on unrecorded conditions -> a red flag to fix before submission
```

For SIGCOMM, downscaled testbed results should be turnkey because evaluators actually run
them; full-scale hardware results may stay scripted with the deviation documented. State the
achieved level honestly rather than promising turnkey behavior that fails on a clean machine.

## Vignette: a wide-area measurement result

A paper characterizes loss and latency on a production overlay, then proposes a routing tweak.
Its reproducibility spine: the measurement window and vantage points, the sampling method, the
anonymization applied before any release, a public-trace or synthetic substitute for the parts
that cannot ship, and a driver that regenerates the loss-latency figures from logged samples —
plus one honest sentence about which production condition the substitute cannot capture.

## Legal and ethical release

- Real user or third-party-infrastructure measurement needs its handling addressed in the
  paper; anonymize before release and record what was removed.
- Prefer an archival host with a DOI for anything you can ship, and document the exact reason
  for anything you cannot.

## Output format

```text
[Claim inventory] <number -> rebuildable location>
[Ledger status] topology / traffic / configuration / run — complete or gaps
[Reproducibility level] turnkey / scripted / descriptive / fragile
[Data-release plan] shippable / substitute (+ provenance) / withheld (+ reason)
[Paper fixes] <must appear in the main PDF>
[Artifact fixes] <what the package still needs>
```
