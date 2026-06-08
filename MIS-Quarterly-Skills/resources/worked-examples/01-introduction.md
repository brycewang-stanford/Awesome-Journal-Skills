> **Illustrative teaching example.** The paper, setting, and every number below are **fictional** and
> exist only to demonstrate MIS Quarterly (MISQ) house style. No real-paper facts are stated, and no
> policy is invented. Corresponding skills:
> [`misq-writing-style`](../../skills/misq-writing-style/SKILL.md),
> [`misq-topic-selection`](../../skills/misq-topic-selection/SKILL.md),
> [`misq-theory-development`](../../skills/misq-theory-development/SKILL.md),
> [`misq-literature-positioning`](../../skills/misq-literature-positioning/SKILL.md), and
> [`misq-contribution-framing`](../../skills/misq-contribution-framing/SKILL.md).

# Worked Example: A MISQ-Style Introduction (before → after)

This demonstrates the **MISQ introduction discipline** drawn from this pack's own skills: by the end of
the introduction an interdisciplinary IS reader — spanning the **four IS traditions** (behavioral,
design science, economics of IS, organizational) — should know the **IS phenomenon, the role of the IT
artifact, the approach, and the contribution** (`misq-writing-style`). The front end must **join a named
IS conversation and problematize an assumption** rather than spot a gap (`misq-literature-positioning`),
keep the **IT artifact load-bearing** (`misq-topic-selection`, `misq-theory-development`), and state the
contribution in **the currency of its tradition** (`misq-contribution-framing`).

> **A note on scope.** Because IS is pluralistic, this example uses an **economics-of-IS** paper with a
> behavioral mechanism — a cross-tradition blend MISQ explicitly welcomes. The econometric
> [`code/`](../code/) kit (DiD / IV / RDD / DML) is **supporting infrastructure** here, not the center of
> gravity: in MISQ the load-bearing claim is the *IS theory and the artifact's role*, with identification
> as the evidentiary backbone, not the headline. A behavioral, design-science, or qualitative paper would
> swap the estimator for an SEM measurement model, an artifact evaluation, or a coded data structure
> (`misq-data-analysis`) while keeping the **same introduction discipline**.

**Illustrative paper (fictional):** *"Does Algorithmic Wage Transparency Change Gig Effort? Evidence from
a Staggered Dashboard Rollout."* Fictional setting: a ride-hailing platform that switched on a per-trip
**earnings-breakdown dashboard** (the IT artifact) for drivers in different cities at different times.

---

## Before (buries the IS contribution — typical first-draft intro)

> The gig economy has grown rapidly and has attracted considerable attention from researchers across
> disciplines. Prior work has examined many aspects of platform work. In this paper, we study the effect
> of an information feature on a ride-hailing platform. We use a staggered difference-in-differences
> design with the Callaway and Sant'Anna (2021) estimator, supplemented by Sun and Abraham (2021), and we
> assemble a large panel of drivers. Information transparency is an important issue for platforms and for
> society. Our results have implications for managers. Section 2 reviews the literature, Section 3
> describes the data, Section 4 presents the empirical strategy, Section 5 reports results, and Section 6
> concludes.

**What's wrong (against this pack's skills):**

- **No IS phenomenon and no contribution on page one.** A reader cannot tell what *information-systems*
  question is at stake or what the paper adds (`misq-writing-style`: front-load the contribution and the
  IT artifact).
- **The IT artifact is invisible.** "An information feature" is interchangeable with any treatment — the
  named anti-pattern of a "management study with IT as window dressing" (`misq-topic-selection`,
  `misq-literature-positioning`: keep the artifact load-bearing).
- **Leads with the estimator** ("we use a Callaway and Sant'Anna design") rather than the IS mechanism —
  method demoted-to-lead, the wrong altitude for MISQ.
- **Gap-spotting and throat-clearing** ("has attracted considerable attention," "an important issue")
  instead of **problematizing an assumption** in a named IS conversation (`misq-literature-positioning`).
- **No mechanism, no boundary condition** (`misq-theory-development`); **no contribution in the currency
  of the tradition** and no theory-*and*-practice implication (`misq-contribution-framing`).
- **Author-led / over-signposted** roadmap doing the argument's work, and (in MISQ's
  lead-with-the-information citation style) author-led citation phrasing (`misq-writing-style`).

---

## After (MISQ arc — IS phenomenon + artifact + approach + contribution, front-loaded)

