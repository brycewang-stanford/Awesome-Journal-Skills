> **Illustrative teaching example.** The paper, setting, and every number below are **fictional** and
> exist only to demonstrate REStud house style. No real-paper facts are stated, and no journal policy
> is invented here — for venue facts see [`../official-source-map.md`](../official-source-map.md).
> Corresponding skills: [`restud-writing-style`](../../skills/restud-writing-style/SKILL.md),
> [`restud-literature-positioning`](../../skills/restud-literature-positioning/SKILL.md), and
> [`restud-topic-selection`](../../skills/restud-topic-selection/SKILL.md).

# Worked Example: A REStud-Style Introduction (before → after)

This demonstrates the **REStud introduction arc** from `restud-writing-style`:
**hook & question → what we do (the contribution) → how (the design/idea that makes it work) → what we
find (with magnitude) → why it matters / closest work** — under the journal's two governing constraints:
the contribution is **stated by the end of page 1**, and the prose must read cleanly to **both a
theorist and an applied economist** (the REStud balance since its 1933 founding). The contribution must
be one clean original object — here, **a new identification strategy** (per `restud-topic-selection`).

**Illustrative paper (fictional):** *"Notaries and Credit: How a Profession's Geography Shaped the
Spread of Mortgage Markets."* Fictional setting: a country whose 19th-century law fixed the number of
licensed notaries per district by a population rule, leaving some districts permanently under-served.

---

## Before (buries the contribution — typical first-draft intro)

> The development of credit markets has received considerable attention in economics. A large
> literature studies the determinants of financial development, and many factors have been proposed,
> including legal origin, trust, and institutions. In this paper we revisit this question using
> historical data on notaries, who were important intermediaries in many countries. We use an
> instrumental-variables strategy and also report OLS, fixed-effects, and a battery of robustness
> checks in the appendix. The topic of financial development is important for growth and welfare.
> Section 2 reviews the literature, Section 3 describes the institutional background, Section 4
> presents the data, Section 5 the empirical strategy, Section 6 the results, and Section 7 concludes.

**What's wrong (against `restud-writing-style` / `restud-topic-selection` / `restud-literature-positioning`):**

- **No contribution on page 1.** A reader finishes the paragraph not knowing what is *new* — the core
  REStud failure mode ("an introduction that spends pages on motivation before naming the contribution").
- **Motivation in place of result.** "Has received considerable attention," "is important for growth" —
  the named anti-pattern of selling importance instead of stating the finding.
- **Method paraded, contribution hidden.** It lists IV/OLS/FE/robustness before the reader knows the
  question — heavy machinery is not itself the contribution.
- **Literature as a dump, not an argument.** "legal origin, trust, and institutions" with no closest
  paper confronted — fails the positioning skill's "argument, not a list."
- **No "why not before" clause** — nothing tells the reader why this question was previously unanswerable.
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (REStud arc — contribution by end of page 1, legible to theorist and applied reader)

> Why do credit markets take root in some places and not others? We provide new causal evidence that
> the **local supply of contract-enforcing intermediaries** — not just law or culture in the abstract —
> determines whether a mortgage market forms. *(hook + the broad question, stated so a non-specialist
> on either side of the field cares.)*
>
> Our contribution is **a new identification strategy**: a 19th-century statute fixed the number of
> licensed notaries in each district by a step function of population, so two otherwise-similar
> districts on opposite sides of a population threshold were assigned sharply different notary density
> for purely administrative reasons. This rule lets us isolate the effect of intermediary supply from
> the demand for credit that ordinarily moves with it. *(what we do — one clean original object — and
> the idea that makes it work, by the top of page 1.)*
>
> Districts just above a threshold received roughly **30% more notaries per capita**, and we use this
> discontinuity to estimate the effect on credit. A district with one additional notary per ten
> thousand residents had a mortgage-origination rate **5.2 percentage points** higher two decades later,
> off a base of 18%. The effect is absent before the statute and concentrated where alternative
> enforcement was weakest. *(what we find — headline magnitude with units — and the variation that
> identifies it; the placebo-in-time reassures the applied reader, the mechanism the theorist.)*
>
> This speaks directly to the closest work. The legal-origin literature (e.g., a canonical cross-country
> study) shows *which legal systems* correlate with finance but cannot separate law from the agents who
> operate it; a recent paper on trust establishes a cultural correlate but not a supply channel.
> **We confront both: holding law and culture fixed within a country, the marginal enforcer still moves
> the market.** The question could not be answered before because the notary-assignment rule had not
> been digitized at the district level — there was no lever that shifted enforcement supply without
> shifting demand. *(why it matters, positioned against the nearest papers as an argument; the
> "why not before" clause supplies the originality spine.)*
>
> The paper proceeds as follows. Section 2 describes the statute and the assignment rule; Section 3
> presents the discontinuity design and the main estimates; Section 4 examines the enforcement
> mechanism. *(brief roadmap — no over-signposting.)*

---

## Why the "after" meets the REStud bar

Mapped to the skill checklists:

- **Contribution stated by the end of page 1** — `restud-writing-style`'s first checklist item; the new
  identification strategy is named in the second paragraph, not deferred to Section 5.
- **Result-forward, not motivation-forward** — the headline magnitude (5.2 pp; ~30% more notaries) appears
  with units, satisfying "we show X" rather than "X is important and understudied."
- **One clean original object** — exactly one of {new model, new design, new fact}: here a **new
  identification strategy** (`restud-topic-selection`), not a bundle. The contribution sentence fills
  cleanly: *"We show that intermediary supply causes mortgage-market formation, which is new because
  prior work could not separate enforcers from law/demand, established via a notary-assignment
  discontinuity, and this matters for why finance develops unevenly."*
- **Legible to both audiences** — the placebo-in-time and discontinuity reassure the applied econometrician
  (hand off to [`restud-identification`](../../skills/restud-identification/SKILL.md)); the
  supply-vs-demand framing speaks to the theorist — the REStud balance.
- **Positioning is an argument, not a list** (`restud-literature-positioning`): the two closest strands are
  **confronted in the introduction**, each with "what it could not do," and the marginal contribution is
  one sentence relative to them — closest competitors cited in the text, never buried in a footnote.
- **"Why not before" clause present** — the un-digitized assignment rule — supplying the originality spine
  the positioning skill requires.
- **Author-date references** ("a canonical cross-country study," rendered as `Author (Year)` in a real
  draft), consistent with REStud house style; never numbered.
- **Economy** — five short paragraphs; main text carries intuition while full proofs/robustness go to the
  online appendix, consistent with the ~45-page discipline. Verify the current page and abstract limits on
  the journal's official author guidelines before submission (do not rely on this file for policy).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for verified real REStud papers whose
> introductions execute this arc, and [`../code/`](../code/) for the RDD / IV command chain a design like
> the one above would adapt.
