---
name: aistats-supplementary
description: Use when preparing AISTATS supplementary material, appendices, proof details, code/data archives, simulation scripts, additional tables, and anonymized artifacts under deadline, size, anonymity, and reviewer-discretion constraints, including how to split a theory-plus-experiments paper between body and supplement.
---

# AISTATS Supplementary

Use this when assembling AISTATS supplementary material. The supplement can support the
paper, but the main submission must remain understandable without it.

## Supplement structure

- Put theorem proofs, derivations, extra ablations, simulation details, dataset
  documentation, and robustness tables in a clean appendix or supplementary manuscript.
- Put executable assets in a separate archive when current OpenReview forms allow it.
- Respect the current supplementary deadline. AISTATS 2026 placed supplementary-material
  submission after the paper deadline but before review.
- Keep all supplementary files double-blind: no authors, institutions, acknowledgements,
  private paths, repository owners, grants, or identifying metadata.
- Do not use the supplement to hide essential motivation, core method description, main
  theorem statements, or primary empirical results.
- Verify archives open on a clean machine and contain no credentials, cache directories,
  large irrelevant files, or hidden OS metadata.

## Appendix architecture for proofs

- Order appendix sections to mirror main-text theorem order; statistician reviewers navigate
  by theorem number, not by page.
- Restate each theorem before its proof so the appendix reads standalone without flipping
  back to the two-column body.
- Standard partition: notation and assumptions, main proofs, auxiliary lemmas, additional
  simulations, then real-data details.
- Keep one proof-sketch paragraph per major theorem in the body itself; an AISTATS submission
  whose entire argument lives in the supplement reads as unreviewable within the page limit.
- Cross-reference every appendix table and lemma from the body at least once; orphaned
  supplement material is invisible to reviewers and wasted under reviewer discretion.
- If the cycle allows appendices inside the main PDF after the references, confirm against
  the current instructions whether that or a separate file upload is expected.

## What gets opened first

| Supplement item | Inspection likelihood | Practical implication |
|---|---|---|
| Proof of the headline theorem | High | Polish it to main-text standard |
| Extra ablation and robustness tables | Medium | Reference each one from the body |
| Code archive | Variable, reviewer discretion | The README must orient a reader in one minute |
| Raw experiment logs | Low | Include for completeness, never rely on them |

## Vignette: splitting an optimization paper

A submission proving a convergence guarantee for a stochastic mirror-descent variant, plus
benchmark plots: the body keeps the theorem, the key lemma, the proof roadmap, and two
decision-critical figures; the appendix holds full proofs and step-size sensitivity grids;
the archive carries the seeded experiment runner. Nothing decision-critical lives only in
the archive, because archive inspection at AISTATS is discretionary.

## Output format

```text
[Supplement status] Ready / Needs fixes / Not ready
[Files] <appendix/proofs/code/data/logs>
[Deadline] <current supplement deadline and source>
[Anonymity checks] <passed/issues>
[Main-paper dependency] <what breaks if supplement is ignored>
```
