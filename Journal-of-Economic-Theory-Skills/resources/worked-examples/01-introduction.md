> **Illustrative teaching example.** The paper, model, theorem, and every statement below are
> **fictional** and exist only to demonstrate JET house style. No real-paper facts, parameters, or
> policy claims are made. Corresponding skills:
> [`jet-writing-style`](../../skills/jet-writing-style/SKILL.md),
> [`jet-contribution-framing`](../../skills/jet-contribution-framing/SKILL.md),
> [`jet-topic-selection`](../../skills/jet-topic-selection/SKILL.md), and
> [`jet-identification-strategy`](../../skills/jet-identification-strategy/SKILL.md).

# Worked Example: A JET-Style Introduction (before → after)

This demonstrates the **JET introduction arc** from `jet-contribution-framing` and `jet-writing-style`:
**the question theoretically posed → the result stated as a theorem → why it matters (the delta from
prior theory) → what it does *not* claim (scope guardrail) → subfield signal**, with the JET rule that
a desk editor and two expert referees must **see the theoretical contribution on the first page**. A
JET introduction is *not* a data-story arc — it is a precise statement of *what is now known that was
not before*. The lead deliverable is a **theorem (or a genuinely new model / characterization)**, not a
regression coefficient (`jet-topic-selection` scope gate).

**Illustrative paper (fictional):** *"Robust Disclosure to a Privately Informed Receiver: A
Characterization."* Fictional setting: a sender commits to an information-disclosure rule before a
receiver with privately known preferences takes an action; the sender does not know the receiver's
type. (Mechanism design / information economics — entirely invented for teaching.)

---

## Before (buries the result — typical first-draft intro)

> The economics of information has been studied extensively. A large literature considers how a sender
> can influence a receiver by choosing what information to reveal, and there has been much recent
> interest in problems of this kind. In this paper, we study a disclosure problem. We set up a model
> with a sender and a receiver, the receiver has private information, and we use a fixed-point argument
> together with duality methods to analyze the sender's problem. We believe our framework is quite
> general and our results are robust. We also discuss several examples and extensions. Section 2
> presents the model, Section 3 states assumptions, Section 4 contains the analysis, Section 5 gives
> examples, and Section 6 concludes. Proofs are in the appendix.

**What's wrong (against `jet-contribution-framing` / `jet-writing-style` / `jet-topic-selection`):**

- **No theorem on page one.** A desk editor cannot tell what is *proved*; "we study a disclosure
  problem" is a topic, not a result — fails the `jet-topic-selection` gate ("state the result you would
  put in the abstract as a proposition/theorem").
- **Leads with method** ("a fixed-point argument together with duality methods") instead of the
  characterization — the method is a tool, not the contribution (`jet-identification-strategy`).
- **Overclaiming without a stated scope** ("quite general," "robust") — exactly the "general / robust /
  essentially" language `jet-contribution-framing` forbids unless the theorem literally says so.
- **No delta from prior theory** — which assumption it weakens, which result it generalizes or overturns
  is never named (`jet-literature-positioning`).
- **No scope guardrail** — finite types? a specific preference domain? — so a referee will read in a
  stronger claim than the proof supports.
- **No subfield signal**, so the submission is not routed to the matching editor.
- **An empirical-paper voice** (topic → "framework" → examples → extensions) imposed on a theory result.

---

## After (JET arc — theorem first, delta and scope explicit)

