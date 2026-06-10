---
name: mathfin-identification-strategy
description: Use when the mathematical core of a Mathematical Finance (Wiley) manuscript is the bottleneck — adapted for a theory journal, this means assumptions, theorem statements, proof architecture, and generality, not causal/empirical identification. Stress-tests rigor before exposition is polished.
---

# Assumptions, Theorems & Proof Architecture (mathfin-identification-strategy)

## Note on framing

*Mathematical Finance* is a **theory-first** journal: papers are evaluated on **methodological
novelty and rigor**, not empirical causal identification. The "identification" that matters
here is **mathematical identification** — pinning down the right assumptions, the precise
theorem, and a complete proof. This skill therefore covers assumptions, results, proof
exposition, and generality. (Empirical causal design is out of scope for this venue.)

## When to trigger

- A "model" is proposed but its formal properties (existence, uniqueness, no-arbitrage) are unproved
- The assumptions are vague (which filtration? which integrability? which regularity?)
- A proof has a gap, an unstated measurability/integrability condition, or a circular step
- You are unsure your generality is the right level for the contribution

## The rigor bar (the journal requires self-contained full proofs)

1. **State assumptions precisely.** Probability space, filtration and its conditions (usual
   conditions?), integrability ($L^p$, square-integrability), regularity, market structure
   (complete/incomplete), admissibility of strategies. Number them (A1, A2, ...) and reuse them.
2. **State the theorem cleanly.** Hypotheses → conclusion, with the object's existence,
   uniqueness, and characterization separated. Avoid burying conditions in prose.
3. **Make the proof self-contained.** Full proofs of all formal results are required; cite
   external theorems with exact hypotheses and check they apply (e.g., that a martingale is
   genuinely a martingale, not just a local one).
4. **Get the generality right.** Too narrow → looks like a special case (see
   mathfin-literature-positioning); too broad → the proof breaks. Justify each assumption:
   is it essential, or a convenience that could be relaxed?
5. **Guard the standard pitfalls.** Local vs. true martingale, integrability of stochastic
   integrals, applicability of Itô / Girsanov / Feynman–Kac, well-posedness of SDEs/BSDEs,
   verification of HJB solutions, smooth-fit at free boundaries, NFLVR/FTAP conditions.

## Branch paths

- **Pricing / no-arbitrage:** establish the (equivalent) martingale measure; verify NFLVR /
  FTAP hypotheses; confirm the discounted price is a true martingale.
- **Stochastic control / portfolio:** state the HJB / verification theorem; check admissibility
  and the transversality/integrability conditions; prove the candidate is optimal, not just stationary.
- **BSDE / duality:** existence–uniqueness under stated drivers; comparison theorem if used;
  rigorous duality gap = 0 argument.
- **Optimal stopping / free boundary:** Snell envelope or variational inequality; smooth-pasting
  justified, not assumed.

## Assumption-block and statement templates

A house-style assumption block fixes the stochastic basis once and lets every result refer to
it by label:

```latex
\begin{assumption}\label{ass:basis}
$(\Omega,\mathcal F,(\mathcal F_t)_{t\in[0,T]},\mathbb P)$ is a filtered probability space
satisfying the usual conditions and supporting a $d$-dimensional Brownian motion $W$.
\end{assumption}

\begin{assumption}\label{ass:coeff}
$b,\sigma$ are progressively measurable; $\sigma\sigma^{\top}$ is uniformly elliptic and
$\mathbb E\!\int_0^T \big(|b_t|^2 + |\sigma_t|^4\big)\,dt < \infty$.
\end{assumption}

\begin{theorem}\label{thm:main}
Under Assumptions \ref{ass:basis}--\ref{ass:coeff}, the value function ... Moreover, the
optimal strategy $\pi^{\star}$ is admissible and unique up to indistinguishability.
\end{theorem}
```

Separating the basis assumption from the coefficient assumption lets you weaken one without
touching results that need only the other — referees notice and reward this modularity.

## Where each lemma lives

- **Main text:** the lemma carrying the new idea (a novel estimate, a new compactness or
  selection argument) — referees should meet it before the main proof, with a sentence saying
  why existing estimates fail.
- **Appendix:** routine verifications (moment bounds, measurability of value functions,
  standard localization steps) — each still proved in full, never waved at.
- **Inline remark:** one-line consequences of cited results, with the citation pinned to the
  exact theorem number and a sentence confirming its hypotheses hold here.
- Never split one proof across main text and appendix mid-argument: give a sketch in the text
  and defer the complete proof as a single unit.

## Anti-patterns

- "It is well known that..." standing in for a required step.
- Assuming an integrability/measurability condition only where convenient.
- Treating a local martingale as a martingale without a uniform-integrability argument.
- Stating maximal generality the proof cannot support.
- Relegating a load-bearing lemma to "the reader can verify."

## Output format

```
【Main theorem】hypotheses → conclusion (one line)
【Assumptions】[A1, A2, ...] with role of each
【Proof architecture】lemmas → main steps → where external theorems enter
【Generality check】each assumption: essential / relaxable
【Pitfalls cleared】[martingale, integrability, well-posedness, smooth-fit, ...]
【Gaps remaining】[...]
【Next step】mathfin-contribution-framing
```
