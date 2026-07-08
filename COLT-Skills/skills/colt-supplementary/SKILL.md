---
name: colt-supplementary
description: Use when structuring the appendix of a COLT (Conference on Learning Theory) submission — the unlimited-length proof appendix inside the single PDF — covering body/appendix splitting for a 12-page limit, theorem restatement discipline, lemma ordering, notation tables, and what referees expect to find where.
---

# COLT Supplementary

COLT's "supplementary material" is the appendix of the same PDF: the 2026 CFP (checked
2026-07-08) capped the main body at 12 PMLR-formatted pages excluding references and
put **no page limit on references and appendices**, with the entire manuscript
submitted as a single file. There is no separate upload, no later supplement deadline,
and no distinction between "appendix" and "supplement" — which changes how you should
architect the document compared to venues with detached supplements.

## Consequences of the single-PDF model

- The appendix is unambiguously part of the reviewed record; referees are choosing to
  read it, not to download it. Lower the cost of that choice.
- Nothing can be added after the deadline. A proof hole discovered post-submission
  cannot be patched by a supplement upload the way an artifact fix sometimes can
  elsewhere.
- Length is free but attention is not: a 60-page appendix is normal at COLT, a
  disorganized one is a soft reject, because the referee's verification budget is the
  binding constraint.

## The 12-page split decision

What must stay in the body:

- Formal problem setup: the model, the interaction protocol, the adversary or
  distributional assumptions, and the performance measure — complete, not "see
  Appendix A for the model."
- Every main theorem statement, with all hypotheses visible.
- A proof overview per main theorem: the decomposition, the key lemma, and the step
  where prior techniques fail. This is what earns the referee's appendix time.
- The comparison to nearest prior bounds (a small table often beats prose).

What belongs in the appendix: full proofs, auxiliary lemmas, generalized statements,
deferred case analyses, extended related work, and any numerical-illustration details.

## Appendix architecture that referees can verify

| Appendix section | Contents | Referee use pattern |
|---|---|---|
| A. Notation and preliminaries | Symbol table, standard inequalities used | Consulted repeatedly; keep to 2-3 pages |
| B. Proof of Theorem 1 | Restated theorem, roadmap paragraph, main lemmas, proof | Read linearly, checked line by line |
| C. Proof of Theorem 2 | Same pattern | Read only if Theorem 2 matters to the referee |
| D. Auxiliary lemmas | Technical facts shared across proofs | Jumped to via references |
| E. Deferred discussion / numerics | Extensions, illustration details | Skimmed |

Ordering rule: appendix sections mirror body theorem order, and each proof section is
self-contained modulo Appendix A and D — a referee verifying Theorem 2 must never need
to have read the proof of Theorem 1 unless the dependency is real and declared.

## Restatement discipline

Restate every theorem and lemma before its appendix proof, with identical numbering,
via a restatable environment rather than copy-paste (drift between two hand-maintained
copies of a theorem is a notorious COLT embarrassment):

```latex
\usepackage{thmtools, thm-restate}

\declaretheorem[name=Theorem]{theorem}

% In the body:
\begin{restatable}{theorem}{mainregret}\label{thm:main}
Under Assumptions 1--2, ALG attains $R_T = O(\sqrt{dT\log K})$.
\end{restatable}

% In Appendix B:
\mainregret*   % re-renders Theorem 1 verbatim, same number
\begin{proof}
We decompose the regret as ... (roadmap sentence first, then the argument).
\end{proof}
```

## Roadmap paragraphs are load-bearing

Open each major appendix proof with 4-6 sentences: the decomposition, what each lemma
contributes, where the novelty sits, and which steps are routine. Referees use the
roadmap to allocate verification effort; proofs without one get either shallow reads
(bad for credit) or suspicious reads (bad for scores).

## Vignette: splitting a two-theorem online-learning paper

A draft proves an upper bound (algorithm + potential argument, 14 pages of proof) and
a lower bound (instance family + information argument, 9 pages), plus one simulation.
The COLT-shaped split:

- Body: protocol and definitions (2 pp), both theorem statements with remarks
  (2.5 pp), upper-bound overview with the potential function displayed and one key
  lemma proved in full (3 pp), lower-bound overview with the instance family drawn
  as a figure (2 pp), related-work table and discussion (1.5 pp), simulation figure
  with a two-sentence reading (0.5 pp), intro (1.5 pp) — twelve and a half, so the
  second remark and one corollary move to the appendix to make twelve.
- Appendix: A notation; B full upper-bound proof (restated theorem, roadmap, lemmas);
  C full lower-bound proof; D auxiliary facts; E simulation procedure.
- The key-lemma-in-body choice is deliberate: proving one central lemma completely in
  the body demonstrates the paper's proof standard where every referee will read it.

## Common appendix defects at COLT

- Lemma used before it is stated anywhere, forcing a forward hunt.
- "By a standard argument" covering the one step that is actually new.
- Notation redefined locally inside an appendix section, colliding with Appendix A.
- Case analyses whose cases do not visibly exhaust the space.
- Cross-references into the body by page number instead of by label (page numbers
  shift when the class file changes at camera-ready).
- Illustration figures buried between proofs, breaking the verification flow — give
  numerics their own terminal section.

## Cycle-volatility warnings

- The unlimited-appendix, single-PDF rule is the 2026 formulation; earlier cycles
  phrased limits differently and later ones may again (待核实 in each CFP).
- If a cycle ever adds a separate supplement channel or reviewable-code slot, its CFP
  will say so; do not assume either from this file.

## Output format

```text
[Split verdict] body self-contained / decision-critical material trapped in appendix
[Appendix map] <section -> theorem it serves>
[Restatement check] restatable environments / copy-paste risk
[Roadmaps] present for <k>/<n> major proofs
[Top structural fix] <one reorganization with highest referee payoff>
```
