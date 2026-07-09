> **Illustrative teaching example.** The result, definitions, and every statement below are
> **fictional** and exist only to demonstrate ICDT house style. No real theorem, paper, or bound is
> stated, and no policy is invented. Corresponding skills:
> [`icdt-writing-style`](../../skills/icdt-writing-style/SKILL.md),
> [`icdt-topic-selection`](../../skills/icdt-topic-selection/SKILL.md), and
> [`icdt-experiments`](../../skills/icdt-experiments/SKILL.md).

# Worked Example: An ICDT-Style Abstract + Introduction (before → after)

This demonstrates the **ICDT first-page arc** from `icdt-writing-style`:
**precise data-management problem → why the current state is unsatisfactory → the contribution as
formal statements → the proof technique in one breath → the consequence for data management** — with
the ICDT expectations that the **model is fixed before the theorem**, bounds are **matching and
labeled**, and the paper reads as a **theorem-proof** document, not a systems evaluation.

The framing also reflects `icdt-topic-selection`: ICDT is strongest when the lesson is a **theorem
about querying, constraints, or data** whose data-management consequence is explicit — here, the
combined complexity of evaluating a query language over inconsistent databases — rather than a generic
complexity result whose data connection is incidental (which would route to a pure-TCS venue), and
when the result could sit at ICDT or PODS and one chooses by calendar and publisher.

**Illustrative paper (fictional):** *"The Combined Complexity of Consistent Answers for Guarded Path
Queries."* Fictional contribution: a tight complexity bound for computing certain answers of a query
class over databases violating a set of guarded constraints.

---

## Before (buries the theorem; under-specifies the model — typical first-draft)

> **Abstract.** Inconsistent data is a big problem in modern databases. We study query answering over
> such data and design a new algorithm. Our approach is efficient and outperforms naive methods, and
> we show experiments demonstrating its effectiveness. This is an important step for data quality.
>
> **Introduction.** Databases are often inconsistent. Many people have studied consistent query
> answering. In this paper we look at a certain kind of query and constraints and give an algorithm
> for computing answers. We ran experiments on some datasets and it works well. Section 2 has
> related work, Section 3 the approach, Section 4 experiments, and Section 5 concludes.

**What's wrong (against `icdt-writing-style` / `icdt-topic-selection` / `icdt-experiments`):**

- **No formal statement on the first page** — it promises "an algorithm" and "efficiency" but never
  states a theorem, a complexity class, or which complexity measure is meant.
- **The model is undefined.** Which query class? Which constraint language? Finite databases? Data,
  combined, or query complexity? An ICDT referee cannot tell what would be proved.
- **Evidence shape is wrong for the venue.** "Experiments demonstrating effectiveness" is systems
  evidence; the ICDT claim should be a **bound with matching upper and lower proofs**, not a benchmark.
- **No consequence stated** — "important for data quality" is a slogan, not a database-theory payoff.
- **Reads like an EDBT/SIGMOD paper**, which is the `icdt-topic-selection` re-route signal that either
  the framing or the venue is wrong.

---

## After (ICDT arc — problem → gap → formal contribution → technique → consequence)

> **Abstract.** Computing **certain answers** to queries over databases that violate integrity
> constraints is a central problem in consistent query answering, but the **combined complexity** for
> expressive query and constraint classes is only partially understood. We consider **guarded path
> queries** evaluated under a set of **guarded tuple-generating dependencies** over finite relational
> databases, and determine the exact combined complexity of the certain-answer problem. We prove it is
> **complete for [complexity class C]**: a matching upper bound via a bounded-witness argument and a
> lower bound by reduction from [a canonical C-complete problem]. We further show the bound **drops to
> [class C']** when the constraint set is acyclic, delineating exactly where tractability begins.
> *(problem → gap → formal result → both bounds → boundary — all on the first page.)*
>
> **Introduction.** *(¶1 — the problem, stated precisely.)* Let a database be a finite relational
> structure that may violate a set Σ of guarded tuple-generating dependencies. The **certain answers**
> of a query q are the tuples returned on every repair of the database with respect to Σ. We study the
> **combined complexity** — measured in the size of the database, the query, and Σ together — of
> deciding whether a tuple is a certain answer, for q a **guarded path query**.
>
> *(¶2 — why the current state is unsatisfactory.)* Prior work settles the **data complexity** of this
> problem and the combined complexity for less expressive queries, but leaves the combined complexity
> for guarded path queries under guarded dependencies **open**: the known upper bound is not matched by
> a lower bound, so it is unknown whether the problem is genuinely harder than its data-complexity
> shadow suggests.
>
> *(¶3 — the contribution, as formal statements.)* We close the gap. **Theorem 1** establishes that the
> certain-answer problem for guarded path queries under guarded TGDs is **C-complete** in combined
> complexity. **Theorem 2** shows that restricting Σ to acyclic constraint sets lowers the complexity to
> **C'-complete**, and **Theorem 3** shows the restriction is necessary: dropping acyclicity restores
> C-hardness.
>
> *(¶4 — the technique in one breath.)* The upper bound rests on a **bounded-witness lemma**: every
> certain-answer refutation can be witnessed by a repair of size polynomial in the guard width, letting
> a nondeterministic procedure guess and check it. The lower bound encodes a C-complete tiling/formula
> problem into a fixed schema so that hardness comes from the query and constraints, not the data.
>
> *(¶5 — consequence, and honest scope.)* The result **pinpoints the price of expressiveness**: moving
> from the previously understood class to guarded path queries raises combined complexity by exactly one
> level, and acyclicity is the precise dividing line for tractability. We state the boundary honestly —
> the result concerns **finite** databases and does **not** extend to unrestricted TGDs, which we leave
> open. Section 2 fixes the model and prior bounds; Section 3 proves Theorem 1; Section 4 the acyclic
> case; full proofs are in the appendix. *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the ICDT bar

Mapped to the skill checklists:

- **Formal contribution on the first page** — the abstract and ¶3 state named theorems and a complexity
  class before any procedure detail (`icdt-writing-style`: "put the formal statements early").
- **Model fixed before the theorem** — ¶1 pins finite relational databases, guarded TGDs, guarded path
  queries, and **combined** complexity, so the referee knows exactly what is proved
  (`icdt-writing-style`: "state the models before the theorems").
- **Matching bounds, labeled** — an upper bound *and* a lower bound are claimed and attributed to
  distinct arguments, with the tractability boundary proved necessary (`icdt-experiments`: the proof,
  not a benchmark, is the evidence; tightness is shown, not implied).
- **Right venue** — the lesson is a database-theory theorem about consistent query answering with an
  explicit data-management consequence, so it is an ICDT (or PODS) contribution, not a systems paper and
  not a generic complexity result (`icdt-topic-selection`).
- **Honest scope** — ¶5 states what the result does not cover (finite only; not unrestricted TGDs),
  the verifiability discipline `icdt-reproducibility` asks for.
- **No stray experiment** — there is no benchmark section, because the contribution is the bound; an
  experiment would be at best a proportional supplement and here adds nothing (`icdt-experiments`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified ICDT papers**
> whose first pages execute this arc, and [`../official-source-map.md`](../official-source-map.md) for
> ICDT-specific submission policy and the two-cycle LIPIcs model.
