---
name: pods-writing-style
description: Use when revising an ACM PODS paper for a precise model and result on the first page, exact theorem statements with matching bounds, complete and self-contained proofs (body plus at-submission appendix), honest assumptions and open cases, double-anonymous wording, and disciplined use of the acmsmall 15-page budget.
---

# PODS Writing Style

Use this when revising the main paper. PODS papers are read by database theoreticians, so they need a
**precise model and a precise result stated on the first page** and **proofs a reviewer can verify**.
The failure this skill prevents is a paper whose interesting idea is buried under systems language or
whose theorems are stated loosely enough that no one can tell what was proved.

## Revision rules

- **Lead with the model and the result:** the data-management problem, the exact model (data/query
  model, complexity measure, cost model), the result (a bound, a dichotomy, a semantics, an optimal
  algorithm), why it is tight or complete, and what it settles — all on the first page.
- **State theorems precisely.** Every theorem names its hypotheses, its model, and its exact
  quantities (data vs. combined complexity, worst-case vs. parameterized, exact vs. approximate). A
  vague "our problem is hard" is not a PODS theorem.
- **Match upper and lower bounds.** The strongest PODS papers close the gap; where you cannot, say so
  and state the open case rather than hiding it behind "we leave this to future work" without a
  precise statement.
- **Every stated result has a complete proof.** In the body if it fits, otherwise in the appendix
  incorporated with the submission — PODS forbids online/external appendices, so a proof "omitted" or
  "in the full version" with nothing in the appendix is a reject.
- **Respect the acmsmall budget as a design constraint.** 15 pages excluding references, plus
  unlimited references, plus the appendix; the body must be a self-contained mathematical narrative,
  with routine or long proofs pushed to the appendix behind clear forward references.
- **Maintain lightweight double-anonymity** in self-citations, named systems, acknowledgements, and
  funding — phrase your own prior work in the third person.

## Theory-paper skeleton

| Section | Job it must do | Common failure |
|---|---|---|
| Intro | Problem, model, result, tightness, what it settles — first page | Leads with a system or a trend, not a model and a theorem |
| Preliminaries | Fix the data/query model, notation, and the exact problem | Definitions too informal for the theorem to be unambiguous |
| Main results | State each theorem precisely; give the key proof ideas | Theorems stated so loosely the contribution is unclear |
| Upper bound | The algorithm/construction + its correctness and complexity proof | Complexity asserted, not proved; hidden dependence on parameters |
| Lower bound | The hardness reduction or impossibility, with its assumptions | No matching lower bound, so optimality is unproven |
| Related work | Delta-first positioning against PODS/ICDT/logic literature | A citation catalog with no contrast of results |

## Sentence-level rewrites

| Draft pattern | PODS-safe rewrite |
|---|---|
| "Our algorithm is very efficient." | "runs in `O(n log n)` data complexity (Thm 3), matching the `Ω(n log n)` lower bound of §5" |
| "The problem is hard." | "consistent query answering for this class is `coNP`-complete in data complexity (Thm 2)" |
| "We handle a broad class of queries." | "we prove the dichotomy for all self-join-free conjunctive queries; self-joins remain open (§7)" |
| "Experiments confirm our approach." | "we give a matching lower bound; a small empirical check (§6) illustrates the constants" |
| "It is easy to see that..." | Replace with the actual argument or a pointer to the appendix proof |

## Statement discipline

```text
[Model]        fix the data model, query class, and cost/complexity measure before any theorem
[Quantifiers]  say exactly what is universal and what is existential; data vs. combined complexity
[Tightness]    pair each upper bound with a lower bound or state the gap as an open problem
[Assumptions]  name every conjecture a bound rests on (e.g. OMv, ETH); never present conditional
               hardness as unconditional
-> a reader should be able to restate your main theorem exactly from the abstract alone
```

## Vignette: compressing a two-bound paper

A draft with an upper-bound algorithm, a lower-bound reduction, three corollaries, and a long
preliminaries section: keep both main theorems and their proof ideas in the body, move the full
reduction gadget and the corollary proofs to the appendix with forward references, and cut
preliminaries to exactly the definitions the theorems use. The test of a good cut: a reviewer should
be able to state what was proved and why it is tight from the body alone, and find every full proof in
the appendix.

## Output format

```text
[Writing diagnosis] clear / under-specified model / loose theorems / gap unstated / over-scoped
[First-page fix] <new framing leading with the model and the exact result>
[Theorem audit] <theorem -> hypotheses stated? complexity exact? proof located? tight?>
[Tightness fix] <where a matching lower bound or an honest open-case statement must be added>
[Anonymity edits] <named systems / self-citations / acknowledgements to rewrite>
```
