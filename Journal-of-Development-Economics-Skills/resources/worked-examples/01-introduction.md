> **Illustrative teaching example.** The paper, setting, and every number below are **fictional** and
> exist only to demonstrate JDE house style. No real-paper facts and no real policy are stated. Corresponding
> skills: [`jde-writing-style`](../../skills/jde-writing-style/SKILL.md),
> [`jde-contribution-framing`](../../skills/jde-contribution-framing/SKILL.md),
> [`jde-identification-strategy`](../../skills/jde-identification-strategy/SKILL.md), and
> [`jde-topic-selection`](../../skills/jde-topic-selection/SKILL.md).

# Worked Example: A JDE-Style Introduction (before → after)

This demonstrates the **JDE introduction arc** from `jde-writing-style`:
**development question → why it matters for development → setting & design in a few sentences → headline
result with a welfare-relevant magnitude → contribution relative to the frontier → roadmap** — with the
JDE rules that the **abstract and intro state the finding with a number in welfare-relevant units**, that
**policy/welfare stakes are visible**, and that **external-validity scope is stated honestly** rather than
overclaimed (`jde-contribution-framing`, `jde-writing-style`).

**Illustrative paper (fictional):** *"Clinics on the Bus Route: A Field Experiment on Mobile Antenatal
Care and Birth Outcomes."* Fictional setting: a low-income country where a non-profit randomized which of
160 rural villages received a weekly mobile antenatal-care clinic. The intervention is **invented for
teaching** and is not a real program.

---

## Before (buries the development question — typical first-draft intro)

> The relationship between health-care access and child outcomes has been studied extensively in the
> development literature. Many papers examine clinics, health workers, and maternal health. In this paper,
> we use a cluster-randomized controlled trial, and we estimate intention-to-treat effects with standard
> errors clustered at the village level, supplemented by a Lee-bounds attrition analysis and Romano–Wolf
> multiple-testing adjustment, to study the effects of a mobile antenatal-care intervention. We assemble
> household survey data across treatment and control villages. Maternal and child health is an important
> topic for policymakers in developing countries. Section 2 reviews the literature, Section 3 describes the
> data, Section 4 presents the empirical strategy, Section 5 reports results, and Section 6 concludes.

**What's wrong (against `jde-writing-style` / `jde-contribution-framing` / `jde-topic-selection`):**

