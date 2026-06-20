> **Illustrative teaching example.** The policy, setting, design, and every number below are **fictional**
> and exist only to demonstrate AEJ: Economic Policy (AEJ: Policy) house style. No real-paper facts and no
> real policy are stated. Corresponding skills:
> [`aejpol-writing-style`](../../skills/aejpol-writing-style/SKILL.md),
> [`aejpol-topic-selection`](../../skills/aejpol-topic-selection/SKILL.md),
> [`aejpol-identification`](../../skills/aejpol-identification/SKILL.md), and
> [`aejpol-theory-model`](../../skills/aejpol-theory-model/SKILL.md).

# Worked Example: An AEJ: Policy-Style Introduction (before → after)

This demonstrates the **AEJ: Policy introduction arc** from
[`aejpol-writing-style`](../../skills/aejpol-writing-style/SKILL.md):
**policy question → why credible identification is hard → the design that delivers it → headline causal
estimate (with SE/CI) → welfare / cost-benefit / distributional implication → concrete, calibrated policy
lesson → brief roadmap.**

Two AEJ: Policy house rules drive the rewrite and distinguish it from a general applied-micro journal:

- AEJ: Policy publishes the **economic analysis OF policy**: a paper must lead with a **policy question of
  broad interest** and end the first paragraph with a **welfare / cost-benefit / distributional** reading,
  not merely a clean estimate ([`aejpol-topic-selection`](../../skills/aejpol-topic-selection/SKILL.md)).
- AEA house style **forbids significance asterisks and boldface for significance** — findings are
  communicated through **point estimates with standard errors / confidence intervals** in
  policy-interpretable units ([`aejpol-writing-style`](../../skills/aejpol-writing-style/SKILL.md),
  [`aejpol-tables-figures`](../../skills/aejpol-tables-figures/SKILL.md)).

**Illustrative paper (fictional):** *"Does a Refundable Childcare Credit Pay for Itself? Evidence from a
Staggered State Rollout."* Fictional setting: several U.S. states adopt a refundable childcare tax credit
in different years; the paper evaluates its effect on maternal employment with a modern staggered-DID
design and reads the estimate against the credit's fiscal cost. Every magnitude is invented.

---

## Before (buries the policy question under data and method — typical first-draft intro)

> We use administrative tax records linked to employment data and a two-way fixed-effects difference-in-
> differences specification to study a refundable childcare credit. The literature on childcare subsidies
> is large. We estimate the effect of the credit on maternal employment, controlling for state and year
> fixed effects and a vector of demographic covariates. The coefficient on the post-adoption indicator is
> positive and significant at the 1% level (***). Section 2 reviews the literature, Section 3 describes the
> data, Section 4 presents the empirical strategy, Section 5 the results, and Section 6 concludes.

**What is wrong (against `aejpol-writing-style` / `aejpol-topic-selection` / `aejpol-identification`):**

