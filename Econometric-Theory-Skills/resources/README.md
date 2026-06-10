# Econometric Theory — Resources

Action-oriented resources for the *Econometric Theory* (ET) skill pack. The `skills/ectheory-*`
files give stepwise advice; this directory lets an agent act: frame a theorem-proof contribution,
benchmark against an exemplar structure, check official venue facts, and prepare supplementary
material without confusing ET with applied-econometrics outlets.

ET is a **theoretical econometrics** venue. It publishes original, rigorous work on the probabilistic
and statistical foundations of econometric methodology: asymptotic theory, identification, estimation,
prediction, inference, stochastic-process arguments, and modern challenges from large-scale data,
computing, AI, and adjacent fields. A strong ET paper can include simulations or an implementation, but
the load-bearing contribution is a theorem, proof architecture, or methodological result rather than an
applied causal estimate.

## What's here

| Resource | Use it to... |
|---|---|
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | Model a theorem-first ET introduction: inference problem, theorem in words, assumptions, limiting law, generality delta, and Monte Carlo as support. Fictional example only. |
| [`exemplars/library.md`](exemplars/library.md) | Use the verified-cell template and sibling-journal guard before adding real Cambridge Core exemplars. It deliberately keeps unverified rows as `待核实`. |
| [`official-source-map.md`](official-source-map.md) | Track the official Cambridge pages behind scope, article types, peer-review model, and supplementary-material rules. Volatile items stay marked `待核实` until rechecked. |
| [`external_tools.md`](external_tools.md) | Tooling references for theorem/proof writing, Monte Carlo simulation, reproducibility, and source verification. |

## Why no generic econometrics code kit

This pack deliberately ships **no generic applied causal-inference code kit**. ET is not the right
place to run a default DID/IV/RDD/DML project. If a paper needs computation, the ET-appropriate artifact
is a focused simulation, estimator implementation, or replication supplement that demonstrates a
theoretical result. For an implementation-oriented methods paper, start from
[`ectheory-data-analysis`](../skills/ectheory-data-analysis/SKILL.md) and
[`ectheory-replication-and-data-policy`](../skills/ectheory-replication-and-data-policy/SKILL.md), then
use [`external_tools.md`](external_tools.md) to set reproducibility expectations.

## Suggested workflow

1. Gate the result with [`ectheory-topic-selection`](../skills/ectheory-topic-selection/SKILL.md):
   state the theorem or methodological result as the contribution, not an application.
2. Position the result with
   [`ectheory-literature-positioning`](../skills/ectheory-literature-positioning/SKILL.md) and
   [`ectheory-contribution-framing`](../skills/ectheory-contribution-framing/SKILL.md): name the
   frontier theorem, special case, or asymptotic environment being extended.
3. Stress-test assumptions and proof architecture with
   [`ectheory-identification-strategy`](../skills/ectheory-identification-strategy/SKILL.md).
4. If computation is used, design it with
   [`ectheory-data-analysis`](../skills/ectheory-data-analysis/SKILL.md): simulations probe the theorem's
   boundary cases rather than substituting for proof.
5. Before submission, run
   [`ectheory-submission`](../skills/ectheory-submission/SKILL.md) and verify all volatile facts against
   [`official-source-map.md`](official-source-map.md).
