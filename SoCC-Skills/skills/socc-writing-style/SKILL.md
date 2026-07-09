---
name: socc-writing-style
description: Use when revising an ACM SoCC paper for a cloud-scale problem an operator recognizes on the first page, a contribution at the systems-and-data intersection, evidence measured on a real or realistic deployment with tail latency and cost as first-class, dual-anonymous wording, and disciplined use of the acmart 12-page budget.
---

# SoCC Writing Style

Use this when revising the main paper. SoCC papers are read by a joint **SIGMOD+SIGOPS** audience,
so they need a **cloud-scale problem stated in operator terms on the first page** and evidence a
skeptic from *either* community trusts. The failure this skill prevents is a paper that reads like a
pure-OS result with a cloud title glued on, or a benchmark with no systems contribution.

## Revision rules

- **Lead with the cloud problem, in cost and tail terms:** the problem an operator or platform team
  recognizes, why current systems are inadequate *at scale*, the contribution (mechanism and/or
  measurement), the measured evidence, and what changes for cloud practice.
- **Situate the contribution at the systems-and-data intersection.** Say explicitly what is new: a
  mechanism, a measurement, a benchmark, a deployment lesson, or a cost model. SoCC's twin
  communities both want to see themselves in the paper.
- **Make tail latency and cost first-class.** Report p95/p99 (and p99.9 where it bites) and a
  concrete cost model, not just averages. A cloud paper that reports only the mean signals it has
  not been stress-tested the way an operator would.
- **Pair every claim with measured evidence** — a real or realistic deployment, a tuned baseline, a
  distribution rather than a point, a trace with stated provenance — not adjectives.
- **State limitations honestly** where the results live: single-provider traces, one region, tested
  regimes, the workloads you did not cover. A cloud paper's external validity is part of its claim.
- **Respect the 12-page (full) / 6-page (short) budget as a design constraint;** references are
  unlimited, but the argument and its decision-critical figures fit the body.
- **Maintain dual anonymity** in self-citations, system/cluster/trace names, provider hints,
  acknowledgements, and the availability wording.

## Cloud-systems paper skeleton

| Section | Job it must do | Common failure |
|---|---|---|
| Intro | Operator problem, inadequacy at scale, contribution, evidence preview, cloud payoff — first page | Leads with a technology trend, not a problem |
| Background/Motivation | Why current cloud systems fall short here, grounded in scale | Motivation by assertion, no measured gap |
| Design / Study | The mechanism or the measurement setup, reproducibly, with the testbed/trace | Method described too thinly to re-deploy |
| Evaluation | Throughput, **tail**, and **cost** vs. tuned baselines on a real/realistic system | Mean-only metrics; simulation standing in for deployment |
| Limitations | The external-validity limits that bite (provider, region, regimes) | Generic or absent |
| Related work | Delta-first positioning across systems and data venues | Catalog of citations with no contrast |

## Sentence-level rewrites

| Draft pattern | SoCC-safe rewrite |
|---|---|
| "Our system significantly improves performance." | "raises throughput X% and holds p99 within the SLO on a 200-node testbed vs. <tuned baseline>" |
| "We evaluate on a large workload." | "We replay a production trace of N invocations across M functions (provenance in §3)" |
| "Results show our approach works well." | "cuts provisioned instance-seconds Y% at equal p99 (Fig. 3); limits in §6" |
| "State-of-the-art performance." | Claim scoped to the workloads, scale, and cost model actually tested |
| "It scales." | "sustains the SLO from 10 to 200 nodes; beyond that, <named bottleneck>" |

## Tail-and-cost discipline

```text
[Tail]     report p95/p99 (p99.9 where it bites), not just the mean; show the distribution
[Cost]     state the pricing model; report instance-seconds or $ so the saving is checkable
[Baseline] tune every baseline with a documented, equal budget; an untuned baseline is a weakness
[Scale]    show behavior across sizes; name the bottleneck where it stops scaling
[Limits]   single-provider / one-region / tested-regime limits stated next to the results
```

## Vignette: compressing an over-scoped systems paper

A draft with three mechanisms, twelve figures, and a sprawling background: keep the one mechanism
that carries the contribution, the throughput/p99/cost figures that decide it, tuned baselines, and
a limitations paragraph; move secondary regimes and full config sweeps to the artifact with forward
references; cut background to the measured gap the paper closes. The test of a good cut: a reviewer
should be able to answer "what did it improve, at what tail and cost, versus what baseline, and
where does it stop working?" from the body alone.

## Output format

```text
[Writing diagnosis] clear / under-motivated / mean-only / over-claimed / over-scoped
[First-page fix] <new framing leading with the operator problem in cost/tail terms>
[Evidence audit] <claim -> deployment/trace -> tail+cost reported -> tuned baseline? yes/no>
[Limitations fix] <external-validity limit that bites -> where to state it>
[Anonymity edits] <system/cluster/trace names / self-citations / links to rewrite>
```
