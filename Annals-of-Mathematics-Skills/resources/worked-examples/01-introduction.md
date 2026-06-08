> **Illustrative teaching example.** The theorem, the authors, the prior results, and every
> object below are **fictional** and exist only to demonstrate Annals of Mathematics house style
> for a pure-mathematics introduction. No real theorem is proved or claimed here, and no real
> open problem is asserted to be settled. The mathematics is kept simple, self-consistent, and
> deliberately illustrative. Corresponding skills:
> [`anmath-results-framing`](../../skills/anmath-results-framing/SKILL.md),
> [`anmath-methods`](../../skills/anmath-methods/SKILL.md), and
> [`anmath-writing-style`](../../skills/anmath-writing-style/SKILL.md).

# Worked Example: An Annals-Style Introduction for a Pure-Mathematics Paper (before → after)

This demonstrates the **Annals introduction architecture** from
[`anmath-results-framing`](../../skills/anmath-results-framing/SKILL.md):

> **problem & history → precise statement of the Main Theorem (early) → what is new vs. prior
> work → consequences/corollaries → method in one paragraph → organization** —

with the rule that an expert non-specialist should find the **precise main theorem on or near
the first page** and a **proof overview before the details** (`anmath-methods`), written with
**no hidden gaps** (`anmath-writing-style`).

**Illustrative paper (fictional):** *"A sharp spectral gap for random Cayley graphs of
nilpotent groups."* Fictional setting: a hypothetical family of finite nilpotent groups
\(G_n\) and random generating sets, with a fictional prior result by "Hartley (2009)" and a
fictional conjecture attributed to "the Brandt–Oliveira program." None of these exist.

---

## Before (buries the theorem; soft, gappy, method-led)

> Expander graphs and spectral gaps have been studied extensively, and there is a vast
> literature on Cayley graphs of finite groups. In this paper we study random Cayley graphs and
> prove some strong results about their spectral gaps using representation theory and a trace
> method. The nilpotent case is interesting and has attracted attention. After some preliminary
> estimates it is easy to see that the relevant operator norm is small, and a standard argument
> then gives the spectral gap. Our techniques are similar to earlier work but more refined.
> Section 2 recalls preliminaries, Section 3 develops the representation theory, Section 4
> contains the main estimates, and Section 5 proves the theorem, which is stated there.

**What's wrong (against the Annals skills):**

- **No precise theorem on the first page.** The headline statement is deferred to Section 5 —
  the named anti-pattern "burying the main theorem on page 8" in `anmath-results-framing`.
- **"Strong results about" with no statement** — vague significance, no quantifier, no
  hypotheses; a reader cannot tell what is claimed (`anmath-results-framing` anti-pattern).
- **Leads with method** ("using representation theory and a trace method") instead of the
  problem and the theorem.
- **Hidden gaps:** "it is easy to see," "a standard argument then gives," "similar to earlier
  work but more refined" — each is a fatal-gap flag in `anmath-writing-style`; "standard" and
  "similar" arguments are not named or cited.
- **No positioning:** "attracted attention," "earlier work" — no named prior result, no
  statement of what is new (`anmath-results-framing`: name the closest prior result).
- **No proof overview:** the reader has no roadmap of the argument before the details
  (`anmath-methods` "architecture-first").
- **Over-signposted organization** doing the work the argument should do.

---

## After (Annals arc — precise theorem early, advance quantified, proof overview, no gaps)

