---
name: foundations-of-computational-mathematics
description: Use when targeting Foundations of Computational Mathematics (FoCM) or deciding whether a manuscript at the mathematics–computation interface fits this Springer journal. Encodes the journal's fit, framing, proof-and-rigor bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Foundations of Computational Mathematics (foundations-of-computational-mathematics)

## Journal positioning

Foundations of Computational Mathematics, published by Springer for the Society for the Foundations of Computational Mathematics, is a leading venue for the theory at the interface of mathematics and computation. Its defining character is rigorous mathematical foundations for computation: numerical analysis, approximation and complexity theory, optimization, computational geometry and topology, information-based complexity, and the analysis of algorithms — always with theorems and proofs at the core rather than empirical performance. The journal rewards work that establishes the mathematical basis of computational methods: convergence and error analysis, complexity bounds, stability, and structural theory, addressed to researchers who treat computation as a mathematical subject. It is selective and emphasizes depth and lasting foundational value. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines or the editorial board's judgment. Before submitting, re-check the live author instructions on the FoCM / Springer site.

## When to trigger

- The author names FoCM as the target for a result that establishes rigorous mathematical foundations of a computational method or problem.
- A manuscript proves convergence, error, complexity, or stability theory for numerical, optimization, or geometric/topological computation, and the author is choosing between FoCM and SIAM Review or Journal of the ACM.
- A paper is theory-first at the math–computation interface and would be undersold by a venue that prioritizes empirical results.
- The author needs FoCM's expectations on full rigor, exposition, and submission norms before committing.

## Scope & topic fit

- Numerical analysis with rigorous theory: convergence, error bounds, and stability of methods for differential equations, linear algebra, and approximation.
- Approximation theory, sampling, and information-based complexity: optimal rates, lower bounds, and the mathematics of recovery.
- Optimization theory: convergence and complexity of continuous and convex/nonconvex optimization, with rigorous guarantees.
- Computational complexity in the real/algebraic and continuous settings, and the analysis of algorithms over continuous structures.
- Computational geometry and topology: persistent homology, topological data analysis, and geometric computation with provable foundations.
- Mathematical foundations of learning, signal recovery, and data analysis where the contribution is theorems and bounds.

## Method & evidence bar

- Results must be complete and fully proved: theorems established rigorously with explicit hypotheses, no gaps, and no reliance on empirical evidence in place of proof.
- Foundational significance is required: the contribution must advance the mathematical understanding of a computational method or problem — sharper bounds, new convergence/complexity theory, or a structural insight — not merely a faster implementation.
- Proofs must be referee-verifiable in full; constants, rates, and assumptions must be stated precisely, and lemmas proved or precisely cited.
- Where numerical experiments appear, they illustrate or motivate the theory; they do not substitute for it, and the paper's claims rest on the proofs.
- The Mathematics Subject Classification (MSC) should be assigned accurately; arXiv posting is standard and encouraged, with any computer-assisted proof documented for independent checking. There is no data/code-deposition norm, though making accompanying code available is welcomed.
- Prior and concurrent results must be credited precisely, with the improvement over known rates/bounds stated exactly.

## Structure & house style

- Standard mathematical structure: abstract, introduction stating results and significance, preliminaries and setup, the body of theorems and proofs, optional illustrative experiments, and references.
- The introduction must state the main theorems precisely, give the foundational significance, and position the rates/bounds against prior work.
- Exposition must be rigorous and clear: precise definitions, explicit constants and assumptions, and proofs organized so an expert can verify each step.
- Long arguments may be modularized into lemmas and propositions; technical estimates or auxiliary computations may go to appendices.
- Illustrative numerical experiments, if included, must be clearly subordinate to the theory and described reproducibly.
- LaTeX is expected; bibliographic and formatting conventions follow the journal's current style.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Foundations of Computational Mathematics submission guidelines" and follow the current Springer version.
- Re-check the submission procedure, file-format and LaTeX requirements, and editor-handling conventions.
- Re-check MSC classification requirements and the journal's expectations on exposition, length, and the role of any numerical experiments.
- Re-check authorship, competing-interests, and AI-use disclosure requirements; confirm arXiv/preprint posting policy and documentation expectations for computer-assisted proofs.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence — the main theorem and the foundational advance it makes at the math–computation interface.
- [ ] Every proof is complete and referee-verifiable, with explicit constants/rates/assumptions and lemmas proved or cited.
- [ ] The contribution is theory-first; any numerical experiments illustrate rather than substitute for the proofs.
- [ ] The introduction states results precisely and positions the rates/bounds honestly against prior work.
- [ ] MSC classification is assigned; arXiv status and any computer-assisted-proof documentation are consistent with policy.
- [ ] The result's foundational significance matches FoCM rather than an applications- or empirics-driven venue.

## Common desk-reject triggers

- An empirical or applied paper whose contribution is performance rather than proved foundations.
- A result with incomplete proofs, unstated assumptions, or claims resting on experiments instead of theorems.
- An incremental improvement of a known bound without a new method or structural insight of lasting value.
- Overstated significance or imprecise positioning relative to existing rates and complexity results.
- A manuscript whose exposition is too disorganized for a referee to verify the analysis.

## Re-routing decision

- A broad, expository, survey-style treatment of a computational-mathematics topic for a wide audience: `siam-review`.
- A theoretical-computer-science result centered on algorithms and complexity rather than continuous/numerical foundations: `journal-of-the-acm` or `siam-journal-on-computing`.
- A pure-mathematics result whose computational framing is incidental: a leading pure-math venue such as `acta-mathematica`.
- An applied numerical-methods paper driven by application performance: a SIAM applied journal (e.g., SINUM, SISC).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Foundations of Computational Mathematics
[Topic tags] <2–3 closest areas / MSC themes>
[Method/evidence] <are the proofs complete and referee-verifiable, and is the contribution a foundational advance at the math–computation interface?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission/LaTeX format / MSC classification / role of numerical experiments & length / arXiv & computer-proof documentation / disclosure>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
