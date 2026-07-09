---
name: socc-experiments
description: Use when designing or auditing ACM SoCC evaluations, covering real or realistic deployments over simulation, production or representative workloads and traces, tail-latency and cost as first-class metrics, fair tuned baselines, scale and multi-tenancy behavior, reproducible measurement pipelines, and matching evidence to the shape of each cloud claim.
---

# SoCC Experiments

Use this before submission when the evaluation is not yet locked. SoCC reviewers come from **both
SIGMOD and SIGOPS**, and the evaluation is where a good cloud idea is won or lost. The organizing
principle is **measured evidence proportional to the claim** — the study must test the thing the
paper asserts, on a system and workloads a skeptic from either community would accept, with **tail
latency and cost** reported, not just the mean.

## Evaluation audit

- **Prefer a real or realistic deployment over simulation.** A cloud claim about a system needs the
  system running on a testbed or cluster; simulation alone invites the "does it hold on real
  hardware?" reject. Where full scale is impossible, run a faithful scaled deployment and say so.
- **Use production or representative workloads/traces,** with stated provenance and selection, and
  release the replay harness. Synthetic-only microbenchmarks invite the "does this reflect real
  load?" objection.
- **Report tail and cost, not just averages.** p95/p99 (p99.9 where it bites), the latency
  distribution, and a concrete cost model (instance-seconds or $) are the outcomes operators are
  billed against.
- **Choose fair baselines,** including the strongest prior system and a simple-but-reasonable
  alternative, each tuned with a documented, equal budget. An untuned baseline is a scored weakness.
- **Show scale and multi-tenancy behavior:** how the result holds as nodes, tenants, or load grow,
  and where the bottleneck appears — SoCC papers live at scale.
- **Make the measurement pipeline reproducible** (see the code block) so the evaluation reproduces
  rather than re-samples.
- **Design limits in, not on:** know before you run which provider, region, and regime limits the
  study will have, and instrument to bound them.

## Claim-to-evidence design table

| Cloud claim | Matching evidence | Reject pattern avoided |
|---|---|---|
| "System raises throughput at scale" | Throughput across node counts on a real testbed vs. tuned baseline | "Simulated / small-scale only" |
| "Holds tail latency under bursts" | p99 distribution under bursty replayed load | "Only mean latency reported" |
| "Cuts cost" | Instance-seconds or $ under a stated pricing model | "Cost asserted, never measured" |
| "Fair under multi-tenancy" | Per-tenant SLO attainment with contending workloads | "Single-tenant microbenchmark" |
| "The new mechanism adds the value" | Ablation isolating the mechanism vs. a simpler policy | "Mechanism's marginal value never isolated" |

## Tail, cost, and scale floor

```text
[Tail]   report percentiles and the distribution, not just the mean; state the SLO target
[Cost]   define the pricing model; report the cost metric so a reader can recompute the saving
[Scale]  sweep nodes/tenants/load; identify the bottleneck where the result degrades
[Runs]   report the number of runs and the variance for any measured metric
[Compute] state the testbed actually used (nodes, instance types, kernel), not vague feasibility
```

## Workload and trace provenance floor

- Pin commit SHAs and record trace extraction dates; archive the *replayed* trace or a faithful
  generator, not just a pointer or a query.
- State inclusion/exclusion criteria and the resulting workload, with the filtering/replay scripts
  in the artifact.
- Report how the trace maps onto the testbed (scaling factors, time compression) so a reader can
  judge realism.

## Vignette: evaluating a storage QoS mechanism

Suppose the paper claims a scheduler enforces latency SLOs on shared storage better than the prior
system. The matching plan: run both on a real storage testbed with a mix of latency-sensitive and
batch tenants replayed from a representative workload; tune both with an equal, documented budget;
report per-tenant p99 attainment and aggregate throughput with variance; show behavior as tenants
and load scale and name the bottleneck; report the provisioning cost of each; and state
external-validity limits (storage backend, workload mix) — every number traceable to a logged run in
the artifact.

## Statistical and measurement reporting floor

- Latency **distributions and tail percentiles** for every comparison, not point estimates.
- Number of runs and the source of variance for any measured metric.
- A stated cost model behind any economic claim; the compute actually consumed.

## Output format

```text
[Evaluation readiness] strong / adequate / weak
[Claim -> evidence map] <claim: testbed/workload/metric incl. tail+cost>
[Deployment realism] <real testbed / scaled deployment / simulation-only>
[Baseline fairness] <baseline -> tuned? equal budget? documented?>
[Tail+cost+scale] <percentiles + cost model + scaling behavior reported? yes/no>
[Provenance] <trace SHAs+dates, replay harness, testbed described? yes/no>
[Decision-critical next run] <one experiment or measurement extension>
```
