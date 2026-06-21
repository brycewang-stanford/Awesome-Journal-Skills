> **Illustrative teaching example.** The paper, sample, and every number below are **fictional** and
> exist only to demonstrate Journal of Applied Psychology (JAP) house style. No real-paper facts and no
> journal policy are invented here — policy lives in
> [`../official-source-map.md`](../official-source-map.md).
> Corresponding skills: [`joap-writing-style`](../../skills/joap-writing-style/SKILL.md),
> [`joap-theory-and-hypotheses`](../../skills/joap-theory-and-hypotheses/SKILL.md),
> [`joap-literature-positioning`](../../skills/joap-literature-positioning/SKILL.md),
> [`joap-topic-selection`](../../skills/joap-topic-selection/SKILL.md),
> [`joap-study-design`](../../skills/joap-study-design/SKILL.md), and
> [`joap-open-science-and-transparency`](../../skills/joap-open-science-and-transparency/SKILL.md).

# Worked Example: A Journal of Applied Psychology Introduction (before → after)

This demonstrates the **JAP Introduction arc** that the pack's skills require: **phenomenon + stakes →
the gap, named precisely → the theoretical contribution (mechanism + level + boundary), stated against
the closest prior work → the rigorous design that warrants the claim (multilevel, temporal, causal leg)
→ applied + scientific relevance** — written for the **APA flagship of I-O psychology**, where a paper
must clear a **dual gate**: a real theoretical advance *and* measurement/design rigor
(`joap-theory-and-hypotheses`, `joap-study-design`).

A note on scope for this pack: JAP's persuasive work is **theory plus measurement** — construct
validity, multilevel structure, mediation with proper inference — not an econometric pipeline. There is
**no vendored econometrics code kit** here (see [`../README.md`](../README.md)); the relevant toolkit is
SEM/HLM/meta-analysis (see [`../external_tools.md`](../external_tools.md)).

**Illustrative paper (fictional):** *"Servant Leadership Builds Team Performance Through Psychological
Safety: A Multilevel Field Study and Experiment."* Fictional setting: a two-wave field study of 612
employees in 74 teams plus a lab experiment on the safety mechanism.

---

## Before (buries the contribution — typical first-draft intro)

> Leadership has been studied extensively in organizational psychology, and many leadership styles have
> been examined in relation to performance across a large literature. Servant leadership in particular
> has received growing attention, and prior work has linked it to a variety of outcomes including
> satisfaction, commitment, and performance. In the present study we examine the relationship between
> servant leadership and team performance. We surveyed employees in a sample of teams and measured
> servant leadership, psychological safety, and performance. We predicted that servant leadership would
> be positively related to team performance and that psychological safety would play a role. This is an
> important topic given how much organizations invest in leadership development. The remainder of this
> article describes our methods, presents our results, and discusses their implications.

**What's wrong (against `joap-theory-and-hypotheses` / `joap-literature-positioning` / `joap-topic-selection`):**

