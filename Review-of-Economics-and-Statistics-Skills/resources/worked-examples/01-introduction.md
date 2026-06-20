> **Illustrative teaching example.** The paper, setting, design, and every number below are **fictional**
> and exist only to demonstrate The Review of Economics and Statistics (REStat) house style. No real-paper
> facts and no real policy are stated. Corresponding skills:
> [`restat-writing-style`](../../skills/restat-writing-style/SKILL.md),
> [`restat-topic-selection`](../../skills/restat-topic-selection/SKILL.md),
> [`restat-literature-positioning`](../../skills/restat-literature-positioning/SKILL.md), and
> [`restat-identification`](../../skills/restat-identification/SKILL.md).

# Worked Example: A REStat-Style Introduction (before → after)

This demonstrates the **REStat introduction arc** from
[`restat-writing-style`](../../skills/restat-writing-style/SKILL.md):
**applied question → why prior estimates are unreliable → approach (data + design + measurement credibility)
→ headline estimate (with a standard error) → contribution as a named delta → brief roadmap.**

Two REStat house traits drive the rewrite and distinguish it from a methods journal:

- REStat is **empirical-first applied economics with a measurement tradition**, sister in spirit to
  AEJ: Applied but weighting **measurement and applied econometrics** more heavily, and unlike
  *J. Econometrics* it wants the **application**, not a new estimator, to be the contribution
  ([`restat-topic-selection`](../../skills/restat-topic-selection/SKILL.md)).
- REStat uses **standard economics house style** — report **standard errors** (stars permitted but never
  instead of the SE) — and the **abstract is ≤100 words**
  ([`restat-writing-style`](../../skills/restat-writing-style/SKILL.md)).

**Illustrative paper (fictional):** *"Broadband Expansion and Small-Business Formation: Evidence from a
Staggered Rural Rollout."* Fictional setting: a state subsidy that extended high-speed internet to rural
counties on a staggered timeline, estimated with a heterogeneity-robust difference-in-differences design on
invented county–year business-registration data, with a measurement-error correction for the noisy rollout
date. Every magnitude is invented.

---

## Before (buries the question under machinery — typical first-draft intro)

> We use a two-way fixed effects regression of new business registrations on a broadband-access dummy with
> county and year fixed effects, clustering at the county level. Broadband and entrepreneurship have been
> studied extensively. We construct a panel and run our regressions. The coefficient on broadband is
> positive and significant at the 1% level (\*\*\*). Section 2 reviews the literature, Section 3 describes
> the data, Section 4 presents the empirical model, Section 5 the results, and Section 6 concludes.

**What is wrong (against `restat-writing-style` / `restat-topic-selection` / `restat-literature-positioning`):**

- **Leads with the estimator** ("two-way fixed effects regression… clustering at the county level") instead
  of the economic question — the named REStat anti-pattern (method-first framing reads like a methods paper).
- **No applied question and no quantity on page one.** A reader cannot tell what is being measured or why
  it matters for an applied audience.
- **No headline estimate with units, and no standard error.** "Significant at the 1% level (\*\*\*)" gives
  stars with **no point estimate and no SE** — the opposite of REStat house style.
- **Throat-clearing** ("has been studied extensively") with vague stakes.
- **TWFE on a staggered rollout** with no acknowledgment of heterogeneity bias — a REStat referee's first
  objection.
- **No measurement awareness** — the rollout date is treated as exact when it is plainly noisy.
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (REStat arc — question + design + measurement + estimate-with-SE, contribution early)

