---
name: itcs-supplementary
description: Use when splitting an ITCS paper's content between the body, the appendix, and the arXiv/ECCC/ePrint full version — deciding by what a reviewer must verify, so no central proof lives only in a preprint the PC is not obligated to read, while keeping the first-10-pages merits window clean.
---

# ITCS Supplementary

ITCS gives you three places to put content — the **body**, the **appendix** (part of the
submitted PDF), and the **full version** on arXiv/ECCC/ePrint — and the split is governed by one
rule: **anything a reviewer must read to judge the paper lives inside the submitted PDF.** Because
ITCS has **no hard page limit** and **no rebuttal**, the appendix is generous but load-bearing:
you cannot promise "details in the full version" for a proof that decides acceptance, and you
cannot answer later if a reviewer cannot follow. This skill decides what goes where.

## The governing principle: decision-criticality

Sort every piece of content by whether a reviewer needs it to *decide*:

- **Body (first ~10 pages):** everything needed to grasp the contribution and judge its
  novelty — the model, the motivation, the main theorem statements, proof *ideas*, and the
  novelty delta. This is the merits window the PC actually reads (see
  [`itcs-writing-style`](../itcs-writing-style/SKILL.md)).
- **Appendix (same PDF):** the **complete proofs** of central claims, full definitions, and any
  technical development too long for the body. This is *not* optional reading — it is where the
  "complete proofs of all central claims" requirement is satisfied.
- **Full version (arXiv/ECCC/ePrint):** the permanent, exhaustive record — extended discussion,
  additional corollaries, alternate proofs, and the same central proofs mirrored. It may contain
  *more*, but nothing decision-critical may live *only* here.

## The rule that trips people up

> **No central proof may live only in the external full version.** The PC is not obligated to
> open your arXiv posting. A reviewer who reaches "the proof of our main theorem is in the full
> version [ref]" and stops there will — correctly — treat the claim as unproved in the
> *submission*. Put every load-bearing proof in the submitted PDF's appendix.

Deferring to the full version is acceptable only for genuinely peripheral content: a fourth
corollary, a longer historical discussion, an alternate proof of an already-proved result.

## Use the no-page-limit generously but honestly

ITCS's lack of a hard limit is a gift with a catch:

- **Do put full proofs in the appendix** rather than compressing them into unreadability. A dense,
  unverifiable body proof is worse than a clear appendix proof with a body sketch.
- **Do not pad the merits window.** The first ~10 pages are judged on clarity of the *idea*; extra
  length there dilutes the innovation. Push technical bulk to the appendix, not into the intro.
- **Signpost precisely.** Every deferred proof gets an explicit "proof in Appendix C" and every
  appendix section says which body claim it discharges. A reviewer should never hunt.

## Content-placement table

| Content | Body (~first 10pp) | Appendix (same PDF) | Full version only |
|---|---|---|---|
| Model & definitions | Yes (core ones) | Full/edge-case variants | — |
| Main theorem statements | Yes | — | — |
| Proof ideas / sketches | Yes (a paragraph each) | — | — |
| Complete proofs of central claims | Idea only | **Yes (required)** | Mirror allowed, not sole home |
| Novelty delta / related work | Yes (the deltas) | Extended comparison | — |
| Routine calculations | Reference | Yes | — |
| Peripheral corollaries, alt proofs | — | Optional | Yes |
| Finite separating objects (graphs/codes) | Small ones inline | Larger ones | — |

## Anonymity and the full version

Posting a full version is encouraged under lightweight double-blind, but keep the split
consistent with the anonymity strategy (see [`itcs-submission`](../itcs-submission/SKILL.md)):

- The **submitted PDF** (body + appendix) omits author names, affiliations, and emails.
- The **arXiv/ECCC/ePrint** full version may be non-anonymous — that is permitted and normal.
- Do not let a cross-reference in the submission point at the named preprint in a way that reads as
  a deliberate identity reveal; a neutral "a full version is available" is enough.

## Output format

```text
[ITCS content-split status] clean / decision-critical-content-misplaced
[Merits window] model+motivation+results+deltas within ~10 pages, no padding? yes/no
[Appendix] complete proofs of ALL central claims present in the submitted PDF? yes/no
[Full-version leak] any load-bearing proof deferred ONLY to arXiv/ECCC/ePrint? list them
[Signposting] every deferred proof cross-referenced to its appendix section? yes/no
[Fix queue] <ordered; move any decision-critical content into the PDF first>
```
