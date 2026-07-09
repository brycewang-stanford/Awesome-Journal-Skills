---
name: icalp-artifact-evaluation
description: Use to understand why ICALP (EATCS) has no artifact-evaluation track or badge scheme, and what plays the equivalent role for a pure-theory paper — the full version with complete proofs, reproducible computational certificates, and optional machine formalization — so authors coming from a systems/ML venue do not waste effort building an artifact ICALP does not evaluate.
---

# ICALP Artifact Evaluation (there isn't one — and what replaces it)

Read this first if you are arriving from a venue with an artifact track. **ICALP has no artifact
evaluation, no artifact-evaluation committee, and no ACM/IEEE badges.** It is a **pure theoretical
computer science** venue: the contribution is a theorem, and the "artifact" a referee cares about is
the **proof**. Building a Docker image, a benchmark harness, or a reproducibility capsule for an ICALP
submission is effort spent on something no one will evaluate — and can even signal that the paper is
mis-routed.

## Why no artifact track

- ICALP results are **mathematical**: correctness is established by a proof a referee checks, not by
  running code on a machine.
- The community norm and the LIPIcs open-access model center the **published proof and the full
  version**, not a software deliverable.
- Contrast the software-engineering / systems / ML world (ACM/IEEE Available–Functional–Reusable–
  Reproduced badges, or ML reproducibility checklists): those exist because the contribution *is* a
  system or an empirical result. At ICALP it is not.

## What plays the artifact's role

| Systems/ML artifact concept | ICALP equivalent |
|---|---|
| "Artifacts Available" (archived, DOI) | The **full version** on arXiv/ECCC/HAL, and the open-access **LIPIcs** paper |
| "Functional" (it runs) | The **proof is complete and checkable** in the appendix / full version |
| "Reproduced" (results re-obtained) | An expert **re-derives / verifies the proof**; certificates for any computation |
| Reproducibility capsule | A **machine-checked formalization** (Coq/Lean/Isabelle), when provided |

So the "artifact" work for an ICALP paper is: **write the complete proofs**, make any **computation
checkable** (`icalp-experiments`, `icalp-reproducibility`), and optionally **formalize** the central
theorem.

## When your paper DOES contain software

Some ICALP papers include an implementation or a computer-assisted proof. Even then, there is no badge
track — but you should still:

- Make the code **reproducible** and reference it at camera-ready (public repo, or Zenodo/Software
  Heritage for a DOI), primarily to support the *proof*, not as a graded artifact.
- Provide **certificates** an independent checker can verify where the method allows.
- Keep any such repository from **breaking anonymity** during lightweight double-blind review.

If the implementation/experiment is the *actual contribution* rather than support for a theorem, that
is a routing signal: an experimental-algorithms track (e.g. ALENEX/ESA's experimental track), a
systems venue, or a database/ML venue may be the right home — see `icalp-topic-selection`.

## Do not

- Do not build an artifact-evaluation package for ICALP; there is nothing to submit it to.
- Do not import ACM/IEEE badge language or an ML reproducibility-checklist artifact into the paper.
- Do not assume a future ICALP will add an artifact track without checking the live call (**待核实**
  if ever announced).

## Output format

```text
[Artifact track?] none at ICALP (pure-theory venue)
[Proof-as-artifact] complete proofs in full version? yes/no
[Computation support] certificates / reproducible code where a proof uses computation? n/a or yes/no
[Formalization] none / partial / archived+cited (optional, not required)
[Routing flag] is software the real contribution (=> reconsider venue)? yes/no
```
