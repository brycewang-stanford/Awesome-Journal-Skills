---
name: icde-experiments
description: Use when designing or auditing IEEE ICDE experiments for a data-engineering paper: workload realism, tuned baselines, scale curves over single points, throughput and tail-latency with declared variance, mechanism-isolating ablations, cost/loss disclosure, and hardware reporting that satisfies a builder-heavy committee.
---

# ICDE Experiments

Use this before submission when the evaluation is not yet locked. At ICDE, the experiments are
where a systems paper is won or lost; a builder-heavy committee reads them adversarially.

## Experiment audit

- Map each performance claim to a **figure, table, or measured crossover** — no orphan claims.
- Run **tuned baselines**, not straw men. Document the tuning budget you gave each competitor;
  an untuned baseline is the single most common ICDE reject trigger.
- Prefer **curves over points**: show behavior across scale factors, data sizes, or contention
  levels, not one operating point where you happen to win.
- Report **throughput and tail latency with variance** — multiple runs, and captions that say
  whether bars are standard deviations, confidence intervals, or percentiles. A p99 that hides
  behind a median is a caught omission.
- Add **ablations that isolate the mechanism**: turn off the one idea and show the gain
  disappears, so the improvement cannot be attributed to unrelated engineering.
- Disclose the **cost** of every gain: memory, write amplification, CPU, or read-latency
  penalty. A loss map is a credibility signal, not a weakness.
- Report **hardware, OS, storage device, software versions, dataset construction, and workload
  generators with seeds** so the numbers are reconstructable.

## What experiments are for at this venue

- ICDE experiments exist to **establish and isolate a systems effect**, not to top a
  leaderboard. One clean ablation proving the mechanism causes the gain outweighs five more
  datasets where it merely correlates.
- The strongest design pairs a **synthetic generator** you can sweep (to find the crossover and
  stress the mechanism) with a **real workload** (to show practical relevance). State where the
  synthetic regime matches the real one and where it does not.
- Reviewers check whether the **operating regime** — data size, concurrency, hardware — is one
  where the claimed effect should even appear; a cache-resident benchmark cannot support a
  claim about I/O-bound behavior.

## Evidence-burden table

| Claim | Matching evidence | Reject pattern avoided |
|---|---|---|
| "The problem exists" | Baseline stalls/degrades on the target workload | "Solving a problem nobody has" |
| "Our mechanism causes the gain" | Ablation toggling the one idea | "Gain from unrelated engineering" |
| "It scales" | Curve across scale factors, not a single point | "Single-point win, unknown scaling" |
| "The cost is acceptable" | Disclosed memory/CPU/latency cost table | "Free-lunch claim, hidden trade-off" |
| "It generalizes" | A real workload beside the synthetic sweep | "Only synthetic, no real relevance" |

## Vignette: evaluating a write-optimized index

A paper claims higher ingestion by deferring ordering. The matching plan: sweep the
append-to-scan ratio synthetically to locate the crossover, run a real telemetry trace at the
claimed rate to show the baseline stalls where the new index does not, ablate the deferral to
prove it is the cause, and report the read-latency tail and memory cost so the trade is legible
— every panel tied to a claim in the text.

## Reporting floor

- Multiple runs and reported variance for every performance figure; name the metric precisely
  (throughput, p50/p99 latency, amplification).
- Report the hardware and the compute actually consumed, not vague feasibility language.

## Output format

```text
[Experiment readiness] strong / adequate / weak
[Claim -> evidence map] <claim: figure/table/crossover>
[Baseline fairness] <tuning budget disclosed? untuned competitors?>
[Missing evidence] <scale curve / variance / ablation / cost disclosure>
[Reproducibility gaps] <hardware / versions / generators / seeds>
[Decision-critical next run] <one experiment>
```
