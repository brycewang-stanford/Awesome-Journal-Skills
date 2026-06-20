---
name: automatica
description: Use when targeting Automatica or deciding whether a systems-and-control manuscript fits this venue. Encodes the journal's fit, the methodological-breadth-with-guarantees bar, theory rigor, the Automatica-vs-TAC routing, house style, official-submission re-check, and desk-reject heuristics.
---

# Automatica (automatica)

## Journal positioning

Automatica is the IFAC-affiliated flagship journal of systems and control,
publishing rigorous, methodologically developed contributions across control,
estimation, identification, optimization, and the analysis of dynamical systems.
The defining expectation is a **method with theoretical guarantees** — stability,
convergence, optimality, robustness — developed with enough breadth and depth to
constitute an archival advance, not a single narrow result. Compared with its
sibling `ieee-transactions-on-automatic-control`, Automatica leans toward fuller
methodological development and breadth, whereas TAC also carries sharp short
Technical Notes; route by the **form and length of the main result**. Application
papers that tune a known controller, and simulation studies with no
generalizable guarantee, are a poor fit. This skill is a **fit / venue-selection
/ re-framing** tool. It does not replace the journal's current official author
guidelines. Before submitting, re-check the live Automatica author information.

## When to trigger

- The author names Automatica for a control, estimation, identification, or
  systems-theory manuscript and wants a fit/framing check.
- A contribution must be re-framed from "we solved this instance" into a method
  with stated guarantees and developed generality.
- The author is choosing between Automatica and `ieee-transactions-on-automatic-control`
  by the form and length of the result, or between a full paper and a brief paper.
- The author needs Automatica's methodological-rigor bar and a re-routing path for
  application-heavy work.

## Scope & topic fit

- Control synthesis and analysis: nonlinear, robust, adaptive, optimal,
  predictive, and geometric control, developed as a general method.
- Estimation, filtering, and system identification with consistency, convergence,
  or error guarantees.
- Networked, distributed, multi-agent, hybrid/switched, and event-triggered systems;
  consensus and distributed optimization with proofs.
- Optimization for control, game-theoretic control, and learning-based control when
  the result carries rigorous stability/convergence/regret guarantees.
- Stochastic systems and control; data-driven control with provable properties.

## Method & evidence bar

- The central object is a **method backed by theorems** with correct, complete
  proofs under clearly stated, non-vacuous assumptions; breadth of applicability is valued.
- Assumptions must be reasonable and explicitly discussed; a guarantee that holds
  only under assumptions presupposing the conclusion is not a contribution.
- Numerical examples illustrate and stress-test the method; they support but never
  substitute for the proofs.
- The development should be fuller than a single lemma: motivate the method, prove
  its properties, and discuss its scope and limitations.
- Position precisely against the closest prior methods — weaker assumptions, wider
  system class, tighter bounds, constructive vs. existence, improved computation.
- Notation standard and consistent; the problem formulation mathematically precise
  before any result is stated.

## Structure & house style

- Standard journal article in the systems-and-control style; Automatica publishes
  full papers and shorter **Brief Papers** — match the article type to the scope and
  re-check current definitions and length policy on the live guide.
- The introduction frames the open methodological problem and the gap, then states
  the contribution; it is not an application survey.
- Main results are numbered theorems/propositions/lemmas with proofs (in-text or
  appendix per current format); a clear method statement precedes the analysis.
- Figures are used purposefully — block diagrams, convergence/phase plots — and the
  paper rests on its theorems, not its simulations.
- Keep the example section proportionate to the theoretical development.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the Elsevier anchors, then
  cite the current Automatica author-information page you checked.
- Search the live site for "Automatica guide for authors" and follow the current
  Elsevier/Editorial Manager version.
- Re-check article types (regular paper vs. Brief Paper), length limits, and the
  Automatica/Elsevier manuscript format.
- Confirm reproducibility/data/code expectations for any numerical results.
- Re-check competing-interests, funding, author-contribution (CRediT), and AI-use
  disclosure requirements, and open-access options.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The contribution is a method with explicit guarantees and developed generality — not one solved instance.
- [ ] Every main result has a complete, correct proof under non-vacuous, discussed assumptions.
- [ ] Novelty is pinned to specific prior methods (weaker assumptions / wider class / tighter bound / better computation).
- [ ] The methodological development is fuller than a single short note; scope and limitations are discussed.
- [ ] The problem formulation is mathematically precise before any result is stated.
- [ ] Article type (regular vs. Brief Paper) matches the scope and length fits current limits.

## Common desk-reject triggers

- Application/tuning paper: a known method applied to one system with no general guarantee.
- Simulation-only "validation" with no theorem, or a theorem whose assumptions assume the result.
- Incremental extension with no weakening of assumptions or broadening of the system class.
- Incorrect, incomplete, or hand-waved proofs; inconsistent or undefined notation.
- Scope mismatch: a signal-processing, pure-optimization, or machine-learning paper with control as a label.

## Re-routing decision

- Rigorous theory better suited to a short Technical Note, or sharp single theorem → `ieee-transactions-on-automatic-control`.
- Signal-processing estimation/detection as the core → `ieee-transactions-on-signal-processing`.
- Robotics planning/control as the central contribution → `ieee-transactions-on-robotics` / `the-international-journal-of-robotics-research`.
- Industrial-application control with hardware as the contribution → `ieee-transactions-on-industrial-electronics`.
- Optimization theory with no control object → a dedicated optimization venue.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Automatica
[Topic tags] <2–3 closest control subtopics>
[Contribution type] method-with-guarantee / analysis result / identification-estimation method
[Method/evidence] <does the result clear Automatica's breadth + proof-rigor bar?>
[Top risk] <the single most likely reason for rejection>
[Article type] Regular paper / Brief Paper
[Official items to re-check] <article type / length / format / data-code / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
