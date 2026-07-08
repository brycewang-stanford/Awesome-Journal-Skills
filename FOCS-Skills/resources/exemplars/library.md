# FOCS Exemplars Library (award lineage × decade)

> **Verified via web search on 2026-07-08.** Rows below are anchored to the two
> award trails FOCS itself maintains — the **Test of Time Award** (administered
> through IEEE CS TCMF, honoring FOCS papers ~10/20/30 years later) and the
> **Machtey Award** (best student paper) — cross-checked against dblp
> (`dblp.org/db/conf/focs/`) and the award citations reposted on
> `tc.computer.org/tcmf/` and `focs.computer.org`. Using award-cited papers as
> exemplars has a built-in verification bonus: the venue attribution comes from
> the venue's own award committee, not from a survey's bibliography.
>
> **Twin-venue guard:** FOCS is **not** STOC. The two flagships share scope,
> community, and even award machinery (the Knuth Prize is joint SIGACT/TCMF),
> so classic results are misattributed between them constantly. Before citing,
> check whether the dblp key is `conf/focs/` or `conf/stoc/` — see the
> misattribution list at the end.
>
> **Zero-hallucination rule:** these rows give positioning and lineage only.
> Do not quote bounds, constants, or theorem statements from memory — open the
> paper. Policy facts live in [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Each exemplar shows one way a paper earns a place in FOCS history: opening a
field, killing an assumption, founding a subarea, or unifying a landscape.
Match your draft to the *kind* of durability it aims at, then answer that
row's self-check honestly — it operationalizes the significance test in
[`../../skills/focs-topic-selection/SKILL.md`](../../skills/focs-topic-selection/SKILL.md)
and the front-loading rules in
[`../../skills/focs-writing-style/SKILL.md`](../../skills/focs-writing-style/SKILL.md).

## Test of Time lineage (venue-verified by TCMF award citations)

### The field-opener — Shor, FOCS 1994 (35th, Santa Fe)

- **Peter W. Shor, "Algorithms for Quantum Computation: Discrete Logarithms
  and Factoring," FOCS 1994, pp. 124–134.** Verified:
  `dblp.org/rec/conf/focs/Shor94.html`; FOCS Test of Time Award 2024
  (1994 target year).
  - **Why it endures:** a single algorithmic theorem that revalued an entire
    model of computation and created research programs in three fields
    (quantum computing, cryptography, number-theoretic algorithms). The
    ultimate consequence-outside-your-subarea paper.
  - **Self-check:** can you name, as concretely as Shor could, who outside
    your subarea must react if your theorem is true?

### The coding-theory bridge — Sipser & Spielman, FOCS 1994

- **Michael Sipser and Daniel A. Spielman, "Expander Codes," FOCS 1994.**
  Verified via the FOCS 2024 Test of Time citation (TCMF announcement,
  2024-11-14).
  - **Why it endures:** imported expander graphs into coding theory to get
    codes with linear-time decoding — a technique-transplant paper whose
    *method* outlived its original parameters. Model for the
    broaden-the-reach lane.
  - **Self-check:** does your technique transplant survive if your specific
    parameters are later beaten?

### The assumption-calibrator — Khot, Kindler, Mossel & O'Donnell, FOCS 2004

- **"Optimal Inapproximability Results for MAX-CUT and Other 2-Variable
  CSPs?," FOCS 2004.** Verified via the FOCS 2024 Test of Time citation.
  - **Why it endures:** tied the exact approximability of Max-Cut to the
    Unique Games Conjecture, converting a conjecture into a precision
    instrument. The question mark in the title is honest calibration —
    conditional results, stated as conditional, can be flagship results.
  - **Self-check:** if your result is conditional, does the paper make the
    condition's role a feature (a sharp equivalence) rather than a caveat?

### The barrier-namer — Abboud & Vassilevska Williams, FOCS 2014

- **"Popular Conjectures Imply Strong Lower Bounds for Dynamic Problems,"
  FOCS 2014.** Verified via the FOCS 2024 Test of Time citation.
  - **Why it endures:** systematized fine-grained hardness for dynamic data
    structures, giving a whole community a common explanation for decades of
    stuck upper bounds. A paper whose contribution is a *map*, not a single
    bound.
  - **Self-check:** does your paper explain a pattern of prior failures, or
    only add one data point to it?

### The subfield-founder — Chor, Goldreich, Kushilevitz & Sudan, FOCS 1995

- **"Private Information Retrieval," FOCS 1995 (36th).** Verified via the
  FOCS 2025 Test of Time citation (1995 target year).
  - **Why it endures:** posed a clean new problem at the
    cryptography/information-theory/complexity junction and proved the first
    nontrivial results about it — the canonical
    important-problems-benefit-from-theoretical-investigation acceptance.
  - **Self-check:** if your contribution is a new problem, do you prove
    enough about it to show the problem is rich, not just novel?

### The cross-community export — Auer, Cesa-Bianchi, Freund & Schapire, FOCS 1995

- **"Gambling in a Rigged Casino: The Adversarial Multi-Armed Bandit
  Problem," FOCS 1995.** Verified via the FOCS 2025 Test of Time citation.
  - **Why it endures:** the adversarial bandit model became load-bearing
    infrastructure in learning theory and online decision-making far beyond
    TCS — proof that FOCS rewards work whose audience only fully arrives
    years later.
  - **Self-check:** is the model you introduce minimal enough that other
    communities can adopt it without adopting your whole framework?

## Machtey lineage (student-authored, venue-verified by award coverage)

| Year | Paper | Authors (students) | Signal for your draft |
|---|---|---|---|
| FOCS 2024 | "Capacity Threshold for the Ising Perceptron" | Brice Huang (MIT) | A single sharp threshold, fully resolved, beats a family of partial results |
| FOCS 2024 | "Optimal Quantile Estimation: Beyond the Comparison Model" | Meghal Gupta, Mihir Singhal, Hongxun Wu | Optimality claims paired with the matching lower bound |
| FOCS 2025 | Obfuscation of arbitrary unitary quantum programs | Mi-Ying (Miryam) Huang (USC), Er-Cheng Tang (UW) | A long-open feasibility question answered cleanly |

(Verified via MIT LIDS and UW Allen School award announcements, 2026-07-08;
titles/author details of the 2025 paper follow the university announcement —
confirm against dblp before formal citation.)

## Misattribution guard — famous "FOCS papers" that are not FOCS papers

- **Cook, "The Complexity of Theorem-Proving Procedures"** — STOC 1971
  (`conf/stoc/Cook71`), not FOCS.
- **Goldwasser–Micali–Rackoff, interactive proofs / zero knowledge** — STOC
  1985, not FOCS.
- **Karp's 21 problems** — a book chapter (*Complexity of Computer
  Computations*, 1972), neither FOCS nor STOC.
- **Agrawal–Kayal–Saxena, "PRIMES is in P"** — *Annals of Mathematics*
  (2004), no FOCS/STOC version.
- Conversely, **Shor 1994 and Simon 1994 are FOCS**, routinely mis-cited to
  STOC because the quantum-triumvirate papers are remembered as one event.

## Recipe for adding a row

1. Find the paper on `dblp.org/db/conf/focs/` and record the `conf/focs/`
   key, edition number, pages.
2. Cross-check one independent source (award citation, IEEE Xplore record,
   or the author's own publication page naming FOCS).
3. Record what the row *teaches* — a durability pattern, not a summary.
4. If either check fails, the row enters as 待核实 with no attribution, or
   not at all. Five verified rows beat twenty remembered ones.
