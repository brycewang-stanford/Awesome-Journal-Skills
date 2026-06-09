---
name: siam-journal-on-computing
description: Use when targeting SIAM Journal on Computing (SICOMP) or deciding whether a theoretical-computer-science manuscript fits this foundational algorithms-and-complexity venue. Encodes the journal's fit, framing, proof-and-rigor bar, house style, official-submission re-check, and desk-reject heuristics.
---

# SIAM Journal on Computing (siam-journal-on-computing)

## Journal positioning

SIAM Journal on Computing (SICOMP), published by the Society for Industrial and Applied Mathematics, is a foundational venue for theoretical computer science. Its defining character is rigorous theory of computation: the design and analysis of algorithms, computational complexity, data structures, cryptography, randomness, distributed and parallel computation, and the mathematical foundations of computing — with theorems and proofs at the core. SICOMP is where many landmark TCS results appear in their full, refereed journal form, often as the archival version of work first presented at conferences such as STOC and FOCS. A paper is judged on the importance of its theoretical contribution and the full correctness of its proofs, addressed to the theory-of-computing research community. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines or the editorial board's judgment. Before submitting, re-check the live author instructions on the SICOMP / SIAM site.

## When to trigger

- The author names SICOMP as the target for a rigorous theoretical-computer-science result in algorithms or complexity.
- An author is preparing the full journal version of a STOC/FOCS-type result and is choosing between SICOMP and Journal of the ACM.
- A manuscript proves new algorithmic guarantees, complexity bounds, or hardness results and needs an archival, fully refereed home.
- The author needs SICOMP's expectations on full rigor, exposition, and submission norms before committing.

## Scope & topic fit

- Algorithm design and analysis: exact, approximation, online, randomized, and parameterized algorithms with proved guarantees.
- Computational complexity: complexity classes, reductions, circuit and communication complexity, hardness of approximation, and lower bounds.
- Data structures: provable time/space trade-offs and lower bounds.
- Cryptography and pseudorandomness: rigorous security definitions, constructions, and reductions; expanders and derandomization.
- Distributed, parallel, and online computation with rigorous performance analysis.
- Foundations adjacent to TCS: computational learning theory, algorithmic game theory, and quantum computation where the contribution is theorems.

## Method & evidence bar

- Results must be complete and fully proved: every theorem established rigorously, with precise model and assumptions, no gaps, and no reliance on empirical evidence in place of proof.
- Theoretical significance is required: the contribution must advance the theory — a better algorithm with proved bounds, a new complexity separation or hardness result, a new technique — not an implementation or benchmark study.
- Proofs must be referee-verifiable in full; the computational model, resource measures, and constants/asymptotics must be stated precisely, and lemmas proved or precisely cited.
- The relationship to any conference version must be stated; the journal version is expected to contain full proofs and complete details omitted from the extended abstract.
- arXiv/ECCC posting is standard and encouraged; there is no data/code-deposition norm, though any computer-assisted argument must be documented for independent checking. MSC/ACM classification should be assigned accurately.
- Prior and concurrent results must be credited precisely, with the improvement over known bounds stated exactly.

## Structure & house style

- Standard TCS structure: abstract, introduction stating results and significance, model/preliminaries, technical sections with theorems and proofs, and references; length follows the needs of a complete, rigorous argument.
- The introduction must state the main results precisely, give the theoretical significance, position the bounds against prior work, and sketch the key technical ideas.
- Exposition must be rigorous and clear: the model and resource measures are defined precisely, asymptotics and constants are explicit, and proofs are organized so an expert can verify each step.
- Long arguments may be modularized into lemmas and propositions; technical case analyses or auxiliary computations may go to appendices.
- A clear statement of the contribution relative to any conference version belongs in the introduction.
- LaTeX is expected; SIAM has specific style and macro conventions to follow.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "SIAM Journal on Computing submission guidelines" and follow the current SIAM version.
- Re-check the submission procedure, SIAM LaTeX style/macros, and editor-handling conventions.
- Re-check the policy on conference-version relationship and the expectation of full proofs in the journal version.
- Re-check authorship, competing-interests, and AI-use disclosure requirements; confirm arXiv/ECCC preprint policy and documentation expectations for any computer-assisted argument.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence — the main theorem and the theoretical advance it makes in algorithms or complexity.
- [ ] Every proof is complete and referee-verifiable, with the model, resource measures, and asymptotics stated precisely.
- [ ] The contribution is theory-first; no claim rests on experiments rather than proofs.
- [ ] The introduction states results precisely, positions the bounds against prior work, and notes any conference-version relationship.
- [ ] arXiv/ECCC status and any computer-assisted-argument documentation are consistent with policy; classification is assigned.
- [ ] The result's significance matches a foundational TCS venue, not an applied or systems outlet.

## Common desk-reject triggers

- An empirical, systems, or applied paper whose contribution is implementation or benchmarks rather than proved theory.
- A result with incomplete proofs, an imprecise model, or claims resting on experiments instead of theorems.
- An incremental improvement of a known bound without a new technique or structural insight.
- A journal submission that merely reproduces a conference extended abstract without the full proofs and details expected.
- Overstated significance or imprecise positioning relative to existing algorithmic or complexity results.

## Re-routing decision

- A flagship-level result of the broadest importance across computer science: `journal-of-the-acm`.
- A learning-theory result whose home community is machine learning theory: `journal-of-machine-learning-research`.
- A continuous/numerical-computation result driven by analysis rather than discrete complexity: `foundations-of-computational-mathematics`.
- A broad expository or survey treatment for a wide computational audience: `siam-review`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] SIAM Journal on Computing
[Topic tags] <2–3 closest areas / TCS themes>
[Method/evidence] <are the proofs complete and referee-verifiable, with a precise model, and is the contribution a foundational TCS advance?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission/SIAM LaTeX style / conference-version policy & full proofs / classification / arXiv-ECCC & computer-argument documentation / disclosure>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
