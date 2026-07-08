# MLSys Resources

Working material for the MLSys skill pack. The `skills/` directory tells an agent what to do;
this directory gives it things to do it *with*: a first-page rewrite worked at MLSys standards,
a zero-hallucination exemplar library from the venue's own proceedings, the official source map
behind every cycle fact, and a measurement-oriented adapter for the shared artifact kit.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | Rewrite an abstract/introduction from product-announcement style into the MLSys arc: measured bottleneck → insight → named mechanism → ranged payoff → honest tradeoff. Fully fictional example; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Position against verified MLSys papers (FlexFlow/SOAP, MLPerf Training, FedProx, transformer-inference scaling, AWQ) and dodge the SOSP/NeurIPS misattribution traps. |
| [`official-source-map.md`](official-source-map.md) | Trace every 2026-cycle fact (deadlines, 10-page limit, Industrial Track, AE badges) to its official URL, and see exactly which logistics remain 待核实. |
| [`external_tools.md`](external_tools.md) | Jump straight to the live CFPs, OpenReview group, AE call, dates page, and proceedings archive. |
| [`code/README.md`](code/README.md) | Adapt the shared ML-conference reproducibility kit to MLSys's performance-measurement and badge-evaluation needs. |

## Scope Note

This pack serves a systems conference with an ML soul. Its center of gravity is measurement:
throughput, latency, memory, cost, and the artifacts that let strangers re-measure them. Do not
import accuracy-leaderboard habits from the general ML packs, and do not import the economics
replication kit — the right shared resource is `shared-resources/ml-conference-methods/`, bent
toward system-layer pinning as described in [`code/README.md`](code/README.md).

## Suggested Workflow

1. Route the project with
   [`../skills/mlsys-topic-selection`](../skills/mlsys-topic-selection/SKILL.md) — including the
   research-vs-industrial-track decision — then shape the first page with
   [`../skills/mlsys-writing-style`](../skills/mlsys-writing-style/SKILL.md) and
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
2. Lock the evaluation with [`../skills/mlsys-experiments`](../skills/mlsys-experiments/SKILL.md)
   and [`../skills/mlsys-reproducibility`](../skills/mlsys-reproducibility/SKILL.md), using
   [`code/README.md`](code/README.md) for packaging.
3. Benchmark your framing against [`exemplars/library.md`](exemplars/library.md), then verify
   every deadline and rule through [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before anything ships.
