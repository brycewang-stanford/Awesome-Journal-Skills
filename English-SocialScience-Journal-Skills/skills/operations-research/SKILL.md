---
name: operations-research
description: Use when targeting Operations Research (OR) or deciding whether an optimization / stochastic-models / queueing / applied-mathematical-modeling manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Operations Research (operations-research)

## Journal positioning

Operations Research is the flagship methodological journal of INFORMS and one of the founding journals of the OR discipline. It publishes work that advances the methodology of operations research — optimization, stochastic processes, queueing, dynamic and Markov decision models, game theory, and applied mathematical modeling — where the contribution is a genuine theoretical or methodological advance, not merely an application. The readership is methodologically sophisticated; a paper is judged on the depth, correctness, and significance of its mathematical contribution and the importance of the problem it addresses.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the INFORMS / Operations Research site and the editorial submission system.

## When to trigger

- The author names Operations Research / OR (or the INFORMS methodological flagships) as the target venue.
- An optimization, stochastic-modeling, queueing, or decision-process paper has a real theoretical contribution and the author is choosing among OR, MS, and the computing venue.
- An applied modeling paper needs re-framing around a methodological advance rather than a case study.
- The author needs OR's desk-reject risks and a credible INFORMS / OM alternative list before submitting.

## Scope & topic fit

- Optimization: linear, integer, nonlinear, stochastic, robust, and combinatorial optimization; theory, structure, and provably good algorithms.
- Stochastic models: queueing networks, Markov decision processes, dynamic programming, applied probability, simulation methodology.
- Game theory, mechanism design, and decision analysis applied to operational and strategic problems.
- Application areas (revenue management, logistics, healthcare, energy, networks, supply chains) when the paper delivers a methodological contribution to the problem.

## Method & evidence bar

- A genuine methodological or theoretical advance: new model, new structural result, new algorithm with analysis, or a new framework — with rigorous proofs and clearly stated assumptions.
- Correctness and depth are paramount; results must be non-trivial and the contribution must be situated against the existing OR methodology literature.
- Algorithmic papers need complexity or convergence analysis and, where relevant, computational evidence — but pure benchmark engineering without a methodological contribution fits the computing venue better.
- Modeling assumptions must be defended and the managerial or scientific insight made explicit.

## Structure & house style

- The introduction states the problem, the gap in existing methodology, and the nature of the contribution precisely; it situates the work in the OR literature.
- Theorems, propositions, and proofs are central; lengthy proofs and computational details go to an online supplement / electronic companion.
- Notation is rigorous and consistent; assumptions are stated explicitly and their necessity discussed.
- A concluding discussion draws out the methodological significance and, where applicable, managerial implications.

## Official-submission checklist

- Search the live site for "Operations Research submission guidelines / author instructions" and follow the current INFORMS version, including the relevant area/department and its scope.
- Re-check formatting, abstract length, anonymization/double-blind policy, notation/style conventions, and reference style.
- Re-check the current data and code availability / reproducibility policy and electronic-companion rules.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the methodological contribution (new model / result / algorithm / framework).
- [ ] All theorems are correctly proved; assumptions are explicit and defended.
- [ ] The contribution is positioned against the OR methodology literature, not just an application area.
- [ ] Computational or numerical evidence (if any) supports — but does not substitute for — the theoretical contribution.
- [ ] Abstract, notation, anonymization, references, and data/code policy match the current OR guide.

## Common desk-reject triggers

- An application or case study with no methodological advance ("we applied known method X to problem Y").
- Incremental extensions with trivial or unproven results.
- An algorithm paper that is pure computational benchmarking with no theoretical analysis.
- A managerial-insight paper better suited to an OM venue, or a behavioral/empirical paper with no OR methodology.

## Re-routing decision

- Broad management insight or empirical work across subfields → `management-science` (choose the right department).
- Computational/algorithmic emphasis, ML-for-OR, reproducible solvers → `informs-journal-on-computing`.
- OM theory/models (supply chain, inventory, service, revenue management) → `manufacturing-and-service-operations-management` or `production-and-operations-management`.
- Empirical / behavioral / survey-based OM → `journal-of-operations-management`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Operations Research
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the methodological contribution clear OR's theory bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / area / blinding / electronic companion / data-code>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
