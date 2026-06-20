> **Illustrative teaching example.** The paper, policy, jurisdiction, and every number below are
> **fictional** and exist only to demonstrate JPAM house style. No real reform, state, agency, or finding
> is described. Corresponding skills:
> [`jpam-writing-style`](../../skills/jpam-writing-style/SKILL.md),
> [`jpam-topic-selection`](../../skills/jpam-topic-selection/SKILL.md),
> [`jpam-theory-building`](../../skills/jpam-theory-building/SKILL.md),
> [`jpam-research-design`](../../skills/jpam-research-design/SKILL.md), and
> [`jpam-data-analysis`](../../skills/jpam-data-analysis/SKILL.md).

# Worked Example: A JPAM-Style Introduction (before → after)

This demonstrates the **JPAM introduction bar** from `jpam-writing-style` and `jpam-topic-selection`: by
the end of the introduction the reader knows the **policy decision**, the **credible design**, the
**effect in policy-relevant units**, and the **calibrated implication** — *without overclaiming*. The
funnel is **policy problem & decision → what's known and the gap → the program studied → the credible
design (named as a tool) → the headline effect in policy units → the cost-benefit / distributional
takeaway → the calibrated implication → brief roadmap**, written so an economist, a political scientist,
and a public-management reader all follow it.

**Illustrative paper (fictional):** *"Automatic Enrollment, Real Take-Up: Effects of a Default
Child-Care Subsidy on Maternal Employment."* Fictional setting: several states switched a child-care
subsidy from opt-in application to **automatic enrollment of eligible families** in **different years**,
creating staggered within-country variation. (Field: labor & welfare; method: staggered
difference-in-differences with a heterogeneity-robust estimator — see the verified DiD and within-study
exemplars in [`../exemplars/library.md`](../exemplars/library.md).)

---

## Before (insider, buries the decision, overclaims at the end — typical first draft)

> The literature on child-care subsidies is large. Many studies examine the relationship between subsidy
> generosity and maternal labor supply. In this paper we use a staggered difference-in-differences design
> with a modern estimator to study the effect of automatic enrollment on employment. We assemble a panel
> of states and estimate event-study specifications. Child care is an important policy area. We find a
> positive and significant effect, suggesting that automatic enrollment should be adopted nationwide.
> Section 2 reviews the literature, Section 3 describes the data, Section 4 the empirical strategy,
> Section 5 the results, Section 6 robustness, and Section 7 concludes.

**What's wrong (against `jpam-writing-style` / `jpam-topic-selection`):**

- **No decision and no policy units.** "Positive and significant" tells a policymaker nothing about
  magnitude, cost, or who benefits — JPAM's whole point (`jpam-data-analysis`: report policy-relevant units).
- **Leads with method**, burying the policy question — the `jpam-writing-style` "lead with the estimator"
  anti-pattern.
- **Overclaims at the end** ("should be adopted nationwide") from one set of states with no cost-benefit
  or external-validity argument — the JPAM overclaiming anti-pattern.
- **No mechanism, no distribution.** Nothing about *why* defaults move take-up or *who* gains
  (`jpam-theory-building`).
- **Over-signposted seven-section roadmap** padding length.

---

## After (JPAM arc — decision + credible design + calibrated implication)

