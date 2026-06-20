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

## Novelty-axis evidence table

For each novelty axis the introduction must put specific evidence on the page; referees test
the claim against the theorem statements themselves:

| Novelty axis | What the introduction must show | How a referee tests it |
| --- | --- | --- |
| New tractable model | The closed-form or characterizing equation (PDE/BSDE/transform) the model admits | Re-derive the characterization from the stated dynamics |
| Weaker assumption set | The exact hypothesis removed (e.g., no dominating measure, unbounded coefficients) | Search the proof for a hidden reinstatement of the dropped condition |
| Constructive solution | The object built (optimal strategy, hedging portfolio, stopping boundary) | Check the construction is admissible and attains the value |
| Sharper rate/bound | Old rate vs. new rate, with the regime where the gain bites | Compare against known lower bounds or counterexamples |
| New representation | The dual/variational formula and the space it lives on | Verify both inequalities of the duality, not just one |
| Unifying framework | At least two prior results recovered as corollaries | Confirm the corollaries follow without extra hypotheses |

## Worked vignette: a robust superhedging paper

Hypothetical manuscript: pathwise superhedging duality for path-dependent claims under
volatility uncertainty. Applying the framing rules:

- 【Modelling problem】price and superhedge a claim when no single probabilistic model is trusted.
- 【Obstruction】classical duality needs a reference measure; under non-dominated uncertainty
  the martingale measures are mutually singular, so measurable-selection and capacity issues
  block the standard argument.
- 【Theorem as resolution】duality between the cheapest superhedge and the supremum of
  martingale expectations holds for upper semicontinuous claims, with dual attainment.
- 【Novelty axis】weaker assumption set (no dominating measure) plus a new representation.
- 【Modelling payoff】robust price bounds and an explicit hedge that works model-free.
- 【Scope of claim】upper semicontinuity is essential; the introduction says so and points to
  the counterexample section.

## Calibration against accepted introductions

Accepted *Mathematical Finance* papers typically open in one to two pages: modelling problem
and obstruction in the first paragraphs, the main theorem stated informally (or by number) by
page two, a short literature paragraph keyed to assumptions, then a roadmap. Long motivational
essays are rare; so are introductions that postpone the main result past the model setup.
When unsure of current norms, calibrate against the latest issues rather than older volumes.

## Anti-patterns

- A theorem-dump introduction with no modelling "so what."
- Claiming practical/empirical impact the paper does not establish.
- Selling generality the proofs do not support.
- Framing numerical results as the core contribution.
- Burying the actual novelty under restated background.

## Output format

```
【Modelling problem】one sentence
【Obstruction in prior work】what prevented it
【Theorem as resolution】one sentence
【Novelty axis】model / assumption / constructive / rate / representation / unification
【Modelling payoff】the financial statement the theorem licenses
【Scope of claim】where it holds / does not
【Next step】mathfin-data-analysis (if numerics) or mathfin-writing-style
```
