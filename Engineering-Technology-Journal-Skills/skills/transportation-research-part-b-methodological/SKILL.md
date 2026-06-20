---
name: transportation-research-part-b-methodological
description: Use when targeting Transportation Research Part B (Methodological) or deciding whether a transportation manuscript fits this venue. Encodes the journal's methodological-flagship fit, the theoretical-contribution bar, the Part B vs. Part A/C/E routing, modeling-and-proof rigor, house style, official-submission re-check, and desk-reject heuristics.
---

# Transportation Research Part B: Methodological (transportation-research-part-b-methodological)

## Journal positioning

Transportation Research Part B (Methodological) is the Elsevier methodological
flagship of the transportation research family, publishing work whose primary
contribution is a **methodological or theoretical advance** in transportation
modeling and analysis: traffic flow theory, network equilibrium and traffic
assignment, transportation network design and optimization, travel-demand and
discrete-choice modeling, transport economics methods, and freight/logistics
modeling. The defining expectation is a generalizable method, model, or theorem —
a new formulation, a proven property, a new estimator or algorithm with
analytical justification — not an applied case study that uses existing methods.
A well-executed empirical application with no methodological novelty belongs in
Part A; this skill is a **fit / venue-selection / re-framing** tool. It does not
replace the journal's current official author guidelines. Before submitting,
re-check the live Transportation Research Part B Guide for Authors.

## When to trigger

- The author names Part B for a transportation modeling, network, choice, or
  transport-economics manuscript and wants a fit/framing check.
- A paper must be re-framed from "we applied a model to this city/dataset" into a
  generalizable methodological contribution with analytical results.
- The author is deciding among Part B (methodological), Part A (policy/behavior),
  Part C (emerging technologies), and Part E (logistics/transportation economics
  applications).
- The author needs Part B's modeling-rigor and proof expectations and its
  desk-reject heuristics.

## Scope & topic fit

- Traffic flow theory: kinematic-wave and car-following models, macroscopic
  fundamental diagrams, network loading, with new analytical or modeling results.
- Network equilibrium and traffic assignment: user/system equilibrium, dynamic
  traffic assignment, existence/uniqueness and convergence properties.
- Transportation network design and optimization: bilevel/robust/stochastic
  formulations, exact and approximation algorithms with performance guarantees.
- Travel-demand and discrete-choice modeling: new model structures, identification
  and estimation theory, behavioral econometrics for transportation.
- Transport economics methods: congestion pricing, capacity and investment theory,
  mechanism design — when the contribution is methodological, not a policy case.
- Freight, logistics, and supply-chain modeling when the advance is a formulation,
  algorithm, or analytical property rather than an industry case study.

## Method & evidence bar

- The central object is a **method, model, or theorem** with a clear,
  generalizable contribution; analytical results (existence, uniqueness,
  optimality, convergence, identification) are stated and proven where claimed.
- Assumptions must be explicit and reasonable; a result that holds only under
  assumptions that trivialize the problem is not a contribution.
- Algorithms require complexity or convergence analysis, or rigorous computational
  evidence on benchmark instances, not a single illustrative run.
- Econometric/choice contributions must address identification and estimation
  properties, not merely report coefficient estimates from one dataset.
- Numerical experiments validate and illustrate the method; they support but never
  substitute for the analytical contribution.
- Position precisely against the closest prior models/theorems: state what is new
  (weaker assumptions, broader network class, tighter bound, new identification).

## Structure & house style

- Standard methodological-article structure: precise problem formulation,
  model/method development, analytical results (propositions/theorems with
  proofs), and numerical experiments; Part B publishes full-length methodological
  articles, so route applied or short pieces elsewhere and re-check current article
  types on the live guide.
- The introduction motivates the methodological gap in the transportation
  literature, not the policy importance of a corridor or city.
- Notation must be standard and consistent; the formulation is stated precisely
  before any result, and proofs appear in-text or in an appendix per current rules.
- Figures and tables serve the method (convergence plots, sensitivity to network
  size, benchmark comparisons); the paper stands on its formulation and results.
- Supplementary/appendix material carries long proofs and full computational
  details per the current policy.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md`
  and `../../resources/official-source-map.md`; start from the Elsevier anchors,
  then cite the current Transportation Research Part B Guide for Authors page you
  checked.
- Search the live site for "Transportation Research Part B guide for authors" and
  follow the current Elsevier/Editorial Manager version; confirm you are targeting
  Part B (Methodological), not Part A/C/E.
- Re-check article types, length expectations, and structured-abstract or
  highlights requirements if applicable.
- Confirm data/code availability expectations for numerical experiments and any
  benchmark-instance sharing policy.
- Re-check competing-interests, funding, author-contribution (CRediT), and AI-use
  disclosure requirements.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The contribution is a generalizable method/model/theorem, not an application of existing methods to one dataset.
- [ ] Every analytical claim (existence/uniqueness/optimality/convergence/identification) has a complete, correct proof or rigorous justification.
- [ ] Assumptions are explicit and non-trivializing, and the result's scope is clearly delimited.
- [ ] Novelty is pinned to specific prior models/theorems (weaker assumptions / broader class / tighter bound / new identification).
- [ ] Numerical experiments illustrate and validate but do not substitute for the analytical contribution.
- [ ] The paper targets Part B specifically, not Part A/C/E, and notation/formulation is precise.

## Common desk-reject triggers

- An applied case study that uses existing models with no methodological advance (a Part A fit).
- An algorithm with no complexity/convergence analysis and only a single illustrative run.
- A choice/econometric model reporting estimates from one dataset with no identification or estimation contribution.
- Results stated without proofs, or proofs that are incomplete, incorrect, or rely on trivializing assumptions.
- Scope mismatch: a pure operations-research, pure machine-learning, or technology-deployment paper with transportation only as a label.
- Better framed for the technology-focused Part C or the logistics-applications Part E.

## Re-routing decision

- Policy, behavior, or empirical analysis without methodological novelty → Transportation Research Part A.
- Emerging-technology / sensing / data-driven ITS focus → Transportation Research Part C.
- Logistics and transportation-economics applications → Transportation Research Part E.
- Network optimization with no transportation object as the core → a dedicated operations-research venue.
- General methodological breadth beyond this bundle → consult the natural-science routing slugs only if scope truly leaves engineering.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Transportation Research Part B (Methodological)
[Topic tags] <2–3 closest methodological subtopics>
[Contribution type] new model / formulation / theorem / estimator / algorithm
[Method/evidence] <does it clear the generality + analytical-rigor bar, or is it an application?>
[Top risk] <the single most likely reason for rejection>
[Part check] B vs. A vs. C vs. E
[Official items to re-check] <article type / length / data-code / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