> A sender commits to a disclosure rule before a receiver, whose preferences are private information,
> chooses an action. **We characterize exactly the disclosure rules that are *robustly optimal* for the
> sender — those that maximize her payoff against the worst-case receiver type — and show that every
> such rule is a *monotone partition* of the state space.** *(The question, theoretically posed, and the
> headline result stated as a theorem, in the first breath.)*
>
> Formally, let the state lie in a compact interval and the receiver's type index a single-crossing
> family of action preferences. **Theorem 1** establishes that a disclosure rule is robustly optimal if
> and only if it induces a partition of the state space into intervals; **Theorem 2** shows the optimal
> partition is unique and characterizes its thresholds by a system of indifference conditions.
> *(Two distinct statements — a characterization and a uniqueness/comparative-statics result — not
> collapsed into one vague claim, per `jet-identification-strategy`.)*
>
> The result matters because it **weakens the common-prior and known-receiver assumptions** under which
> full or interval disclosure was previously derived: when the sender faces ambiguity over the
> receiver's type, optimal disclosure is *coarser* than under a known receiver, and the coarsening is
> pinned down by a single robustness margin rather than by fine details of the prior. *(Why it matters,
> as a delta from a specific prior view — the `jet-contribution-framing` step 3.)*
>
> Our characterization holds under **single-crossing preferences and a compact one-dimensional state**;
> we do **not** claim it for multidimensional states or non-monotone preferences, where a counterexample
> (Section 4) shows the partition structure can fail. *(Scope guardrail stated in the introduction, not
> hidden in a footnote — `jet-identification-strategy`'s "any restriction is flagged as a scope limit.")*
>
> The key step is an **envelope/revelation argument** that reduces the sender's infinite-dimensional
> robust problem to a finite system of indifference conditions; we state the lemma chain in dependency
> order and offload the measure-theoretic details to the appendix. *(Proof spine named and motivated —
> method introduced only where the architecture is discussed, never as the lead.)*
>
> This is a contribution to **mechanism design and information economics** (Bayesian persuasion under
> ambiguity); the area signal routes the paper to the matching editor. *(Subfield signal, per
> `jet-topic-selection` "name the area early.")*

---

## Why the "after" meets the JET bar

Mapped to the skill checklists:

- **Theorem on page one** — Theorem 1 (characterization) and Theorem 2 (uniqueness) appear immediately,
  each self-contained, satisfying `jet-contribution-framing`'s "lead with the theorem" and
  `jet-topic-selection`'s "state the result you would put in the abstract as a proposition/theorem."
- **Characterization vs. uniqueness vs. comparative statics are separated** into distinct numbered
  statements — the `jet-identification-strategy` rule against bundling genericity, existence, and
  uniqueness into one claim.
- **The claim is right-sized** — "robustly optimal" and "monotone partition" are exactly what is proved;
  the draft avoids "general" and "robust" as loose adjectives, reserving "robust" for its defined
  worst-case-type meaning (`jet-contribution-framing` right-sizing rule).
- **The delta from prior theory is explicit** — it *weakens* the common-prior / known-receiver
  assumption and yields a *coarser* optimum, stated relative to a specific prior view, not a vague "we
  contribute to the literature" (`jet-literature-positioning`).
- **Scope guardrail is in the intro** — single-crossing, one-dimensional, compact; multidimensional and
  non-monotone cases are flagged as out of scope with a promised counterexample, so no referee reads in
  a stronger claim (`jet-identification-strategy`).
- **Method is demoted to a tool** — the envelope/revelation argument is named where the proof
  architecture is discussed, never as the headline (avoids the "leading with the method" anti-pattern in
  both `jet-identification-strategy` and `jet-writing-style`).
- **Subfield is named** for editor routing (`jet-topic-selection`).
- **No empirical-paper voice** — there is no data story; the arc is question → theorem → delta → scope →
  proof spine, the theory-first structure `jet-writing-style` requires.

> One-line abstract sentence (fillable, per `jet-contribution-framing`): "We characterize the
> [robustly optimal disclosure rules] and show every one is a [monotone partition], weakening the
> [known-receiver assumption]." All three brackets filled with what the proof delivers.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified JET papers**
> whose introductions execute this theorem-first arc, and
> [`../official-source-map.md`](../official-source-map.md) for JET's authoritative scope, review model,
> and house-style policy. For polishing the statements and notation, use
> [`../../skills/jet-writing-style/SKILL.md`](../../skills/jet-writing-style/SKILL.md).
