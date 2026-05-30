---
name: mathematical-finance
description: Use when targeting Mathematical Finance or deciding whether a quantitative / mathematical-finance manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Mathematical Finance (mathematical-finance)

## Journal positioning

Mathematical Finance is a leading journal at the interface of mathematics and finance, publishing rigorous theory: stochastic processes, derivatives pricing, optimal control and portfolio choice, risk measures, and the probabilistic and analytic foundations of financial models. The contribution is mathematical — new models, theorems, or methods with proofs — addressed to readers comfortable with measure-theoretic probability and stochastic analysis. It is not an empirical finance journal; the standard of acceptance is mathematical rigor and financial relevance, not statistical significance.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Mathematical Finance / Wiley site and the editorial submission system.

## When to trigger

- The author names Mathematical Finance (or math-finance / quantitative-finance theory venues) as the target.
- A paper proves new results about pricing, hedging, optimal control, or risk under a stochastic model.
- A quantitative paper has a genuine mathematical contribution that an empirical finance journal would not referee properly.
- The author needs Mathematical Finance's desk-reject risks and a credible math-finance / finance-theory alternative list.

## Scope & topic fit

- Continuous-time finance: arbitrage theory, martingale methods, fundamental theorems of asset pricing, and incomplete markets.
- Derivatives pricing and hedging, stochastic volatility, jump models, and numerical/analytic pricing methods.
- Optimal control, dynamic portfolio choice, utility maximization, and stochastic optimization in finance.
- Risk measures, model uncertainty/robust finance, systemic risk, and the mathematics of market microstructure or high-frequency limits.

## Method & evidence bar

- Theorems with complete, correct proofs: assumptions stated precisely, results general or sharp, and the mathematics self-contained.
- A clear financial motivation and interpretation — pure mathematics with no financial payoff is out of scope, as is finance with no genuine mathematical advance.
- Numerical methods must be analyzed (convergence, stability, error bounds), not merely demonstrated.
- Novelty relative to the existing stochastic-analysis and math-finance literature must be explicit.

## Structure & house style

- The introduction states the financial problem, the mathematical contribution, and the relation to prior theory, with the main theorem(s) previewed early.
- Notation, assumptions, and definitions are precise; proofs are rigorous and may be deferred to an appendix.
- Mathematical Finance uses an abstract suited to a mathematical audience; results are stated as numbered theorems/propositions with proofs.
- Any empirical or numerical illustration supports the theory rather than carrying the contribution.

## Official-submission checklist

- Search the live site for "Mathematical Finance author guidelines" and follow the current Wiley version.
- Re-check formatting (LaTeX class, theorem environments, reference style), abstract and MSC/JEL classification, and anonymization expectations.
- Re-check any code/data or supplementary-material requirements for numerical results.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the mathematical contribution and its financial relevance.
- [ ] The contribution is stated as a new theorem / model / method with proofs, not as an empirical finding.
- [ ] Assumptions are precise and the results are positioned against the prior math-finance literature.
- [ ] Proofs are complete and correct; numerical methods are analyzed, not just shown.
- [ ] Formatting, classification codes, and any supplementary material match the current official guide.

## Common desk-reject triggers

- An empirical finance paper with no mathematical contribution.
- Pure mathematics with no financial motivation or interpretation.
- Incomplete or incorrect proofs, or vague assumptions.
- A numerical-methods paper with no convergence/error analysis, or results already standard in the literature.

## Re-routing decision

- Theory with empirical asset-pricing payoff for a general finance audience → `journal-of-financial-economics`, `review-of-financial-studies`, `journal-of-finance`.
- Econometrics of finance, volatility, and predictability (empirical) → `journal-of-empirical-finance`.
- Quantitatively careful empirical finance → `journal-of-financial-and-quantitative-analysis`; microstructure empirics → `journal-of-financial-markets`.
- Pure probability/stochastic-analysis with no finance core → a probability or applied-mathematics journal (outside this finance bundle).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Mathematical Finance
[Topic tags] <2–3 closest topics>
[Method/evidence] <is there a rigorous, financially relevant mathematical contribution with proofs?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / LaTeX / classification / supplementary material>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
