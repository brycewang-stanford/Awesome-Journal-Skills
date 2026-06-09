---
name: communications-on-pure-and-applied-mathematics
description: Use when targeting Communications on Pure and Applied Mathematics (CPAM) or deciding whether an analysis, PDE, or applied-mathematics manuscript fits this Courant/Wiley venue. Encodes the journal's fit, framing, proof standard, house style, official-submission re-check, and desk-reject heuristics.
---

# Communications on Pure and Applied Mathematics (communications-on-pure-and-applied-mathematics)

## Journal positioning

Communications on Pure and Applied Mathematics, published by Wiley in association with the Courant Institute of Mathematical Sciences, is one of the most prestigious journals at the interface of pure analysis and applied mathematics. Its defining character is depth of analysis applied to problems with mathematical substance: partial differential equations, mathematical physics, calculus of variations, dynamical systems, probability, and applied analysis where the theory is genuine and demanding. CPAM rewards work that develops powerful analytical machinery, resolves a hard problem in PDE or analysis, or builds a rigorous theory for a phenomenon of broad mathematical or physical interest. It is not a venue for routine numerical studies, modeling papers light on theorem-proof content, or narrowly specialized technical notes. Refereeing is exacting and slow.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the CPAM Wiley site and confirm submission procedures.

## When to trigger

- The author is considering CPAM for a deep analysis or PDE paper with substantial theorem-proof content.
- A paper develops new analytical techniques for a problem in mathematical physics, variational analysis, or applied analysis and the author is choosing among CPAM, `advances-in-mathematics`, and `annals-of-mathematics`.
- An applied-mathematics result has genuine theoretical depth that exceeds the scope of a specialized applied journal.
- The author needs CPAM's significance and rigor bar, plus common rejection reasons, before submission.

## Scope & topic fit

- Partial differential equations: existence, regularity, blow-up, asymptotics, free-boundary problems, nonlinear and dispersive equations, fluid equations.
- Analysis: harmonic analysis, geometric analysis, calculus of variations, optimal transport, spectral theory.
- Mathematical physics and applied analysis where the contribution is a rigorous theorem, not a simulation or heuristic.
- Probability and stochastic analysis with deep analytical content; dynamical systems and ergodic theory.
- Applied mathematics in which the analytical theory — not the application alone — carries the contribution.
- Survey or purely expository work is not the focus; contributions must be primary research delivering new, fully proved results.

## Method & evidence bar

- The primary standard is mathematical correctness: every claim must be fully proved; no proof sketches, unresolved cases, or conditional results substituting for complete arguments (unless conditionality is the explicit contribution).
- Analytical depth is the discriminator: CPAM favors work that introduces or substantially advances technique, not incremental extensions however technically demanding.
- For applied problems, the rigorous mathematical content must dominate; modeling or numerics alone do not meet the bar without accompanying analysis.
- Exposition must let expert referees verify correctness: precise statements, complete proofs, and clear delineation of what is new versus standard.
- MSC (Mathematics Subject Classification) codes must be assigned correctly to signal scope and assist referee assignment.
- arXiv posting is standard practice; most CPAM submissions appear on arXiv before or contemporaneously with submission.

## Structure & house style

- No imposed structural template beyond mathematical convention: introduction (context, precise statement of results, proof strategy), preliminaries, core proof sections, optional appendices for technical lemmas.
- The introduction must state main results precisely and convey their significance to analysts and applied mathematicians broadly, then outline the key analytical ideas.
- LaTeX is standard; CPAM/Wiley formatting conventions apply — re-check the current style requirements on the submission site.
- References must be complete and correctly formatted; preprint citations should carry stable arXiv identifiers.
- Length is set by mathematical necessity; there is no fixed page limit, but unnecessary length attracts scrutiny — concise, complete arguments are valued.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Check the current CPAM submission instructions on the Wiley site and re-verify the submission system and procedure.
- Assign MSC primary and secondary classification codes.
- Post to arXiv (or confirm prior posting) with the identifier ready for correspondence.
- Prepare a cover letter stating the main result, its analytical significance, and suggested/excluded referees with conflicts noted.
- Confirm all co-authors have approved the submission and re-check current APC/open-access options under Wiley.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the main theorem and why it matters to analysis / applied mathematics broadly.
- [ ] Every claim is fully proved; no gaps, sketches, or unresolved cases.
- [ ] The analytical contribution is genuinely new technique or theory, not an incremental extension.
- [ ] The introduction states results precisely, explains significance, and outlines proof ideas for a broad analysis readership.
- [ ] The paper is posted or ready to post on arXiv with correct MSC codes.
- [ ] An honest assessment: is the depth at CPAM level, or would `advances-in-mathematics` be a more appropriate first submission?

## Common desk-reject triggers

- A modeling or numerical paper with little or no rigorous theorem-proof content.
- A correct but incremental analytical result that extends a known technique without a substantially new idea.
- An incomplete proof: any identifiable gap, unresolved case, or unjustified claim.
- A narrowly specialized technical note of interest to a small sub-community without broader analytical significance.
- An introduction that fails to convey significance to analysts and applied mathematicians beyond the immediate sub-field.

## Re-routing decision

Broad pure-mathematics result of high quality across any field → `advances-in-mathematics`. Truly exceptional, field-reshaping significance → `annals-of-mathematics`. Specialized PDE or applied-analysis results without broad significance → field-specific journals (Archive for Rational Mechanics and Analysis, SIAM Journal on Mathematical Analysis). Primarily numerical or computational contributions → a specialized SIAM journal.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Communications on Pure and Applied Mathematics
[Topic tags] <2–3 MSC areas>
[Method/evidence] <is the main result fully proved, analytically deep/novel, and of broad significance?>
[Top risk] <the single most likely reason for rejection — usually depth or significance>
[Official items to re-check] <submission procedure / MSC codes / arXiv posting / cover letter / style file>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
