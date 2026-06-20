---
name: jhe-theory-model
description: Use when a Journal of Health Economics (JHE) manuscript needs a model — insurance demand/selection, provider behavior under a payment rule, or a health-production/human-capital frame — to interpret estimates or run a counterfactual. Disciplines the conceptual frame; it does not establish identification (jhe-identification) or write prose.
---

# Theory and Model Craft (jhe-theory-model)

## When to trigger

- A reduced-form health-policy estimate needs a model to be interpreted as welfare, demand, or a structural parameter
- An insurance/selection paper needs the demand-and-selection model to map data to risk preferences or adverse selection
- A provider paper needs a payment-response model to predict how DRG/P4P/capitation reshapes behavior
- A counterfactual (a coverage expansion, a price change, an optimal cost-sharing rule) requires a model to extrapolate beyond the estimated variation

## How JHE uses models

At JHE a model rarely stands alone; it **earns the right to interpret an estimate or run a counterfactual**. The bar is that the model be **tight enough to discipline the data and realistic enough to match the institution**. JHE's house demand-and-selection and provider-incentive models are the lingua franca — use them rather than reinventing. The decisive questions: does the model identify the object you claim (an elasticity, a selection parameter, a welfare quantity)? Are its parameters **policy-invariant** for the counterfactual you run (the Lucas critique bites hard for coverage and payment reforms)? Does it respect institutional facts — risk adjustment, network rules, mandatory-coverage floors — that change the equilibrium?

## Model archetypes and what each must deliver

| Model type | Core object | Must show |
|------------|-------------|-----------|
| Insurance demand & selection | demand elasticity, adverse/advantageous selection | the price/cost-sharing variation that identifies the elasticity; the selection sign and where it comes from; the welfare cost of mispricing (à la cost-curve / Einav–Finkelstein logic) |
| Moral hazard | ex-ante vs. ex-post response | separation of behavioral hazard from selection; whether the utilization response is efficient or distortionary |
| Provider incentives | response to the payment rule | the provider's objective (margin, altruism, capacity); how the rule shifts intensity, coding, or patient selection; equilibrium under competition |
| Health production / human capital | health as input/output | the production function or investment problem; how a health shock maps to downstream earnings/education |
| Market / competition | hospital/insurer equilibrium | demand + supply + the regulatory constraint; how consolidation or network design moves prices/quality |

In practice most JHE papers sit in the demand-selection or provider-incentive rows; the production and market rows appear when health is the input (human capital) or when the regulated equilibrium itself is the object. Pick the row that matches your contribution and resist borrowing apparatus from another row that the data cannot support.

## Discipline checks

1. **State the object the model identifies** and tie each structural parameter to the data feature that pins it.
2. **Match the institution.** If risk adjustment, a coverage mandate, or a network constraint is present in the data, it must be in the model — a model that ignores the binding institutional rule will not survive review.
3. **Defend policy-invariance** for any counterfactual: argue the estimated parameters are not themselves functions of the policy you change.
4. **Report what the model assumes away** and whether the result is robust to relaxing it (e.g., homogeneous vs. heterogeneous risk preferences).
5. **Keep the model proportionate.** A reduced-form paper needs only enough theory to interpret the sign and magnitude; do not bolt on a structural model the data cannot identify.

## Checklist

- [ ] The object the model identifies is named (elasticity / selection parameter / welfare quantity)
- [ ] Each structural parameter is tied to the identifying data feature
- [ ] Binding institutional rules (risk adjustment, mandates, networks) are in the model, not assumed away
- [ ] Policy-invariance defended for every counterfactual
- [ ] Welfare claims rest on the model, not on a reduced-form coefficient alone
- [ ] What the model assumes away is stated and stress-tested
- [ ] Model complexity is proportionate to what the data can identify
- [ ] The chosen model archetype matches the contribution, not borrowed from another subfield

## Anti-patterns

- A model whose equilibrium ignores a binding institutional rule the data clearly reflects
- A structural model whose parameters the data cannot actually identify ("calibration in disguise")
- Reading a reduced-form coefficient as welfare with no model linking them
- A demand/selection model that ignores risk adjustment or the mandate that shapes the real market
- Running a counterfactual that changes a policy the parameters secretly depend on
- A heavy structural apparatus where a one-equation interpretive frame would do
- Borrowing a model from another health-econ subfield without checking the data can identify it

## Referee pushback mapped to the model fix

- *"Your utilization effect is not a welfare statement."* → Add the demand-and-cost frame that splits the value of risk protection from the deadweight cost of moral hazard; report the net welfare quantity.
- *"What in the data identifies this structural parameter?"* → Tie each parameter to the variation that pins it (a cost-sharing kink, a coverage discontinuity) and show moment sensitivity.
- *"Your counterfactual changes a policy your parameters depend on."* → Argue policy-invariance explicitly (Lucas critique); show the parameters are primitives, not reduced-form responses to the policy.
- *"The model ignores risk adjustment / the mandate that defines this market."* → Put the binding institutional rule into the model; re-derive the equilibrium under it.

## Worked vignette (illustrative)

A coverage-expansion paper reports a 4pp rise in utilization and calls it a welfare gain. A referee objects: utilization up is not welfare up — some is efficient moral hazard, some is the value of risk protection, some is wasteful. The JHE fix: add an Einav–Finkelstein-style demand-and-cost frame that separates the value of insurance (risk protection) from the deadweight cost of ex-post moral hazard, identify the demand elasticity off the cost-sharing variation already in the design, and report the net welfare quantity with its sensitivity to the risk-aversion parameter. The "welfare gain" claim now rests on a model, not a utilization coefficient.

## How much model does the paper need?

Match the theoretical apparatus to the claim, not to fashion. A reduced-form policy-evaluation paper usually needs only a **one-equation interpretive frame** — enough to sign the effect and say what welfare quantity it does (and does not) capture. A paper whose contribution *is* a structural object (a demand elasticity, a selection parameter, an optimal cost-sharing rule) needs the full model, and then the burden is identification: the data must actually pin the parameters. The mismatch JHE punishes is a heavy structural model bolted onto data that cannot identify it, or a welfare claim with no model at all. Decide which paper you are writing before adding equations.

## Output format

```text
【Journal】Journal of Health Economics
【Skill】jhe-theory-model
【Model type】demand-selection / moral-hazard / provider-incentive / health-production / market
【Object identified】elasticity / selection parameter / welfare quantity
【Parameter → data feature】[each parameter tied to what identifies it]
【Institutional fidelity】binding rules in the model? [Y/N]
【Counterfactual validity】policy-invariance defended? [Y/N]
【Next skill】jhe-robustness
```

## Handoff boundary

This skill disciplines the conceptual frame that interprets an estimate; it does not establish what identifies the parameters (`jhe-identification`) or stress-test the result (`jhe-robustness`). For a structural paper, identification and the model are tightly coupled — iterate with `jhe-identification` until each parameter is tied to a data feature. When the model earns its interpretation and any counterfactual is policy-invariant, hand off to `jhe-robustness`.
