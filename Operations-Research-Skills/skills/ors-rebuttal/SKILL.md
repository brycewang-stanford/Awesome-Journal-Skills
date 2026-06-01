---
name: ors-rebuttal
description: Use when responding to an Operations Research (OR) decision letter — writing the point-by-point response, closing proof gaps, adding baselines/instances, and passing the ORJournal code/data reproducibility review across a revision cycle. Drafts the revision and response; it does not parse the decision in the first place (ors-review-process) or run the final preflight (ors-submission).
---

# Revision & Response (ors-rebuttal)

## When to trigger

- You have a major/minor revision decision from the handling Area Editor and must respond.
- A reviewer found a proof gap, a missing baseline, or a reproducibility shortfall.
- You are preparing the code/data deposit for the ORJournal pull-request review.

## The OR response letter

*Operations Research* revisions are **technical**. Reviewers expect the mathematics and
computation to actually change, not just the prose. Structure the response so every
point is traceable:

- **Point-by-point, verbatim.** Quote each reviewer/editor comment, then give your
  response and the **exact location** of the change (section, theorem, table, e-companion).
- **Honor the editor's synthesis first.** Address the binding points the Area/Associate
  Editor emphasized before optional reviewer suggestions.
- **Be precise about what changed.** "We now prove Theorem 3 without Assumption 2; see
  the new Lemma 4 and Appendix B" beats "we revised the proof."

## Closing the common technical asks

| Reviewer ask | Substantive response |
|--------------|----------------------|
| "Proof gap / assumption smuggled in" | Repair the proof; state where each assumption is used; add a lemma if needed |
| "Assumption too strong" | Weaken it (relaxation/counterexample) or justify necessity with a counterexample |
| "Bound not tight" | Prove tightness with a matching instance, or reframe as best-known |
| "Missing baseline / weak instances" | Add the closest prior method and recognized benchmark instances; rerun |
| "Stochastic results unreliable" | Add confidence intervals, more replications, CRN, fixed seeds |
| "Not reproducible" | Provide the ORJournal repo: README/LICENSE, structure, runnable scripts |

## Reproducibility review (ORJournal)

If accepted in principle, code/data go through the **ORJournal GitHub pull-request**
process: a structured repository with **README/LICENSE**, the prescribed **directory
structure**, and documented **hardware/software/data/installation/run** steps so a
reviewer can regenerate the results. Pin versions and seeds. If data are
confidential/licensed/non-public or the paper is purely methodological, ensure the
**exemption** (requested in the cover letter, decided by the Area Editor with EiC
authority) is in place. Respond promptly to reproducibility comments on the PR.

## Length & format discipline through revision

- Keep the introduction **equation-free**; new long proofs go to the **e-companion**
  (which must not be longer than the manuscript).
- Stay within the **page tier** for your manuscript type; move ablations/extra tables to
  the e-companion rather than bloating the main text.
- Maintain **author-year** citations and consistent notation across new material.

## Anti-patterns

- A defensive letter that argues instead of fixing a genuine proof gap.
- Claiming a change without pointing to where it appears.
- Adding experiments but no confidence intervals or seeds.
- Blowing past the page tier or the e-companion length rule to answer reviewers.
- Ignoring the editor's synthesis to chase every minor reviewer remark.

## Output format

```
【Response letter】point-by-point, verbatim quotes + change locations?
【Editor synthesis】binding points addressed first?
【Technical fixes】proofs / assumptions / bounds / baselines / stochastic care
【Reproducibility】ORJournal repo ready / exemption in place?
【Format】equation-free intro; within page tier; e-companion ≤ manuscript
【Next step】resubmit → ors-review-process (next round) or ors-submission (final checks)
```
