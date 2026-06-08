> **Illustrative teaching example.** The paper, sample, and every number below are **fictional** and
> exist only to demonstrate Psychological Science house style. No real-paper facts and no journal policy
> are invented here — policy lives in [`../official-source-map.md`](../official-source-map.md).
> Corresponding skills: [`psci-writing-style`](../../skills/psci-writing-style/SKILL.md),
> [`psci-literature-positioning`](../../skills/psci-literature-positioning/SKILL.md),
> [`psci-topic-selection`](../../skills/psci-topic-selection/SKILL.md),
> [`psci-study-design`](../../skills/psci-study-design/SKILL.md), and
> [`psci-open-science-and-transparency`](../../skills/psci-open-science-and-transparency/SKILL.md).

# Worked Example: A Psychological Science Introduction (before → after)

This demonstrates the **Psychological Science Introduction arc** that the pack's skills require:
**question + stakes → the gap, named precisely → contribution stated early → the design that settles it
(power, preregistration) → broad relevance** — written for a **short-format, broad-interest** empirical
psychology venue, post-replication-crisis, where **rigor is part of the claim**: the Introduction and
Discussion *share* a **≤ 2,000-word** budget, so positioning must be surgical
(`psci-writing-style`, `psci-literature-positioning`).

A note on scope for this pack: experiments dominate Psychological Science, so the persuasive work here is
**design and effect-size reporting**, not an econometric pipeline. The vendored econometric
[`../code/`](../code/) kit is **supporting infrastructure** (e.g., if a study has a quasi-experimental or
panel component), **not** the center of a typical submission.

**Illustrative paper (fictional):** *"Sleep Debt Narrows the Window of Prosocial Choice: A Preregistered
Experiment."* Fictional setting: a two-night sleep-restriction experiment on prosocial decision-making.

---

## Before (buries the idea — typical first-draft intro)

> Sleep has been studied extensively in psychology, and its effects on cognition, mood, and health are
> well documented across a large literature. Many theories have been proposed about how sleep loss
> affects behavior, and prior work has examined attention, memory, and emotion regulation. In the present
> research we examine the relationship between sleep and prosocial behavior. We conducted an experiment in
> which participants were assigned to a sleep condition and then completed a decision task. We predicted
> that sleep loss would affect prosocial choices. This is an important and timely topic given how common
> insufficient sleep is in modern society. The remainder of this article describes our methods, presents
> our results, and discusses their implications.

**What's wrong (against `psci-writing-style` / `psci-literature-positioning` / `psci-topic-selection`):**

- **No question, no answer, no effect on page one.** A broad-interest reader cannot tell what was found
  or how big it is — the venue front-loads (`psci-writing-style`: "front-load ruthlessly").
- **Throat-clearing literature history** ("studied extensively," "well documented") that the **2,000-word
  Intro+Discussion budget cannot hold** (`psci-literature-positioning` anti-pattern).
- **Gap stated as vagueness** ("examine the relationship"), not as a precise, unresolved question.
- **Contribution not stated early**; **breadth not made explicit** — no reason a non-sleep psychologist
  should care.
- **No signal of rigor** — no power/sample-size justification, no preregistration, no effect size — which
  is exactly what this post-replication-crisis venue treats as load-bearing
  (`psci-study-design`, `psci-open-science-and-transparency`).
- **Over-signposted roadmap** doing work the argument should do.

---

## After (Psychological Science arc — question + effect + rigor, contribution early)

> **Does a night of lost sleep make people less willing to help — and how large is the effect?** In a
> preregistered experiment, two nights of sleep restriction reduced prosocial giving by **18%** relative
> to a rested control, *d* = 0.42, 95% CI [0.21, 0.63]. *(question + headline effect with an effect size
> and CI, in the first breath — the rigor is part of the claim.)*
>
> Whether sleep loss changes *what people choose to do for others* — not just how they feel or perform —
> is unresolved: prior work links short sleep to worse mood and slower cognition, but it is contested
> whether those changes translate into a measurable shift in **prosocial decisions**, and most existing
> studies are small and correlational. *(the gap, named precisely — not "little is known.")*
>
> We test this with a **preregistered, adequately powered** between-subjects experiment (*N* = 240;
> healthy adults), with sample size fixed in advance by a power analysis targeting the smallest effect of
> interest and all exclusion and analysis rules locked before data collection. *(the design that settles
> it; power + preregistration stated up front, per `psci-study-design`.)*
>
> Restricting sleep to 4 hours for two nights cut donations in an incentivized giving task by **18%**
> (*d* = 0.42, 95% CI [0.21, 0.63]); the effect held controlling for mood and was absent in a rested
> control. *(headline effect restated with direction, magnitude, and the key control.)*
>
> Our contribution is to show that sleep loss moves a **choice**, not merely a feeling or a reaction
> time: it narrows the margin on which people act prosocially, even when they report no worse mood. This
> reframes sleep not only as a cognitive and affective variable but as an input to **everyday moral
> behavior**. *(contribution stated early, relative to a specific prior view.)* Beyond the lab, the result
> implies that conditions producing chronic sleep debt — shift work, caregiving, early school start times
> — may have an under-recognized cost in **how much people help one another**, a question relevant to
> social, health, and organizational psychology alike. *(broad relevance made explicit — who outside the
> subarea should care.)*
>
> All data, materials, and analysis scripts are openly available, and the study was preregistered (links
> in the Research Transparency Statement below). *(transparency flagged where the venue expects it; the
> statement itself lives between Introduction and Methods — see
> [`psci-open-science-and-transparency`](../../skills/psci-open-science-and-transparency/SKILL.md). No
> specific policy wording is invented here; confirm current requirements in
> [`../official-source-map.md`](../official-source-map.md).)*

---

## Why the "after" meets the Psychological Science bar

Mapped to the pack's skill checklists:

- **Front-loaded question + effect** — the headline effect (18%; *d* = 0.42, 95% CI [0.21, 0.63]) appears
  immediately, **with effect size and CI**, as `psci-writing-style` requires (stats with ES + CI, never
  bare).
- **Surgical positioning** — the gap is named in one tight paragraph and the contribution stated early,
  fitting the **2,000-word Intro+Discussion** budget (`psci-literature-positioning`); no chronological
  review.
- **Rigor is visible and early** — sample-size justification and preregistration are stated in the
  Introduction, not buried, because in this venue robustness *is* part of the claim
  (`psci-study-design`, `psci-topic-selection` robustness filter).
- **Breadth made explicit** — the broad lesson reaches social, health, and organizational psychology, so
  a reader outside sleep research sees the stakes (`psci-topic-selection` impact + breadth).
- **Transparency signposted, not improvised** — open data/materials/scripts and the Research Transparency
  Statement are flagged where the venue expects them; exact policy is deferred to
  [`../official-source-map.md`](../official-source-map.md), not invented.
- **One-sentence hook is fillable:** "We show that [two nights of lost sleep cut prosocial giving by 18%]
  using [a preregistered, powered experiment]" — both brackets filled, as `psci-topic-selection` asks.

> Next: if your study has a quasi-experimental/panel component, adapt the supporting
> [`../code/`](../code/) kit. For the 150-word structured abstract that pairs with this Introduction, see
> [`psci-writing-style`](../../skills/psci-writing-style/SKILL.md).
