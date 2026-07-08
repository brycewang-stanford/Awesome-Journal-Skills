---
name: colt-topic-selection
description: Use when deciding whether a result is COLT-shaped (Conference on Learning Theory) — a theorem-first learning-theory contribution — versus better routed to ALT, STOC/FOCS, NeurIPS/ICML/AISTATS, JMLR, or a statistics journal, and whether the right vehicle is a full paper or a COLT open-problem piece.
---

# COLT Topic Selection

Use this before writing begins. COLT solicits papers on theoretical aspects of machine
learning, described in the 2026 CFP (checked 2026-07-08) as a subject at the
intersection of computer science, statistics, and applied mathematics, with an
explicitly inclusive view that includes theory shedding light on empirical phenomena.
The practical bar: the contribution must be a theorem — a rate, a separation, a
characterization, a hardness result, or an algorithm whose guarantee is the point.

## The three-question fit test

1. **Is the headline sentence a mathematical statement?** "We prove the first
   $O(\sqrt{T})$ regret bound for X" is COLT-shaped. "We propose a method that
   empirically improves X" is not, regardless of how much analysis decorates it.
2. **Would a learning theorist care before seeing experiments?** COLT reviewers
   evaluate the result on the model's motivation and the bound's strength alone.
3. **Does the proof carry the weight?** If the technique is assembly of known parts,
   the result must be strong enough to stand without technique credit; if the result
   is modest, the technique must be the contribution — one of the two must be true.

## Routing table

| Signal in the project | Best venue reading |
|---|---|
| Regret/sample-complexity/oracle-complexity bound, new or improved rate | Core COLT |
| Matching lower bound via a new instance construction | Core COLT |
| Theory explaining a deep-learning phenomenon, theorem-first | COLT (in-scope by the CFP's inclusive view) or ML-conference theory track |
| Learning theory with a long, self-contained development (60+ pages of ideas, not just proofs) | JMLR or Annals of Statistics — journal-length exposition |
| Algorithmic result where combinatorial/complexity machinery dominates the learning content | STOC / FOCS / SODA |
| Learning theory, but the community fit is the smaller algorithmic-learning-theory circuit | ALT (sister venue, autumn deadline cycle — verify) |
| Theorems plus substantial experiments as co-equal evidence | AISTATS or NeurIPS/ICML |
| Statistical methodology with inference guarantees and applied audience | AISTATS or a statistics journal |
| Probabilistic/Bayesian modeling contribution, uncertainty-first | UAI |
| A precise, motivated question you cannot answer | COLT Open Problem piece (see below) |

## The open-problem vehicle

COLT has a tradition of publishing short open-problem pieces in its proceedings —
citable, reviewed, and historically influential (verified instance: Agarwal,
Krishnamurthy, Langford, Luo & Schapire, "Open Problem: First-Order Regret Bounds for
Contextual Bandits," COLT 2017, PMLR v65:4-7; several such problems have been resolved
by later full papers). In the 2025 cycle the format was: at most 4 pages excluding
references, title beginning "Open Problem:", non-anonymous, submitted via CMT on its
own timeline. Whether and how the track runs in your cycle: 待核实 in the current CFP.

Choose the open-problem route when you can state the question with full formality,
prove the easy directions, explain why standard techniques fail, and ideally attach a
modest prize of honor (tradition, not requirement). It converts a stalled project into
community agenda-setting.

## Scope self-interrogation

```text
Q1. State the main claim as: quantifier prefix + model + bound/separation.
    -> Cannot? The project is not yet a COLT project; it is a research direction.
Q2. Name the nearest prior theorem and your delta type
    (gap-closing / log-removal / assumption-weakening / new-model separation).
    -> No nameable neighbor? Either the model is unmotivated or the search
       is incomplete -- both are pre-writing problems.
Q3. Is every experiment you are planning deletable without weakening the claim?
    -> If deleting them guts the paper, route to AISTATS/NeurIPS/ICML instead.
Q4. Will the proof survive a hostile expert with unlimited appendix access?
    -> "Probably" means the verification pass comes before the venue decision.
```

## Vignette: three fates for one project

A team analyzes gradient descent on a two-layer network and can prove convergence to
a global minimum under an over-parameterization condition.

- **As stands — plausible COLT:** the headline is a theorem about a practical
  algorithm, in-scope under the CFP's "theory that sheds light on empirical
  phenomena." The COLT version leads with the convergence rate, the
  over-parameterization threshold, and the technique that beats prior NTK-style
  arguments; the experiment section shrinks to one illustrative training curve.
- **Weakened theory, strong benchmarks — misroute:** if the honest version needs
  assumptions no practical network meets *and* the interesting content is empirical,
  the NeurIPS/ICML framing (empirical contribution, theory as support) is both more
  honest and more likely to succeed.
- **Question sharpened, proof missing — open problem:** if the threshold conjecture
  resists proof but can be stated exactly, a COLT open-problem piece stating the
  conjecture, the partial results, and why current techniques fail converts the
  stall into a citable contribution.

## Common misroutes seen at COLT

- The "theory-flavored systems paper": an algorithm with a convergence guarantee
  under assumptions the target application violates, pitched as theory. Reviewers ask
  what the theorem teaches; have an answer that is not the benchmark table.
- The "known result in new clothes": a bound classical in sequential analysis or
  empirical-process theory, rediscovered. The statistics lane of `colt-related-work`
  exists to catch this before a reviewer does.
- The "journal paper in a 12-page costume": a development whose value is the full
  landscape, mutilated to fit. If the body cannot carry the spine (see
  `colt-writing-style`), choose JMLR.
- The "two-community orphan": too applied for COLT, too theoretical for an applied
  venue. Usually a framing failure — pick the community whose open question you
  actually answer and write for it alone.

## Timing considerations

- COLT's single annual deadline (February 4, 2026 for the 39th edition) sits between
  the autumn ML-conference cluster and summer; a NeurIPS reject in September leaves
  comfortable repair time, an ICML reject usually does not — plan the cascade.
- ALT and COLT deadlines are roughly anti-phased, making ALT the natural same-community
  fallback; verify the current ALT cycle before promising the team.

## Cycle-volatility warnings

- Scope emphasis and the topics list are re-issued every cycle; the intersection
  framing above is the 2026 wording (待核实 later).
- Open-problem track existence, format, and deadline: current CFP only.

## Output format

```text
[Fit] core COLT / plausible COLT / misroute
[Headline claim] <quantifiers + model + bound/separation, one line>
[Delta type] <vs. nearest prior theorem>
[Alternative vehicle] full paper / open-problem piece / ALT / JMLR / AISTATS / STOC-FOCS
[Pre-writing blocker] <verification, motivation, or search gap to close first>
```
