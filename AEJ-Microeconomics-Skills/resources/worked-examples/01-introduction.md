> **Illustrative teaching example.** The paper, model, result, and every number below are **fictional**
> and exist only to demonstrate American Economic Journal: Microeconomics (AEJ: Micro) house style for a
> **theory** paper. No real-paper facts are stated. Corresponding skills:
> [`aejmic-writing-style`](../../skills/aejmic-writing-style/SKILL.md),
> [`aejmic-topic-selection`](../../skills/aejmic-topic-selection/SKILL.md),
> [`aejmic-theory-model`](../../skills/aejmic-theory-model/SKILL.md), and
> [`aejmic-identification`](../../skills/aejmic-identification/SKILL.md).

# Worked Example: An AEJ: Micro Theory Introduction (before → after)

This demonstrates the **AEJ: Micro theory-paper intro arc** from
[`aejmic-writing-style`](../../skills/aejmic-writing-style/SKILL.md):
**question / puzzle → model + equilibrium concept (in words) → main result (a proposition, stated in
words) → what drives it / which assumption is doing the work → contribution & scope → brief roadmap.**

Two house rules drive the rewrite and distinguish AEJ: Micro from a specialist theory journal (JET/GEB)
and from an empirical journal (AEJ: Applied):

- AEJ: Micro is **theory-first but broad-interest**. A paper must make the **economic question** legible to
  a general micro audience and lead with a **result a non-specialist can state in one sentence**, not with
  maximal generality ([`aejmic-topic-selection`](../../skills/aejmic-topic-selection/SKILL.md)).
- The deliverable is a **clean, well-motivated proposition** with the **driving assumption named**
  ([`aejmic-theory-model`](../../skills/aejmic-theory-model/SKILL.md),
  [`aejmic-identification`](../../skills/aejmic-identification/SKILL.md)). Any empirical/experimental
  content reports **standard errors, never significance asterisks**.

**Illustrative paper (fictional):** *"Vague by Design: Disclosure and Pooling in a Search Market."*
Fictional setting: a seller with private knowledge of product quality chooses how precisely to disclose it
to consumers who search across sellers at a cost. Every magnitude is invented.

---

## Before (buries the question under machinery — typical first-draft intro)

> We consider a Bayesian game with state space Θ = [0,1], a sender who commits to a signal π: Θ → Δ(M),
> and a receiver with utility u(a,θ). We solve for the sender-optimal signal using the concavification
> approach of the persuasion literature, to which this paper contributes. Under Assumptions 1–4 the
> optimal mechanism is characterized by a fixed point of the operator T defined in Section 3. We also run
> a lab experiment; the treatment effect is significant at the 1% level (***). Section 2 reviews the
> literature, Section 3 sets up the model, Section 4 proves the main theorem, Section 5 reports the
> experiment, and Section 6 concludes.

**What is wrong (against `aejmic-writing-style` / `aejmic-topic-selection` / `aejmic-theory-model`):**

- **Leads with notation and the solution method** (state space, signal operator, concavification) instead
  of the economic question — the named AEJ: Micro anti-pattern ("machinery-first"). This reads like a
  specialist JET paper, not AEJ: Micro.
- **No economic question and no result on page one.** A general micro reader cannot tell what is being
  asked or what is shown.
- **"Contributes to the persuasion literature"** with no named closest result and no delta
  ([`aejmic-literature-positioning`](../../skills/aejmic-literature-positioning/SKILL.md)).
- **The driving assumption is invisible** — "Assumptions 1–4" are never economically motivated, so the
  reader cannot see which one is load-bearing ([`aejmic-identification`](../../skills/aejmic-identification/SKILL.md)).
- **Significance asterisks** ("significant at the 1% level (\*\*\*)") — exactly what AEA house style asks
  authors to avoid; no point estimate, no standard error.
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (AEJ: Micro arc — question + model + proposition-in-words + driving assumption, early)

