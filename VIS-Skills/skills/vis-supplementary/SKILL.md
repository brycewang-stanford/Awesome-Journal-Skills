---
name: vis-supplementary
description: Use when deciding what belongs in an IEEE VIS paper body versus its supplemental materials, covering the VGTC/TVCG 9+2 page budget, the supplemental video that VIS reviewers routinely watch, the one-week supplemental deadline extension, double-blind supplemental anonymization, and how to split a visualization paper between the reviewed pages and the archive.
---

# VIS Supplementary

Use this when assembling IEEE VIS supplemental material. The governing rule is strict: **the paper
must be judgeable from the reviewed pages alone.** But VIS is unusual among conferences in how much
its reviewers *rely on the supplemental video and code* to understand an interactive contribution —
so the split is not "body carries everything, supplement is optional" but "body carries the decision,
supplement makes the interaction and reproduction legible."

## What goes where

| Content | Body (within 9-page budget) | Supplemental (archive/video) |
|---|---|---|
| The contribution and its claims | Yes | — |
| Core technique / system design / study design | Yes | Full parameter grids, extra configs |
| Headline results and the evaluation that backs them | Yes | Full result tables, secondary conditions |
| The encoding/interaction rationale | Yes | — |
| A static figure of the interface | Yes | The **video** showing the interaction in motion |
| Statistical tests behind a claim | The result + test named | The analysis notebook |
| Datasets, stimuli, raw study responses | Summary + selection criterion | The full data/stimuli |
| Reproduction instructions | A pointer | The README + build/run scripts |

If a reviewer would need to open the archive to know whether to accept, the paper is
mis-partitioned — move that evidence into the body. But an interactive system that cannot be
understood without seeing it move **should** ship a video; a static screenshot alone under-sells it.

## The supplemental video (a VIS-specific expectation)

For technique and system papers, the video is often how reviewers judge whether an interaction
actually works. Treat it as a first-class deliverable:

```text
[Length]     keep to the customary short length; lead with the contribution, not a long intro
[Content]    show the real interaction on real data, at usable speed; caption what to watch
[Quality]    legible resolution, readable text, no stutter; a required codec/container
[Anonymity]  if double-blind, strip affiliation slates, voice-over names, visible usernames,
             desktop clutter, and watermarked project URLs
[Deadline]   VIS 2026 gives a one-week window AFTER the paper deadline for supplemental material —
             use it to finish and anonymize the video, not to keep editing the paper
```

## The page-budget discipline

VIS's VGTC/TVCG budget is **9 pages of content + up to 2 pages of references and acknowledgements**.
It counts figures and tables — and visualization papers are figure-heavy. Consequences:

- Keep the evaluation that decides acceptance and the encoding rationale **in the body**.
- Push full parameter tables, additional conditions, extra stimuli, and long apparatus details to
  the supplemental archive with explicit forward references.
- Do not use the supplement to smuggle in a result that would not fit — an argument that only closes
  with material outside the reviewed pages reads as unreviewable.
- Budget figure space deliberately: one well-designed teaser and the key result figures earn their
  space; a wall of thumbnails does not.

## Double-blind supplemental rules (when you opt in)

```text
[No identity]   no authors, affiliations, acknowledgements, grants, cluster paths, lab names, or
                repo owners anywhere in the archive, README, or video
[Anonymized links] the open-materials link points at an anonymizing host, not a personal repo/OSF
[Clean archive]  no .git history, .DS_Store, credentials, caches, or huge irrelevant files
[Playable]       verify the video plays in a standard player and the archive unzips and builds
                from a one-minute README on a fresh machine
```

## Vignette: splitting a system + study paper

A paper contributing an interactive analytics system plus a user study: the body keeps the design
rationale, the system's key views, the headline study results with effect sizes, and the threats;
the supplement holds the **video** demonstrating the interaction, the system's source with a build
script, the study stimuli and anonymized responses, and the analysis notebook. Nothing
decision-critical lives only in the archive, but the interaction is only fully legible via the video.

## Output format

```text
[Supplement status] ready / needs fixes / not ready
[Partition check] anything decision-critical outside the body? <none / move: what>
[Video] present and legible? shows real interaction? anonymized (if double-blind)? yes/no
[Page budget] body within 9 pages? refs within 2? figures earning their space? yes/no
[Anonymity] archive + video clean of identity + metadata? passed/issues
[Body dependency] <what a reviewer can decide without opening the archive>
```
