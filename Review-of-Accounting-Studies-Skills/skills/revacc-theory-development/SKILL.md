---
name: revacc-theory-development
description: Use when the economic mechanism, analytical model, or testable predictions are the bottleneck for a Review of Accounting Studies (RAST) manuscript — articulating the friction behind an accounting effect or building a parsimonious disclosure/contracting model with proven propositions. Builds the argument; it does not design identification (revacc-methods) or run estimation (revacc-data-analysis).
---

# Theory & Model Development (revacc-theory-development)

## When to trigger

- Predictions read as bald associations ("disclosure X relates to outcome Y") with no friction
- You have archival results and are tempted to write predictions around them (HARKing risk)
- An analytical paper needs a clean information structure, equilibrium, and comparative statics
- A claimed channel (information asymmetry, agency, real effects) is asserted but not modeled
- A referee says "what is the friction?", "the model is not minimal", or "the comparative static has no accounting reading"

## RAST is a genuine home for analytical accounting

Unlike outlets where modeling is marginal, RAST runs a real **analytical lane** alongside archival and experimental work. That raises two distinct bars depending on the lane, and the most common failure is mixing them up.

- **Analytical / modeling.** State primitives — players, **information structure** (who knows what, when), payoffs — then solve for equilibrium and present **propositions with proofs** and **comparative statics**. The RAST-specific demand: the model must be the **minimal structure** that delivers an *accounting* implication (optimal disclosure granularity, the demand for conservatism, signaling through reporting choices, audit-effort incentives, performance-measure design, the real effects of mandatory reporting). An elegant equilibrium with no accounting payoff is a math paper RAST will reject.
- **Empirical archival.** Derive directional predictions from accounting and information economics *before* estimation. Name the friction the accounting acts on and the channel verb (reduces information asymmetry, tightens monitoring, relaxes a covenant, disciplines investment, deters tax aggressiveness).
- **Experimental / behavioral.** Ground hypotheses in psychology plus accounting theory (judgment, motivated reasoning, professional skepticism, investor processing) where archival data cannot isolate the mechanism; the experiment manipulates the construct to establish the channel directly.

## The mechanism chain (archival/experimental)

1. **Setting & construct** — the accounting object (disclosure, accrual, audit, tax position) and the institutional setting that makes it bite.
2. **Friction** — the information or agency friction (asymmetric information, adverse selection, moral hazard, contracting/monitoring force, attention constraint).
3. **Channel** — the economic process linking construct to outcome (pricing, contracting, real investment, litigation, reputation, enforcement).
4. **Direction & form** — sign; monotone, non-monotone, or conditional.
5. **Cross-section / boundary** — where the effect strengthens or reverses, and *why* economically.

## Building the analytical model (RAST-style)

- Make the **information structure explicit** and defend each assumption as load-bearing — referees probe whether a simpler model gives the same result.
- **Prove** propositions; never assert equilibrium properties. Put proofs in an appendix, intuition in the text.
- Translate comparative statics into **empirical predictions or policy implications** an accounting reader cares about; pair the model with a stylized empirical illustration where feasible — RAST values theory that speaks to data.
- Name the closest existing disclosure/agency model and state the **marginal modeling move** (a new friction, a relaxed assumption, an added stage).

## Checklist

- [ ] Every prediction rests on a named friction and channel, not a mechanical correlation
- [ ] Archival predictions were fixed before estimation (no HARKing)
- [ ] Analytical claims are stated as **proven propositions** with comparative statics
- [ ] The model is defended as the minimal structure for the result
- [ ] Each comparative static has an explicit **accounting** reading (not just an economics one)
- [ ] At least one rival explanation is named and will be tested or modeled out
- [ ] The marginal move over the nearest prior model/theory is stated

## Anti-patterns

- **HARKing:** writing predictions to match regression output after the fact.
- **Model without payoff:** a clean equilibrium whose comparative statics carry no accounting implication.
- **Non-minimal model:** assumptions a referee can strip without changing the result.
- **Borrowed friction:** invoking "information asymmetry" with no account of how it operates here.
- **Mechanical prediction:** a sign that follows from accounting identities rather than economics.
- **Channel by proxy:** asserting a real-effects channel the design cannot separate from pricing.

## Output format

```text
【Lane】archival / analytical / experimental
【Friction】information asymmetry / agency / contracting / attention ...
【Analytical only】primitives + information structure stated? propositions proven? minimal? yes/no
【Prediction P1 (focal)】construct → channel → outcome; direction/form
【Prediction P2 (channel/mediation)】...
【P3+ (cross-section/boundary)】... economic reason
【Accounting payoff】the implication a reporting reader cares about
【Rival explanation】named + how it will be ruled out
【Next skill】revacc-literature-positioning, then revacc-methods
```
