---
name: qe-contribution-framing
description: Use to sharpen the one-sentence contribution of a Quantitative Economics (QE) manuscript so a general-interest Econometric Society reader sees the quantitative payoff immediately. Frames the claim and its scope; it does not redo estimation or write full prose.
---

# Contribution Framing (qe-contribution-framing)

## When to trigger

- The "so what?" of the paper is not crisp in one sentence
- Reviewers (or co-authors) disagree about what the paper's main point actually is
- The contribution is described as a method or a dataset rather than as an answer
- The claim's scope (what it does and does not establish) is blurry

## Framing the QE contribution

QE publishes papers that **apply quantitative methods to substantive economic questions**, so the contribution should be framed as a **quantitative answer**, not as machinery. A QE-fit contribution sentence names three things: the **question**, the **quantity** you deliver (an estimate, a counterfactual, a welfare number, a measured fact), and the **lesson** that travels beyond the setting. Frame against the Econometric Society lens: if the only honest framing is "we propose a new estimator," the paper belongs at Econometrica; QE wants "using [method], we answer [question] and find [quantity], which implies [lesson]."

Match the framing to the paper type:

- **Structural/computational:** the contribution is usually a *counterfactual or welfare quantity* the model identifies, plus the credibility of the estimated parameters behind it.
- **Empirical (applied micro/finance):** the contribution is a *credibly identified magnitude* and what it teaches about the mechanism.
- **Experimental:** the contribution is a *causal quantity or parameter* the design pins down, plus its discipline on theory.
- **Simulation/measurement:** the contribution is a *newly quantified object* and the method that makes it measurable.

## Scope discipline (QE rewards calibrated claims)

State plainly what the result **does** establish (the estimand, the population, the assumptions) and what it **does not** (external validity limits, identifying assumptions that could fail, computational approximations). Because QE forbids significance asterisks and asks for standard errors and coverage sets, frame the contribution with its **uncertainty attached**, not as a point claim.

## Checklist

- [ ] One-sentence contribution names question + quantity + lesson
- [ ] The quantity (estimate / counterfactual / welfare / measured fact) is explicit and carries uncertainty
- [ ] Framed as an answer, not as "a method" or "a dataset"
- [ ] Scope stated: estimand, population, key assumptions, what is NOT claimed
- [ ] The "why QE, not Econometrica/TE" cut is visible in the framing
- [ ] No over-claiming beyond what the design/estimation supports

## Anti-patterns

- "We build a model / collect a dataset" framed as the contribution, with no answer
- A contribution sentence with no number and no scope
- Over-claiming a local estimate or a calibrated counterfactual as a universal law
- Method-first framing that really belongs at Econometrica
- Hiding identifying assumptions or computational approximations from the claim

## What a QE handling coeditor weighs in the claim

The general-interest Econometric Society readership wants the payoff, not the plumbing. Grade a candidate contribution sentence against this table.

| Framing pattern | Coeditor reading | Verdict at QE |
|-----------------|------------------|---------------|
| "We estimate [parameter] and find a welfare gain of [number]" | quantity-first, answer travels | strong fit |
| "We measure [object] previously assumed, getting [magnitude, s.e.]" | a fact the field lacked | strong fit |
| "We propose a new [estimator]" with a toy application | machinery, not an answer | Econometrica lane |

The most common desk-reject framing is the **method-as-contribution sentence**: a computational or inference device with no economic quantity attached. Re-anchor it on the number the method delivers.

## Worked vignette: a dynamic retirement model (illustrative)

A paper estimates a dynamic model of retirement timing and evaluates raising the early-claiming age. Machinery-first framing: "We solve a dynamic program with a nested fixed-point estimator." A QE-fit rewrite names question + quantity + lesson: "Raising the early eligibility age by two years cuts early claiming by 14 percentage points (s.e. 3) and raises lifetime benefits 6% on average, but the gains are regressive — a margin reduced-form work leaves unquantified." (Numbers illustrative.) The rewrite carries uncertainty, states the policy quantity, and flags the distributional lesson; the estimator becomes a credibility footnote, not the headline.

## Referee pushback and the framing fix

- *"This reads like a methods paper; where is the question?"* → Lead with the counterfactual or estimand; demote the algorithm to a credibility clause.
- *"The contribution is just a number for one sample."* → Add the scope clause: the estimand, the population it generalizes to, what it overturns.
- *"You claim more than the design supports."* → Attach the uncertainty and the explicit "does NOT establish" line.

## Output format

```
【One-sentence contribution】question + quantity + lesson
【Quantity type】estimate / counterfactual / welfare / measured fact (+ uncertainty)
【Scope — establishes】estimand / population / assumptions
【Scope — does NOT establish】[...]
【QE fit】answer-first, not method-first? [Y/N]
【Next step】qe-identification-strategy
```
