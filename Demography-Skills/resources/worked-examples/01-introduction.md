> **Illustrative teaching example.** The paper, setting, and every number below are **fictional** and
> exist only to demonstrate *Demography* house style. No real-paper facts are stated, and no real policy
> is invoked. Corresponding skills:
> [`demog-writing-style`](../../skills/demog-writing-style/SKILL.md),
> [`demog-topic-selection`](../../skills/demog-topic-selection/SKILL.md), and
> [`demog-theory-building`](../../skills/demog-theory-building/SKILL.md).

# Worked Example: A *Demography*-Style Introduction (before → after)

This demonstrates the introduction arc *Demography* rewards (from `demog-writing-style` and
`demog-topic-selection`): **population question → why it matters across components → data & demographic
method → headline quantity with its magnitude and interval → what it decomposes/identifies →
contribution to population science → brief roadmap.** The governing rule from `demog-writing-style` is
**front-load the contribution** (by the end of the intro the reader knows the population question, the
data and method, the finding, and why it matters for demography broadly) and write **quantity-first**
(lead with the demographic quantity and its magnitude, then interpret). Jargon is defined on first use
so a reader from another component can follow.

**Illustrative paper (fictional):** *"Tempo or Quantum? Decomposing the Rise in Completed Cohort
Childlessness in a Mid-Income Population, 1960–1985 Birth Cohorts."* Fictional setting: a single
mid-income country with high-quality vital registration; childlessness here means reaching age 45 with
zero births.

---

## Before (buries the contribution — typical first-draft intro)

> Childlessness has been studied extensively across many disciplines, including sociology, economics,
> and demography. Many factors have been associated with not having children, such as education,
> employment, partnership, and values. In this paper, we apply an age-period-cohort model and a
> Kitagawa decomposition to register data to study trends in childlessness. We estimate a series of
> models and present the results. Understanding childlessness is important for policymakers and for
> society. Section 2 reviews the literature, Section 3 describes the data, Section 4 presents the
> methods, Section 5 reports results, and Section 6 concludes.

**What's wrong (against `demog-writing-style` / `demog-topic-selection` / `demog-theory-building`):**

- **Leads with method** ("we apply an age-period-cohort model and a Kitagawa decomposition") instead of
  the population question — the named anti-pattern in `demog-writing-style`.
- **No population question and no answer on page one.** A mortality or migration demographer cannot tell
  what changed, by how much, or why it matters for population science broadly (fails the
  `demog-topic-selection` general-interest test).
- **No headline quantity with magnitude or uncertainty** — violates quantity-first prose.
- **Descriptive framing with no contribution type.** It is unclear whether this is an estimate, a
  measurement fix, a decomposition, or a mechanism (the `demog-theory-building` contribution test).
- **Throat-clearing** ("studied extensively," "is important for policymakers") and an undefined
  tempo/quantum distinction that a non-fertility reader cannot follow.
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (*Demography* arc — population question + quantity + what it decomposes, contribution early)

