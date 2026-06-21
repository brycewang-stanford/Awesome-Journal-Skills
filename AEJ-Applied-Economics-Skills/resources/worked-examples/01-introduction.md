> **Illustrative teaching example.** The paper, setting, policy, and every number below are **fictional**
> and exist only to demonstrate American Economic Journal: Applied Economics (AEJ: Applied) house style. No
> real-paper facts and no real policy are stated. Corresponding skills:
> [`aeja-writing-style`](../../skills/aeja-writing-style/SKILL.md),
> [`aeja-topic-selection`](../../skills/aeja-topic-selection/SKILL.md),
> [`aeja-literature-positioning`](../../skills/aeja-literature-positioning/SKILL.md), and
> [`aeja-identification`](../../skills/aeja-identification/SKILL.md).

# Worked Example: An AEJ: Applied Introduction (before → after)

This demonstrates the **AEJ: Applied introduction arc** from
[`aeja-writing-style`](../../skills/aeja-writing-style/SKILL.md):
**question → why credible identification is hard → the design that solves it → headline causal estimate
(with a standard error) → mechanism → policy/economic lesson → brief roadmap.**

Two AEJ: Applied house rules drive the rewrite and distinguish it from a field-internal note or an AER
agenda paper:

- AEJ: Applied is the AEA's **empirical applied-microeconomics** journal — the contribution is a
  **credibly identified answer to a substantive question of broad applied-micro interest**, not a policy
  verdict (AEJ: Economic Policy) and not a general-interest agenda swing (AER)
  ([`aeja-topic-selection`](../../skills/aeja-topic-selection/SKILL.md)).
- The **identification is the star**: name the design plainly and put the headline estimate, with units and
  a standard error, in the first breath
  ([`aeja-writing-style`](../../skills/aeja-writing-style/SKILL.md),
  [`aeja-identification`](../../skills/aeja-identification/SKILL.md)). AEA permits significance stars but
  expects standard errors — so the magnitude and its SE live in the sentences.

**Illustrative paper (fictional):** *"Free Bus Passes and Teen Employment: Evidence from a Staggered
Municipal Rollout."* Fictional setting: a transit authority gives free bus passes to high-schoolers,
phased across invented municipalities over several years; the paper estimates the effect on teen
employment using a heterogeneity-robust difference-in-differences design on invented administrative data.
Every magnitude is invented.

---

## Before (buries the question; leans on TWFE; reports only stars)

> We study public transit and youth labor markets, a topic of longstanding interest. Using a panel of
> municipalities, we estimate a two-way fixed-effects regression of teen employment on an indicator for
> whether a free-bus-pass program is in place, controlling for municipality and year fixed effects and a
> vector of covariates. The literature on transportation and employment is extensive. We find that the
> program has a positive and statistically significant effect on teen employment (significant at the 1%
> level). Section 2 reviews the literature, Section 3 describes the data, Section 4 presents the
> specification, Section 5 the results, and Section 6 concludes.

**What is wrong (against `aeja-writing-style` / `aeja-topic-selection` / `aeja-identification`):**

- **No economic question and no magnitude on page one.** A broad applied-micro reader cannot tell what is
  being measured or how big it is — only that something is "significant."
- **Leads with the estimator and a wall of controls** instead of the design that makes the estimate
  credible. "Two-way fixed effects" on a **staggered rollout** is exactly the setup AEJ: Applied referees
  flag for negative-weighting bias ([`aeja-identification`](../../skills/aeja-identification/SKILL.md)
  Path B).
- **Stars without standard errors or a magnitude.** "Significant at the 1% level" carries no point
  estimate, no units, no SE — AEA expects the SE and the number.
- **Throat-clearing** ("longstanding interest," "the literature is extensive") with vague stakes and no
  contribution sentence.
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (AEJ: Applied arc — question + credible design + estimate-with-uncertainty, contribution early)

