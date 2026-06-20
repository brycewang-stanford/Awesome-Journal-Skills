---
name: aeri-theory-model
description: Use when a model — a full theory paper's argument or the structural/conceptual scaffolding behind an empirical AER: Insights short-format manuscript — needs to be made minimal, so it carries the single insight in a few pages. Keeps only what the insight requires; it does not develop a general framework.
---

# Theory / Model — Minimal to Carry One Insight (aeri-theory-model)

## When to trigger

- A theory paper's single result (a theorem, an impossibility, a sharp comparative static) needs a tight model
- An empirical paper carries a structural or conceptual model that has grown beyond what the result needs
- The model section is eating the word budget that the result and identification need
- A referee might ask "why all this machinery for one point?"

## The AER: Insights modeling discipline

AER: Insights rewards a **single, surprising, clean theoretical or modeling insight** delivered with **the smallest model that produces it**. The question is never "is the framework general?" but "**what is the most economical model whose one result is important and surprising?**" Generality, extensions, and robustness of the modeling go to the Supplemental Appendix; the main text states the assumptions, the one key result, and the intuition. A theory paper here is *short and pointed*, the opposite of a foundational framework paper for AER or a field journal.

## Two cases

### Case 1: The paper IS the theory (a theory short paper)
- **One headline result.** A single theorem, impossibility, or characterization that overturns or sharply refines a believed claim. State it early, prove it economically.
- **Minimal assumptions.** Strip to the assumptions the result actually needs; flag which are substantive vs. technical.
- **Intuition before proof.** Give the one-paragraph mechanism that makes the result memorable; full proofs to the appendix if long.
- **Surprise stated.** Name the prior intuition the result violates — that is why it is an AER: Insights paper, not a field-theory note.

### Case 2: The model SUPPORTS an empirical insight
- **Justify the model's job.** It exists to deliver one object (an identifying restriction, a counterfactual, a structural parameter the data identify). Cut anything not in service of that.
- **Minimal structure for identification.** Tie the key parameter to a data moment ([`aeri-identification`](../aeri-identification/SKILL.md) Branch C); keep solution/estimation detail in the appendix.
- **One counterfactual, if any.** If the structure delivers a counterfactual, report the single one that matters with its uncertainty; alternatives to the appendix.

## What stays in vs. goes to the appendix

| In the main text (few words) | Supplemental Appendix |
|------------------------------|------------------------|
| Setup + key assumptions | Proofs (if long), lemmas, regularity conditions |
| The one headline result + intuition | Generalizations, extensions, alternative specifications |
| The one identifying restriction / counterfactual | Robustness of the model, additional counterfactuals |

## Word budget for the model section

The model competes with identification, result, and discussion for the same **≤7,000-word (minus exhibits)**
budget ([`aeri-writing-style`](../aeri-writing-style/SKILL.md)). A useful rule: the in-text model should be
sketchable on a single page — assumptions, the one result, the intuition. If the derivation cannot be
sketched that compactly, the full version belongs in the Supplemental Appendix with only the statement and
intuition in-text. A theorem environment plus a one-paragraph proof sketch is often the right in-text
footprint for a theory short paper.

## Worked vignette (illustrative)

A fictional theory paper proves that, under a mild condition, **certification fee structure is irrelevant to
information transmission**. The AER: Insights version states the model in half a page (a sender, a certifier,
two fee regimes), states the irrelevance result, and gives the one-paragraph intuition (the certifier's
incentive constraint is unchanged by who pays). The full proof, the regularity conditions, and two
generalizations go to the Supplemental Appendix. The surprise — that a policy lever people assume matters
does not — is what makes it a single-insight AER: Insights paper rather than a general mechanism-design
framework for a field journal.

## Checklist

- [ ] The model delivers **one** headline result / object, stated early
- [ ] Assumptions stripped to what the result needs; substantive vs. technical flagged
- [ ] One-paragraph **intuition** present; long proofs/derivations to the appendix
- [ ] (Theory) the prior intuition the result violates is named
- [ ] (Empirical support) the model's single job is explicit; extras cut
- [ ] Model section does not crowd out the result and its identification within the cap

## Anti-patterns

- A general framework with the AER: Insights result as a corollary buried inside
- Extensions and generalizations kept in-text "for completeness"
- A model more elaborate than the single insight requires
- Proofs in the main text that could sit in the appendix without loss
- (Empirical) structural machinery whose only output the reduced form already gives

## Output format

```
【Case】theory-is-the-paper / model-supports-empirics
【Headline result/object】<one theorem / restriction / counterfactual>
【Minimal assumptions】<the few that matter; substantive vs technical>
【Intuition】one paragraph
【To the appendix】proofs / extensions / generalizations / robustness
【Next step】aeri-robustness
```
