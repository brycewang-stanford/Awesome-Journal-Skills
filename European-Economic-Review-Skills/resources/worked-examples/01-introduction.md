> **Illustrative teaching example.** The paper, setting, and every number below are **fictional** and
> exist only to demonstrate European Economic Review (EER) house style. No real-paper facts and no real
> policy are stated. Corresponding skills:
> [`eer-writing-style`](../../skills/eer-writing-style/SKILL.md),
> [`eer-topic-selection`](../../skills/eer-topic-selection/SKILL.md),
> [`eer-literature-positioning`](../../skills/eer-literature-positioning/SKILL.md), and
> [`eer-identification`](../../skills/eer-identification/SKILL.md).

# Worked Example: An EER-Style Introduction (before → after)

This demonstrates the **EER introduction arc** from
[`eer-writing-style`](../../skills/eer-writing-style/SKILL.md):
**question → why it is hard/open → approach → headline result (with a standard error) → mechanism →
contribution & lesson → scope → brief roadmap.**

Two EER house features drive the rewrite and distinguish it from a field-journal intro:

- EER is **Elsevier's general-interest** European economics journal (all fields, theory and empirical),
  so the question and the answer must be legible to an economist **outside** the subfield, fast
  ([`eer-topic-selection`](../../skills/eer-topic-selection/SKILL.md)). "European" is institutional
  history, not a scope restriction.
- EER house style **reports standard errors** and lets the **magnitude carry the result** — findings are
  written as **point estimates with standard errors / confidence intervals**, not significance asterisks
  ([`eer-tables-figures`](../../skills/eer-tables-figures/SKILL.md)). Elsevier also requires **research
  highlights** and a **declaration of interest**.

**Illustrative paper (fictional):** *"Commuting Costs and Local Wage Adjustment: Evidence from a Staggered
Regional Rail Expansion."* Fictional setting: a staggered rollout of regional rail lines is used to study
how falling commuting costs pass through to local wages. Every magnitude is invented.

---

## Before (buries the question under data and machinery — typical first-draft intro)

> We use administrative matched employer–employee data and a two-way fixed-effects regression of log wages
> on a rail-access dummy with year and municipality fixed effects, clustering by municipality. Commuting and
> local labor markets have been studied extensively. We exploit the staggered opening of regional rail lines.
> The coefficient on rail access is positive and significant at the 1% level (***). Section 2 reviews the
> literature, Section 3 describes the data, Section 4 the empirical strategy, Section 5 the results, and
> Section 6 concludes.

**What is wrong (against `eer-writing-style` / `eer-topic-selection` / `eer-identification`):**

