---
name: cvpr-supplementary
description: Use when deciding what belongs in a CVPR supplementary upload versus the 8-page body, covering the one-week-later supplement deadline, video and qualitative-result norms in computer vision, anonymous code packaging, the no-external-links rule, and keeping decision-critical evidence out of material reviewers may skip.
---

# CVPR Supplementary Material

CVPR gives supplementary material its own deadline — November 20 in the 2026 cycle, one
week after the November 13 paper deadline — and vision reviewers open supplements more
than reviewers at most venues, because qualitative evidence lives there. That makes the
supplement a designed deliverable, not an attic. Facts below are the 2026 cycle as read
on 2026-07-08.

## The placement decision

One rule sorts everything: **anything a reviewer needs to judge the claims must be in
the 8-page body.** The supplement is legitimately for *depth* on things the body already
establishes. A useful decision table:

| Content | Body or supplement? | Reasoning |
|---|---|---|
| Headline quantitative results | Body | The claim itself |
| Core ablation (the one that justifies the design) | Body | Reviewers rank papers on it |
| Full ablation grids, extra datasets | Supplement | Depth on an established point |
| Method details needed to believe the numbers | Body (compressed) | "See supplement" for correctness reads as evasion |
| Derivations, proofs, extra math | Supplement | Vision reviewers spot-check |
| Qualitative result grids beyond page 8 | Supplement | Expected and widely read |
| Failure cases | Both: one in body, catalog in supplement | Honesty signal reviewers reward |
| Video results (tracking, generation, 3D, robotics) | Supplement | The only sanctioned channel — external video links are banned |
| Code + configs | Supplement | See `cvpr-artifact-evaluation` |

## Video is evidence, not marketing

For temporal or 3D work, the video *is* the result, and since external links are
prohibited, the uploaded file is your one shot:

- Lead with uncut, representative sequences; put comparisons side-by-side with labeled
  methods (anonymized — "Ours" vs "[24]", never lab-recognizable branding).
- Include at least one failure sequence; a flawless reel reads as curation.
- Keep an index (`README.txt`) mapping each clip to the paper section it supports.
- Strip authorship metadata from containers; MP4 tags leak names more often than PDFs.
- Mind size: the 2026 cap on supplement uploads was not verifiable (待核实) — compress
  to survive a strict cap and check the current page before rendering hours of footage.

## The extra week is for packaging, not new results

The supplement deadline trailing the paper by a week is a packaging window. The
submitted PDF is frozen; a supplement that introduces results the body never mentions
effectively smuggles content past the page limit, and reviewers treat it that way.
Legitimate week-two work: rendering video, cleaning code, formatting the extended
tables the body already cites. Every body reference ("see Suppl. B") must resolve — a
dangling pointer is the most common supplement bug at every CVF venue.

## Structure a tired reviewer can navigate

```text
supplement.zip
├── suppl.pdf            # A: extended results · B: ablation grids · C: failures
│                        # D: implementation detail · E: derivations
├── videos/
│   ├── README.txt       # clip → claim map, one line each
│   ├── 01_main_comparison.mp4
│   └── 02_failure_modes.mp4
└── code/                # scrubbed; see cvpr-artifact-evaluation
    └── REPRODUCE.md     # table/figure → command
```

Use the same numbering scheme as the paper (Suppl. Table 7 continues Table 6), start the
supplement PDF with a half-page table of contents, and repeat each research question
above its ablation grid so sections stand alone.

## Recurring supplement bugs, ranked by frequency

Seen across CVF-venue submission cycles; all are findable in a one-hour audit:

1. **Dangling pointers** — "see Suppl. E" where the supplement stops at D, usually
   after a late reorganization. Grep the body for `Suppl` and resolve each.
2. **Numbering resets** — supplement tables restarting at "Table 1", colliding with
   the body's Table 1 in reviews ("which Table 1?").
3. **Contradictory hyperparameters** — the body says 90 epochs, the supplement's
   config dump says 100, because one was updated post-freeze. Generate both from the
   recipe ledger.
4. **Un-anonymized third-party assets** — a baseline's output video with its authors'
   watermark, or a dataset figure carrying a lab logo.
5. **Compression damage** — qualitative comparisons where JPEG artifacts exceed the
   method differences being illustrated; export lossless crops for the regions the
   text argues about.
6. **The kitchen-sink PDF** — 40 unnumbered pages of grids with no table of contents,
   which reviewers close after page 2. Curated depth beats exhaustive depth.

## Anonymity applies with full force

The supplement is reviewed double-blind under the same rules as the paper: no author
names in code headers, no institutional dataset paths, no acknowledgements, no grant
IDs, no watermark from a lab's internal tooling. And the external-link ban applies —
a "project page" URL inside the supplement PDF is a policy violation, not a shortcut.

## How reviewers actually consume it

Design for the observed reading pattern, not the hoped-for one: the supplement gets
opened (a) right after the body's qualitative section, looking for more examples and
the failure cases, (b) during score justification, verifying one implementation
detail, and (c) in discussion week, when another reviewer cites it. Each entry point
should land in seconds — which is why the table of contents, paper-continuous
numbering, and the clip-to-claim README are not cosmetics but the difference between
a supplement that testifies for you and one that never takes the stand.

## Reverify each cycle

- Supplement deadline offset and whether late supplement upload is still permitted.
- Size caps and accepted formats (待核实 for 2026).
- Whether reviewers are formally told supplements are optional reading — phrase body
  pointers so the paper survives an unopened supplement either way.

## Output format

```text
[Supplement audit] ship-ready / issues
[Placement violations] decision-critical content found in supplement: <list or none>
[Video] clips indexed · failures included · metadata stripped
[Pointer check] body references resolving: <n/m>
[Anonymity] clean / leaks: <locations>
[Size] archive size vs current cap (cap 待核实)
```
