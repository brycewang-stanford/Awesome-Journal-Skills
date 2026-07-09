---
name: pods-experiments
description: Use when designing or auditing the analytical "evidence" of an ACM PODS paper — worst-case and average-case analyses, matching upper and lower bounds, dichotomy completeness, correct complexity assumptions, and the occasional empirical validation when a theory paper claims practicality — matching the rigor to the shape of each theoretical claim.
---

# PODS Experiments

Use this before submission when the technical story is not yet locked. For PODS the "experiments" are
mostly **analyses and proofs**, because the reviewers are theoreticians and the evidence is a theorem,
not a benchmark. The organizing principle is **rigor proportional to the claim** — the analysis must
establish exactly what the paper asserts, in the model it names, with no hidden gap.

## Analysis audit

- **Match the analysis to the claim shape.** A claim of optimality needs a *matching lower bound*; a
  claim of a classification needs *completeness* (every case decided); a claim of efficiency needs an
  exact complexity in a stated measure (data vs. combined), not an asymptotic hand-wave.
- **Close the upper/lower-bound gap, or state it.** An upper bound without a lower bound is not
  optimality; if the gap is open, say so precisely rather than implying tightness.
- **State every complexity assumption.** Conditional hardness (ETH, SETH, OMv, the exponential-time
  hypothesis, `P ≠ NP`, `#P`-hardness) must be named where the bound is stated; never dress a
  conditional lower bound as unconditional.
- **Check the model does not smuggle the result.** A cost model, a data model restriction, or an
  encoding choice can trivialize or inflate a bound; make the modeling assumptions explicit and defend
  them as realistic for data management.
- **Handle constants and parameters honestly.** Hidden dependence on the query size, the schema, or a
  fixed parameter can turn a "linear" claim into something else; state what is held constant.
- **When you claim practicality, show it — carefully.** PODS papers occasionally include a small
  empirical validation to illustrate that the theory's constants are reasonable. If you do, it is a
  supporting illustration, not the contribution: report it modestly, and never let a benchmark stand
  in for a missing proof.

## Claim-to-rigor design table

| PODS claim | Matching rigor | Reject pattern avoided |
|---|---|---|
| "Our algorithm is worst-case optimal" | Upper bound + matching lower bound in the same model | "Fast in experiments" with no lower bound |
| "We classify the whole query class" | A dichotomy proof covering every case, both sides | A tractability result for some queries only |
| "Evaluation is `coNP`-complete" | Membership proof + a hardness reduction | Hardness asserted from a single example |
| "The semantics is well-defined and computable" | Well-definedness proof + a decidability/complexity result | A definition with no algorithmic content |
| "This bound is unconditional" | A proof that names no unproven conjecture | A conditional bound presented as absolute |

## Assumption and model discipline

```text
[Complexity measure]  data complexity / combined complexity / parameterized — state which and stay consistent
[Cost model]          RAM / arithmetic / communication (MPC rounds) — fix it before stating a bound
[Conjectures]         name each (ETH/SETH/OMv/#P) exactly where a conditional bound depends on it
[Encoding]            make input encoding explicit when it affects the bound (unary vs. binary, etc.)
[Parameters]          say what is fixed and what varies; expose hidden query-size dependence
```

## Optional empirical validation (when a paper claims practicality)

- Keep it small and clearly secondary; state the implementation and inputs so the illustration is
  reproducible, but do not turn the paper into a systems submission.
- Never use measured speed to substitute for an unproven bound — a PODS reviewer reads that as a gap.
- If the practical behavior diverges from the worst-case theory, say so; the honesty strengthens the
  paper.

## Vignette: proving an algorithm optimal

Suppose the paper claims a new join-evaluation algorithm is worst-case optimal. The matching plan:
state the exact output-size bound the algorithm meets; prove the running-time upper bound in the stated
cost model; prove a matching lower bound showing no algorithm in the model beats it (or cite the known
information-theoretic bound and prove your algorithm meets it); and state precisely the class of queries
and inputs for which optimality holds, flagging what is left open — every step in the body or the
at-submission appendix.

## Rigor reporting floor

- A matching lower bound for every optimality claim, or an explicit open-gap statement.
- Every conditional result labeled with its assumption at the point of statement.
- The complexity measure and cost model fixed once and used consistently.

## Output format

```text
[Rigor readiness] strong / adequate / gap present
[Claim -> rigor map] <claim: upper bound / lower bound / completeness / assumption>
[Tightness] <matching bound present? or open gap stated precisely?>
[Assumptions] <every conditional bound labeled with ETH/OMv/#P/etc.? yes/no>
[Model check] <cost/data model explicit and not smuggling the result? yes/no>
[Decision-critical next step] <the one proof to finish or the one bound to match>
```
