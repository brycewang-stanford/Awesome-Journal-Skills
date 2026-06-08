> **Illustrative teaching example.** The paper, setting, mechanism, and every number below are
> **fictional** and exist only to demonstrate *The Journal of Politics* (JOP) house style. No real-paper
> facts and **no journal policy** are stated here. Corresponding skills:
> [`jop-writing-style`](../../skills/jop-writing-style/SKILL.md),
> [`jop-topic-selection`](../../skills/jop-topic-selection/SKILL.md),
> [`jop-theory-building`](../../skills/jop-theory-building/SKILL.md),
> [`jop-literature-positioning`](../../skills/jop-literature-positioning/SKILL.md), and
> [`jop-research-design`](../../skills/jop-research-design/SKILL.md).

# Worked Example: A JOP-Style Introduction (before → after)

This demonstrates the **JOP introduction arc** assembled from this pack's skills:
**substantive political question → live debate the paper enters → testable theory + mechanism →
identification strategy that adjudicates the strongest rival → headline estimate with its interval →
contribution & scope conditions → brief roadmap.**

The JOP-specific bar layered on top of a generic empirical intro:

- The question must be of **general interest across subfields** and the argument **testable** — a
  directional claim with a stated estimand, not a theme (`jop-topic-selection`, `jop-theory-building`).
- JOP is **methodologically diverse** but makes **acceptance contingent on replicability**: the design
  must be one a **JOP replication analyst** could re-run, so the estimand, data, and analysis are stated
  plainly (`jop-research-design`, `jop-replication-and-data-policy`).
- JOP counts **pages, not words** (Research Article ≤ 35 pp, inclusive of notes, references, and
  exhibits), so the intro earns its space — lead with the estimate and its interval, then interpret;
  push apparatus to the Online Appendix (`jop-writing-style`).
- The contribution is staked as a **move against a named rival explanation** (`jop-literature-positioning`),
  and because JOP is **double-blind**, the author's own prior work is referred to in the **third person**.

**Illustrative paper (fictional):** *"Do Local Election Observers Deter Vote Buying? Evidence from a
Randomized Monitoring Roll-Out."* Fictional setting: a (made-up) developing democracy where an NGO
randomly assigned independent observers to polling stations in one election cycle.

---

## Before (buries the contribution — typical first-draft intro)

> Electoral integrity is a major topic in comparative politics, and many scholars have studied vote
> buying. In this paper, we study election observers. We use data from a recent election and run a
> regression of vote buying on the presence of observers, controlling for district characteristics. As we
> argued in our prior work, monitoring can shape behavior. We also report matching and instrumental-
> variables models as robustness checks. Clean elections are important for democracy. Section 2 reviews
> the literature, Section 3 describes the data, Section 4 presents the methods, Section 5 reports results,
> and Section 6 concludes.

**What's wrong (against the JOP skills):**

- **No substantive question and no estimand on page one.** A reader cannot tell what causal quantity is
  claimed (`jop-writing-style`: contribution by end of intro; `jop-topic-selection`: general-interest,
  testable).
- **Leads with method and a robustness inventory** instead of the argument, and an **observational
  regression with controls** is presented as identification where a randomized design is actually
  available (`jop-research-design`).
- **"As we argued in our prior work"** breaks **double-blind anonymity** (`jop-writing-style`).
- **No live debate named** and **no rival explanation**, so the design's leverage is invisible
  (`jop-literature-positioning`, `jop-research-design`).
- **No headline estimate with uncertainty** — violates quantity-first prose.
- **Throat-clearing** ("major topic," "important for democracy") and an **over-signposted roadmap** that
  also wastes scarce **pages** (`jop-writing-style`).

---

## After (JOP arc — question + estimand + identification, contribution early)

