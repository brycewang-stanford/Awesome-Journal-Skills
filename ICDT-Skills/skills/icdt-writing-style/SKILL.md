---
name: icdt-writing-style
description: Use when shaping the prose of an ICDT (International Conference on Database Theory) paper — the theorem-proof structure, stating the data model and computation model precisely, leading with the result and its data-management consequence, proof-sketch-then-appendix discipline within the lipics-v2021 15-page budget, and the notation conventions a database-theory referee expects.
---

# ICDT Writing Style

Write for a referee who will **read the proof**. An ICDT paper is judged on whether a precise
theorem is correctly established and matters for data management, so the house style is the
theorem-proof style of mathematical writing, disciplined into the **`lipics-v2021` 15-page budget**
(excluding references) with the full details in a marked appendix. Exposition that hides the exact
statement, the model, or the assumptions reads as imprecision at this venue.

## The ICDT first-page arc

Lead with the result, not a survey. A strong ICDT introduction moves:

1. **The data-management problem, stated precisely** — what query language / constraint class /
   data model, and what question about it (expressiveness? evaluation complexity? decidability?).
2. **Why the current state is unsatisfactory** — the exact gap: an open bound, a case the prior
   dichotomy missed, a model whose complexity was unknown.
3. **The contribution as formal statements** — "We prove that evaluation for [class] is
   [complexity], and that this is tight," ideally with the main theorem paraphrased in the intro.
4. **The technique in one breath** — the proof idea a theorist can recognize (a reduction, a
   game argument, a normal form, a semiring homomorphism).
5. **The consequence** — what changes for querying, integration, or reasoning over data.

Put the formal theorem statements early and label them; a referee should find "Theorem 1" and know
your result before page three.

## State the models before the theorems

The commonest avoidable ICDT weakness is an under-specified setting. Before the first theorem, pin:

- **The data model** — relational, graph/RDF, semistructured, probabilistic, inconsistent,
  incomplete — and whether structures are finite (they usually are; finite model theory is the
  default over databases).
- **The query/constraint language** — CQs, UCQs, Datalog, FO, MSO, regular path queries, TGDs/EGDs
  — with its exact syntax and semantics, not a hand-wave.
- **The computation and complexity measure** — combined vs data vs query complexity, the machine
  model, and the complexity classes in play. "Data complexity" vs "combined complexity" is a
  distinction ICDT referees will hold you to.

## Theorem-proof discipline within 15 pages

- **Body:** definitions, theorem statements, and the *ideas* of the proofs — enough that a referee
  can judge correctness and see the structure. Full proofs may be sketched here.
- **Appendix (marked):** the complete proofs, read at the PC's discretion. Write the body so a
  referee who never opens the appendix still believes the result is provable; write the appendix so
  one who does can certify it.
- Do not pad the body with restated related work to fill space, and do not shrink the font or margins
  to reclaim it — `lipics-v2021` is fixed; compress by editing.

## Precision conventions a referee expects

- **Every symbol is introduced before use;** overloaded notation across sections is a correctness
  hazard, not a style nit.
- **Quantify claims exactly** — "for every schema," "there exists a database," "in the worst case."
  A theory referee reads quantifier order literally.
- **Match bounds explicitly** — if you claim tightness, state and prove both the upper and the lower
  bound, and say which is which.
- **Distinguish conjecture from theorem** — "we conjecture" and "it is easy to see" are read
  literally; only write "it is easy to see" when it truly is, and give the argument if a referee
  might not.
- **Use standard names** — call it a UCQ, a guarded TGD, a semiring provenance annotation, using the
  community's established terminology so the referee maps you to known results.

## Common failure modes

- **Model-last writing** — theorems before the data model is fixed, so the referee cannot tell what
  was proved.
- **One-sided bounds sold as tight** — an upper bound with no matching lower bound presented as a
  complete answer.
- **Proof-by-citation** — "the argument is similar to [12]" where the difference is exactly the hard
  part.
- **Survey-as-introduction** — three pages of background before the first formal statement, burning
  the 15-page budget.
- **Undefined asymptotics** — big-O over an unspecified parameter (data size? query size? both?).

## Output format

```text
[First-page arc] problem -> gap -> formal contribution -> technique -> data consequence: present?
[Models fixed] data model / query language / complexity measure stated before Theorem 1? yes/no
[Budget] body <=15 pages excl. refs; full proofs in the marked appendix? yes/no
[Precision] quantifiers exact / bounds matched / notation introduced: pass/fix
[Fix queue] <ordered edits>
```