> **When a platform shows gig workers exactly how each dollar of their pay is computed, do they work
> harder — or do they pull back once the algorithm's logic is laid bare?** Drawing on the IS conversation
> on **digital platforms, algorithmic management, and IT-enabled transparency**, we show that switching on
> a per-trip **earnings-breakdown dashboard** raises driver effort by 6.3% in the quarter after rollout,
> and that the gain runs through **perceived procedural fairness** of the pay algorithm rather than
> through new monetary incentives. *(IS phenomenon + the artifact + approach + headline contribution, in
> the first breath — with units.)*
>
> The dominant assumption in work on algorithmic management is that revealing an algorithm's workings
> mainly reduces *uncertainty*, so any effort response should be a mechanical reaction to clearer
> piece-rate information. **We problematize that assumption:** the same dashboard can *legitimize* a pay
> rule workers already distrust, making the IT artifact's effect a question of **fairness perception, not
> just information provision** — a distinctly IS twist on a transparency literature borrowed from
> economics and organizational behavior. *(problematization + the IS twist on borrowed theory;
> `misq-literature-positioning`.)*
>
> Identifying this is hard because platforms rarely roll out features at random: a dashboard often ships
> exactly when a city's labor supply is already tightening, conflating the artifact with the boom that
> prompted it. We exploit the platform's **staggered activation** of the dashboard across cities in
> different months for engineering-capacity reasons unrelated to local effort trends, comparing each city
> to **not-yet-treated** cities and verifying no differential pre-trends in effort before activation.
> *(setting, artifact-centered variation, and the identification logic — the econometrics is the
> backbone, not the headline; see [`../code/`](../code/).)*
>
> Effort rises **6.3%** after activation (off a pre-period base), grows over the three months after
> rollout, and is **absent beforehand**; the increase is concentrated among drivers who had previously
> filed pay disputes, and a pre-registered survey on a driver subsample shows the channel is **higher
> perceived procedural fairness**, not changed beliefs about expected pay. *(headline restated with the
> theorized mechanism and a boundary condition; `misq-theory-development`.)*
>
> We contribute to the IS conversation on **algorithmic management** by identifying **legitimation
> through transparency**, not mere uncertainty reduction, as the mechanism through which an information
> artifact reshapes platform work — revising the prevailing information-provision account and specifying
> *when* transparency backfires (when the underlying rule is seen as unfair). *(contribution in the
> economics-of-IS currency — an identified effect and mechanism — tied to the named conversation;
> `misq-contribution-framing`.)* For platform designers and policymakers debating algorithmic-transparency
> mandates, the lesson is that **disclosure is not neutral plumbing: exposing an unfair rule can erode the
> very effort transparency is meant to protect**, so the design question is fairness-by-design, not
> disclosure alone. *(theory + practice/societal implication, as MISQ requires.)*
>
> The paper proceeds as follows. Section 2 develops the legitimation mechanism and hypotheses; Section 3
> describes the rollout, data, and identification; Section 4 reports the effect and the fairness channel.
> *(brief roadmap — no over-signposting.)*

---

## Why the "after" meets the MISQ bar

Mapped to this pack's skill checklists:

- **Contribution and IT artifact stated plainly in the introduction** — the dashboard is named and
  load-bearing, and the "so what for IS" appears on page one (`misq-writing-style`,
  `misq-topic-selection`). Deleting the artifact would destroy the argument — the central test of an
  *IS* question.
- **Joins a named IS conversation and problematizes** — "algorithmic management / IT-enabled transparency"
  is named with its prevailing assumption (transparency = uncertainty reduction) surfaced and challenged,
  rather than "no one has studied X" (`misq-literature-positioning`).
- **Theory in the tradition's form, derived a priori** — a stated mechanism (legitimation via perceived
  fairness), a moderator (prior disputes), and a boundary condition (when the rule is seen as unfair),
  not a bare correlation (`misq-theory-development`).
- **Contribution in the currency of the tradition** — an *identified economic effect and its mechanism*,
  with both theory and practice/policy implications, justifying the page budget
  (`misq-contribution-framing`).
- **Method demoted to backbone, not lead** — the staggered-DiD design and the [`code/`](../code/) chain
  appear only where identification is discussed; the headline is the IS mechanism, not the estimator.
- **Cross-tradition blend declared** — economics-of-IS identification carrying a behavioral
  (fairness-perception) mechanism, a blend MISQ welcomes when the primary tradition is named
  (`misq-topic-selection`).
- **Readable across the four traditions; MISQ citation style** — terms are defined in plain language, and
  in the manuscript proper the in-text citations would **lead with the information, not the author**
  (`misq-writing-style`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **verified real MISQ papers** whose
> front ends execute this discipline across the four traditions, and [`../code/`](../code/) for the
> staggered-DiD command chain that serves as the evidentiary backbone here. For what counts as a
> contribution and how to defend it, see
> [`../../skills/misq-contribution-framing/SKILL.md`](../../skills/misq-contribution-framing/SKILL.md);
> for the shared, venue-neutral inference audit, see
> [`../../../shared-resources/empirical-methods/reporting-standards.md`](../../../shared-resources/empirical-methods/reporting-standards.md)
> and
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).
