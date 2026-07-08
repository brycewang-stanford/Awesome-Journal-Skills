---
name: stoc-reproducibility
description: Use when hardening a STOC (ACM Symposium on Theory of Computing) paper so its results can be independently checked — proof completeness across the extended-abstract/full-version split, single-source builds that prevent statement drift between the two documents, and determinism for any computation a claim relies on.
---

# STOC Reproducibility

For a proofs-only venue, "reproducible" means a third party can verify every
claimed theorem without contacting the authors. STOC's structure makes this a
**two-document problem** that pure-appendix venues do not have: the committee
reads a 12-page guaranteed window, the community reads the arXiv/ECCC full
version, and the paper is only as checkable as the *pair* is consistent. No
checklist form enforces any of this — the STOC 2026 CFP contains none (checked
2026-07-08) — so the discipline below is self-imposed or absent.

## Statement drift: the STOC-specific failure

Whenever the same theorem exists in two documents, the versions decay apart:
a hypothesis strengthened during a proof repair gets updated in one file only; a
constant improves in the full version while the abstract still advertises the old
one; numbering shifts and cross-references silently point at the wrong lemma.
Drift is not cosmetic — a reader who finds Theorem 2's statement differing
between the proceedings and arXiv cannot tell which one is proved.

The mechanical cure is a **single-source build**: one repository of statement
files included by both documents, so a statement physically cannot fork.

```latex
% statements/thm-main.tex  (the only copy of the claim, ever)
\begin{theorem}[Main; restated in the full version as Theorem~\ref{thm:main}]
\label{thm:main}
Under Assumption~\ref{ass:degree}, there is a deterministic
$O(m \log^{3} n)$-time algorithm computing a $(1+\varepsilon)$-approximate
solution for every fixed $\varepsilon > 0$.
\end{theorem}

% extended-abstract.tex          % full-version.tex
\input{statements/thm-main}      % \input{statements/thm-main}
\begin{proofsketch} ... \end{proofsketch}   % \begin{proof} ... \end{proof}
```

An `\iffull` toggle in a shared preamble achieves the same with one master file;
either way, the invariant is *one copy of every statement on disk*.

## Checkability audit before submission

| Question a verifier will ask | Passing standard |
|---|---|
| Is every claim in the first 12 pages proved somewhere I can reach? | Each theorem carries a forward pointer (appendix section or full-version anchor) |
| Do the two documents state identical theorems? | Single-source statements, or a diff run over extracted statement blocks |
| Are all hypotheses visible at the statement? | No condition introduced only inside a proof ("assume wlog the graph is connected" that is not wlog) |
| Do invoked external theorems apply? | Citation with result number, plus a line confirming your setting meets its hypotheses |
| Can the parameter trail be followed? | Constants named where they first appear; "for sufficiently large n" bounded explicitly at least once |
| Are "standard" steps actually standard? | Anything a second-year graduate student cannot fill in gets written out |

## Computation that claims depend on

If any theorem rests on a machine check (case enumeration, solver certificate,
verified numerics), reproducibility requirements sharpen from "nice" to
"load-bearing":

- Determinism: the run must be exactly repeatable — fixed enumeration order,
  no wall-clock cutoffs deciding mathematical facts, solver versions pinned.
- Independence: publish the certificate and a *separate* checker, so trust does
  not reduce to trusting your search program (see `stoc-artifact-evaluation`
  for packaging mechanics).
- Description: the paper itself must specify the computation precisely enough
  that someone could rewrite it from scratch; code is evidence, prose is the
  specification.

Illustrative-only plots and timing anecdotes carry no proof weight and need only
honesty: seed and instance disclosure, no claims beyond what is proved
(`stoc-experiments` covers when to include them at all).

## Verification workflow for the author team

1. Freeze statements four weeks out; from then on, statement edits require a
   team-visible diff, because every edit can invalidate a downstream proof.
2. Assign each theorem a verifier who did not write its proof; record
   pass/fail per proof section, and treat any "I believe it but cannot check
   line 5" as a fail.
3. Grep both documents for confessions: `wlog`, `clearly`, `standard`,
   `similar`, `it is easy to see` — each hit either survives justification or
   gets expanded.
4. Re-derive the main constant chain once, by hand, on paper, from the final
   text only. This catches the strengthened-hypothesis-updated-once bug that
   review will otherwise catch for you.
5. After camera-ready, keep the full version live-maintained: arXiv revision
   with a dated changelog is the community's accepted correction channel.

## Vignette: how drift actually happens

A team submits in November with Theorem 2 requiring subgaussian noise. In
December a reviewer-anticipating coauthor realizes the proof of Lemma 7 uses a
fourth-moment bound that subgaussianity gives but the written hypothesis does
not state; she patches the full-version draft to "subgaussian with parameter
$\sigma$" and adjusts two constants. The extended abstract is not touched —
nobody is editing a submitted file. At camera-ready in March, the proceedings
version is produced from the *submitted* sources, and the published extended
abstract now states a theorem the team knows is proved only under the amended
hypothesis. Nothing dishonest happened at any step; the pipeline had two copies
of one statement and no synchronization rule. The single-source layout above
makes this sequence structurally impossible, which is why it is worth the
Makefile friction.

## Cycle-volatility warnings

- If a future CFP introduces any structured checklist, code policy, or
  supplementary channel, it will say so; the 2026 cycle had none (待核实 yearly).
- The 12-page guaranteed window and the full-version expectation are 2026
  wording; both shape where proofs must live, so re-read the live CFP before
  restructuring.

## Output format

```text
[Checkability verdict] verifiable end-to-end / gaps found
[Statement-drift control] single-source / manual sync (risk) / diverged <- fix
[Hypothesis visibility] clean / hidden conditions at: <list>
[External results] all hypothesis-checked / unchecked: <citations>
[Load-bearing computation] none / deterministic + certified / unreproducible <- blocker
```
