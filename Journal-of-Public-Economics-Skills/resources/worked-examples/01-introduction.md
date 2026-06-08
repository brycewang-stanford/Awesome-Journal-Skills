> **Illustrative teaching example.** The paper, setting, reform, and every number below are **fictional**
> and exist only to demonstrate *Journal of Public Economics* (JPubE) house style. No real-paper facts are
> stated, and no real policy is invoked. Corresponding skills:
> [`jpube-writing-style`](../../skills/jpube-writing-style/SKILL.md),
> [`jpube-contribution-framing`](../../skills/jpube-contribution-framing/SKILL.md), and
> [`jpube-identification-strategy`](../../skills/jpube-identification-strategy/SKILL.md).

# Worked Example: A *Journal of Public Economics*-Style Introduction (before → after)

This demonstrates the introduction arc JPubE rewards (from `jpube-writing-style` and
`jpube-contribution-framing`): **government-policy question → why the behavioral margin matters →
identifying variation (the policy discontinuity) → headline causal estimate with magnitude and interval →
translation into welfare/revenue terms → contribution to public-finance theory or evidence → brief
roadmap.** The governing rule from `jpube-writing-style` is **lead with the policy question and then the
answer**, and **translate every headline estimate** into deadweight loss, revenue, MVPF, or distributional
language a policy economist reads instantly. Jargon (elasticity, bunching, notch) is defined on first use.

**Illustrative paper (fictional):** *"How Elastic Is Reported Income at a Benefit Notch? Bunching Evidence
from a Childcare-Subsidy Cliff."* Fictional setting: a single country whose childcare subsidy is withdrawn
entirely once household earnings cross a sharp eligibility threshold (a *notch*), with full-population
administrative earnings and benefit records.

---

## Before (buries the contribution — typical first-draft intro)

> The labor supply effects of transfer programs have been studied extensively by economists across many
> fields. Many factors affect how people respond to taxes and benefits, including wages, hours
> constraints, and information. In this paper, we use administrative data and a bunching estimator to study
> behavioral responses around a childcare-subsidy threshold. We estimate several specifications and present
> the results. Understanding these responses is important for policymakers. Section 2 reviews the
> literature, Section 3 describes the data, Section 4 presents the methods, Section 5 reports results, and
> Section 6 concludes.

**What's wrong (against `jpube-writing-style` / `jpube-contribution-framing` / `jpube-identification-strategy`):**

- **Leads with method and a literature gesture** ("we use … a bunching estimator") instead of the
  government-policy question — the named anti-pattern in `jpube-writing-style`.
- **No policy question and no answer on page one.** A reader cannot tell which policy lever is at stake,
  what the behavioral response is, or what it implies for welfare or revenue (fails the
  `jpube-contribution-framing` "what do we now know about government policy?" test).
- **No headline estimate with magnitude or uncertainty**, and no translation into deadweight loss, revenue,
  or distributional terms.
- **Identification is invisible** — the notch (the policy-induced discontinuity that JPubE prizes) is never
  named as the source of identifying variation.
- **Throat-clearing** ("studied extensively," "is important for policymakers") and an **over-signposted
  roadmap** doing the work the argument should do.

---

## After (JPubE arc — policy question + causal estimate + welfare translation, contribution early)

> **Should a childcare subsidy be withdrawn at a sharp earnings cliff, or phased out gradually?** The answer
> turns on how much households distort their reported earnings to stay below the cliff. We show that the
> notch — the complete loss of the subsidy at the eligibility threshold — induces sharp **bunching** (excess
> mass of households reporting earnings just below the cutoff), implying a compensated elasticity of
> reported income of **0.21 (95% CI 0.16–0.26)**, and that the resulting earnings distortion destroys
> **\$0.34 of social welfare per \$1 of subsidy withdrawn** at the cliff. *(Policy question + headline causal
> estimate with magnitude and interval + welfare translation, in the first breath; "notch" and "bunching"
> are defined in place.)*
>
> Identifying this elasticity is hard because earnings around the threshold also reflect ordinary income
> dynamics and measurement, so a raw density contrast would confound behavioral bunching with the smooth
> shape of the earnings distribution. *(Why it is hard — the identification problem, stated in public-finance
> terms.)*
>
> We use complete-count administrative earnings and benefit records and estimate the **excess mass at the
> notch against a counterfactual density** fitted from the distribution away from the cutoff, recovering the
> structural elasticity after accounting for the dominated region just above the cliff and for optimization
> frictions that attenuate bunching. Inference is by bootstrap over the counterfactual fit, and we show the
> estimate is stable across bin widths and excluded-region choices. *(Identifying variation — the policy
> notch — and method in one paragraph; the dominated region and frictions handled explicitly, per
> `jpube-identification-strategy` Branch A.)*
>
> The implied elasticity of 0.21 is concentrated among the self-employed and among households with a
> second earner, and it is **absent in wage-only single-earner households**, whose earnings cannot be
> finely adjusted — the behavioral signature a frictionless account would not predict. *(Headline result
> restated with the subgroup signature that distinguishes the mechanism.)*
>
> Our contribution is to convert this elasticity into a **sufficient-statistic welfare verdict**: replacing
> the cliff with a linear phase-out at the revenue-equivalent rate would **lower the deadweight loss of the
> subsidy by roughly 60%** while holding the transfer to eligible families fixed — a design lesson that
> travels to any means-tested program with a benefit cliff. *(Contribution stated early, mapped to a named
> counterfactual reform and a welfare quantity, per `jpube-contribution-framing`.)* We are precise about
> scope: the elasticity is a local response at this threshold for this population, not a global structural
> parameter or a universal optimal phase-out rate. *(Scope honesty for an international policy readership.)*
>
> The article proceeds as follows. Section 2 sets out the notch model and the welfare mapping; Section 3
> describes the data and the bunching estimator; Section 4 reports the elasticity, the subgroup signature,
> and the phase-out counterfactual with its sensitivity to the friction correction. *(Brief roadmap — no
> over-signposting.)*

---

## Why the "after" meets the JPubE bar

Mapped to the skill checklists:

- **Policy question leads, answer follows** — the first paragraph names the government policy (subsidy
  cliff vs. phase-out), the behavioral margin (reported-earnings adjustment), and the welfare stake, exactly
  the `jpube-writing-style` "lead with the policy question, then the answer" rule.
- **Every headline estimate is translated** — the elasticity (0.21) is immediately converted into welfare
  (\$0.34 per \$1; a ~60% DWL reduction under the counterfactual), never left for the reader to convert
  (`jpube-writing-style` + `jpube-data-analysis`).
- **Uncertainty is reported** — the elasticity leads with a **95% interval**, and the welfare conclusion's
  sensitivity to the friction correction is flagged, per `jpube-data-analysis` (propagate SEs into the
  welfare object).
- **Identification is the policy discontinuity** — the notch is named as the identifying variation, with the
  dominated region, counterfactual density, and frictions handled, satisfying the
  `jpube-identification-strategy` bunching branch and its diagnostics.
- **Contribution type is explicit** — this is a **sufficient-statistic welfare verdict** mapped to a named
  reform (cliff → phase-out), the `jpube-contribution-framing` "welfare verdict via a transparent
  framework" shape, not "we find a significant effect."
- **The rival is confronted, scope is disciplined** — the frictionless reading would predict bunching even
  among wage-only single earners; the data show the opposite, and the paper states the estimate is local,
  avoiding the over-claiming anti-pattern.

> Next: adapt the reproducible analysis skeleton in [`../code/`](../code/) when turning this
> introduction arc into a full empirical workflow, and stress-test the design against
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).
