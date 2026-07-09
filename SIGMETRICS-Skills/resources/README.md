# ACM SIGMETRICS Resources

Action-oriented resources for the SIGMETRICS skill pack. The `skills/` give advice; this directory
lets an agent model a SIGMETRICS-shaped paper, benchmark against verified exemplars, and prepare an
artifact for the rolling, hybrid conference-journal POMACS process.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a performance-evaluation paper that pairs a theorem with a measurement. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified SIGMETRICS/POMACS papers across contribution shapes (queueing theory, measurement, learning-for-systems), and avoid confusion with IMC, SIGCOMM/NSDI, and SIGMOD. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current-cycle deadlines, page budget, one-shot-revision rules, POMACS publication, and track list before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official SIGMETRICS, POMACS, per-deadline HotCRP, and ACM artifact surfaces, plus the cross-check sources for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Use the shared replication-package tooling: a claim-to-evidence matrix, an ACM-badge checklist, and a dependency-free smoke checker for anonymized artifacts. |

## Scope Note

This is a **computer-systems performance-evaluation** pack whose papers publish in a **journal**
(POMACS) on a **three-cycle rolling model**, not a pure network-measurement pack (IMC) or a
networking-systems pack (SIGCOMM/NSDI). SIGMETRICS evidence is a **blend**: a stochastic or
queueing model with a **proof of a performance bound**, a **principled measurement study**, or a
**learning-for-systems** algorithm with regret/convergence guarantees — often two of these in one
paper. Do not import the pure-measurement framing or the networking-testbed machinery of the
siblings; a SIGMETRICS reviewer expects mathematical rigor *and* empirical grounding.

## Suggested Workflow

1. Route and frame with
   [`../skills/sigmetrics-topic-selection`](../skills/sigmetrics-topic-selection/SKILL.md) and
   [`../skills/sigmetrics-writing-style`](../skills/sigmetrics-writing-style/SKILL.md) — deciding
   SIGMETRICS vs. IMC/SIGCOMM/NSDI/a theory venue before writing is the highest-leverage move.
2. Build evidence with
   [`../skills/sigmetrics-experiments`](../skills/sigmetrics-experiments/SKILL.md),
   [`../skills/sigmetrics-reproducibility`](../skills/sigmetrics-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle
   in [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the HotCRP audit in
   [`../skills/sigmetrics-submission`](../skills/sigmetrics-submission/SKILL.md).
