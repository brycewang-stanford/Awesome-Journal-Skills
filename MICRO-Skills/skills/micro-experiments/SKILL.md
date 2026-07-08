---
name: micro-experiments
description: Use when designing or auditing the evaluation of a MICRO paper — choosing the right instrument on the ladder from analytical model to cycle-level simulator to RTL to silicon, tuning baselines the PC will respect, selecting workload suites, running ablations and sensitivity sweeps, and reporting geomeans with full overhead accounting.
---

# MICRO Experiments

MICRO's evaluation culture is instrument-centric: the community knows exactly what
each measurement tool can and cannot prove, and reviewers score the *match between
claim and instrument* before they look at the numbers.

## The instrument ladder

| Instrument | Proves | Cannot prove | Typical tools |
|---|---|---|---|
| Analytical / trace model | First-order potential, limit studies | Interaction effects, timing | custom, trace-driven models |
| Cycle-level simulation | Relative performance of mechanisms | Absolute wall-clock, physical cost | gem5, ChampSim, Sniper, Ramulator/DRAMsim3 |
| Power/area models on top of sim | Energy and area trends | Sign-off-quality numbers | McPAT, CACTI, Accelergy |
| RTL + synthesis | Timing closure, real area/power at a node | Full-system performance | Verilog/Chisel + synthesis flow |
| FPGA prototype | Functional correctness at scale, OS interaction | ASIC frequency/power | FireSim, custom boards |
| Silicon measurement | Everything, for that one chip | Generality across designs | perf counters, power rails |

Rule: **claim one rung below your strongest instrument.** Cycle-level simulation
plus McPAT supports "reduces memory-stall cycles by X% with ~Y mm² estimated
overhead"; it does not support "improves datacenter TCO." The lineage here is the
venue's own: CACTI 6.0 (MICRO 2007) and McPAT (MICRO 2009) were published *at MICRO*
precisely because the community polices modeling fidelity.

## Baseline construction — where most rejections start

- The baseline core must be **configured like a current product**, not a textbook
  default: wide OoO, capable branch predictor, competent multi-stream prefetcher,
  realistic DRAM timing. A win over gem5's out-of-the-box config is a non-result.
- Include the **best prior mechanism in your exact category**, re-implemented in
  your simulator with its published parameters — not just numbers copied from its
  paper under a different config.
- Add an **idealized upper bound** (oracle predictor, infinite table) so readers see
  what fraction of the headroom you capture.
- If your mechanism uses N KB of extra storage, give the baseline the same N KB as
  additional cache/predictor capacity in at least one comparison — the
  "iso-storage" check reviewers ask for in rebuttal anyway.

## Workloads

- Name the suite and the subsetting rule: SPEC CPU2017 (all, or a stated-criterion
  subset), PARSEC/GAP for multithreaded, MLPerf or named DNNs for accelerators,
  plus the domain traces your mechanism targets.
- Disclose sampling methodology: SimPoint regions, warmup lengths, instruction
  budgets per region. Cherry-picked "representative regions" without a stated
  selection rule are a rebuttal magnet.
- Report **per-workload bars plus geomean** — never arithmetic means of speedups,
  and never geomean-only (it hides the regressions reviewers will hunt for).

```python
# the only defensible summary statistic for speedups
from math import prod
def geomean(xs):
    return prod(xs) ** (1.0 / len(xs))
speedups = per_workload_ipc_new / per_workload_ipc_base   # elementwise
print(f"geomean {geomean(list(speedups)):.3f}, "
      f"min {min(speedups):.3f} ({worst_workload}), "
      f"regressions: {(speedups < 1.0).sum()} of {len(speedups)}")
```

## The ablation and sensitivity contract

Every design decision named in the mechanism section owes the evaluation section a
figure or table row:

- **Ablate** each component (drop the filter, halve the table, disable the guard)
  to show each earns its area.
- **Sweep** the structural parameters: table sizes, associativities, thresholds,
  core counts, LLC capacities, DRAM bandwidth. The mechanism should degrade
  gracefully at the sweep edges — cliffs demand explanation in the text.
- **Stress adversarially:** the workload class the mechanism should *not* help, the
  access pattern designed to defeat it. Reporting a bounded loss builds more trust
  than an unbroken win column.

## Simulation-length and validation sanity

Two credibility checks reviewers apply that authors often skip:

- **Enough simulated instructions per region.** Sub-100M-instruction detailed
  windows on memory-bound workloads mostly measure the warmup transient. State
  warmup and detailed lengths, and show at least once that doubling them does not
  move the headline.
- **Baseline validation against published numbers.** Before trusting relative
  results, show your baseline's absolute behavior is sane: IPC or MPKI within
  the published envelope for the same suite and a comparable config. A baseline
  whose branch predictor achieves 2x the published MPKI of the modeled design
  invalidates the comparison silently.

For multicore results, disclose how heterogeneity was handled: mix construction
rule, per-mix repetitions, and whether throughput is weighted speedup, harmonic
mean, or raw IPC sum — each answers a different question and reviewers check that
the metric matches the claim (fairness claims need a fairness metric).

## Overhead accounting checklist

- [ ] Storage: bits/entry × entries, totaled in KB, per core and shared.
- [ ] Area and power: model named with version (e.g., McPAT vX at Ynm), numbers
      labeled as estimates.
- [ ] Latency: added pipeline stages or access-path cycles; off critical path
      claims justified.
- [ ] Energy: dynamic + leakage deltas, not just "negligible."
- [ ] Complexity: verification surface, new SRAM ports, wiring — one honest
      paragraph.

## Output format

```text
[Instrument] <rung used> — claim height matches: yes / no (quote the overclaim)
[Baseline strength] product-like config / best-prior reimplemented / oracle bound /
                    iso-storage check: present-absent each
[Workloads] suite + subset rule + sampling disclosure: complete / gaps listed
[Summary stats] per-workload + geomean + regression count: yes / no
[Ablations] each mechanism component covered: list of unablated components
[Sensitivity] parameters swept vs parameters hardcoded
[Overheads] storage / area / power / latency / energy: quantified-missing each
```
