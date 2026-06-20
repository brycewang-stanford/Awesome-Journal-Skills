> **Illustrative teaching example.** The paper, setting, design, and every number below are **fictional**
> and exist only to demonstrate *American Economic Review: Insights* (AER: Insights) house style. No
> real-paper facts and no real policy are stated. Corresponding skills:
> [`aeri-writing-style`](../../skills/aeri-writing-style/SKILL.md),
> [`aeri-topic-selection`](../../skills/aeri-topic-selection/SKILL.md),
> [`aeri-identification`](../../skills/aeri-identification/SKILL.md), and
> [`aeri-robustness`](../../skills/aeri-robustness/SKILL.md).

# Worked Example: An AER: Insights-Style Introduction (before → after)

This demonstrates the **AER: Insights short-paper arc** from
[`aeri-writing-style`](../../skills/aeri-writing-style/SKILL.md):
**lead with the single result → why it matters / the prior it overturns → identification in one paragraph →
the one decisive caveat → (brief) roadmap.** Everything secondary is pushed to the Supplemental Appendix.

Three AER: Insights house facts drive the rewrite (检索于 2026-06；以官网为准):

- AER: Insights publishes **short, self-contained papers built around ONE important idea**. The intro must
  state the answer immediately, not build to it ([`aeri-topic-selection`](../../skills/aeri-topic-selection/SKILL.md)).
- A **hard length cap** — **≤7,000 words with no exhibits, minus 200 per exhibit, ≤5 exhibits**, abstract
  **≤100 words** — means the introduction cannot afford a literature survey, a second result, or
  method throat-clearing. Over the cap, the paper is **returned unreviewed**.
- AEA house style **forbids significance asterisks** — report **point estimates with standard errors /
  confidence sets** in the sentence ([`aeri-identification`](../../skills/aeri-identification/SKILL.md)).

**Illustrative paper (fictional):** *"Do Posted Wages Reduce the Gender Application Gap? Evidence from a
Job-Board Policy Change."* Fictional setting: an online job board that switched some occupations to
**mandatory posted wages** on a staggered schedule, with an invented application panel, analyzed by a
heterogeneity-robust difference-in-differences. Every magnitude is invented.

---

## Before (buries the single result under setup and a second result — typical first-draft intro)

> The gender gap in labor markets has been studied extensively across many literatures, including
> bargaining, sorting, and discrimination. In this paper we use data from a large online job board and
> exploit a policy change. We first describe patterns in application behavior, then we estimate the effect
> of wage posting on applications, and we additionally explore effects on offered wages and on match
> quality. Wage posting is implemented at different times across occupations. Our difference-in-differences
> estimates suggest that women's applications increase, and the effect is statistically significant
> (\*\*\*). We also find suggestive effects on the wage distribution. Section 2 reviews the large
> literature, Section 3 describes the institutional setting in detail, Section 4 presents the data,
> Section 5 the empirical strategy, Section 6 the main results, Section 7 additional results, and Section 8
> concludes.

**What is wrong (against `aeri-writing-style` / `aeri-topic-selection` / `aeri-robustness`):**

- **No result on page one.** The headline number appears nowhere in the first breath — the cardinal
  AER: Insights sin. A short-paper reader must see the answer immediately.
- **Two or three results, not one.** "Applications… offered wages… match quality" is a multi-result AER
  paper, not a single-insight AER: Insights paper ([`aeri-topic-selection`](../../skills/aeri-topic-selection/SKILL.md)).
- **Asterisk reporting** ("significant at \*\*\*") is **exactly what AEA style forbids** — no point
  estimate, no standard error.
- **A literature survey and an eight-section roadmap** the **word cap cannot afford**; this intro alone
  signals an over-cap paper.
- **Identification is invisible** — staggered timing is mentioned but not the modern estimator or the
  diagnostic that makes it credible.

---

## After (AER: Insights arc — single result first, identification in one paragraph, rest to the appendix)

> **When employers must post wages, do more women apply?** Using a job board that switched occupations to
> **mandatory posted wages** on a staggered schedule, we find that posting raises women's applications by
> **14% (s.e. 3)** relative to men's, closing about **a third of the baseline gender application gap** —
> with **no detectable change in men's applications**. *(question + the single headline number + its
> standard error + why it matters, in the first two sentences; no asterisks.)*
>
> This matters because the application gap is widely attributed to preferences or confidence, yet a simple
> **information** change — revealing the wage before applying — moves it substantially. *(the prior the
> result overturns: it is partly an information friction, not only a preference gap.)*
>
> Identification comes from the **staggered rollout** across occupations: we estimate a
> heterogeneity-robust difference-in-differences (Callaway–Sant'Anna), and the **event-study leads are flat**
> (Figure 1), so treated and not-yet-treated occupations were on parallel paths before posting began. The
> single most threatening alternative — that posting coincided with occupation-specific demand shocks — is
> ruled out by a placebo on vacancy counts; all remaining checks are in the Supplemental Appendix.
> *(identification + the one decisive diagnostic + the one decisive caveat, in a single paragraph;
> [`aeri-identification`](../../skills/aeri-identification/SKILL.md) Branch A.)*
>
> Our contribution is **one clean fact**: posted wages close a meaningful share of the gender application
> gap, and they do so by changing women's behavior, not men's. We do **not** claim posting changes who is
> hired or offered wages — those questions, and effects on match quality, are beyond this short paper and
> are taken up in the Supplemental Appendix only as descriptive context. *(single insight, calibrated
> scope; secondary results explicitly demoted — [`aeri-robustness`](../../skills/aeri-robustness/SKILL.md).)*
>
> Section 2 describes the setting and data; Section 3 presents the design and the main estimate; Section 4
> discusses the mechanism and scope. *(three-section roadmap — short paper, light signposting.)*

---

## Why the "after" meets the AER: Insights bar

Mapped to this pack's skill checklists:

- **The single result leads** — "14% (s.e. 3), about a third of the gap" is in the first two sentences,
  with a standard error and no asterisk, satisfying
  [`aeri-writing-style`](../../skills/aeri-writing-style/SKILL.md) ("first paragraph states the headline
  result with magnitude + SE/CI").
- **One idea, not three** — offered wages and match quality are explicitly removed to the Supplemental
  Appendix, satisfying [`aeri-topic-selection`](../../skills/aeri-topic-selection/SKILL.md)'s single-insight
  test and [`aeri-robustness`](../../skills/aeri-robustness/SKILL.md)'s triage rule.
- **Identification is one paragraph, with one in-text diagnostic** — flat event-study leads (Figure 1) and
  a single placebo carry the design; alternative bandwidths, windows, and clustering go to the appendix,
  matching [`aeri-identification`](../../skills/aeri-identification/SKILL.md).
- **Length discipline is visible** — no survey, no eight-section roadmap, no second result; this intro
  reads like a paper that will clear the **7,000-word (minus exhibits) cap**, where the "before" signals an
  over-cap return.
- **Sibling check passes:** this is **not** a multi-result flagship paper (*AER*), **not** a field-specific
  full paper (*AEJ: Applied*), and **not** a long-form QJE paper — it is **one general-interest fact,
  short** — AER: Insights's identity.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified** AER: Insights
> papers whose introductions execute this single-result arc,
> [`../../skills/aeri-replication-package/SKILL.md`](../../skills/aeri-replication-package/SKILL.md) for
> building the deposit so it clears the AEA Data Editor check, and [`../code/`](../code/) for a runnable
> empirical command chain. For the venue-neutral referee objections a staggered-DiD claim must pre-empt —
> critical here because AER: Insights has **no R&R** — see
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).
