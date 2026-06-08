> **Illustrative teaching example.** The paper, setting, and every number below are **fictional** and
> exist only to demonstrate JOLE house style. No real-paper facts are stated, and no real policy is
> described. Corresponding skills:
> [`jole-writing-style`](../../skills/jole-writing-style/SKILL.md),
> [`jole-topic-selection`](../../skills/jole-topic-selection/SKILL.md), and
> [`jole-contribution-framing`](../../skills/jole-contribution-framing/SKILL.md).

# Worked Example: A JOLE-Style Introduction (before → after)

This demonstrates the **JOLE introduction arc** from `jole-writing-style`:
**labor question → why it is hard → setting & variation → headline result (with units) → mechanism &
interpretation → contribution & external relevance → brief roadmap** — written for a general
labor-economics audience, within JOLE's word economy, with the result stated early and the contribution
calibrated to what the design supports (`jole-contribution-framing`).

**Illustrative paper (fictional):** *"Apprenticeship Slots and Young Workers' Earnings: Evidence from a
Staggered Capacity Expansion."* Fictional setting: a country whose regional training agencies expanded
the number of subsidized apprenticeship slots in different years, for reasons of administrative budget
cycles rather than local labor-market conditions. **All figures are invented for teaching.**

---

## Before (buries the question — typical first-draft intro)

> The returns to vocational training have been studied extensively in the labor-economics literature.
> Many papers examine human capital, schooling, and on-the-job training. In this paper, we apply a
> Callaway and Sant'Anna staggered difference-in-differences estimator, together with a Sun and Abraham
> interaction-weighted specification, to administrative earnings records linked to a training register.
> We estimate event-study coefficients and report robustness checks. Training is an important policy
> topic. Section 2 reviews the literature, Section 3 describes the data, Section 4 sets out the empirical
> strategy, Section 5 presents results, and Section 6 concludes.

**What's wrong (against `jole-writing-style`, `jole-topic-selection`, `jole-contribution-framing`):**

- **Leads with the estimator** ("we apply a Callaway and Sant'Anna … estimator") instead of the labor
  question — the named anti-pattern in `jole-writing-style` ("Leading the intro with method").
- **No labor question and no result on page one.** A labor economist outside the training literature
  cannot tell what was learned or why it matters across labor economics.
- **No headline number with units** in the intro (`jole-writing-style`: "Headline result appears early in
  the intro, with units").
- **Throat-clearing** ("studied extensively," "is an important policy topic") with no stakes — the kind
  of padding JOLE's word economy will not survive.
- **No external relevance** ("beyond this setting") and **no stated contribution** — `jole-contribution-framing`
  requires margin + variation + magnitude + lesson.
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (JOLE arc — labor question + result early, contribution calibrated)

> **Does expanding access to subsidized apprenticeships raise the early-career earnings of young
> workers — and through which margin?** We show that enlarging apprenticeship capacity raises the
> annual earnings of affected young workers by **5.8%** three years out, by moving them into training
> rather than into immediate low-wage employment. *(labor question + headline answer with units, in the
> first breath.)*
>
> Answering this cleanly is hard because training capacity is rarely exogenous: regions tend to add
> apprenticeship slots precisely when their youth labor markets are already tightening, so a naive
> comparison conflates the expansion with the local upturn that prompted it. *(why it is hard — the
> identification problem, named before any estimator.)*
>
> We exploit a setting in which regional training agencies expanded apprenticeship slots in **different
> years**, on administrative budget cycles unrelated to local labor-market trends. The staggered timing
> lets us compare each region to not-yet-expanded regions, and the leads in our event study are flat,
> consistent with no differential pre-trends before an expansion. *(setting & variation, in one
> paragraph; preview of `jole-identification-strategy` Branch A.)*
>
> Capacity expansion raises affected young workers' earnings by **5.8%** (off a base of roughly €19,000)
> three years after entry, with effects absent before the expansion and growing over the first two
> post-entry years. The gains are concentrated among workers with no prior tertiary schooling, and we
> show the channel is **occupational upgrading**: treated workers are 7 percentage points more likely to
> hold a skilled occupation, not merely better paid within the same job. *(headline result restated with
> the labor mechanism; interpretation — `jole-writing-style` step 5.)*
>
> Our contribution is to identify **capacity, not price**, as a binding margin in vocational training:
> the expansion changes no wage schedule and no curriculum, yet raises earnings by relaxing a rationing
> constraint on who can train. This sharpens a literature that has focused on the returns to completed
> training by showing that **access to a training slot is itself a first-order determinant of young
> workers' earnings.** *(contribution stated early and calibrated, relative to a specific prior view —
> `jole-contribution-framing` "new answer / new mechanism".)* Beyond apprenticeships, the result implies
> that **any human-capital policy that rations slots — community-college seats, licensing classes,
> active labor-market programs — should be evaluated partly on the capacity margin, not only on the
> return to those who already get in.** *(external relevance that travels beyond the setting.)*
>
> The paper proceeds as follows. Section 2 describes the institutional setting and the linked register;
> Section 3 presents the design and main results; Section 4 examines the occupational-upgrading
> mechanism and robustness. *(brief roadmap — no over-signposting.)*

---

## Why the "after" meets the JOLE bar

Mapped to the skill checklists:

- **Labor question on page one in plain language**, legible to a labor economist outside the training
  literature (`jole-topic-selection`: "general-interest within labor").
- **Headline number appears early, with units** (5.8%; +7 pp skilled-occupation share) —
  `jole-writing-style`'s rule that the result, with units, lands in the introduction.
- **Identification problem named before the estimator**; the modern staggered-DID tools are demoted to
  where the design is discussed, never the lead (avoids the `jole-writing-style` "leading with method"
  anti-pattern; design ladder per [`../../skills/jole-identification-strategy/SKILL.md`](../../skills/jole-identification-strategy/SKILL.md)).
- **Contribution is one calibrated sentence** — margin (earnings/occupation), variation (staggered
  capacity expansion), magnitude (5.8%), lesson (capacity is a binding margin) — exactly what
  `jole-contribution-framing` requires, with **no global-from-local leap**.
- **External relevance is explicit** ("beyond apprenticeships … community-college seats, licensing,
  ALMPs"), satisfying the `jole-topic-selection` and `jole-writing-style` "travels beyond the setting"
  filter.
- **One-sentence hook is fillable:** "We show that [expanding apprenticeship slots raises young workers'
  earnings by 5.8%] using [staggered, budget-driven capacity expansion]" — both brackets filled, the
  test in `jole-contribution-framing`.
- **Word economy respected** — the arc carries the argument in six tight paragraphs, leaving heavy detail
  for a bounded online appendix rather than padding the body (`jole-writing-style` ~20,000-word economy).

> Note: the abstract for a paper like this must restate the question, the 5.8% result, and the labor
> lesson in **≤ 100 words** (`jole-writing-style`) — the introduction above is not the abstract.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **verified real JOLE papers** whose
> intros execute this arc, and [`../code/`](../code/) for the staggered-DID command chain
> (`stata/03_did_modern.do`, `python/event_study_plot.py`) referenced above.
