> **Illustrative teaching example.** The paper, model, theorem, and every claim below are
> **fictional** and exist only to demonstrate PODS house style. No real-paper results, bounds, or
> policies are stated, and no theorem is invented as fact. Corresponding skills:
> [`pods-writing-style`](../../skills/pods-writing-style/SKILL.md),
> [`pods-topic-selection`](../../skills/pods-topic-selection/SKILL.md), and
> [`pods-experiments`](../../skills/pods-experiments/SKILL.md).

# Worked Example: A PODS-Style Abstract + Introduction (before → after)

This demonstrates the **PODS first-page arc** from `pods-writing-style`:
**problem in data management → the precise model and question → the result (a bound, a dichotomy, a
semantics) → why it is tight/complete → what it settles** — with the PODS expectations that the
contribution is a **provable** statement about a cleanly defined model, that upper and lower bounds
**match** wherever possible, and that a **complete proof** exists (in the body or the at-submission
appendix), not a promise.

The framing also reflects `pods-topic-selection`: PODS is strongest when the lesson is a
**foundational** statement about queries, complexity, logic, or data models — here, the exact
complexity of maintaining answers to a query class under updates — rather than a systems win whose
theoretical content is incidental (which would route to SIGMOD/VLDB/ICDE), and when the paper cannot
simply be re-labeled a systems benchmark paper without losing its point.

**Illustrative paper (fictional):** *"A Dichotomy for Constant-Delay Enumeration of Conjunctive
Queries under Single-Tuple Updates."* Fictional result: a complete PTIME/hardness classification of
which self-join-free conjunctive queries admit constant-delay answer enumeration with logarithmic
update time.

---

## Before (buries the result in systems language — typical first-draft abstract + intro)

> **Abstract.** Modern applications need fast query answers over changing data. We propose a new
> incremental technique for enumerating the answers of conjunctive queries, and show experimentally
> that it is much faster than recomputation on several datasets. Our system scales to large inputs
> and demonstrates the promise of incremental query processing.
>
> **Introduction.** Query processing is important, and data changes all the time. Many systems
> recompute query answers from scratch, which is slow. In this paper we design an algorithm that
> maintains the answers of conjunctive queries incrementally and enumerates them quickly. We
> evaluate our approach on real and synthetic datasets and show it outperforms baselines. Section 2
> covers related work, Section 3 our algorithm, Section 4 experiments, Section 5 concludes.

**What's wrong (against `pods-writing-style` / `pods-topic-selection` / `pods-experiments`):**

- **No model or precise question on the first page** — it leads with "applications need speed" and a
  systems claim, not with a defined class of queries, an update model, and a complexity measure. PODS
  wants the formal object stated up front.
- **Wrong evidence for the venue.** "Faster on several datasets" is a SIGMOD contribution, not a PODS
  one; the paper never states *which* queries are and are not maintainable, or proves any bound.
- **No dichotomy, no lower bound.** The interesting PODS content — a complete classification with a
  matching hardness result — is absent, so the paper reads as an engineering artifact.
- **Result-as-system.** If the algorithm were replaced by another heuristic, no theorem would remain
  — the `pods-topic-selection` re-route signal that this belongs at a systems venue.
- **No proof obligation acknowledged** — a double-anonymous PODS reviewer will look immediately for
  the theorem statements and the appendix with complete proofs.
- **Over-signposted roadmap** substituting for a mathematical contribution.

---

## After (PODS arc — problem → model → result → tightness → what it settles)

