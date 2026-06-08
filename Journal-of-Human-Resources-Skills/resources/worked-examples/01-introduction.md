> **Illustrative teaching example.** The paper, setting, reform, and every number below are **fictional**
> and exist only to demonstrate *Journal of Human Resources* (JHR) house style. No real-paper facts are
> stated, and no real policy is invoked. Corresponding skills:
> [`jhr-writing-style`](../../skills/jhr-writing-style/SKILL.md),
> [`jhr-contribution-framing`](../../skills/jhr-contribution-framing/SKILL.md), and
> [`jhr-identification-strategy`](../../skills/jhr-identification-strategy/SKILL.md).

# Worked Example: A *Journal of Human Resources*-Style Introduction (before → after)

This demonstrates the introduction arc JHR rewards (from `jhr-writing-style` and `jhr-contribution-framing`):
**empirical-micro / public-policy question → why the human-capital margin matters → identifying variation →
headline causal estimate with magnitude and interval → reconciliation with prior estimates → policy lesson
→ brief roadmap.** The governing rules from `jhr-writing-style` are **front-load the policy-relevant
finding** and, because JHR judges papers partly on whether they **reconcile results with prior published
work** (`jhr-identification-strategy`), say early how your estimate squares with — or overturns — what the
literature already believes. Jargon is defined on first use, and the paper stays inside JHR's empirical-
microeconomics scope (it is *not* an HR-management paper).

**Illustrative paper (fictional):** *"Does a Longer School Day Raise Earnings? Evidence from a Staggered
Full-Day-Schooling Reform."* Fictional setting: a single country that extended the primary-school day from
half-day to full-day, rolled out district by district over several years, with linked school and
administrative earnings records.

---

## Before (buries the contribution — typical first-draft intro)

> The relationship between education and labor market outcomes has been a central topic in economics for
> decades. Many studies have examined how schooling affects wages, employment, and other outcomes. In this
> paper, we use a difference-in-differences design and administrative data to study a full-day-schooling
> reform. We run several regressions and report the estimates. The results have implications for education
> policy. Section 2 reviews the literature, Section 3 describes the data, Section 4 presents the methods,
> Section 5 reports results, and Section 6 concludes.

**What's wrong (against `jhr-writing-style` / `jhr-contribution-framing` / `jhr-identification-strategy`):**

- **Leads with a literature gesture and the method** ("we use a difference-in-differences design") instead
  of the policy question and the answer — the named anti-pattern in `jhr-writing-style`.
- **No causal estimate, magnitude, or uncertainty on page one**, so a reader cannot tell what the reform
  did or how large the effect is.
- **No reconciliation with prior estimates** — JHR explicitly weighs whether a paper squares its results
  with the existing literature; this intro never says where its number sits relative to known returns.
- **Identification is invisible** — the staggered rollout (the source of quasi-experimental variation) is
  never named, and the modern-DID concern with staggered timing is ignored.
- **Vague policy payoff** ("implications for education policy") and an **over-signposted roadmap**.

---

## After (JHR arc — policy question + causal estimate + reconciliation, contribution early)

> **Does lengthening the school day build enough human capital to raise adult earnings, or does it mostly
> substitute for time children would have spent learning elsewhere?** Exploiting the staggered district-by-
> district rollout of a reform that doubled the primary-school day, we estimate that exposure to full-day
> schooling raised adult earnings by **6.2% (95% CI 3.9–8.5)** — a return at the **upper end of, but
> consistent with, the schooling-returns literature** once the extra instructional hours are converted to
> equivalent years of schooling. *(Policy question + headline causal estimate with magnitude and interval +
> reconciliation with prior estimates, in the first breath.)*
>
> Identifying this effect is difficult because districts that adopted the reform earlier may differ in
> labor-market trajectories from later adopters, and a naive two-way-fixed-effects comparison of early and
> late adopters can be contaminated by treatment-effect heterogeneity across cohorts. *(Why it is hard — the
> identification problem, stated in modern-DID terms.)*
>
> We use linked school-enrollment and administrative earnings records and a **heterogeneity-robust
> difference-in-differences estimator** (a staggered-adoption design that avoids the negative-weighting
> problem of two-way fixed effects), with an event-study plot showing flat pre-reform earnings trends across
> districts and clustering at the district level. *(Identifying variation — the staggered rollout — and the
> design in one paragraph, with the pre-trend and inference handled, per `jhr-identification-strategy`.)*
>
> The 6.2% earnings gain is concentrated among children from lower-income households and is **absent for
> children who already attended after-school programs**, whose effective instructional time changed least —
> the pattern a human-capital mechanism predicts and a pure credentialing story does not. *(Headline result
> restated with the subgroup signature that adjudicates the mechanism.)*
>
> Our contribution is to provide a **credible causal return to instructional time** — distinct from the
> return to years of schooling — and to **reconcile it with prior compulsory-schooling estimates**: per
> equivalent year of added instruction, our return brackets the IV estimates from school-leaving-age
> reforms, suggesting those estimates are not driven by credentialing alone. *(Contribution stated early,
> tied to a policy lever and explicitly reconciled with the literature, per `jhr-contribution-framing` and
> the JHR reconciliation norm.)* We are precise about scope: this is the return to instructional time for
> primary-school cohorts in this setting, not a universal return to the school day. *(Scope honesty.)*
>
> The article proceeds as follows. Section 2 places the estimate in the returns-to-schooling and
> instructional-time literatures; Section 3 describes the linked data and the staggered-DID design; Section 4
> reports the earnings effect, the subgroup signature, and robustness to estimator choice and pre-trend
> tests. *(Brief roadmap — no over-signposting.)*

---

## Why the "after" meets the JHR bar

Mapped to the skill checklists:

- **Policy question and answer lead** — the first paragraph names the education-policy lever (school-day
  length), the human-capital margin, and the earnings stake, front-loading the finding as `jhr-writing-style`
  requires.
- **Causal estimate with uncertainty** — the headline effect (6.2%) leads with a **95% interval**, not "the
  regression shows…," per `jhr-data-analysis`.
- **Reconciliation is explicit** — the intro says where the estimate sits relative to compulsory-schooling
  and instructional-time work, the distinctive JHR demand that papers reconcile with prior published results
  (`jhr-identification-strategy`).
- **Identification is named and modernized** — the staggered rollout is the variation, and the design uses a
  heterogeneity-robust DID with an event-study pre-trend check and district-level clustering, satisfying the
  `jhr-identification-strategy` DID/event-study checklist.
- **Contribution type is explicit** — a **credible causal parameter** (return to instructional time) that is
  distinct from, and reconciled with, the return to years of schooling — the `jhr-contribution-framing`
  shape, not "we find a significant effect."
- **The rival is adjudicated, scope disciplined** — a pure credentialing account would not predict the
  low-income / instructional-time-gradient signature; the data show it, and the paper states the estimate is
  local rather than universal.

> Next: adapt the reproducible analysis skeleton in [`../code/`](../code/) when turning this introduction
> arc into a full empirical workflow, and stress-test the design against
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).
