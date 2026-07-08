---
name: cvpr-related-work
description: Use when building the related-work section and positioning for a CVPR paper, covering literature that moves at arXiv speed, concurrent-work etiquette, the CVPR/ICCV/ECCV sibling triangle, double-blind self-citation, verifying that cited "CVPR papers" are actually CVPR papers, and defining deltas against the true nearest neighbors.
---

# CVPR Related Work

At CVPR the related-work problem is not scarcity but velocity: the field's literature
updates weekly on arXiv, the venue itself accepted 4,090 papers in the 2026 edition
alone, and reviewers are drawn from a 25,000-person pool that includes the authors of
whatever you forgot to cite. Position precisely or be positioned by Reviewer 2.

## Five shelves to cover

| Shelf | What reviewers check | Failure smell |
|---|---|---|
| Canonical lineage | The 2–3 ancestors of your method family | Reinventing a 2019 module under a new name |
| Current SOTA | The methods atop your benchmark's leaderboard *now* | Comparing only against year-old baselines |
| Nearest neighbors | The 2–3 papers a hostile reviewer calls "the same" | No explicit delta stated |
| Cross-venue siblings | ICCV/ECCV/NeurIPS/WACV/3DV/SIGGRAPH work on the task | Treating CVPR citations as the whole field |
| Concurrent arXiv | Preprints within a few months of the deadline | Pretending they don't exist |

The nearest-neighbor shelf deserves half the section's words. For each: one sentence of
credit, one sentence of mechanism difference, one sentence of consequence ("because
[24] rebuilds the volume per frame, it cannot run online; we amortize it"). A delta
stated in mechanisms survives review; a delta stated in adjectives does not.

## Concurrent work, CVPR norms

With a November deadline and instant preprinting, collisions are routine. The working
etiquette: preprints appearing close to or after the deadline are *concurrent* — cite
them once you know of them, in a short "concurrent work" note, without being obligated
to outperform them. Two cautions. First, do not use concurrency as a shield for work
that predates your submission by months. Second, during the rebuttal you may be pointed
at a "missing comparison" that is actually concurrent — answer with dates, calmly, not
with indignation.

## Double-blind self-citation

CVPR requires citing your own lineage in the third person ("[12] proposed…"), never
omitting it — a hole where your prior paper should be identifies you as effectively as
a name. Because arXiv posting is legal during review (verified 2026 policy), reviewers
may suspect who you are; your job is only to avoid *confirming* it in the text:
no "our previous work [12]", no shared project-page naming, no acknowledgements.

## Cite the version of record, and verify the venue

Vision bibliographies rot in a specific way: a paper gets cited as "arXiv 2024" forever
after it appeared at CVPR 2025, or gets attributed to CVPR when it was ECCV (NeRF is
ECCV 2020; Mask R-CNN and Segment Anything are ICCV; ViT is ICLR). Before the deadline,
reconcile the .bib against dblp or the CVF open-access index:

```bash
# Bibliography hygiene pass
grep -c '@' refs.bib                                    # how big is the problem
grep -A2 'archivePrefix\|eprint' refs.bib | grep -B2 '20(1|2)[0-9]' | head
# → for each arXiv-only entry older than ~1 year, check dblp for the published venue
grep -in 'cvpr\|iccv\|eccv' refs.bib | awk -F: '{print $1}' | head
# → spot-check 5 random "CVPR" entries on openaccess.thecvf.com before trusting them
```

Fabricated or wrong citations carry venue-level risk: the verified 2026 author policy
makes citations of non-existent material grounds for rejection, without an LLM excuse.
Machine-suggested BibTeX gets the same verification as machine-written prose.

## A positioning paragraph that does its job

The shape worth copying — question, lanes, deltas, gap — in a fictional example:

> *How do prior trackers survive long occlusions?* Motion-memory methods [3, 17]
> extend Kalman gates over time, but the gate widens until identity switches dominate
> beyond ~30 frames. Re-identification banks [8, 24] match appearance on re-entry,
> yet require high-confidence detections that occlusion exits rarely produce. Query
> propagation [11] carries identity implicitly but only within the training clip
> length. None maintains identity through occlusions longer than the model's temporal
> horizon — the setting we target.

Four sentences, three lanes, each with a mechanism and a failure, ending in the gap
the paper fills. A reviewer can disagree with the gap, but cannot say the authors
don't know the field — which is the section's actual job.

## Sizing and placement

Related work at CVPR is conventionally ~0.5–0.75 of the 8 inclusive pages, either as
Section 2 or woven into the intro when space is desperate. Organize by *question*
("How do prior methods obtain temporal consistency?") rather than by laundry-listed
subfield headers; end each paragraph with the sentence that turns the survey into an
argument: what remains unsolved that your method solves.

## Positioning under fire: rebuttal-time related work

Related work re-opens in January. When a review says "not novel, see [X]":

- If [X] genuinely differs, answer with the mechanism delta in two sentences —
  never with "we are the first," which invites counterexamples.
- If [X] is concurrent (post-deadline or within the courtesy window), say so with
  dates and offer a camera-ready citation.
- If [X] actually anticipates you, the honest play is scoping the claim down in the
  rebuttal rather than defending the indefensible; ACs read the exchange, and a
  calibrated concession on novelty can coexist with acceptance when the execution
  and analysis carry weight.
- If [X] does not exist (LLM-flavored reviews hallucinate citations too), report it
  to the AC via the confidential channel with your search evidence — see
  `cvpr-review-process`.

## Reverify each cycle

- The current cycle's guidance to reviewers about very recent/concurrent work (the
  courtesy window is convention, not published law — treat cut-off claims as 待核实).
- Whether citation-format rules changed in the author kit.
- Leaderboard state on your benchmarks in the month before the deadline — SOTA claims
  age in weeks at this venue.
- The venue's own accepted-paper lists (CVF open access posts them around the
  conference) for late-breaking nearest neighbors your reviewers will have seen.

## Output format

```text
[Coverage] shelves complete: lineage / SOTA / neighbors / cross-venue / concurrent
[Nearest neighbors] <paper → mechanism delta → consequence> ×3
[Concurrent notes] <preprints + dates>
[Self-citation] third-person clean: yes/no
[Bib hygiene] arXiv-only entries checked: <n>; venue misattributions fixed: <n>
[Gaps] <missing comparisons a reviewer will name>
```
