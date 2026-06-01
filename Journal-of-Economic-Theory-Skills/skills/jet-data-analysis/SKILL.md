---
name: jet-data-analysis
description: Handle any numerical, computational, or empirical content in a Journal of Economic Theory (JET) paper — JET is theory-first, so numerical examples, simulations, and computed equilibria are admitted only as illustration or test of a theoretical result, must stay subordinate to the theorem, and should be reproducible. Light by design for a theory journal.
---

# Numerical & Computational Content (jet-data-analysis)

## When to trigger

- Your theory paper includes a worked numerical example, a simulation, a computed equilibrium, or
  (rarely) empirical/experimental evidence
- You want to know how much computational content JET will accept and how to present it
- You need to keep a computation from overshadowing the theorem

## The JET rule: theory-first, computation subordinate

JET publishes **rigorous, original theoretical results**. Empirical, experimental, quantitative, and
computational work is welcome **only when firmly grounded in theory** — i.e., as the **illustration or
test of a theoretical contribution that is itself the paper's point**, never as a stand-alone empirical
or computational paper. This skill is deliberately **light**: most JET papers are pure theory, so the
default is *minimal* numerical content.

## How to present numerical content

- **Make it serve the theorem.** A numerical example should make an assumption bite, exhibit the
  characterized object, or show tightness of a bound — not stand alone as a finding.
- **Keep examples small and transparent.** A 2x2 game, a two-type screening problem, or a three-agent
  matching market usually communicates more than a large simulation.
- **Use computation to probe necessity.** A computed **counterexample** is the cleanest way to show an
  assumption cannot be dropped (feeds jet-identification-strategy and jet-rebuttal).
- **Reproducibility.** Provide a small self-contained script (SymPy/`numpy`/`scipy`, Julia, MATLAB/Octave)
  that regenerates every reported number and figure; pin versions and **set/report seeds** for anything
  stochastic. Sharing is **encouraged, not required** (see jet-replication-and-data-policy).
- **If genuinely empirical/experimental:** state the theoretical prediction first, then test it; the
  prediction is the contribution.

## Anti-patterns

- A large simulation presented as the result, with theory as decoration (off-fit for JET)
- A numerical figure whose underlying values cannot be reproduced
- Calibration/estimation with no theorem behind it (send elsewhere)
- Stochastic illustration with no seed reported

## Output format

```
【Content type】worked example | simulation | computed equilibrium | empirical test | none
【Role】illustrates / tests / counterexample to <theorem/assumption>
【Subordinate to theory?】[Y/N]  ← must be Y for JET
【Reproducible】script + pinned env + seed? [Y/N]
【Next】jet-tables-figures / jet-replication-and-data-policy
```
