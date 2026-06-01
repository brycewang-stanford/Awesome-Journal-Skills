---
name: mathfin-contribution-framing
description: Use when articulating the contribution of a Mathematical Finance (Wiley) manuscript — frame the methodological novelty and its payoff for financial modelling (pricing, hedging, risk, portfolio, microstructure) so editor and referees see why the theorem matters, not just that it is true.
---

# Contribution Framing (mathfin-contribution-framing)

## When to trigger

- The math is correct but the introduction does not say why it advances financial modelling
- A referee might ask "this is rigorous, but what is the new modelling insight?"
- Reviewing whether the stated contribution matches what the theorems actually deliver

## The Mathematical Finance contribution bar

The journal evaluates papers on **methodological novelty and contribution to financial
modelling**. Rigor is necessary but not sufficient: a correct theorem with no modelling payoff
reads as a math paper sent to the wrong venue, while a modelling claim without proof reads as
informal finance. The contribution must be **both** mathematically novel **and** consequential
for a financial-modelling problem (pricing, hedging, risk measurement, portfolio choice,
optimal execution, arbitrage theory).

## How to frame the contribution

1. **Lead with the modelling problem**, then the obstruction prior methods hit, then your
   theorem as the resolution.
2. **Name the novelty axis** explicitly: a new tractable model, a weaker assumption set, a
   constructive solution where only existence was known, a sharper rate/bound, a new
   representation (e.g., of a risk measure), or a unifying framework.
3. **Translate the theorem into a modelling statement**: "hence the option price solves...",
   "hence the optimal strategy is...", "hence the risk measure admits the representation..."
4. **Bound the claim to the hypotheses** — state where the result holds and where it does not,
   consistent with the rigor culture (over-claiming is penalized).
5. **Place numerics in service of the claim**: if you include experiments, frame them as
   illustrating the theorem (convergence, qualitative behavior), never as the contribution
   itself — routine computation on data is out of scope.

## Anti-patterns

- A theorem-dump introduction with no modelling "so what."
- Claiming practical/empirical impact the paper does not establish.
- Selling generality the proofs do not support.
- Framing numerical results as the core contribution.
- Burying the actual novelty under restated background.

## Output format

```
【Modelling problem】one sentence
【Obstruction in prior work】what blocked it
【Theorem as resolution】one sentence
【Novelty axis】model / assumption / constructive / rate / representation / unification
【Modelling payoff】the financial statement the theorem licenses
【Scope of claim】where it holds / does not
【Next step】mathfin-data-analysis (if numerics) or mathfin-writing-style
```
