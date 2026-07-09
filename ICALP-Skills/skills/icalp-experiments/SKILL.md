---
name: icalp-experiments
description: Use when matching the argument of an ICALP (EATCS) theory paper to its claim — choosing the proof strategy for an upper or lower bound, deciding when supporting computation (SAT/SMT-verified base cases, computer-assisted case analysis, exhaustive small-case checks) legitimately backs a theorem, and keeping any such computation reproducible without turning a proof paper into an experimental one.
---

# ICALP Experiments (proof strategy, and computation in service of proofs)

At ICALP there is usually **no experiment section** — the evidence for the claim *is the proof*. This
skill is therefore about matching the **argument** to the **claim shape**, and about the narrow, real
cases where **computation supports a theorem** (a computer-assisted proof, an SMT-checked base case, an
exhaustive small-case verification). It is deliberately not an empirical-evaluation guide: a paper
whose contribution is a benchmark result is mis-routed (`icalp-topic-selection`).

## Match the argument to the claim

| Claim shape | The argument that fits | Common failure caught by referees |
|---|---|---|
| Upper bound / faster algorithm | Algorithm + correctness proof + complexity analysis | Correctness hand-waved; complexity ignores a hidden cost |
| Approximation ratio | An analysis bounding cost vs optimum, with a tight example | Ratio proved only on the easy case; no tight instance |
| Lower bound (unconditional) | A reduction, adversary, or information-theoretic argument | Model too weak to be interesting, or gap left open |
| Conditional lower bound | A fine-grained reduction from SETH/3SUM/APSP | Wrong assumption invoked; reduction loses a factor |
| Decidability / complexity (Track B) | A decision procedure + matching hardness | Procedure sketched; hardness for a different fragment |
| Dichotomy / characterization | Exhaustive case analysis with each case proved | A case silently dropped; "similarly" hiding a hard case |

## When computation legitimately supports a theorem

Some ICALP results genuinely rely on computation. It must be **rigorous and checkable**, not
suggestive:

- **Exhaustive small-case verification** — checking a property for all objects up to size *k* as a base
  case of an induction. State the exact range, the encoding, and make the search reproducible.
- **SAT/SMT-certified steps** — using a solver to verify a finite gadget or unsatisfiability. Ship the
  encoding and, where possible, an independently checkable **certificate** (UNSAT proof, Farkas
  witness), not just "the solver said so."
- **Computer-assisted case analysis** — a program enumerating cases in a proof. The program is part of
  the proof; its logic must be described and its output verifiable.

The bar: a referee (or a reader of the full version) must be able to **re-run or independently check**
the computation. A number a solver produced with no reproducible input is not a proof step.

## Keep it a proof paper, not an experiment paper

- Supporting computation **certifies a step**; it does not *replace* the theorem. If the only evidence
  for the main claim is "it worked on our instances," the paper is experimental and belongs elsewhere.
- Do **not** add a benchmark table to a theory paper to look more complete — ICALP referees read it as
  either irrelevant or as a signal the theorem is weak.
- Running time *measured* is not running time *proved*. The contribution is the provable bound.

## Reproducibility of the computational part

If computation backs a proof, treat it like the full version (see `icalp-reproducibility`):

- Provide the **code and inputs** (or precise pseudocode) in the appendix / full version or a public
  repository referenced at camera-ready.
- Provide **certificates** an independent checker can verify where the technique allows.
- Pin versions (solver, seed if randomized search) so the check is deterministic.

## Worked vignette: a dichotomy with a computer-checked base

A Track B paper proves a dichotomy over a family of constraint languages: tractable vs NP-hard. The
inductive step is by hand; the base cases (finitely many small languages) are verified by an exhaustive
program. To meet the bar: state the finite base set precisely, describe the enumeration, ship the code
and its output in the full version, and — for the hardness base cases — include reductions a referee can
check by hand rather than leaving them to the program alone. State clearly which cases are
machine-verified and which are proved analytically.

## Output format

```text
[Claim shape] upper / approximation / lower (uncond) / lower (conditional) / decidability / dichotomy
[Argument fit] the proof strategy matches the claim? gaps: <where>
[Computation role] none / base-case check / solver-certified step / computer-assisted cases
[Checkability] certificate or reproducible input provided? independent check possible? yes/no
[Not-an-experiment guard] is the theorem the evidence (not benchmark performance)? yes/no
[Fix queue] <ordered: proof gaps, missing certificates, mis-routed empirical framing>
```
