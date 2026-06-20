> **Illustrative teaching example.** The paper, setting, and every number below are **fictional**
> and exist only to demonstrate The Economic Journal (EJ) house style. No real-paper facts and no
> real policy are stated. Corresponding skills:
> [`ecj-writing-style`](../../skills/ecj-writing-style/SKILL.md),
> [`ecj-topic-selection`](../../skills/ecj-topic-selection/SKILL.md),
> [`ecj-literature-positioning`](../../skills/ecj-literature-positioning/SKILL.md), and
> [`ecj-identification`](../../skills/ecj-identification/SKILL.md).

# Worked Example: An EJ-Style Introduction (before → after)

This demonstrates the **EJ introduction arc** from
[`ecj-literature-positioning`](../../skills/ecj-literature-positioning/SKILL.md):
**question (why a generalist cares) → what we know → the gap → approach (identification + mechanism)
→ headline result (with a standard error) → broad portable lesson → brief roadmap.**

Two EJ house traits drive the rewrite and distinguish it from a niche field-journal intro:

- EJ is the **Royal Economic Society's** general-interest flagship (founded 1891, published by OUP).
  Its bar is a **substantial contribution of broad interest to economists at large** — the intro
  must make a *generalist* economist, not only the subfield, want to read on
  ([`ecj-topic-selection`](../../skills/ecj-topic-selection/SKILL.md)).
- EJ **values clear exposition as part of the contribution** — the economics is stated in plain
  words before the machinery, and the headline result appears early with a magnitude and a standard
  error ([`ecj-writing-style`](../../skills/ecj-writing-style/SKILL.md)).

**Illustrative paper (fictional):** *"Commuting Time and the Take-Up of Local Public Services:
Evidence from a Bus-Network Reform."* Fictional setting: a mid-size city restructures its bus
network, sharply cutting travel time to public clinics for some neighborhoods and not others; the
paper estimates the effect on clinic take-up using the staggered rollout. Every magnitude is
invented.

---

## Before (buries the question; written for the subfield — typical first-draft intro)

> We estimate a two-way fixed-effects regression of clinic visits on a post-reform indicator
> interacted with treated neighborhoods, controlling for neighborhood and month fixed effects. The
> transport-accessibility literature is large. Using administrative panel data we find a coefficient
> of 0.18 (significant at the 1% level, ***). Identification comes from the staggered rollout. The
> effect is robust to alternative controls. Section 2 reviews the literature, Section 3 describes the
> data, Section 4 the empirical strategy, Section 5 the results, and Section 6 concludes.

**What is wrong (against `ecj-writing-style` / `ecj-topic-selection` / `ecj-literature-positioning`):**

- **Leads with the estimator** ("two-way fixed-effects regression… interacted…") instead of the
  economic question — the named EJ anti-pattern (method-first writing the reader must decode).
- **No broad-interest hook.** A generalist cannot tell why this matters beyond one city's buses;
  EJ's defining bar — broad relevance — is never argued.
- **Reports stars, not economics.** "0.18 (***)" has no units, no magnitude relative to a baseline,
  and no standard error a reader can use; `ecj-tables-figures` and `ecj-identification` want the
  magnitude and its uncertainty in the sentence.
- **Staggered TWFE asserted as identification** with no mention of heterogeneity-bias — exactly the
  [`ecj-identification`](../../skills/ecj-identification/SKILL.md) Branch A red flag.
- **No mechanism.** Why does travel time change take-up? Search/time-cost? Information? The "why"
  that travels across settings is missing.
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (EJ arc — broad question + mechanism + identified magnitude with uncertainty, exposition-first)

