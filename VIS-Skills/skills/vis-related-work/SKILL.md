---
name: vis-related-work
description: Use when positioning an IEEE VIS submission against the visualization literature across TVCG, the six VIS areas, EuroVis/CGF, PacificVis, and adjacent HCI/graphics venues, writing delta-first contrast rather than a citation catalog, keeping self-citations double-blind when opted in, and handling concurrent, preprint, and prior-version overlap for a TVCG journal article.
---

# VIS Related Work

Use this to audit novelty and positioning. IEEE VIS reviewers are close to the visualization
literature and expect to see where your paper sits relative to the nearest prior work — stated as a
**delta**, not a list. Because VIS full papers are **TVCG articles**, the novelty bar is a journal
bar. Reopen the current call for dual-submission, anonymity, and prior-publication rules before
advising authors.

## Positioning checks

- **Separate the visualization novelty from the engineering.** What is new: a visual encoding, an
  interaction technique, a system integrating known parts in a newly effective way, an empirical
  finding about perception or use, or a model/methodology?
- **Cover the visualization lanes.** VIS reviewers expect TVCG/VIS prior work in your area, the
  European (EuroVis / Computer Graphics Forum) and Pacific (PacificVis) literature, and the adjacent
  HCI/graphics venues when you borrow from them (see the table). A bibliography missing the obvious
  sibling work reads as unaware.
- **Write delta-first.** Each closely related paper gets one sentence naming what it did and one
  naming what you do differently — not a summary. Position, don't catalog.
- **Preserve double-blind (if opted in).** Cite your own prior work in the third person and never
  link reviewers to an identity-revealing preprint, repository, demo, or homepage.
- **Declare overlap** with any prior short-paper, poster, or workshop version, or a concurrent
  submission; do not re-submit archival work as new.

## Visualization literature lanes

| Lane | Typical venues | What VIS reviewers check |
|---|---|---|
| Core VIS by area | IEEE VIS / TVCG (your primary area of the six) | Whether the nearest technique/study/system in your area is compared or distinguished |
| European visualization | EuroVis, Computer Graphics Forum (CGF) | Whether closely related European work is credited |
| Pacific / regional | PacificVis, and regional venues | Whether adjacent regional contributions are engaged |
| Adjacent HCI | CHI, UIST | Whether interaction/usability predecessors are cited to origin |
| Adjacent graphics/analysis | SIGGRAPH, KDD/ML when relevant | Whether borrowed rendering or analytics methods are cited to their real source |

A bibliography that cites only your own narrow topic tells a reviewer the delta may be smaller than
claimed; one that reaches the sibling areas, EuroVis, and the adjacent venues signals command of the
field.

## Delta-first positioning vignette

Suppose the paper proposes a new **set-visualization** technique. Its nearest neighbors: a
matrix-based set technique (dense but hard to read at scale), an Euler-diagram approach (intuitive
but not scalable), and an aggregation-based tabular technique (scalable but less expressive for
individual elements). The novelty sentence should name all three contrasts — readability where the
matrix failed, scale where the Euler diagram failed, and expressiveness where the tabular technique
traded it away — rather than summarizing each.

## Concurrent and prior-version judgment calls

```text
[Concurrent arXiv work]   cite neutrally, state the technical difference, avoid unverifiable
                          priority claims; keep the citation double-blind if opted in
[Your short paper/poster] usually non-archival and citable, but confirm against the current call
                          and phrase so anonymity survives
[Prior workshop version]  declare the overlap and state what the full paper adds beyond it
[Archival status unclear] declare the overlap in the submission form rather than guessing a
                          chair's interpretation
```

## Eligibility red flags

- Substantial text or figure overlap with a published paper by the same authors (self-plagiarism).
- A "new" system that re-reports a prior technique's results without a new contribution.
- Citations exclusively to non-visualization venues, signaling the paper may be a visitor from
  HCI/ML/graphics rerouted without reframing for a visualization audience.

## Output format

```text
[Eligibility] clear / needs declaration / risky
[Lanes covered] <core-VIS-area / EuroVis-CGF / PacificVis / adjacent-HCI / adjacent-graphics>
[Nearest 3 works] <work -> one-line delta>
[Archival-overlap risk] <none / declare: what>
[Novelty sentence] <VIS-ready contribution contrast against the nearest prior work>
```
