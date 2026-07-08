---
name: stoc-experiments
description: Use when judging whether computation belongs in a STOC (ACM Symposium on Theory of Computing) paper at all — STOC accepts on theorems, with no empirical-evaluation expectation — and when it does, scoping it as certified proof computation, constructive search, or clearly labeled illustration rather than benchmarking.
---

# STOC Experiments

The ground truth about this venue: STOC papers are accepted on the strength of
theorems, and the STOC 2026 Call for Papers asks for original research on the
theory of computation with no empirical-evaluation requirement of any kind
(checked 2026-07-08). Most STOC papers contain zero computation. The question
this skill answers is not "how do I run experiments for STOC" but "does this
computation have a legitimate job in a STOC paper, and if so, which job?"

## The three legitimate jobs of computation

| Job | Example | Proof weight | Obligations |
|---|---|---|---|
| Proof step | Exhaustive check of base cases $n \le 8$; SAT-certified nonexistence of a small counterexample | Full — the theorem is false if the run is wrong | Determinism, published certificate, independent checker (see `stoc-reproducibility`) |
| Discovery instrument | Computer search that found the gadget/construction the humans then verify by hand | None — the found object is verified analytically | Optional to even mention; a sentence of credit suffices |
| Illustration | A plot showing the new algorithm's iteration count on random instances | None | Honest labeling, disclosed instances and seeds, no performance claims |
| Benchmarking against baselines | Runtime tables vs. prior implementations | Not a STOC job | Re-route: this evidence belongs at SODA's experimental siblings, ALENEX/ESA, or a systems venue |

The fourth row is the routing trap. A STOC submission whose contribution needs
runtime tables to be convincing is announcing that its theorems do not stand
alone; committees read that accurately.

## Constructive search, done credibly

Computer search that *finds* mathematical objects is a quiet workhorse of modern
combinatorics and complexity papers. The credibility rules:

- Whatever the search finds must be verified by something other than the search:
  a short analytical argument, or a tiny independent checking program whose
  correctness is inspectable.
- Report the search honestly as heuristic ("found by simulated annealing over
  weight assignments") — the *found object* is the contribution, so the finder
  needs no rigor, but pretending the finder is exhaustive when it is not would
  be a false completeness claim.
- If the paper claims *no* object exists below some size, that is a proof step,
  not discovery; it jumps to row one of the table with all its obligations.

```python
# Independent checker pattern: ~30 lines, no dependencies, verifies the
# certificate that the (arbitrarily messy) search produced.
import itertools

def is_valid_gadget(g):            # transcribes Definition 4.1 literally
    return all(constraint(g, s) for s in itertools.product([0, 1], repeat=k))

g = load("gadget.json")            # the object the paper's Lemma 4.2 uses
assert is_valid_gadget(g)          # a reader re-runs this in seconds
print("certificate valid: gadget satisfies Definition 4.1")
```

The checker transcribes a definition from the paper; anyone can audit 30 lines
against Definition 4.1. That closure — messy finder, trivial checker — is what
lets a theory reviewer accept a computed object without trusting your code.

## Illustrations, if you must

A figure can help a cross-area committee member see a phenomenon (a threshold, a
tradeoff curve, the shape of a potential function). Norms for keeping it from
harming the paper:

- Caption it as illustration explicitly; never write "experiments confirm our
  theory" — theorems are not confirmed by samples, and the phrasing invites the
  benchmark framing you are avoiding.
- Keep it small: one figure, placed near the concept it illuminates, with the
  generation procedure in one appendix paragraph (instances, sizes, seed).
- Spend no guaranteed-read space on it. The first twelve pages are for theorem
  statements and proof overview; a decorative figure inside that window costs
  real estate the reading contract makes precious.
- Ask the deletion question: if the figure vanished, would any reviewer miss
  it? If not, delete it and reclaim the page.

## Vignette: an illustration earning its page

A submission proves that a new local-search rule escapes a known family of bad
local optima. The authors add one figure: the objective-value trajectory of the
old rule and the new rule on the *lower-bound instance from their own Section
5*, showing the old rule plateauing exactly where Theorem 5.2 says it must and
the new rule passing through. Why this works as illustration rather than
benchmark: the instance is the paper's own analyzed object, not a dataset; the
phenomenon shown is the theorem's content, not a performance claim; the caption
states the instance parameters and that the plot is illustrative; and the
figure sits in the appendix with a one-line pointer from the body, spending no
guaranteed-read space. The same figure drawn on "20 standard TSPLIB instances"
would have been a benchmark — and an invitation to review the paper as an
experimental contribution it never intended to be.

## Signals you are at the wrong venue

- The abstract's strongest sentence cites a speedup factor, not a theorem.
- Reviewers would need the code to evaluate the contribution.
- The natural comparison set is prior *implementations* rather than prior
  *bounds*.
- The result's interest depends on real-world input distributions rather than
  worst-case, average-case, or smoothed analysis.

Any two of these: run `stoc-topic-selection` and look hard at SODA, ALENEX,
ESA, or an applied venue where empirical craft is rewarded instead of tolerated.

## Cycle-volatility warnings

- The theorems-first culture is structural, but scope sentences are rewritten
  each cycle; check the live CFP's topics list before arguing fit (待核实).
- Subcommunities differ: algorithmic game theory and quantum papers at STOC
  carry numerics somewhat more often than complexity papers do. Calibrate
  against recent accepted-paper lists (`acm-stoc.org/stoc2026/accepted-papers.html`).

## Output format

```text
[Computation verdict] none needed / proof step / discovery / illustration / benchmark <- re-route
[Proof-step obligations] certificate + independent checker in place? yes / no / n.a.
[Illustration budget] <figures, placement outside the 12-page window?>
[Deletion test] <what is lost if all numerics are removed>
[Venue signal] STOC-shaped / drifting empirical (target: <venue>)
```
