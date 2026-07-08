---
name: iccv-related-work
description: Use when positioning an ICCV paper against the literature, covering the intervening-cycle problem of citing a CVPR and an ECCV that happened since the last ICCV, concurrent-preprint etiquette around the March deadline, double-blind self-reference and the do-not-cite-your-repo rule, and venue-attribution hygiene across the vision big three.
---

# ICCV Related Work

Positioning at ICCV has a built-in time-lapse problem: between one ICCV and the
next, a full CVPR cycle and a full ECCV cycle (and usually a second CVPR) have
deposited their papers. Your related-work section is judged on whether it
metabolized *those*, not on whether it knows the classics. This skill organizes
the section around that clock.

## The intervening-cycle sweep

Before writing a word, sweep the venues that published since the last ICCV in
your area, newest first:

```text
sweep order for an ICCV 2027 submission (deadline 待核实, ~early 2027)
  1. CVPR 2026 proceedings + late-2026 arXiv        ← your reviewers' own papers
  2. ECCV 2026 proceedings
  3. ICCV 2025 proceedings                          ← the venue's own last word
  4. CVPR 2025
  5. journals/others (TPAMI, IJCV, NeurIPS) same window
  6. classics that define the problem (pre-window)
```

The most common positioning failure at biennial venues is a related-work section
written when the project started — 18 months stale by the deadline. Diff your
.bib's newest entry date against the deadline; a gap over ~4 months means the
sweep never re-ran.

## Nearest neighbors get the words

Reviewers do not need coverage; they need to see that you know which two or
three papers a skeptic would call equivalent, and why they are not. For each
nearest neighbor spend three sentences: what it does (credit, accurately), where
the mechanisms diverge (the actual delta), and what the divergence costs or buys
(the consequence). Divergence stated as adjectives ("more efficient and more
general") is what draws the "limited novelty" review; divergence stated as
mechanism ("[31] fuses at the feature level and therefore needs paired data; we
fuse at the loss level and train unpaired") is what preempts it.

## Concurrency at a March deadline

The weeks before an ICCV deadline coincide with the post-CVPR-decision preprint
wave (CVPR decisions land in February), so collisions are structural, not bad
luck. Working norms:

| Situation | Handling |
|---|---|
| Preprint appeared within ~2 months of the deadline | Cite as concurrent in a short note; no obligation to outperform |
| Preprint predates your submission by a season | It is prior work; compare properly or scope your claim |
| Reviewer cites a "missing baseline" that is concurrent | Rebuttal answers with dates, one calm sentence |
| Your own preprint is on arXiv | Legal at ICCV (2025 policy: arXiv posting is not an anonymity violation); do not cite it as yours |
| A concurrent paper *supersedes* yours before the deadline | The honest move is repositioning before submission, not hoping reviewers missed it — they wrote it |

## Double-blind reference mechanics

ICCV's 2025 anonymity guidance has one wrinkle beyond standard third-person
self-citation: **do not cite your public codebase** — say code "will be made
publicly available" instead of linking a repo that names your lab. The standard
rules still apply on top: prior work of yours is "[17] showed", never "our
earlier work"; no acknowledgements; no grant IDs; and no citation *hole* where
your obvious prior paper should be, because an expert reviewer reads the gap as
a signature.

## Venue attribution: the big-three trap

Vision citations rot toward the wrong sibling, and ICCV papers misattributed to
CVPR (or vice versa) appear in published bibliographies every cycle. Ground
truth for the confusable landmarks:

- **Actually ICCV**: SIFT's conference debut (Lowe, ICCV 1999), Mask R-CNN
  (2017, Marr Prize), CycleGAN (2017), Swin Transformer (2021, Marr Prize),
  ControlNet (2023, Marr Prize), Segment Anything (2023).
- **Not ICCV**: ResNet and YOLO (CVPR), NeRF (ECCV 2020), ViT (ICLR),
  Faster R-CNN (NeurIPS), U-Net (MICCAI), latent diffusion / Stable Diffusion's
  paper (CVPR 2022).

Mechanical hygiene before the deadline:

```bash
# .bib venue hygiene, ten minutes
grep -c '@' main.bib
grep -B1 -iE 'journal.*arxiv|eprint' main.bib | grep -iE 'year.*20(1[0-9]|2[0-3])' | head
#   → old arXiv-only entries: check dblp for the published venue and upgrade
grep -iE 'booktitle.*(ICCV|CVPR|ECCV)' main.bib | sort | uniq -c
#   → spot-check 5 entries per venue against dblp / CVF open access
```

Wrong venues signal carelessness; citations to papers that do not exist are far
worse — under CVF-family policy, fabricated references (a known failure of
machine-drafted bibliographies) can sink the paper regardless of who typed them.

## Organize by question, close with the gap

Structure the section as the two or three questions the field has been asking,
not as a tour of research groups. Each paragraph: the question, the families of
answers with their mechanisms and limits, and a closing sentence that names what
remains unsolved — which must be exactly what your paper solves. A reviewer
should be able to read only the final sentence of each paragraph and
reconstruct your claim's coordinates. If the last ICCV's own papers appear
nowhere in this story, either the sweep failed or the venue is wrong — reviewers
notice when a submission ignores the conference's own lineage.

## Positioning against the two-year echo

A subtlety unique to the cadence: work you compare against from ICCV 2025 has
had two years of follow-ups by the 2027 deadline. Compare against the *current
best version* of an idea (often a CVPR/ECCV successor), while citing the ICCV
original for the idea itself. Beating a two-year-old implementation of a living
research line is the polite version of a strawman, and the line's authors are in
the reviewer pool.

## Reverify each cycle

- The current cycle's anonymity/self-citation wording, including the repo
  clause.
- Concurrent-work courtesy conventions (custom, not codified — treat any hard
  cutoff you read as 待核实).
- Accepted-paper lists of the newest CVPR/ECCV before the deadline, for
  last-moment neighbors.

## Output format

```text
[Sweep freshness] newest .bib entry vs deadline: <gap>; intervening cycles covered: CVPR/ECCV/ICCV
[Nearest neighbors] <paper → mechanism delta → consequence> ×2-3
[Concurrent notes] <preprints + dates + handling>
[Self-reference] third person clean · repo uncited · no citation holes
[Attribution check] entries verified against dblp/CVF: <n>
[Gap sentence] <the one-sentence unsolved thing the paper solves>
```
