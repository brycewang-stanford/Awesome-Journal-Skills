---
name: jet-topic-selection
description: Test whether a project clears the Journal of Economic Theory (JET) scope gate — a rigorous, original theoretical contribution in one of JET's core areas (mechanism design, information, decision theory, game theory, matching, market design, political economy, finance/macro theory), with empirical/computational work admitted only when firmly grounded in theory. Use at the very start.
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
