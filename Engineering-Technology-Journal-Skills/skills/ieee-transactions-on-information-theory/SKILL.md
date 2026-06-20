---
name: ieee-transactions-on-information-theory
description: Use when targeting IEEE Transactions on Information Theory or deciding whether an information-theory manuscript fits this venue. Encodes the journal's fit, the theorem-driven achievability-and-converse bar, proof rigor, the paper-vs-correspondence framing, house style, official-submission re-check, and desk-reject heuristics.
---

# IEEE Transactions on Information Theory (ieee-transactions-on-information-theory)

## Journal positioning

IEEE Transactions on Information Theory is the archival home of information theory:
Shannon theory, channel and source coding, capacity and rate-distortion, data
compression, information-theoretic security and privacy, and the information-theoretic
limits of statistical inference and learning. The defining expectation is a
**theorem with a complete proof** — typically a matching achievability and converse,
a new bound, or a sharp characterization of a fundamental limit. Applied
communication-system papers that design or simulate a scheme without establishing an
information-theoretic result are a poor fit and are routinely redirected. This skill
is a **fit / venue-selection / re-framing** tool. It does not replace the journal's
current official author guidelines. Before submitting, re-check the live IEEE
Transactions on Information Theory author information and submission system.

## When to trigger

- The author names this journal for a Shannon-theory, coding-theory, or
  information-theoretic-limits manuscript and wants a fit/framing check.
- A coding or communication result must be re-framed from "our scheme performs well"
  into a fundamental-limit statement (capacity, exponent, converse, optimality).
- The author is choosing between this Transactions and an applied-communications
  venue, or between a full Paper and a shorter Correspondence.
- The author needs the achievability-plus-converse rigor bar and desk-reject
  heuristics specific to information theory.

## Scope & topic fit

- Shannon theory: channel capacity, source coding and rate-distortion, network
  information theory, multiterminal and feedback settings, error exponents.
- Coding theory: algebraic, graph-based (LDPC/polar), and lattice codes; bounds on
  codes; list decoding; coding for storage and distributed settings, with proofs.
- Information-theoretic security and privacy: secrecy capacity, wiretap channels,
  differential-privacy and information-leakage limits.
- Information-theoretic methods in statistics and learning: minimax and sample-complexity
  bounds, estimation and hypothesis-testing limits, information measures.
- Quantum and combinatorial information theory, and the mathematics (probability,
  combinatorics, convexity) underpinning information-theoretic results.

## Method & evidence bar

- The central object is a **theorem**: an achievability result, a converse (often a
  matching pair), a new bound, or an exact/asymptotic characterization, with a
  complete and correct proof.
- Converse arguments matter as much as constructions; a scheme without a limit, or a
  claimed optimality without a converse, is usually incomplete here.
- Asymptotic regimes and order/constant tightness must be stated precisely; clarify
  whether results are exact, asymptotic, or bounds, and under what assumptions.
- Position against the closest information-theoretic prior work: what limit is newly
  characterized, what gap is closed, or what assumption is removed.
- Notation and problem formulation must be mathematically precise and standard before
  any result is stated; simulations, if any, are illustrative only.

## Structure & house style

- IEEE format; the journal publishes full **Papers** and shorter **Correspondence**
  items — match the article type to the contribution and re-check current definitions
  on the live guide.
- The problem model (channel, source, code, estimator) and assumptions are stated
  precisely up front; main results are numbered theorems/lemmas with proofs in-text
  or in appendices per current format.
- The introduction positions the fundamental-limit question and the prior bounds, not
  application motivation.
- Figures are sparse and analytical (rate regions, exponents, bound comparisons); the
  paper stands on its theorems, not on plots.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the IEEE Author Center anchors,
  then cite the current Information Theory page you checked.
- Search the live site for "IEEE Transactions on Information Theory information for
  authors" and follow the current submission-system version.
- Re-check article types (Paper vs. Correspondence), length/overlength policy, and the
  IEEE template.
- Confirm any expectations for proof completeness, supplementary appendices, and (where
  relevant) code for constructions.
- Re-check ORCID, competing-interests, funding, author-contribution, and AI-use
  disclosure requirements, and IEEE open-access options.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The contribution is an information-theoretic theorem (achievability / converse / bound / characterization), not a scheme that "works."
- [ ] Where applicable, achievability is matched by a converse, or the gap is stated honestly.
- [ ] Every main result has a complete, correct proof under precise assumptions.
- [ ] The novelty is pinned to a specific prior limit or bound that is improved or newly established.
- [ ] Notation, channel/source model, and asymptotic regime are precise and standard.
- [ ] Article type (Paper vs. Correspondence) and length fit current limits.

## Common desk-reject triggers

- Applied communications/coding paper with a designed scheme and simulations but no information-theoretic result.
- Achievability claimed with no converse, or an "optimality" claim with no matching lower bound.
- Incorrect, incomplete, or hand-waved proofs; undefined or non-standard notation.
- Incremental bound improvement with no new technique and negligible tightening.
- Scope mismatch: a machine-learning or systems paper using information-theoretic vocabulary without an actual limit theorem.

## Re-routing decision

- Communication-system design/performance without a limit theorem → `ieee-transactions-on-communications`.
- Wireless-specific PHY/MAC scheme design → `ieee-transactions-on-wireless-communications`.
- Signal-processing estimation/detection methods → `ieee-transactions-on-signal-processing`.
- Topical systems-frontier coding/security in a special issue → `ieee-journal-on-selected-areas-in-communications`.
- Broad tutorial synthesis of an information-theory area → `proceedings-of-the-ieee`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] IEEE Transactions on Information Theory
[Topic tags] <2–3 closest information-theory subtopics>
[Result type] achievability / converse / bound / exact characterization
[Achievability vs converse] <matched? gap stated honestly?>
[Top risk] <the single most likely reason for rejection>
[Article type] Paper / Correspondence
[Official items to re-check] <article type / length / template / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
