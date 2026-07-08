---
name: osdi-experiments
description: Use when designing or auditing the evaluation of an OSDI submission — choosing mature baselines and realistic workloads, structuring the section around research questions, measuring scalability and tail behavior, quantifying the design's costs, and fitting the evidence into the 12-page reviewed body.
---

# OSDI Experiments

Design the evaluation as the paper's proof obligation. The page constraints referenced
here are OSDI '26 rules (12 reviewed pages, no appendices at submission — verified
2026-07-08); the evidence standards are the durable expectations of systems PCs.

## Research questions first

Write the evaluation's research questions before running anything, and derive the
experiment set from them. Every OSDI evaluation ultimately answers versions of:

1. **Does the idea work end to end?** — the headline comparison on a realistic
   workload against the strongest baseline.
2. **Where does the benefit come from?** — component breakdown attributing the win to
   the named design idea rather than to incidental engineering.
3. **What does it cost?** — the overheads the design admits (memory, write
   amplification, CPU, complexity), measured, not estimated.
4. **When does it break?** — scalability limits, adversarial workloads, failure and
   recovery behavior.

An evaluation organized as RQ1–RQ4 with one experiment cluster each reads as an
argument; a tour of every benchmark you happened to run reads as padding, which the
OSDI '26 CFP explicitly invites reviewers to down-rank.

## Baselines that fight back

The baseline question decides more OSDI reviews than any other. Standards:

- Compare against the **strongest deployed or published system** for the problem, at
  its tuned best — not a strawman configuration. Reviewers who built the baseline
  will recognize a sandbagged setup instantly.
- If the nearest competitor is unavailable, re-implement from its paper and say so,
  with the re-implementation validated against published numbers where possible.
- Include the **do-nothing baseline** where it is honest: sometimes the existing
  system plus more hardware is the real alternative, and the paper is stronger for
  pricing it.
- Version, configuration, and tuning of every baseline belong in the paper. Under the
  no-appendix rule this is body text — budget for it.

## Workload realism

| Workload tier | Role in the argument | Trap |
|---|---|---|
| Microbenchmarks | Isolate a mechanism; explain *why* the end-to-end effect exists | As the only evidence: workshop-grade |
| Standard suites (e.g., YCSB-class) | Comparability with prior papers | Defaults nobody runs in production |
| Trace-driven / production-derived | The claim's load-bearing evidence | Provenance undocumented (see osdi-reproducibility) |
| Adversarial / stress | Answers RQ4 honestly | Omitted, leaving reviewers to imagine worse |

Systems reviewers read workload sections looking for the flattering-choice smell: the
one skew setting, working-set size, or thread count where the design shines. Sweep the
parameter, show the crossover point, and say where the baseline wins — a visible
crossover is credibility, not weakness.

## Measurement discipline

- Report **distributions, not averages**, wherever latency matters: medians and p99s
  diverge exactly where systems papers live. State run counts and variance.
- Separate **warm and cold** behavior; state measurement windows and what was
  discarded.
- Attribute wins: a profile or counter-level breakdown connecting the speedup to the
  mechanism ("the win disappears when we disable per-tenant ordering") beats any
  additional benchmark.
- Failure experiments need injected faults with stated injection method and timing,
  not prose about what recovery "would" do.

```text
Experiment matrix skeleton (freeze ~8 weeks before the December deadline):
RQ | workload (tier + provenance) | baselines (version, tuning) | metric
   | scale points | runs x seeds | expected figure/table | status
Freeze the matrix, then let deadline pressure cut rows, never redefine them —
redefinition under pressure is how flattering choices happen.
```

## Fitting evidence into 12 pages

With no appendix at submission, the evaluation must be self-sufficient and compact:

- One figure or table per research question, each with a caption stating its takeaway.
- Cut experiments that do not serve an RQ, even if they took weeks — the accepted-paper
  14-page budget (plus appendices) can resurrect them later (`osdi-camera-ready`).
- Keep the setup paragraph brutal: hardware, topology, versions, workloads, runs — in
  one place, once (`osdi-reproducibility` owns the full ledger).

## Reporting grid

Match each metric class to its honest presentation before making figures:

| Metric class | Report as | Not as |
|---|---|---|
| Throughput | Curve vs offered load, to saturation | Single peak number |
| Latency | Median + p99 (p999 if claimed), distribution across runs | Mean ± nothing |
| Recovery/failover | Timeline from fault injection, per scale point | "Fast recovery" prose |
| Overhead (the design's cost) | Same rigor as the win, same table | Footnote estimate |
| Scalability | Efficiency vs ideal at each point | "Near-linear" unquantified |

One convention repays its cost: keep the baseline's color/marker identical across
every figure, so the skim (`osdi-review-process`) reads the comparison correctly
without consulting legends.

## Review-time exposure

The evaluation objections you cannot rebut (no response period in 2026) are the
predictable ones: weak baseline, unrealistic workload, missing cost measurement, and
average-only latency. Audit for exactly these four before submission; each unaddressed
one is a review point conceded silently.

## Output format

```text
[RQ coverage] RQ1-4 each mapped to experiments? gaps: <list>
[Baseline verdict] strongest opponent present + tuned? <one-line judgment>
[Workload realism] tiers present; flattering-choice risks: <list>
[Cost honesty] design's costs measured? <which, where>
[Tail discipline] distributions + variance reported? <yes/no + fix>
[Page fit] evaluation length vs 12-page budget; cut candidates: <list>
```
