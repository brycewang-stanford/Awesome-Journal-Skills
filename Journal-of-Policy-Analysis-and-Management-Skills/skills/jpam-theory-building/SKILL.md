---
name: jpam-theory-building
description: Use when building the conceptual frame of a Journal of Policy Analysis and Management (JPAM) manuscript — the theory of change / logic model linking the policy lever to outcomes, the mechanism, and the scope conditions that govern transfer to other settings. Sharpens the argument; it does not run estimation or design identification.
---

# Theory of Change & Mechanism (jpam-theory-building)

JPAM is empirical, but the best policy papers are not atheoretical. The "theory" here is a **theory of
change**: a transparent logic that says *why* the policy lever should move the outcome, *through what
mechanism*, *for whom*, and *under what conditions it would (or would not) transfer* to another
jurisdiction or scale. This frame is what turns a single estimate into evidence a policymaker elsewhere
can use, and it disciplines the cost-benefit and heterogeneity analysis downstream.

## When to trigger

- Specifying the logic model / theory of change before or alongside the design
- A reviewer asked "what's the mechanism?" or "why would this generalize?"
- Deciding which heterogeneity and mediation analyses are theory-driven (not fishing)
- Framing scope conditions for external validity and scale-up

## Building the theory of change

1. **Lever → mechanism → outcome.** Write the causal chain explicitly: the policy changes X (incentive,
   constraint, information, price, access), which operates through mechanism M, producing outcome Y.
2. **Behavioral or institutional micro-foundation.** Say *who* responds and *why* — incentives,
   liquidity, salience, capacity, compliance, take-up. Ground it in the relevant econ / PS / PA theory.
3. **Predicted heterogeneity.** Whom should the effect be larger or smaller for? Specify *before*
   estimation so subgroup results read as tests, not data-mining.
4. **Scope conditions for transfer.** What features of this setting (administrative capacity, market
   structure, population, complementary policies) does the effect depend on? This governs external
   validity and scale-up claims.
5. **Unintended effects and general equilibrium.** Name plausible offsetting or spillover responses a
   policymaker would worry about (displacement, crowd-out, behavioral adaptation).

## What the theory buys (JPAM-specific)

- It tells policymakers in *other* jurisdictions whether the result should travel.
- It pre-commits the heterogeneity and mediation analyses, protecting them from fishing critiques.
- It specifies which costs and benefits enter the cost-benefit analysis and for whom (distribution).
- It distinguishes "the program worked here" from "this *kind* of program works through this mechanism."

## Checklist

- [ ] An explicit lever → mechanism → outcome chain written down
- [ ] A behavioral/institutional micro-foundation for who responds and why
- [ ] Predicted heterogeneity stated before estimation
- [ ] Scope conditions for transfer / scale-up named
- [ ] Plausible unintended effects, spillovers, or GE responses flagged
- [ ] Mechanism tied to specific, testable observable implications

## Anti-patterns

- A bare estimate with no mechanism — "the program raised Y" with no account of why
- Post hoc storytelling that fits whatever heterogeneity the data happened to show
- Claiming broad generalizability with no stated scope conditions
- Ignoring unintended consequences a policymaker would immediately ask about
- Borrowing a formal model that adds notation but no testable, policy-relevant implication

## Worked micro-example (illustrative)

A team evaluates a tax-credit expansion. The bare version says "the credit raised employment." The
JPAM theory-of-change version writes the chain — *credit raises the after-tax return to work
(mechanism: labor-supply incentive) → larger response for the population facing the steepest
participation tax (predicted heterogeneity: single parents near the phase-in) → effect depends on local
labor demand and on take-up via tax-filing (scope conditions)* — and flags a plausible **unintended
effect** (employers capturing part of the credit through wage adjustment). Each link is then a testable
implication the design and heterogeneity analysis must address, and the scope conditions tell a
policymaker in another state whether the result should travel. (Fields/numbers illustrative.)

## Calibration anchors (hedged)

- The "theory" JPAM wants is a **transparent logic model**, not necessarily a formal model; added
  notation must buy a testable, policy-relevant implication.
- Scope conditions are a *strength*, not a hedge: they are how a single evaluation informs decisions
  elsewhere, which is JPAM's whole purpose.
- Pre-specify heterogeneity and mechanism tests so they read as confirmatory, not as fishing.

## Output format

```
【Lever → mechanism → outcome】the causal chain in one line
【Micro-foundation】who responds and why
【Predicted heterogeneity】subgroups specified ex ante
【Scope conditions】what the effect depends on for transfer
【Unintended effects】spillovers / GE / displacement flagged
【Next】jpam-research-design
```

## Supplementary resources

- [`../../resources/exemplars/library.md`](../../resources/exemplars/library.md) — JPAM papers whose mechanism makes the result portable
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — mediation / mechanism estimation packages
