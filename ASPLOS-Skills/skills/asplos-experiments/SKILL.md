---
name: asplos-experiments
description: Use when designing or auditing the evaluation of an ASPLOS paper — choosing among real silicon, FPGA prototypes, and simulators with cycle-accuracy caveats stated, selecting workload suites and baselines that hold up across three communities, attributing wins via ablation, and reporting energy, area, and overhead honestly.
---

# ASPLOS Experiments

An ASPLOS evaluation answers to three communities at once: architects who will audit
the modeling, OS people who will audit the workload realism, and PL people who will
audit what the software layer actually does. The section's core discipline is
**matching each claim to an instrument whose error model can carry it** — and saying
what that error model is.

## The instrument ladder

| Instrument | What it can prove | What it cannot | Must be reported |
|---|---|---|---|
| Real silicon | End-to-end effects, OS interactions, true tails | Designs needing hardware that doesn't exist | CPU/stepping, kernel + config, microcode, BIOS knobs (SMT/turbo/prefetchers), memory topology |
| FPGA prototype | Feasibility, cycle behavior of new logic at the prototype's clock | Absolute performance of an ASIC-class part | Board, clock, resource utilization, what was scaled down and why |
| Cycle-level simulator (e.g. gem5-class) | Relative effects of microarchitectural change under stated configs | Anything outside modeled fidelity — I/O, OS noise, firmware behavior are commonly stylized | Simulator + exact version/commit, config files, warm-up and region-selection method, validation against a real machine where possible |
| Analytical/energy models (McPAT-class, first-order area) | Trend-level energy/area comparisons | Absolute mW or mm² as truth | Model version, technology node assumptions, and the claim written as trend not absolute |

The cardinal sin is a claim-instrument mismatch: absolute latency claims from an
unvalidated simulator, or OS-interaction claims from a user-space harness. Rapid
and full reviewers both hunt for it.

## Cycle-accuracy caveats are content, not apology

When simulation carries a claim, the paper must state: which structures are modeled
in detail vs stylized; how simulation regions were chosen (full runs, checkpoints,
sampled regions à la SimPoint-style methodology); how long the warm-up was; and —
strongest of all — a **validation experiment** showing the simulator tracks a real
machine on a measurable subset. A one-paragraph validation against silicon buys
credibility that no amount of extra benchmarks can.

## Workloads and baselines that survive three audiences

- Draw workloads from suites the communities recognize (SPEC-class CPU suites,
  parallel suites, cloud/graph/serving workloads appropriate to the claim) *and*
  include at least one full application or kernel-integrated scenario — accelerator
  papers evaluated only on extracted kernels routinely get the "where is the rest of
  the system" review.
- The baseline is the **strongest deployed alternative configured by someone who
  wants it to win**: current kernel policy with its tunables set properly, the
  vendor library, the state-of-the-art accelerator at an honest technology
  normalization.
- Technology normalization must be explicit when comparing across nodes or clocks:
  state the scaling assumptions rather than silently converting.

## Attribution: ablate the mechanism you credit

Every "X improves Y because of mechanism M" needs a run with M removed, weakened,
or transplanted onto the baseline. In cross-layer papers this means ablating **each
side of the boundary separately** — hardware hints without the new policy, policy
without the hints — because the venue's whole premise is that the coupling matters;
prove the coupling, not just the sum.

## The claim-instrument matrix

Freeze this before writing; it becomes the evaluation section's skeleton and the
rebuttal's ammunition:

```text
claim                          instrument        workloads          baseline(+config)      metric + spread          where
end-to-end speedup             real 2-socket+CXL  SPEC17 + graph(5)  Linux 6.9 tiering,     runtime, gmean, 10 runs, §6.2
                                                                     tuned per docs         95% CI
coupling is necessary          same               subset(6)          each-half ablation     delta vs full design     §6.4
generality across latency      gem5 (pinned cfg)  subset(6)          same policy            trend, sim-validated     §6.5
overhead where design idles    real hardware      non-tiered set     stock kernel           <=2% regression bound    §6.6
energy trend                   McPAT-class model  subset             baseline design        trend only, node stated  §6.7
```

Report dispersion for anything measured on real hardware (runs, variance source,
CI); report *sensitivity* for anything simulated (which config parameters move the
result). Include the workload where the design loses and explain the boundary — a
measured regression with a mechanism story is evidence of understanding, and its
absence is conspicuous to reviewers who build systems themselves.

## Measurement noise on real hardware is a design input

Silicon experiments carry noise sources that simulators hide, and the paper's
run protocol must name its countermeasures: pin frequency governors or report
the governor used; control or randomize NUMA placement; interleave A/B runs
rather than batching (thermal and cache state drift over a session); and
distinguish warm-start from cold-start numbers explicitly. When an effect is
within the machine's observed run-to-run variance, the honest sentence is that
the experiment cannot distinguish the designs — reviewers respect the sentence
and pounce on its absence.

## Energy, power, and area claims

- On silicon, name the meter: RAPL-class counters, wall-power instrumentation,
  or board-level telemetry — each has known blind spots worth one caveat clause.
- Model-derived energy or area numbers (McPAT-class, synthesis estimates)
  support **comparisons under stated assumptions**, not datasheet-grade values;
  write them as ratios with the technology node and model version attached.
- FPGA utilization (LUTs, BRAM, DSPs) is evidence of feasibility at the
  prototype's scale — extrapolating it to ASIC area needs an explicit argument,
  or the claim should stay at feasibility.

## Evaluation-methodology papers

Note that "experimental methodologies" is itself on the 2027 topics list: if
the most defensible contribution turns out to be the measurement approach — a
validation harness, a workload characterization, a simulation-sampling method —
consider promoting it from a subsection to the paper, with `asplos-topic-selection`
re-run on the promoted claim.

## Sweeps and knees

Cross-layer designs live or die on regime boundaries, so at least one sweep per
load-bearing parameter (device latency, core count, working-set size, offered
load) should run **past the knee** — the point where the benefit saturates or
inverts. A curve truncated before its knee is read by systems reviewers as a
curve hiding its knee. State where the knee is and why it sits there; the
mechanism story at the boundary is often the most-cited sentence in the paper.

## Output format

```text
[Matrix] every claim has instrument+baseline+location: Y/N (orphans listed)
[Instrument audit] any claim exceeding its instrument's error model? list
[Simulator hygiene] version/config/regions/warm-up stated · validated vs silicon?
[Baseline strength] strongest deployed alternative, tuned: Y/N per claim
[Attribution] per-layer ablations present: Y/N
[Adverse results] losing workload + boundary explanation in paper: Y/N
```