> **When a seller knows more about quality than buyers do, when does it pay to be deliberately vague —
> and what does that vagueness do to prices?** We study a market in which a seller commits to how precisely
> to disclose its quality and consumers can search across sellers at a cost. We show that the
> seller-optimal disclosure **pools high-quality goods with mediocre ones rather than revealing quality
> fully**, and that this vagueness *raises* the equilibrium price. *(question + result-in-words, in the
> first breath — no notation, no asterisks.)*
>
> The tension is that full disclosure lets a high-quality seller charge more today, but it also sharpens
> consumers' incentive to keep searching when quality looks merely average. Pooling blunts that search
> incentive. *(why the result is not obvious — the economic force, in words.)*
>
> We model disclosure as a commitment to an information structure and solve for the sender-optimal policy
> under a standard solution concept (perfect Bayesian equilibrium with seller commitment). Our main result
> is a **characterization**: *Proposition 1 — the seller-optimal disclosure is a two-message "pass/withhold"
> policy with a quality cutoff, and the cutoff falls as search costs rise.* *(model + equilibrium concept +
> the proposition stated in words; [`aejmic-theory-model`](../../skills/aejmic-theory-model/SKILL.md).)*
>
> **What drives the result is the search friction, not commitment per se.** When search is costless the
> seller discloses fully (Proposition 2); pooling is profitable *only* because costly search makes "looks
> average" enough to deter further shopping — so the search-cost assumption is load-bearing, and we show by
> counterexample that the characterization fails without it.
> *([`aejmic-identification`](../../skills/aejmic-identification/SKILL.md): naming the assumption doing
> the work.)*
>
> Our contribution is a **broadly interesting result, not a new technique**: we identify when strategic
> vagueness is optimal and tie it to a single, measurable primitive — the cost of consumer search. Closest
> is the canonical single-sender persuasion result with no search; we relax that to a *search market* and
> show the optimal policy is coarser and the price higher.
> *([`aejmic-literature-positioning`](../../skills/aejmic-literature-positioning/SKILL.md): the
> theorem-relative delta.)* We do **not** claim the cutoff structure survives when consumers hold
> heterogeneous priors — Section 5 shows it can break — so the scope is markets with a common prior and
> costly search. *(scope stated honestly.)*
>
> The paper proceeds as follows. Section 2 sets up the search market and the disclosure technology;
> Section 3 proves the characterization; Section 4 derives the comparative static in search costs; Section 5
> discusses extensions and limits. *(brief roadmap — no over-signposting.)*

---

## Why the "after" meets the AEJ: Micro bar

Mapped to this pack's skill checklists:

- **First paragraph states the economic question and the result in words** — "when does it pay to be vague,
  and what does it do to prices" plus "pooling raises the price" — no notation, no asterisks
  ([`aejmic-writing-style`](../../skills/aejmic-writing-style/SKILL.md): "main result stated in words on
  page one, with its driving force named").
- **Broad interest is legible** — an IO/information reader and a non-specialist both see the question; the
  paper is not pitched at maximal generality, which would read as JET/GEB
  ([`aejmic-topic-selection`](../../skills/aejmic-topic-selection/SKILL.md)).
- **The result is a clean, numbered proposition** stated in words, with the equilibrium concept named, and
  the *simplest* environment (a two-message policy) that exhibits the mechanism
  ([`aejmic-theory-model`](../../skills/aejmic-theory-model/SKILL.md)).
- **The driving assumption is named and shown necessary** — costless search kills the result (Proposition 2)
  and a counterexample shows the characterization fails without the friction, which is exactly the
  "what makes it tight" bar in [`aejmic-identification`](../../skills/aejmic-identification/SKILL.md).
- **Contribution is a result with scope, not a method** — plus an explicit statement of what is *not*
  shown (heterogeneous priors), satisfying
  [`aejmic-literature-positioning`](../../skills/aejmic-literature-positioning/SKILL.md).
- **Sibling check passes:** this is broad-interest micro theory with the AEA process (AEJ: Micro), not a
  maximal-generality specialist paper (JET/GEB), not a new solution concept (TE/Econometrica), and not an
  empirical applied-micro finding (AEJ: Applied).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified** AEJ: Micro
> papers by area whose introductions execute this arc,
> [`../../skills/aejmic-theory-model/SKILL.md`](../../skills/aejmic-theory-model/SKILL.md) for building the
> model and proof, and
> [`../../skills/aejmic-replication-package/SKILL.md`](../../skills/aejmic-replication-package/SKILL.md) for
> the proof appendix and numerical-example code the AEA Data Editor will expect. For the venue-neutral
> referee objections an empirical or experimental companion must pre-empt, see
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).
