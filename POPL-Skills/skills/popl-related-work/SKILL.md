---
name: popl-related-work
description: Use when positioning a POPL paper in the semantics, type-systems, and verification literature — stating per-line technical deltas against the nearest formal systems, covering the PACMPL family and LICS/CAV/CPP/TOPLAS neighbors, citing PACMPL-era papers in journal form, and dblp-verifying every classic before it is attributed to POPL.
---

# POPL Related Work

At POPL the related-work section is part of the *proof of novelty*: reviewers are
specialists who know the three closest systems, and the section must say — precisely
— what your formalism can do that each of them cannot, or what assumption of theirs
you discharge. Venue-form facts below were checked 2026-07-08.

## Delta sentences, not tours

Weak: "Much work has studied gradual typing [1-9]." Strong: each nearest neighbor
gets a sentence with a technical object in it —

- "[X]'s soundness needs whole-program compilation; our Theorem 5 holds under
  separate compilation because the logical relation is defined on open terms."
- "Our rules coincide with [Y] on the pure fragment (Prop. 2) and diverge exactly at
  effect handlers, which [Y] does not treat."

If you cannot write the delta sentence, you have not finished reading the neighbor
paper — or the delta does not exist, which is a `popl-topic-selection` conversation.

## The neighborhood map

| Where the closest work lives | Typical relationship to your POPL paper |
|---|---|
| POPL / PACMPL Issue POPL | The direct predecessors; deltas must be theorem-level |
| ICFP, OOPSLA, PLDI (same PACMPL journal) | Same idea family, different evidence culture — compare formal content, not venue prestige |
| LICS, CSL, FSCD | The logic-side siblings; cite them for the semantic foundations you build on |
| CAV, TACAS, CPP, ITP | Verification tools and mechanization techniques; CPP is co-located with POPL itself |
| TOPLAS, JFP, LMCS | Journal-length versions of conference lines — cite the mature statement when one exists |
| ESOP, APLAS | The European/Asian PL circuit; recent near-neighbors often debut here |

Coverage duty is highest for the last two POPL/PACMPL cycles: a 2026 paper on your
exact judgment form, missed, reads as either carelessness or concealment under full
double-blind.

## Cite the PACMPL era correctly

Since POPL joined PACMPL, "a POPL 2018 paper" is bibliographically a journal
article. Get the form right before reviewers do:

```bibtex
@article{RustBelt2018,
  author  = {Jung, Ralf and Jourdan, Jacques-Henri and
             Krebbers, Robbert and Dreyer, Derek},
  title   = {RustBelt: Securing the Foundations of the Rust Programming Language},
  journal = {Proc. ACM Program. Lang.},
  volume  = {2},
  number  = {POPL},
  pages   = {66:1--66:34},
  year    = {2018}
}
```

Volume anchors verified on the ACM DL: Vol 2 = POPL 2018, Vol 7 = POPL 2023,
Vol 10 = POPL 2026.

## Verify before attributing

PL folklore misfiles its classics. Check dblp before writing "at POPL": separation
logic's canonical paper (Reynolds 2002) is **LICS**, not POPL; Milner's type
polymorphism paper is **JCSS 1978**; "Theorems for Free!" is **FPCA 1989**. Genuine
POPL landmarks that *are* safe to cite as POPL — each dblp/ACM-DL verified
2026-07-08 — include Cousot & Cousot 1977 (abstract interpretation), Damas & Milner
1982, Necula 1997 (proof-carrying code), Leroy 2006 (certified compilation), and
Jung et al. 2015 (Iris). See `resources/exemplars/library.md`.

## Output format

```text
[Nearest neighbors] <3-5 systems with one-line technical deltas>
[Coverage gaps] <last-two-cycle POPL/PACMPL items not yet cited>
[Attribution audit] <claims of venue/priority verified on dblp? failures listed>
[Citation form] <PACMPL journal-form errors found>
```
