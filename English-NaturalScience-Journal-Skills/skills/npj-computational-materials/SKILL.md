---
name: npj-computational-materials
description: Use when targeting npj Computational Materials (npj Comput. Mater.) or deciding whether a computational or data-driven materials manuscript fits this open-access Springer Nature venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# npj Computational Materials (npj-computational-materials)

## Journal positioning

npj Computational Materials is an open-access Springer Nature journal (part of the Nature Partner Journals series) dedicated to computational and data-driven materials science. Its defining character is rigorous computation that delivers materials insight or discovery: first-principles and electronic-structure methods (DFT and beyond), molecular dynamics, multiscale modeling, machine learning and materials informatics, high-throughput screening, and the data infrastructure that supports them. The journal rewards work where the computational approach yields a generalizable conclusion, a predictive capability, or a discovery of broad materials interest — not routine single-system calculations or method applications without a clear advance. It values methodological rigor, reproducibility, and FAIR data practices, and increasingly experimental validation or testable predictions strengthen a submission. Readership spans computational materials scientists, condensed-matter physicists, materials chemists, and the growing materials-ML and informatics community. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the npj Computational Materials site.

## When to trigger

- The author names npj Computational Materials as the target for a computational or data-driven materials study of broad interest.
- A manuscript uses DFT, MD, machine learning, or high-throughput screening to reveal a generalizable materials principle, predict new materials, or develop a method, and the author is choosing between this venue and Nature Materials or Advanced Materials.
- A paper's primary contribution is computational discovery, a predictive model, or materials informatics rather than an experimental result.
- The author needs the journal's rigor, reproducibility, and FAIR-data bar plus desk-reject criteria before submission.

## Scope & topic fit

- First-principles and electronic-structure studies (DFT, GW, DMFT, beyond-DFT) that establish a materials principle, mechanism, or design rule of broad relevance.
- Molecular dynamics and multiscale modeling resolving structure-property or kinetic questions in materials.
- Machine-learning interatomic potentials, surrogate models, and ML-accelerated simulation with demonstrated accuracy and transferability.
- Materials informatics and data-driven discovery: descriptor design, property prediction, generative/inverse design, and active learning that yield validated materials insight.
- High-throughput screening and computational materials databases that produce actionable candidates or design principles.
- Methodological and workflow advances (new functionals, algorithms, automation, benchmarking) that demonstrably improve computational materials science.

## Method & evidence bar

- The generalizable conclusion, prediction, or methodological advance must be stated in one or two sentences; a single-system calculation without broader insight is misfit.
- Computational rigor is mandatory: convergence tests, justified functionals/parameters, error estimates, and validation against known references or experiment where available.
- Machine-learning work must report proper train/validation/test splits, out-of-distribution behavior, uncertainty quantification, and baselines; performance claims compared to relevant prior models.
- High-throughput and screening studies must state the search space, filters, and confidence in candidates, with experimental validation or testable predictions strengthening the case.
- Reproducibility is central: input files, structures, code/workflows, and datasets should be deposited following FAIR principles in recognized repositories.
- Claims of accuracy, transferability, or discovery must be benchmarked against the best current methods and data, not the authors' baseline alone.

## Structure & house style

- npj Computational Materials uses a Nature-style format; Articles are the primary type, with concise abstracts and integrated narrative — re-check current types and limits on the live site.
- The introduction frames the materials question and the gap the computation resolves; the readership is expert, so background is minimal and the advance is stated early.
- Figures must be efficient and quantitative: each carries a key computational result, with validation and benchmark comparisons made explicit.
- Methods describe the computational setup completely — codes, functionals/force fields, parameters, convergence criteria, ML architectures, and data provenance — for full reproducibility.
- Supplementary Information carries extended computational details, additional results, and validation data; data and code availability statements are expected.
- Claims of predictive power or discovery must be supported by validation against experiment or by clearly testable predictions.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "npj Computational Materials author guidelines" and follow the current Springer Nature version.
- Re-check current article types, length/figure expectations, and abstract format; confirm Methods and Supplementary Information conventions.
- Re-check the data- and code-availability requirements and FAIR/repository expectations central to this journal.
- Re-check open-access/APC, licensing, competing-interests, funding, and AI-use disclosure requirements; confirm preprint policy (arXiv posting compatibility).
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence — the generalizable conclusion, prediction, or method advance, and why it matters across materials.
- [ ] Computational rigor (convergence, functional/parameter choices, error estimates, reference validation) is documented.
- [ ] ML work reports proper splits, OOD behavior, uncertainty, and baselines; screening states search space and candidate confidence.
- [ ] Inputs, structures, code/workflows, and datasets are deposited following FAIR principles.
- [ ] Predictions are validated against experiment or stated as clearly testable.
- [ ] The paper is positioned against recent npj Computational Materials / Nature Materials computational work on this question.

## Common desk-reject triggers

- A routine single-system DFT or MD calculation with no generalizable principle, prediction, or method advance.
- A machine-learning model with no proper validation, baselines, uncertainty, or out-of-distribution assessment.
- A high-throughput screen with no stated confidence in candidates and no validation or testable predictions.
- Computational results with missing convergence tests, unjustified parameters, or no reference/experimental validation.
- Absent or inadequate data/code availability inconsistent with the journal's FAIR-data expectations.

## Re-routing decision

- A fundamental materials discovery whose primary impact is the new physics/chemistry of the material itself, computation supporting: `nature-materials`.
- A combined computation-plus-experiment study where a synthesized, characterized functional material is the headline result: `advanced-materials`.
- An energy-materials computational study where energy-device metrics are central: an energy-materials venue.
- A broad cross-domain methods or data paper without materials-specific framing: a general computational-science venue.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] npj Computational Materials
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the computation yield a generalizable conclusion or prediction with rigor, validation, and FAIR-data reproducibility?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article types/limits / data-code FAIR deposition / open-access & licensing / disclosure / preprint policy>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