> **When a child-care subsidy is hard to claim, does the paperwork itself keep eligible mothers out of
> work — and would simply enrolling them automatically change that?** We show that when states switched
> from opt-in application to **automatic enrollment** of eligible families, subsidy take-up rose by **22
> percentage points** and maternal employment rose by **4.1 percentage points** (95% CI: 2.3–5.9),
> concentrated among single mothers with the least time and administrative capacity to navigate the old
> application. *(question + decision + effect in policy units in the first breath.)*
>
> Why this matters beyond child-care policy: a recurring finding across economics and public management is
> that **administrative burden** — not just benefit generosity — governs whether a program reaches the
> people it is designed for. If a change in *default* rather than *dollars* moves employment, it speaks to
> how agencies across the policy fields should design enrollment. *(the cross-disciplinary stake, framed
> for an economist and a public-management reader alike — `jpam-topic-selection` cross-field test.)*
>
> Identifying this cleanly is hard because states do not adopt automatic enrollment at random: a state may
> switch precisely when its labor market is already tightening. *(why it is hard — the identification
> problem stated plainly, per `jpam-research-design`.)* We exploit the **staggered timing** of adoption
> across states, comparing each adopting state to not-yet-adopting states with a heterogeneity-robust
> difference-in-differences estimator, and we verify no differential pre-trends in employment before
> adoption. The strongest rival — that adoption coincided with local labor-demand booms — is ruled out:
> if it drove the result, employment would have risen *before* the policy; instead it moves only after.
> *(design as a tool + the adjudication sentence.)*
>
> The mechanism is **take-up, not generosity**: benefit levels did not change, only the default, and the
> employment gain tracks the take-up gain almost one-for-one among the newly enrolled. *(mechanism tied to
> the theory of change — `jpam-theory-building`.)*
>
> Putting costs against benefits, the additional subsidy outlay is **\$1,950 per newly employed mother per
> year**, against an estimated **\$3,400** in combined earnings and reduced cash-assistance receipt — a
> benefit-cost ratio above one under our central discount rate, though it falls below one if take-up
> among non-working eligibles is much higher than we observe. The gains accrue disproportionately to
> lower-income single-parent households. *(cost-benefit with a stated sensitivity and the distributional
> incidence — the `jpam-data-analysis` premium.)*
>
> Our contribution is to show that **default design is a policy lever in its own right**: holding benefit
> dollars fixed, automatic enrollment converts an existing subsidy into measurably higher employment for
> the families least able to clear the application hurdle. We therefore conclude that **states running
> opt-in subsidies should consider switching the default** — while noting that the benefit-cost case
> depends on the take-up margin and on local labor demand, conditions we make explicit. *(contribution +
> a *calibrated* recommendation bounded by the evidence — `jpam-writing-style`.)*
>
> The paper proceeds as follows. Section 2 develops the administrative-burden mechanism and its observable
> implications; Section 3 presents the design and the take-up and employment results; Section 4 reports the
> cost-benefit and distributional analysis and scope conditions. *(brief roadmap — no over-signposting.)*

---

## Why the "after" meets the JPAM bar

Mapped to the skill checklists:

- **Decision and policy units up front** — the reader learns the magnitude (22 pp take-up, 4.1 pp
  employment, with a CI) and the policy lever in the first paragraph (`jpam-data-analysis`: report
  policy-relevant units; `jpam-writing-style`: finding *and* implication by page one).
- **Cross-disciplinary stake stated** — administrative burden is named so an economist and a
  public-management reader both see why it matters (`jpam-topic-selection` cross-field test).
- **Credible design as a tool, with the rival adjudicated** — staggered, heterogeneity-robust DiD is
  named where the design is discussed, no-differential-pre-trends is stated, and the strongest rival is
  ruled out with the `jpam-research-design` adjudication sentence (estimator choice follows the modern
  staggered-DiD guidance in [`../code/`](../code/)).
- **Mechanism, not just an estimate** — the effect is attributed to take-up under a fixed benefit, the
  `jpam-theory-building` lever → mechanism → outcome chain.
- **Cost-benefit and distribution included, with sensitivity** — a benefit-cost ratio with its
  fragility stated and the incidence shown (`jpam-data-analysis` premium), not a bare "significant."
- **Calibrated, not overclaimed** — the recommendation ("states running opt-in subsidies should
  consider switching the default") is bounded by the take-up margin and labor-demand conditions, avoiding
  the JPAM overclaiming anti-pattern.

> Next: stress-test the design with the shared
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md)
> and report results to the shared
> [`../../../shared-resources/empirical-methods/reporting-standards.md`](../../../shared-resources/empirical-methods/reporting-standards.md);
> benchmark the framing against verified real JPAM papers in
> [`../exemplars/library.md`](../exemplars/library.md); and adapt the staggered-DiD command chain in
> [`../code/`](../code/).
