---
name: podc-reproducibility
description: Use when making an ACM PODC paper's result independently checkable — reproducibility for a proofs venue, not an artifact venue. Covers a self-contained proof appendix, an explicit and checkable model/assumption box, honest handling of any optional simulation, and keeping the full version (with proofs) in sync with the 10-page camera-ready.
---

# PODC Reproducibility

"Reproducibility" at a proofs venue means a reader can **independently verify the theorem**. PODC has
**no artifact track** and no ACM badge program, so there is nothing to package for evaluators — the
deliverable that makes your result checkable is a **self-contained proof** and an **honest model
box**. This skill translates the open-science instinct into what actually matters at PODC.

## What "checkable" means here

A PODC result is reproducible when a competent reader, given only your submission and its full
version, can:

1. Read the **model box** and know exactly what network, timing, fault, adversary, randomness, and
   cost-measure assumptions are in force.
2. Follow every proof to its base cases and cited lemmas **without needing an external file, a
   private note, or a "details omitted"**.
3. Confirm that each theorem holds in the stated model and nowhere relies on a stronger assumption.

## The self-contained proof appendix

Because the 10-page merits budget cannot hold full proofs, the **full version** (submitted as the
paper, and later posted to arXiv) carries them. Make it self-contained:

```text
[Every lemma stated]     each lemma the main theorem uses appears with a full proof, or a precise
                         citation to an external theorem (statement quoted, not just referenced)
[No "it is easy to see"] for any nontrivial step; either prove it or mark it explicitly routine
[Base cases present]     inductions and recursions have their base cases proved
[Invariants proved]      each named invariant is shown to hold initially and be preserved
[Notation defined once]  a single notation table the appendix and body share
[Cross-references exact]  "by Lemma 3.2" points to the right statement in both body and full version
```

A proof that says "the remaining case is symmetric" is fine only if it truly is; reviewers check the
"symmetric" cases that turn out not to be.

## The model/assumption box is the reproducibility contract

The single most common reason a PODC result fails to reproduce is an **assumption used but not
declared**. Treat the model box (see `podc-writing-style`) as a contract:

- Every assumption the proofs use must be *in the box*. If a proof needs a shared coin, the box must
  grant one. If it needs FIFO channels, the box must say so.
- Nothing in the box may be silently strengthened mid-proof (asynchrony becoming "eventually
  synchronous" without invoking GST; an oblivious adversary becoming "non-adaptive within a phase").
- If a result holds only in a parameter regime, the box or the theorem states the regime.

Run the assumption audit from `podc-experiments` and confirm the box covers everything the proofs
consume.

## Optional simulations: transparent, not load-bearing

If the paper includes a simulation (many do not), make it reproducible *as an illustration*:

- State the parameters, ranges, number of trials, and **random seeds**; pin the environment
  (language/version) in the full version or a linked bundle.
- One-command reproduction is a nice-to-have, not a requirement — the result stands on the proof.
- Keep any simulation repository/author-page link out of the anonymized submission (lightweight
  double-blind), and add it only in the camera-ready / arXiv version.
- Never present simulation output as if it verified the theorem; label it "illustrative."

## Keeping the full version in sync

- The **camera-ready** (≤10 proceedings pages) and the **arXiv full version** must state identical
  theorems; only the proof detail differs. A theorem tightened in one and not the other is a
  correctness-record bug.
- When you fix a proof after acceptance, propagate the fix to the arXiv version and note the revision
  — the community reads arXiv for the proofs.
- Cross-reference the full version from the proceedings paper ("full proofs in the full version
  [arXiv:...]") so a reader can always reach the complete argument.

## Common failures

- **"Proof omitted" with no full version** — the result is then unverifiable; unacceptable at a
  proofs venue.
- **Assumption used but not in the model box** — the reproducibility contract is broken.
- **Body and full version disagree** on a theorem statement or constant.
- **Simulation dressed as verification** — a plot presented as if it proved correctness.
- **De-anonymizing link in the submission** — a simulation repo that reveals authorship under
  double-blind.

## Output format

```text
[Proof appendix] self-contained? every lemma proved/precisely cited? base cases + invariants present?
[Model box contract] every assumption the proofs use is declared and never silently strengthened?
[Body <-> full version] theorem statements identical; full proofs reachable from the proceedings paper?
[Simulation] absent / illustrative-with-seeds-and-ranges; no de-anonymizing links at review time?
[Fix queue] <omitted proofs to supply; undeclared assumptions; sync mismatches>
```