- **No theoretical contribution on page one.** A reader cannot tell what is *new* to I-O theory — this
  reads as one more correlate of a known construct (`joap-topic-selection`: rigor without theory is the
  venue's most common reject).
- **Throat-clearing construct history** ("studied extensively," "growing attention") instead of a
  precise gap (`joap-literature-positioning` anti-pattern).
- **Mechanism unnamed and level muddled** — "psychological safety would play a role" is not a theorized
  cross-level mediator with a stated level of analysis (`joap-theory-and-hypotheses`).
- **No signal of rigor** — sounds like a cross-sectional single-source survey, exactly the design JAP
  desk-rejects; no temporal separation, no multilevel structure, no causal leg (`joap-study-design`).
- **No venue boundary** — nothing distinguishes this from an AMJ or Personnel Psychology framing.
- **Over-signposted roadmap** doing work the argument should do.

---

## After (JAP arc — contribution + mechanism + level + rigor, stated early)

> **Do servant leaders raise team performance, and if so, through what process — and when?** We argue,
> and show, that servant leadership builds **team psychological safety**, which in turn raises team
> performance, and that this cross-level mechanism is **stronger when tasks are highly interdependent**.
> *(phenomenon + the theoretical contribution — mechanism, level, boundary — in the first breath.)*
>
> Whether servant leadership improves performance by **building a safe team climate** rather than by
> direct monitoring is unresolved: the closest prior studies are cross-sectional and single-source, so
> they cannot establish the mediating mechanism, separate it from reverse causation, or locate it at the
> team level. *(the gap, named precisely against the contrast class — not "growing attention.")*
>
> We test this with a **two-wave multilevel field study** (612 employees in 74 teams; leadership and
> safety member-rated at Wave 1, performance supervisor-rated at Wave 2) and a **lab experiment** that
> manipulates servant-leader behavior to provide causal warrant for the safety path; sample sizes were
> fixed in advance by power analyses, and exclusion and analysis rules were locked before data
> collection. *(the rigorous design — temporal and source separation, multilevel structure, a causal
> leg, preregistration — stated up front, per `joap-study-design`.)*
>
> Across both studies, servant leadership raised performance through team psychological safety (field
> indirect effect = .13, 95% CI [.05, .23]; the experiment confirmed the leadership→safety path,
> *d* = 0.46, 95% CI [0.21, 0.71]); the indirect effect was stronger under high task interdependence.
> *(the result, with effect sizes and CIs and the boundary condition.)*
>
> Our contribution is to identify the **mechanism and its boundary**: servant leadership develops
> performance by **building a psychologically safe team**, a cross-level process distinct from a direct
> leadership-performance correlate, and one that operates most strongly where coordination demands are
> high. *(contribution stated against a specific prior view; this is a JAP micro/measurement
> contribution, not an AMJ firm-outcome study.)* For practice, the result reframes leader development
> around **climate-building rather than monitoring**, with implications for how teams are staffed and
> structured. *(applied + scientific relevance made explicit.)*
>
> All data, materials, and analysis code are openly available with persistent identifiers, and the
> experiment was preregistered (links in the data-availability statement). *(transparency flagged where
> the venue expects it under TOP — see
> [`joap-open-science-and-transparency`](../../skills/joap-open-science-and-transparency/SKILL.md). No
> specific policy wording is invented here; confirm current requirements in
> [`../official-source-map.md`](../official-source-map.md).)*

---

## Why the "after" meets the JAP bar

Mapped to the pack's skill checklists:

- **Theoretical contribution legible early** — the mechanism (psychological safety), the level (team /
  cross-level), and the boundary (task interdependence) appear immediately, as
  `joap-theory-and-hypotheses` and `joap-literature-positioning` require.
- **Rigor is visible and early** — multilevel structure, temporal and source separation, an
  experimental causal leg, and preregistration are stated in the Introduction because in this venue
  rigor *is* part of the claim (`joap-study-design`, `joap-topic-selection` dual gate).
- **Estimation-first reporting** — the headline carries effect sizes and CIs (indirect = .13, 95% CI
  [.05, .23]; *d* = 0.46), never bare significance, as `joap-data-analysis` and `joap-writing-style` require.
- **Venue boundary explicit** — framed as a micro/measurement, cross-level mechanism contribution,
  distinct from an AMJ or Personnel Psychology paper (`joap-literature-positioning` sibling guard).
- **Transparency signposted, not improvised** — open data/materials/code and preregistration are flagged
  where the venue expects them; exact policy is deferred to
  [`../official-source-map.md`](../official-source-map.md), not invented.
- **One-sentence hook is fillable:** "We show that [servant leadership raises team performance through
  psychological safety, stronger under high interdependence] using [a multilevel field study + a
  preregistered experiment]" — both brackets filled, as `joap-topic-selection` asks.

> Next: harden the measurement and CMV/nesting plan with
> [`joap-study-design`](../../skills/joap-study-design/SKILL.md), then the SEM/HLM mediation reporting
> with [`joap-data-analysis`](../../skills/joap-data-analysis/SKILL.md). For the structured abstract that
> pairs with this Introduction, see [`joap-writing-style`](../../skills/joap-writing-style/SKILL.md).
