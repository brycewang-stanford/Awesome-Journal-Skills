---
name: aejpol-theory-model
description: Use when an AEJ: Economic Policy manuscript needs a framework that maps reduced-form estimates into a welfare, cost-benefit, or distributional policy object — sufficient statistics, MVPF, optimal-policy, or a small applied model. Builds the estimate-to-welfare bridge and states its assumptions; it does not run the empirical estimation or write the prose.
---

# Theory / Welfare Model — Estimate-to-Policy Bridge (aejpol-theory-model)

## When to trigger

- You have a credible causal estimate but no framework to say what it means for welfare or policy
- A referee says the welfare claim is "hand-waved" or the "so what" is missing
- You need to convert an elasticity / treatment effect into a cost-benefit or optimal-policy statement
- A reviewer asks "what is the sufficient statistic, and does your estimate identify it?"

## The AEJ: Policy role of theory

At AEJ: Policy theory is usually **in service of the policy reading**, not the headline. Most papers do not need a full structural model; they need a transparent framework that turns a reduced-form estimate into a **welfare, cost-benefit, or distributional** object a policymaker can use. Pick the lightest framework that delivers the policy statement and make its assumptions explicit.

### Bridge paths (lightest first)

#### Path A: Sufficient statistics / MVPF
- Write the welfare expression and show **which estimated objects are the sufficient statistics** (e.g., an elasticity, a fiscal externality, a pass-through). State that your design identifies exactly those.
- For spending/tax policies, a **Marginal Value of Public Funds** (benefit to recipients per dollar of net government cost) is the canonical AEJ: Policy summary — define the numerator and denominator and which estimates feed each.
- State the assumptions the sufficient-statistic formula buys you (envelope conditions, no income effects, partial-equilibrium scope) and where they could fail.

#### Path B: Cost-benefit / fiscal accounting
- Build the explicit ledger: program cost, behavioral-response fiscal effects, benefits to recipients, externalities. Show the **net cost per unit of outcome** (cost per job, per ton abated, per QALY-equivalent, per child lifted) with uncertainty propagated from the estimate's SE.
- Distinguish mechanical from behavioral effects; the behavioral term is what your causal estimate supplies.

#### Path C: Optimal-policy / re-optimization
- Use the estimated elasticity in a standard optimal-tax / optimal-transfer formula to back out the policy-relevant optimum, then compare to the status quo. Frame as "the policy-relevant elasticity implies the current level is too high/low."

#### Path D: Small calibrated / structural model
- Only when reduced-form + sufficient statistics cannot deliver the counterfactual (general-equilibrium feedback, extrapolation beyond observed variation). Tie parameters to data, validate against untargeted moments, and argue policy-invariance for the counterfactual (Lucas critique).

### Distributional reading
Whatever the path, ask **who gains and who pays**. An incidence split across income, region, or demographic groups is often the AEJ: Policy contribution and is cheap to add once the estimate exists.

## Checklist

- [ ] The welfare/policy object is named (MVPF, net cost-per-outcome, optimum, incidence)
- [ ] The sufficient statistic(s) are identified by the empirical design, not assumed
- [ ] The framework's assumptions are stated and their failure modes flagged
- [ ] Uncertainty from the estimate is propagated into the welfare number
- [ ] A distributional / incidence reading is provided where the policy has clear winners and losers
- [ ] The model is no heavier than the policy statement requires

## Anti-patterns

- A welfare claim with no formula linking it to the estimate ("this is welfare-improving" asserted)
- Importing a sufficient-statistic formula whose assumptions your setting violates
- A full structural model where a one-line MVPF would have sufficed (overengineering)
- Reporting a point welfare number with no uncertainty band
- Ignoring incidence when the policy obviously redistributes

## Worked vignette (illustrative)

A clean RDD shows a benefit-eligibility threshold raises take-up and reduces hardship. Alone it is "the program helps." Bridged: the take-up and hardship estimates are the sufficient statistics for an **MVPF** — recipients value the transfer at, say, $1.20 per $1 of net government cost after behavioral offsets (illustrative) — and the incidence falls mostly on the lowest-income tercile. Now the paper states whether the program is a good use of public funds and for whom.

## Output format

```
【Policy object】MVPF / net cost-per-outcome / optimum / incidence
【Framework】sufficient statistics / cost-benefit ledger / optimal-policy / small model
【Sufficient statistic(s)】which estimates feed the welfare expression
【Key assumptions + failure modes】[...]
【Uncertainty】how the estimate's SE propagates to the welfare number
【Distributional reading】who gains / who pays
【Next step】aejpol-robustness then aejpol-writing-style
```
