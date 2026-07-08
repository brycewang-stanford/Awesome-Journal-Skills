# POPL Exemplars Library (era × contribution type)

> **Verified via web search against dblp and the ACM Digital Library, access date
> 2026-07-08.** Every entry below was confirmed to have appeared at the ACM SIGPLAN
> Symposium on Principles of Programming Languages (or, in the PACMPL era, in a
> PACMPL Issue POPL) — matching authors, year, and where surfaced, page or article
> numbers. Anything that could not be cleanly pinned to POPL was moved to the
> misattribution list at the bottom. Six verified beats sixteen remembered.
>
> **Misattribution warning:** PL folklore routinely files famous papers at POPL that
> live elsewhere — LICS, JCSS, FPCA, CGO. dblp is the arbiter; check it before any
> "appeared at POPL" sentence leaves your draft (`popl-related-work` has the drill).
>
> **Zero-hallucination rule:** this library gives positioning only. It does not
> restate theorem contents, definitions, or results from memory — read the original
> before citing anything technical. Policy facts live in
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use these

Each entry answers one question: *what does a POPL-defining contribution of this
shape look like?* Find the row nearest your project's shape, read how the landmark
made a **principle** — not an artifact — the contribution, then apply the self-check.
Pair with [`../../skills/popl-topic-selection/SKILL.md`](../../skills/popl-topic-selection/SKILL.md)
and [`../../skills/popl-writing-style/SKILL.md`](../../skills/popl-writing-style/SKILL.md).

---

## The verified six

### A reasoning framework that became a field — static analysis

- **Cousot & Cousot, "Abstract Interpretation: A Unified Lattice Model for Static
  Analysis of Programs by Construction or Approximation of Fixpoints," 4th POPL,
  Los Angeles, 1977, pp. 238-252.** Verified: dblp `conf/popl/popl77` and ACM DL DOI
  10.1145/512950.512973.
  - **Shape:** unifies scattered analysis techniques under one mathematical frame —
    the archetype of a POPL principle whose payoff is every later instantiation.
  - **Self-check:** does your framework *subsume* existing techniques as instances,
    provably, rather than sit beside them?

### A type-inference result with an algorithm and its theorem — type systems

- **Damas & Milner, "Principal Type-Schemes for Functional Programs," POPL 1982,
  pp. 207-212.** Verified: dblp `conf/popl/DamasM82`.
  - **Shape:** a precisely stated property (principal types) plus the algorithm that
    attains it — claim and construction sealed together by proof.
  - **Self-check:** is your system's key guarantee stated as a theorem about *all*
    programs, with the algorithm's correctness proved against it?

### A trust mechanism founded on proof theory — language-based security

- **Necula, "Proof-Carrying Code," 24th POPL, 1997.** Verified: ACM DL DOI
  10.1145/263699.263712.
  - **Shape:** relocates a systems problem (running untrusted code) into proof
    obligations and checking — the POPL move of solving by *logical architecture*.
  - **Self-check:** does your design reduce a trust or safety question to something
    a small checker can verify?

### Mechanized metatheory at scale — certified compilation

- **Leroy, "Formal Certification of a Compiler Back-end, or: Programming a Compiler
  with a Proof Assistant," 33rd POPL, 2006.** Verified: Inria HAL inria-00000963 and
  the POPL 2006 record; origin of the CompCert line.
  - **Shape:** the proof assistant is the load-bearing method, not decoration — the
    paper that made "mechanized, end to end" a POPL evidence standard
    (`popl-artifact-evaluation` is its descendant).
  - **Self-check:** if you claim mechanization, is the *whole* headline theorem
    checked, with the trusted base stated?

### A reusable logic others build on — concurrency verification

- **Jung, Swasey, Sieczkowski, Svendsen, Turon, Birkedal & Dreyer, "Iris: Monoids
  and Invariants as an Orthogonal Basis for Concurrent Reasoning," 42nd POPL,
  Mumbai, 2015, pp. 637-650.** Verified: dblp `conf/popl/popl2015`.
  - **Shape:** minimal primitives chosen so that other people's program logics
    become derivable — transferability as the explicit design goal.
  - **Self-check:** can a stranger instantiate your machinery on *their* language
    without re-proving your metatheory?

### A PACMPL-era landmark applying that logic — real-language soundness

- **Jung, Jourdan, Krebbers & Dreyer, "RustBelt: Securing the Foundations of the
  Rust Programming Language," PACMPL 2(POPL), article 66, 2018.** Verified: ACM DL
  DOI 10.1145/3158154.
  - **Shape:** takes a principle (semantic typing in Iris) to an industrial
    language's safety story — note the citation form: journal article, volume 2,
    issue POPL (`popl-related-work` shows the BibTeX).
  - **Self-check:** when you scale a principle to a real language, is the modeled
    fragment stated exactly, and is the gap to the full language disclosed?

---

## Era × contribution grid

| Era | Framework/analysis | Types/inference | Security/trust | Mechanization | Logics/concurrency |
| --- | --- | --- | --- | --- | --- |
| Classic POPL (1977-1997) | Cousot & Cousot 1977 | Damas & Milner 1982 | Necula 1997 | — | — |
| Pre-PACMPL 2000s-2015 | — | — | — | Leroy 2006 | Jung et al. 2015 (Iris) |
| PACMPL Issue POPL (2018-) | — | — | — | — | Jung et al. 2018 (RustBelt) |

> The Iris → RustBelt pair is deliberately included as a *research line inside
> POPL*: a logic introduced at one edition carrying a landmark application three
> editions later — the strongest available template for "principle, then payoff."

---

## Do not attribute to POPL without re-checking

Checked or long-established venue records; each is a live trap:

- **Reynolds, "Separation Logic: A Logic for Shared Mutable Data Structures"** —
  **LICS 2002**, not POPL, despite separation logic's deep POPL afterlife.
- **Milner, "A Theory of Type Polymorphism in Programming"** — **JCSS 1978**;
  the POPL entry in that line is Damas & Milner 1982 above.
- **Wadler, "Theorems for Free!"** — **FPCA 1989**, not POPL.
- **Lattner & Adve's LLVM paper** — **CGO 2004**; neither POPL nor PLDI.
- **Hoare's axiomatic-basis paper** — **CACM 1969**, predating POPL entirely.

Adding a new exemplar: confirm on dblp (`dblp.org/db/conf/popl/`) or the PACMPL
issue table of contents on the ACM DL, record authors/year/pages or article number,
and update the access date. If verification tooling is unavailable, add the row as
**待核实** with no venue attribution.