- **Leads with the data and the estimator** ("matched employer–employee data… two-way fixed-effects
  regression") instead of the economic question — the named EER anti-pattern.
- **No general-interest question and no quantity on page one.** A non-specialist EER reader cannot tell
  what is being measured or why it matters beyond commuting specialists.
- **No headline estimate with units, and no uncertainty.** "Significant at the 1% level (\*\*\*)" is the
  **asterisk reporting EER house style discourages** — there is no point estimate, no standard error.
- **Naive TWFE on staggered timing**, with no acknowledgment of heterogeneity bias — exactly what a
  single-anonymized field referee will flag ([`eer-identification`](../../skills/eer-identification/SKILL.md)).
- **Throat-clearing** ("has been studied extensively") with vague stakes.
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (EER arc — general-interest question + result-with-uncertainty, contribution early)

> **When commuting gets cheaper, who captures the gain — workers, through higher wages, or firms?** Using a
> staggered expansion of regional rail, we find that gaining rail access raises local wages by **3.4%
> (s.e. 0.9)** within three years, and that roughly **two-thirds of the commuting-cost saving is passed to
> workers** rather than retained by firms. *(general-interest question + headline quantity + its uncertainty
> + why it matters, in the first breath — no asterisks.)*
>
> Measuring this is hard because rail lines are **not placed at random**: regions that get rail tend to be
> those with already-rising labor demand, so a naive wage-on-access regression conflates the commuting effect
> with the demand trend that prompted the line. *(why it is hard — the identification obstacle, stated
> plainly.)*
>
> We address this with the **staggered timing** of openings and a heterogeneity-robust difference-in-
> differences estimator (Callaway–Sant'Anna), showing **flat, precisely estimated pre-trends** in the three
> years before each opening and a dynamic post path that builds over three years. We probe the parallel-
> trends assumption with an honest-DiD sensitivity analysis and confirm the estimate against an instrumental-
> variables design using historical rail corridors. *(approach + the key identifying assumption and its
> defense, in one paragraph; [`eer-identification`](../../skills/eer-identification/SKILL.md) Branch A.)*
>
> The wage gain is **3.4% (s.e. 0.9)**, robust across leave-one-region-out samples (range 2.8–3.9%,
> illustrative) and to alternative clustering; it is concentrated among **commuters in mid-skill occupations**,
> consistent with cheaper commuting widening workers' effective labor market. *(headline result restated with
> mechanism and robustness; [`eer-robustness`](../../skills/eer-robustness/SKILL.md).)*
>
> Our contribution is a **credible, general lesson about incidence**: cheaper commuting is not just an urban-
> economics curiosity — it reallocates surplus toward workers by enlarging the set of jobs they can reach.
> Closest are A (estimates rail effects on employment but not wage incidence) and B (studies wage effects
> assuming exogenous placement); we relax placement endogeneity and recover the **incidence split** neither
> pins down. *(contribution framed as a checkable delta + portable lesson;
> [`eer-literature-positioning`](../../skills/eer-literature-positioning/SKILL.md).)* The estimand is the
> local effect on incumbent workers in receiving regions over three years; we do **not** claim it captures
> long-run general-equilibrium adjustment or transfers to settings without comparable spatial mismatch.
> Beyond rail, the result implies that **any policy lowering commuting costs shifts wage incidence toward
> workers wherever spatial mismatch binds** — relevant to transport, remote-work, and place-based policy.
> *(calibrated scope + broad lesson.)*
>
> The paper proceeds as follows. Section 2 describes the rail expansion and the data; Section 3 lays out the
> identification strategy; Section 4 reports estimates, dynamics, and robustness; Section 5 examines the
> incidence mechanism. *(brief roadmap — no over-signposting.)*

---

## Why the "after" meets the EER bar

Mapped to this pack's skill checklists:

- **First paragraph states a general-interest question + the quantity + its uncertainty** — the wage effect
  (3.4%, s.e. 0.9) appears immediately, with units and a standard error, never an asterisk
  ([`eer-writing-style`](../../skills/eer-writing-style/SKILL.md): "headline result with its uncertainty
  appears early"; "no significance asterisks in prose").
- **Breadth is legible to a non-specialist** — an incidence question (who captures the gain) that a labor,
  public, or urban economist all care about, satisfying
  ([`eer-topic-selection`](../../skills/eer-topic-selection/SKILL.md)) without being Europe-parochial.
- **Identification is credible and modern** — staggered, heterogeneity-robust DiD with flat pre-trends, an
  honest-DiD sensitivity check, and an IV confirmation, matching
  [`eer-identification`](../../skills/eer-identification/SKILL.md) Branch A and pre-empting the obvious
  field-referee objection to naive TWFE.
- **Contribution is a calibrated answer with scope, not a method** — "we recover the incidence split,"
  plus an explicit statement of what the estimand does **not** establish, satisfies
  [`eer-literature-positioning`](../../skills/eer-literature-positioning/SKILL.md) (named frontier delta +
  portable lesson).
- **Sibling check passes:** this is a broad-interest empirical result with credible identification — an
  EER paper, not a field-internal increment for a transport-economics outlet, and not chosen over JEEA /
  The Economic Journal on prestige but on fit.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified** EER papers whose
> introductions execute this arc, [`../../skills/eer-replication-package/SKILL.md`](../../skills/eer-replication-package/SKILL.md)
> for building the deposit so it meets the mandatory replication policy, and [`../code/`](../code/) for a
> runnable empirical command chain. For the venue-neutral referee objections a staggered-DiD wage-incidence
> claim must pre-empt, see
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).
