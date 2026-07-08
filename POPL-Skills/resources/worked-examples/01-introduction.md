> **Illustrative teaching example.** The paper, calculus, theorem names, and every
> technical detail below are **fictional**, invented solely to demonstrate the POPL
> first-page arc. No real paper's content is reproduced and no venue policy is
> invented. Companion skills:
> [`popl-writing-style`](../../skills/popl-writing-style/SKILL.md),
> [`popl-topic-selection`](../../skills/popl-topic-selection/SKILL.md), and
> [`popl-reproducibility`](../../skills/popl-reproducibility/SKILL.md).

# Worked Example: A POPL-Style Opening (before → after)

The target is the **informal-to-formal ramp** from `popl-writing-style`: a concrete
program that misbehaves → the principle that explains it → a sharply stated theorem
with its assumptions → what is mechanized → why the machinery transfers beyond this
paper. POPL's 25-pages-of-text budget means the failure mode is rarely space; it is
opening in the formalism instead of the phenomenon.

**Fictional paper:** *"Gradual Session Types with Sound Blame."* Fictional claim: a
gradually typed session calculus where a runtime communication failure is always
attributable to the dynamically typed side.

---

## Before (formalism-first — the draft POPL reviewers bounce off)

> **Abstract.** We present λ<sub>GS</sub>, a novel calculus integrating gradual
> typing with session types. We define its syntax, static semantics, and dynamic
> semantics, and prove several metatheoretic properties, including type safety.
> A prototype implementation demonstrates practicality.
>
> **Introduction.** Session types have received significant attention. Gradual
> typing has also been widely studied. However, their combination remains
> under-explored. This paper fills this gap. We make the following contributions:
> (1) the syntax and semantics of λ<sub>GS</sub>; (2) proofs of type safety and
> blame soundness; (3) a prototype. Section 2 presents syntax, Section 3 the type
> system, Section 4 the dynamics, Section 5 metatheory, Section 6 the prototype.

**Why this fails the POPL read (per `popl-writing-style` / `popl-review-process`):**

- **No phenomenon.** Nothing misbehaves on page 1 — no program, no protocol
  violation, no reason this combination is *hard* rather than merely unwritten.
- **"Fills this gap" is not a principle.** Combining two literatures is framing by
  adjacency; POPL reviewers ask what *new truth* the combination forces you to
  discover.
- **Theorems named, never stated.** "Type safety" and "blame soundness" appear
  with no assumptions, no failure boundary, no hint of which is hard.
- **Mechanization unmentioned** — the evidence a POPL committee weighs most for
  metatheory papers is invisible.
- **"Demonstrates practicality"** is an empirical adjective with no evidence shape
  behind it (`popl-experiments` would strike it).

---

## After (phenomenon → principle → theorem → evidence → transfer)

> **Abstract.** In gradually typed message-passing programs, a runtime protocol
> violation raises an error — but *at the wrong place*: existing systems can blame
> a fully statically typed process for a message forged by untyped code. We present
> λ<sub>GS</sub>, a gradual session calculus whose casts carry protocol-stage
> provenance, and prove **blame soundness**: under a well-formedness condition on
> initial configurations (Def. 3.4), every runtime failure is attributed to a term
> whose static type was `dyn` at the failing stage (Thm. 5.2). The proof is by a
> step-indexed simulation between the blame semantics and an oracle semantics; all
> results except the auxiliary decidability claim (Prop. 6.1, on-paper proof in
> App. D) are mechanized in Rocq. Sound blame is what makes gradual migration
> *diagnosable*: the type checker's promises survive linking with untrusted peers.
>
> **Introduction.** *(¶1 — the misbehaving program.)* Consider a payment service
> whose protocol is statically verified, linked against a legacy client typed
> `dyn`. When the client sends a malformed settlement message, today's gradual
> session systems report the failure *inside the verified service* — the one
> component that provably cannot be at fault. The example is three lines (Fig. 1)
> and runs in our prototype.
>
> *(¶2 — why the obvious fixes fail.)* Wrapping every channel in higher-order
> contracts either re-checks messages the type system already verified, or loses
> track of *which protocol stage* a cast guards, so blame collapses to the whole
> channel. The difficulty is that session types evolve during execution: the blame
> label that was accurate at stage k is stale at stage k+1. *(named technical
> obstacle, not "under-explored.")*
>
> *(¶3 — the principle and the theorem, stated.)* Our observation is that blame
> must be **staged like the protocol itself**. λ<sub>GS</sub> casts carry a
> provenance map from protocol stages to parties; the type system threads it
> through session advancement. We prove: *if the initial configuration is
> well-formed (Def. 3.4 — every channel endpoint's static and dynamic views agree
> on completed stages), then any failing reduction blames a stage typed `dyn` in
> the failing party's view* (Thm. 5.2). Without Def. 3.4 the theorem is false; §5.4
> gives the counterexample.
>
> *(¶4 — evidence, scoped.)* The metatheory is mechanized in Rocq (~9k lines,
> no admits; correspondence table in App. A); Prop. 6.1's decidability argument is
> on-paper only, and we say so. A prototype checks the paper's examples; we make no
> performance claims. *(evidence typed and bounded, per `popl-reproducibility`.)*
>
> *(¶5 — transfer.)* Staged provenance is not specific to sessions: any gradual
> discipline whose types evolve at runtime — typestate, effect protocols — faces
> the stale-blame problem, and §8 sketches the instantiation recipe.

---

## What changed, mapped to the skills

- A **concrete failing program** now precedes any grammar (`popl-writing-style`
  ramp, step 1); the calculus arrives because the example demands it.
- The main theorem is **stated with its load-bearing assumption named and its
  necessity shown** — the counterexample sentence is the credibility move POPL
  committees reward (`popl-review-process`).
- Mechanization status is **claim-by-claim honest**: what is in Rocq, what is
  on-paper, where the correspondence table lives (`popl-reproducibility`).
- "Practicality" was replaced by a **scoped, non-performance role** for the
  prototype (`popl-experiments`).
- The closing paragraph argues **transferability** — the principle outlives the
  calculus — which is `popl-topic-selection`'s core fit signal.

> Next: measure your own opening against the real landmarks in
> [`../exemplars/library.md`](../exemplars/library.md), then check every
> deadline-facing fact in [`../official-source-map.md`](../official-source-map.md).
