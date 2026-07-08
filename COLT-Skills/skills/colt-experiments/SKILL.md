---
name: colt-experiments
description: Use when deciding whether a COLT (Conference on Learning Theory) paper needs numerical content at all — COLT has no experiments requirement — and, when numerics genuinely help, designing small illustrative simulations that visualize a proved bound, a separation, or a phase transition without diluting the theory.
---

# COLT Experiments

Start from the venue truth: **COLT imposes no experiments requirement, and most COLT
papers contain no experiments.** The 2026 CFP (checked 2026-07-08) asks for
theoretical machine-learning contributions and mentions no empirical-evaluation
expectation; papers are accepted on theorems. The decision this skill supports is
therefore *whether* to include numerics, and only then *how*.

## Should this paper contain numerics at all?

| Situation | Include numerics? | Rationale |
|---|---|---|
| Clean upper/lower bound pair, standard model | No | Plots add length, not belief |
| New algorithm whose practicality is part of the pitch | Small illustration | Shows the constants are not absurd |
| Theory explaining an empirical phenomenon (in-scope per the CFP's inclusive view) | Yes, essential | The phenomenon must be exhibited, then explained |
| Conjectured tightness you cannot prove | Careful, labeled | A scaling plot can support a conjecture — never upgrade it |
| Phase transition / separation between models | Often worthwhile | A picture of the transition is the most readable evidence |
| Purely structural result (equivalences, characterizations) | No | Nothing to simulate |

If the answer is no, spend the pages on proof overviews instead; a decorative
benchmark table in a COLT submission signals venue confusion and can *lower* reviewer
confidence.

## Design rules when numerics earn their place

- Simulate the theorem's exact regime: the assumptions, the adversary, the parameter
  ranges. An illustration outside the proved regime must be labeled exploratory.
- Prefer synthetic constructions where ground truth is computable; COLT illustrations
  are about visualizing mathematics, not about datasets.
- Overlay the proved bound on the empirical curve so the reader sees slope agreement,
  constant gap, and where finite-size effects fade.
- Report the estimator of variability (bars = standard error over R runs, stated in
  the caption), fixed seeds, and replication counts — theorists distrust single
  trajectories on principle.
- Keep total numerical content to roughly a figure or two; the appendix holds the
  procedure description (no code-upload channel existed in the 2026 cycle).

## A rate-illustration recipe

The canonical COLT figure is a log-log rate check — empirical error or regret against
the driving parameter, with the theoretical slope for reference:

```python
import numpy as np

rng = np.random.default_rng(seed=2026)          # fixed, reported seed
ns, R = np.logspace(2, 5, 8).astype(int), 50    # sample sizes, replications

emp = np.array([[run_once(n, rng) for _ in range(R)] for n in ns])
mean, se = emp.mean(axis=1), emp.std(axis=1, ddof=1) / np.sqrt(R)

slope = np.polyfit(np.log(ns), np.log(mean), 1)[0]
print(f"fitted slope {slope:.3f} vs. theoretical -1/2")
# plot log-log with se bars; overlay C * n**(-0.5) reference line
```

The caption must state: the model matches Assumptions 1-2, R = 50 replications, bars
are ±1 standard error, and the reference line is the Theorem 1 rate with fitted
constant. A fitted slope of −0.48 against a proved −1/2 is a persuasive picture; a
slope of −0.7 is a finding you must discuss (constants regime? bound loose? bug?)
rather than hide.

## Separation and phase-transition pictures

- For a separation between two models or algorithm classes, plot both behaviors on
  the same instance family so the divergence is visual, and print the instance-family
  parameters in the caption.
- For a threshold phenomenon (learnable iff α > α*), sweep across the threshold with
  enough resolution to show the transition sharpening as n grows — a single n is not
  a phase-transition picture.
- Adversarial constructions from lower-bound proofs often make the best instances:
  simulating your own hard instance shows it is concretely hard, not just
  asymptotically.

## Placement and captioning inside the paper

- Body placement: at most one illustration figure in the 12-page body, positioned
  next to the theorem it visualizes, never in the introduction as decoration; the
  remaining panels and the full procedure live in a terminal appendix section
  (`colt-supplementary` keeps numerics out of the proof flow).
- A COLT-grade caption is self-sufficient: instance family and parameters, the
  assumptions regime, replication count, what the bars are, what the reference line
  is, and the one-clause takeaway ("empirical slope matches the Theorem 1 rate").
- In-text discussion of the figure belongs in a Remark or a short subsection titled
  for what it shows ("Illustration of the separation"), keeping the paper's logical
  skeleton purely deductive.
- If space runs out, the figure is the first cut — state the numerical finding in one
  sentence with a pointer to the appendix, and spend the recovered half page on a
  proof overview.

## Honesty rules that theorist reviewers enforce

- Never claim empirical support for regimes the theorem does not cover without the
  word "conjecture" or "exploratory" attached.
- Never tune the illustration (seeds, instances) to flatter the bound; if fluctuations
  are visible, show them.
- If the observed constants are large, say so — "the constant in Theorem 1 is
  pessimistic; empirically C ≈ 3" is a respected sentence at this venue.
- A numerical section may not compensate for a proof gap, and reviewers will not
  trade one for the other.

## Cycle-volatility warnings

- The no-experiments-expected norm is structural to COLT, but scope language and any
  code policy are re-stated each cycle in the CFP (待核实 annually).
- Reviewer appetite for numerics varies by subfield: optimization and RL-theory
  reviewers often welcome a good rate plot; pure statistical-learning reviewers
  frequently prefer the pages spent on proofs. Calibrate to your subject area.
- If your empirical component outgrows illustration into contribution, re-run venue
  selection (`colt-topic-selection`) — the paper may be drifting toward NeurIPS,
  ICML, or AISTATS.

## Output format

```text
[Numerics verdict] none needed / illustration justified / empirical core (re-route?)
[Regime match] simulation inside proved regime / exploratory (labeled?)
[Figure plan] <rate plot / separation / phase transition; caption contents>
[Statistical floor] seeds, replications, bars defined
[Honesty check] <any claim exceeding the theorems>
```
