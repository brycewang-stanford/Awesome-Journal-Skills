---
name: journal-of-economic-theory
description: Use when targeting Journal of Economic Theory (JET) or deciding whether a pure economic theory manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of Economic Theory (journal-of-economic-theory)

## Journal positioning

The Journal of Economic Theory (JET) is a field-defining outlet for pure economic theory — decision theory, general equilibrium, game theory, mechanism design, and the foundations of economic reasoning. The paper that wins here proves a theorem that is correct, general, and consequential, advancing the theory itself rather than illustrating it with an application. The readership is economic theorists, so the contribution is judged on generality, novelty, and the depth of the result, not on empirical relevance.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the publisher's own site or submission system.

## When to trigger

- The author names JET (or a top theory outlet) as the target venue.
- A paper proves a general theoretical result and the author is choosing among theory venues.
- An applied-theory or modeling paper needs re-framing to make clear whether the contribution is the theory (here) or the application (elsewhere).
- The author needs JET's desk-reject risks and a credible theory / general-interest alternative list before submitting.

## Scope & topic fit

- Decision theory: choice under risk and uncertainty, ambiguity, time preference, and the axiomatic foundations of preferences.
- General equilibrium: existence, efficiency, dynamics, incomplete markets, and the structure of competitive economies.
- Game theory: solution concepts, equilibrium refinements, learning, repeated and dynamic games, and information.
- Mechanism and market design, social choice, and the theory of contracts, matching, and information economics.

## Method & evidence bar

- Theorems with complete, rigorous, correct proofs are the entire deliverable; assumptions must be stated precisely and their necessity made transparent.
- Results should be general — robust to the natural extensions a theorist would ask about — and positioned as advancing the relevant theoretical frontier.
- Examples and counterexamples are expected to delimit the result; the proof technique itself can be part of the contribution.
- No empirical or quantitative evidence is required; the bar is the importance, generality, and correctness of the theory.

## Structure & house style

- The introduction states the theoretical question, the existing gap, the main result in words, and why it matters for theory, before the formal development.
- Make the contribution explicit against the closest theoretical work; separate primitives, the main theorem, and corollaries cleanly.
- The journal uses an unstructured abstract and JEL codes; a supplementary appendix may carry long proofs and additional results while the main text stays readable.
- Notation must be standard and consistent; the logical flow from assumptions to theorem to discussion should be transparent.

## Official-submission checklist

- Search the live site for "Journal of Economic Theory guide for authors / submission guidelines" and follow the current Elsevier version, not a third-party broker's copy.
- Re-check formatting, abstract/JEL codes, reference style, and the supplementary-appendix / proof policy.
- Re-check any structured-submission requirements and the current expectations for supplementary material on the editorial system.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why a theorist should care — what the theorem establishes that was not known or general before.
- [ ] The contribution is stated as a theorem / general result / proof technique, not as an application or empirical claim.
- [ ] The introduction positions the paper against the relevant theoretical literature and frontier.
- [ ] Proofs are complete and correct; assumptions are minimal and their roles transparent; examples delimit the result.
- [ ] The result's generality and robustness to natural extensions are addressed.

## Common desk-reject triggers

- A narrow extension of a known result with no new technique and no added generality.
- Proofs that are incomplete, hand-waved, or wrong.
- An applied or empirical paper with a thin model dressed up as a theory contribution.
- A modeling exercise whose "result" is a numerical example rather than a general theorem.

## Re-routing decision

- Game theory and behavioral/experimental-adjacent theory → `games-and-economic-behavior`; econometric/identification theory → `journal-of-econometrics`.
- General-interest theory with a consequential result → `american-economic-review` or `aej-microeconomics`; finished, field-defining theory → `econometrica`.
- IO-flavored strategic theory with market application → `rand-journal-of-economics`; quantitative macro mechanism → `journal-of-monetary-economics`.
- A theory built mainly to deliver an empirical or policy point → the relevant applied/field journal (`journal-of-public-economics`, `journal-of-international-economics`).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of Economic Theory
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the theorem's generality and rigor clear this venue's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / JEL / supplementary proof appendix / formatting>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
