---
name: podc-experiments
description: Use when building the evidence for an ACM PODC paper — where "evidence" is a proof, not a benchmark. Covers matching upper and lower bounds, tightness arguments, model and assumption stress-tests, adversary-strength calibration, and the honest, clearly-optional role of any simulation in a distributed-computing-theory paper.
---

# PODC Experiments

At PODC the "experiment" is a **proof**, and the strongest result is a **matching bound**. This
skill is the theory analogue of an empirical-evaluation section: it is about making the *evidence for
correctness and optimality* as strong as the venue expects. There is no benchmark leaderboard, no
artifact track, and a simulation never establishes the result — it can only illustrate it.

## Match the evidence to the claim shape

| Claim | What counts as evidence at PODC | Common failure caught |
|---|---|---|
| "Algorithm A solves problem P in model M" | A proof of the required properties (e.g., agreement, validity, termination) in exactly M | Property proved in a stronger model than claimed |
| "A costs O(f(n))" | A proof of the upper bound over all executions/adversary choices | Bound holds only in the best case, not worst/expected as stated |
| "A is optimal" | A **matching Ω(f(n)) lower bound** in the same model | "Optimal" asserted with no lower bound |
| "P is impossible in M" | An impossibility proof (valency, indistinguishability, covering) | Impossibility shown for a weaker model than claimed |
| "A self-stabilizes" | A proof of convergence from every state + closure | Convergence shown from some states only |

## The matching lower bound is the headline evidence

A PODC upper bound is good; an upper bound **plus a matching lower bound** is the venue's gold
standard, because together they *close the problem*. Before submission, ask:

- Is there a lower bound in the literature my algorithm meets? Cite it and state that I match it.
- If not, can I prove one? A matching bound often turns a solid paper into a distinguished one.
- If my bound is not tight, say so explicitly and state the gap — an honest "we leave closing the
  gap open" is far better than an unsupported "optimal."

## Stress-test the model and assumptions

The most common fatal flaw at PODC is a proof that quietly relies on an assumption stronger than the
stated model. Audit every assumption:

```text
[Timing]     does any step assume a message arrives "soon" in an asynchronous model? (illegal)
[Faults]     does the proof assume a Byzantine party behaves in a bounded way? (only if justified)
[Adversary]  is the adversary adaptive as claimed, or does the analysis secretly need oblivious?
[Atomicity]  in shared memory, are the assumed primitives (CAS, LL/SC, registers) really available?
[Randomness] does correctness need a shared coin the model does not provide?
[Initialization] for self-stabilization, does convergence hold from *every* configuration?
```

For each, either the proof survives the weakest form of the assumption in your model box, or the
theorem statement must be weakened to name the stronger assumption. This audit is the theory
equivalent of a threats-to-validity section, and reviewers perform it whether or not you do.

## Calibrate the adversary and the regime

- **Adversary strength:** state whether the adversary is adaptive (corrupts reacting to the
  execution) or oblivious (fixed in advance), and whether it sees message contents or only patterns.
  A protocol secure against an oblivious adversary and claimed against an adaptive one is a classic
  overclaim.
- **Fault threshold:** state the exact resilience (t < n/2, t < n/3, etc.) and whether it is tight
  for the model. Optimal-resilience claims need the corresponding impossibility.
- **Parameter regime:** if a bound holds only for a range of n, t, or network diameter, state the
  range; do not present a conditional result as unconditional.

## Simulations: optional, illustrative, honest

If your paper includes a simulation (many PODC papers include none), it must be framed as *optional*:

- State plainly that it **illustrates** a constant, a convergence rate, or average-case behavior and
  does **not** establish the theorem.
- Report the parameter ranges, number of trials, and random seeds; a plot without these is not
  reproducible even as an illustration.
- Never let a plot substitute for a missing proof or a missing lower bound. A reviewer who sees
  "scales well" in place of a bound reads it as a systems paper in the wrong venue
  (`podc-topic-selection`).
- Keep any simulation code out of the anonymized submission's identifying links (see
  `podc-reproducibility` and `podc-submission`).

## Pre-submission evidence checklist

```text
[ ] Every claimed property is proved in exactly the stated model (no assumption creep)
[ ] Upper bounds hold in the stated case (worst/expected), not just best case
[ ] Optimality claims carry a matching lower bound (or are downgraded to "we conjecture / leave open")
[ ] Resilience threshold stated and, if claimed optimal, backed by an impossibility
[ ] Adversary strength and randomness assumptions match the proof's real needs
[ ] Any simulation is labeled optional, with ranges/trials/seeds, and establishes nothing
```

## Output format

```text
[Claim -> evidence] each theorem mapped to its proof; property proved in the stated model?
[Tightness] matching lower bound present / cited / proved / honestly left open?
[Assumption audit] timing/faults/adversary/atomicity/randomness/initialization all consistent with the model box?
[Adversary/regime] strength and parameter range stated correctly?
[Simulation] absent / present-and-labeled-optional (ranges, trials, seeds)?
[Fix queue] <assumption creep to fix; missing lower bound; overclaimed optimality>
```
