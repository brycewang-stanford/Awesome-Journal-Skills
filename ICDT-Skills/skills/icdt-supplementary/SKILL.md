---
name: icdt-supplementary
description: Use when deciding how to split an ICDT (International Conference on Database Theory) paper between the 15-page lipics-v2021 body and the clearly-marked appendix that referees read at their discretion, given that online/external appendices are not allowed and every proof needed to certify the result must live inside the single submitted PDF.
---

# ICDT Supplementary Material

Decide what goes in the body, what goes in the appendix, and — the ICDT-specific constraint — accept
that **there is no online supplement**. ICDT allows a **clearly marked appendix** inside the
submission PDF, read **at the discretion of the program committee**, but it **does not allow
online/external appendices**. So everything a referee could need to certify your theorem must be in
the one PDF, and you must write the body assuming the appendix might not be read.

## The one hard rule

> **The 15-page body (excluding references) must let a referee judge that the result is correct and
> significant on its own. The appendix supplies the full proofs for the referee who chooses to check
> them. Nothing decision-critical may depend on material outside the submitted PDF.**

Because online appendices are forbidden, you cannot offload proofs to arXiv "for the reviewers." The
full version on arXiv is for *readers after publication*; the *reviewed* object is the single PDF.

## What belongs where

| Content | Location | Reason |
|---|---|---|
| Definitions, models, main theorem statements | Body | The referee must have them to judge the claim |
| Proof ideas / sketches of the main results | Body | Enough to make correctness plausible without the appendix |
| Full, detailed proofs | Marked appendix | Read at the PC's discretion; keep the body within budget |
| Routine lemmas and calculations | Appendix | Necessary but not illuminating in the body |
| A worked example that clarifies the construction | Body | High-value, checkable by hand; earns its space |
| Extended related work, tables of cases | Appendix | Useful reference, not needed to follow the argument |
| Anything that decides acceptance | **Body (at least in sketch)** | A referee who skips the appendix must still be convinced |

## Writing for "read at the PC's discretion"

Referees may or may not open the appendix, so:

- **Self-contained body:** each main theorem has, in the body, either a proof or a sketch detailed
  enough that a referee believes it is provable and sees the key step.
- **Signposted appendix:** label appendix sections to match the theorems ("Appendix A: Proof of
  Theorem 3"), so a referee checking one claim finds it instantly.
- **No forward-dependence on the appendix for understanding** — the body should never say "see the
  appendix for what this means"; definitions and statements are in the body.
- **The appendix is proofs, not new results** — do not smuggle an additional theorem into the
  appendix to dodge the page limit; a result that matters belongs in the body.

## What the appendix is not

- **Not an online link.** No "additional experiments/proofs available at <url>" for the review — the
  URL both breaks the no-online-appendix rule and can de-anonymize you.
- **Not overflow for a too-long paper.** If the body cannot state the contribution in 15 pages, the
  fix is compression or splitting the result, not exiling half the argument to the appendix.
- **Not a dumping ground** — an unreadable 40-page appendix is as unpersuasive as no proof; keep it
  organized and referee-navigable.

## The full version (separate from the appendix)

Keep a **full version** with all proofs, typically on arXiv, for after acceptance. It is the
permanent scholarly record and the thing the camera-ready references — but it plays no role in the
anonymous review, where only the single PDF counts. See `icdt-camera-ready` for linking it and
`icdt-reproducibility` for keeping it consistent with the published version.

## Output format

```text
[Body self-sufficiency] every acceptance-critical claim provable-from-the-body (>= sketch)? yes/no
[Appendix] present, clearly marked, signposted per theorem? yes/no
[No-online-appendix] zero external links required for review? yes/no
[Budget] body <= 15 pages excl. refs? yes/no
[Fix queue] <move X to body / compress Y / no external dependence>
```
