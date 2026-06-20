---
name: jbes-contribution-framing
description: Use when sharpening the core methodological contribution of a Journal of Business & Economic Statistics (JBES) paper into one legible claim that pairs novelty with empirical relevance. Frames the contribution; it does not develop the theory or run the analysis.
---

# Contribution Framing (jbes-contribution-framing)

## When to trigger

- The paper has results but the "what is the contribution?" answer is muddy
- Reviewers/co-authors disagree on whether the paper is a method paper, an application, or both
- The introduction lists many small points instead of one organizing contribution
- You need a one-sentence pitch the handling Co-Editor can grasp on a first read

## The JBES contribution shape: novelty × relevance

A JBES contribution is not "we found an empirical result" and not "we proved a theorem." It is a **method-level claim with an empirical consequence**: *we develop/improve method M so that practitioners can now do D in setting S, which prior methods could not.* Because JBES sits between modern data science and classical econometrics, the framing must make the **methodological delta** explicit (what is new about M) **and** the **empirical relevance** explicit (why D in S matters). A contribution naming only one of these reads as off-scope for a methods-with-empirics journal.

## Framing protocol

1. **Write the one-sentence claim.** Template: "We propose [method], which [methodological advance — relaxes/extends/accelerates], enabling [empirical task] in [setting], where [prior approach] fails or is infeasible."
2. **Name the deliverables.** Most JBES papers offer a bundle: a method, its theoretical guarantees (consistency / asymptotic distribution / rates / validity), Monte Carlo evidence, and a substantive application. State which you deliver.
3. **Right-size the claim.** Match the breadth of the claim to the proof and the simulations. "Generally valid" requires general conditions; if you only show it under specific assumptions, scope the claim to them.
4. **Tie novelty to relevance in the same breath.** Avoid a method section that never connects to the application and an application that never uses the method's novelty.
5. **Front-load it.** The contribution belongs in the abstract and the first page, stated plainly, before the machinery.

## Checklist

- [ ] A single one-sentence contribution exists (method advance + empirical consequence)
- [ ] The methodological delta is concrete (what is new vs. what existed)
- [ ] The empirical relevance is concrete (what practitioners can now do)
- [ ] Theoretical deliverables named (consistency / distribution / rates / size-power validity)
- [ ] Monte Carlo and the application are listed as part of the contribution
- [ ] The claim's breadth matches what is actually proved and simulated
- [ ] The contribution appears in the abstract and on page one

## Anti-patterns

- A contribution stated only as an empirical finding (off-scope: no method)
- A contribution stated only as a theorem (off-scope: no empirical relevance)
- A laundry list of minor points with no organizing claim
- Over-claiming generality the assumptions/proofs do not support
- Burying the contribution after pages of setup

## Worked vignette: framing a synthetic-control inference contribution

A hypothetical JBES paper builds a conformal prediction interval for synthetic-control counterfactuals and applies it to a state minimum-wage change (figures **illustrative**). A muddy draft framed it twice over — as a finding ("the policy raised employment") and as a theorem ("our interval is finite-sample valid"). Neither is a JBES contribution alone. The legible claim pairs them: a conformal interval valid with one treated unit and few pre-periods, enabling honest policy-evaluation bands where the placebo distribution is too coarse. The deliverables then line up: method, theory (coverage under stated exchangeability), Monte Carlo (an illustrative 94.6% near nominal 95%), and the minimum-wage application. The claim is right-sized to the exchangeability condition the proof uses, not "generally valid."

## Referee-pushback patterns on the contribution (venue-specific fixes)

| JBES referee reaction | Fix this skill enforces |
|----|----|
| "Where is the method?" | Lead with the methodological delta; name what is new versus prior estimators |
| "Why JBES not a statistics theory journal?" | Attach the empirical task the method now enables in micro/macro/finance |
| "You claim generality the proof does not deliver." | Scope the claim to the conditions actually proved and simulated |

Calibration anchor (hedged): a JBES contribution is the **method-plus-application arc**, not either pole
— theory-and-methods-style work still owes a substantive application and applications-and-case-studies
work still owes a methodological increment. Confirm any current ASA/T&F section taxonomy against the
live author guidelines.

## Output format

```
【One-sentence contribution】method advance + empirical consequence: ...
【Methodological delta】new vs. prior: ...
【Empirical relevance】what practitioners can now do: ...
【Deliverables】theory / Monte Carlo / application present? [Y/N each]
【Claim right-sized?】matches proofs + simulations? [Y/N]
【Front-loaded?】in abstract + page one? [Y/N]
【Next step】jbes-identification-strategy
```
