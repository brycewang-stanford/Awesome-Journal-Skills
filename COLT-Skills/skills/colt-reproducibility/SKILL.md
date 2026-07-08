---
name: colt-reproducibility
description: Use when strengthening the reproducibility of a COLT (Conference on Learning Theory) paper, where reproducing means re-deriving — complete proofs, explicit assumptions, tracked constants, correctly invoked external results, self-contained notation — plus seeds and scripts for any numerical illustration the paper carries.
---

# COLT Reproducibility

At COLT, reproducibility means a competent reader can *re-derive* every claim from the
PDF alone. There is no reproducibility checklist form in the COLT 2026 CFP (checked
2026-07-08) — the venue enforces the property the hard way, through referees who
attempt the re-derivation during review. This skill is the pre-submission audit that
makes that attempt succeed.

## The re-derivability standard

A theorem is reproducible when all of the following hold:

- Its statement is formally complete: every symbol quantified, every assumption named
  in the statement itself or cited by an explicit assumption label, the probability
  space and adversary model unambiguous.
- Its proof exists in full inside the submitted PDF — COLT's unlimited appendix
  removes every excuse for "omitted for lack of space."
- Each proof step is locally checkable: an expert reading line k needs only lines
  1..k-1, cited external results, and standard background — never your unpublished
  intuition.
- Constants and parameter regimes survive the chain: if Theorem 1 needs
  n ≥ C·d·log(1/δ), the reader can trace what C is or where it was declared absolute.

## Audit table: where re-derivation fails

| Failure mode | Typical symptom in the PDF | Repair |
|---|---|---|
| Hypothesis smuggling | Proof uses independence never assumed | Add the assumption to the statement, or redo the step |
| External-result misuse | "By [X], ..." where [X] needs bounded support you don't have | Check [X]'s hypotheses; find the right variant or prove a lemma |
| Constant drift | C doubles silently between two displays | Number constants (C_1, C_2, ...) and track them in a ledger |
| Case leakage | "The case d=1 is analogous" when it is not | Write the case or prove the reduction |
| Notation overload | Same symbol for a filtration and a function class | One notation table, enforced globally |
| Silent regime switch | Bound proved for T large, quoted for all T | State the threshold explicitly in the theorem |

## Assumption bookkeeping pattern

Give assumptions their own numbered environment and cite them by label everywhere:

```latex
\newtheorem{assumption}{Assumption}

\begin{assumption}[Bounded losses]\label{ass:bounded}
For all $t$, the loss $\ell_t$ maps to $[0,1]$.
\end{assumption}

\begin{theorem}\label{thm:regret}
Under Assumptions~\ref{ass:bounded} and~\ref{ass:oblivious}, the algorithm's
regret satisfies $R_T \le 4\sqrt{T \log K}$ for all $T \ge 1$.
\end{theorem}
```

The payoff is auditable dependency: a reviewer can grep which theorems rely on
obliviousness, and your rebuttal can answer "is Assumption 2 needed for Theorem 3?"
with a pointer instead of an essay.

## Numerical illustrations, when present

Some COLT papers plot a simulated regret curve or a phase transition to illustrate a
bound. The theory community's floor for those figures:

- Fixed seeds, stated replication counts, and error bars whose meaning the caption
  defines; a noisy single run "consistent with the theory" persuades no one here.
- The simulated regime must be the theorem's regime — matching horizon, dimension, and
  noise assumptions — or the mismatch must be acknowledged as exploratory.
- The generating script should be one dependency-light file, releasable after
  acceptance; during review, describe the procedure precisely in the appendix since no
  upload channel exists.
- Never let an illustration silently extend the claim ("the bound appears to hold for
  heavy tails too") without labeling it as conjecture.

## Vignette: the spine of a lower-bound paper

Consider a submission whose main result is a $\Omega(\sqrt{TK})$ lower bound via a
new instance family. Its re-derivability spine, in the order a referee will attack it:

- the instance family's construction, with every distribution parameter explicit and
  the randomization protocol (oblivious vs. adaptive) named;
- the information-theoretic step (say, a KL-divergence calculation) with the exact
  divergence bound displayed, not cited as "standard";
- the reduction from learner performance to the divergence quantity, where hypothesis
  smuggling most often hides (does the argument secretly assume deterministic
  learners? say so or generalize);
- the final optimization over instance parameters, with the maximizing choice written
  out — "choosing ε appropriately" is where constants go to die.

A referee who can walk this spine without leaving the PDF marks correctness resolved;
each externalized step converts into a review question, and three review questions
into a reject.

## Pre-submission re-derivation drill

1. Print the numbered-statement list (all definitions, assumptions, lemmas, theorems).
2. For each, a non-author coauthor answers: can I state precisely what this claims,
   including quantifiers, without reading the proof? Rewrite until yes.
3. Verify proofs in dependency order, marking each line verified/unverified; the
   `colt-artifact-evaluation` skill's ledger format works here.
4. Re-check every external citation against the cited source's actual hypotheses —
   allocate real time; this is where careful papers die.
5. Reconcile body sketches against appendix proofs: a sketch that describes an older
   proof strategy than the appendix executes reads as a gap to a referee.

## Cycle-volatility warnings

- If a future COLT cycle adds any checklist, code policy, or supplementary channel,
  the current CFP announces it; the 2026 cycle had none (待核实 in later cycles).
- The 12-page body and single-PDF rules that shape where proofs live are the 2026
  formulation; re-read the live CFP before restructuring a paper around them.
- Formatting of assumptions and environments is a house-style choice, not a CFP rule;
  the CFP-level constraints remain the 12-page body and the single PDF.

## Output format

```text
[Re-derivability verdict] re-derivable / gaps found
[Statement completeness] <theorems needing quantifier or assumption repair>
[Constant ledger] tracked / drift at <displays>
[External-results audit] <citations with unchecked hypotheses>
[Illustration floor] seeds+replications stated / absent / no numerics in paper
```
