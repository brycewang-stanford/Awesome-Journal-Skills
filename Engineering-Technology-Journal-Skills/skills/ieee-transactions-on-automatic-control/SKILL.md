---
name: ieee-transactions-on-automatic-control
description: Use when targeting IEEE Transactions on Automatic Control (TAC) or deciding whether a systems-and-control manuscript fits this venue. Encodes the journal's fit, the theory-first contribution bar, proof and assumption rigor, paper-vs-technical-note framing, house style, official-submission re-check, and desk-reject heuristics.
---

# IEEE Transactions on Automatic Control (ieee-transactions-on-automatic-control)

## Journal positioning

IEEE Transactions on Automatic Control (TAC) is the flagship archival journal of
the systems-and-control field, publishing rigorous theoretical and methodological
contributions across control theory, estimation, optimization for control, hybrid
and networked systems, and the mathematics of dynamical systems. The defining
expectation is a **provable, general result**: a new theorem, a new method with
guarantees, or a sharp answer to an open systems-and-control question. Application
papers that tune a known controller for one plant, or simulation studies without a
generalizable theoretical contribution, are a poor fit and are routinely returned.
This skill is a **fit / venue-selection / re-framing** tool. It does not replace
the journal's current official author information. Before submitting, re-check the
live IEEE TAC author guidance and submission system.

## When to trigger

- The author names TAC as the target for a control-theory, estimation, or
  dynamical-systems manuscript and wants a fit/framing check.
- A control contribution must be re-framed from "we controlled this system" into a
  general theorem or method statement with explicit assumptions.
- The author is choosing between TAC and `automatica`, or between a full Paper and a
  Technical Note / shorter contribution.
- The author needs TAC's specific desk-reject heuristics and a credible
  alternative-venue route for application-heavy work.

## Scope & topic fit

- Control theory: stability, robust/H-infinity, adaptive, nonlinear, optimal,
  model-predictive, and geometric control, with new analysis or synthesis results.
- Estimation and filtering: state estimation, observers, Kalman-type and set-membership
  filtering, when the contribution is a new guarantee or method, not a tuning.
- Networked, distributed, multi-agent, and hybrid/switched systems; event-triggered
  and quantized control; consensus and distributed optimization with convergence
  proofs.
- Optimization, game-theoretic, and learning-based control when the result is
  rigorous (stability/convergence/regret guarantees), not purely empirical.
- Stochastic systems and control; systems-theoretic aspects of dynamical systems.

## Method & evidence bar

- The central object is a **theorem with a correct, complete proof** under clearly
  stated, non-vacuous assumptions; the generality and tightness of the result are
  what carry the paper.
- Assumptions must be reasonable and explicitly discussed: a result that holds only
  under assumptions that effectively presuppose the conclusion is not a contribution.
- Numerical examples are illustrations, not evidence of generality; simulations
  support intuition but never substitute for the proof.
- Position against the closest prior results precisely: state what is new relative to
  existing theorems (weaker assumptions, larger class of systems, tighter bound,
  constructive vs. existence).
- Notation must be standard and self-consistent; the problem formulation must be
  mathematically precise before any result is stated.

## Structure & house style

- IEEE double-column format; TAC publishes full **Papers** and shorter
  **Technical Notes / Correspondence** — match the article type to the size and
  scope of the contribution, and re-check current definitions on the live guide.
- Problem statement and assumptions come early and precisely; main results are
  stated as numbered theorems/propositions/lemmas with proofs (in-text or in an
  appendix per the current format).
- The introduction must position the open problem and the gap in existing theory,
  not survey applications.
- Figures are used sparingly and purposefully (block diagrams, convergence/phase
  plots); the paper stands on its theorems, not its plots.
- Supplementary proofs/appendices carry length-limited material per current rules.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the IEEE Author Center
  anchors, then cite the current TAC-specific page you checked.
- Search the live site for "IEEE Transactions on Automatic Control information for
  authors" and follow the current ScholarOne/IEEE version.
- Re-check article types (Paper vs. Technical Note), page/length limits and
  overlength policy, and the IEEE double-column template.
- Confirm reproducibility/data/code expectations for any numerical or experimental
  results.
- Re-check ORCID, competing-interests, funding, author-contribution, and AI-use
  disclosure requirements, and IEEE open-access options.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The contribution is stated as a general theorem/method with explicit, non-vacuous assumptions — not as a successful control of one plant.
- [ ] Every main result has a complete, correct proof; simulations are illustrative only.
- [ ] The novelty is pinned to specific prior theorems (weaker assumptions / wider class / tighter bound / constructive).
- [ ] The problem formulation is mathematically precise before any result is stated.
- [ ] Article type (Paper vs. Technical Note) matches the scope, and length is within current limits.
- [ ] Notation is standard, consistent, and defined.

## Common desk-reject triggers

- Application/tuning paper: a known control method applied to one specific system with
  no generalizable theoretical contribution.
- Simulation-only "validation" with no theorem, or a theorem whose assumptions
  effectively assume the result.
- Incremental extension of an existing result with no weakening of assumptions or
  broadening of the system class.
- Incorrect, incomplete, or hand-waved proofs; mismatched or undefined notation.
- Scope mismatch: a signal-processing, pure-optimization, or machine-learning paper
  with control only as a label.

## Re-routing decision

- Methodological control breadth, longer development → `automatica`.
- Signal-processing estimation/detection as the core → `ieee-transactions-on-signal-processing`.
- Power-system or power-electronics control application → `ieee-transactions-on-power-systems` / `ieee-transactions-on-power-electronics`.
- Robotics planning/control as the central contribution → `ieee-transactions-on-robotics` / `the-international-journal-of-robotics-research`.
- Optimization theory with no control object → a dedicated optimization venue.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] IEEE Transactions on Automatic Control
[Topic tags] <2–3 closest control subtopics>
[Contribution type] theorem / method-with-guarantee / open-problem answer
[Method/evidence] <does the result clear the generality + proof-rigor bar?>
[Top risk] <the single most likely reason for rejection>
[Article type] Paper / Technical Note
[Official items to re-check] <article type / length / template / data-code / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