> **Abstract.** We study the **enumeration complexity of conjunctive queries under updates**: given a
> self-join-free conjunctive query `q` and a database subject to single-tuple insertions and
> deletions, when can the answers of `q` be enumerated with **constant delay** after only
> **logarithmic update time**? We prove a **dichotomy**: `q` admits such maintenance **iff** `q` is
> *q-hierarchical* (a syntactic condition on its atoms and variables); otherwise, no algorithm
> achieves constant delay with sub-linear update time unless the **OMv conjecture** fails. The upper
> bound is a maintenance data structure; the lower bound is a fine-grained reduction, and the two
> **match** on every self-join-free CQ. *(problem → model → exact result → tightness → assumption —
> all on the first page.)*
>
> **Introduction.** *(¶1 — the data-management problem, stated formally.)* Applications increasingly
> issue the *same* query repeatedly against data that changes one tuple at a time, and want each
> refreshed answer set streamed without recomputation. The foundational question is not "can we make
> this fast in practice?" but **"for which queries is constant-delay enumeration under updates even
> possible, and where is the exact boundary?"**
>
> *(¶2 — why the current understanding is incomplete.)* Prior work gives efficient maintenance for
> specific queries and hardness for isolated others, but **no complete classification**: it is not
> known which self-join-free conjunctive queries admit constant delay with poly-logarithmic updates,
> nor whether the boundary is syntactic. Without a dichotomy, each new query requires a fresh,
> ad-hoc analysis.
>
> *(¶3 — contribution, stated as theorems.)* We settle the question with a **dichotomy theorem**. We
> introduce the *q-hierarchical* condition and prove: (i) every q-hierarchical query admits
> constant-delay enumeration after `O(log n)` update time (Theorem 1, via a maintained trie-of-tries
> structure); and (ii) for every non-q-hierarchical self-join-free CQ, any data structure with
> constant-delay enumeration requires `n^{1-o(1)}` update time under the OMv conjecture (Theorem 2,
> via an online-matrix-vector reduction). The condition is decidable in polynomial time in the query.
>
> *(¶4 — why the result is tight and complete.)* The two theorems have **matching regimes**: the same
> syntactic line separates the tractable and intractable cases, so the classification is exhaustive
> over self-join-free CQs — there is no unclassified middle. We state precisely the model (single-tuple
> updates, RAM cost measure, data complexity) under which the dichotomy holds, and note exactly where
> self-joins break the argument (an open problem we do not overclaim).
>
> *(¶5 — what it settles and the proof location.)* The result draws a **sharp, syntactic boundary**
> for a problem previously handled case by case, and connects database enumeration to fine-grained
> complexity through the OMv conjecture. Complete proofs of Theorems 1 and 2 appear in the appendix,
> incorporated with the submission; a full version is available on arXiv. Section 2 fixes the model;
> Section 3 proves the upper bound; Section 4 the lower bound. *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the PODS bar

Mapped to the skill checklists:

- **Model and question on the first page** — the abstract and ¶1 fix the query class, the update
  model, and the complexity measure before any algorithm (`pods-writing-style`: "lead with the model
  and the precise question").
- **Result proportional to the venue** — the contribution is a **dichotomy with matching bounds**,
  not a speedup; the evidence is two theorems, not a benchmark table (`pods-experiments`: PODS
  "experiments" are analyses and matching lower bounds).
- **Tightness made explicit** — ¶4 states that the upper and lower bounds meet on the same syntactic
  line, so the classification is complete, and it names the exact model and the open self-join case
  rather than overclaiming (`pods-writing-style`: bound the claim to the model proven).
- **Right venue, result-swap test passes** — the lesson (a syntactic boundary tied to OMv) survives
  swapping the specific data structure, so it is a PODS contribution, not a systems re-route
  (`pods-topic-selection`).
- **Proof obligation met** — complete proofs are in the at-submission appendix and a full version is
  posted on arXiv, matching PODS's expectation that every stated theorem is verifiable now
  (`pods-reproducibility`, `pods-artifact-evaluation`).
- **Assumptions stated honestly** — the lower bound is conditional on a named conjecture (OMv), stated
  as such rather than presented as unconditional (`pods-experiments`: never dress a conditional
  result as absolute).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified PODS
> papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for PODS submission policy and the
> multi-cycle, PACMMOD-track process.
