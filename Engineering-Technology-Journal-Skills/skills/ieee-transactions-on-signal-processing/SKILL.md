---
name: ieee-transactions-on-signal-processing
description: Use when targeting IEEE Transactions on Signal Processing or deciding whether a signal-processing methods manuscript fits this venue. Encodes the journal's fit, the algorithm-plus-analysis bar, the baseline-and-guarantee expectation, the regular-paper-vs-correspondence framing, house style, official-submission re-check, and desk-reject heuristics.
---

# IEEE Transactions on Signal Processing (ieee-transactions-on-signal-processing)

## Journal positioning

IEEE Transactions on Signal Processing is the archival venue for the theory and
methods of signal processing: estimation, detection, sampling and reconstruction,
filtering, spectral analysis, and array, graph, and statistical signal processing,
together with the optimization machinery that underpins them. The defining
expectation is a **new signal-processing method with analysis** — an algorithm whose
behavior is characterized (consistency, convergence, performance bounds, identifiability)
or that demonstrably outperforms correct, current baselines under a clear model. A
generic machine-learning paper, or an application study that merely runs an existing
pipeline on new data, is a poor fit. This skill is a **fit / venue-selection /
re-framing** tool. It does not replace the journal's current official author
guidelines. Before submitting, re-check the live IEEE Transactions on Signal
Processing author information and submission system.

## When to trigger

- The author names this journal for an estimation, detection, sampling, or
  array/graph signal-processing manuscript and wants a fit/framing check.
- A method must be re-framed from "our algorithm gives good results" into a result
  with a signal model, analysis, and the right baselines.
- The author is choosing between this Transactions and an applications-oriented SP
  venue, a machine-learning venue, or `ieee-transactions-on-communications`.
- The author needs the SP-theoretic framing bar and desk-reject heuristics specific to
  signal-processing methods.

## Scope & topic fit

- Statistical signal processing: parameter estimation, detection and hypothesis
  testing, Cramér–Rao-type bounds, Bayesian and robust estimation.
- Sampling, reconstruction, and sparse/compressive methods; sampling theory beyond
  Nyquist; dictionary and subspace methods with recovery guarantees.
- Array and sensor-array processing: beamforming, direction-of-arrival, source
  localization, distributed and networked sensing.
- Graph signal processing and signal processing over networks: spectral methods,
  filtering, and sampling on graphs.
- Optimization for signal processing: convex/nonconvex methods, ADMM and proximal
  algorithms, with convergence or optimality analysis tied to an SP problem.

## Method & evidence bar

- The contribution is a **method with analysis**: an estimator/detector/algorithm
  whose properties (bias/variance, consistency, convergence rate, identifiability,
  recovery conditions) are characterized, or a clearly superior empirical result.
- Baselines must be the correct, current competitors under the same signal model and
  conditions; beating a strawman or an outdated method is not evidence.
- When the claim is empirical, experiments must use realistic models, report variance
  across trials, and isolate the source of improvement; when the claim is theoretical,
  proofs must be complete.
- The signal/observation model and assumptions must be explicit; performance claims
  must hold under those assumptions, with sensitivity to model mismatch discussed.
- Position precisely against prior SP results: tighter bound, weaker assumptions,
  lower complexity, or a genuinely new processing principle.

## Structure & house style

- IEEE format; the journal publishes full **Regular Papers** and shorter
  **Correspondence** items — match the article type to the contribution and re-check
  current definitions on the live guide.
- The signal model and problem statement come early and precisely; the proposed method
  and its analysis are the core, with derivations in-text or in appendices.
- The introduction motivates the SP gap, not an application novelty; relate the method
  to classical SP theory.
- Figures are analytical and comparative: MSE-vs-SNR curves, ROC curves, convergence
  plots, and benchmark comparisons under matched conditions.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the IEEE Author Center anchors,
  then cite the current Signal Processing page you checked.
- Search the live site for "IEEE Transactions on Signal Processing information for
  authors" and follow the current submission-system version.
- Re-check article types (Regular Paper vs. Correspondence), length/overlength policy,
  and the IEEE template.
- Confirm reproducibility expectations: code/data availability and reproducible-research
  practices for any empirical claims.
- Re-check ORCID, competing-interests, funding, author-contribution, and AI-use
  disclosure requirements, and IEEE open-access options.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The contribution is an SP method with analysis or a clearly superior result under a stated signal model — not a generic ML pipeline on new data.
- [ ] Baselines are the correct, current competitors under matched conditions.
- [ ] Theoretical claims have complete proofs; empirical claims report variance and isolate the improvement's source.
- [ ] The signal/observation model and assumptions are explicit, with model-mismatch sensitivity discussed.
- [ ] Novelty is pinned to a specific SP-theoretic gain (tighter bound / weaker assumptions / lower complexity / new principle).
- [ ] Article type and length fit current limits.

## Common desk-reject triggers

- A generic machine-learning or deep-learning method with no signal-processing theory or model-based framing.
- Application-only study running an existing SP pipeline on a new dataset with no methodological contribution.
- Empirical gains over weak or outdated baselines, or with no reported variance across trials.
- Algorithm proposed with no analysis and no guarantee, where the analysis was the expected contribution.
- Scope mismatch: a communications-system or control paper using SP vocabulary without an SP-theoretic result.

## Re-routing decision

- Communication-system design/performance is the core → `ieee-transactions-on-communications`.
- Wireless PHY/MAC and resource allocation → `ieee-transactions-on-wireless-communications`.
- Information-theoretic limits rather than estimators/detectors → `ieee-transactions-on-information-theory`.
- Control/estimation as a dynamical-systems theorem → `ieee-transactions-on-automatic-control` / `automatica`.
- Broad tutorial synthesis of an SP area → `proceedings-of-the-ieee`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] IEEE Transactions on Signal Processing
[Topic tags] <2–3 closest SP subtopics>
[Method + analysis] <algorithm and the guarantee/analysis that anchors it>
[Baselines] <are competitors correct, current, and matched?>
[Top risk] <the single most likely reason for rejection>
[Article type] Regular Paper / Correspondence
[Official items to re-check] <article type / length / reproducibility / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