> **Do small frictions in getting somewhere keep people from using public services they are entitled
> to?** When a city reorganized its bus network, the door-to-clinic travel time fell by about 12
> minutes for some neighborhoods and was unchanged for others. We use that staggered change to show
> that **a 10-minute cut in travel time raised clinic take-up by 4.6 percentage points (s.e. 1.1)**,
> a 14% increase on a base take-up rate of 33% — evidence that **time cost, not just price, rations
> access to public services.** *(broad question + headline magnitude + its uncertainty + why it
> matters, in the first breath — no asterisks; legible to a generalist.)*
>
> This matters beyond transport policy. A large literature treats the take-up of public programs as
> driven by eligibility, price, and information; far less is known about whether the **time and
> hassle of physically reaching a service** is a first-order barrier — even though, if it is, the
> same benefit can reach very different populations depending on where it is delivered. *(what we
> know + the gap, argued for a general audience, not a subfield;
> [`ecj-literature-positioning`](../../skills/ecj-literature-positioning/SKILL.md).)*
>
> Identifying this is hard because neighborhoods that get better transit are rarely comparable to
> those that do not. We exploit the **staggered rollout** of the network reform and, because
> treatment timing varies across neighborhoods, estimate the effect with a **heterogeneity-robust
> difference-in-differences estimator** rather than two-way fixed effects, which would mix together
> effects from different cohorts. Event-study leads are flat, a placebo on pre-reform timing is null,
> and the result survives dropping each district in turn. *(approach — identification stated in
> plain words, with the modern-estimator choice justified;
> [`ecj-identification`](../../skills/ecj-identification/SKILL.md) Branch A.)*
>
> The mechanism is **time cost, not information**: the effect is concentrated among households far
> from a clinic and with young children (for whom a trip is most costly), is absent where travel
> time did not change, and does not move a placebo outcome (library visits) that the reform also made
> easier to reach but that carries no eligibility. A rival "the buses also spread information" story
> cannot explain why only the time-cost-sensitive groups respond. *(mechanism discrimination, the
> test a rival fails; [`ecj-robustness`](../../skills/ecj-robustness/SKILL.md).)*
>
> Our contribution is to **measure a barrier the take-up literature has mostly assumed away** and to
> show it is large: where a service sits can matter as much as what it costs. The estimate is a
> local average for this city and service, and we do **not** claim the same elasticity for every
> program; but the lesson — that **the geography of delivery is a policy lever for take-up** — travels
> to any setting where benefits are claimed in person. *(contribution as question + magnitude +
> broad, bounded lesson; [`ecj-topic-selection`](../../skills/ecj-topic-selection/SKILL.md).)*
>
> The paper proceeds as follows. Section 2 describes the reform and the data; Section 3 lays out the
> identification and presents the main result; Section 4 isolates the time-cost mechanism. *(brief
> roadmap — no over-signposting.)*

---

## Why the "after" meets the EJ bar

Mapped to this pack's skill checklists:

- **First paragraph states a broadly interesting question + the magnitude + its uncertainty** — 4.6
  pp (s.e. 1.1), 14% of the base, appears immediately, with units and a standard error, never an
  asterisk ([`ecj-writing-style`](../../skills/ecj-writing-style/SKILL.md): "results stated plainly
  with magnitudes"; [`ecj-tables-figures`](../../skills/ecj-tables-figures/SKILL.md): "economic
  magnitude, not stars alone").
- **Broad relevance is argued, not assumed** — the take-up question reaches any economist who cares
  about how public programs reach people, satisfying
  [`ecj-topic-selection`](../../skills/ecj-topic-selection/SKILL.md)'s broad-interest test, and the
  positioning speaks to a general literature rather than a transit niche
  ([`ecj-literature-positioning`](../../skills/ecj-literature-positioning/SKILL.md)).
- **Identification is credible and stated in plain words** — staggered rollout, a heterogeneity-robust
  estimator instead of TWFE, flat leads, a placebo and a leave-one-out — matching
  [`ecj-identification`](../../skills/ecj-identification/SKILL.md) Branch A.
- **The mechanism is named and a rival is excluded** — time cost vs. information, with a test only
  the time-cost story passes ([`ecj-robustness`](../../skills/ecj-robustness/SKILL.md)).
- **The contribution is an answer with a bounded, portable lesson** — "geography of delivery is a
  policy lever," with an explicit statement of what the local estimate does **not** establish,
  satisfying [`ecj-topic-selection`](../../skills/ecj-topic-selection/SKILL.md).
- **Sibling check passes:** this is a substantial, broadly interesting applied result with clear
  exposition — EJ's identity — not a purely methodological piece (which would route to The
  Econometrics Journal).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified** EJ papers,
> [`../../skills/ecj-replication-package/SKILL.md`](../../skills/ecj-replication-package/SKILL.md) for
> building the analysis so it clears the EJ Data Editor reproducibility check, and
> [`../code/`](../code/) for a runnable empirical command chain. For the venue-neutral referee
> objections a staggered-DiD take-up claim must pre-empt, see
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).
