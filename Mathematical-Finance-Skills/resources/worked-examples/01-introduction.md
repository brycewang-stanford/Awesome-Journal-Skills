> **Illustrative teaching example.** The paper, model, theorem, and every symbol below are
> **fictional** and exist only to demonstrate *Mathematical Finance* house style. No real-paper
> facts, no policy, and no empirical claims are stated. Corresponding skills:
> [`mathfin-writing-style`](../../skills/mathfin-writing-style/SKILL.md),
> [`mathfin-contribution-framing`](../../skills/mathfin-contribution-framing/SKILL.md),
> [`mathfin-topic-selection`](../../skills/mathfin-topic-selection/SKILL.md), and
> [`mathfin-literature-positioning`](../../skills/mathfin-literature-positioning/SKILL.md).

# Worked Example: A *Mathematical Finance*-Style Introduction (before → after)

This demonstrates the **theorem-first introduction arc** that the skills in this pack require for a
*Mathematical Finance* (Wiley) submission. Unlike an empirical-economics intro (question → headline
number → policy), a math-finance intro leads with a **financial-modelling problem**, names the
**obstruction** prior machinery hit, and states the **main theorem as the resolution** — with
assumptions visible and the financial payoff (pricing / hedging / risk / portfolio) spelled out. The
controlling skills are:

- `mathfin-topic-selection` — the fit bar is *methodological novelty + contribution to financial
  modelling, with a result that needs a proof*; routine computation on data is off-fit.
- `mathfin-contribution-framing` — lead with the modelling problem, name the novelty axis, translate
  the theorem into a modelling statement, bound the claim to its hypotheses.
- `mathfin-writing-style` — define before use (probability space, filtration, admissible strategies,
  integrability); number assumptions and results; separate intuition from proof.
- `mathfin-literature-positioning` — position at the **theorem level**, naming the closest prior
  result, its assumptions, and exactly which assumption you relax.

**Illustrative paper (fictional):** *"Utility-Indifference Pricing of Defaultable Claims under a
Rough-Volatility Reference Filtration: A Verification Theorem."* Fictional model: a defaultable
contingent claim written on an asset whose log-volatility is driven by a fractional process, traded by
an agent who cannot perfectly hedge the default event.

---

## Before (theorem-dump / topic-level — typical first-draft intro)

> Stochastic volatility and credit risk have both been studied extensively in the mathematical-finance
> literature. In this paper we consider utility-indifference pricing. We work on a filtered probability
> space and assume the volatility is rough. We use the dynamic programming principle and BSDE
> techniques to characterize the value function. We prove a verification theorem and provide numerical
> experiments calibrated to market data showing that our prices fit observed CDS spreads well. Section 2
> sets up the model, Section 3 states the main results, Section 4 gives the proofs, Section 5 presents
> the numerical study, and Section 6 concludes.

**What's wrong (against the pack's skills):**

- **Leads with a topic, not a theorem.** "have both been studied extensively" is the survey opening
  `mathfin-literature-positioning` warns against; the reader cannot tell which prior theorem is being
  sharpened or which assumption is relaxed.
- **No modelling problem and no obstruction.** `mathfin-contribution-framing` requires *problem →
  obstruction → theorem as resolution*; here the contribution axis (new model? weaker assumption?
  constructive solution?) is never named.
- **Assumptions invisible.** "assume the volatility is rough" hides the probability space, filtration,
  admissibility, and integrability that `mathfin-writing-style` requires *before use*; the theorem's
  scope cannot be read off the prose.
- **Numerics framed as the contribution.** "fit observed CDS spreads well" presents calibration to
  market data as the result — exactly the off-fit pattern `mathfin-topic-selection` and
  `mathfin-data-analysis` rule out for this theory-first venue.
- **Over-signposted roadmap** doing the argument's job, and "well" is an unproven empirical claim.

---

## After (theorem-first arc — modelling problem → obstruction → theorem → payoff → scope)

