---
name: focs-related-work
description: Use when building the related-work and citation apparatus of a FOCS (IEEE Symposium on Foundations of Computer Science) paper — tracing result lineages across the FOCS/STOC record, citing arXiv/ECCC full versions with version pins, handling concurrent preprints, and keeping self-citation double-blind-safe.
---

# FOCS Related Work

At FOCS the bibliography sits inside the guaranteed-read set — the 2026 CFP
promises committee attention to the abstract, the references, and the first
ten pages (checked 2026-07-08). Theory reviewers routinely open a submission's
reference list first, to place the paper in a lineage they already know. This
skill treats related work as lineage engineering, not as a courtesy section.

## The lineage table

For each headline theorem, reconstruct its history as a table before writing a
word of prose. The table becomes the skeleton of the related-work section and a
private audit of your novelty claim:

| Year | Bound / result | Venue + version of record | Technique |
|---|---|---|---|
| 1998 | $O(n^2)$ | FOCS '98 → journal '01 | spectral partition |
| 2011 | $O(n^{1.5})$ | STOC '11 (arXiv v3 = full) | flow rounding |
| 2023 | $O(n^{1+o(1)})$, randomized | FOCS '23 (arXiv only full proofs) | (their name) |
| **this work** | deterministic $O(n^{1+o(1)})$ | — | (your name) |

Rules the table enforces: the "version of record" column forces you to learn
where each proof actually lives (the conference version often omits it); the
technique column reveals whether your delta is a new bound or a new method —
the committee weighs those differently.

## Citing theory literature correctly

- **Pin versions.** When a proof you rely on exists only in a preprint, cite
  the specific arXiv version, because v4 may have repaired — or broken — the
  lemma you use:

```bibtex
@misc{doe-widget-2024,
  author        = {Jane Doe and Wei Ren},
  title         = {Widget Sparsifiers in Almost-Linear Time},
  year          = {2024},
  eprint        = {2403.01234v3},
  archiveprefix = {arXiv},
  note          = {Full version of a FOCS 2024 paper; Lemma 5.2 cited
                   from v3 -- statement differs in v1--v2}
}
```

- **Distinguish the twins.** FOCS and STOC records are chronically confused in
  bibliographies; verify every `conf/focs/` vs `conf/stoc/` attribution on
  dblp rather than copying a `.bib` entry from a survey. A committee member
  who catches a misattributed classic discounts the rest of your scholarship.
- **Cite both versions when both matter.** Standard theory form: cite the
  conference announcement for priority and the journal/arXiv full version for
  the proofs, in one entry ("Conference version in FOCS 2019; full version in
  SIAM J. Comput. 2022").
- **ECCC has first-class status** in complexity; treat an ECCC technical
  report as citable and version-pinned exactly like arXiv.

## Concurrent and independent work

Theory's arXiv-first culture makes collisions visible early. House norms:

- A preprint appearing before your submission date must be engaged, even if
  only weeks old; "we were unaware" reads as "we did not check arXiv".
- Genuine independence is stated plainly and generously: one paragraph, what
  they prove, what you prove, where the techniques differ. Committees reward
  gracious handling and punish burying.
- If the concurrent result subsumes yours, say so to yourselves honestly
  before the committee does — a partially-subsumed paper can survive on its
  technique if the overview says which parts remain novel (`focs-writing-style`).

## Self-citation under double-blind

FOCS has run double-blind for multiple cycles. The operating rule: your own
prior work is ordinary literature. Cite it in the third person, with no
possessives, and never structure the paper so that understanding it *requires*
knowing the prior paper is yours. If your submission is the strengthening of
your own arXiv preprint, cite the preprint as an independent object; the CFP's
stated aim is unbiased first judgment, not unbreakable anonymity — but the
prose must not do the unmasking itself.

## The reference list as a guaranteed-read surface

Because FOCS promises committee attention to the references themselves,
treat the bibliography's *form* as reviewed prose:

- Consistent venue naming (decide once: "FOCS 2014" or "55th FOCS" — not
  both), full author lists, and no "et al." truncation in entries.
- Dead giveaways of haste — `[Anonymous, 2023]` placeholders, duplicate
  entries with different keys, arXiv entries for papers long since published
  — each costs credibility with the one reader who sees only abstract,
  references, and ten pages.
- Order citations within a bracket chronologically so lineage sentences read
  as history: "[12, 31, 7]" forces the reviewer to reconstruct the timeline
  you should have presented.
- A reference list that omits the obvious experts is also a signal — the
  committee infers whom you expect as reviewers, and gaps look strategic
  even when they are accidental.

## Pre-submission citation audit

1. Every bibliography entry checked against dblp or the publisher page — no
   entries inherited untested from other papers' `.bib` files.
2. Every "best known bound" claim paired with a citation dated within the
   last year — improvements you missed are the most common review correction.
3. Every reliance on an external theorem carries theorem number and version
   (this doubles as the checkability audit in `focs-reproducibility`).
4. arXiv swept for the last six months of your keywords; concurrent work
   engaged, not omitted.
