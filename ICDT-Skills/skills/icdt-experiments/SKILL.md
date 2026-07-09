---
name: icdt-experiments
description: Use when deciding what counts as evidence for an ICDT (International Conference on Database Theory) result — matching-bound complexity analysis as the primary evidence, worked examples and counterexamples that establish separations, and, only for papers with an algorithmic contribution, a proportional and honestly-scoped experimental evaluation that does not pretend to be the contribution.
---

# ICDT Experiments

At ICDT the primary "evidence" is a **proof**, not a benchmark. This skill is about matching your
*form of evidence* to your *claim*: most ICDT papers are purely theoretical and need no experiments
at all, while a minority with a genuine algorithmic contribution benefit from a small, honest
evaluation. Bolting a systems-style experiment section onto a theorem paper does not raise its
standing — a loose bound or an unproved lemma will still sink it.

## Match the evidence to the claim shape

| Claim shape | Primary evidence | Experiments? |
|---|---|---|
| Complexity of evaluating a query class | Matching upper and lower bounds, with proofs | No — the bound is the result |
| Expressiveness / separation | A construction or an Ehrenfeucht-Fraisse game establishing the separation | No — a witness, not a benchmark |
| Decidability / undecidability of a problem | An algorithm + termination proof, or a reduction from an undecidable problem | No |
| A new *algorithm* with a claimed practical complexity | The complexity proof **plus** an optional experiment showing the constants are reasonable | Optional, proportional |
| A dichotomy | Proof that each side holds and the boundary is exactly as stated | No |

The default answer is "the theorem is the evidence." Reach for experiments only when your paper
claims something about *practice* that the asymptotic bound alone does not settle.

## Making the theoretical evidence airtight

- **Tightness:** if you claim a bound is tight, prove both directions and label which is the upper
  and which the lower. A one-sided bound presented as a complete answer is the classic "revise."
- **The right complexity measure:** be explicit about data vs combined vs query complexity, and prove
  the bound in the measure you claim it for.
- **Worked examples and counterexamples:** a small concrete database and query that illustrates the
  construction, or a counterexample that rules out a tempting stronger statement, is high-value
  evidence a referee can check by hand — include it in the body.
- **Corner cases:** state what happens at the boundaries of your class (empty instances, cyclic vs
  acyclic, bounded arity) rather than leaving the referee to wonder whether a case breaks the proof.

## If your paper does include an experiment

Some ICDT papers contribute an algorithm whose *worst-case* bound understates or overstates its
behavior on realistic inputs. If you evaluate it, do so with the rigor the theory earns:

```text
[Purpose]     state exactly what the experiment tests that the proof does not (e.g., typical-case
              runtime, the size of the hidden constant, scaling on real query workloads)
[Subjects]    real or standard benchmark data/queries, described precisely; no cherry-picked inputs
[Baseline]    a fair comparison (a prior algorithm, a naive method) implemented honestly
[Reporting]   enough runs, hardware stated, and results that support only what you claim
[Scope]       the experiment supplements the theorem; it never substitutes for a missing proof
```

Keep it proportional: an ICDT experiment is a paragraph-to-a-page confirmation, not a systems-paper
evaluation. If the experiment *is* the contribution, the paper likely belongs at **EDBT/SIGMOD**, not
ICDT (see `icdt-topic-selection`).

## Honesty and scope

- Do not report an experiment whose setup you would not want a referee to reproduce; ICDT referees
  are skeptical of evaluations that appear to decorate a theorem.
- Do not claim practical impact the experiment does not show — "faster on our three instances" is not
  "faster in practice."
- State the model assumptions your algorithm relies on and whether the experiment respects them.

## Output format

```text
[Claim -> evidence] <each claim -> proof (bounds/construction) or experiment>
[Tightness] bounds matched and labeled? yes/no/na
[Complexity measure] data / combined / query, proven in the claimed measure? yes/no
[Experiment] none (theory-complete) / proportional supplement / over-scoped (reroute?)
[Fix queue] <ordered: close bound gaps first, then examples, then any experiment>
```
