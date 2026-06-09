---
name: acta-mathematica
description: Use when targeting Acta Mathematica (Acta Math.) or deciding whether a pure-mathematics manuscript meets the bar of one of the most selective journals in the field. Encodes the journal's fit, framing, proof-and-rigor bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Acta Mathematica (acta-mathematica)

## Journal positioning

Acta Mathematica, published by the Institut Mittag-Leffler (distributed by International Press), is among the most selective pure-mathematics journals in the world. Its defining character is exceptional results, not topical breadth: it publishes a small number of papers per year, drawn from across all of mathematics, that resolve major problems, introduce methods of lasting influence, or open new directions. There is no thematic restriction — analysis, geometry, number theory, algebra, dynamics, topology, and mathematical physics all appear — but the importance bar is uniform and extremely high. Readership is the research mathematics community at large, and a paper is judged on the depth, correctness, and significance of its theorems and on the durability of the techniques it introduces. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines or the editorial board's judgment. Before submitting, re-check the live author instructions on the Acta Mathematica / Institut Mittag-Leffler site.

## When to trigger

- The author believes a result resolves a long-standing problem or introduces a method of broad and lasting significance, and is considering the very top general venues.
- A manuscript is being weighed between Acta Mathematica and Annals of Mathematics or Inventiones Mathematicae.
- An author needs a candid read on whether a strong, correct result is also significant enough for an extremely selective generalist journal rather than a strong specialist one.
- The author needs Acta Mathematica's expectations on full rigor, exposition, and submission norms before committing.

## Scope & topic fit

- Major advances in analysis: harmonic analysis, PDE, functional analysis, complex analysis, and ergodic theory at the level of resolving central problems.
- Number theory and arithmetic geometry: deep results in analytic or algebraic number theory, automorphic forms, and arithmetic of varieties.
- Geometry and topology: differential and algebraic geometry, geometric analysis, low-dimensional and geometric topology with field-shaping consequences.
- Dynamical systems and probability: structural theorems, rigidity, and probabilistic results of broad importance.
- Algebra, representation theory, and mathematical physics where the contribution reshapes a research area.
- Cross-cutting work that introduces a technique used widely afterward, regardless of its home subfield.

## Method & evidence bar

- Results must be complete and fully proved: every theorem is established rigorously, with no gaps, no appeals to unpublished or "folklore" claims without proof, and no reliance on unverified computation.
- Significance is the binding constraint: correctness alone is insufficient; the work must resolve an important problem or introduce methods of lasting, cross-area influence.
- Proofs must be referee-verifiable in full; the exposition must let an expert referee check every step, with technical lemmas either proved or precisely cited.
- The Mathematics Subject Classification (MSC) should be assigned accurately to situate the work for editors and referees.
- arXiv posting is standard and encouraged in mathematics; there is no data- or code-deposition norm, but any computer-assisted proof must be documented so it can be independently checked.
- Priority and context must be honest: prior and concurrent results are credited precisely, and the advance over the state of the art is stated exactly.

## Structure & house style

- Standard pure-mathematics structure: abstract, introduction stating the main theorems and their significance, preliminaries, the body of proofs, and references; length follows the needs of a complete, rigorous argument.
- The introduction must state the main results precisely and explain why they matter and how they relate to prior work; for a top generalist venue this framing carries real weight.
- Exposition must be of the highest quality: definitions precise, notation consistent, and proofs organized so a reader can follow the architecture before the technical detail.
- Long or technical arguments may be modularized into lemmas and propositions; auxiliary computations or routine verifications may go to appendices.
- Statements of theorems should be self-contained and quotable; hypotheses and conclusions must be unambiguous.
- LaTeX is expected; bibliographic and formatting conventions follow the journal's current style.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Acta Mathematica submission instructions" and follow the current Institut Mittag-Leffler / International Press version.
- Re-check the submission procedure, file-format and LaTeX requirements, and any editor-handling or pre-screening conventions.
- Re-check MSC classification requirements and the journal's expectations on exposition and length.
- Re-check authorship, competing-interests, and any AI-use disclosure requirements; confirm arXiv/preprint posting policy and documentation expectations for computer-assisted proofs.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence — the main theorem and why it is a major advance across mathematics, not only within its subfield.
- [ ] Every proof is complete and referee-verifiable, with all lemmas proved or precisely cited and no unverified computation.
- [ ] The introduction states results precisely and positions them honestly against prior and concurrent work.
- [ ] MSC classification is assigned accurately.
- [ ] Any computer-assisted component is documented for independent verification; the preprint/arXiv status is consistent with policy.
- [ ] The work is genuinely at the significance level of Acta Mathematica, not merely strong and correct.

## Common desk-reject triggers

- A correct and solid result that is not significant enough for an extremely selective generalist journal — a specialist or strong field journal is the right home.
- A proof with gaps, hand-waved steps, or reliance on unproved "folklore" or unverified computation.
- Overstated significance or imprecise positioning relative to known results.
- A manuscript whose exposition is too disorganized for a referee to verify the argument.
- Incremental improvement of an existing theorem without a method or consequence of lasting, cross-area importance.

## Re-routing decision

- A field-defining result that is an equally natural fit for the other apex generalist venue: `annals-of-mathematics`.
- A major advance, especially in geometry, number theory, or arithmetic geometry, at top generalist level: `inventiones-mathematicae`.
- A strong, correct, but more specialized result: the leading journal of the relevant subfield.
- Computation-at-the-interface results with rigorous foundations rather than pure-math significance: `foundations-of-computational-mathematics`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Acta Mathematica
[Topic tags] <2–3 closest areas / MSC themes>
[Method/evidence] <are the proofs complete and referee-verifiable, and is the result significant enough for an apex generalist journal?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission/LaTeX format / MSC classification / exposition & length / arXiv & computer-proof documentation / disclosure>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
