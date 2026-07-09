---
name: tacas-writing-style
description: Use when revising a TACAS (ETAPS) paper for a clear construction-or-analysis contribution on the first page, a stated soundness/completeness claim, honest benchmark evidence, category-appropriate structure (research vs tool vs case-study vs tool-demo), disciplined use of the 16-page (or 6-page) LNCS budget, and correct handling of double-blind wording for research papers.
---

# TACAS Writing Style

Use this when revising the main paper. TACAS papers are LNCS articles read by verification experts,
so they need the **contribution stated precisely on the first page** and **claims a reviewer can
check** — a soundness argument for a research paper, a working tool with reproducible numbers for a
tool paper. The failure this skill prevents is a paper that gestures at "efficiency" and "novelty"
without a crisp algorithmic claim or an honest evaluation.

## Revision rules (all categories)

- **Lead with the construction/analysis problem and the contribution.** State what the paper builds
  or decides, on what inputs, and how — before any adjective. A verification reader wants the object
  of study (a property, a system model, a decision problem) named immediately.
- **State the soundness claim explicitly.** "Sound," "sound and complete," "complete up to bound
  *k*," or "unsound but effective, and here is why that is acceptable" — say which, and point to the
  argument. An unstated correctness posture is the first thing a TACAS reviewer probes.
- **Pair every empirical claim with honest evidence** — named benchmarks, a fair baseline, wall-clock
  time on stated hardware, and solved/unsolved counts — not "outperforms."
- **Match structure to category.** A research paper foregrounds the algorithm and its proof; a tool
  paper foregrounds the tool, its architecture, and its artifact; a case study foregrounds the
  system and the lessons; a tool-demo foregrounds a reproducible demonstration in six pages.
- **Respect the page budget as a design constraint.** 16 pages (or 6 for a tool-demo) in `llncs.cls`,
  excluding references and appendix — a contribution that only fits by compressing the soundness
  argument is over-scoped for the category.
- **For a research (double-blind) paper, maintain anonymity in prose:** third-person self-citation,
  no tool name that identifies you, no identifying acknowledgements. A tool/case-study paper is
  single-blind and names itself.

## Category skeletons

| Category | First-page job | Backbone sections | Common failure |
|---|---|---|---|
| Research | Problem, algorithm, soundness claim, evidence preview | Preliminaries; algorithm; correctness; evaluation | Leads with a trend, hides the algorithm and its guarantee |
| Regular tool | What the tool does, how, availability | Architecture; technique realized; evaluation on benchmarks; artifact | Adjectives instead of an architecture and a fair comparison |
| Case study | The real system and the question | System; method applied; results; lessons and threats | Anecdote instead of transferable, honestly bounded lessons |
| Tool-demo | A concrete demonstration in 6 pages | What is shown; how a user drives it; what is reproducible | Compressed research paper instead of a genuine demonstration |

## Sentence-level rewrites

| Draft pattern | TACAS-safe rewrite |
|---|---|
| "Our tool is very efficient and novel." | "solves N/120 benchmarks vs M/120 for <baseline>, median 3.1x less wall-clock time (same hardware, equal timeout)" |
| "We prove the approach is correct." | "Theorem 1: the encoding is sound and complete up to bound k (proof in §3.2 / appendix)" |
| "We outperform existing approaches." | "against <named baseline> configured with an equal time budget, on <named benchmark set>" |
| "The tool scales well." | "runtime grows sub-linearly to inputs of 10^6 states; the largest solved instance is stated in Table 2" |
| "Extensive experiments show..." | "we evaluate on <benchmark set> (N tasks); results, hardware, and timeouts are in §4 and the artifact" |

## Soundness-and-evidence discipline

```text
[Guarantee]   sound? complete? bounded? unsound-but-useful? -> state it and cite the argument
[Baseline]    the strongest available tool, configured fairly, on the same benchmarks and hardware
[Reporting]   solved/unsolved, wall-clock with timeouts, memory; no single hidden headline ratio
[Reproduce]   every reported number traces to a script/log in the artifact (mandatory for tools)
-> place the guarantee near the algorithm and the evidence near the claim it supports
```

## Vignette: compressing a research paper to 16 pages

A draft with a full proof, three optimizations, and a sprawling background: keep the algorithm, the
soundness theorem with a proof sketch (full proof to the appendix), the one optimization that
carries the speedup, and the benchmark comparison; move the secondary optimizations and extended
proofs to the appendix with forward references; cut background to what the argument needs. The test
of a good cut: a reviewer can state your guarantee and reproduce your headline benchmark result from
the body alone.

## Output format

```text
[Writing diagnosis] clear / under-specified / over-claimed / evidence-thin / wrong-category-shape
[First-page fix] <new framing: problem -> contribution -> guarantee -> evidence>
[Guarantee audit] <soundness/completeness/bound stated? where argued?>
[Evidence audit] <claim -> benchmark -> baseline -> fair? reproducible? yes/no>
[Anonymity edits] (research only) <tool names / self-citations / acks to rewrite>
```
