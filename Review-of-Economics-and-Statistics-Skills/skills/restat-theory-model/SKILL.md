---
name: restat-theory-model
description: Use when deciding how much theory or structure a The Review of Economics and Statistics (REStat) manuscript should carry — right-sizing a model so it interprets or disciplines the empirical estimate without becoming the contribution. Calibrates the theory's role; it does not develop new theory for its own sake.
---

# Theory & Model Right-Sizing (restat-theory-model)

## When to trigger

- A reduced-form result needs an economic interpretation a referee will ask for
- The draft has a sprawling model section that overshadows the empirical contribution
- You are unsure whether to estimate a structural model or stay reduced-form
- A referee asked "what is the mechanism?" or "what is the model behind this regression?"

## The REStat theory bar

REStat is **empirical-first**: theory is in service of the estimate, not the headline. The right amount of model is the amount that (1) **defines the estimand** — names the parameter the design recovers and why it is interesting; (2) **disciplines the interpretation** — maps the coefficient to an economic object (an elasticity, a welfare-relevant margin, a structural parameter); or (3) **delivers a counterfactual** the reduced form cannot. Anything more risks turning the paper into a theory or pure-structural paper that belongs elsewhere. A short, transparent model that yields a testable prediction or an interpretable parameter is worth more at REStat than an elaborate one that buries the empirics.

## Decision: how much theory?

| Situation | Theory dose | Form |
|-----------|-------------|------|
| Clean causal estimate of broad interest | Minimal | A paragraph mapping the coefficient to an economic object; estimand stated |
| Coefficient is ambiguous without a frame | Light model | A simple model giving a sign/comparative-static prediction the data test |
| Question demands a counterfactual / welfare number | Structural-light | A parsimonious model estimated/calibrated to deliver the counterfactual, validated out of sample |
| Mechanism is the contribution | Mechanism model + tests | Model that generates distinguishing predictions; test them against rival mechanisms |
| You want to publish the model itself | Wrong journal | Redirect to a theory/structural venue |

## Right-sizing moves

- **Lead with the estimand, not the equations.** State the parameter the design identifies before any model algebra.
- **Make every modeling assumption earn its place** — if removing it does not change the interpretation, cut it.
- **Tie structure to data features.** If you estimate a structural parameter, name what in the data identifies it (hand to `restat-identification` Branch on measurement/identification logic).
- **Validate, don't just calibrate.** Show fit to an untargeted moment when the model does real work.
- **Keep the counterfactual honest.** State the policy-invariance assumption a counterfactual relies on.

## Checklist

- [ ] The estimand is named and economically interpreted (elasticity / margin / structural parameter)
- [ ] Theory dose matched to the question (minimal / light / structural-light / mechanism)
- [ ] Every modeling assumption is load-bearing; non-essential ones cut
- [ ] If structural: identification of each parameter named; an untargeted moment validates fit
- [ ] If a counterfactual is run: policy-invariance / extrapolation assumptions stated
- [ ] The model does not overshadow the empirical contribution (page budget reflects priorities)

## Anti-patterns

- A 10-page model section in front of a reduced-form paper — reads as a theory paper REStat will redirect
- Equations with no estimand stated, leaving the referee to guess what is identified
- A structural model calibrated, not validated, then used for a bold counterfactual
- Theory used decoratively (a model that predicts nothing the empirics test)
- Hiding a weak design behind structural machinery

## Worked vignette: right-sizing a model to an estimate (illustrative)

A reduced-form paper finds that a transport-subsidy raised rural employment. A referee asks "what is the
welfare implication?" — the reduced form alone cannot say. The wrong response is to bolt on a full spatial
general-equilibrium model that takes over the paper. The right REStat response is a **structural-light**
addition: a parsimonious model whose one new parameter (the commuting elasticity) is **identified by the
estimated employment response itself**, validated against an untargeted moment (the change in commuting
distance), and used to deliver a single welfare number with its uncertainty. The model earns exactly its
keep — it converts the credible estimate into a welfare statement — without becoming the contribution.

## Output format

```
【Theory role】define estimand | discipline interpretation | deliver counterfactual | model mechanism
【Theory dose】minimal | light | structural-light | mechanism-model
【Estimand】[parameter] = [economic object]; identified by [data feature]
【Counterfactual assumptions】[policy-invariance / extrapolation] — or "n/a"
【Cut】assumptions/sections removed as non-load-bearing: [...]
【Next step】restat-robustness
```
