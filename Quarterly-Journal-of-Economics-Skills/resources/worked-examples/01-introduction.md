> **Illustrative teaching example.** The paper, setting, and every number below are **fictional** and
> exist only to demonstrate QJE house style. No real-paper facts are stated. Corresponding skills:
> [`qje-writing-style`](../../skills/qje-writing-style/SKILL.md) and
> [`qje-topic-selection`](../../skills/qje-topic-selection/SKILL.md).

# Worked Example: A QJE-Style Introduction (before → after)

This demonstrates the **QJE introduction arc** from `qje-writing-style`:
**question → why it's hard → setting & variation → headline result → interpretation → contribution &
broad lesson → brief roadmap** — with the QJE rule that the **first paragraph states the question, the
answer, and why it matters**, framed for a general-interest reader, with the contribution stated early.

**Illustrative paper (fictional):** *"Free Buses and the Geography of Jobs: Evidence from a Staggered
Fare-Abolition Reform."* Fictional setting: a country where 40 mid-sized cities abolished public-transit
fares in different years.

---

## Before (buries the idea — typical first-draft intro)

> The relationship between transportation and labor markets has been studied extensively in the
> literature. Many papers have examined commuting, congestion, and infrastructure. In this paper, we
> use a Callaway and Sant'Anna (2021) staggered difference-in-differences estimator, supplemented with
> the Sun and Abraham (2021) interaction-weighted estimator, to study the effects of public-transit fare
> policy. We assemble a panel of cities and estimate event-study specifications. Transit policy is an
> important topic for policymakers. Section 2 reviews the literature, Section 3 describes the data,
> Section 4 presents the empirical strategy, Section 5 reports results, and Section 6 concludes.

**What's wrong (against `qje-writing-style` / `qje-topic-selection`):**

- **Leads with method** ("we use a Callaway and Sant'Anna estimator") instead of the question — a named
  anti-pattern in both skills.
- **No question and no answer on page one.** A general-interest reader cannot tell what was found, or why
  a macro/development economist should care.
- **No headline number with units** in the intro.
- **Throat-clearing** ("has been studied extensively," "is an important topic") with vague stakes.
- **No broad lesson** that travels beyond this setting; **contribution is not stated**.
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (QJE arc — question + answer + why it matters, contribution early)

> **Does cheaper commuting widen the set of jobs a worker can actually reach — and does that translate
> into higher earnings?** We show that abolishing public-transit fares raises the employment rate of
> low-income residents by 2.4 percentage points and their annual earnings by 3.1%, by enlarging the
> geographic area within which they search for work. *(question + headline answer + why it matters, in
> the first breath — units included.)*
>
> Answering this cleanly is hard because transit investment is rarely exogenous: cities expand or
> subsidize transit precisely when their labor markets are already improving, so a simple comparison
> conflates the policy with the boom that prompted it. *(why it's hard — the identification problem.)*
>
> We exploit a reform in which 40 mid-sized cities abolished transit fares in **different years** between
> 2012 and 2021, for budgetary reasons unrelated to local labor-market trends. The staggered timing lets
> us compare each city to not-yet-treated cities, and we verify there are no differential pre-trends in
> employment before a city goes fare-free. *(setting & variation, in one paragraph.)*
>
> Fare abolition raises low-income employment by **2.4 percentage points** (off a base of 61%) and
> earnings by **3.1%**, with effects that grow over the three years after the reform and are absent
> before it. The gains are concentrated among workers who live far from the central business district,
> and we show the mechanism is a **larger commuting radius**: treated workers take jobs 4.8 km farther
> from home on average. *(headline result restated with the mechanism; interpretation.)*
>
> Our contribution is to identify **access, not just price**, as the margin through which transport
> policy moves labor markets: the reform changes no wage and no job, yet reallocates workers to better
> matches by relaxing a spatial search constraint. This reframes transit subsidies as **labor-market
> policy** rather than a transport amenity. *(contribution stated early, relative to a specific prior
> view.)* Beyond free buses, the result implies that **any policy lowering the cost of distance — remote
> work, ride-sharing subsidies, road pricing — should be evaluated partly by how much it expands the
> reachable job set of the spatially constrained.** *(broad lesson that travels beyond the setting.)*
>
> The paper proceeds as follows. Section 2 describes the reform and data; Section 3 presents the design
> and results; Section 4 examines the commuting-radius mechanism. *(brief roadmap — no over-signposting.)*

---

## Why the "after" meets the QJE bar

Mapped to the skill checklists:

- **First paragraph states question + answer + why it matters** — the QJE funnel; the headline number
  (2.4 pp; 3.1%) appears immediately, with units (`qje-writing-style`: "headline result appears early in
  the introduction, with units").
- **General-interest framing** — the question is legible to a labor, macro, *and* development economist;
  the broad lesson generalizes to remote work and road pricing (`qje-topic-selection` question and
  breadth filters).
- **Contribution stated early and relative to a specific prior view** ("access, not just price"), not a
  vague "we contribute to the literature."
- **Identification problem named** before the design is introduced; **no-pre-trends** stated plainly —
  consistent with the arc's "why it is hard → the variation that solves it."
- **Method is demoted to a tool**, mentioned only where the design is discussed, never as the lead
  (avoids the shared "leading with the estimator" anti-pattern).
- **One-sentence hook is fillable:** "We show that [free transit raises low-income earnings by 3.1%]
  using [staggered fare abolition]" — both brackets filled, as `qje-topic-selection` requires.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for verified real QJE papers whose
> intros execute this arc, and [`../code/`](../code/) for the staggered-DID command chain referenced
> above.
