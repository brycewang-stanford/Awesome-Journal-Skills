---
name: tacas-related-work
description: Use when positioning a TACAS (ETAPS) submission against the verification literature across TACAS, CAV, VMCAI, FMCAD, SPIN, and journals (STTT, FMSD), writing delta-first contrast against the nearest tools and algorithms, crediting the benchmarks and solvers you build on, keeping self-citations anonymous for double-blind research papers, and handling competition-tool and prior-version overlap.
---

# TACAS Related Work

Use this to audit novelty and eligibility. TACAS reviewers are close to the verification literature
and to the tools it produces, so they expect to see where your algorithm or tool sits relative to
the nearest prior work — as a **delta**, not a catalog. Reopen the current call for dual-submission,
anonymity, and prior-publication rules before advising authors.

## Positioning checks

- **Separate the algorithmic novelty from the engineering.** What is new: a new decision procedure,
  a new encoding, a new abstraction, a tool that first makes a technique usable, or a case study
  that first applies it at scale? Name it precisely.
- **Cover the verification venues.** TACAS reviewers expect the flagships and the journals, not just
  the papers nearest your method (see the table). Missing the obvious CAV/VMCAI/FMCAD predecessor
  reads as unaware.
- **Credit what you build on.** If you use an SMT solver, a benchmark suite, or a model-checking
  backend, cite it — TACAS is a tool-and-algorithm community and reviewers notice uncredited
  infrastructure or benchmarks.
- **Write delta-first.** Each closely related tool/algorithm gets one sentence on what it did and one
  on what you do differently (a stronger guarantee, a new class handled, an order-of-magnitude
  scaling, a first working tool) — not a summary.
- **Anonymity by category.** For a **double-blind research** paper, cite your own prior work in the
  third person and never link reviewers to an identity-revealing preprint or repository. A **tool /
  case-study** paper is single-blind and cites itself normally.
- **Declare overlap** with any prior workshop version, SV-COMP competition paper, or concurrent
  submission; do not re-submit archival work as new.

## Verification literature lanes

| Lane | Typical venues | What TACAS reviewers check |
|---|---|---|
| Tools & algorithms (home) | **TACAS** | Whether the nearest tool/algorithm predecessor is compared or distinguished |
| Broad formal methods | **CAV** | Whether the closest FM-flagship technique is credited and contrasted |
| Verification / abstract interpretation foundations | **VMCAI** | Whether the foundational predecessor is engaged |
| Hardware / SAT-centric FM | **FMCAD** | Whether the relevant hardware/SAT lineage is acknowledged |
| Explicit-state / software model checking | **SPIN** | Whether the model-checking predecessor is cited |
| Journals | **STTT, FMSD** | Whether deeper journal treatments on the topic are engaged |
| Competitions | **SV-COMP, VerifyThis** | Whether shared benchmarks / competing verifiers are credited |

A bibliography that cites only your own subarea suggests the delta is smaller than claimed; one that
reaches the flagships, journals, and competitions signals command of the field.

## Delta-first positioning vignette

Suppose the paper presents a new **tool** for bounded refinement checking. Its nearest neighbors: a
CAV algorithm that requires linearization-point annotations (yours is annotation-free), a TACAS tool
that enumerates histories without reduction (yours uses an SMT reduction and scales further), and a
journal study characterizing the problem (no tool). The novelty sentence should name all three
contrasts — annotation-free where prior work needed annotations, an SMT reduction where prior work
enumerated, and a working, benchmarked tool where the journal offered only characterization.

## Concurrent and prior-version judgment calls

```text
[SV-COMP competition paper]  your tool's competition entry is often citable but archival-limited;
                             state what the TACAS paper adds beyond the competition contribution
[Concurrent arXiv work]      cite neutrally, state the technical difference, avoid priority claims;
                             keep the citation anonymous for a double-blind research paper
[Prior workshop version]     usually citable; declare the overlap and state what the full paper adds
[Prior tool release]         crediting your own earlier tool version is fine (single-blind tool paper);
                             for a research paper, keep it third-person
```

## Eligibility red flags

- Substantial text overlap with a published paper by the same authors (self-plagiarism risk).
- A "new" tool paper that re-reports a prior release's benchmarks without a new capability.
- Citations only to non-verification venues, signaling the paper may be a visitor better suited to
  another community and not reframed.

## Output format

```text
[Eligibility] clear / needs declaration / risky
[Lanes covered] <TACAS / CAV / VMCAI / FMCAD / SPIN / journals / competitions>
[Nearest 3 works] <work -> one-line delta>
[Infrastructure credited] <solvers / benchmarks / backends cited? yes/no>
[Archival-overlap risk] <none / declare: what (incl. SV-COMP entry)>
[Novelty sentence] <TACAS-ready contribution contrast against the nearest tools/algorithms>
```
