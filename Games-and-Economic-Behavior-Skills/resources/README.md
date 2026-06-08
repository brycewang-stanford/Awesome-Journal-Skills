# GEB Resources

Action-oriented resources for the *Games and Economic Behavior* (GEB) skill pack. The `skills/` give
advice; this directory lets an agent **act** — model a GEB-style game-theory section and benchmark
against verified exemplars. Pair these with the relevant `skills/geb-*/SKILL.md`.

GEB publishes **game theory** — a model plus an equilibrium/characterization result, with a strong
secondary stream of behavioral and experimental work. The resources here are scoped to that venue.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a **game-theory** paper introduction in GEB house style (question → result-in-words-then-formally → key idea → scope; the contribution sentence on page one). Illustrative fictional model + equilibrium result — no invented policy. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified GEB (Elsevier) papers** organized by theme × method (theory, solution concepts, learning, behavioral, experimental, market design). Design positioning only — no fabricated results — with a sibling-confusion guard against Econometrica / JET / Theoretical Economics / Games (MDPI) / IJGT. |
| [`official-source-map.md`](official-source-map.md) | **GEB-specific policy & facts:** Editorial Manager submission, elsarticle / `elsarticle-num`, the 250-word abstract cap, the Game Theory Society affiliation, the Editor-in-Charge / Advisory-Editor process, data policy (*encouraged, not mandatory*), and explicit 待核实/to-verify flags. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | Game-theory toolkit referenced by the pack: theorem typesetting; equilibrium computation (Gambit, `nashpy`, SymPy, QuantEcon); mechanism/market-design solvers; experiment platforms (oTree, z-Tree); and session-level experimental inference. |

## Scope note: no econometric code kit (game-theory venue)

Unlike the empirical-craft packs, this directory **does not vendor a causal-inference / econometrics
code kit** (DID / IV / RDD / DML Stata + Python pipeline). GEB is a specialist **game-theory** journal:
the relevant computational tools are **equilibrium solvers, symbolic proof-checkers, and experiment
platforms**, not panel-data estimators. Those tools — and how to use them so a numerical example is a
verifiable *illustration* of a proof, never a substitute for it — are documented in
[`external_tools.md`](external_tools.md). For the *encouraged-but-not-mandatory* GEB data/replication
stance, see [`official-source-map.md`](official-source-map.md).

## Suggested workflow

1. Scope and frame with [`../skills/geb-topic-selection`](../skills/geb-topic-selection/SKILL.md)
   ("what does this advance in game theory?") and
   [`../skills/geb-contribution-framing`](../skills/geb-contribution-framing/SKILL.md); model the
   introduction on [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
2. Position against the frontier with
   [`../skills/geb-literature-positioning`](../skills/geb-literature-positioning/SKILL.md), benchmarking
   theme × method against the verified papers in [`exemplars/library.md`](exemplars/library.md).
3. Build and check the result with the game-theory toolkit in
   [`external_tools.md`](external_tools.md) (Gambit / `nashpy` / SymPy for equilibria and counterexamples;
   oTree / z-Tree + session-level inference for experiments).
4. Polish prose and the ≤250-word abstract with
   [`../skills/geb-writing-style`](../skills/geb-writing-style/SKILL.md); confirm submission, formatting,
   AI-declaration, and data policy in [`official-source-map.md`](official-source-map.md).
