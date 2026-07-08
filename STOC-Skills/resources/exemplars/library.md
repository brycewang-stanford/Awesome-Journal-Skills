# STOC Exemplars Library (era × contribution type)

> **Verified via web search on 2026-07-08**, with dblp (`dblp.org/rec/conf/stoc/...`)
> and the ACM Digital Library as the checking sources for venue, year, and pages.
> Direct fetches of dblp were gateway-blocked at the access date, so each row was
> confirmed through search renderings of the exact dblp/ACM DL record. It is a
> deliberately short, verified list — five confirmed rows beat fifteen guessed ones.
>
> **Sibling-confusion guard:** STOC is **not** FOCS. The two venues alternate
> through the theory year with near-identical scope, and famous results are
> routinely misattributed between them (see the omissions section). "It's a top
> theory paper" proves nothing about which of the two it appeared at — check the
> dblp `conf/stoc/` vs `conf/focs/` key before citing.
>
> **Use principle (zero hallucination):** rows give positioning only. Do not quote
> theorem statements, constants, or claims from memory — open the paper. Policy
> facts live in [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row nearest your contribution type and study how the paper makes a
result legible to a *cross-area* committee — the STOC-specific bar tested by
[`../../skills/stoc-topic-selection/SKILL.md`](../../skills/stoc-topic-selection/SKILL.md)
and executed on the page by
[`../../skills/stoc-writing-style/SKILL.md`](../../skills/stoc-writing-style/SKILL.md).
Then ask the row's self-check question about your own draft.

---

## Verified exemplars

### Foundational concept: NP-completeness

- **Stephen A. Cook, "The Complexity of Theorem-Proving Procedures," STOC 1971,
  pp. 151–158.** Verified: `dblp.org/rec/conf/stoc/Cook71.html`.
  - **Why it is an exemplar:** the canonical proof that a *conceptual* move — a
    definition and a reduction — can be a flagship result with no improved bound
    in sight. The paper that made "STOC-scale significance" mean opening a field.
  - **Self-check:** if your result's bounds are modest, does the conceptual
    payoff stand alone the way a new complexity class did?

### Algorithmic technique with cross-field reach: high-dimensional search

- **Piotr Indyk and Rajeev Motwani, "Approximate Nearest Neighbors: Towards
  Removing the Curse of Dimensionality," STOC 1998, pp. 604–613.** Verified:
  `dblp.org/rec/conf/stoc/IndykM98.html`.
  - **Why it is an exemplar:** locality-sensitive hashing is the model of a
    *transferable technique* — a STOC paper whose machinery was adopted far
    outside theory. The introduction sells the problem to everyone, then the
    technique to specialists.
  - **Self-check:** could a reviewer from another sub-area name a use for your
    technique after reading only your overview?

### New analysis framework: beyond worst case

- **Daniel A. Spielman and Shang-Hua Teng, "Smoothed Analysis of Algorithms: Why
  the Simplex Algorithm Usually Takes Polynomial Time," STOC 2001, pp. 296–305.**
  Verified: `dl.acm.org/doi/10.1145/380752.380813`; journal version J. ACM 51(3),
  2004.
  - **Why it is an exemplar:** answers a decades-old mismatch between theory and
    practice by *changing the question* — a new analysis model rather than a new
    algorithm. Also the standard example of the conference/journal version pair
    (`stoc-related-work`'s version-aware citation).
  - **Self-check:** does your paper state plainly which question it changes, and
    why the old question was stuck?

### Closing a long-open problem: derandomization

- **Omer Reingold, "Undirected ST-Connectivity in Log-Space," STOC 2005,
  pp. 376–385.** Verified: `dl.acm.org/doi/10.1145/1060590.1060647`.
  - **Why it is an exemplar:** a complete resolution of a problem the whole field
    tracked (SL = L), with a technique overview a non-derandomization reader can
    follow. The shape of the "lineage test" passed at the highest level.
  - **Self-check:** is the problem you close one the committee already knows, or
    must your introduction first convince them it was worth opening?

### Modern bound-breaking: approximation barriers

- **Anna R. Karlin, Nathan Klein, and Shayan Oveis Gharan, "A (Slightly) Improved
  Approximation Algorithm for Metric TSP," STOC 2021 (STOC Best Paper); full
  version arXiv:2007.01409; journal version Operations Research 72(6), 2023.**
  Verified via the authors' publication records and the arXiv/ACM trail.
  - **Why it is an exemplar:** the improvement is numerically tiny (below 3/2 by
    an explicit ε) and the paper says so in its own title — honesty as framing.
    The significance case rests entirely on the *barrier* broken, which is
    exactly how `stoc-related-work`'s barrier lane should be argued. Also a
    model of the extended-abstract/arXiv-full-version split this pack teaches.
  - **Self-check:** if your improvement is small, does the paper name the
    barrier and prove that crossing it required new machinery?

---

## By era and contribution type

| Era | Exemplar | Contribution type | Pack skill it illustrates |
| --- | --- | --- | --- |
| 1971 | Cook, STOC 1971, 151–158 | Field-opening concept | `stoc-topic-selection` (conceptual payoff) |
| 1998 | Indyk–Motwani, STOC 1998, 604–613 | Transferable technique | `stoc-writing-style` (two-audience overview) |
| 2001 | Spielman–Teng, STOC 2001, 296–305 | New analysis model | `stoc-related-work` (version pairs) |
| 2005 | Reingold, STOC 2005, 376–385 | Closing a named problem | `stoc-topic-selection` (lineage test) |
| 2021 | Karlin–Klein–Oveis Gharan, STOC 2021 | Barrier-breaking bound | `stoc-camera-ready` (full-version culture) |

---

## Omitted after checking (do not attribute to STOC without re-verification)

- **Shor's quantum factoring algorithm** — "Algorithms for Quantum Computation:
  Discrete Logarithms and Factoring" is **FOCS 1994**, not STOC. The single most
  common STOC/FOCS misattribution; omitted as a guardrail.
- **The PCP theorem papers** — Arora–Safra and Arora–Lund–Motwani–Sudan–Szegedy
  are **FOCS 1992** announcements (with JACM 1998 journal versions). Related
  hardness milestones do appear at STOC, but do not place "the PCP theorem"
  there without checking the specific paper.
- **AKS primality ("PRIMES is in P")** — journal publication in **Annals of
  Mathematics (2004)**; not a STOC paper despite its ubiquity in theory syllabi.
- **Gödel Prize 2026 basis papers** (robust high-dimensional estimation,
  Diakonikolas et al.) — the awarded line runs through **FOCS 2016 / SICOMP**;
  the prize is SIGACT-administered but the papers are not STOC papers.

Before adding a row: locate the dblp record under `conf/stoc/`, match the edition
year and page range, note the journal version if one exists, and update the
access-date header. If dblp cannot be reached, add the candidate as
**待核实 with no venue attribution** rather than guessing between STOC and FOCS.
