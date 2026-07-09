---
name: itcs-experiments
description: Use when deciding what counts as evidence for an ITCS theory claim — proofs as the primary evidence, worked examples and separations that make a model concrete, and the rare, well-scoped illustrative computation or simulation — and how to keep any computational content checkable and subordinate to the mathematics.
---

# ITCS Experiments

ITCS is a **pure-theory** venue: the primary — usually the only — evidence for a claim is a
**proof**. There is no experiments requirement, no benchmark, no leaderboard, and no reviewer
expectation of an empirical section. Bringing an ML-conference or SE reflex here (a table of
numbers "showing" the method works) misreads the venue: at ITCS a theorem is proved, not
measured. This skill is about matching **evidence to a theory claim** and about the *rare* case
where a small computation genuinely helps.

## Proofs are the evidence

- **Every central claim is settled by a complete proof**, not by examples. A pattern that "holds
  in all cases we tried" is a conjecture, not a theorem — label it as such and prove or drop it.
- **Match the claim shape to the argument shape:** an upper bound needs a construction + analysis;
  a lower bound needs an adversary/reduction; a separation needs a witness object; an
  impossibility needs a contradiction from the assumption. Reviewers check that the *kind* of
  argument fits the *kind* of claim.
- **A new model needs an anchoring result** (see
  [`itcs-writing-style`](../itcs-writing-style/SKILL.md)) — a separation or a surprising
  possibility that proves the model is neither empty nor everything. That anchoring result *is*
  the "experiment" an ITCS PC wants: evidence the model is alive.

## Worked examples and separations as evidence

Non-proof evidence that *is* welcome, because it makes the mathematics concrete:

- **Worked examples** that instantiate a definition on a small case and show the intended
  behavior — invaluable for a new model, and cheap insurance against the "is this trivial?"
  objection.
- **Explicit separating objects** — a small graph, code, distribution, or gadget that witnesses a
  gap between two settings. If finite, *include the object* so a reviewer verifies the separation
  directly.
- **Tight-example constructions** showing an analysis cannot be improved — the theory analogue of
  an ablation, demonstrating the bound is not loose by accident.

## The rare, well-scoped computation

Some ITCS papers include a *small* computational component: a computer search that found a
gadget, a SAT/SMT solve certifying a finite separation, a numerically evaluated construction.
When one genuinely helps, scope it tightly:

- **It supports a proved claim; it is never the claim.** "A search over all graphs on <= 12
  vertices found the gadget of Lemma 4, whose properties we then prove" is legitimate. "Our
  method achieves 92% on a benchmark" is a category error at ITCS.
- **Make it checkable without rerunning.** State the exact search space, the tool and version, and
  — crucially — **include the finite object** the search produced (the graph, certificate, code)
  so verification is a static check, not a re-computation. A reviewer should be able to confirm
  the object has the claimed property by hand or with a one-line check.
- **Report it honestly.** If a construction is only verified numerically (not proved), say so and
  mark exactly which claims rest on computation versus proof.
- **Keep it off the anonymity leak surface.** A linked repository under a personal GitHub is a
  lightweight-double-blind slip; fold the object into an appendix or host it neutrally (see
  [`itcs-submission`](../itcs-submission/SKILL.md)).

## What NOT to import from empirical venues

| Empirical-venue habit | Why it misfires at ITCS |
|---|---|
| A benchmark table as the main result | ITCS proves; it does not measure. A table cannot establish a theorem |
| "Outperforms baselines by X%" framing | There are no baselines to beat; the contribution is an idea/proof |
| Runtime plots to argue efficiency | State and prove the asymptotic bound instead |
| An artifact/reproducibility package of code | No artifact track exists; the "artifact" is the proof (see itcs-artifact-evaluation) |
| Statistical significance / error bars | Irrelevant to a deterministic mathematical claim |

## Decision procedure

```text
[Claim] is it a theorem (prove it) or a pattern (label as conjecture, or prove/drop)?
[Argument fit] upper=construction+analysis / lower=adversary / separation=witness / impossibility=contradiction
[Alive] new model? -> anchoring separation or surprising-possibility result present?
[Compute?] does a small search/solve genuinely help a proved claim? if not, omit it
[Checkable] if compute used: search space + tool/version stated, finite object included?
[Honesty] each claim tagged proved vs. numerically-verified; anonymity leak surface clean?
```

## Output format

```text
[ITCS evidence status] proof-complete / gaps / mis-imported-empirics
[Central claims] each has a complete proof of matching shape? yes/no + list gaps
[Model alive] anchoring result present for any new model? yes/no
[Computation] present? if so: supports-a-proof only? checkable object included?
[Anonymity] no personal-repo leak from any computational content? yes/no
[Fix queue] <ordered edits>
```
