> **Illustrative teaching example.** The paper, setting, model, data, and every number below are
> **fictional** and exist only to demonstrate AEJ: Macroeconomics house style. No real-paper facts and
> no real policy are stated. Corresponding skills:
> [`aejmac-writing-style`](../../skills/aejmac-writing-style/SKILL.md),
> [`aejmac-topic-selection`](../../skills/aejmac-topic-selection/SKILL.md),
> [`aejmac-literature-positioning`](../../skills/aejmac-literature-positioning/SKILL.md),
> [`aejmac-identification`](../../skills/aejmac-identification/SKILL.md), and
> [`aejmac-theory-model`](../../skills/aejmac-theory-model/SKILL.md).

# Worked Example: An AEJ: Macro-Style Introduction (before → after)

This demonstrates the **AEJ: Macro introduction arc** from
[`aejmac-writing-style`](../../skills/aejmac-writing-style/SKILL.md):
**macro question → why it is hard → approach (identified design and/or quantitative model) → headline
quantity (with uncertainty) → mechanism → contribution & lesson → brief roadmap.**

Two AEJ: Macro house features drive the rewrite and distinguish it from a field-macro journal:

- AEJ: Macro is the AEA's **broad-interest** macro journal (one of four AEJs), sister to *AEJ: Applied*
  and below *AER* in generality. A paper must make **both** the substantive macro question **and** the
  quantitative apparatus legible to a *general* macroeconomist early
  ([`aejmac-topic-selection`](../../skills/aejmac-topic-selection/SKILL.md)).
- The **abstract is ≤100 words** — tighter than most economics journals — so the headline quantity must
  appear with no throat-clearing ([`aejmac-writing-style`](../../skills/aejmac-writing-style/SKILL.md)).

**Illustrative paper (fictional):** *"How Much Does Monetary Tightening Cost Output? High-Frequency
Evidence and a HANK Account."* Fictional design: high-frequency monetary surprises around announcements,
purged of an information effect, fed into a proxy-VAR and corroborated with local projections, then matched
to a calibrated heterogeneous-agent New Keynesian (HANK) model. Every magnitude is invented.

---

## Before (buries the question under machinery — typical first-draft intro)

> We estimate a proxy structural vector autoregression with an external instrument constructed from
> high-frequency interest-rate movements in a thirty-minute window around FOMC announcements, identified
> via a heteroskedasticity-robust two-stage projection, and we compare it to a medium-scale
> heterogeneous-agent New Keynesian model solved with the sequence-space Jacobian. Monetary transmission
> has been studied extensively. We find that the output response is statistically significant at the 1%
> level (***). Section 2 reviews the literature, Section 3 presents the data, Section 4 the VAR, Section 5
> the model, and Section 6 concludes.

**What is wrong (against `aejmac-writing-style` / `aejmac-topic-selection`):**

- **Leads with the estimator and the solver** ("proxy SVAR… external instrument… sequence-space Jacobian")
  instead of the macro question — the named anti-pattern. Method-first framing reads as a field/methods
  paper, not broad-interest AEJ: Macro.
- **No macro question and no quantity on page one.** A general macroeconomist cannot tell what is measured
  or why it matters.
- **No headline number with units or uncertainty.** "Significant at the 1% level (\*\*\*)" gives no point
  estimate, no band — the inference is carried by a star, not by a reported magnitude.
- **Throat-clearing** ("has been studied extensively") with vague stakes.
- **Contribution is machinery, not an answer**, with no lesson that travels.
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (AEJ: Macro arc — question + approach + quantity-with-uncertainty, contribution early)

