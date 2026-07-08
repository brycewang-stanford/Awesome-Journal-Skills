---
name: colt-writing-style
description: Use when revising a COLT (Conference on Learning Theory) paper for theorem-first exposition — formal setup before results, informal-then-formal theorem statements, proof overviews that sell the technique, quantifier and constant hygiene, and fitting the argument's spine into 12 PMLR-formatted pages.
---

# COLT Writing Style

Use this when revising prose and mathematics for COLT. The style target is a paper a
learning theorist can referee efficiently: the model is unambiguous by page 3, the
main theorem is quotable in one breath, and the proof overview convinces the reader
the technique is new before the appendix is opened.

## The COLT first-pages arc

1. **Problem in the field's own vocabulary** — regret, sample complexity, minimax
   risk, oracle complexity, mistake bound — within the first paragraphs.
2. **What was known**: the best prior upper and lower bounds, with citations, ideally
   as an inline mini-table when three or more results interact.
3. **The new result, informally**: "we close this gap up to log factors" /
   "we show the two models are not equivalent" — one sentence, no notation debt.
4. **The formal setup**: complete model, protocol, and assumptions, before any formal
   theorem. COLT readers refuse theorems whose objects are undefined.
5. **Main theorems, then the technique paragraph**: what the proof does that prior
   arguments could not, named honestly (a new potential function, a reduction, a
   coupling, a lower-bound instance family).

## Informal/formal pairing

State important results twice — an informal version in the introduction and the formal
version after the setup — and keep them visibly consistent:

```latex
% Introduction:
\begin{theorem}[informal; see Theorem~\ref{thm:main}]
Any proper learner needs $\Omega(d/\epsilon)$ samples in this model,
and an improper learner achieves $O(\log(d)/\epsilon)$.
\end{theorem}

% After the setup:
\begin{theorem}\label{thm:main}
Let $\mathcal{H}$ satisfy Assumption~\ref{ass:vc}. For every proper learner $A$
there is a distribution $D$ with ... . Moreover, Algorithm~\ref{alg:improper}
outputs $h$ with $\mathrm{err}_D(h) \le \epsilon$ using
$m = O(\epsilon^{-1}\log d)$ samples, with probability $1-\delta$.
\end{theorem}
```

The informal statement is a promise; reviewers check that the formal statement redeems
it without weasel adjustments (an extra assumption appearing only in the formal
version is a credibility leak).

## Sentence-level repairs

| Draft habit | COLT-grade replacement |
|---|---|
| "It is easy to see that..." | "By Jensen's inequality applied to (7)," — name the tool |
| "For simplicity assume..." (silently binding) | "Assumption 3 (stated formally in Section 2); we discuss removing it in Remark 4" |
| "significantly improves prior work" | "improves the dependence on $d$ from $d^2$ to $d\log d$ (Table 1)" |
| "standard concentration arguments give" | "Bernstein's inequality with variance bound (12) gives" |
| "we believe the bound is tight" | "we conjecture the $\log$ factor is necessary; Section 5 gives partial evidence" |
| "our novel technique" | Describe the technique; let the reviewer call it novel |

## Quantifier and constant hygiene

- Every theorem fixes its quantifier order explicitly: for all horizons, there exists
  an algorithm — or the reverse. Half of "counterexamples" reviewers report are
  quantifier misreadings the author invited.
- High-probability versus expectation must be declared in the statement, with the
  δ-dependence visible if the bound carries one.
- Absolute constants may be absorbed into O(·); problem parameters (d, K, horizon,
  condition numbers, norm bounds) may not, unless the notation section says which
  parameters O(·) is allowed to hide — and then it must obey its own declaration.
- Lower bounds state the instance family; "there is a hard distribution" without its
  construction location reads as unfinished.

## Budgeting 12 pages

The 2026 CFP allowed 12 PMLR-formatted body pages (references and appendix free,
checked 2026-07-08). A working allocation for a two-theorem paper:

- 1.5 pages: introduction with the known-vs-new table.
- 1 page: related work (compressed to contrasts; full survey in the appendix).
- 2 pages: setup and definitions — resist compressing this below completeness.
- 2.5 pages: main results with remarks and consequences.
- 4 pages: proof overviews and key lemmas — the section that wins the paper.
- 1 page: discussion, open questions (COLT culture rewards honest open questions),
  and the illustration figure if one exists.

If the spine does not fit, cut a secondary theorem to the appendix wholesale rather
than thinning every proof overview into mush.

## Abstract formula

Five sentences carry a COLT abstract: (1) the model and the question, in field
vocabulary; (2) the best known bounds; (3) your result with explicit rates or the
separation named; (4) the technique in one clause; (5) an optional consequence or
open question. Numbers belong in the abstract at this venue — an abstract without a
rate reads as an abstract without a result. Delete from drafts: application
motivation beyond one clause, "extensive experiments," and any sentence beginning
"Recently, there has been growing interest."

## Tone and culture notes

- First person plural, plain declarative sentences, no marketing register. "We prove"
  outranks "we are excited to present."
- Name predecessors generously and precisely; the community is small and the referee
  may be one of them.
- Remarks after theorems are for interpretation and sharpness discussion; new claims
  hiding in remarks must be flagged proved/unproved.
- British/American spelling is unregulated; consistency is the rule that exists.

## Anonymity phrasing

Write self-references in third person ("extending the reduction of [14]") and strip
acknowledgements for review — the 2026 template's `anon` option handles the author
block, but prose leaks are on you. See `colt-submission` for the full sweep.

## Output format

```text
[Style verdict] referee-efficient / setup-deficient / overclaimed / disorganized
[First-pages arc] <which of the five steps is missing or out of order>
[Statement hygiene] <quantifier / constant / probability-mode fixes>
[Technique paragraph] present and honest / absent / vague
[12-page plan] <sections over budget and the cut>
```