> **When high-speed internet reaches a rural county, how many new small businesses does it create — and is
> the effect real or an artifact of where broadband went first?** Using a staggered rural broadband subsidy,
> we estimate that gaining access raises new business registrations by **8.1 per 10,000 residents per year
> (s.e. 1.4)**, a **14% increase** over the rural baseline. *(question + headline quantity + its standard
> error + why it matters, in the first breath — the number, not a star.)*
>
> Estimating this credibly is hard for two reasons prior work did not fully resolve. First, broadband did
> **not arrive randomly**: counties with more latent entrepreneurship may have been wired earlier, so a
> simple before–after comparison conflates the effect with selection. Second, the **rollout date is measured
> with error** — administrative "service-available" dates lag actual usable access — which attenuates any
> naive estimate toward zero. *(why it is hard — both an identification obstacle and a measurement obstacle,
> the REStat signature.)*
>
> We address the first with a **heterogeneity-robust difference-in-differences** design (Callaway–Sant'Anna)
> that uses the staggered timing and avoids the bias of two-way fixed effects under heterogeneous treatment
> timing; flat pre-trends across event-time leads support the parallel-trends assumption. We address the
> second by validating the administrative date against a subsample of **independently observed** first-usage
> dates and applying an attenuation correction, which moves the estimate from 6.0 to **8.1** (s.e. 1.4).
> *(approach — design + measurement credibility in one paragraph;
> [`restat-identification`](../../skills/restat-identification/SKILL.md) Branches A and D.)*
>
> The effect is **8.1 per 10,000 (s.e. 1.4)**, concentrated in counties with a pre-existing supplier base,
> survives leave-one-cohort-out and alternative bandwidths, and is robust to wild-cluster-bootstrap inference
> with few treated cohorts. A back-of-envelope calculation implies the subsidy's cost per new business is
> well below comparable rural programs. *(result restated with heterogeneity, robustness, and honest
> inference — [`restat-robustness`](../../skills/restat-robustness/SKILL.md).)*
>
> Our contribution is a **credibly identified and correctly measured** estimate of broadband's effect on
> rural firm entry. Relative to the closest prior work, which used TWFE on a coarser access measure and
> found near-zero effects, we show that **both** the heterogeneity-robust estimator **and** the
> measurement-error correction matter: each alone leaves the effect understated, and together they reconcile
> the earlier null with a positive effect. *(contribution as a delta against named work that also reconciles
> a prior puzzle; [`restat-literature-positioning`](../../skills/restat-literature-positioning/SKILL.md).)*
> The estimand is the average effect on treated rural counties over this period; we do **not** claim it
> transfers to urban markets or to fiber technologies our data do not cover.
>
> The paper proceeds as follows. Section 2 describes the rollout, the data, and the validation of the access
> measure; Section 3 sets out the design; Section 4 reports estimates, heterogeneity, and robustness;
> Section 5 discusses cost-effectiveness. *(brief roadmap — no over-signposting.)*

---

## Why the "after" meets the REStat bar

Mapped to this pack's skill checklists:

- **First paragraph states the applied question + the estimate + its standard error** — 8.1 per 10,000
  (s.e. 1.4) appears immediately, with units and an SE, never a bare star
  ([`restat-writing-style`](../../skills/restat-writing-style/SKILL.md): "first paragraph states the applied
  question + the headline estimate (units + SE)").
- **Both identification and measurement are made credible** — the het-robust estimator handles staggered
  timing and the attenuation correction handles the noisy rollout date, matching
  [`restat-identification`](../../skills/restat-identification/SKILL.md) Branches A (DID) and D (measurement).
  This measurement awareness is what most distinguishes a REStat intro from a generic applied-micro one.
- **Contribution is an applied answer with scope, not a method** — "a credibly identified and correctly
  measured estimate," plus what the estimand does **not** claim, satisfies
  [`restat-literature-positioning`](../../skills/restat-literature-positioning/SKILL.md) (delta vs named
  work; reconciliation of a prior null; bounded scope).
- **House style respected** — the result is communicated through a point estimate and a standard error, not
  an asterisk standing alone ([`restat-writing-style`](../../skills/restat-writing-style/SKILL.md)).
- **Sibling check passes:** this is not a new estimator with a toy application (*J. Econometrics*) and not a
  general-interest agenda-setting piece (AER); it is a credibly identified, carefully measured applied
  estimate — REStat's identity.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified** REStat papers
> whose designs execute this arc,
> [`../../skills/restat-replication-package/SKILL.md`](../../skills/restat-replication-package/SKILL.md) for
> building the analysis so it clears the Harvard Dataverse data/code deposit, and
> [`../code/`](../code/) for a runnable empirical command chain. For the venue-neutral referee objections a
> staggered-DID claim must pre-empt, see
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).
