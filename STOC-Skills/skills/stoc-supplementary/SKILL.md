---
name: stoc-supplementary
description: Use when architecting everything beyond the first twelve pages of a STOC (ACM Symposium on Theory of Computing) submission — the discretionary-read appendix, the reviewed table of contents, theorem-to-proof pointer discipline, and the division of labor between the submission appendix and the arXiv/ECCC full version.
---

# STOC Supplementary

STOC has no supplementary-upload channel, no ZIP, and no page cap. One PDF
carries everything, and the 2026 CFP draws the line inside that PDF: the
abstract, the **table of contents**, and the first twelve pages are read;
material beyond that is read at the committee's discretion (checked 2026-07-08).
So "supplementary material" at STOC means *the discretionary region of your own
submission* — and designing it is a first-class writing task, because reviewers
enter it selectively, through the pointers you leave.

## The table of contents is part of the supplement's interface

Uniquely among major venues, STOC names the ToC as guaranteed-read material.
Treat it as the map reviewers use to decide *which* discretionary pages to open:

```latex
\tableofcontents   % after the abstract, before Section 1
% Section titles should narrate the argument, not label boilerplate:
%   4  Reducing multi-commodity routing to tree embeddings
%   5  The potential-function analysis (proof of Theorem 1.2)
%   A  Deferred proofs from Section 4
%   B  The lower-bound construction (proof of Theorem 1.4)
%   C  Extension to weighted instances
```

A ToC whose appendix entries name the theorem each section proves lets a
reviewer verify exactly the claim they doubt. "Appendix A: Omitted proofs" is a
map with no street names.

## Placement decision table

| Content | First 12 pages | Discretionary appendix | Full version only |
|---|---|---|---|
| Every theorem/corollary statement | Required | Restated with proof | Mirror |
| Technical overview of the main proof | Required | — | Mirror |
| Complete proof of the main theorem | Idea + hardest step | Yes, in full | Yes |
| Routine lemma proofs | No | Yes | Yes |
| Secondary results and extensions | One-sentence pointers | Statements + proofs | Yes |
| Long definitions/preliminaries variants | Compressed | Full generality | Full generality |
| Illustration figures, search procedures | No | Brief procedure note | Complete detail |
| Anything the paper's acceptance depends on | Must be at least *stated* here | Cannot live only here | Cannot live only here |

The invariant behind every row: a committee member who stops at page twelve must
still be able to state your contribution correctly and believe it is probably
true; a reviewer who continues must find every belief redeemable.

## Pointer discipline

Deferred proofs are only as good as their forward and backward links:

- At each in-body statement: `\emph{Proof in Appendix~\ref{app:lb}.}` — one
  pointer, exact target, never "proofs appear in the appendix" globally.
- At each appendix proof: restate the theorem before proving it (the
  `thmtools`/`\restatable` mechanism keeps restatements literally identical),
  so the discretionary reader does not page-flip to reconstruct the claim.
- Order appendix sections by the body's order of claims, not by proof
  dependency; a reviewer chasing Theorem 1.4 should not wade through the
  machinery of Theorem 1.2 to find it.
- Give the appendix its own two-or-three-sentence opening paragraph stating
  dependency structure ("Appendix B is self-contained; Appendix C uses
  Lemma A.3").

## What the appendix is not for

- Not an overflow valve for a bloated body. Twelve pages that read like a
  compressed twenty signal that the writing pass never happened; cutting
  secondary material *entirely* (into the full version) usually beats squeezing
  everything in.
- Not a second paper. Extensions that would each need their own referee
  ("we also resolve the directed case") dilute the committee's confidence
  budget; state one, defer the rest to the full version, or split the work.
- Not a hiding place. Burying a known limitation on page 47 while the body
  implies generality is the kind of asymmetry that turns a positive review
  negative when discovered — and assigned theory reviewers do discover it.

## Appendix smells and their repairs

- **The monolith:** one 30-page "Appendix A: Proofs" with no internal
  structure. Repair: one appendix section per body section or per major
  theorem, each named for what it proves.
- **The dependency maze:** Appendix C's lemma silently requires Appendix B's
  notation established twenty pages earlier. Repair: per-section dependency
  sentences and local notation reminders at first reuse.
- **The duplicate drift:** the appendix restatement of Theorem 1.2 differs by
  one quantifier from the body statement. Repair: `\restatable` or shared
  statement files — never retype (`stoc-reproducibility`).
- **The dangling pointer:** the body promises "Appendix D" and the appendix
  ends at C. Repair: a pre-upload pass compiling with `\refcheck` or grepping
  every `Appendix~\ref` target.
- **The kitchen sink:** half-finished generalizations kept "for completeness."
  Repair: cut to the full version; the submission appendix is a verification
  surface, not a notebook.

## Relationship to the full version

The submission appendix and the eventual arXiv/ECCC full version usually share
sources but serve different masters: the appendix is optimized for *selective
verification during review*; the full version for *linear reading forever*.
Before camera-ready, the full version typically re-expands what the appendix
compressed, restores the general statements, and becomes the canonical document
(`stoc-camera-ready` and `stoc-reproducibility` handle that transition and its
drift risks). During review, though, the single submitted PDF must stand alone:
STOC 2026 was double-blind, and a reviewer following an external link to your
named preprint is an anonymity event you caused.

## Cycle-volatility warnings

- The guaranteed-read wording (abstract + ToC + 12 pages) is 2026 CFP text;
  earlier cycles used a 10-page window, so re-read the live CFP each fall
  before budgeting pages (待核实 per cycle).
- Font/margin specifics (11-point, 1-inch, letter) are also restated annually.

## Output format

```text
[Appendix architecture] navigable / needs restructuring
[ToC audit] narrates argument / boilerplate labels <- rewrite
[Placement violations] <decision-critical content outside guaranteed pages>
[Pointer check] statement->proof links complete? restatements identical?
[Deferral plan] <what moves to full version entirely>
```
