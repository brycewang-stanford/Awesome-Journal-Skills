> **Illustrative teaching example.** The paper, setting, and every number below are **fictional** and
> exist only to demonstrate *Journal of Economic Growth* house style. No real-paper facts are stated, and
> no real policy is invoked. Corresponding skills:
> [`jeg-writing-style`](../../skills/jeg-writing-style/SKILL.md),
> [`jeg-topic-selection`](../../skills/jeg-topic-selection/SKILL.md),
> [`jeg-contribution-framing`](../../skills/jeg-contribution-framing/SKILL.md), and
> [`jeg-identification-strategy`](../../skills/jeg-identification-strategy/SKILL.md).

# Worked Example: A *JEG*-Style Introduction (before → after)

This demonstrates the introduction arc the *Journal of Economic Growth* rewards (from `jeg-writing-style`
and `jeg-topic-selection`): **first-order growth question → why it matters for the deep determinants of
development → data & identification (or, for theory, the quantitative target) → headline estimate with
magnitude and interval → what it identifies and against which rival → contribution to growth knowledge →
brief roadmap.** The governing rule from `jeg-writing-style` is **lead with the economic question and the
headline number, demote the method to a tool**, and write for a reader who cares about long-run growth
broadly, not only your sub-literature.

**Illustrative paper (fictional):** *"Printing Presses and the Take-Off: Early Information Technology and
Long-Run Growth Across European Regions, 1480–1700."* Fictional setting: a panel of fictional European
regions with reconstructed output and book-production data; "early adopter" means a region that hosted a
press within 25 years of the technology's fictional 1470 arrival.

---

## Before (buries the contribution — typical first-draft intro)

> The relationship between technology and growth has been studied extensively in economics, economic
> history, and other disciplines. Many factors have been associated with long-run development, including
> institutions, geography, human capital, and culture. In this paper, we assemble a regional panel and run
> two-stage least squares regressions, using distance to the technology's origin as an instrument, to study
> the effect of early printing on growth. We estimate a series of specifications and present the results.
> Understanding the deep roots of growth is important. Section 2 reviews the literature, Section 3 describes
> the data, Section 4 presents the methods, Section 5 reports results, and Section 6 concludes.

**What's wrong (against `jeg-writing-style` / `jeg-topic-selection` / `jeg-contribution-framing`):**

- **Leads with method** ("we assemble a panel and run two-stage least squares") instead of the growth
  question — the named anti-pattern in `jeg-writing-style`.
- **No growth question and no answer on page one.** A reader cannot tell what the long-run magnitude is, or
  why it matters for the deep determinants of development (fails the `jeg-topic-selection` first-order test).
- **No headline estimate with magnitude or uncertainty** — violates the estimate-first norm.
- **Identification is asserted, not motivated.** "Distance as an instrument" appears with no exclusion
  argument and no rival named (the `jeg-identification-strategy` gap).
- **Contribution type is unclear** — is this a new estimate, a new measure, a mechanism, a theory match?
  (the `jeg-contribution-framing` test).
- **Throat-clearing** ("studied extensively," "is important") and an **over-signposted roadmap**.

---

## After (*JEG* arc — growth question + estimate + identification, contribution early)

> **Did the first information-technology revolution leave a permanent mark on growth — and how large, two
> centuries on?** We estimate that European regions that adopted the printing press within a generation of
> its arrival were **growing 0.34 log points per century faster by 1700 (95% CI 0.21–0.47)**, an advantage
> equivalent to roughly a fifth of the cross-regional output gap that had opened by the eve of
> industrialization. *(First-order growth question + headline estimate with magnitude and interval, in the
> first breath.)*
>
> Identifying this effect is hard because presses did not locate at random: commercially dynamic regions
> were both more likely to host an early press and more likely to grow for unrelated reasons, so a raw
> adopter–non-adopter gap conflates the technology with the prosperity that attracted it. *(Why it is hard —
> the identification problem stated in growth terms, per `jeg-identification-strategy`.)*
>
> We address this with a panel of fictional European regions, 1480–1700, instrumenting early adoption with a
> region's **least-cost transport distance to the technology's point of origin**, conditional on
> pre-1470 output, latitude, and market access. The exclusion restriction is that, conditional on these
> controls, proximity to the origin affected later growth *only* through earlier press adoption; we probe it
> with placebo "presses" dated before the technology existed and with pre-trend tests on 1480–1500 growth.
> *(Data and identification in one paragraph; the instrument is *defended*, not merely named — per
> `jeg-identification-strategy` / `jeg-data-analysis`.)*
>
> The growth advantage is **concentrated in regions that also had high baseline literacy and weakens to
> statistical insignificance where literacy was low**, and it does *not* appear in the 1480–1500 placebo
> window. *(Headline result restated with the mechanism signature — the heterogeneity that distinguishes the
> technology channel from a generic prosperity story.)*
>
> Our contribution is to show that this episode is **a human-capital-complementary technology shock with a
> durable growth payoff — not a transient level effect, and not merely prosperity selecting into adoption**,
> the two readings a naïve cross-section would support. This places early information technology among the
> deep, complementarity-driven determinants of long-run divergence. *(Contribution stated early and against
> the specific rival, per `jeg-contribution-framing`.)* The result is **portable**: the
> instrument-plus-placebo design travels to any setting where a general-purpose technology diffuses from a
> point of origin and one fears that adoption is endogenous to local dynamism. *(Portability — the
> growth-knowledge payoff beyond the setting.)*
>
> The paper proceeds as follows. Section 2 places the result among the deep-determinants and unified-growth
> literatures and describes the data; Section 3 develops the instrument and the placebo/pre-trend tests;
> Section 4 reports the estimates, the literacy-complementarity heterogeneity, and robustness. *(Brief
> roadmap — no over-signposting.)*

---

## Why the "after" meets the *JEG* bar

Mapped to the skill checklists:

- **Contribution front-loaded** — by the end of the first paragraph the reader has the growth question, the
  headline magnitude with a 95% interval, and what it identifies (`jeg-writing-style`: lead with the
  economic question and the number).
- **Estimate-first prose** — the headline (0.34 log points/century; 95% CI 0.21–0.47) leads with magnitude
  **and uncertainty**, then is interpreted, rather than "the regression shows…" (`jeg-data-analysis`: report
  intervals, not bare point estimates).
- **First-order, reads past the sub-field** — pitched as a deep-determinant-of-divergence question a growth
  economist outside economic history cares about, satisfying the `jeg-topic-selection` first-order test.
- **Identification is motivated and defended** — the endogeneity of adoption is stated, the exclusion
  restriction is articulated, and it is stress-tested with placebos and pre-trends (the
  `jeg-identification-strategy` standard), not asserted.
- **The strongest rival is named and adjudicated** — "prosperity selects into adoption" would imply a
  pre-1470 growth advantage and no literacy interaction; the data show the opposite (`jeg-identification-strategy`
  adjudication test: "if the rival were true… instead it looks like ___").
- **Contribution type is explicit** — a **new causal estimate with a mechanism** (human-capital
  complementarity), the exact move `jeg-contribution-framing` calls turning "a paper about X" into "the
  first result that Y."
- **Method is demoted to a tool** — 2SLS appears only where the design is described, never as the lead
  (avoids the `jeg-writing-style` "leading with the method" anti-pattern).

> Next: adapt the reproducible analysis skeleton in [`../code/`](../code/) when turning this introduction arc
> into a full empirical workflow, and pressure-test the design against
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).
