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

## Active-frontier scan (hedged)

Strands with sustained presence in the journal's recent volumes — verify against the latest
issues before committing, since frontiers move:

- robust finance and model uncertainty (non-dominated superhedging, Knightian preferences);
- rough volatility: approximation theory, short-maturity asymptotics, Markovian lifts;
- mean-field games and large-population equilibria with financially meaningful constraints;
- (martingale) optimal transport methods for model-free pricing bounds;
- equilibrium and price-impact models with frictions; optimal execution theory;
- dynamic risk measures, time consistency, and capital-allocation representations;
- term-structure theory beyond classical HJM, including stochastic discontinuities and
  overnight-rate benchmarks.

A topic on a cold strand still fits if the theorem is strong; a hot strand never excuses a
routine corollary.

## Tractability stress test

```text
Q1 Can you state the conjectured theorem now, with explicit hypotheses?      no  -> not ready
Q2 Which known machinery carries 80% of the proof?                           none -> high risk
Q3 What is the genuinely new step, in one sentence?                          none -> incremental
Q4 Does a financial quantity (price, hedge, boundary, equilibrium) appear
   in the conclusion, not just the motivation?                               no  -> wrong venue
Q5 Is there a degenerate case you can solve completely first?                yes -> start there
```

## Vignette: choosing between two term-structure problems

Problem A: extend a known HJM consistency theorem from continuous to càdlàg forward curves —
statable theorem, identified obstacle (jump measures break the old compactness step), clear
payoff (benchmark-rate discontinuities at announcement dates). Problem B: simulate a new
three-factor curve model and show it fits swaption smiles. A passes Q1–Q4; B fails Q4's
theorem requirement and lands in the journal's explicit out-of-scope zone. Choose A, and scope
it by Q5: deterministic jump times first, the general case after.

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
