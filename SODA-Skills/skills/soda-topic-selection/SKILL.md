---
name: soda-topic-selection
description: Use when deciding whether a result is SODA-shaped (ACM-SIAM Symposium on Discrete Algorithms) — concrete algorithmic problems, data structures, and discrete mathematics with quantitative progress — versus routing to STOC/FOCS, ESA, ICALP, ITCS, SOSA, ALENEX, SoCG, or a journal, judged from SODA's algorithms-first identity.
---

# SODA Topic Selection

SODA's identity: the joint ACM-SIAM venue for the design and analysis of
efficient algorithms and data structures for discrete problems, including the
combinatorics and discrete mathematics that feed them, and admitting
experimental validation alongside theory (SIAM SODA conference pages, checked
2026-07-08). The reviewing bench is the deepest *algorithms-specialist* pool of
any annual venue — which is precisely the fit test: SODA rewards papers whose
value is legible to algorithms experts as progress on concrete problems, not
papers needing a general theory-of-computation audience or a systems audience.

## The three-question fit test

1. **Is there a problem with a bound?** SODA papers move a quantitative frontier:
   running time, space, approximation ratio, query complexity, update time,
   list size, competitive ratio. If your contribution cannot be stated as a
   before/after on some measure of some problem, the fit is doubtful.
2. **Does the improvement need an expert to be appreciated?** SODA's specialist
   bench is an advantage exactly when the answer is yes — a `log` shaved off a
   bound that experts know is hard earns more at SODA than at a general venue
   where "only a log factor" is a slur.
3. **Is the technique discrete-algorithmic?** Combinatorial, graph-theoretic,
   geometric, algebraic, probabilistic — the toolbox of the community. A result
   proved entirely with, say, cryptographic machinery may be better read
   elsewhere even if it mentions running time.

Two of three is submission territory; the third question then picks the frame.

## Routing map from SODA's seat

| Signal in the work | Consider instead | Why |
|---|---|---|
| The point is a new complexity-theoretic barrier or model | STOC / FOCS / CCC | Cross-area significance is their filter; SODA wants the algorithm |
| Bold new problem or model, modest technical depth | ITCS | Conceptual-first reviewing; SODA referees will ask for the bound |
| Solid algorithmic result, European-cycle timing or ESA-community topic | ESA / ICALP | Same community, different calendar seats |
| The contribution is that a known result becomes *simple* | SOSA (co-located, papers due August 6, 2026 for 2027) | Simplicity is SOSA's explicit mandate; at SODA it reads as non-novel |
| The contribution is implementation and measurement | ALENEX (co-located, due July 20, 2026) | Experiments are the reviewed object there (`soda-experiments`) |
| Computational geometry core | SoCG | Its own community and calendar, though SODA takes geometry too |
| Distributed / parallel model is the point | PODC / DISC / SPAA | Model-specialist audiences |
| Learning-theoretic sample/regret bounds | COLT / ALT | Statistical-learning reviewer pool |
| Result deserves 60 pages of record, no deadline pressure | SICOMP / JACM / ACM ToA / Algorithmica | Journals archive what conferences announce |

## SODA-shaped in practice: verified exemplars

Recent best-paper-level SODA work shows the shape (verified via SIAM epubs and
institutional award announcements; details in `resources/exemplars/library.md`):

- Solving sparse linear systems faster than matrix multiplication (SODA 2021) —
  a named computational barrier crossed for a concrete problem class.
- Deterministic near-linear time minimum cut in weighted graphs (SODA 2024) —
  derandomizing a celebrated randomized bound: pure "problem with a bound."
- Breaking the metric voting distortion barrier (SODA 2024) — a stuck constant
  in social choice moved by combinatorial technique.
- Improved list size for folded Reed-Solomon codes (SODA 2025) — a parameter
  frontier in coding theory, an algorithms-adjacent lane SODA owns.

The pattern: *named problem, stuck frontier, quantitative movement, discrete
technique.* Note what is absent: new models for their own sake, systems
measurements, and philosophy.

## Borderline cases, adjudicated

Three recurring gray zones, with the deciding question for each:

- **"My result is about a model, proved with algorithms."** A new dynamic-graph
  adversary model plus matching bounds: if the bounds are the hard part and the
  model formalizes existing practice, SODA. If the model is the provocation and
  the bounds are demonstrations, ITCS. Deciding question: *would experts cite
  this for the theorem or for the definition?*
- **"My result is a lower bound."** Conditional hardness (SETH/3SUM/APSP-style)
  for a concrete problem is fully SODA-shaped — the frontier moves downward
  instead of upward, and the comparison table lists upper bounds you now match.
  Circuit or communication lower bounds whose interest is complexity-internal
  route to CCC/STOC/FOCS. Deciding question: *does the bound speak to
  algorithm designers or to complexity theorists?*
- **"My result is both simpler and slightly faster."** If the speedup stands on
  its own, SODA, with simplicity as a bonus paragraph. If the speedup is a log
  factor nobody was stuck on and the real value is a two-page proof of a known
  theorem, SOSA — where that is the entire point of the venue. Deciding
  question: *delete the simplicity claim; is what remains publishable?*

## Anti-fit signals

```text
Re-route if any of these describes the draft:
- The abstract's key sentence has no O(), no ratio, no complexity measure.
- The honest comparison table has no prior row (new problem: consider ITCS)
  or your row doesn't beat any existing row (consider the journal of record).
- The proof's interest is a connection between fields, with the algorithmic
  corollary routine (STOC/FOCS frame the connection better).
- The value is empirical dominance on real inputs (ALENEX).
- The value is that the proof fits on three pages (SOSA).
```

## Framing once fit is established

The same theorem often supports several frames; at SODA, lead with the problem
lineage ("the complexity of X has been open since [Y]"), not the technique
("we introduce a new framework"). Technique-first framing at SODA invites the
question "what does it buy?" — answer it in the title if possible:
bound-carrying titles are quoted; framework-carrying titles are skimmed.

## Output format

```text
[Fit verdict] SODA-shaped / borderline / re-route
[Three-question score] <bound? expert-legible? discrete technique?>
[Route] <SODA, or named alternative with the deciding signal>
[Frame] <problem-lineage lead sentence for the abstract>
[Calendar note] <the live deadline this verdict implies (soda-workflow)>
```
