---
name: journal-of-high-energy-physics
description: Use when targeting Journal of High Energy Physics (JHEP) or deciding whether a high-energy physics manuscript fits this author-formatted, open-access SISSA/Springer venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of High Energy Physics (journal-of-high-energy-physics)

## Journal positioning

JHEP is published by SISSA (Scuola Internazionale Superiore di Studi Avanzati) in partnership with Springer, fully open access, and is one of the highest-volume primary venues for the high-energy physics community. Its defining character is fast, author-formatted publication of technically complete work across the full HEP spectrum: formal/string theory, quantum field theory, particle phenomenology, collider and experimental HEP, and aspects of cosmology and gravity that connect to fundamental interactions. JHEP rewards correctness, completeness, and technical depth over headline novelty — it is the working journal where a community deposits the full derivation, not a glamour venue that demands broad impact. There is no length limit; long, detailed papers with full appendices are normal and expected. Readership is specialist theorists and phenomenologists who read on arXiv and value reproducible calculations. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the JHEP/SISSA site.

## When to trigger

- The author names JHEP as the target venue for a complete HEP theory, phenomenology, or experimental-interpretation paper.
- A manuscript is a full, technically detailed calculation (amplitudes, effective field theory, holography, SUSY/string constructions, BSM phenomenology) and the author is choosing between JHEP, Physical Review D, and Physical Review Letters.
- A paper is too long and detailed for a Letter and is aimed at the specialist HEP community rather than a broad-physics audience.
- The author needs JHEP's author-formatting (JHEP LaTeX class), open-access, and arXiv-first conventions, plus desk-reject criteria, before submission.

## Scope & topic fit

- Formal theory: string theory, M-theory, supergravity, conformal field theory, integrability, the swampland program, and mathematical structures of QFT.
- Quantum field theory: scattering amplitudes, effective field theories, lattice gauge theory, resurgence, anomalies, and non-perturbative methods.
- Particle phenomenology: physics beyond the Standard Model, flavor and CP, neutrino physics, dark matter model-building, electroweak and Higgs phenomenology, precision predictions for colliders.
- Collider and experimental HEP: LHC and other collider analyses, interpretation papers, Monte Carlo and reconstruction methods feeding HEP measurements.
- Holography and gravity: AdS/CFT, black-hole microstructure, entanglement and quantum information in gravity, early-universe and inflationary cosmology tied to fundamental fields.
- Heavy-ion and QCD matter when the question is fundamentally field-theoretic or thermodynamic in nature.

## Method & evidence bar

- The calculation or analysis must be complete and self-contained: derivations carried through, conventions fixed, and key steps reproducible from the paper plus appendices.
- Theoretical claims must be technically correct above all; JHEP referees check derivations, limiting cases, and consistency with known results rather than asking for broad significance.
- Phenomenology must use current data and realistic constraints (e.g., latest LHC limits, relic-density and direct-detection bounds), with explicit treatment of uncertainties and assumptions.
- Numerical and Monte Carlo results must specify tools, versions, settings, and statistical treatment so they can be reproduced.
- New formal results should be checked against established limits, dualities, or independent methods where possible.
- arXiv posting is standard practice; the submitted version should match the arXiv version, and data/code underlying numerical results should be available on request or deposited.

## Structure & house style

- JHEP uses its own JHEP LaTeX document class; manuscripts are author-formatted and the accepted version is published largely as the author typesets it.
- There is no length limit — completeness is preferred over compression; long technical appendices are normal and welcome.
- Standard structure is flexible (Introduction, technical sections, Conclusions, Appendices); section organization follows the logic of the calculation rather than a fixed template.
- Equations, conventions, and notation must be defined explicitly and used consistently; this is a major referee focus.
- References follow the JHEP/SPIRES-INSPIRE conventions; use INSPIRE-HEP citation keys and complete bibliographic data.
- Abstracts are unstructured and should state the setup, the technical result, and its consequence for the field concisely.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "JHEP author guidelines" / "JHEP submission" and follow the current SISSA/Springer version.
- Re-check the JHEP LaTeX class requirement and current author-formatting rules; confirm figure, table, and appendix conventions.
- Re-check the open-access / article-processing-charge terms and any waiver or membership arrangements that apply.
- Re-check data-availability, code-availability, and competing-interests requirements; confirm arXiv/preprint policy and INSPIRE citation conventions.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence — the technical result of this paper and where it sits in the HEP literature.
- [ ] The calculation/analysis is complete and reproducible from the main text plus appendices; conventions are fixed.
- [ ] Phenomenology uses current experimental constraints with explicit uncertainty treatment, or formal results are checked against known limits.
- [ ] The manuscript is typeset in the JHEP LaTeX class with INSPIRE-style references.
- [ ] The arXiv version matches the submission; underlying numerical data/code is available.
- [ ] The paper is positioned against recent JHEP / Phys. Rev. D work on the same problem.

## Common desk-reject triggers

- A speculative idea or model with no complete calculation, no derivation, and no testable consequence.
- A phenomenology paper using outdated constraints or ignoring obvious existing experimental bounds.
- A result that duplicates or trivially extends known work without new technical content.
- A manuscript with undefined conventions, inconsistent notation, or unverifiable numerical claims.
- A broad-audience or interdisciplinary framing that belongs in a general-physics venue rather than a specialist HEP journal.

## Re-routing decision

- US-style HEP or a paper better matched to the APS readership and PRD section structure: `physical-review-d`.
- Short, high-impact result needing rapid broad visibility and a strict length limit: `physical-review-letters`.
- Condensed-matter or non-HEP field-theory application: `physical-review-b`.
- Broad-physics or interdisciplinary high-impact framing: `physical-review-x` or a Nature-family physics venue (`nature-physics`).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of High Energy Physics (JHEP)
[Topic tags] <2–3 closest topics>
[Method/evidence] <is the calculation/analysis complete, technically correct, and reproducible, with current constraints or limit checks?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <JHEP LaTeX class / open-access charge / data-code availability / arXiv & INSPIRE conventions>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
