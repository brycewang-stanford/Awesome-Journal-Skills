---
name: focs-supplementary
description: Use when architecting everything after page ten of a FOCS (IEEE Symposium on Foundations of Computer Science) submission — a venue with no separate supplement channel where the paper itself continues past the guaranteed-read window — covering body organization, proof placement, and navigation for the discretionary reader.
---

# FOCS Supplementary

FOCS has no supplementary-material upload, no appendix size cap, and no
separate supplement deadline: the submission is one PDF, the CFP encourages it
to be the full version, and everything beyond the abstract, references, and
first ten pages is read at the committee's discretion (2026 CFP, checked
2026-07-08). "Supplementary material" at this venue therefore means *the rest
of your own paper* — pages eleven onward — and the design question is how to
serve two readers at once: the committee member who stops at page ten, and
the assigned expert who reads to the end.

## The two-reader contract

| Reader | What they read | What pages 11+ must give them |
|---|---|---|
| Breadth reviewer (any PC member) | Window only | Nothing — the window must be self-sufficient; pages 11+ may not carry any *claim* absent from it |
| Depth reviewer / subreferee | Window, then targeted dives | Fast navigation from each windowed statement to its complete proof, with no re-derivation required |
| Post-acceptance community | The public full version | The same body, now the record of correctness for a decade |

The contract's first clause is the one authors break: introducing a new
result, a stronger bound, or a hidden assumption after page ten. Discretionary
pages can *prove* anything, but may *announce* nothing.

## Organizing the discretionary body

A structure that has served full-version submissions well:

```latex
% pages 1-10: intro, overview, formal statements (focs-writing-style)
\section{Preliminaries}                 % p.11+: full notation, standard facts
\section{Proof of Theorem 1}            % one top-level section per result
  \subsection{The key lemma}            % mirrors the overview's decomposition
  \subsection{From Lemma 3.1 to Theorem 1}
\section{Proof of Theorem 2}
\appendix
\section{Deferred calculations}         % mechanical verifications only
\section{Certificate for Lemma 4.7}     % computed-step documentation
                                        % (focs-experiments)
```

Design rules embedded there:

- **Mirror the overview.** The depth reviewer arrives holding the proof sketch
  from pages 3–6; the body's section tree should be that sketch made formal,
  in the same order with the same lemma names. A body organized differently
  from its own overview doubles refereeing work.
- **One theorem, one section.** Interleaved proofs (Lemma 6 needed by both
  Theorem 1 and 2) go in the earliest section that needs them, with a forward
  pointer from the later one.
- **Appendices are for the mechanical.** Reserve `\appendix` for calculations
  a reader could reproduce but should not have to: routine concentration
  arguments, case tables, computed certificates. A conceptually essential
  proof placed in an appendix reads as an attempt to hide its weakness.

## Pointer discipline

Every formal statement inside the window carries an explicit address for its
proof ("proved in Section 5.2"), and every body section opens by naming which
windowed statement it discharges. Concretely test the navigation: a reader
who doubts only Theorem 2 should reach its complete proof in one jump and
find it self-contained given the preliminaries — not dependent on notation
invented mid-proof of Theorem 1.

## The window boundary is a design object

Page ten's edge deserves deliberate placement. Ending the window mid-proof
wastes it; ending with the organization note leaves the breadth reader with
a map in hand. If the formal statements run long (many theorems, heavy
definitions), compress preliminaries rather than pushing statements past the
edge — a definition can be informal-plus-pointer inside the window
("(formal version: Definition 11.2)") but a theorem cannot. Check the
boundary on the compiled PDF, not the source: LaTeX pagination shifts, and
a statement that drifted to page eleven during deadline-week edits is
invisible in the diff.

## Length judgment

No cap does not mean no cost. Referees allocate finite hours per paper; a
70-page submission whose last 30 pages are routine variations taxes exactly
the reader you most need. Calibration:

- Include every proof needed for correctness — completeness is the point of
  full-version culture and reviewers penalize "details omitted" at this venue.
- Cut or fold repetitive case analyses into representative cases plus a
  stated symmetry argument, with the full enumeration in an appendix or a
  cited certificate.
- Extensions that need no new ideas ("the weighted case follows similarly")
  earn a remark, not a section — expand them later in the journal version.

## Mechanics that keep a long document navigable

- Load `cleveref` (or equivalent) so every reference states its own type —
  "Lemma 5.3" not a bare "5.3" — because the discretionary reader jumps in
  cold at arbitrary depth.
- Hyperlink everything (`hyperref` with visible-but-quiet link colors); a
  reviewer reading on screen navigates a 50-page PDF through your links or
  not at all.
- Repeat, do not paraphrase: when a body section restates its windowed
  theorem, generate the restatement with `thm-restate`
  (`focs-writing-style`) so the two are mechanically identical.
- Number *everything* that might be referenced, including remarks and
  displayed equations used later; "the displayed inequality above" fails a
  reader who arrived by hyperlink.

## Final check before upload

1. Claim audit: nothing asserted after page 10 that is not stated within it.
2. Navigation audit: window → proof in one hop for every statement.
3. Self-containment audit: each proof section readable given only the
   preliminaries and its own lemmas.
4. Anonymity audit: pages 11+ leak identity as often as page 1 — grant
   numbers in appendix headers and dataset paths in certificate listings are
   recurring offenders (`focs-submission`).
