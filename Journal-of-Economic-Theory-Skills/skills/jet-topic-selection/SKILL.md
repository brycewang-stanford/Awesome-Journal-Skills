---
name: jet-topic-selection
description: Use when testing whether a project clears the Journal of Economic Theory (JET) scope gate — a rigorous, original theoretical contribution in a core theory area, with empirical/computational work only when firmly grounded in theory.
---

# Topic Selection (jet-topic-selection)

## When to trigger

- Deciding whether a result belongs at JET versus a field or empirical journal
- You have data, an experiment, or a computation and want to know if it can go to JET
- Choosing which of several results to lead with

## The JET scope gate

JET publishes across **mechanism design, information economics, decision theory, game theory,
matching, market design, political economy, and finance / macroeconomic / monetary theory** —
broad **general theory** in one venue, not a subfield niche. The single deciding criterion is a
**rigorous, original theoretical contribution**. Ask three questions:

1. **Is the core deliverable a theorem (or a genuinely new model/characterization)?** If the headline
   is a regression coefficient or a calibration with no new theoretical result, JET is off-fit —
   regardless of how clean the empirics are.
2. **Is it original and non-trivial?** A restatement of a known result, or a special case of an existing
   theorem, will not clear the desk screen (see jet-review-process).
3. **If there is empirical / experimental / quantitative / computational content, is it *firmly grounded
   in theory*?** JET admits such work **only** as the application or test of a theoretical contribution
   that is itself the paper's point — not as a stand-alone empirical paper.

## Decision rule

- **Lead with the theory.** State the result you would put in the abstract as a proposition/theorem.
  If you cannot, the project is not yet a JET paper.
- **Generality vs. tractability.** A clean result under transparent assumptions usually beats a more
  general result that no referee can verify (see jet-identification-strategy).
- **Subfield routing.** Name the area early — submissions are routed to the matching editor.

## Deliverable-type scope table

| Your core deliverable | JET verdict | If off-fit, reroute |
|---|---|---|
| New characterization / existence / impossibility theorem in a core area | in scope — lead with it | — |
| Counterexample overturning a folk presumption | in scope when the presumption matters to a literature | frame the economics of why the presumption mattered |
| New solution concept or preference axiomatization | in scope; expect heavy scrutiny of the axioms' behavioral content | — |
| Asset-pricing result whose substance is stochastic-analysis machinery (semimartingales, no-arbitrage functional analysis) | usually a better fit at a mathematical-finance venue; JET wants the economics of the theorem | finance theory belongs at JET when incentives, information, or equilibrium do the work |
| Structural estimation / calibration exercise | off-fit regardless of model quality | empirical or quantitative-macro journals |
| Market-design algorithm with performance proofs | in scope when the theorem is the contribution | otherwise an OR/CS venue |

## Vignette: a matching project at the gate

A team holds (i) a stability-existence theorem for matching with regional constraints, (ii)
simulations on synthetic data, and (iii) a policy application. Running the three questions:

- **Q1:** yes — the existence theorem is the deliverable; the simulations and policy story are not.
- **Q2:** check against the closest constrained-matching theorem before claiming novelty; if the
  result is a special case of a published substitutes condition, it will not clear the screen.
- **Q3:** the simulations only exhibit the constrained core's shape, so they compress into one
  numbered Example with a script (jet-data-analysis).

Verdict: JET-ready — lead with the theorem, demote the policy narrative to one motivation
paragraph, and name "matching / market design" for editor routing.

## Lead-result selection when you have several

- Prefer the result whose **assumptions are cleanest to state**, even if a sibling result is
  technically harder — the lead theorem is what the desk screen reads.
- A characterization beats an existence result as the headline when both are proved; existence can
  follow as a corollary section.
- Never lead with the comparative static if the underlying equilibrium object is itself new.

## Anti-patterns

- An applied-micro or finance paper with a token model bolted on
- A computational exercise with no characterization result behind it
- A marginal generalization of a published theorem framed as new

## Output format

```
【Core result】<the theorem/characterization in one sentence>
【Scope fit】in-scope theory area: <area> | off-fit: <why>
【Empirical/computational content】none | grounded-in-theory | stand-alone (off-fit)
【Verdict】JET-ready / reframe / send elsewhere → jet-literature-positioning
```
