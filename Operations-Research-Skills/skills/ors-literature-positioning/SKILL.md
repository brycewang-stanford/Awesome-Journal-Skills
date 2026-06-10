---
name: ors-literature-positioning
description: Use when placing an Operations Research (OR) manuscript against the OR/MS literature — separating your model, results, and algorithmic guarantees from the closest prior work so the novelty is unambiguous. Positions the contribution; it does not formulate the model (ors-theory-development) or write the contribution statement (ors-contribution-framing).
---

# Literature Positioning (ors-literature-positioning)

## When to trigger

- Reviewers will ask "how is this different from [closest paper]?"
- Multiple streams (optimization, stochastic, learning) touch your problem and you must situate it.
- You need to show your bound/rate/model strictly improves or genuinely differs from prior art.

## How OR positioning differs

In *Operations Research*, positioning is **technical**, not rhetorical. The reader
must see exactly which model assumptions, result strengths, or algorithmic guarantees
you change relative to the nearest prior work. Vague "gap" language does not satisfy
OR reviewers — they want a precise delta.

## Map the neighborhood precisely

- **Identify the closest 3-5 papers**, not a wall of citations. For each, record:
  the model class and assumptions, the strongest result, the algorithm and its
  complexity/convergence, and the regime where it applies.
- **State your delta against each** in concrete terms: weaker assumptions, a tighter
  bound, a better rate or complexity, a broader model class, a new regime
  (heavy-traffic, high-dimensional, adversarial), or the first provable guarantee.
- **Cross-stream placement.** OR problems often sit between Optimization, Stochastic
  Models, Simulation, and Machine Learning and Data Science. Name the streams and say
  which tools you borrow and what you add.

## Make novelty checkable

| Dimension | Make explicit |
|-----------|---------------|
| Generality | Which assumptions you remove or weaken |
| Strength | Optimality / tightness / matching lower bound |
| Efficiency | Complexity or convergence-rate improvement |
| Scope | New problem class, regime, or performance measure |
| Rigor | First *provable* result where prior work was heuristic |

A short comparison table (prior work × {assumptions, result, complexity}) is the
most persuasive OR positioning device.

## Author-year citation convention

OR uses **author-year** citations, e.g., "(Norman 1977)" or "Norman (1977)". Cite the
canonical OR sources for the model class and the technique; missing a well-known prior
result is a frequent reviewer flag. Keep the reference list in the INFORMS author-year
style.

## Positioning pushback patterns and the OR-specific fix

| Referee/AE remark | Underlying gap | Fix that satisfies Operations Research |
|-------------------|----------------|-----------------------------------------|
| "How is this different from [Author year]?" | the closest competitor's delta is implicit | add a row to the comparison table making the {assumption, result, complexity} delta explicit |
| "This duplicates a known result" | a relabeled prior theorem exists | either cite-and-differentiate the regime, or retract the novelty claim |
| "You ignore the learning literature on this" | a parallel stream solved a close variant | place the cross-stream paper; state what its tools cannot give and you add |
| "Citations are dated" | canonical OR sources missing | cite the foundational model-class and technique papers in author-year style |
| "Gap is asserted, not shown" | rhetorical 'gap' language | replace with a per-paper technical delta a referee can check line by line |

Because *Operations Research* is the INFORMS flagship for methodology, positioning is
judged on **technical** distance — a weaker assumption, a tighter bound, a better rate,
a new regime — not on a narrative gap. This is sharper than the managerial-contribution
framing used at Management Science, M&SOM, or *Journal of Operations Management*, where
positioning often turns on the decision question rather than the theorem's strength.

## Worked positioning vignette (illustrative numbers)

Suppose your result is a 1.58-approximation for a stochastic facility-location variant.
The closest prior work gives a 2-approximation under an i.i.d.-demand assumption. Naive
positioning ("we improve the approximation factor") invites the flag "but they assume
less / more." Defensible OR positioning builds the row:

| Paper | Assumption | Guarantee | Complexity |
|-------|-----------|-----------|------------|
| Prior (Author year) | i.i.d. demand | 2-approx | O(n²) |
| This paper | correlated demand (weaker) | 1.58-approx | O(n² log n) |

Now the delta is checkable on three axes at once — **broader model** (correlated
demand), **tighter guarantee** (1.58 vs 2), at a stated complexity cost. That table,
not a paragraph, is what converts an OR referee.

## Anti-patterns

- A citation dump with no per-paper delta.
- Claiming novelty against a strawman while ignoring the closest competitor.
- Overclaiming "first to study X" when a relabeled prior result exists.
- Ignoring a parallel stream (e.g., a learning paper) that solved a close variant.

## Output format

```
【Closest work】3-5 papers with {model, result, complexity}
【Delta】per paper: weaker assumptions / tighter bound / better rate / new regime
【Comparison table】drafted? yes/no
【Canonical cites】present? gaps: [...]
【Next step】ors-methods or ors-contribution-framing
```
