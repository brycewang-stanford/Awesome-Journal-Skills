---
name: smr-derivation-and-properties
description: Use when stating assumptions, identification, and analytical properties (bias, consistency, efficiency, asymptotics, validity conditions) of a method in a Sociological Methods & Research (SMR) paper. Audits the theory and proof economy; does not design the Monte Carlo or the real-data illustration.
---

# SMR Derivation and Properties

Use this for theory integrity. SMR is a methods journal: a property that is asserted but neither
derived nor argued is the most common reviewer wound. You do not need Econometrica-level generality,
but every claim about what the method *does* must be traceable from stated assumptions.

## The traceable chain

A reader should be able to follow, in order:

1. **Target / estimand** — the population quantity or hypothesis the method addresses.
2. **Assumptions** — each one labeled by the role it plays (existence, identification, consistency,
   asymptotic normality, finite-sample approximation, computation).
3. **Estimator / statistic** — the exact object computed from data.
4. **Properties** — bias (finite-sample and asymptotic), consistency conditions, efficiency relative
   to the incumbent, the variance estimator, and the regime where it holds.
5. **Failure boundary** — where the assumptions fail and what happens to the property there.

If any link is missing, that link is what the report will quote back.

## Assumption ledger

Build this before rewriting the theory section:

```text
Assumption | Role | Where used | Empirical/sim check | If weakened
```

Use it to (a) delete decorative assumptions, (b) expose missing ones, and (c) tie each assumption to
something a sociologist can recognize in real data. SMR readers are applied methodologists: a
condition stated only for proof convenience must say whether it can be relaxed and whether the
simulation probes its boundary.

## Property claims at SMR (what reviewers expect)

- **Consistency / unbiasedness**: state the conditions, not just the conclusion. "Consistent under
  MAR and correct outcome model" is a claim; "performs well" is not.
- **Efficiency**: relative to *what*? Name the comparison estimator and the regime.
- **Inference validity**: give the variance estimator and the conditions under which its coverage is
  nominal; SMR papers routinely live or die on coverage, not point estimates.
- **Robustness**: be explicit about what the method is and is not robust to (e.g., doubly robust to
  one of two models, not to both failing).

## Proof economy for a methods-journal audience

- Keep the **main argument** legible in the body; route long algebra to an appendix, but never hide a
  load-bearing step there with only "it can be shown."
- Match the rigor to the claim: a closed-form bias correction needs a derivation; an evaluation paper
  needs a clear analytical reason the failure occurs, not a theorem for its own sake.
- Separate **theorem** (proved), **result** (derived under stated conditions), and **finding**
  (observed in simulation). Label them so a reviewer never has to guess the evidentiary status.

## Pair every property with a finite-sample check

Each analytical property should name the simulation exhibit that demonstrates it at realistic sample
sizes — SMR treats an unpaired asymptotic claim as unfinished. Hand the boundary cases to
`smr-simulation-studies` so the Monte Carlo stresses exactly the assumption most likely to fail.

## Checklist

- [ ] Estimand, assumptions, estimator, and properties are stated in that order before derivations.
- [ ] Each assumption is labeled by role and tied to a recognizable data feature.
- [ ] Consistency/efficiency/inference claims state conditions and the comparison method.
- [ ] The variance estimator and its coverage conditions are given.
- [ ] The failure boundary is stated, not hidden.
- [ ] Each property names the simulation exhibit that checks it in finite samples.
- [ ] Proved / derived / simulated claims are labeled distinctly.

## Anti-patterns

- **Asserted properties**: "our estimator is consistent and efficient" with no conditions or proof.
- **Decorative assumptions**: regularity conditions never used or never tied to data.
- **Hidden load-bearing steps**: a key derivation replaced by "it can be shown."
- **Evidence laundering**: simulation regularities phrased as theorems.
- **Coverage silence**: a new estimator with no variance estimator or coverage argument.

## Output format

```text
[Theory status] defensible / needs repair / not ready
[Estimand] <population quantity or hypothesis>
[Critical assumptions] <assumption -> role>
[Properties claimed] <bias / consistency / efficiency / coverage, with conditions>
[Property gaps] <missing condition, variance estimator, or failure boundary>
[Next SMR skill] smr-simulation-studies
```
