> **Illustrative teaching example.** The paper, sample, and every number below are **fictional** and
> exist only to demonstrate *Developmental Psychology* house style. No real-paper facts and no journal
> policy are invented here — policy lives in [`../official-source-map.md`](../official-source-map.md).
> Corresponding skills: [`devpsych-writing-style`](../../skills/devpsych-writing-style/SKILL.md),
> [`devpsych-literature-positioning`](../../skills/devpsych-literature-positioning/SKILL.md),
> [`devpsych-topic-selection`](../../skills/devpsych-topic-selection/SKILL.md),
> [`devpsych-study-design`](../../skills/devpsych-study-design/SKILL.md), and
> [`devpsych-open-science-and-transparency`](../../skills/devpsych-open-science-and-transparency/SKILL.md).

# Worked Example: A Developmental Psychology Introduction (before → after)

This demonstrates the **Developmental Psychology Introduction arc** that the pack's skills require:
**developmental question + stakes → the gap, named as change/age/mechanism → contribution stated early →
the design that supports a change claim (power, measurement invariance, preregistration) → broad
developmental relevance** — written for a **lifespan-development** venue under **APA 7th edition + JARS**,
where the load-bearing demand is a credible claim about *change*, not a snapshot in one age group
(`devpsych-writing-style`, `devpsych-literature-positioning`, `devpsych-topic-selection`).

A note on scope for this pack: experiments, longitudinal/cohort designs, and observational coding dominate
*Developmental Psychology*, so the persuasive work here is **developmental design and change-modeling**
(growth curves, invariance, attrition handling), not an econometric pipeline (see
[`../README.md`](../README.md) on why there is no `code/` kit).

**Illustrative paper (fictional):** *"How Self-Control Grows: A Preregistered Three-Wave Study of Effortful
Control and Parental Scaffolding From Ages 4 to 8."* Fictional setting: an accelerated longitudinal study
of self-regulation development.

---

## Before (buries the developmental claim — typical first-draft intro)

> Self-control has been studied extensively in developmental psychology, and its importance for children's
> outcomes is well documented across a large literature. Many theories have addressed how children regulate
> their behavior, and prior work has examined attention, temperament, and parenting. In the present research
> we examine the relationship between parenting and effortful control in children. We measured effortful
> control and parenting and tested whether they were related. We predicted that parenting would be
> associated with effortful control. This is an important and timely topic given how much self-control
> matters for development. The remainder of this article describes our methods, results, and implications.

**What's wrong (against `devpsych-writing-style` / `devpsych-literature-positioning` / `devpsych-topic-selection`):**

- **No developmental claim.** It promises a *relationship*, measured once — not **change with age**. A
  developmental reader cannot tell whether this is about a trajectory or a single-age correlation
  (`devpsych-topic-selection`: the fit test is *change*, not a phenomenon in an age group).
- **Throat-clearing literature history** ("studied extensively," "well documented") instead of a precise
  **developmental gap** (`devpsych-literature-positioning` anti-pattern).
- **Gap stated as vagueness** ("examine the relationship"), not as what is unknown about *how self-control
  grows* or *what drives that growth*.
- **No signal of design rigor** — no waves, no power, no measurement invariance, no preregistration — which
  is exactly what this venue treats as load-bearing for a change claim (`devpsych-study-design`).
- **Breadth not made explicit**; **over-signposted roadmap** doing work the argument should do.

---

## After (Developmental Psychology arc — change + mechanism + rigor, contribution early)

> **Does children's self-control grow steadily across early childhood, and does supportive parenting make
> it grow faster?** In a preregistered three-wave study of 300 children (ages 4, 6, and 8), effortful
> control showed positive within-person growth (latent slope *b* = 0.42/year, 95% CI [0.31, 0.53]), and
> higher maternal scaffolding at age 4 predicted a steeper slope (*b* = 0.18, 95% CI [0.07, 0.29]).
> *(developmental question + the change, with effect sizes and CIs, in the first breath.)*
>
> How effortful control *develops* — its within-person trajectory, and what drives the rate of growth — is
> unresolved: most evidence is cross-sectional, so we know children differ in self-control by age but not
> how individual children change, or whether early parenting accelerates that change. *(the gap, named as
> change and mechanism — not "little is known.")*
>
> We test this with a **preregistered, adequately powered** accelerated longitudinal design (*N* = 300;
> sample size fixed in advance by a Monte Carlo power simulation for the growth slope and the
> scaffolding × time interaction), and we establish **measurement invariance** across waves before
> interpreting change, so the trajectory reflects growth in one construct rather than a shifting measure.
> *(the design that supports a change claim; power + invariance + preregistration stated up front, per
> `devpsych-study-design`.)*
>
> Our contribution is to move from "children differ in self-control" to "self-control **grows**, and early
> scaffolding shapes how fast" — a within-person, mechanism-bearing claim rather than an age-group contrast.
> *(contribution stated early, relative to a specific prior view.)* Beyond this sample, the result implies
> that the preschool years may be a leverage point for supporting self-regulation, a question relevant to
> developmental, educational, and family-clinical science alike. *(broad developmental relevance made
> explicit.)*
>
> All de-identified data and analysis scripts are openly available, identifiable observational video is
> shared under permission, and the study was preregistered (details in the data-availability statement).
> *(transparency flagged where the venue expects it; the exact policy is deferred to
> [`devpsych-open-science-and-transparency`](../../skills/devpsych-open-science-and-transparency/SKILL.md)
> and [`../official-source-map.md`](../official-source-map.md), not invented.)*

---

## Why the "after" meets the Developmental Psychology bar

Mapped to the pack's skill checklists:

- **The claim is change, not a snapshot** — the headline is a within-person *slope* with an effect size and
  CI, exactly the developmental contribution `devpsych-topic-selection` and `devpsych-data-analysis` require.
- **The gap is developmental** — named as *how* self-control grows and *what drives the rate*, not a topic
  survey (`devpsych-literature-positioning`), and the contribution is stated by paragraph two.
- **Rigor specific to developmental designs is visible and early** — power for the growth parameter,
  **measurement invariance before interpreting change**, and preregistration are stated in the Introduction,
  because here the credibility of the change claim *is* part of the claim (`devpsych-study-design`).
- **Breadth made explicit** — the lesson reaches developmental, educational, and clinical science, so a
  reader outside self-regulation research sees the stakes (`devpsych-topic-selection` impact + breadth).
- **Transparency signposted, not improvised** — open de-identified data/scripts and permission-based video
  sharing are flagged where the venue expects them; exact policy is deferred to
  [`../official-source-map.md`](../official-source-map.md), not invented.
- **One-sentence hook is fillable:** "We show that [self-control grows from age 4 to 8 and early scaffolding
  steepens that growth] using [a preregistered, powered, invariance-checked longitudinal design]" — both
  brackets filled, as `devpsych-topic-selection` asks.

> Next: for the abstract and the Public Significance Statement that pair with this Introduction, see
> [`devpsych-writing-style`](../../skills/devpsych-writing-style/SKILL.md); to harden the invariance and
> attrition plan, see [`devpsych-study-design`](../../skills/devpsych-study-design/SKILL.md).
