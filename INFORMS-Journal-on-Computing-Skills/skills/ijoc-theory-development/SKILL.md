---
name: ijoc-theory-development
description: Use when the algorithm or model formulation, its correctness, and its theoretical guarantees are the bottleneck for an INFORMS Journal on Computing (IJOC) manuscript. Pins down formulation, complexity, and what the method provably does before experiments are finalized; it does not run the experiments.
---

# Algorithm & Model Formulation (ijoc-theory-development)

## When to trigger

- An algorithm "works" empirically but its **statement, invariants, and termination** are not written down rigorously
- A formulation is proposed but its **validity** (the model exactly captures the problem; the cuts are valid; the relaxation is correct) is asserted, not argued
- A referee asks for **complexity, convergence, approximation ratio, or correctness** and the paper has none
- A heuristic or ML method needs the **theoretical scaffolding** (what it guarantees, when it can fail) that distinguishes IJOC from a pure benchmark paper

## What "theory" means at IJOC

IJOC is not a pure-theory journal, but it expects the **method to be defined and defended**, not just demonstrated. The advance is computational, yet referees want to know *why the method is correct* and *what it provably achieves* before they trust the experiments. Match the rigor to the archetype — an exact method needs validity and finiteness; a heuristic needs a clear procedure and, where possible, bounds; an ML-for-OR method needs a stated learning task and a guarantee or a falsifiable claim. The theory and the experiments must agree: a proven worst case should be visible in the runtime-vs-size plot.

## Branch paths

### Branch A: Exact methods (B&B / B&C / B&P, decomposition)
- **State the formulation precisely** and prove it is a valid model of the problem (feasible region = exactly the intended solutions).
- **Prove validity of cuts / columns / Benders cuts**; show the separation/pricing problem and its complexity.
- **Argue finite termination / correctness** of the algorithm; state the relaxation and any bound-tightening.
- **Complexity:** give the per-iteration cost and, where possible, worst-case size; if NP-hard, say so and motivate the empirical study that follows.

### Branch B: Heuristics / metaheuristics / matheuristics
- **Write the procedure as pseudocode** with explicit neighborhood/operators, acceptance rule, and stopping criterion — reproducibility starts here.
- **State guarantees where they exist:** approximation ratio, performance bound, local-optimality conditions; if none, say the contribution is empirical and design the experiments to earn that claim.
- **Argue why the design fits the structure** of the problem (what the operator exploits), not just "it performed well."

### Branch C: Machine learning for OR / learning-to-optimize
- **Define the learning task and the loss** precisely; state what is learned and what is solved exactly.
- **Generalization claim:** state the distribution of instances and what is claimed to transfer; provide a guarantee or a falsifiable out-of-distribution test plan.
- **Feasibility/optimality safeguards:** if a learned policy can produce infeasible or arbitrarily bad solutions, state the repair/guarantee that prevents it.

### Branch D: Simulation / computational probability
- **Specify the model and estimator**; state unbiasedness/consistency and the variance behavior.
- **Variance reduction:** state the technique (CRN, control variates, importance sampling) and prove or argue it reduces variance for this estimand.
- **Convergence / error bounds** for the computational scheme; state regularity assumptions.

## Checklist

- [ ] Branch chosen; the method is stated as a formal formulation or pseudocode, not prose only
- [ ] Exact: model validity proven; cuts/columns valid; finite termination/correctness argued; complexity stated
- [ ] Heuristic: full pseudocode; bounds stated where they exist; design tied to problem structure
- [ ] ML-for-OR: learning task + loss defined; generalization claim falsifiable; feasibility safeguard stated
- [ ] Simulation: estimator properties + variance-reduction justification given
- [ ] Every theorem has assumptions stated and a proof (main text or supplement, but referenced)
- [ ] The theoretical claim and the experimental claim do not contradict each other

## Anti-patterns

- "The algorithm converged / it works" presented as if it were correctness or a guarantee
- Asserting cut/column validity without proof — a fatal flaw for an exact-methods paper
- A heuristic with no pseudocode, so neither referee nor the GitHub deposit can reproduce it
- An ML-for-OR method that can return infeasible solutions with no stated safeguard
- Claiming an approximation ratio that the experiments quietly violate
- Burying the proof of a key result in a supplement the main paper depends on (keep the main paper self-contained on its central claims)

## Worked vignette (illustrative)

A paper proposes new valid inequalities for a stochastic facility-location MIP and a branch-and-cut that uses them. A weak version says "the cuts helped." An IJOC version: state the polyhedral result (the inequalities are facet-defining under a stated condition), give the separation algorithm and its O(n log n) cost, and prove they are valid for the original feasible region. Then the experiments are interpretable — the root-gap closure (say 31%, illustrative) and the node-count reduction are *predicted* by the theory, not surprises.

## Output format

```text
【Branch】exact / heuristic / ML-for-OR / simulation
【Formulation or pseudocode】stated? [Y/N]
【Guarantee】validity / finiteness / complexity / approx ratio / variance — which, and proven where
【Assumptions】[...]
【What it does NOT guarantee】[...]
【Theory–experiment consistency】[Y/N]
【Next skill】ijoc-literature-positioning
```
