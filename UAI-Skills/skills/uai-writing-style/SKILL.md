---
name: uai-writing-style
description: Use when revising a UAI manuscript for probabilistic-inference readers, enforcing precise notation for distributions, graphs, and interventions, explicit assumption and identifiability statements, an 8-page main part that carries the whole argument while proofs sit in the appendix, and claims calibrated to what the theory and experiments show.
---

# UAI Writing Style

Use this during revision. The UAI readership lives on probabilistic reasoning, graphical
models, causality, and Bayesian methods, and the posted review criteria end with
"clarity of writing" as a first-class axis. At this venue clarity is mostly a formal
property: whether every symbol, assumption, and probability statement means exactly one
thing.

## Notation is the first review

Probabilistic papers die by notation drift more than by grammar. Enforce a single
notational regime before polishing sentences:

- One symbol per object: if `p` is a density, do not let it moonlight as a probability
  mass function and a marginal without saying so.
- Distinguish conditioning from intervention typographically everywhere:
  `p(y | x)` versus `p(y | do(x))`; a causality paper that blurs this once loses its
  causal readers.
- Declare graph notation on first use — nodes, parents `pa(V)`, whether graphs are
  DAGs, MAGs, or CPDAGs — and never switch mid-paper.
- Fix measure-theoretic hygiene where it matters (densities exist with respect to
  what?), and say nothing about it where it does not; ostentatious rigor on trivialities
  reads as inexperience.

```latex
% Preamble discipline: define once, use everywhere
\newcommand{\E}{\mathbb{E}}
\newcommand{\indep}{\perp\!\!\!\perp}          % conditional independence
\newcommand{\do}[1]{\mathrm{do}(#1)}           % interventions, always \do{x}
\newtheorem{assumption}{Assumption}            % A1, A2... citable by label
% Every theorem names its assumptions explicitly:
% \begin{theorem}[Identifiability]\label{thm:id}
%   Under Assumptions~\ref{a:faithful} and \ref{a:positivity}, ...
```

## Assumptions carry the argument

- Give each assumption a number and a name, state it once, and cite it by label inside
  every result that uses it. UAI reviewers audit which assumption powers which theorem;
  make that audit trivially easy.
- Say early which assumptions are standard, which are novel, and which are restrictive —
  and for the restrictive ones, what breaks without them. Preempting "A3 is strong" in
  the text is worth a rebuttal round.
- Identifiability claims deserve their own sentence structure: what is identified, from
  what observational or interventional regime, under which assumptions. Compressed
  versions of that sentence become wrong versions.

## The 8-page main part as an argument spine

With unlimited appendices in the same PDF, the 8 pages are pure argument budget. Spend
them so a reviewer can reach a verdict on correctness, novelty, and backing without
opening the appendix — and needs the appendix only to verify:

- Page 1 states the inference problem, why existing treatment of uncertainty fails, the
  contribution, and the strongest guarantee or empirical finding.
- Every theorem in the body gets a proof sketch conveying the mechanism; the appendix
  holds the full argument.
- Every experimental claim in the body gets its central table or figure; per-dataset
  breakdowns move back.
- Related work earns its space by sharpening the delta, not by demonstrating erudition.

## Calibrated prose

A venue about uncertainty notices overconfident language immediately.

| Overclaimed | Calibrated for UAI |
|---|---|
| "Our method outperforms all baselines" | "Improves over X and Y on 5 of 6 datasets (mean ± sd over 10 seeds); ties on Z" |
| "The posterior is accurate" | "R-hat ≤ 1.01 on all parameters; ESS > 400 per chain" |
| "Our intervals are well calibrated" | "Empirical coverage 89.3% ± 0.8 at nominal 90%" |
| "Works for any graphical model" | "Applies to discrete pairwise MRFs; extensions in App. E" |
| "First to study X" | "To our knowledge, the first identifiability result for X under A1–A2" |

Symmetrically, do not under-claim guarantees you actually prove — "may help in some
settings" wastes a theorem.

## First-page arc, checkable

The opening page should let a bidding reviewer and a skimming AC reconstruct the paper.
Verify each element exists and appears in roughly this order:

- [ ] The inference problem, stated as a probabilistic question (what is unknown,
      what is observed, what regime).
- [ ] Why current uncertainty handling fails — named per method family, not "prior
      work has limitations".
- [ ] The contribution as an object: estimator, bound, graph class, algorithm,
      identification condition.
- [ ] The attached guarantee or diagnostic, with its key assumption named inline.
- [ ] One headline number or theorem pointer a reader could verify later.
- [ ] Vocabulary matching the CFP's topic list, so bidding routes correctly.
- [ ] Nothing on page 1 that the appendix cannot back.

## Sentence-level habits for this audience

- Lead paragraphs with the probabilistic object ("The posterior over structures...", not
  "It can be seen that...").
- Keep inline math out of load-bearing sentences where a display would let the reader
  check indices.
- Write the abstract as: problem, gap in uncertainty handling, method or result,
  guarantee or diagnostic, headline evidence. UAI abstracts also drive reviewer bidding,
  so name the model class and the contribution type explicitly.
- Anonymize style too: distinctive lab phrasing plus first-person history ("in previous
  work we showed") undermines double-blind review.

## Titles that route correctly

UAI titles are unusually literal, and bidding rewards that: name the object and the
regime ("Identifiability of X under Y", "Unbiased Z estimation via W") rather than
branding a system name. A memorable acronym can ride along after a colon, but the
pre-colon half should let a reviewer decide "mine" or "not mine" in one read. Avoid
question titles and avoid claiming words ("optimal", "exact") the paper then
qualifies — at this venue the title is the first claim checked against the evidence.

## Output format

```text
[Notation audit] consistent / drift found at: <symbols, sections>
[Assumption ledger] labeled? cited-by-label in each theorem? novel ones flagged?
[Spine check] verdict reachable from 8 pages alone? weakest section: <n>
[Claim calibration] <overclaims and underclaims with suggested rewording>
[Bid signal] abstract names model class + contribution type? 
```
