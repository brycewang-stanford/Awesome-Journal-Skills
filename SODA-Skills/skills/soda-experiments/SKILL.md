---
name: soda-experiments
description: Use when deciding whether and how experiments belong in a SODA (ACM-SIAM Symposium on Discrete Algorithms) paper — SODA's scope includes experimental validation but theorems carry the decision, so this skill designs supporting numerics honestly and routes implementation-led work to co-located ALENEX or to SEA.
---

# SODA Experiments

SODA's stated scope covers the design and analysis of efficient algorithms and
data structures, "including theoretical analysis and experimental validation"
(SIAM SODA conference pages, checked 2026-07-08) — but the reviewing center of
gravity is the theorem. Experiments at SODA are admissible evidence, never the
verdict. Meanwhile the same registration desk in Philadelphia hosts **ALENEX**,
the SIAM Symposium on Algorithm Engineering and Experiments, where experiments
*are* the verdict (ALENEX 2027: January 24-25, 2027, submissions due July 20,
2026, with formal artifact evaluation). The first decision is always routing.

## The routing question

| Property of your work | SODA | ALENEX | SEA |
|---|---|---|---|
| New asymptotic bound; implementation as color | Yes | No | No |
| Known-optimal theory; engineering makes it fast in practice | No | Yes | Yes |
| Experimental methodology contribution (benchmarks, measurement standards) | No | Yes (explicit scope) | Yes |
| Theory + experiments both genuinely novel | Split into two papers with disjoint claims | second paper | alternative |
| Heuristic that works, no analysis | No | Maybe, with rigorous evaluation | Maybe |

The eleven-day gap between SODA's deadline (July 9, 2026) and ALENEX's (July 20,
2026) exists to be used: the theory paper goes to SODA, and the engineering
follow-up — with its own contribution, not a reformat — goes to ALENEX.

## When numerics help a SODA submission

- **Constant-factor sanity.** A bound with towering constants invites the
  "galactic algorithm" objection; a small experiment showing the constants are
  civilized defuses it in one figure.
- **Tightness illustration.** Plotting measured cost against the proved bound on
  generated worst-case-family instances makes a tightness conjecture visible.
- **Heuristic-gap motivation.** When the paper's point is that theory lags
  practice (or vice versa), measured evidence of the gap justifies the question.
- **Counterexample exhibition.** A constructed instance defeating prior
  heuristics is stronger shown than described.

If none of these apply, include no experiments. A benchmark table bolted onto a
pure-theory SODA paper signals venue confusion and spends referee goodwill.

## Honest-numerics protocol

Experiments inside a theory paper are held to theory standards of precision
about what they claim:

- Label the claim class explicitly: *illustration* (visualizing a proved fact),
  *evidence* (supporting an unproved conjecture), or *motivation* (documenting a
  phenomenon). Never let an illustration drift into implied proof.
- Generate instances from stated distributions or named public families;
  "random graphs" without the model named is unfalsifiable.
- Report the machine, the implementation language, and whether comparisons use
  your reimplementation of the baseline (say so — reimplementation fairness is
  the standard objection).
- Deterministic seeds, released generator scripts (`soda-artifact-evaluation`
  for anonymity-safe packaging).

```text
Figure caption pattern (illustration class):
"Measured comparisons of Algorithm 1 on the lower-bound family of
Section 5 (n = 2^10..2^20, 50 seeds, median and quartiles), against
the proved O(n log n) curve (dashed). Instance generator and seeds:
see the verification archive. This figure illustrates Theorem 2; the
theorem's proof does not depend on it."
```

The final sentence of that caption is the SODA-specific move: it tells the
referee the mathematics stands alone.

## Instance-generation discipline

The credibility of a theory paper's numerics lives in the generator, not the
plot. A generator worth releasing:

```python
# gen_lowerbound_family.py -- worst-case family from Section 5 (fictional)
import argparse, random

def instance(n: int, seed: int):
    rng = random.Random(seed)          # single seeded source, no globals
    # ... construct the Section-5 gadget deterministically from (n, seed) ...
    return gadget

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, required=True)
    p.add_argument("--seed", type=int, required=True)
    a = p.parse_args()
    emit(instance(a.n, a.seed))        # documented, versioned output format
```

Requirements the referee-side rerun imposes: the paper names the family and the
parameter grid; the generator is deterministic in `(n, seed)`; the exact seeds
behind every figure are listed in the archive; and any "real-world" inputs are
named public datasets with checksums, not "graphs from our collaborators."

## Placement and proportion

- Experiments go in one clearly bounded section (or an appendix), after the
  theory, never interleaved with proofs.
- Proportion signals identity: one figure and half a page reads as a theory
  paper with due diligence; five tables reads as an ALENEX paper trapped in the
  wrong submission queue.
- The abstract mentions experiments only if they carry a claim; "we also
  implement our algorithm" is title-page noise at SODA.

## Output format

```text
[Routing verdict] SODA / ALENEX / SEA / split, with the deciding property
[Inclusion verdict] <which of the four helper roles applies, or none>
[Claim-class labels] <illustration/evidence/motivation per figure>
[Protocol gaps] <instance models, seeds, baseline fairness, machine specs>
[Proportion check] <experimental mass appropriate for a theorem-led paper?>
```
