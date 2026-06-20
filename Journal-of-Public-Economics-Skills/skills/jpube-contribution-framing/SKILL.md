---
name: jpube-contribution-framing
description: Use when the contribution of a Journal of Public Economics (JPubE) manuscript needs sharpening — what the paper teaches about the economic role of government, why it matters for policy, and how it advances public-finance theory or evidence. Frames the contribution; it does not survey the literature (use jpube-literature-positioning) or run analysis.
---

# Contribution Framing (jpube-contribution-framing)

## When to trigger

- The intro lists results but never states the contribution in one sentence
- Reviewers might ask "what do we now know about government policy that we didn't?"
- The paper has a clean estimate but no welfare / policy payoff
- You are deciding whether the contribution is empirical, theoretical, or both

## What "contribution" means at JPubE

JPubE judges a paper by what it adds to our understanding of the **economic role of government** — the legacy of Atkinson's founding mandate and the standard the Hendren–Kopczuk editorial team applies. A coefficient is not a contribution; a **policy-relevant parameter, mechanism, or welfare conclusion** is. The strongest JPubE contributions take one of these shapes:

1. **A first-order policy elasticity** estimated credibly (e.g., the taxable-income or labor-supply elasticity, a take-up or moral-hazard parameter) that disciplines optimal-policy or welfare analysis.
2. **A welfare verdict** via a transparent framework — deadweight loss, the Marginal Value of Public Funds (MVPF), or a **sufficient-statistics** mapping from estimated behavioral responses to welfare, holding stated primitives fixed.
3. **A mechanism** that resolves an equity-efficiency trade-off or overturns a received result about a tax, transfer, or public-good policy.
4. **A theoretical advance** in optimal taxation, social insurance, or public-goods provision, ideally connected to measurable quantities.

## Framing moves

- **State the parameter and its policy use.** "We estimate X; X is the sufficient statistic for Y policy question" beats "we find a significant effect."
- **Name the counterfactual policy.** Public economics is normative-adjacent: tie the estimate to a reform, an optimal rate, or a program-design choice.
- **Quantify the stakes.** Translate effects into revenue, welfare, MVPF, or distributional terms an international policy audience recognizes.
- **Be honest about scope.** A LATE from one country's reform is a contribution if its lesson transports; say what it does and does not identify.

## Checklist

- [ ] Contribution stated in one sentence tied to a policy lever
- [ ] The estimated object is mapped to welfare / optimal policy (DWL / MVPF / sufficient stat)
- [ ] The counterfactual reform or design choice is named
- [ ] Stakes quantified in revenue / welfare / distributional units
- [ ] Scope and external validity stated honestly for an international readership

## Anti-patterns

- "We find a statistically significant effect of [policy]" with no welfare payoff
- Claiming an optimal-policy conclusion the design cannot support
- Burying the contribution under a literature recap (that is positioning, not framing)
- Framing a public-finance paper as if novelty of data alone were the contribution

## What the JPubE referee weighs (decision table)

A public-finance referee scores a framing on whether the estimated object earns a normative reading.

| Framing as written | Referee reads it as | Upgrade move |
|--------------------|---------------------|--------------|
| "Significant effect of the reform on earnings" | A reduced-form fact | Name the sufficient statistic the earnings response identifies |
| "Elasticity of taxable income is 0.3" | A parameter, but for what? | Feed it into a Saez optimal-top-rate or DWL statement |
| "Take-up rose by 8 points" | Descriptive program fact | Convert to an MVPF numerator/denominator term |

Desk-reject framing tells: a coefficient with no policy lever; a welfare claim asserted, not derived; a government-role angle bolted onto a labor/IO core.

## Worked vignette: a bunching paper that almost mis-framed itself (illustrative)

A draft estimates bunching at a progressive-schedule kink, with excess mass implying a taxable-income elasticity of **e = 0.25** (illustrative). The abstract said only "we find significant bunching" — a fact, not a contribution. The fix runs this skill's rules: state the parameter and its use ("e = 0.25 is the sufficient statistic for the marginal deadweight loss of raising the kink rate"); name the counterfactual (a 5-point bracket-rate increase); quantify stakes (marginal DWL scales with e·t/(1−t), so the same revenue carries a higher efficiency cost than a t-only reader expects — magnitudes illustrative). Contribution sentence: "We recover the taxable-income elasticity at a salient kink and map it to the deadweight cost of the bracket reform it disciplines."

## Calibration anchors

- The discriminating test: a JPubE contribution answers "what should government do, or what does this cost society?", not "did the policy move behavior?"
- Hedge: the weight current handling editors place on theory-vs.-evidence framings is not a published rule — confirm against the journal's current author guidelines.

## Output format

```
【Contribution】one sentence (parameter / mechanism / welfare verdict)
【Policy lever】[...]
【Welfare mapping】DWL / MVPF / sufficient stat / optimal-tax / none-yet
【Stakes】revenue / welfare / distribution quantified? [Y/N]
【Scope honesty】external-validity note for international readers
【Next step】jpube-literature-positioning
```