> **Has childlessness risen because successive cohorts are permanently forgoing children (a *quantum*
> shift in completed fertility), or because births are being postponed into ages where they are
> increasingly foregone (a *tempo* shift in timing)?** We show that completed childlessness rose from
> 9.1% of women in the 1960 birth cohort to 18.7% in the 1985 cohort (a 9.6-percentage-point increase,
> 95% CI 8.8–10.4), and that **70% of that rise reflects a genuine quantum decline in cohort fertility
> rather than postponement** that later recuperates. *(Population question + headline quantity with
> magnitude and interval + what it decomposes, in the first breath; "tempo" and "quantum" are defined in
> place for a reader from another component.)*
>
> Separating these two channels is hard because period childlessness and the tempo of childbearing are
> entangled: a cohort that merely postpones looks, in any single period, much like a cohort that will
> end childless, and mortality and migration selection can further distort who remains under
> observation at later reproductive ages. *(Why it is hard — the identification and selection problem,
> stated in demographic terms.)*
>
> We use complete-count vital-registration birth histories linked to population exposures for the 1960
> through 1985 female birth cohorts, observed to age 45, and decompose the change in completed
> childlessness with a parity-progression decomposition that separates the **quantum** component (the
> share who never progress to a first birth) from the **tempo** component (shifts in the age schedule of
> first births), with bootstrap intervals on every component and a competing-risks adjustment for
> mortality and out-migration before age 45. *(Data and demographic method in one paragraph; exposure
> and selection handled explicitly, per `demog-research-design` / `demog-data-analysis`.)*
>
> Of the 9.6-percentage-point rise in childlessness, **6.7 points (70%) are quantum** — women who never
> have a first birth — while **2.9 points (30%) are tempo** — first births postponed past age 40 that do
> not recuperate. The quantum share is concentrated in the 1972–1985 cohorts and among women who reach
> age 30 never-partnered, and it does *not* appear before the 1968 cohort. *(Headline result restated
> with the cohort and subgroup signature — the observable implications from `demog-theory-building`.)*
>
> Our contribution is to show that this population's childlessness transition is **a quantum transition,
> not a postponement that statistics will later revise away** — the opposite reading of the same
> aggregate trend that a period-based account would give. This reframes rising childlessness here as a
> durable change in completed cohort fertility, with direct consequences for projected population growth
> and kin availability. *(Contribution stated early and relative to a specific rival reading.)* The
> decomposition is **portable**: any population scientist facing an aggregate rise in a parity-
> progression ratio can apply it to separate durable quantum change from recoverable tempo distortion,
> in mortality (avoidable vs. postponed deaths) as readily as in fertility. *(Portability — the
> population-science payoff that travels beyond the setting, per `demog-theory-building`.)*
>
> The paper proceeds as follows. Section 2 places the result in the tempo–quantum literature and
> describes the data; Section 3 presents the decomposition and the competing-risks adjustment; Section 4
> reports the cohort and subgroup decomposition and its sensitivity to the selection correction.
> *(Brief roadmap — no over-signposting.)*

---

## Why the "after" meets the *Demography* bar

Mapped to the skill checklists:

- **Contribution front-loaded** — by the end of the first paragraph the reader has the population
  question, the data and method, the finding, and why it matters (`demog-writing-style`: "by the end of
  the introduction the reader knows the population question, the data and method, the finding, and why
  it matters for demography broadly").
- **Quantity-first prose** — the headline number (9.6 pp; 70% quantum) leads with its magnitude **and a
  95% interval**, then is interpreted, rather than "the model shows…" (`demog-writing-style` +
  `demog-data-analysis`: report uncertainty honestly, not just point estimates).
- **Reads past the component** — *tempo* and *quantum* are defined on first use, and the portability note
  speaks to a mortality demographer, satisfying the `demog-topic-selection` general-interest test.
- **Contribution type is explicit** — this is a **decomposition** that separates what prior period-based
  work conflated (tempo vs. quantum), the exact move `demog-theory-building` calls a measurement/
  decomposition contribution.
- **The strongest rival is named and adjudicated** — the postponement (tempo) account would imply later
  recuperation and an earlier-cohort signature; the data show the opposite, satisfying the
  `demog-research-design` adjudication test ("if the rival were true… the cohort pattern would look like
  ___; instead it looks like ___").
- **Selection is handled, not ignored** — mortality and out-migration before age 45 are addressed with a
  competing-risks adjustment, avoiding the `demog-data-analysis` anti-pattern of letting selection
  masquerade as an effect.
- **Method is demoted to a tool**, introduced only where the design is described, never as the lead
  (avoids the `demog-writing-style` "leading with the method" anti-pattern).

> Next: adapt the reproducible analysis skeleton in [`../code/`](../code/) when turning this
> introduction arc into a full empirical workflow.
