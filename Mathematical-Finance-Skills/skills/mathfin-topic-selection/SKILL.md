---
name: mathfin-topic-selection
description: Use when choosing or sharpening a problem for Mathematical Finance (Wiley) — tests whether the question is a methodologically novel, rigorously tractable contribution to financial modelling (stochastic analysis, pricing, risk, portfolio, microstructure) rather than a routine computational application to data.
---

# Problem Selection (mathfin-topic-selection)

## When to trigger

- Deciding whether a financial-mathematics idea is a fit for *Mathematical Finance*
- Holding a result that might be "just a numerical study" and unsure it clears the bar
- Choosing between an incremental extension and a genuinely novel modelling contribution

## The Mathematical Finance fit bar

*Mathematical Finance* evaluates submissions on **methodological novelty and contribution to
financial modelling**, presented with full mathematical rigor. The litmus test is not "is this
about finance" but "does it advance the *mathematics* of a financial-modelling problem with a
result that needs a proof." Strong topics live in the journal's stochastic-analysis tradition:

1. **New tractable models** — e.g., a jump/rough/Lévy or stochastic-volatility model with a
   provable pricing or hedging characterization.
2. **New structural results** — existence/uniqueness, FTAP-type equivalences, duality,
   verification theorems for control/BSDE problems.
3. **New methods** — a transform, free-boundary, mean-field, or stochastic-control technique
   that solves a previously open financial-modelling problem.
4. **New mathematical objects with financial meaning** — risk measures, time-consistency
   notions, arbitrage concepts with rigorous representation theorems.

## Disqualifiers (off-fit)

- **Routine computation on financial data** with no supporting rigorous analysis — explicitly
  not considered by the journal.
- A purely empirical/econometric finance result (better fit for an empirical finance journal).
- An incremental special case of a known theorem with no new technique or insight.
- A model proposed without proofs of its formal properties (the paper must be self-contained,
  proofs included).

## Sharpening questions

- What is the **theorem**, in one sentence, and why is it new?
- Is the contribution the **model**, the **method**, or the **result** — and is that the novel part?
- Could a referee from the Bachelier-Finance-Society community see the **financial-modelling**
  payoff, not just a math exercise?
- Are the assumptions general enough to matter, but precise enough to prove?

## Output format

```
【Problem】one sentence
【Type of novelty】model / method / structural result / object
【Core theorem】one sentence (what gets proved)
【Financial-modelling payoff】why it matters for pricing/risk/portfolio/microstructure
【Fit verdict】fit / off-fit + reason
【Next step】mathfin-literature-positioning
```
