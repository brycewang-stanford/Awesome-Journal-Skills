---
name: tar-theory-development
description: Use when the economic mechanism, analytical model, or predictions are the bottleneck for a The Accounting Review (TAR) manuscript — articulating why an accounting effect occurs and deriving testable predictions or model propositions. Builds the argument; it does not design identification (tar-methods) or run the estimation (tar-data-analysis).
---

# Mechanism & Model Development (tar-theory-development)

## When to trigger

- Predictions read as bald associations ("disclosure X relates to outcome Y") with no economic logic
- You have archival results and are tempted to write predictions around them (HARKing risk)
- An analytical paper needs a clean model, equilibrium, and comparative statics
- Mediating channels (information asymmetry, agency costs, real effects) are claimed but not modeled
- A reviewer says "the prediction is mechanical," "what is the friction?", or "why would this hold?"

## The TAR theory bar

TAR is open to all methods, but it does not publish atheoretical regressions. Whether the paper is
archival, experimental, or analytical, every prediction must rest on an **explicit economic
mechanism** — typically an information friction (asymmetric information, adverse selection, moral
hazard), an agency conflict, a contracting or monitoring force, a processing/attention constraint,
or a real-decision channel through which accounting information changes behavior. Name the friction
and the channel verb (reduces information asymmetry, tightens monitoring, relaxes a covenant,
disciplines investment, deters tax aggressiveness).

## The three theory lanes at TAR

- **Archival/empirical:** derive directional predictions from accounting and information economics
  (disclosure theory, earnings-management incentives, audit-quality demand, conservatism,
  tax-avoidance trade-offs). Predictions are written *before* estimation; the data test them.
- **Analytical/modeling:** state primitives (players, information structure, payoffs), solve for
  equilibrium, and present **propositions with proofs** and **comparative statics** that yield
  testable or normative implications for accounting (optimal disclosure, signaling, the demand for
  conservatism, audit effort, performance measurement). Keep assumptions minimal and defend each.
- **Experimental/behavioral:** ground hypotheses in psychology and accounting theory (judgment,
  motivated reasoning, professional skepticism, investor processing) where archival data cannot
  isolate the mechanism; the experiment manipulates the construct to establish the channel directly.

## Building a prediction (the mechanism chain)

1. **Setting & construct** — the accounting object (disclosure, accrual, audit, tax position) and
   the institutional setting that makes it bite.
2. **Friction** — the information or agency friction the accounting acts on.
3. **Channel** — the economic process linking the construct to the outcome (pricing, contracting,
   real investment, litigation, reputation, regulatory enforcement).
4. **Direction & form** — sign, and whether monotone, non-monotone, or conditional.
5. **Cross-section / boundary** — where the effect strengthens or reverses, and *why* economically.

## For analytical papers specifically

- Make the **information structure** explicit (who knows what, when).
- Prove propositions; do not assert equilibrium properties.
- Translate comparative statics into empirical predictions or policy implications an accounting
  reader cares about; a model with no accounting payoff is a math paper.

## Checklist

- [ ] Every prediction rests on a named friction and channel, not a mechanical correlation
- [ ] The relevant accounting/information-economics theory is invoked through its logic, not a citation
- [ ] Archival predictions were fixed before estimation (no HARKing)
- [ ] Analytical claims are stated as proven propositions with comparative statics
- [ ] Cross-sectional/boundary predictions have an economic reason
- [ ] At least one alternative explanation is named and will be tested or modeled out

## Anti-patterns

- **HARKing**: writing predictions to match the regression output after the fact.
- **Mechanical predictions**: a sign that follows from accounting identities, not economics.
- **Borrowed friction**: invoking "information asymmetry" with no account of how it operates here.
- **Model without payoff**: an elegant equilibrium with no accounting implication.
- **Channel by proxy**: asserting a real-effects channel the design cannot distinguish from pricing.

## Output format

```
【Lane】archival / analytical / experimental
【Friction】information asymmetry / agency / attention / contracting ...
【Prediction P1 (focal)】construct → channel → outcome; direction/form
【Prediction P2 (channel/mediation)】...
【P3+ (cross-section/boundary)】... economic reason
【Analytical only】propositions proven? comparative statics stated? yes/no
【Rival explanation】named + how it will be ruled out
【Next step】tar-literature-positioning, then tar-methods
```
