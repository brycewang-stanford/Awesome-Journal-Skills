---
name: colt-review-process
description: Use when reasoning about COLT (Conference on Learning Theory) peer review — the double-anonymous-with-informed-area-chair model, correctness-first evaluation by expert theorists, the rebuttal stage before decisions, single-track acceptance stakes, and how PMLR publication and the community's proof culture shape outcomes.
---

# COLT Review Process

Use this to plan around COLT's review pipeline. Process facts below were verified
against the COLT 2026 CFP on 2026-07-08; mechanics are re-decided by each edition's
program chairs, so reconfirm in the cycle you are in.

## The 2026 pipeline

- Submission via Microsoft CMT by February 4, 2026 (AoE) for the 39th edition.
- Double-anonymous refereeing with a twist: reviewers do not see author names, but the
  area chair handling the paper does, and may reveal identities to a reviewer during
  the rebuttal period on request when needed for a proper review.
- Initial reviews go to authors before decisions; a rebuttal window follows.
- Accepted papers appear in PMLR (v291 carried COLT 2025; the 2026 volume number is
  assigned at publication).
- COLT is run by the Association for Computational Learning, with program chairs
  rotating yearly; the 2026 chair names were not published in a form verifiable at the
  access date (待核实 — check learningtheory.org/colt2026/).

## Who reviews a COLT paper

The pool is learning theorists: statistical learning, online learning and bandits,
optimization theory, RL theory, privacy, and adjacent CS theory. Practical
consequences:

- Expect at least one reviewer working within epsilon of your subfield who will
  actually verify proofs, not skim them.
- "Standard techniques" claims get adjudicated by people who know the standard
  techniques' exact reach — bluffing about novelty of technique fails here faster than
  anywhere else in ML.
- Empirical framing earns nothing by itself; a reviewer may value an illustrative
  experiment, but no reviewer will accept one in lieu of a proof.

## What the scores actually track

| Dimension | Raises it | Sinks it |
|---|---|---|
| Correctness | Complete proofs, tracked constants, checked external results | One irreparable gap — usually terminal regardless of other strengths |
| Significance | Resolving a known open question; improving a known rate; a clean new model | A bound in a model nobody asked about, unmotivated |
| Novelty of technique | An argument that visibly cannot be assembled from known parts | A reduction the reviewer completes in the margin |
| Tightness / completeness | Matching upper and lower bounds; explicit regime coverage | Upper bound only, gap to the known lower bound unexamined |
| Clarity | Formal setup early, roadmap per proof, stable notation | Definitions scattered; appendix required to parse the theorem |

## Decision dynamics

- One sustained correctness objection outweighs any number of enthusiasm points; the
  AC's first job is deciding whether the proofs close.
- Because the AC knows author identities, arguments in rebuttal should stand on
  mathematics alone — appeals to seniority or track record are visible and land badly.
- Significance disputes ("who cares about this model?") are where rebuttals genuinely
  move decisions: a crisp paragraph tying the model to a named prior line, an open
  problem, or an empirical phenomenon can flip a fence-sitter.
- COLT is single-track and relatively small; acceptance implies your talk enters the
  entire community's field of view, and the bar reflects that.
- Some editions have used an "accept with minor revisions verified by the AC" flavor
  of shepherding for fixable issues; whether the current cycle does is announced with
  decisions (待核实).

## Reading a COLT review

```text
Review anatomy — where the decision signal lives:
1. Summary paragraph      -> did the reviewer parse the model correctly?
                             If not, your rebuttal's first job is the misread.
2. "Detailed comments"    -> line-numbered proof remarks; each is a verification
                             trace. Silence about App. C means C was not read.
3. Questions to authors   -> the actual decision hinges; answer these first.
4. Typo list              -> free labor; acknowledge briefly, fix silently.
```

Reviews that engage deeply with the proofs are good news even when negative — the
paper was taken seriously, and precise objections are answerable. The dangerous review
is the short, high-level one; it signals the significance case never landed, and that
is a framing problem the rebuttal must solve.

## After the decision: reading the outcome

- **Accept:** the reviews still matter — camera-ready promises made in rebuttal are
  expected in the final PDF, and the AC may check (`colt-camera-ready` keeps the
  ledger).
- **Reject with proof-level reviews:** you received a free verification report from
  three experts. Patch the mathematics, then choose between the next COLT, ALT
  (the same community's sister venue, roughly anti-phased deadline), or a journal if
  the fixed version grew.
- **Reject with significance objections only:** the theorems survived; the framing
  died. Rebuild the known-vs-new ledger and the model-motivation paragraph before
  resubmitting anywhere — the same reviewers may see it again in a small community.
- **Reject you believe is wrong:** there is no formal appeals process to rely on;
  the productive channel is a stronger paper, since the community re-reviews
  resubmissions on their mathematics.

## Confidentiality and conduct

- Submissions are confidential; reviewers may not use or share the results before
  publication.
- COLT publishes a code of conduct for participants (a 2026 page exists at
  learningtheory.org); professional-conduct expectations extend to the rebuttal tone.
- Reviewer conflicts run through CMT domain and coauthor declarations — enter them
  completely, since the informed-AC model depends on accurate conflict data.
- Discussing your submission publicly (talks, social media) during review is not
  forbidden by anonymity rules aimed at reviewers, but volume-seeking publicity
  during the review window is poor form in a community this small.

## Cycle-volatility warnings

- Portal, anonymity mechanics, rebuttal format, shepherding, and decision timeline are
  annual decisions. Decision dates for 2026 were not on the pages checked (待核实).
- Reviewer-volunteering expectations for submitting authors have not been a stated
  COLT policy in the verified material; do not assume one either way without the
  current CFP.

## Output format

```text
[Stage] pre-submission / under review / rebuttal / decision
[Score driver] correctness / significance / technique / tightness / clarity
[Reviewer engagement] deep proof-level / shallow-summary (framing failed)
[Rebuttal leverage] <the one thread that can move the decision>
[Process facts to reconfirm] <current-cycle items still 待核实>
```
