---
name: psychrev-contribution-framing
description: Use when articulating the theoretical advance of a Psychological Review manuscript — what the field can explain after the paper that it could not before, stated against the specific prior models it improves on. Frames the contribution; it does NOT build the model (psychrev-theory-construction) or position it in the literature (psychrev-literature-positioning).
---

# Contribution Framing (psychrev-contribution-framing)

## When to trigger

- The theory is built, derived, and bounded; now you must say why it matters
- You can describe what your model *is* but not what is *new* about it
- A reviewer will ask "how is this an advance over [the standing model]?"
- The contribution reads as "we propose a model of X" with no before → after

## The two questions every Review reviewer asks

1. **What can the field explain after this paper that it could not before?** Stated as a
   concrete *before → after* against a **named** prior model — not against "the literature."
2. **Why could the prior models not get there?** Identify the specific commitment or omission
   in the rival that your theory replaces or adds. "More accurate fit" is rarely enough; the
   advance should be a *mechanism* or *unification*, not a better-tuned curve.

## Sizing the contribution (be honest about which you have)

| Contribution type        | What it claims                                          | Strength at Review |
|--------------------------|--------------------------------------------------------|--------------------|
| New mechanism            | A previously unexplained phenomenon now follows from a stated process | Strong |
| Unification              | Phenomena treated by separate theories follow from one model | Strong |
| Adjudication             | Settles a standing dispute between rival theories       | Strong |
| Formalization            | Makes a verbal theory precise and thereby newly predictive | Strong if it yields novel predictions |
| Generalization           | Extends a model to a new domain it could not reach      | Moderate — must be non-trivial |
| Re-parameterization      | Same model, better fit                                  | Weak — usually not a Review contribution |
| Relabeling               | New name for an existing construct/mechanism            | None — desk-reject signal |

## Differentiation discipline

- State the contribution as **"before this paper, theory could not X; after it, theory can X,"**
  naming the prior model displaced or extended.
- Show the advance is **not** (a) a relabel, (b) a mere better fit, or (c) an accommodation of
  data the model was built on — each is a known reviewer objection at this journal.
- Tie the contribution to the **diagnostic phenomena** and **novel predictions** from
  `psychrev-argument-development`: the advance is credible only if the model gets the diagnostic
  cases right and risks a falsifiable new one.
- Where you formalize a verbal theory, the contribution is the **new predictions** the
  formalization yields, not the formalization itself.

## Generality, the journal's premium

Review pays for **generality**. The strongest contribution framing shows the mechanism reaches
beyond the originating paradigm — "the same mechanism predicts patterns in [adjacent domain]."
Claim only the generality the derivations support (per `psychrev-boundary-conditions`); overclaimed
generality is as damaging as undersized contribution.

## Checklist

- [ ] Contribution stated as before → after against a *named* prior model
- [ ] The specific commitment/omission in the rival that the theory replaces is identified
- [ ] Contribution type is honestly sized (mechanism/unification/adjudication, not relabel/refit)
- [ ] Shown not to be a relabel, a better fit, or an accommodation
- [ ] Advance tied to diagnostic phenomena and at least one novel falsifiable prediction
- [ ] Generality claimed only to the extent the derivations and scope support

## Anti-patterns

- "We propose a model of X" with no before → after and no named rival
- Claiming an advance that is a better fit of the same mechanism
- Relabeling an existing construct and presenting it as new theory
- Differentiating from "the literature" instead of a specific model
- Overclaiming generality the scope analysis does not support
- Letting the contribution rest on accommodated data rather than novel prediction

## Output format

```
【Before → after】before this paper, theory could not [...]; after it, theory can [...]
【Named rival displaced/extended】[model] — the commitment/omission replaced: [...]
【Contribution type】mechanism | unification | adjudication | formalization | generalization
【Not a relabel/refit】evidence: tied to diagnostic phenomena + novel prediction [...]
【Generality】[reach beyond originating paradigm, within stated scope]
【Next step】psychrev-review-process (understand masked review) → psychrev-submission
```
