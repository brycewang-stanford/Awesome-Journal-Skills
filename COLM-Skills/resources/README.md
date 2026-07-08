# COLM Resources

Working materials behind the COLM skill pack. The `skills/` directory carries the
advice; this directory carries the evidence — verified sources, the venue's award
lineage, a rebuilt first page, and the LM-specific reproducibility tooling notes.

## Contents

| Resource | Use it to... |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Trace every COLM fact in the pack to a dated official source, see the access-method caveat, and read the explicit 待核实 list. |
| [`exemplars/library.md`](exemplars/library.md) | Study the eight Outstanding Papers of COLM's first two editions — the clearest signal of what this young venue celebrates — with venue-attribution guards. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | Watch a fictional leaderboard-style LLM-evaluation first page get rebuilt into COLM shape: phenomenon first, contamination addressed, models pinned, claims scoped. |
| [`external_tools.md`](external_tools.md) | Open the live official surfaces and run the five author-side verification passes. |
| [`code/README.md`](code/README.md) | Reach the shared ML-conference reproducibility kit and see the five LM-specific checks it cannot make for you. |

## Scope note

COLM publishes on OpenReview, not through the ACL Anthology or PMLR, and it is three
editions old — do not import ARR mechanics, PMLR forms, or mature-venue folklore.
Where a question is not answered by a dated source in the source map, the honest
answer is 待核实.

## Suggested route

1. **Route the project** with [`../skills/colm-topic-selection`](../skills/colm-topic-selection/SKILL.md),
   sanity-checked against the award lineage in [`exemplars/library.md`](exemplars/library.md).
2. **Build trustworthy evidence** with [`../skills/colm-experiments`](../skills/colm-experiments/SKILL.md),
   [`../skills/colm-reproducibility`](../skills/colm-reproducibility/SKILL.md), and the checks in
   [`code/README.md`](code/README.md).
3. **Write and package** against [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md),
   then verify policy in [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before upload.
