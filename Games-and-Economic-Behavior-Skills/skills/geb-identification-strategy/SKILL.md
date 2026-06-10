---
name: geb-identification-strategy
description: Use when the analytical core of a Games and Economic Behavior (GEB) manuscript is the bottleneck — assumptions, theorem statements, proof exposition, and generality for a game-theory paper (and the experimental-identification analogue for behavioral work). Stress-tests the argument's correctness, tightness, and readability.
---

# Identification Strategy — Assumptions, Results & Proofs (geb-identification-strategy)

## When to trigger

- The theorem is (you believe) true but the proof is hard to follow or audit
- You are unsure which assumptions are doing the work versus merely convenient
- A reviewer may ask "does this hold without assumption A / with infinite players / in continuous time?"
- For experimental work: the design does not cleanly separate competing strategic theories

## What "identification" means at a theory journal

GEB is a **game-theory** journal, so for theoretical papers the "identification strategy" is the **logical architecture of the result**, not a causal-inference design. The bar is correctness, tightness, and generality, with proofs a referee can verify. Because the Editor in Charge routes the paper to an **anonymous Advisory Editor** and expert referees, the argument must withstand specialists who will reconstruct each step. Treat this skill in two branches.

### Branch A — Theory (equilibrium, mechanism design, learning)

- **Map the assumptions.** List every assumption; for each, state *why it is needed* and *what breaks without it*. Separate substantive assumptions from normalizations.
- **State results precisely.** Each theorem/lemma/proposition self-contained: domain (class of games), hypotheses, conclusion. Number them for cross-reference.
- **Establish generality and limits.** Finite vs. infinite players/actions, complete vs. incomplete information, static vs. dynamic; give the most general statement the proof supports and note where it fails (a clean counterexample at the boundary is valued).
- **Proof exposition.** Lead with the idea before the algebra; signpost the construction; relegate long calculations to an appendix; ensure every invoked result (fixed-point theorem, separating hyperplane, etc.) has its hypotheses checked. Tightness: is the bound achieved? Is uniqueness or only existence shown?
- **Verify computationally as illustration, not proof.** Use a solver (e.g., Gambit) to confirm worked examples and equilibria, but the written proof must stand alone.

### Branch B — Behavioral / experimental identification

- **Design separates theories.** Treatments must distinguish the competing strategic hypotheses (e.g., level-k vs. QRE vs. equilibrium), not just reject a null.
- **Power and unit of observation.** Justify sample size per cell; the independent unit is the **session**, not the subject — cluster inference accordingly.
- **Confounds and incentives.** Salient incentives, no demand effects, randomization across roles/order; pre-register the hypotheses where possible.
- **Structural discipline.** If estimating a behavioral model, state identification of its parameters.

## Anti-patterns

- A proof that is a wall of algebra with no stated idea or roadmap
- Unstated assumptions silently used mid-proof
- Claiming generality the proof does not reach (e.g., asserting an infinite-game result proved only for finite games)
- Numerical examples presented as if they were a proof
- An experiment that rejects a null but cannot tell which strategic theory wins


## Identification pass for Games and Economic Behavior

Use this as a second-pass capability check. First lock the primitives, equilibrium concept, comparative statics, and proof or experiment boundary; then test whether the manuscript addresses game theorists who ask what the model teaches beyond a clever example.

- **Primary move:** State identifying variation, identifying assumption, falsification, sensitivity, and the table/figure that would convince a skeptical referee.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against JET for theory abstraction, Theoretical Economics for compact theory contribution, Experimental Economics for experiment-first designs; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Branch】theory / behavioral-experimental
【Main result】one-line statement (domain → conclusion)
【Assumptions】[each: needed because ... / fails without ...]
【Generality】most general statement supported; known limits
【Proof exposition】idea-first? steps signposted? invoked theorems checked? [Y/N each]
【Tightness】bound achieved / uniqueness vs. existence
【(Behavioral) design】separates theories? session-clustered? powered? [Y/N each]
【Next step】geb-data-analysis or geb-tables-figures
```