> **How much output does a surprise monetary tightening cost, and through which channel?** We find that a
> 100 basis-point monetary shock lowers output by **0.6% (90% band [0.2, 1.0])** at its peak about a year
> out, and that **roughly two-thirds of the decline runs through investment** rather than consumption.
> *(macro question + headline quantity + its uncertainty + mechanism, in the first breath — the number, not
> a star, carries the claim.)*
>
> Measuring this is hard because policy moves are **partly anticipated and partly responses to the outlook**:
> a simple regression of output on the policy rate confounds the shock with the conditions that prompted it,
> and high-frequency surprises can themselves signal the central bank's private view of the economy (the
> "information effect"). *(why it is hard — the identification obstacle stated plainly.)*
>
> We resolve this with **monetary surprises measured in a tight window around announcements, purged of the
> information effect** by orthogonalizing against professional forecasts, used as an external instrument in
> a proxy-VAR and **corroborated by local projections** with the same instrument. We then ask whether a
> **calibrated HANK model**, disciplined to match the empirical distribution of marginal propensities to
> consume, reproduces the response — and what it implies for the channel. *(approach — identified design
> plus a disciplined model — in one paragraph, after the question;
> [`aejmac-identification`](../../skills/aejmac-identification/SKILL.md) Branch C and
> [`aejmac-theory-model`](../../skills/aejmac-theory-model/SKILL.md).)*
>
> The peak output response is **0.6% (90% band [0.2, 1.0])**, stable across the proxy-VAR and the
> local-projection implementations and across pre- and post-1984 samples. The HANK model, calibrated to the
> MPC distribution (a **targeted** moment) and matching the **untargeted** share of hand-to-mouth
> households, reproduces the response and attributes **two-thirds of it to investment** via the firm
> financing channel; a counterfactual with acyclical credit spreads halves the peak to **0.3% (90% band
> [0.0, 0.6])**. *(headline result restated with mechanism, robustness, and uncertainty carried into the
> counterfactual.)*
>
> Our contribution is a **quantitative answer, not an estimator**: we measure the output cost of monetary
> tightening with a credibly exogenous shock, and we show a standard HANK model reproduces it **only when
> the firm financing channel is active** — reframing monetary transmission as substantially a
> firm-side, not purely a household-side, phenomenon. *(contribution as question + quantity + lesson;
> [`aejmac-literature-positioning`](../../skills/aejmac-literature-positioning/SKILL.md).)* The estimand is
> the average response over our sample's monetary regime; we do **not** claim it holds at the effective
> lower bound, and the counterfactual assumes the calibrated parameters are policy-invariant. Beyond this
> case, the result implies that **models without a cyclical firm-financing channel will understate the cost
> of tightening** — relevant to how central banks weigh the output cost of disinflation. *(scope + broad
> lesson.)*
>
> The paper proceeds as follows. Section 2 builds the high-frequency instrument and the proxy-VAR; Section 3
> reports the empirical response and its robustness; Section 4 presents the HANK model and the channel
> decomposition; Section 5 runs the credit-spread counterfactual. *(brief roadmap — no over-signposting.)*

---

## A ≤100-word abstract for the same paper (illustrative)

> How much output does a surprise monetary tightening cost, and through which channel? Using high-frequency
> policy surprises purged of the information effect in a proxy-VAR, corroborated by local projections, we
> find a 100 basis-point shock lowers output by 0.6% (90% band [0.2, 1.0]) at its peak, two-thirds through
> investment. A heterogeneous-agent New Keynesian model calibrated to the MPC distribution reproduces the
> response only when a cyclical firm-financing channel is active; shutting it down halves the effect. The
> output cost of tightening is substantially a firm-side phenomenon. *(~95 words; one number, one
> mechanism, one lesson.)*

---

## Why the "after" meets the AEJ: Macro bar

Mapped to this pack's skill checklists:

- **First paragraph states the macro question + the quantity + its uncertainty** — the peak response
  (0.6%, 90% band [0.2, 1.0]) appears immediately, with units and a band, never carried by a star alone
  ([`aejmac-writing-style`](../../skills/aejmac-writing-style/SKILL.md)).
- **Both the substance and the apparatus are legible early** — a general reader sees the monetary-cost
  question; a quantitative reader sees the identified design and the HANK model. This is the AEJ: Macro
  sweet spot where method and answer reinforce each other
  ([`aejmac-topic-selection`](../../skills/aejmac-topic-selection/SKILL.md)).
- **Identification is named, not assumed** — the information effect is confronted and the cross-method
  agreement (proxy-VAR ↔ LP) is the credibility argument, matching
  [`aejmac-identification`](../../skills/aejmac-identification/SKILL.md) Branch C.
- **The model is disciplined** — a targeted moment (MPC distribution) plus an untargeted match
  (hand-to-mouth share) and a channel-shutdown counterfactual, per
  [`aejmac-theory-model`](../../skills/aejmac-theory-model/SKILL.md).
- **Contribution is an answer with scope** — "we measure the output cost and locate the channel," plus an
  explicit statement of what the estimand does **not** establish (the ELB; policy-invariance), satisfying
  [`aejmac-literature-positioning`](../../skills/aejmac-literature-positioning/SKILL.md).
- **Sibling check passes:** this is broad-interest macro with quantitative discipline (AEJ: Macro), not a
  field-specialist monetary paper (*J. Monetary Economics*), not a pure quantitative-dynamics methods piece
  (*RED*), and not a micro-empirical applied paper (*AEJ: Applied*).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified** AEJ: Macro
> papers whose introductions execute this arc,
> [`../../skills/aejmac-robustness/SKILL.md`](../../skills/aejmac-robustness/SKILL.md) for building the
> robustness program these claims need, and
> [`../../skills/aejmac-replication-package/SKILL.md`](../../skills/aejmac-replication-package/SKILL.md)
> for assembling the package (incl. simulation/solver code) that clears the AEA Data Editor check. For the
> venue-neutral referee objections an empirical macro claim must pre-empt, see
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).
