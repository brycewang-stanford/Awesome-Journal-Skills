---
name: siggraph-writing-style
description: Use when structuring or revising a SIGGRAPH / TOG technical paper, covering the teaser figure, a results-first first page, the graphics contribution framing (technique + quality/performance), comparison-driven evaluation, honest limitations, and the acmart 7-page discipline for the conference track.
---

# SIGGRAPH Writing Style

A SIGGRAPH paper earns acceptance by making a **graphics contribution** legible on the first page
and **showing** its results, not merely describing them. The reader is a domain expert who will
form an opinion from your **teaser figure and results video** before finishing the abstract. This
skill builds the SIGGRAPH first-page arc and the body discipline the `acmart` budget enforces.
Anchor format facts to `resources/official-source-map.md`.

## The SIGGRAPH first-page arc

**problem a graphics practitioner recognizes -> why prior methods fall short (quality, speed,
generality, or robustness) -> our technique in one sentence -> the result shown (teaser) -> what it
enables.** All of it visible on page one, with the **teaser figure** doing half the work.

- Lead with the *visual/temporal* problem: a rendering that is too slow or too noisy, a simulation
  that is unstable, a geometry operation that fails on real meshes. Not "deep learning has
  transformed graphics."
- State the contribution as a **method plus a measurable gain** — "Nx faster at equal quality,"
  "converges where prior work diverges," "handles inputs prior methods cannot." A method with no
  quality/performance axis to move is not yet a SIGGRAPH contribution.
- The **teaser** must show the best result on a recognizable case and, ideally, a side-by-side with
  the strongest baseline. It is the single most-read object in the paper.

## The teaser figure carries the paper

Spend disproportionate effort here:

- One glance should convey *what problem, what input, what output, how much better*.
- Prefer a real, hard scene over a toy; reviewers distrust teasers that only work on the easy case.
- If the contribution is temporal, the teaser points at the video ("see supplemental video") — but
  the still must still stand alone.

## Body structure (conference/dual-track: <= 7 pages)

A workable graphics-paper skeleton:

1. **Introduction** — the first-page arc above; contributions as a short bulleted list.
2. **Related work** — positioned by *what prior methods cannot do that you can* (see
   `siggraph-related-work`), not a chronological survey.
3. **Method** — the technique, with the math and algorithm a reader needs to reimplement; push
   long derivations to the supplemental appendix.
4. **Results** — comparisons, ablations, timings, and quality metrics (see `siggraph-experiments`),
   each figure earning its space against the page budget.
5. **Limitations** — honest failure cases, shown not hidden; this *builds* credibility here.
6. **Conclusion** — one paragraph; no over-signposting.

## Page-budget discipline (acmart)

- The conference-track body is **<= 7 pages excluding references and up to two figures-only pages**.
  Every figure competes with text for that space — cut a figure that does not change a reader's
  belief.
- Move derivations, parameter tables, and network architecture details to the supplemental
  appendix. The body carries the argument and the decisive results; the supplemental carries depth.
- Do not shrink fonts or edit the `acmart` class to recover space — that is a mechanical reject.
  Recover space by cutting, not by tampering.

## Voice and honesty

- **Show, then claim.** "Our method removes the flicker (Fig. 4, video 0:30)" beats "our method is
  temporally coherent." Graphics reviewers believe pixels, not adjectives.
- **Quantify every comparison** with a metric and equal conditions; a qualitative "looks better"
  invites the reviewer to disagree.
- **Name limitations before the reviewer does.** A shown failure case with an explanation is far
  stronger than a concealed one the reviewer discovers in your video.
- **Timings are claims** — report them with hardware, resolution, and settings, or do not make
  them.

## Anti-patterns

- A method paper with no comparison to the obvious prior work — the fastest path to reject.
- A teaser that only works on the easy input.
- Prose that describes results the figures/video do not actually show.
- Over-length body recovered by font/margin tampering.
- Limitations reduced to a boilerplate sentence, or omitted entirely.

## Output format

```text
[First page] graphics problem + inadequacy + technique + teaser + payoff all present? yes/no
[Teaser] shows best result on a recognizable case, ideally vs baseline? yes/no
[Contribution] method + measurable quality/performance gain stated? yes/no
[Body budget] conference-track <=7 pages, derivations moved to appendix? yes/no
[Honesty] comparisons quantified + limitations shown (not hidden)? yes/no
[Revision queue] <ordered>
```
