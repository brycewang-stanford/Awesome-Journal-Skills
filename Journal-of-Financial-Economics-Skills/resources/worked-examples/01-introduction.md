> **Illustrative teaching example.** The paper, setting, regulation, and every number below are
> **fictional** and exist only to demonstrate JFE house style. No real-paper facts are stated, and no JFE
> policy is invented. Corresponding skills:
> [`jfe-writing-style`](../../skills/jfe-writing-style/SKILL.md),
> [`jfe-topic-selection`](../../skills/jfe-topic-selection/SKILL.md),
> [`jfe-literature-positioning`](../../skills/jfe-literature-positioning/SKILL.md), and
> [`jfe-identification`](../../skills/jfe-identification/SKILL.md).

# Worked Example: A JFE-Style Introduction (before → after)

This demonstrates the **JFE introduction arc** from `jfe-writing-style`, in order:

1. **the question** and why it matters — first paragraph;
2. **what you do** — setting, design, data, concretely;
3. **what you find** — headline result with direction and magnitude;
4. **why it is credible** — one or two sentences on identification/inference;
5. **the contribution** — explicit, relative to the closest work;
6. a short, optional roadmap.

It also applies the JFE-specific rules those skills state: **lead with results, not a literature tour**;
**calibrate verbs to evidence** (reserve "shows," never "proves"); **state economic magnitudes in
interpretable units**; and make the **contribution unmissable on the first page**.

**Illustrative paper (fictional):** *"Covenants and the Quiet Boardroom: Evidence from a Staggered
Disclosure Mandate."* Fictional setting: a securities regulator that, in different years, phased in a rule
forcing firms above a registration threshold to disclose private-loan covenant terms.

---

## Before (buries the contribution — typical first-draft intro)

> The relationship between debt and corporate governance has been studied extensively in the finance
> literature. Many papers examine creditors, covenants, and managerial behavior. In this paper, we use a
> staggered difference-in-differences design with two-way fixed effects to study the effect of a
> covenant-disclosure mandate on firm investment. We assemble a panel of firms and run event-study
> regressions. We find statistically significant effects (t = 3.1). Our results prove that disclosure
> disciplines managers. Understanding governance is important for regulators and investors. Section 2
> reviews the literature, Section 3 describes the data, Section 4 presents the empirical strategy, Section
> 5 reports results, and Section 6 concludes.

**What's wrong (against `jfe-writing-style`, `jfe-topic-selection`, `jfe-identification`):**

- **Leads with method** ("we use a staggered difference-in-differences design") and a literature tour
  instead of the question — `jfe-writing-style` says lead with results, not a literature tour.
- **No economic question and no answer on page one;** no contribution sentence — a JFE referee "cannot
  tell what the contribution is."
- **Reports significance (t = 3.1) with no economic magnitude** — a named anti-pattern in both
  `jfe-writing-style` and `jfe-empirical-design`.
- **"Our results prove that…"** — overclaiming, which `jfe-writing-style` says JFE referees recoil at.
- **Two-way FE on a staggered mandate with no acknowledgment of the heterogeneous-treatment-effects
  bias** — the headline `jfe-identification` anti-pattern.
- **Credibility of the design is never argued** (parallel trends, exogeneity of the rollout).
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (JFE arc — question → what → finding → credibility → contribution, on page one)

> **Does forcing firms to disclose the fine print of their private loans change how their managers
> invest?** We show that a mandate requiring public disclosure of loan-covenant terms is **consistent
> with** creditors exercising tighter control: in the three years after a firm becomes subject to the
> rule, its capital expenditure falls by **8.5% relative to the pre-mandate mean**, concentrated in firms
> that were close to a covenant threshold. *(question + headline answer in interpretable units, in the
> first breath; verb calibrated to evidence.)*
>
> Answering this cleanly is hard because disclosure rules are not imposed at random: regulators tighten
> them precisely when corporate borrowing looks risky, so a naive before-after comparison conflates the
> rule with the credit conditions that prompted it. *(why it is credible begins with naming the
> endogeneity problem — `jfe-identification`.)*
>
> We exploit a securities-disclosure mandate that was phased in across **registration-size cohorts in
> different years**, for administrative reasons unrelated to any individual firm's investment trajectory.
> The staggered timing lets us compare newly-covered firms to not-yet-covered firms; because adoption is
> staggered, we estimate the effect with a heterogeneity-robust difference-in-differences estimator and
> report a Goodman-Bacon decomposition, and we show the event study has flat pre-trends and no
> anticipation. *(what we do + why it is credible: the design, the modern estimator, and the
> identification checks `jfe-identification` requires for staggered adoption.)*
>
> Investment falls by **8.5%** off the pre-mandate mean, the effect grows over the three post-mandate
> years and is absent before, and it is concentrated in firms near a covenant threshold — the margin
> where creditor control bites. Standard errors are clustered at the cohort level, the level at which the
> mandate is assigned. *(finding restated with the cross-sectional pattern that points to the mechanism;
> inference matched to treatment assignment, per `jfe-empirical-design`.)*
>
> Our contribution is to identify **disclosure, not the covenant itself**, as a margin through which
> creditor governance operates: the rule changes no contract term, yet it moves real investment by making
> existing terms observable and therefore enforceable by the market. This sharpens the closest prior work
> — which establishes that covenant *violations* transfer control to creditors, but stops at the
> contracting stage — by showing that *disclosure* of the terms is itself a governance channel. *(the
> contribution, explicit and stated relative to where the closest paper stops — `jfe-literature-positioning`.)*
>
> The paper proceeds as follows. Section 2 describes the mandate and data; Section 3 presents the design
> and the main results; Section 4 examines the covenant-threshold mechanism and robustness. *(brief
> roadmap — no over-signposting.)*

---

## Why the "after" meets the JFE bar

Mapped to the skill checklists:

- **First page does question → what → finding → credibility → contribution** — the
  `jfe-writing-style` introduction arc, with the headline magnitude (−8.5% capex) stated **in
  interpretable units**, not as a t-statistic.
- **Verbs are calibrated to evidence** — "is consistent with," "we show"; **no "proves"** (the original's
  overclaim is removed), per `jfe-writing-style`.
- **The staggered-adoption bias is handled, not ignored** — a heterogeneity-robust estimator plus a
  Goodman-Bacon decomposition, flat pre-trends, and no anticipation, exactly what
  `jfe-identification` Branch A requires; standard errors are clustered at the **treatment-assignment
  level** (`jfe-empirical-design`).
- **The contribution is explicit on page one and stated relative to the closest paper's stopping point**
  ("disclosure, not the covenant itself"), not a vague "we extend the literature" — the
  `jfe-literature-positioning` differentiation test.
- **Method is demoted to a tool**, introduced only where the design is discussed, never as the lead
  (avoids `jfe-writing-style`'s "leading with the estimator" / literature-tour anti-pattern).
- **The one-sentence contribution is fillable** in the `jfe-topic-selection` gap/move/finding/why frame:
  *gap* — prior work stops at covenant violation; *move* — a staggered disclosure mandate; *finding* —
  capex falls 8.5%; *why* — disclosure is itself a creditor-governance channel.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified JFE papers**
> whose designs this example imitates (Schwert 1996 event study; Yermack 1996 governance), and
> [`../code/`](../code/) for the staggered-DID command chain (`03_did_modern.do`) and clustered-inference
> templates referenced above. Confirm submission and data-sharing policy in
> [`../official-source-map.md`](../official-source-map.md).
