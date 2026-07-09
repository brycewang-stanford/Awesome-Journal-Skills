> **Illustrative teaching example.** The problem, theorem, bounds, and every number below are
> **fictional** and exist only to demonstrate ICALP house style. No real-paper facts, results, or
> constants are stated, and no policy is invented. Corresponding skills:
> [`icalp-writing-style`](../../skills/icalp-writing-style/SKILL.md),
> [`icalp-topic-selection`](../../skills/icalp-topic-selection/SKILL.md), and
> [`icalp-experiments`](../../skills/icalp-experiments/SKILL.md).

# Worked Example: An ICALP-Style Abstract + Introduction (before → after)

This demonstrates the **ICALP first-page arc** from `icalp-writing-style`:
**problem in a precise model → what was known and why it was stuck → the theorem, stated exactly →
the technique that breaks the barrier → where the argument lives (body + full version)** — with the
ICALP expectations that the **model is fixed before the theorem**, the **improvement is stated against
a named prior bound**, and a reader can see the contribution **without opening the proof**.

The framing also reflects `icalp-topic-selection`: this is a **Track A** result (an algorithm with a
provable bound), it is a *theorem* rather than an empirical system, and it could not simply be
re-labelled a Track B (automata/logic) paper without losing its point.

**Illustrative paper (fictional):** *"A Deterministic Fully-Dynamic Algorithm for Bounded-Genus
Reachability with Sub-Polynomial Update Time."* Fictional contribution: a data structure maintaining
single-source reachability under edge insertions and deletions on graphs of bounded genus.

---

## Before (buries the theorem — typical first-draft abstract + intro)

> **Abstract.** Dynamic graph algorithms are an important and active area. We study reachability,
> which has many applications. We design a new algorithm using a clever combination of known
> techniques and show experimentally that it is fast on several benchmark graphs, outperforming
> previous implementations. Our approach demonstrates the promise of dynamic data structures.
>
> **Introduction.** Graphs are everywhere and change over time. Maintaining reachability under
> updates is a natural problem that people have studied a lot. In this paper we give a new algorithm
> and evaluate it. Section 2 has preliminaries, Section 3 our algorithm, Section 4 experiments, and
> Section 5 concludes.

**What's wrong (against `icalp-writing-style` / `icalp-topic-selection` / `icalp-experiments`):**

- **No model and no theorem on the first page.** ICALP reviewers want the exact computational model
  (deterministic? fully dynamic? what update operations? what complexity measure?) and the theorem
  statement, not a mood.
- **The contribution is a benchmark win, not a bound.** "Fast on benchmark graphs" is an
  experimental-algorithms claim; ICALP Track A judges a **provable** update-time bound. As written,
  the paper reads as mis-routed to an experimental venue (an `icalp-topic-selection` re-route signal).
- **No positioning against a prior bound.** "A clever combination of known techniques" hides whether
  anything is actually improved and by how much.
- **The barrier is never named.** A dynamic-algorithms reader immediately asks what *conditional
  lower bound* or prior obstacle this update time gets past; the draft is silent.
- **Over-signposted roadmap** substituting for the statement of a result.

---

## After (ICALP arc — model → prior state → theorem → technique → where the proof lives)

> **Abstract.** We consider **fully dynamic single-source reachability** on directed graphs of genus
> at most *g*, in the standard model where each update inserts or deletes one edge and each query asks
> whether a fixed source reaches a given vertex. The best previous deterministic data structures
> required update time polynomial in *n*, and a known reduction suggested polynomial update time might
> be unavoidable for general graphs. We show that **bounded genus breaks this barrier**: we give a
> **deterministic** data structure with **n^{o(1)}** worst-case update and query time (with the
> dependence on *g* stated in Theorem 1), the first sub-polynomial deterministic bound for this class.
> The technique is a genus-aware hierarchical separator decomposition maintained under updates; we
> also show the genus dependence is necessary up to the stated form (Theorem 2). Full proofs are in
> the appendix and the arXiv full version. *(model → prior bound + barrier → exact theorem → technique
> → matching necessity — all on the first page.)*
>
> **Introduction.** *(¶1 — the problem in a precise model, first breath.)* A dynamic reachability data
> structure maintains a directed graph under edge insertions and deletions and answers, for a fixed
> source *s* and a query vertex *v*, whether *s* reaches *v*. We work in the **fully dynamic**,
> **worst-case update time** setting with a deterministic algorithm — the strongest of the usual
> variants, and the one where the fewest positive results are known.
>
> *(¶2 — what was known and why it was stuck.)* For general directed graphs, the best deterministic
> update time is polynomial in *n*, and a fine-grained reduction from a well-studied problem gives
> evidence that **sub-polynomial update time is unlikely in general**. This is the barrier: any
> sub-polynomial result must exploit structure the hardness reduction destroys.
>
> *(¶3 — the theorem, stated exactly.)* Our main result is **Theorem 1**: for directed graphs of
> genus at most *g*, there is a deterministic fully dynamic single-source reachability structure with
> worst-case update and query time **n^{o(1)}**, where the hidden dependence on *g* is as stated. To
> our knowledge this is the first sub-polynomial deterministic bound for any non-trivial graph class
> in this setting.
>
> *(¶4 — the technique that breaks the barrier.)* The engine is a **hierarchical separator
> decomposition tailored to bounded genus**, maintained incrementally so that each update touches only
> a sub-polynomial number of pieces. Bounded genus is exactly the structure the general-case hardness
> reduction cannot produce, which is why the barrier does not apply. We state the decomposition and its
> update procedure in Section 3 and prove the invariants in Section 4.
>
> *(¶5 — matching necessity and where the proof lives.)* We complement the algorithm with **Theorem 2**,
> showing the genus dependence cannot be removed under the same fine-grained assumption, so the result
> is tight in its parameter. Because the 15-page body sketches the two most technical invariants, the
> **complete proofs are in the clearly labelled appendix and the arXiv full version**; every lemma the
> body uses is proved there. Section 2 fixes notation; Sections 3-4 give the algorithm; Section 5 the
> lower bound. *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the ICALP bar

Mapped to the skill checklists:

- **Model before theorem** — the abstract and ¶1 fix the exact setting (fully dynamic, deterministic,
  worst-case update time) before any claim (`icalp-writing-style`: "state the model, then the
  theorem").
- **Improvement against a named prior bound** — polynomial deterministic update time and a
  conditional barrier are stated, so the n^{o(1)} result is legible as progress
  (`icalp-writing-style`: position against the best known bound).
- **Right venue and track** — the contribution is a *provable* bound in a clean model, so it is Track
  A theory, not an experimental-algorithms benchmark win (`icalp-topic-selection`: the benchmark-win
  framing is the re-route signal).
- **Barrier engaged** — the fine-grained lower-bound obstacle is named and the paper explains exactly
  which structural assumption evades it (`icalp-experiments`: match the proof strategy to the known
  obstruction).
- **Tightness** — a matching necessity result (Theorem 2) shows the parameter dependence is not an
  artifact, the ICALP taste for upper and lower bounds together (`icalp-writing-style`).
- **Proof rigor over "artifact"** — there is no code to ship; the deliverable is complete, checkable
  proofs in the labelled appendix and the full version, which is ICALP's analogue of reproducibility
  (`icalp-reproducibility`, `icalp-supplementary`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified ICALP
> papers** across both tracks whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for ICALP-specific submission policy and
> the LIPIcs open-access model.
