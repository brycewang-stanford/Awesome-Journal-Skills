---
name: isca-experiments
description: Use when designing or auditing the evaluation of an ISCA paper — pinning simulator fidelity to the claims it must carry, documenting gem5-class configurations and sampling choices, selecting workload suites that represent the claim's domain, tuning baselines in good faith, and separating architectural effect from modeling artifact.
---

# ISCA Experiments

Most ISCA evaluations run on models of machines rather than machines, so the
evaluation section is really two nested arguments: that the *modeled* effect is
real, and that the *model* deserves trust for this effect. Reviewers at this venue
are professionally skeptical about the second argument, and papers die on it more
often than on the first. Everything below serves one rule: **the paper must state
what its numbers are made of.**

## Declare the methodology contract

Early in the methodology section, answer four questions explicitly — this is the
contract reviewers try to reconstruct when authors omit it:

1. **Tool and version.** Which simulator/emulator/RTL flow, at which exact version
   or commit, with which local modifications? "gem5" without a commit is not a
   methodology; behavior differs meaningfully across releases and forks.
2. **Fidelity scope.** Which parts of the machine are modeled cycle-by-cycle,
   which are stylized (fixed-latency, functional-only), and which are absent
   (typical gaps: OS effects, TLB behavior, DRAM refresh, on-chip network
   contention)? A claim must not rest on a component in the stylized list.
3. **Simulation regions.** Full workloads, checkpoints, or sampled regions
   (SimPoint-style)? How many instructions of warm-up before measurement, and how
   was that length chosen? Cold-structure artifacts masquerade as results.
4. **Anchoring.** What ties the model to reality — validation against a physical
   machine on a subset, cross-checking against published characterization, or
   agreement between two independent instruments? One honest anchoring paragraph
   outweighs three extra benchmark suites.

## Match each claim to an instrument that can carry it

| Claim type | Sufficient instrument | Chronic mismatch to avoid |
|---|---|---|
| Relative IPC/latency effect of a microarchitectural change | Cycle-level simulation with the changed structures modeled in detail | Quoting the result as absolute time or absolute joules |
| Absolute end-to-end performance | Real silicon or FPGA prototype measurement | Deriving it from an unvalidated software model |
| Energy/power | Measured power, or a named model (McPAT-class) with node assumptions stated | Modeled milliwatts presented without the model's error bars or vintage |
| Area/timing feasibility | Synthesis of the added logic, or a sizing argument from structure counts | "Negligible area" with no numbers |
| OS/IO-dependent behavior | Full-system simulation or hardware | User-level simulation silently ignoring the kernel |
| Datacenter/at-scale effects | Measurement study or trace-driven analysis with trace provenance | Extrapolating single-node simulation to fleet claims |

## Workloads argue representativeness, not volume

Choose suites because they exercise the mechanism's operating region, and say so.
A cache-hierarchy paper needs memory-intensive selections and must report MPKI or
footprint evidence that the pressure is real; an accelerator paper needs at least
one end-to-end application, because kernels-only evaluation invites the question
of what fraction of total time the kernel is. Standard anchors (SPEC-class CPU
suites, graph/ML/server suites as appropriate) buy comparability; a workload
nobody recognizes needs a characterization subsection justifying its inclusion.
Report per-workload results — geomean-only reporting reads as concealment, and
the interesting review questions live in the outliers.

## Baselines: configure the adversary to win

The baseline is the strongest relevant prior mechanism *tuned the way its authors
would tune it*, at equal hardware budget where the comparison implies one. State
the equalization: same storage, same ports, same technology assumptions. When
comparing against a prior paper's mechanism, reimplement it in your framework and
say how you verified the reimplementation reproduces its published behavior —
reviewers who authored those baselines are plausibly on the committee.

## Attribution and sensitivity

For every "gain comes from M" sentence, include the run with M disabled or
replaced by its naive variant. Then sweep the two or three parameters the design
is most sensitive to (table sizes, thresholds, latencies) and show where the
benefit collapses — a visible break point is credibility, not weakness. Report
run-to-run variation wherever nondeterminism exists (real hardware, multithreaded
simulation): repeated trials with dispersion, not single lucky runs.

## A config manifest per reported number

Make every figure regenerable from a manifest the artifact ships (see
`isca-reproducibility` and `isca-artifact-evaluation`):

```ini
; exp/f7-headline.manifest — one file per figure/table
[instrument]
simulator   = gem5
commit      = a1b2c3d4 (+ local patches: patches/*.diff)
mode        = full-system, O3 core model

[machine-model]
core        = 8-wide OOO, 352-entry ROB, 3.2 GHz nominal
l1d/l1i     = 48K/32K, 8-way
l2          = 1.25M private ; llc = 3M/core shared, 16-way
dram        = DDR5-4800, 2 ch, model=detailed

[measurement]
regions     = simpoints(k=10, interval=100M)
warmup      = 50M inst per region
metric      = IPC, geomean over per-workload weighted regions
trials      = 3 (report min/median/max where variance > 1%)

[workloads]
suite       = SPEC-class CPU suite, ref inputs; list = workloads.txt
```

## Evaluation-section order that answers reviewers in sequence

Headline comparison first; attribution/ablation second; sensitivity third;
overheads (storage, energy, area, complexity) fourth; explicit limitations last.
Burying overheads after the conclusion-adjacent paragraphs is the venue's most
transparent tell; putting them in the main flow signals confidence.

## Red flags this venue's reviewers name in reviews

- Simulator described in one sentence; configuration table missing latencies.
- Warm-up unstated; sampled regions chosen by an unnamed procedure.
- Baseline older than the idea it defends, or untuned defaults.
- Geomean-only reporting; suspicious absence of any losing workload.
- Modeled energy stated to three significant figures.
- A limitations paragraph that lists only limitations the design doesn't have.

Verified cycle facts (page rules, dates, double-blind handling of artifact links)
live in `../../resources/official-source-map.md`, checked 2026-07-08; methodology
norms above are community practice, not CFP text, and should be applied with
judgment. The manifests built here are reused verbatim by `isca-reproducibility`
(freeze ritual) and `isca-artifact-evaluation` (claims table) — invest once,
spend three times.
