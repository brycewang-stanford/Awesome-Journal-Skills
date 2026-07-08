> **Illustrative teaching example.** The paper, problem history, bounds, and every
> number below are **fictional**, constructed only to demonstrate STOC first-page
> craft. No real results are quoted and no venue policy is invented. Corresponding
> skills: [`stoc-writing-style`](../../skills/stoc-writing-style/SKILL.md),
> [`stoc-topic-selection`](../../skills/stoc-topic-selection/SKILL.md), and
> [`stoc-related-work`](../../skills/stoc-related-work/SKILL.md).

# Worked Example: A STOC-Style Opening (before → after)

The exercise: the same fictional result — a faster fully dynamic algorithm for
maintaining graph connectivity — written first as a competent journal-style
opening, then rebuilt for STOC's reading contract: a cross-area committee member
must grasp *result, lineage, and barrier* from page one, and the table of
contents plus twelve pages carry the whole persuasion
(see `stoc-submission` on the guaranteed-read rule).

**Fictional paper:** *"Fully Dynamic Connectivity in Amortized
$O(\log n \, (\log\log n)^2)$ Update Time."*

---

## Before (journal-style: correct, complete, and invisible)

> **Abstract.** We study the fully dynamic connectivity problem, in which a graph
> on $n$ vertices undergoes edge insertions and deletions and connectivity
> queries must be answered. This problem has a long history and many variants
> have been considered. We present a new data structure based on a hierarchy of
> spanning forests together with a novel amortization argument. We analyze its
> update time and prove correctness. Experimental questions are left for future
> work.
>
> **Introduction.** Dynamic graph algorithms are an important area of algorithmic
> research. Section 1.1 defines the model. Section 1.2 surveys prior work in
> chronological order [23 citations]. Section 1.3 outlines our data structure.
> We begin by recalling the definition of a spanning forest...

**Why this fails at STOC** (against `stoc-writing-style` / `stoc-related-work`):

- **The bound is nowhere.** Neither the abstract nor the opening states the new
  update time or the bound it beats — the one thing a lineage-aware reviewer
  scans for first.
- **No barrier account.** Nothing explains what obstructed progress or why the
  known lower bound leaves room; the significance case is implicit.
- **Chronological literature survey** instead of a positioning argument; twenty-
  three citations ordered by year answer no reviewer question.
- **The corridor test is unattempted** — no sentence tells a complexity or
  crypto PC member why they care.
- **Roadmap prose** ("Section 1.1 defines...") spends guaranteed-read space on
  navigation the table of contents already provides.

---

## After (STOC arc: result → lineage → barrier → technique → consequences)

> **Abstract.** We give a deterministic data structure maintaining connectivity
> of an $n$-vertex graph under edge insertions and deletions in amortized
> $O(\log n \, (\log\log n)^2)$ time per update with $O(\log n / \log\log n)$
> query time. This is the first improvement over the
> $O(\log^2 n)$ amortized bound of [FG] in two decades, and approaches the
> $\Omega(\log n)$ cell-probe lower bound of [PD] up to doubly logarithmic
> factors. The obstruction to improving [FG] was the rebuilding cost of its
> forest hierarchy; we replace global rebuilds with a lazy repair scheme whose
> analysis couples a new potential function to a fractional relaxation of the
> hierarchy — a technique we believe applies to other rebuild-bound dynamic
> structures.
>
> **Introduction.**
> *(¶1 — the result, first breath, informal/formal pair.)*
> **Theorem 1.1 (informal).** *Fully dynamic connectivity is solvable in
> amortized $O(\log n\,(\log\log n)^2)$ update time, deterministically.*
> The formal statement, with the exact query tradeoff and the word-RAM model
> pinned down, is Theorem 2.3; Theorem 1.1 is its $q = O(1)$ specialization.
>
> *(¶2 — lineage, strongest prior quoted.)* Connectivity is the touchstone
> dynamic graph problem. After [early work], the amortized frontier reached
> $O(\log^2 n)$ [FG], where it has remained despite sustained attack; the best
> randomized bound is $O(\log n\,\log\log n)$ [R2], and the cell-probe lower
> bound is $\Omega(\log n)$ [PD]. Our bound is the first deterministic movement
> below $\log^2 n$ and lands within $(\log\log n)^2$ of the lower bound.
> *(each claim names the exact bound and model it is measured in.)*
>
> *(¶3 — the barrier, named and confronted.)* Every descendant of [FG] pays for
> hierarchy rebuilds: when a level overflows, the structure is rebuilt from
> scratch, and a standard charging argument shows this costs $\Theta(\log n)$
> per level per update — hence $\log^2 n$ appears to be structural, and [S]
> proved it is, *for any algorithm that rebuilds levels atomically*. Our
> departure is to make rebuilds non-atomic. *(the reviewer's "why was this
> stuck?" is answered before it is asked — the objection-ledger discipline of
> `stoc-author-response`.)*
>
> *(¶4 — technique, obstacles and moves.)* The lazy repair scheme spreads each
> rebuild across future updates. The difficulty is that queries may observe a
> half-rebuilt hierarchy; correctness needs an invariant that partial levels
> still route connectivity witnesses. Section 3 (Technical Overview) develops
> this in three steps... the new potential function enters in step two, where
> atomic-rebuild charging fails. Complete proofs of Theorems 2.3 and 5.1 appear
> in Appendices A and B respectively; the full version carries the general
> $q$-tradeoff. *(pointer discipline per `stoc-supplementary`.)*
>
> *(¶5 — consequences beyond the sub-area.)* Beyond connectivity, the fractional
> hierarchy analysis gives the first sub-$\log^2 n$ bounds for two other
> rebuild-bound structures (Corollaries 6.1–6.2), and we leave as an open
> problem whether it derandomizes [R2] entirely — a question with implications
> for the dynamic-algorithms/derandomization interface. *(the corridor
> sentence: a non-specialist now has a reason to care, per
> `stoc-topic-selection`.)*

---

## What changed, mapped to the skills

- **Bound on page one, informal/formal paired** — Theorem 1.1 (informal) with a
  one-hop pointer to Theorem 2.3 (`stoc-writing-style`, first-page rule).
- **Lineage quantified** — prior deterministic, randomized, and lower bounds
  each quoted with their exact form, strongest versions cited
  (`stoc-related-work`, lane one; no weakest-prior inflation).
- **Barrier named** — the atomic-rebuild obstruction and its conditional lower
  bound [S] explain the two-decade gap, converting a small-looking improvement
  into a significance case (the Karlin–Klein–Oveis Gharan framing pattern in
  [`../exemplars/library.md`](../exemplars/library.md)).
- **Overview as obstacles-and-moves** — ¶4 says where the standard argument
  breaks and which step is new, honestly attributing the rest.
- **Guaranteed-read budget respected** — no roadmap prose; deferred proofs get
  exact appendix pointers; the general tradeoff lives in the full version
  (`stoc-supplementary` placement table).
- **Fictional throughout** — bounds, citations ([FG], [PD], [R2], [S]), and the
  open problem are invented scaffolding for the *shape* of the argument; never
  reuse them as facts.

> Next: study the verified first pages in
> [`../exemplars/library.md`](../exemplars/library.md), then run the draft
> against [`../../skills/stoc-submission/SKILL.md`](../../skills/stoc-submission/SKILL.md)
> before upload.
