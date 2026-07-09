---
name: icdt-reproducibility
description: Use when strengthening the verifiability of an ICDT (International Conference on Database Theory) paper — the theory-venue analogue of reproducibility — covering complete and self-contained proofs, exact models and assumptions, claim-to-proof mapping, matching upper and lower bounds, consistency between the LIPIcs paper and the arXiv full version, and honest labeling of what is proved versus conjectured.
---

# ICDT Reproducibility

At a theory venue, "reproducibility" means **verifiability**: a competent reader, given your paper,
can reconstruct every proof and independently confirm every theorem. There is no dataset to re-run
and no benchmark to re-execute — the standard is that nothing is asserted without a checkable
argument, and nothing in the published record contradicts the full version. Use this before
submission and again before camera-ready.

## Verifiability map

- Map each **theorem, lemma, and stated bound** to a **complete proof** — in the body or the marked
  appendix — with every case handled. An unproved "it can be shown" is the theory-venue equivalent of
  a missing script.
- Pin the **model and assumptions** exactly: the data model, the query/constraint language, the
  complexity measure (data vs combined vs query), and any restriction (bounded arity, acyclicity)
  the proof relies on. A hidden assumption that makes the theorem easier is a correctness defect.
- Ensure **definitions are self-contained**: every symbol and notion used in a proof is defined in
  the paper, not assumed from a specific prior paper the referee may not have open.
- Keep the paper **internally consistent**: a bound stated in the abstract, restated in a theorem,
  and used in a corollary must be the same bound.

## Proof-completeness audit

| Claim in the paper | Weak (non-verifiable) form | ICDT-ready form |
|---|---|---|
| "Evaluation is [class]-complete" | Upper bound only; "hardness is standard" | Both bounds proved; the reduction given explicitly |
| "The construction works" | Sketch with the hard case omitted | Every case, including the awkward one, in the appendix |
| "This generalizes [X]" | Asserted | The generalization proved, with X recovered as a special case |
| "The problem is decidable" | Algorithm without a termination/correctness proof | Algorithm + proof it halts and is correct |
| "W.l.o.g. assume acyclic" | Unjustified | The reduction to the acyclic case proved, or the assumption dropped |

"It is easy to see" is treated as *not shown* unless it genuinely is; convert each such line into a
one-line argument or move it to the appendix as a short proof.

## Matching bounds and tightness

```text
[Upper bound]  algorithm/argument establishing membership in the claimed class, proved
[Lower bound]  a reduction (or game/adversary argument) establishing hardness, proved
[Label]        say which is which, and state explicitly when the two meet (tight)
[Gaps]         if a bound is one-sided, say so honestly rather than implying tightness
```

A one-sided bound presented as a settled answer is the most common verifiability failure ICDT
referees catch — and the most common reason for a Cycle-1 "revise."

## Paper / full-version consistency

- Before submission: the single PDF is self-contained; every acceptance-critical claim has a
  checkable proof inside it (online appendices are not allowed).
- Before camera-ready: post/update the **arXiv full version** and confirm it states **the same
  theorems and bounds** as the LIPIcs paper. If the revision changed a bound, change it in **both**.
- A published LIPIcs paper whose full version silently proves a weaker (or stronger) result than
  claimed is a lasting citation hazard; keep them in lockstep (`icdt-camera-ready`).

## Honest labeling

- Distinguish **theorem** (proved), **conjecture** (believed, unproved), and **open problem** (not
  known) explicitly; a referee reads these words literally.
- State what your result does **not** cover — the cases outside your class, the measures you did not
  bound — so no reader over-reads it.
- Attribute reused proof techniques to their source rather than re-deriving them silently.

## Output format

```text
[Claim inventory] <each theorem/lemma -> complete proof location>
[Models pinned] data model / language / complexity measure / restrictions stated? yes/no
[Bounds] matched and labeled; one-sided gaps disclosed? yes/no
[Self-contained] all definitions in-paper; no external-appendix dependence? yes/no
[Consistency] LIPIcs paper == arXiv full version on all bounds? yes/no
[Fix queue] <close proof gaps first, then pin models, then align full version>
```