- **Leads with the dataset and the estimator** ("administrative tax records… two-way fixed-effects
  difference-in-differences") instead of the policy question — the named AEJ: Policy anti-pattern. This
  reads as a generic applied-micro paper, not a policy paper.
- **No policy question and no welfare stake on page one.** A broad AEA reader cannot tell what policy is at
  issue or why it matters.
- **No headline estimate with units, and no uncertainty.** "Significant at the 1% level (\*\*\*)" is
  **exactly the asterisk reporting AEA house style forbids** — there is no point estimate, no standard
  error, no confidence interval, no policy magnitude.
- **Staggered TWFE with no acknowledgment of heterogeneity bias** — a fast referee kill shot
  ([`aejpol-identification`](../../skills/aejpol-identification/SKILL.md) Path A).
- **No cost-benefit reading.** The paper never says whether the credit is *worth it* — the AEJ: Policy
  "so what."
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (AEJ: Policy arc — policy question + credible design + estimate-with-uncertainty + welfare reading)

> **Does a refundable childcare credit raise maternal employment enough to pay for a meaningful share of
> its own cost — and who actually benefits?** Exploiting the staggered adoption of such credits across
> states, we find the credit raises employment among mothers of young children by **3.4 percentage points
> (90% CI [2.1, 4.7])**, and that the resulting earnings and tax revenue offset roughly **40 cents of every
> dollar of credit**, with the employment gains concentrated among lower-income mothers. *(policy question
> + headline magnitude + its uncertainty + a cost-benefit and distributional reading, in the first
> breath — no asterisks.)*
>
> Identifying this is hard because states do not adopt the credit at random: the same labor-market
> conditions that make a credit politically feasible also move maternal employment, so a naive before-after
> or two-way fixed-effects comparison conflates the policy with the trends that produced it. *(why credible
> identification is hard — the policy is not a clean experiment.)*
>
> We address this with a **heterogeneity-robust staggered difference-in-differences** design (Callaway–
> Sant'Anna), comparing newly adopting states to not-yet-adopting states, and we show the **pre-adoption
> event-study leads are flat and precisely estimated**, with an honest-DID bound confirming the sign
> survives pre-trends twice the largest observed lead. A Goodman-Bacon decomposition shows a conventional
> TWFE estimate would be biased by already-treated comparisons. *(the design that delivers credible causal
> evidence; [`aejpol-identification`](../../skills/aejpol-identification/SKILL.md) Path A.)*
>
> The employment effect is **3.4 pp (90% CI [2.1, 4.7])** in the medium run. Translating it through a
> transparent fiscal ledger — additional earnings, the mechanical credit cost, and the behavioral revenue
> response — the credit's **net cost per additional employed mother is about $X**, and it recovers roughly
> **40% of its gross cost** through higher earnings and taxes; the incidence of the employment gain falls
> mainly on the **bottom third of the maternal earnings distribution**. *(headline estimate restated with
> its welfare/cost-benefit and distributional reading;
> [`aejpol-theory-model`](../../skills/aejpol-theory-model/SKILL.md).)*
>
> Our contribution is a **policy answer, not just an estimate**: we show a refundable childcare credit is a
> partially self-financing way to raise maternal employment, and that its benefits are progressive. *(the
> contribution framed as a policy lesson;
> [`aejpol-literature-positioning`](../../skills/aejpol-literature-positioning/SKILL.md).)* The estimate is
> the medium-run effect for the marginal mothers these state credits reach; we do **not** claim it
> generalizes to a national credit at a much larger scale, and the cost-recovery figure assumes the
> behavioral responses we estimate are stable at that scale. *(calibrated scope — no overclaim.)* Beyond
> childcare, the result illustrates that **a transfer's true cost depends on the labor-supply response it
> induces** — relevant to any means-tested credit whose recipients are on an employment margin. *(broad,
> calibrated lesson.)*
>
> The paper proceeds as follows. Section 2 describes the state credits and the data; Section 3 presents the
> design and pre-trend evidence; Section 4 reports the employment effect and robustness; Section 5 builds
> the fiscal ledger and the incidence analysis. *(brief roadmap — no over-signposting.)*

---

## Why the "after" meets the AEJ: Policy bar

Mapped to this pack's skill checklists:

- **First paragraph states the policy question + the magnitude + its uncertainty + a welfare reading** —
  the employment effect (3.4 pp, 90% CI [2.1, 4.7]) and the cost-recovery share appear immediately, with
  units and a confidence interval, never an asterisk
  ([`aejpol-writing-style`](../../skills/aejpol-writing-style/SKILL.md): "headline estimate with SE/CI
  appears early, in policy-interpretable units"; "no significance asterisks").
- **It is unmistakably a policy paper** — a non-specialist sees the childcare-credit question and the
  "does it pay for itself / who benefits" stake, the AEJ: Policy sweet spot, not a generic applied-micro
  application ([`aejpol-topic-selection`](../../skills/aejpol-topic-selection/SKILL.md)).
- **Identification is credible and design-appropriate** — heterogeneity-robust DID, flat pre-trends,
  honest-DID bound, and a Bacon decomposition, exactly the
  [`aejpol-identification`](../../skills/aejpol-identification/SKILL.md) Path A bar; the staggered-TWFE
  trap from the "before" is named and avoided.
- **The estimate is read as a welfare / cost-benefit / distributional object** — a fiscal ledger turns the
  employment effect into net cost per job and a cost-recovery share, with an incidence statement,
  satisfying [`aejpol-theory-model`](../../skills/aejpol-theory-model/SKILL.md) (sufficient statistics →
  policy object; distributional reading).
- **The claim is calibrated, not overstated** — the estimand, the population, and the scale at which the
  cost-recovery figure holds are stated explicitly, the AEJ: Policy "do not overclaim" discipline
  ([`aejpol-writing-style`](../../skills/aejpol-writing-style/SKILL.md)).
- **Sibling check passes:** this is not identification-for-its-own-sake with no policy lever (*AEJ:
  Applied*) and not a specialist field-public-finance contribution with no broad framing (*J. Public
  Economics*); it is a credibly identified, welfare-relevant analysis of a real policy — AEJ: Policy's
  identity.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified** AEJ: Policy
> papers whose introductions execute this arc,
> [`../../skills/aejpol-robustness/SKILL.md`](../../skills/aejpol-robustness/SKILL.md) for defending the
> policy estimate, and [`../code/`](../code/) for a runnable empirical command chain. For the venue-neutral
> referee objections a staggered-DID policy claim must pre-empt, see
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).
