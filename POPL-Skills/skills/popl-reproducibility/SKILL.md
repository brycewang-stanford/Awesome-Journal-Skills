---
name: popl-reproducibility
description: Use when making a POPL paper's results independently checkable — deciding which theorems to mechanize versus hand-prove, maintaining a paper-to-proof correspondence table from day one, keeping on-paper proofs auditable with explicit assumption tracking, and making any accompanying prototype's numbers regenerable.
---

# POPL Reproducibility

At a theory venue "reproducible" does not mean rerunnable seeds; it means **an
independent reader can re-establish your claims**. For POPL that decomposes by claim
type, and the discipline pays twice: once with reviewers under full double-blind, and
again with artifact evaluators after conditional acceptance, where reusable proof
claims must be complete — no `admit`, no `sorry` (AE criteria read 2026-07-08).

## What each claim type owes the reader

| Claim type | Its reproducibility obligation |
|---|---|
| Mechanized theorem | Development compiles; theorem checkable; axioms printed and declared |
| On-paper theorem | Full proof in the appendix; every hypothesis stated where used, not discovered mid-proof |
| Definitional adequacy ("our semantics models X") | Examples or an adequacy theorem connecting formalism to the informal system |
| Prototype measurement | Scripted runs, versioned inputs, stated machine — see `popl-experiments` |

## Mechanize deliberately, not maximally

Full mechanization is powerful but not free; partial mechanization is respectable at
POPL **when scoped honestly**. Decide per theorem:

- Mechanize the theorems whose proofs are long, syntactic, and error-prone — subject
  reduction, soundness of a logical relation — where hand-proof mistakes hide.
- Hand-prove what is short and conceptual, and write the proof in full; "routine
  induction" is a claim reviewers test by attempting the induction.
- Never let paper and mechanization silently diverge: if the mechanized calculus
  drops polymorphism, the paper's theorem statement must say so.
- Statement drift is the classic failure — the `.v` file proves a lemma about a
  judgment the paper revised two drafts ago.

## The correspondence table

Start this file the week the first lemma lands, not the week AE starts:

```markdown
| Paper stmt | Formal name | File:line | Status | Axioms |
|---|---|---|---|---|
| Thm 3.1 (soundness) | `soundness` | theories/Sound.v:212 | Qed | none |
| Lem 3.2 (subst) | `subst_pres` | theories/Subst.v:88 | Qed | funext (declared) |
| Thm 5.4 (full abstraction) | — | on-paper only, App. D | complete proof | classical logic |
```

Regenerate the status column mechanically (`grep -c "Admitted" theories/*.v` should
be zero or explained) and cite the table in the paper's contributions paragraph — it
is the sentence "all results are mechanized except Thm 5.4" made auditable.

## Assumption hygiene for on-paper proofs

- Number global assumptions once (Assumption 1, 2, ...) and cite them by number in
  every theorem; unnumbered ambient hypotheses are where soundness doubts breed.
- Keep one notation table; a symbol that changes meaning between Section 3 and
  Appendix B costs a review cycle.
- When a proof cites "standard techniques," name the technique and the source
  theorem — the reader must be able to find the exact statement being invoked.
- Archive the appendix, proofs, and development in the same repository so a revision
  to one forces a visible diff in the others.

## Output format

```text
[Claim inventory] mechanized:<n> on-paper:<n> empirical:<n>
[Correspondence table] exists / stale / missing
[Divergences] <paper statement vs formalization deltas, each disclosed?>
[Assumption hygiene] <numbered? notation table? invoked-theorem citations?>
[Weakest link] <the one claim an independent reader cannot currently re-establish>
```
