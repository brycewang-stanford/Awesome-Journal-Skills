---
name: siggraph-topic-selection
description: Use before committing a project to SIGGRAPH / SIGGRAPH Asia / TOG, to decide whether the contribution is graphics-shaped and which venue and track fit, routing among SIGGRAPH, SIGGRAPH Asia, direct-to-TOG, and siblings (CVPR/ICCV, CHI/UIST, Eurographics/EGSR/SGP/SCA/HPG/I3D), and whether to aim dual-track or Journal-only.
---

# SIGGRAPH Topic Selection

Choosing SIGGRAPH — and the right cycle and track — before you write is a high-leverage decision,
because SIGGRAPH's bar is a **graphics contribution shown through results**, and several sibling
venues will serve a differently-shaped contribution better. This skill routes the project. Anchor
venue facts to `resources/official-source-map.md`.

## Is it a graphics contribution?

SIGGRAPH rewards work that advances how images, geometry, motion, or interactive experiences are
**created, simulated, rendered, captured, or fabricated** — and demonstrates it on results a
graphics audience can *see*. Apply three tests:

1. **The visual/temporal-result test.** Can the contribution be shown as an image, mesh, frame
   sequence, or interactive demo that a graphics reviewer judges by eye? If the payoff is a table
   of accuracy numbers with nothing to show, it is likely a vision or ML paper.
2. **The capability-axis test.** Does it move a graphics axis — quality, speed, generality,
   robustness, controllability? If there is no such axis, the contribution is not yet SIGGRAPH-shaped.
3. **The method-vs-application test.** Is the advance a reusable technique, or an application of an
   existing method to a new dataset? The latter routes to a domain venue or a shorter track.

## Route the project

| If the contribution is... | Consider | Why not SIGGRAPH main |
|---|---|---|
| A graphics technique with strong visual results | **SIGGRAPH / SIGGRAPH Asia Technical Papers (TOG)** | This is the target |
| Rendering-specific, incremental but solid | EGSR or HPG (and TOG) | Better-matched reviewers; faster cycle |
| Geometry-processing-specific | SGP (and TOG/CGF) | Specialized geometry audience |
| Animation / physical simulation focused | SCA (and TOG) | Sub-community venue |
| Interactive/real-time rendering technique | I3D or HPG | Real-time-focused reviewers |
| Recognition/reconstruction where the *model* is the point | CVPR / ICCV / ECCV | A vision contribution, not a graphics one |
| Interaction/UI/hardware where usability is the point | CHI / UIST | An HCI contribution |
| A mature, comprehensive result with no conference talk needed | **Direct-to-TOG (rolling)** | Journal-only, off-cycle |
| Early-stage but promising graphics idea | SIGGRAPH **Conference track** (dual-track) or Technical Communications | Lighter validation bar |

The neural-rendering / generative-3D overlap with CVPR is the most common routing decision: if the
lesson survives swapping the network (a graphics capability), aim SIGGRAPH; if the network *is* the
contribution and the graphics is a testbed, aim a vision venue.

## Choose the cycle

- **SIGGRAPH (North America), ~January deadline, summer conference** vs **SIGGRAPH Asia, ~May
  deadline, December conference.** Same TOG journal outcome, same review model — pick by which
  deadline your results can *finish* to the journal bar, and by conference travel.
- A near-miss at one cycle is naturally revised for the next; do not rush an unfinished paper into
  the nearer deadline.
- **Direct-to-TOG** (rolling, ScholarOne) suits a comprehensive journal paper that does not need a
  conference talk; most authors still go through the conference cycle for the presentation and
  visibility.

## Choose the track

- **Dual-track** (default): eligible for Journal (TOG) or Conference publication; keeps the
  lighter-validation Conference outcome available for riskier/earlier-stage work. The committee
  assigns the final track — you cannot appeal it (see `siggraph-review-process`).
- **Journal-only:** choose when a Conference-track publication would not serve a mature, complete
  result. This forgoes the lighter-validation safety net.
- You do not choose *between* journal and conference reviewers — there is one review on one scale;
  the track is decided at accept time.

## Honest self-check before committing

- Do I have a **results video and head-to-head comparisons** against the strongest prior method, or
  can I produce them by the deadline? Without them, SIGGRAPH is a long shot.
- Is the closest prior work at SIGGRAPH, or at Eurographics/EGSR/SGP/SCA/CVPR? Submit where your
  reviewers and canon live.
- Is the contribution a **reusable technique** or a one-off result? The former is SIGGRAPH-shaped.

## Output format

```text
[Graphics-shaped?] visual-result / capability-axis / method-vs-application tests: pass/fail
[Venue] SIGGRAPH / SIGGRAPH Asia / TOG-direct / sibling (name it) + why
[Cycle] which deadline the results can credibly finish to
[Track] dual-track / journal-only + rationale
[Readiness] results video + strongest-baseline comparison in hand or schedulable? yes/no
[Route decision] <one line + next skill to invoke>
```
