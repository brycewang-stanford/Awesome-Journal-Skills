---
name: icalp-reproducibility
description: Use when making an ICALP (EATCS) theory result independently checkable — writing complete, self-contained proofs in the appendix and a full version (arXiv/ECCC/HAL), pinning any computational steps to reproducible certificates, and (optionally) formalizing key theorems in Coq/Lean/Isabelle, since ICALP has no runnable-artifact track and proof verifiability is the analogue of reproducibility.
---

# ICALP Reproducibility (proof verifiability and the full version)

At a pure-theory venue, "reproducibility" means a referee — and later any reader — can **check the
proof**. ICALP has **no artifact-evaluation track and no badges**; the deliverable that plays that role
is the **full version** with complete proofs, plus, where relevant, reproducible computational
certificates and optional machine formalization. This skill builds that checkability into the paper
from the start, because a proof cannot be reconstructed after the fact any more than a lost dataset can.

## The full version is the reproducibility story

- The 15-page body sketches; the **full version** (a clearly labelled appendix at submission, and an
  **arXiv/ECCC/HAL** posting at/after notification) contains **every proof in full**. This is what
  makes an ICALP result reproducible: an independent expert can verify it end to end.
- Write proofs **self-contained**: state every lemma the argument uses, prove or cite each, and avoid
  "it is easy to see" for steps that are not. The test is whether a competent non-author can follow it
  without asking you.
- Keep the **submission appendix and the eventual arXiv version consistent** — divergence between "what
  the referees checked" and "what is public" undermines trust.

## Self-contained proof checklist

```text
[ ] Every theorem's proof is present in full somewhere the referee can read it
[ ] Every lemma used is stated and proved or cited to a precise source
[ ] No "omitted" / "similarly" hiding a genuinely hard case
[ ] Constants and asymptotics are traceable (no unexplained factor changes mid-proof)
[ ] Definitions precede use; notation is defined once and used consistently
[ ] The dependency structure of lemmas is clear (nothing circular)
```

## Reproducible computation, when a proof uses it

If a proof relies on computation (see `icalp-experiments`), the computation must be checkable, not
merely asserted:

- Ship **code and inputs**, or precise pseudocode, in the full version or a referenced public repo.
- Prefer an **independently verifiable certificate** (UNSAT proof, LP/Farkas witness, explicit witness
  object) over "our program confirms it."
- **Pin** solver versions and any random seeds so the check is deterministic.

## Optional: machine-checked formalization

ICALP does not require formalization, but a **Coq/Lean/Isabelle** proof of a central theorem is a
strong, increasingly valued signal — especially for intricate combinatorial or semantic arguments:

- Formalize the **load-bearing** theorem, not the whole paper, and say precisely **what** is formalized
  and **what is assumed** (axioms, unformalized lemmas).
- Archive the development (a public repo, or Software Heritage / Zenodo for a DOI) and reference it in
  the camera-ready. Do not let it break anonymity during review.
- Be honest about the gap between the paper's statement and the formal statement; an over-claimed
  formalization is worse than none.

## What ICALP reproducibility is NOT

- It is **not** a runnable-system artifact, a Docker image of an implementation, or a benchmark
  harness — there is no artifact track and no badge to earn (`icalp-artifact-evaluation` explains the
  distinction).
- It is **not** "available upon request." A proof that only the authors can complete is, for review
  purposes, not a proof.
- It is **not** satisfied by an arXiv link alone if that version, too, defers the hard steps.

## Worked vignette: an intricate lower bound

A Track A conditional lower bound hinges on a delicate gadget construction. To make it reproducible:
prove the gadget's properties in full in the appendix (not "by inspection"); include a small
computer-checked verification of the gadget's truth table with a shipped, re-runnable script and its
output; post an arXiv full version at notification identical in content to the checked appendix; and,
optionally, formalize the core combinatorial lemma in Lean and cite the archived development at
camera-ready. State clearly which parts are machine-checked.

## Output format

```text
[Full version] complete proofs present (appendix now, arXiv at notification)? gaps: <where>
[Self-containment] lemmas stated+proved/cited; no hidden hard cases? yes/no
[Computation] certificates / reproducible inputs provided where a proof uses computation? n/a or yes/no
[Formalization] none / partial (what theorem, what assumed) / archived+cited
[Anonymity] full version / repo referenced without breaking the blind during review? yes/no
[Fix queue] <ordered: proof completeness, certificates, formalization scope>
```
