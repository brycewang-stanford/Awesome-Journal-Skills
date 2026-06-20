---
name: aejmic-theory-model
description: Use when the model setup, equilibrium concept, or proof architecture is the bottleneck for an American Economic Journal: Microeconomics (AEJ: Micro) manuscript — the central skill for a theory-first paper. Builds the model to the AEJ: Micro bar (clean, general, well-motivated result); it does not check whether your theorem is correct.
---

# Theory Model & Proof Architecture (aejmic-theory-model)

This is the **central skill** for AEJ: Micro. The journal is theory-first: the deliverable is a **clean, general, well-motivated result** — a theorem, characterization, or impossibility — that a broad microeconomics audience finds illuminating. Get the model and the proof right before anything else.

## When to trigger

- The primitives (players, actions, information, timing, payoffs) are not yet pinned down
- The **equilibrium / solution concept** is unstated or mismatched to the question
- A result is conjectured but the **proof strategy** is unclear or fragile
- You are trading **generality against tractability** and cannot decide where to cut
- A referee questions which assumption the result actually depends on (then pair with `aejmic-identification`)

## The AEJ: Micro modeling bar

AEJ: Micro wants the **economics to be the point**: the model should be the *simplest* environment in which the mechanism is visible, and the result should travel beyond the example. It sits between *JET*/*GEB* (specialist, often maximal generality) and *AEJ: Applied* (empirical). Aim for a result that a non-specialist micro theorist can state in one sentence and that a specialist finds non-obvious.

### 1. Model setup — make primitives minimal and motivated
- State **players, action sets, information structure, timing, and payoffs** explicitly; flag every assumption that is substantive vs. WLOG.
- Prefer the **minimal environment** that exhibits the mechanism; add structure only when it earns its keep in the result.
- Motivate each non-standard assumption economically (an institution, a friction), not just for tractability.

### 2. Equilibrium / solution concept — name it and justify it
- Pick the concept that matches the question: Nash / subgame-perfect / sequential / PBE; dominant-strategy or Bayesian incentive compatibility (mechanism design); stability / core (matching, market design); rationalizability or level-k (behavioral).
- State **existence** and, where it matters, **uniqueness** (or characterize the equilibrium set). Refinements should be justified, not invoked to rescue a result.

### 3. Proof strategy — choose the architecture before writing it
- Common architectures: **construction** (exhibit the object), **revelation principle** then optimize over direct mechanisms, **fixed-point / monotone-comparative-statics** (Topkis, single-crossing), **duality / LP** (information design, Bayesian persuasion), **induction on type/stage**, **variational / first-order** arguments, **impossibility by contradiction**.
- For a characterization, prove both directions; for an optimum, verify the candidate is global (not just a local/first-order point).

### 4. Generality vs. tractability — decide deliberately
- A finite/binary type space that exposes the mechanism cleanly often beats a continuum that buries it. State the cost: what does the simplification rule out?
- If the general case is the contribution, prove it generally; if the *insight* is the contribution, prove it where it is cleanest and discuss extension in `aejmic-robustness`.

### 5. Where proofs live
- Short, illuminating proofs (or proof sketches) in the **main text**; long or routine proofs in the **appendix**. The main paper should be self-contained for the key results — do not hide a load-bearing proof in supplementary material.

## Checklist

- [ ] Primitives stated explicitly; each assumption marked substantive vs. WLOG, with economic motivation
- [ ] Solution concept named, matched to the question, with existence (and uniqueness/characterization where relevant)
- [ ] Main result stated as a numbered **Proposition/Theorem** in words a non-specialist can parse
- [ ] Proof architecture chosen and stated; candidate optima verified global, both directions of a characterization proved
- [ ] Generality-vs-tractability call made deliberately, with the cost of any simplification stated
- [ ] Key proofs in main text; appendix carries the rest; main paper self-contained

## Anti-patterns

- A model loaded with assumptions, several only for tractability, none flagged — the mechanism is invisible
- Asserting an equilibrium without existence, or invoking a refinement only to rescue the result
- "It can be shown that…" standing in for a proof of a load-bearing claim
- Maximal generality that obscures the economic point (reads as *JET*, not AEJ: Micro), or a one-off example with no result that travels
- A first-order condition presented as if it established a global optimum

## Worked vignette: a screening result (illustrative)

A monopolist screens buyers with private values. A weak setup throws in a continuum of types and three frictions at once; the optimal-contract characterization becomes a thicket. The AEJ: Micro move: start with **two types**, derive the standard "no distortion at the top, downward distortion below" characterization as a clean Proposition, prove it by the relaxed-program-then-verify-monotonicity architecture, then in `aejmic-robustness` show the continuum case preserves the qualitative result. The two-type model is the simplest environment where the distortion is visible — and the result travels.

## Output format

```
【Model】players / actions / information / timing / payoffs (substantive vs. WLOG flagged)
【Solution concept】[Nash/SPE/PBE/IC/stability/…] + existence/uniqueness
【Main result】Proposition stated in words
【Proof architecture】[construction / revelation+optimize / fixed-point / duality / induction / impossibility]
【Generality call】where proved + cost of any simplification
【Proofs live】main text: [...]; appendix: [...]
【Next step】aejmic-identification (what makes it tight) or aejmic-robustness (extensions)
```

## Supplementary resources

- [`../../resources/worked-examples/01-introduction.md`](../../resources/worked-examples/01-introduction.md) — a theory-paper intro arc (puzzle → model → proposition → driving assumption)
- [`../../resources/exemplars/library.md`](../../resources/exemplars/library.md) — real AEJ: Micro theory papers by area
