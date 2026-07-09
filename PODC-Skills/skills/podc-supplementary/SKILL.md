---
name: podc-supplementary
description: Use when deciding what goes in the first 10 read-guaranteed pages of an ACM PODC submission versus the full version / appendix, and when choosing between a regular paper and a Brief Announcement — so that nothing which decides acceptance lives past page 10 and every deferred proof remains reachable.
---

# PODC Supplementary

PODC's content-placement problem is unusual: the *submission* has no page limit, but only the
abstract and the **first 10 pages after the title page** are guaranteed to be read. Everything else —
including most of your proofs — is read at the committee's discretion. So the split is not
"paper vs. appendix" but "**decision-critical (must be in 10 pages) vs. verification-detail (may be
deferred)**." Get it wrong and a reviewer decides against a paper whose key idea sat on page 15.

## The placement rule

```text
Anything that decides ACCEPTANCE  -> first 10 pages after the title page (guaranteed read)
Anything that only VERIFIES it    -> full version / appendix (read at the committee's discretion)
```

Decision-critical means: the model box, the theorem statements, the delta over prior work, and
**enough of the proof to convince a reviewer the full proof exists** (the key lemma or the proof
idea). Verification-detail means: routine calculations, standard-lemma proofs, symmetric cases, and
the long technical core once its idea has been conveyed.

## What must live in the first 10 pages

| Element | Why it cannot be deferred |
|---|---|
| The model box | A reviewer cannot judge a theorem whose model they must reconstruct from page 14 |
| Theorem statements (all main results) | The contribution is the theorems; they anchor the whole review |
| Positioning / delta over prior bounds | Novelty is judged here; a buried comparison reads as none |
| The key idea / hardest proof step (at least a sketch) | The reviewer must believe the proof closes; a sketch of the crux earns that belief |
| Any matching lower bound's statement and idea | Optimality is a headline claim; its idea belongs up front |

## What may be deferred to the full version / appendix

- Full proofs of lemmas whose role and idea are already stated in the body.
- Routine or symmetric cases, provided the body says which cases are routine.
- Extended related-work discussion beyond the closest results.
- Optional simulation details (parameters, seeds, extra plots).
- Auxiliary constructions that support but do not constitute the main result.

Deferred does **not** mean absent: every deferred proof must be present in the submitted full version
and reachable by an exact cross-reference. "Proof omitted" with no full version is a soundness
red flag, not a space-saving move (see `podc-reproducibility`).

## Regular paper vs. Brief Announcement — a content decision

The most consequential supplementary decision is the *track*:

| You have... | Choose | Content shape |
|---|---|---|
| A complete result with full proofs | **Regular paper** | 10-page merits case + full version with all proofs |
| A result whose full version is/will be published elsewhere, or work in progress, or a small contribution | **Brief Announcement** | **≤5-page** self-contained submission; published ≤3 pages |

A Brief Announcement is not a place to dump an incomplete regular paper — it is a complete, small
statement of a result (or an announcement of one proved in full elsewhere). If your proof will not
close by the deadline, a Brief Announcement timestamps the idea honestly and leaves a full paper open
for a later venue; a regular paper with a gap is simply rejected. See `podc-submission` and
`podc-workflow` for the timing.

## Structuring the full version

- Mirror the body's numbering so "Lemma 3.2" is the same statement in both.
- Put the complete proofs in the order the body introduces their lemmas.
- Keep a single shared notation table.
- If posting to arXiv, the arXiv full version and the submitted full version should be the same
  document (modulo anonymization) — and after acceptance, keep it in sync with the camera-ready.

## Common failures

- **Key idea past page 10** — the crux of the proof only appears in the appendix, so the reviewer
  never sees why the result holds.
- **Model box deferred** — the theorem is unjudgeable in the first 10 pages.
- **"Proof omitted" with no full version** — deferral becomes disappearance.
- **Incomplete result forced into a regular paper** — should have been a Brief Announcement.
- **Complete result shrunk into a Brief Announcement** — throws away a full-paper slot.
- **Body/full-version cross-references that do not line up.**

## Output format

```text
[Track] regular paper / brief announcement — justified by proof completeness and length
[First-10-pages audit] model box / theorems / delta / key proof idea / lower-bound idea all present?
[Deferred correctly] routine proofs, symmetric cases, extended relwork, sim details in the full version?
[Reachability] every deferred proof present in the full version with an exact cross-reference?
[Fix queue] <content to promote into 10 pages; proofs to restore to the full version>
```
