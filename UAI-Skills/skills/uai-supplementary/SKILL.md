---
name: uai-supplementary
description: Use when splitting a UAI paper between the 8-page main part, the unlimited in-PDF appendix for proofs and protocols, and the optional 50 MB supplementary ZIP, deciding what reviewers must see in the body versus what may sit in material they are not required to read, all under double-blind and single-file constraints.
---

# UAI Supplementary

UAI's packaging model (2026 cycle, verified 2026-07-08) has three tiers with sharply
different review status. Getting content into the right tier is a strategic decision,
not a formatting chore. Reconfirm tier rules in the current submission instructions
before finalizing.

## The three tiers

| Tier | 2026 constraint | Review status | Belongs here |
|---|---|---|---|
| Main part | ≤ 8 pages, UAI template | Read by everyone, judged on all four criteria | Claims, assumptions, method, key evidence, limitations |
| Appendix | Unlimited, same PDF, after references | Part of the reviewed submission; consulted when reviewers verify | Full proofs, protocols, extra experiments, derivations |
| Supplementary ZIP | ≤ 50 MB, separate upload | Explicitly optional for reviewers | Code, data, generators, logs, checkpoints |

Two structural consequences follow. First, because the appendix travels inside the
reviewed PDF, UAI has no "the reviewers never saw my proofs" excuse — but also no mercy
for identity leaks buried on appendix page 30. Second, because the ZIP is officially
optional reading, nothing decision-critical may live only there.

## Placement heuristics

- A result whose absence would change the accept/reject argument goes in the main part,
  even as a two-line proof sketch pointing to the appendix.
- A step a skeptical reviewer must verify to trust a theorem goes in the appendix — in
  full, with the theorem restated so the appendix reads without page-flipping.
- Anything executable goes in the ZIP, plus a pointer sentence in the paper so its
  existence is on the reviewed record.
- Never cite the ZIP as evidence for a claim ("see supplementary code for the full
  results"): reviewers are entitled to ignore it, so the claim becomes unbacked.

## Appendix architecture that works here

Statisticians and probabilistic-ML researchers navigate by statement numbers. Structure
for that reading style:

- One appendix section per theorem or per experiment family, in main-text order.
- Restate every assumption with its original label (A1, A2…) before using it; an
  appendix proof invoking an unlabeled assumption is where correctness objections start.
- Give experimental appendices the same table discipline as the body: full
  hyperparameter grids, per-dataset results, per-seed dispersion.
- Cross-reference forward from the body precisely ("proof in App. B.2", not "proofs in
  the appendix").

```latex
% Single-PDF assembly, UAI style: appendix follows references in the same document
\bibliography{refs}          % references end the main part
\clearpage
\appendix
\section{Proofs for Section 3}\label{app:proofs}
\paragraph{Assumption A2 (restated).} The mixing weights are bounded away from zero.
\begin{proof}[Proof of Theorem 3]
  ... % full argument; the body kept only the sketch
\end{proof}
\section{Experimental Protocols}\label{app:protocols}
% grids, seeds, per-dataset tables, compute
```

## ZIP assembly under the 50 MB cap

- Ship generators and configs rather than bulky outputs; include checksums for anything
  regenerable.
- Structure by claim, not by code module: a reviewer looks for `figure2/`, not for
  `src/utils/`.
- Keep the archive as anonymous as the PDF: no `.git` history, no notebook author
  metadata, no cluster paths, no account-bound experiment-tracker URLs.
- Test the unzip-and-run path on a clean machine; a broken optional artifact is worse
  than no artifact, because it documents carelessness.

## Pre-merge integrity checklist

Run after the last content edit, before assembling the final PDF:

- [ ] Every theorem/lemma/proposition statement in the body is character-identical to
      its restatement in the appendix (diff them mechanically, not by eye).
- [ ] Every assumption label used in an appendix proof is defined in the body.
- [ ] Every "App. X.Y" reference in the body resolves to an existing section after
      the latest appendix reshuffle.
- [ ] Appendix figures and tables are numbered in a scheme that cannot collide with
      the body's (e.g., Table 7 vs Table A.3 — pick one convention).
- [ ] No appendix section silently introduces a claim absent from the body; reviewers
      may treat body-less claims as unreviewable.
- [ ] The references section sits between main part and appendix per the current
      template's convention.
- [ ] Page count of the main part re-verified **after** the merge; late appendix
      edits sometimes push floats forward into page 8.
- [ ] The ZIP's README points into the appendix ("protocol details in App. C") and
      not vice versa for anything decision-critical.

## Budgeting the 50 MB

A workable allocation when the archive is tight: code and configs are effectively
free (rarely over 5 MB); reserve the bulk for whichever single item most de-risks
your weakest claim — a gold-standard posterior sample set, a preprocessed data
extract with checksums, or trained-model files for the headline table. Everything
else ships as a generator script plus a hash of its output. If two heavyweight items
compete, keep the one a reviewer cannot regenerate in minutes.

## Failure patterns seen at single-PDF venues

- Overflow laundering: pushing the method description itself into the appendix to make
  the 8-page cap. Reviewers score clarity on the main part; an unintelligible body with
  a beautiful appendix fails.
- Appendix drift: editing a theorem in the body during deadline week without touching
  its appendix proof. Diff statement text mechanically before upload.
- Reference squeeze: trimming citations to save space, forgetting references are outside
  the 8-page cap and cost nothing.
- ZIP-only ablations: the reviewer asks "why no ablation?" and the answer "it was in the
  ZIP" wins no points, because the rules told them they could skip it.

## Output format

```text
[Tier map] main <pages> / appendix <pages> / ZIP <MB>
[Misplaced content] <items in the wrong tier, with target tier>
[Appendix integrity] statements match body? assumptions labeled?
[ZIP status] runs clean? anonymous? claim-indexed?
[Pointer sentences] <paper locations announcing appendix and ZIP contents>
```
