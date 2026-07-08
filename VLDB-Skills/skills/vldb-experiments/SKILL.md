---
name: vldb-experiments
description: Use when designing or auditing the evaluation of a VLDB paper, covering workload and dataset realism at scale, competitor tuning fairness, scalability curves versus single points, tail-latency and throughput reporting, ablations that isolate the mechanism, and the loss-case disclosure PVLDB reviewers look for first.
---

# VLDB Experiments

Use this before the evaluation section hardens. At this venue the experiments
*are* the argument: a PVLDB reviewer typically flips from the introduction
straight to the plots and decides how skeptically to read everything else.

## What the evaluation must establish

Four distinct burdens, each needing its own experiments:

1. **The problem exists** — measure the baseline failing on a credible
   workload before showing your fix.
2. **The mechanism causes the gain** — ablate your components; a monolithic
   "our system vs. theirs" plot proves selection, not mechanism.
3. **The gain survives scale** — curves along data size, cluster size, and
   concurrency, not one configuration chosen after the fact.
4. **The cost is known** — measure where your design loses and say so.

## Workload realism ladder

| Rung | Example | Reviewer credit |
|---|---|---|
| Micro-benchmark | single operator, synthetic keys | Mechanism insight only |
| Standard benchmark | TPC-style, YCSB, JCC-H-class | Comparable, but "benchmark-only" is a known flag |
| Benchmark + skew/drift | standard suite with realistic distributions | Solid |
| Trace or production-derived | replayed real workload | Strongest, disclose provenance |

Climb as high as the data you can legally use allows; state the rung honestly.

## Baseline fairness protocol

The people who built your baselines review here. For every competitor:

- Latest stable version (or a justified pin), same hardware, same data.
- Tuning effort comparable to what you gave your own system — document the
  knobs tried in both cases.
- If a competitor is excluded, one honest sentence why (license, no support
  for the workload) beats silence.
- Include the strong-but-inconvenient baseline: the hand-tuned config, the
  single-node engine that wins at small scale, the "just add an index"
  answer. Reviewers propose these in their first pass; preempt them.

## Reporting floor

- Throughput **and** latency, with tails (p95/p99) where users feel tails.
- Repetition counts and spread (see `vldb-reproducibility` for the variance
  protocol); medians for skewed metrics.
- Axes from zero or clearly marked; log scales labeled; error bands defined
  in the caption.
- Every number in the abstract traceable to a specific figure or table.

## Ablation and sweep matrix

```text
For each design component C1..Cn:
  full system  vs  full-minus-Ci        (mechanism attribution)
For each claimed robustness dimension D:
  sweep D across its realistic range    (skew, size, concurrency, selectivity)
Loss map:
  identify >=1 region where a baseline wins; measure it; discuss it
```

The loss map is deliberately mandatory. A paper whose system wins everywhere
in every plot triggers reviewer search behavior — they will find the losing
region themselves, without your framing.

## Scale honesty

Run the largest experiments your infrastructure permits, then scope claims to
what was run. "Designed for larger deployments" is acceptable prose;
extrapolated curves presented as measurements are not. If cloud credits capped
the study, say so — builders on the panel have lived that constraint.

## Output format

```text
[Burden coverage] problem-exists / mechanism / scale / cost — evidence per burden
[Workload rung] <ladder position, justification>
[Baseline fairness] <competitor -> version, tuning parity, exclusions>
[Reporting floor] tails, reps, spread — gaps
[Loss map] present (region, magnitude) / missing (risk)
[Next decisive run] <the one experiment that most changes acceptance odds>
```
