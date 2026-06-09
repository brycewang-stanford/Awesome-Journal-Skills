---
name: physical-review-e
description: Use when targeting Physical Review E (PRE) or deciding whether a statistical, nonlinear, soft-matter, or complex-systems physics manuscript fits this APS archival venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Physical Review E (physical-review-e)

## Journal positioning

Physical Review E is the American Physical Society's archival journal for statistical, nonlinear, biological, and soft-matter physics, covering the physics of complex systems broadly. Its defining character is methodological rigor over headline novelty: PRE publishes complete, fully documented studies that advance the quantitative understanding of statistical mechanics, nonlinear dynamics, fluid dynamics, soft and granular matter, networks, and biological physics. Unlike Physical Review Letters, PRE does not require broad-impact framing — a careful, technically sound contribution that other workers in the subfield will build on is the standard. Readership is the specialist statistical-and-complex-systems-physics community across physics, applied mathematics, and quantitative biology. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Physical Review E APS site.

## When to trigger

- The author names Physical Review E as the target venue for a complete statistical-physics, nonlinear-dynamics, soft-matter, or complex-systems study.
- A manuscript is technically rigorous and archival but lacks the broad-impact, short-format framing that Physical Review Letters demands.
- A paper develops or applies a method in statistical mechanics, kinetic theory, stochastic processes, or pattern formation and the author is choosing between PRE, PRL, and a specialist soft-matter or nonlinear-science journal.
- The author needs PRE's scope boundaries, evidence expectations, and desk-reject criteria before submission.

## Scope & topic fit

- Statistical physics: equilibrium and nonequilibrium statistical mechanics, phase transitions, critical phenomena, stochastic thermodynamics, large-deviation theory, kinetic theory.
- Nonlinear dynamics and chaos: dynamical systems, synchronization, pattern formation, reaction-diffusion systems, nonlinear waves, and time-series analysis.
- Soft matter and granular physics: colloids, polymers, liquid crystals, active matter, jamming, granular flows, and complex fluids.
- Fluid dynamics: turbulence, instabilities, microfluidics, and computational fluid physics where the physical mechanism is central.
- Biological and interdisciplinary physics: biophysics of molecules and cells, population dynamics, epidemics, and physics of living systems treated quantitatively.
- Networks and computational/complex systems: network science, statistical inference on complex systems, Monte Carlo and molecular-dynamics methods with a physics question at the core.

## Method & evidence bar

- The contribution must be a complete, self-contained study: full derivations, numerical methods, parameter ranges, and error analysis — not a preliminary or letter-length result.
- Analytical work must be rigorous and reproducible; key steps should be derivable from the paper or its appendices/Supplemental Material.
- Numerical and simulation results require documented methods (integrator, system size, equilibration, sampling), convergence checks, and statistical uncertainties, not single-run illustrations.
- Claims of universality or scaling must be supported by finite-size analysis, multiple parameter regimes, or cross-method validation as appropriate.
- Data and code supporting nontrivial computations should be made available; deposition or Supplemental Material is expected where reproducibility depends on it.
- Comparison with established theory, prior numerical results, or experiment is required to situate the advance quantitatively.

## Structure & house style

- PRE uses the standard Physical Review article format with Regular Articles as the primary type; length is governed by completeness rather than a strict short-format cap.
- Use REVTeX with the APS PACS-successor classification and structured sections (Introduction, Theory/Methods, Results, Discussion); appendices carry lengthy derivations.
- The abstract states the physical problem, method, and principal quantitative result; broad-impact rhetoric is unnecessary and discouraged.
- Figures must be quantitative and reproducible: axis-labeled, with uncertainties shown; scaling plots and data collapses are standard for critical-phenomena work.
- Supplemental Material carries extended derivations, additional parameter scans, and movies for dynamics/pattern-formation studies.
- Equations and notation follow Physical Review conventions; cite the relevant PRE/PRL literature precisely to position the work within the subfield.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Physical Review E author guidelines" and follow the current APS version.
- Re-check article-type definitions (Regular Article, Rapid Communication status if any, Comment/Reply) and current length and figure conventions.
- Re-check data-availability and code-availability requirements; confirm Supplemental Material formatting and deposition expectations.
- Re-check competing-interests, funding, and AI-use disclosure requirements; confirm preprint policy (arXiv posting is standard and compatible).
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence — the statistical/nonlinear/soft-matter advance this paper makes and which workers will build on it.
- [ ] The study is complete: derivations, numerical methods, parameter ranges, and uncertainties are fully documented.
- [ ] Simulation/numerical results include convergence and finite-size or sensitivity checks, not single-run illustrations.
- [ ] The result is quantitatively compared against established theory, prior computation, or experiment.
- [ ] Data and code needed for reproduction are available or in Supplemental Material; accession details are ready.
- [ ] The paper is positioned against recent PRE / PRL literature on this problem.

## Common desk-reject triggers

- A preliminary or letter-length result better suited to PRL, submitted without the completeness PRE expects.
- A numerical study without convergence, finite-size, or error analysis, or whose methods cannot be reproduced.
- A paper outside PRE scope (e.g., condensed-matter electronic structure belonging in PRB, or a high-energy/gravitation topic belonging in PRD).
- An incremental parameter sweep with no new physical mechanism, scaling result, or methodological advance.
- An interdisciplinary application with no genuine physics question or quantitative modeling at its core.

## Re-routing decision

- Short, broad-impact result meriting rapid high-visibility publication: `physical-review-letters`.
- Exceptionally broad, transformative result across physics: `physical-review-x`.
- Condensed-matter electronic/structural physics at the core: `physical-review-b`.
- Soft-matter or nonlinear-science specialist treatment beyond APS scope: Soft Matter (RSC), Physical Review Fluids, or Chaos (AIP) depending on subfield.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Physical Review E
[Topic tags] <2–3 closest topics>
[Method/evidence] <is the study complete and reproducible, with convergence/error analysis and quantitative comparison to theory or experiment?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / length conventions / Supplemental Material / data-code deposition / disclosure / preprint policy>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