- **Leads with method and inference machinery** ("cluster-randomized … clustered standard errors … Lee
  bounds … Romano–Wolf") instead of the development question — a named anti-pattern in
  `jde-identification-strategy` and `jde-writing-style`.
- **No finding and no magnitude.** The abstract/intro "names a topic but states no effect size" — the exact
  `jde-writing-style` anti-pattern. No welfare-relevant number appears.
- **No policy/welfare framing.** Nothing translates the effect into terms a development economist or a
  policymaker can weigh (cost per outcome, share of a gap, SDs) — fails `jde-contribution-framing`.
- **Throat-clearing** ("has been studied extensively," "is an important topic") with vague development
  stakes; the development *question* is never posed in paragraph one.
- **No stated contribution** — what we did not know and now know is missing; an editor skimming for two
  minutes could not restate it.
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (JDE arc — development question + magnitude + welfare framing + honest scope)

> **Can bringing antenatal care to villages — rather than waiting for women to travel to distant clinics —
> improve newborn health where maternal mortality is high and roads are poor?** In a cluster-randomized
> field experiment across 160 villages, weekly mobile antenatal clinics raised the share of women receiving
> at least four antenatal visits by 22 percentage points and reduced low-birth-weight births by 4.1
> percentage points (off a control mean of 18%). *(development question + headline answer + welfare-relevant
> magnitude, in the first breath.)*
>
> This matters for development because the binding constraint on antenatal care in poor rural settings is
> often **distance, not price or demand**: care is nominally free, yet travel time and forgone work keep
> attendance low, and the resulting gaps in newborn health propagate into later human capital. Whether
> moving the point of care closer relaxes that constraint — and how much health it buys per dollar — is a
> first-order question for how scarce health budgets are spent. *(why it matters for development; the
> mechanism stated before the design.)*
>
> We randomized, at the village level, which of 160 villages received a weekly mobile antenatal clinic over
> 18 months, with the remaining villages retaining the existing fixed-facility system. Randomization was
> stratified by district and baseline clinic distance; we registered a pre-analysis plan, verify balance on
> baseline characteristics, and bound the estimates for the modest differential attrition we observe.
> *(setting & design in a few sentences — design as a tool, diagnostics named, not foregrounded.)*
>
> Mobile clinics raised four-visit antenatal coverage by **22 percentage points** and cut low-birth-weight
> births by **4.1 percentage points**, with the largest gains in the villages that started farthest from a
> fixed facility — consistent with **distance** as the operative margin. At an estimated program cost of
> **US$X per averted low-birth-weight birth** (fictional), the intervention compares favorably with
> fixed-facility expansion on a cost-per-outcome basis. *(headline result restated with the mechanism and a
> policy-comparable unit; magnitude in welfare-relevant terms, per `jde-contribution-framing`.)*
>
> Our contribution is to show that **the geography of delivery, not just the price or supply of care, is a
> policy lever for newborn health** in poor rural settings: holding the service constant, relocating it
> closer reallocates care toward the women who were previously priced out by distance. *(contribution stated
> early, as one restatable sentence, relative to a specific prior view.)* We are deliberately cautious about
> external validity: the result is a local average treatment effect for villages with poor road access and
> an underused fixed-facility system, and it need not carry to settings where distance is not the binding
> constraint. *(honest scope — calibrated claim, not an overclaimed universal law, per `jde-writing-style`
> and `jde-topic-selection`.)*
>
> The paper proceeds as follows. Section 2 describes the experiment and data; Section 3 presents the design,
> balance, and attrition handling; Section 4 reports effects on care and birth outcomes and the
> distance-gradient mechanism; Section 5 discusses cost-effectiveness and scope. *(brief roadmap — no
> over-signposting.)*

---

## Why the "after" meets the JDE bar

Mapped to the skill checklists:

- **Abstract/intro states the finding with a number in welfare units** — the headline effects (22 pp
  coverage; 4.1 pp low birth weight) and a cost-per-averted-outcome appear immediately
  (`jde-writing-style`: "abstract states the finding with a number"; `jde-contribution-framing`:
  "effect in welfare/policy-comparable terms").
- **Development question first, method demoted to a tool** — the RCT and its inference machinery
  (clustering, Lee bounds, MHT) are mentioned only where the design is described, never as the lead,
  avoiding the shared "leading with the estimator" anti-pattern (`jde-identification-strategy`).
- **Policy/welfare made visible** — effects are translated into coverage, birth outcomes, and cost per
  averted outcome a policymaker can weigh.
- **Contribution stated early and restatable** ("geography of delivery, not just price or supply"), not a
  vague "we contribute to the literature" (`jde-contribution-framing` one-sentence test).
- **Honest external validity** — the result is framed as a LATE for poor-road, underused-facility villages,
  explicitly *not* a universal development law (`jde-topic-selection` / `jde-writing-style` anti-patterns
  on overclaiming a single-site LATE).
- **Identification diagnostics signposted but not foregrounded** — PAP, stratified randomization, balance,
  and attrition bounding are named, matching the `jde-identification-strategy` RCT branch (PAP, balance,
  attrition/Lee bounds, inference at the unit of randomization, MHT) without burying the question.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for verified **real** JDE papers whose
> introductions execute this arc, and [`../code/`](../code/) for the runnable estimator chain — e.g. the
> RCT/DiD inference and event-study skeleton in [`../code/stata/03_did_modern.do`](../code/stata/03_did_modern.do)
> and the publication-grade plot in [`../code/python/event_study_plot.py`](../code/python/event_study_plot.py).
