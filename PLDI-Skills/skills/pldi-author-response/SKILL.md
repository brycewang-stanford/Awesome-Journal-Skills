---
name: pldi-author-response
description: Use when drafting a PLDI author response inside the short February window — triaging reviewer objections about soundness, baselines, and benchmark validity, correcting factual errors with pointers into the submitted PDF, and committing to feasible revisions without promising new systems work.
---

# PLDI Author Response

PLDI 2026 gave authors a five-day response window, February 17-21, 2026, between
review delivery and the March 5 notification (dates from `pldi26.sigplan.org`,
read 2026-07-08; every cycle re-times this). The response is read by people who
build compilers and verifiers for a living: precision beats rhetoric, and a
pointer into your own submitted PDF beats a paragraph of reassurance.

## Triage before writing

Sort every reviewer point into one of four buckets and answer them in this order:

| Bucket | Example at PLDI | Correct move |
|---|---|---|
| Factual error | "The analysis ignores exceptions" when §4.2 handles them | Quote §4.2 verbatim, one sentence of context |
| Soundness doubt | "Theorem 2 seems to assume no reentrancy" | State the assumption's exact location; if the reviewer is right, say what the fix costs |
| Evaluation gap | "No comparison against the LLVM baseline at -O2" | Give the number if it exists in your logs; otherwise commit to the exact experiment, not to "more evaluation" |
| Scope disagreement | "Why not handle JIT compilation?" | Defend the stated scope; do not promise to widen it |

A soundness doubt outranks everything. One reviewer convinced your core theorem
or transformation is broken outweighs three asking for extra benchmarks, so spend
your first and best paragraph there.

## Rules that keep responses alive

- **Answer the question asked.** Implementor-reviewers notice deflection
  immediately; a direct "yes, our technique fails on X, and here is why the claim
  survives" earns more than a hedge.
- **No new contributions.** New numbers are acceptable only when they answer a
  direct question and come from the already-described setup — for instance, a
  requested baseline flag configuration. A new algorithm or proof in a rebuttal
  reads as an admission the submission was premature.
- **Quote yourself by section and line, not by memory.** Reviewers reread exactly
  what you cite; a wrong pointer costs credibility twice.
- **Budget by damage.** Give the most negative *substantive* review the most
  space; do not spend a page thanking the champion reviewer.
- **Stay anonymous.** Double-blind persists through the response; no links that
  resolve to your lab.

## A working skeleton

```text
We thank all reviewers. We first address the soundness question (Rev B),
then the baseline request (Rev A, Rev C), then smaller points.

[B1: soundness of Thm 2 under reentrancy]
Assumption A3 (§5.1, p.12) excludes reentrant callbacks; the proof uses it
in Lemma 4. We will state A3 in the theorem statement itself. The
restriction removes 2 of 14 benchmark programs (§6.1 already notes this).

[A2/C3: -O2 baseline]
Our logs include this configuration: geomean 1.11x vs 1.17x reported.
We will add the column to Table 4.

[C5: JIT scope]
Out of scope by design (§2); AOT-only assumptions are used in §4.3.
```

## After the window

Archive the response beside the submitted PDF. If the decision is acceptance,
your camera-ready and artifact must actually deliver every "we will" sentence —
PLDI reviewers routinely check; see `pldi-camera-ready` and
`pldi-artifact-evaluation`. If it is rejection, the response doubles as the
revision plan for the next November.

## Output format

```text
[Decisive issue] <the one objection that moves the decision>
[Bucket map] Rev A: ... / Rev B: ... / Rev C: ...
[New-number policy] <what may be cited, from which logged runs>
[Commitments] <numbered, feasible, camera-ready-sized>
[Anonymity check] pass / fail
```