> **Can independent monitoring actually deter electoral fraud, or do parties simply move vote buying to
> stations no one is watching?** We show that randomly assigning a trained observer to a polling station
> **cut reported vote buying by 6.4 percentage points (95% CI 4.1–8.7)** in the monitored stations — but
> that fraud **rose by 3.1 points in nearby unmonitored stations in the same constituency**, so the net
> constituency-level effect is roughly half the station-level estimate. *(substantive question + headline
> estimate with interval + the displacement that qualifies it, in the first breath.)*
>
> This speaks to a live debate about whether election monitoring **deters** manipulation or merely
> **displaces** it. *(the debate the paper enters, legible to Americanists and comparativists alike.)*
> The pure-deterrence view predicts a clean station-level drop with no spillover; our contribution is to
> show that observers **deter where they stand but displace nearby**, which reframes monitoring as a
> *reallocation* technology and means station-level estimates overstate the integrity gain. *(contribution
> stated early, as a move against the named rival.)*
>
> The mechanism is a cost-of-fraud story: an observer raises the probability that manipulation at *that*
> station is detected and sanctioned, so parties shift effort to lower-risk stations they still control —
> displacement that should appear only where parties have nearby unmonitored options. *(mechanism — who,
> why, under what constraint — with a clear prediction about *where* fraud should reappear.)* It should
> weaken where every station in a constituency is monitored, or where parties lack a local presence
> elsewhere. *(scope conditions.)*
>
> Identifying this cleanly is hard because observers are usually **sent to the riskiest places**, so a raw
> comparison confounds monitoring with the fraud propensity that drew the monitors — the selection story a
> referee raises first. We use the NGO's **randomized assignment** of observers across stations, which
> breaks that selection, and we measure spillover by comparing unmonitored stations near a monitored one
> to unmonitored stations in all-unmonitored constituencies, with randomization inference and clustering
> at the constituency level. *(identification built to adjudicate the rival, with the spillover design and
> inference stated for a replication analyst to re-run.)* **If observers only deterred and never displaced,
> nearby unmonitored stations would look like distant ones; instead, fraud is measurably higher precisely
> next to monitored stations.** *(the adjudication sentence — what the data would show under the rival vs.
> under our argument.)*
>
> Vote buying falls by **6.4 points** off a base of 19% at monitored stations and rises by **3.1 points**
> at adjacent unmonitored stations, with the spillover concentrated in constituencies where a party
> controls multiple stations — the displacement signature the reallocation mechanism predicts and pure
> deterrence does not. *(headline result restated with the test that separates the two theories.)*
>
> The paper proceeds as follows. Section 2 develops the deterrence-versus-displacement argument and its
> observable implications; Section 3 describes the randomization and the spillover design; Section 4
> reports the station- and constituency-level effects and the heterogeneity by party presence. Derivations
> and balance tables are in the Online Appendix. *(brief roadmap — apparatus pushed to the appendix to
> protect the page budget.)*

---

## Why the "after" meets the JOP bar

Mapped to the skill checklists:

- **Substantive question + testable estimand stated by end of intro** — the deterrence-vs-displacement
  claim is directional, the estimand (an ATT on vote buying, plus a spillover) is explicit, and the
  headline magnitudes (6.4 pp and 3.1 pp, with a 95% interval) appear immediately with units
  (`jop-topic-selection`; `jop-writing-style` quantity-first).
- **Positioned as a move in a live debate** ("deter vs. displace"), engaging the rival on its terms rather
  than piling cites (`jop-literature-positioning`).
- **Identification defended and replicable** — randomized assignment breaks the selection that confounds
  observational designs, and the spillover comparison, randomization inference, and clustering are stated
  so a **JOP replication analyst** could re-run them (`jop-research-design`,
  `jop-replication-and-data-policy`).
- **The strongest rival is named and adjudicated** — pure deterrence would imply no spillover; the data
  show higher fraud next to monitored stations instead (`jop-research-design` adjudication test).
- **Mechanism made observable** — the by-party-presence heterogeneity ties the reallocation story to
  *where* displacement should appear, the move `jop-theory-building` calls deriving observable
  implications.
- **Scope conditions stated** — displacement should vanish under saturation monitoring or absent a local
  party network — so the claim is bounded, not universal (`jop-theory-building`).
- **Fits the page budget and stays anonymous** — apparatus is pushed to the Online Appendix and
  self-citation is removed, preserving the **35-page** budget and **double-blind** review
  (`jop-writing-style`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified JOP papers**
> whose introductions execute this arc across experimental, formal, and observational work, and
> [`../code/`](../code/) for the randomized-design command chain referenced above. Pre-empt referees with
> the shared
> [`reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md)
> and report to the shared
> [`reporting-standards.md`](../../../shared-resources/empirical-methods/reporting-standards.md).