> **How should an agent who cannot hedge default risk price a defaultable claim when the reference
> asset's volatility is rough — and does a well-posed indifference price even exist in that
> non-Markovian, incomplete market?** We give a constructive answer: under Assumptions (A1)–(A4) the
> utility-indifference price is the unique solution of a quadratic backward stochastic differential
> equation driven by the enlarged default filtration, and we characterize the optimal hedging strategy
> in feedback form. *(modelling problem + the theorem's deliverable, stated in the first breath, with
> the result that needs a proof named.)*
>
> The difficulty is that roughness breaks the tools that make this problem tractable. When
> log-volatility is driven by a fractional process with Hurst index $H<\tfrac12$, the model is
> **non-Markovian**, so the Hamilton–Jacobi–Bellman PDE and the verification theorems of the Markovian
> stochastic-control literature no longer apply; and because the default event is **not hedgeable**,
> the market is incomplete and no equivalent martingale measure prices the claim uniquely. *(the
> obstruction prior machinery hits — stated at the theorem level, per `mathfin-literature-positioning`.)*
>
> We work on a filtered probability space $(\Omega,\mathcal F,(\mathcal G_t)_{0\le t\le T},\mathbb P)$,
> where $(\mathcal G_t)$ is the progressive enlargement of a Brownian reference filtration by the
> default time $\tau$. The agent maximizes expected exponential utility over admissible strategies —
> predictable, self-financing, and square-integrable under (A2). **Assumption (A1)** fixes the rough
> log-volatility dynamics; **(A2)** the admissibility and integrability class; **(A3)** an intensity
> (conditional density) hypothesis on $\tau$ making the default totally inaccessible; **(A4)** a
> boundedness condition on the claim's payoff. *(define before use; assumptions numbered and visible,
> per `mathfin-writing-style`.)*
>
> **Theorem 3.1 (Verification and representation).** *Under (A1)–(A4), the exponential
> utility-indifference price $p_t$ of the defaultable claim is the unique $\mathcal G_t$-adapted
> solution of a quadratic BSDE with a bounded terminal condition; the value function admits the
> stochastic representation $V_t=-\exp(-\gamma(X_t-p_t))$, and the indifference-hedging strategy is the
> $Z$-component of that BSDE in feedback form.* In financial terms, this means the price is
> **well-defined and computable as a BSDE** in a market where neither PDE methods nor a unique pricing
> measure are available, and the hedge is read directly off the solution. *(theorem stated with scope
> visible, then translated into a modelling statement — the `mathfin-contribution-framing` step.)*
>
> Our contribution is **constructive existence-and-uniqueness where prior work had only existence under
> Markovian or complete-market assumptions**: we replace the HJB/verification route with a quadratic-BSDE
> argument in the enlarged filtration, so the result holds for $H<\tfrac12$ and for genuinely
> unhedgeable default. The novelty axis is a **weaker assumption set** (non-Markovian volatility,
> incomplete market) carried by a **new method** (default-enlarged quadratic BSDE), not a special case
> of an existing verification theorem. *(novelty axis named; special-case objection pre-empted, per
> `mathfin-literature-positioning`.)* **We do not claim** model completeness, a closed-form price, or
> any empirical fit; numerical experiments in Section 5 only **illustrate the proven $O(n^{-1/2})$
> Monte-Carlo convergence rate** of a BSDE scheme, in keeping with the journal's rule that numerics
> support the theory rather than constitute it. *(scope bounded to the hypotheses; numerics subordinated,
> per `mathfin-topic-selection` / `mathfin-data-analysis`.)*
>
> The paper is organized as follows. Section 2 fixes the model and states Assumptions (A1)–(A4);
> Section 3 proves Theorem 3.1; Section 4 derives the feedback hedge; detailed estimates are deferred to
> the Appendix. *(brief roadmap; detailed mathematics moved to the Appendix, as the journal asks.)*

---

## Why the "after" meets the *Mathematical Finance* bar

Mapped to the pack's skill checklists:

- **Theorem-first, not topic-first** — the opening states the modelling problem *and* what gets proved
  (constructive existence/uniqueness via BSDE), satisfying `mathfin-topic-selection`'s "what is the
  theorem, in one sentence, and why is it new?"
- **Problem → obstruction → resolution** — non-Markovian roughness and unhedgeable default are named as
  the precise obstructions before the theorem is stated, the structure `mathfin-contribution-framing`
  requires.
- **Assumptions defined before use and numbered** — probability space, enlarged filtration,
  admissibility/integrability, and (A1)–(A4) are visible, so a referee can read the theorem's scope off
  the prose (`mathfin-writing-style`).
- **Theorem-level positioning** — the delta is stated as a *weaker assumption set carried by a new
  method*, explicitly not a corollary of an existing verification theorem (`mathfin-literature-positioning`).
- **Scope honesty** — the intro states what is **not** claimed (no completeness, no closed form, no
  empirical fit), consistent with the rigor culture that penalizes over-claiming.
- **Numerics subordinated to theory** — the experiments illustrate a *proven* convergence rate, never
  market calibration as a result, keeping the paper on-fit for a theory-first venue
  (`mathfin-data-analysis`).
- **One-sentence hook is fillable:** "We show that [the indifference price of a defaultable claim under
  rough volatility] is [the unique solution of a default-enlarged quadratic BSDE]" — the modelling
  problem and the theorem both filled, as `mathfin-contribution-framing` requires.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified**
> *Mathematical Finance* papers whose introductions execute this theorem-first arc across risk
> measures, arbitrage theory, term-structure and rough-volatility models, Lévy pricing, and
> transaction-cost portfolio control; and [`../official-source-map.md`](../official-source-map.md) for
> the journal's self-contained-proofs, appendix, and numerics-support-theory rules.