> A finite group \(G\) with a symmetric generating multiset \(S\) yields a Cayley graph whose
> spectral gap controls mixing of the associated random walk. For abelian \(G\) the gap is
> well understood, but for **nilpotent** \(G\) of unbounded step the size of the gap for a
> *random* generating set of fixed cardinality has remained open. *(problem & history, in two
> sentences.)*
>
> Throughout, \(\{G_n\}\) is a fictional family of finite nilpotent groups of step \(c\) and
> order \(N_n \to \infty\), and \(S_n\) is a multiset of \(k\) elements drawn independently and
> uniformly from \(G_n\). Write \(\lambda(G_n,S_n)\) for the second-largest eigenvalue, in
> absolute value, of the normalized adjacency operator.
>
> > **Main Theorem (fictional, illustrative).** *Fix an integer \(k \ge 3\) and a step bound
> > \(c \ge 1\). There is a constant \(C = C(k,c) > 0\), depending only on \(k\) and \(c\),
> > such that for the family \(\{G_n\}\) above,*
> > \[
> >   \mathbb{P}\!\left[\, \lambda(G_n, S_n) \le \frac{C}{\sqrt{k}} \,\right] \;\longrightarrow\; 1
> >   \qquad (n \to \infty).
> > \]
> > *In words: a random \(k\)-element generating multiset makes \(G_n\) a near-optimal expander,
> > with a gap matching the Alon–Boppana-type bound up to the constant \(C(k,c)\).*
>
> *(The Main Theorem is stated precisely, with all hypotheses and the dependence of the constant
> made explicit, on the first page.)*
>
> **What is new.** The closest prior result is the fictional Hartley (2009), which obtained a
> gap of the form \(\lambda \le C'(\log N_n)^{-1/2}\) — decaying with the group order — and only
> for step \(c = 2\). Our bound is **independent of \(N_n\)**, holds for **every fixed step
> \(c\)**, and is **sharp in \(k\)** up to the constant. Thus we remove the step-2 restriction
> and replace an order-dependent estimate by the optimal order of magnitude. *(advance quantified
> against a named prior result: hypothesis removed, rate sharpened.)*
>
> **Consequences.** Two corollaries follow. First, the random walk on \((G_n, S_n)\) mixes in
> \(O(\log N_n)\) steps with probability tending to one, settling the fictional Brandt–Oliveira
> conjecture for nilpotent groups of bounded step. Second, the same estimate yields explicit
> expander families on nilpotent quotients. *(reach beyond the headline.)*
>
> **Method, in one paragraph.** The proof is a non-abelian trace method. The new ingredient
> (isolated as Proposition 3.1) is a *representation-theoretic flattening lemma*: the
> lower-central-series filtration of \(G_n\) lets us bound a high moment of the adjacency
> operator by a sum over irreducible representations whose dimensions are controlled uniformly
> in the step \(c\). The standard abelian Fourier argument fails here precisely because
> high-dimensional irreducibles dominate the trace; the flattening lemma is what tames them, and
> it is the crux. The remaining steps are a moment computation (Section 4) and a second-moment
> concentration argument (Section 5). *(proof overview before the details; the new idea is named,
> and why the obvious method fails is stated — no "standard argument" hand-waving.)*
>
> **Organization.** Section 2 fixes notation and recalls the representation theory of nilpotent
> groups. Section 3 proves the flattening lemma (Proposition 3.1). Section 4 establishes the
> moment bound, and Section 5 completes the proof of the Main Theorem and deduces the corollaries.

---

## Why the "after" meets the Annals bar

Mapped to the skill checklists:

- **Precise Main Theorem near the first page**, with **all hypotheses explicit** and the
  **constant's dependence stated** ("\(C = C(k,c)\), depending only on \(k\) and \(c\)") —
  `anmath-results-framing` and the `anmath-writing-style` rule on constant dependence and
  quantifier order.
- **The advance is quantified against a named prior result** (fictional Hartley 2009): the
  step-2 hypothesis is removed and the order-dependent rate is sharpened to the optimal order —
  not a vague "improving earlier work" (`anmath-results-framing`).
- **Headline separated from consequences:** one Main Theorem, with two corollaries flagged as
  consequences — so the contribution is unambiguous.
- **Proof overview appears before the details, and the new idea is named as the crux** (the
  flattening lemma, Proposition 3.1), with one sentence on **why the standard abelian Fourier
  approach fails** — exactly the `anmath-methods` architecture-first principle.
- **No hidden gaps:** every "easy to see," "standard argument," and "similar to earlier work"
  from the *before* is gone — replaced by a named lemma, a named prior result, and an explicit
  reason (`anmath-writing-style`).
- **Statement matches the proof:** the introduction claims exactly the high-probability
  \(O(1/\sqrt{k})\) bound the outlined argument delivers — no over- or under-claim.
- **Scope signalled honestly:** the framing positions the result as removing a long-standing
  restriction and settling a (fictional) named conjecture — the significance basis
  `anmath-scope-fit` asks for, without pretending to resolve any real open problem.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified
> Annals of Mathematics papers** whose introductions execute this arc, and
> [`../external_tools.md`](../external_tools.md) for the TeX / AMS typesetting and reference
> tooling used to prepare such a manuscript.
