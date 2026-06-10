---
name: geb-rebuttal
description: Use after a Games and Economic Behavior revise-and-resubmit to organize responses on theory novelty, equilibrium/proof details, experiments, simulations, Editor-in-Charge priorities, and Elsevier revision files.
---

# R&R Rebuttal (geb-rebuttal)

## When to trigger

- A GEB revision decision has arrived
- Referees question novelty, proof correctness, equilibrium selection, experiment design, or fit
- You need a response letter that respects the Editor-in-Charge process

## Triage categories

1. **Theory correctness**: missing proof step, equilibrium existence/uniqueness,
   refinement, comparative statics, boundary case, or counterexample.
2. **Novelty and positioning**: the paper may be a corollary, special case, or
   incremental extension of known game-theory results.
3. **Experimental / numerical evidence**: underpowered experiment, unclear
   treatment, robustness, code, or simulation design.
4. **Exposition**: notation, game form, timing, payoff matrix, assumptions, or
   abstract length.
5. **Fit**: contribution to game theory is not visible enough.

## Response strategy

- Start with the editor's synthesis, then handle referee comments in order.
- For proof comments, add the missing lemma/proof or narrow the theorem.
- For novelty comments, compare theorem-by-theorem with the closest prior result.
- For experimental comments, add power, robustness, treatment checks, or clearer
  implementation details.
- Keep the contribution framed as advancing game theory or its applications, not
  merely adding a new empirical setting.

## Response paragraph pattern

```text
We thank the referee for identifying this issue. We now revise [theorem/model/
experiment] by [change]. The new material appears in [section/table/appendix].
It addresses the concern because [logic tied to equilibrium/proof/design].
```


## Response pass for Games and Economic Behavior

Treat this skill as an executable review pass, not a prose hint. First lock the primitives, equilibrium concept, comparative statics, and proof or experiment boundary; then judge whether the current manuscript answers the venue's real reader: game theorists who ask what the model teaches beyond a clever example.

- **Do the pass:** Separate editor-order changes from referee-specific changes; answer each major objection with manuscript edits plus a short evidence citation, not tone.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against JET for theory abstraction, Theoretical Economics for compact theory contribution, Experimental Economics for experiment-first designs; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```text
[Decision] major revision / minor revision
[Editor priority] ...
[Theory changes] ...
[Experiment/numerics changes] ...
[Positioning changes] ...
[Next step] revise manuscript + response letter
```
