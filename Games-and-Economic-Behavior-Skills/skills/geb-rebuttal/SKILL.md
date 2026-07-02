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

## Who reads the GEB response

- The **Editor in Charge** — one of the seven Editors, publicly known to you,
  with final decision authority — decides whether the revision returns to
  referees or is settled directly. Open the letter with a half-page summary
  written for that person: which objections were resolved, and how the main
  theorem or finding changed (or did not).
- The **Advisory Editor** who recommended the decision remains anonymous, as do
  referees; never guess identities or address evaluators by name.
- Under GEB's single-anonymized model, a referee may be an author of the
  nearest prior result. Meet novelty objections with theorem-level precision,
  not dismissal — that reader likely knows the prior proof better than you do.
- If a revision weakens or renames a theorem, flag it prominently; an Editor
  in Charge who finds a silently narrowed result late in the letter stops
  trusting the rest of it.

## Worked micro-example: a novelty objection

Referee: "Proposition 2 appears to be a special case of [prior theorem]."

- *Weak reply:* "Our setting differs, so the results are not comparable." —
  asserts without demonstrating, and reads as evasion to a specialist.
- *Strong reply:* "Proposition 2 is not implied by [prior theorem]: their
  argument uses quasi-concavity of payoffs (their Assumption A2), which our
  class violates (new Example 3). Remark 4 now states exactly which step of
  their proof fails in our environment, and Corollary 1 cites their result
  where the two genuinely overlap." — concedes the true overlap, isolates the
  delta, and gives manuscript locations for both.

## Revision-package mechanics (Editorial Manager)

- [ ] Point-by-point response letter + a marked-changes manuscript alongside
      clean **editable Word or LaTeX source** (required at every round)
- [ ] Keep theorem/section numbering stable where possible; if numbering moved,
      give an old-to-new map at the top of the letter
- [ ] New simulations or sessions added in revision: update seeds, scripts, and
      the voluntary data statement (see geb-replication-and-data-policy)
- [ ] Abstract still within the **250-word cap** after any reframing
- [ ] Generative-AI declaration still accurate if AI tools touched the revision


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
