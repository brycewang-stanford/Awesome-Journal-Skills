---
name: joe-contribution-framing
description: Use when a Journal of Econometrics (JoE) manuscript has a correct result but fails to articulate why it matters to econometrics. Frames the methodological contribution as a general, reusable advance rather than a narrow technical fix.
---

# Contribution Framing (joe-contribution-framing)

## When to trigger

- The paper proves something true but the "so what for econometrics?" is unstated
- The abstract/intro describe *what you did* but not *what the field gains*
- The method looks like a one-off fix rather than a reusable tool
- A referee could say "correct, but why should anyone use this?"

## Why framing matters at JoE

The *Journal of Econometrics* rewards **substantive methodological contributions** — advances that change how econometricians identify, estimate, test, decide, or predict. A technically correct result that is framed as a narrow patch reads as incremental; the same result framed as a **general principle with a class of applications** reads as a contribution. Editors screen first and send only suitable papers to referees, so the framing in the abstract and introduction is part of clearing that screen. The contribution must be legible to a methodologist who does not work on your exact model.

## Framing the contribution

1. **Name the general problem class.** Not "an estimator for model M," but "a way to do valid inference whenever [condition] holds" — then show M is a leading instance.
2. **State the advance as a property, not a procedure.** Weaker assumptions, broader validity, an oracle/efficiency property, uniform size control, computational feasibility with the same guarantees.
3. **Map the reach.** Which existing methods does this improve, generalize, or correct? Where else does the same idea transfer? Reuse the lineage from `joe-literature-positioning`.
4. **Anchor in economics.** JoE prizes methods motivated by and useful for economic data — say which econometric settings (endogeneity, dependence, heterogeneity, high dimension, nonstationarity) the advance unlocks.
5. **Be honest about scope.** Over-claimed generality invites a one-citation rebuttal; a precisely-bounded contribution is more credible and more publishable.

## Calibrating to the venue

- A purely empirical payoff is **not** the contribution here; the methodological advance is. If the only novelty is an application, the paper is out of scope (see `joe-topic-selection`).
- If the contribution is a clean theorem with no application, consider adding an econometric anchor and illustration — pure statistical theory may be steered toward a statistics-oriented venue.
- If the work fits an active **Themed or Annals Issue**, frame the contribution to that theme's question (see `joe-review-process`).

## Anti-patterns

- "We propose an estimator for [narrow model]" with no statement of the general principle
- Listing technical steps as if they were the contribution
- Claiming sweeping generality the theorems do not support
- Burying the contribution under notation instead of stating it in the abstract


## Contribution pass for Journal of Econometrics

Use this as a second-pass capability check. First lock the estimand or theorem, assumptions, asymptotic/simulation evidence, and applied relevance; then test whether the manuscript addresses econometrics reviewers who expect methodological novelty, assumptions, simulation or empirical illustration, and reproducibility.

- **Primary move:** Translate the result into who learns what, which mechanism changes, and which rival explanation is ruled out; keep the claim narrower than the evidence.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Econometric Theory for proof-first work, JBES for applied statistical methods, Quantitative Economics for economics-theory methods; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Problem class】the general problem solved (not the single model)
【Advance as a property】weaker assumptions / efficiency / uniform validity / feasibility
【Reach】methods improved/generalized; where the idea transfers
【Economic anchor】settings this unlocks
【Scope honesty】what it does NOT cover
【One-sentence contribution】for the abstract
【Next step】joe-tables-figures
```
