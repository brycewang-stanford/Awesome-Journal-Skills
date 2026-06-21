---
name: aejpol-writing-style
description: Use when drafting or revising the prose of an AEJ: Economic Policy manuscript — especially the abstract and introduction — to translate causal estimates into a clear policy takeaway without overclaiming. Shapes the policy-first narrative and house style; it does not design identification or build the welfare model.
---

# Writing Style — From Estimate to Policy Takeaway (aejpol-writing-style)

## When to trigger

- The intro buries the policy question under data or method
- The abstract reports a coefficient but no policy lesson
- The paper has a clean estimate but no sentence a policymaker could act on — or it overclaims
- You are polishing for submission and need AEA house tone

> Late-stage polish: do not rewrite the intro until identification (`aejpol-identification`), the welfare bridge (`aejpol-theory-model`), and robustness (`aejpol-robustness`) have settled.

## The AEJ: Policy introduction arc

**Policy question → why credible identification is hard → the design that delivers it → headline causal estimate (with SE/CI) → welfare / cost-benefit / distributional reading → concrete, calibrated policy lesson → brief roadmap.**

The distinctive moves vs. a general applied-micro intro:

1. **Open with the policy question, not the dataset or estimator.** A non-specialist AEA reader should know within two sentences what policy is at stake and why the answer matters.
2. **Put the headline estimate, with its uncertainty, on page one** — in policy-interpretable units (a percentage-point effect, a cost-per-outcome), never an asterisk.
3. **Translate into a policy takeaway** — the cost-benefit / MVPF / incidence reading — and state it as the contribution.
4. **Calibrate the claim.** Say exactly what the estimand is, for whom, and the conditions under which the lesson holds. The credibility of an AEJ: Policy paper rests as much on *not overclaiming* as on the estimate.

## Translating estimates into policy language without overclaiming

- Convert coefficients into decision-relevant quantities ("a $1,000 expansion raises take-up by X and costs $Y per additional recipient") rather than leaving them as elasticities.
- Tie magnitude to a benchmark a policymaker recognizes (the program's budget, the status-quo level, a comparable policy).
- **Hedge precisely, not vaguely:** state the population the estimate applies to, the time horizon, and the assumptions the welfare reading needs. Replace "this shows policy X is good" with "for this population and horizon, the marginal dollar of X returns $Z, assuming [stated condition]."
- Separate what the data show (the causal estimate) from what the framework adds (the welfare reading) so a referee can grant one without the other.

## AEA house style
- Author–year citations; SEs/CIs not asterisks (mirror `aejpol-tables-figures`); active voice; abstract that states question, design, headline estimate, and policy lesson. Online appendix carries the long material; the main text stays self-contained and readable. Review is single-blind, so the front matter names the authors — no need to anonymize the prose.

## Checklist

- [ ] First two sentences state the policy question and why it matters
- [ ] Headline estimate with SE/CI appears early, in policy-interpretable units
- [ ] A one-sentence policy takeaway (cost-benefit / MVPF / incidence) is stated as the contribution
- [ ] The claim is calibrated: population, horizon, and assumptions named
- [ ] Causal estimate and welfare reading are separable in the prose
- [ ] No significance asterisks; author–year citations; abstract carries the policy lesson
- [ ] Self-citations cited normally (single-blind — no anonymization needed)

## Anti-patterns

- An intro that leads with the dataset, the institutional weeds, or the estimator
- An abstract that ends at the coefficient with no policy lesson
- Overclaiming ("our results prove policy X should be adopted nationwide") beyond the estimand
- Vague hedging ("results should be interpreted with caution") instead of a precise scope statement
- Burying the policy takeaway in the conclusion where a policymaker will not find it
- Padding the prose with self-citations to signal a track record (cite only what the argument needs)

## Worked vignette (illustrative)

Before: "Using administrative data and a difference-in-differences design, we estimate the effect of the reform on enrollment; the coefficient is 0.06 (s.e. 0.01)." After (AEJ: Policy): "Does auto-enrollment raise retirement-plan participation enough to justify its administrative cost? Exploiting the staggered rollout across employers, we find auto-enrollment raises participation by 6 percentage points (90% CI [4, 8]). At the program's per-worker cost this implies roughly $X per additional participant — cost-effective relative to a matching subsidy for this low-saver population, though the gain is concentrated among workers who would not have opted in (illustrative)." Question first, estimate with CI, policy lesson, calibrated scope.

## Output format

```
【Opening policy question】one sentence
【Headline estimate】value + SE/CI in policy units, stated early
【Policy takeaway】cost-benefit / MVPF / incidence sentence
【Calibration】population + horizon + assumptions named
【Overclaim check】claim ≤ what design+framework support? [Y/N]
【Next step】aejpol-replication-package or aejpol-referee-strategy
```
