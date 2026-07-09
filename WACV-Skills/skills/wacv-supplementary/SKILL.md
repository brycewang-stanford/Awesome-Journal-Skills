---
name: wacv-supplementary
description: Use when organizing WACV supplementary material, covering what belongs in the anonymized supplement versus the 8-page body, packaging qualitative videos and extra results without breaking double-blind, keeping the supplement consistent with the paper across the two-round revision, and honoring WACV's no-author-identifying-links rule.
---

# WACV Supplementary

Use this to decide what leaves the 8-page body for the supplement and how to package it
without leaking identity. WACV's applications work is often visual and systems-heavy, so the
supplement carries videos and protocol detail — and the two-round model means it must stay
consistent with the paper across a revision. Facts are the WACV 2026/2027 cycles as read on
2026-07-09.

## Body vs supplement split

The **8-page body including figures and tables** holds the argument; the supplement holds
the evidence a reviewer consults to verify it. Keep the body self-sufficient — a reviewer
must be able to follow the contribution without opening the supplement — and push depth down:

| Keep in the 8-page body | Move to the supplement |
|---|---|
| The contribution, the constraint, the headline comparison | Full protocol: splits, devices, meters, hyperparameters |
| One teaser + the decisive qualitative and quantitative results | Extra qualitative grids and per-class breakdowns |
| The claim → evidence pairing | Video demonstrations of the deployed system |
| The core ablation | Additional ablations and sensitivity studies |
| A short proof sketch (if any) | Full derivations |

## Anonymity is the hard constraint

Everything in the supplement is double-blind. The failure modes are specific to rich media:

```text
Supplement anonymity sweep:
  - Video overlays / watermarks / on-screen titles naming a lab or product  → remove
  - File and folder names carrying author or institution strings            → rename
  - Metadata in videos, PDFs, and archives (author/creator fields)          → strip
  - Any link to a project page, repo, or drive that identifies the authors  → delete
  - Acknowledgements, grant IDs, or dataset provenance that de-anonymizes    → redact
```

Do not use an external link to smuggle content past the page limit or the anonymity rule; a
reviewer following a link to an identifying site is an anonymity break, and content that
review depends on must be in the uploaded files, not behind a URL.

## Package it as evidence, not a dump

A supplement is read to answer a specific doubt, so structure it so a reviewer can find the
answer: index the videos to the claims they support, label extra tables by the body figure
they extend, and name the protocol section for the experiment it reproduces. An unindexed
pile of results earns no credit for the effort.

## Consistency across the two rounds

When a Revise-and-Resubmit paper changes an experiment, the supplement must change with it —
the same number, split, or video cannot say one thing in the body and another in the
supplement. Re-run the anonymity sweep on the revised supplement too; a revision is a common
place for an identifying link or filename to slip back in.

## Reverify each cycle

- The supplementary submission deadline (in some cycles it trails the paper deadline).
- Supplementary size and file-type caps (not fetchable for 2026 — 待核实).
- The anonymity and external-link rules for the current cycle.

## Output format

```text
[Body self-sufficient] argument stands without the supplement: yes/no
[Split] what moved to supplement: <list>
[Media anonymity] videos/filenames/metadata/links clean: yes/no
[Indexing] supplement items mapped to the claims they support: yes/no
[Round sync] supplement matches revised body: yes/no
[Blocker] <the item risking an anonymity break>
```