> **Does cheap transportation help teenagers find work?** Using a staggered municipal rollout of free high-
> school bus passes, we find that the program **raised teen employment by 3.1 percentage points (s.e. 0.9)**
> — a 7% increase off a baseline employment rate of 44% — concentrated among teens living far from the job
> centers their town's transit network connects to. *(question + headline causal estimate + its uncertainty
> + who it moves, in the first breath.)*
>
> Estimating this is hard because towns that adopt transit subsidies differ from those that do not, and a
> naive comparison conflates the program with the local economies that chose it. *(why credible
> identification is hard — selection into adoption.)* Because the passes were phased in across
> municipalities over several years, we use a **difference-in-differences design with staggered timing**,
> estimated with a heterogeneity-robust estimator (Callaway–Sant'Anna) rather than two-way fixed effects,
> which would mix in **contaminating comparisons** between newly treated and already-treated towns. We show
> **flat pre-trend leads**, report a Goodman-Bacon decomposition, and bound the estimate under a plausible
> violation of parallel trends. *(the design that solves it, named plainly;
> [`aeja-identification`](../../skills/aeja-identification/SKILL.md) Path B.)*
>
> The 3.1-point effect (s.e. 0.9) is stable across alternative samples, clustering at the municipality level
> with a wild-cluster bootstrap given the modest number of treated towns, and an honest-DID bound keeps the
> effect positive under pre-trend violations up to the largest observed pre-period deviation. *(robustness
> and inference matched to the design;
> [`aeja-robustness`](../../skills/aeja-robustness/SKILL.md).)* The employment gain is largest for teens in
> transit deserts and near zero where job centers were already walkable, pointing to **reduced commuting
> cost**, not income effects, as the mechanism. *(mechanism that distinguishes channels.)*
>
> Our contribution is a **credibly identified magnitude for a policy lever many cities can pull**: we show
> that a low-cost transit subsidy moves teen employment, and that the effect operates through access rather
> than income. This is the **local average effect for marginal teens in transit-poor neighborhoods**; we do
> **not** claim it transfers to dense cities with universal transit, and the estimate is an intent-to-treat
> effect of program availability. *(contribution as question + magnitude + lesson, with a calibrated scope;
> [`aeja-literature-positioning`](../../skills/aeja-literature-positioning/SKILL.md).)* Beyond this setting,
> the result suggests that **commuting frictions are a binding constraint on youth employment**, relevant to
> the design of school-to-work and transit policy. *(broad applied-micro lesson.)*
>
> The paper proceeds as follows. Section 2 describes the rollout and data; Section 3 lays out the design and
> pre-trend evidence; Section 4 reports the main estimate, robustness, and heterogeneity; Section 5 examines
> the access mechanism. *(brief roadmap — no over-signposting.)*

---

## Why the "after" meets the AEJ: Applied bar

Mapped to this pack's skill checklists:

- **First paragraph states the question + the causal magnitude + its uncertainty** — the 3.1pp effect
  (s.e. 0.9) appears immediately, with units and a standard error, never a bare asterisk
  ([`aeja-writing-style`](../../skills/aeja-writing-style/SKILL.md): "Intro ¶1 gives the economic question
  and the headline number with uncertainty").
- **The identification is named and defended before the machinery** — staggered DID, heterogeneity-robust
  estimator, flat leads, Bacon decomposition, honest-DID bound — matching
  [`aeja-identification`](../../skills/aeja-identification/SKILL.md) Path B and pre-empting the modal AEJ:
  Applied referee objection.
- **Inference matches the design** — clustering at the municipality level with a wild-cluster bootstrap for
  few clusters ([`aeja-robustness`](../../skills/aeja-robustness/SKILL.md)).
- **Contribution is an answer with calibrated scope, not a method** — "a credibly identified magnitude for a
  policy lever," plus an explicit statement that it is a local ITT effect that need not transfer, satisfies
  [`aeja-literature-positioning`](../../skills/aeja-literature-positioning/SKILL.md) and
  [`aeja-topic-selection`](../../skills/aeja-topic-selection/SKILL.md).
- **Mechanism distinguishes channels** — access vs. income — which is what turns a coefficient into an
  economic finding.
- **Sibling check passes:** this is method/identification-driven applied micro (AEJ: Applied), not a
  general-interest agenda paper (AER) and not a program-ROI policy verdict (AEJ: Economic Policy).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified** AEJ: Applied
> papers whose introductions execute this arc,
> [`../../skills/aeja-replication-package/SKILL.md`](../../skills/aeja-replication-package/SKILL.md) for
> building the analysis so it clears the AEA Data Editor reproducibility check, and
> [`../code/`](../code/) for a runnable empirical command chain. For the venue-neutral referee objections a
> staggered-DID claim must pre-empt, see
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).
