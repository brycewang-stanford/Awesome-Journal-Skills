---
name: informs-journal-on-computing
description: Use when targeting INFORMS Journal on Computing (IJOC) or deciding whether an algorithms / optimization / computational-methods / ML-for-OR manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# INFORMS Journal on Computing (informs-journal-on-computing)

## Journal positioning

The INFORMS Journal on Computing (IJOC) sits at the interface of operations research and computer science. It publishes work on the design, analysis, and implementation of algorithms and computational methods for OR and management science: exact and heuristic optimization, computational stochastic and simulation methods, and increasingly machine learning and analytics for OR. The distinguishing requirement is a *computational* contribution — a new algorithm, a substantial methodological advance, or rigorous, reproducible computational science — not just a model or an application. The readership is the computational OR/CS-interface community.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the INFORMS / IJOC site and the editorial submission system.

## When to trigger

- The author names IJOC (or the OR/computing interface) as the target venue.
- An algorithmic, optimization-computation, simulation-method, or ML-for-OR paper needs a computing-focused INFORMS home.
- A modeling paper whose real contribution is computational needs re-framing around the algorithm and its analysis.
- The author needs IJOC's desk-reject risks and a credible INFORMS alternative list before submitting.

## Scope & topic fit

- Algorithm design and analysis for optimization: exact methods, decomposition, cutting planes, branch-and-bound/price, metaheuristics with rigor.
- Computational stochastic optimization, simulation methodology, and large-scale computation.
- Machine learning and data-driven analytics in service of OR/management problems, with a methodological contribution.
- Software, modeling languages, and reproducible computational science for OR.

## Method & evidence bar

- A genuine computational contribution: new or substantially improved algorithm/method with analysis (complexity, convergence, or bounds where applicable).
- Rigorous, reproducible computational experiments: appropriate benchmarks, fair comparisons, statistical care, and enough detail to reproduce.
- For ML-for-OR, the contribution must be methodological (not a leaderboard win) and connect to an OR/management problem.
- Code and data sharing / reproducibility is increasingly expected; experimental design must support the claimed advance.

## Structure & house style

- The introduction states the computational problem, prior methods, and the precise nature of the algorithmic/methodological advance.
- Algorithms are stated clearly with analysis; experimental sections specify instances, hardware/settings, baselines, and metrics.
- Proofs, extended results, and reproducibility artifacts go to an electronic companion / online supplement.
- Results emphasize what the method achieves (speed, scale, quality, guarantees) with honest comparison.

## Official-submission checklist

- Search the live site for "INFORMS Journal on Computing submission guidelines / author instructions" and follow the current INFORMS version, including area scope.
- Re-check formatting, abstract length, anonymization/double-blind policy, and reference style.
- Re-check the current code/data availability and reproducibility policy (badging if any) and electronic-companion rules.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the computational contribution (new/improved algorithm or method).
- [ ] Analysis (complexity/convergence/bounds) is provided where applicable; assumptions are explicit.
- [ ] Computational experiments are reproducible with fair baselines, real instances, and statistical care.
- [ ] For ML-for-OR, the methodological contribution is clear and tied to an OR/management problem.
- [ ] Abstract, anonymization, references, and code/data reproducibility policy match the current IJOC guide.

## Common desk-reject triggers

- An application or model paper with no computational/algorithmic contribution.
- Benchmark engineering or a leaderboard result with no methodological advance.
- Computational claims without reproducible experiments, fair baselines, or adequate detail.
- A pure OR theory paper with no computation, or a managerial-insight paper better suited elsewhere.

## Re-routing decision

- OR methodology / optimization theory / queueing / stochastic theory for its own sake → `operations-research`.
- Broad management insight or empirics across subfields → `management-science` (choose the right department).
- OM theory/models or empirical OM → `manufacturing-and-service-operations-management`, `production-and-operations-management`, or `journal-of-operations-management`.
- An IS contribution (analytics/ML with IS theory) → `mis-quarterly` / `information-systems-research`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] INFORMS Journal on Computing
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the algorithmic/computational contribution clear IJOC's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / blinding / reproducibility / electronic companion / code-data>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
