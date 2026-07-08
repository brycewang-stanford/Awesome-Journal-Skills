# NDSS Resources

Working material that complements the twelve `skills/`. The skills advise; these files let an
agent check facts against recorded official sources, study verified NDSS papers, rebuild a
first page, and smoke-test an artifact package.

## Contents

| Resource | Purpose |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Eleven official sources with URLs and 2026-07-08 access dates, the verified 2027 cycle facts, the access-method note (direct fetches were blocked), and the explicit 待核实 list. |
| [`external_tools.md`](external_tools.md) | The live official surfaces plus six author-side verification passes (cycle, format, anonymity, ethics, cap, post-acceptance). |
| [`exemplars/library.md`](exemplars/library.md) | Five verified NDSS papers spanning 2005-2018 — two of them Test of Time winners — with self-check questions and a checked misattribution list. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | A fictional stale-delegation DNS paper's abstract and introduction, rebuilt before → after around adversary model, measurement discipline, and disclosure posture. |
| [`code/README.md`](code/README.md) | Adapter to the shared reproducibility kit plus the NDSS-specific hand checks (trace scrubbing, live-Internet snapshots, exploit gating, badge targeting). |

## What this pack is not

Not an econometrics pack (no Stata/DiD/IV tooling), and not a generic "top conference"
checklist: everything here assumes NDSS's own mechanics — two submission cycles, two-round
review with an early reject, Minor/Major Revision outcomes, an Ethics Review Board, and
free Internet Society proceedings.

## A sensible route through the material

1. Decide fit and cycle with
   [`../skills/ndss-topic-selection`](../skills/ndss-topic-selection/SKILL.md) and
   [`../skills/ndss-workflow`](../skills/ndss-workflow/SKILL.md), sanity-checking dates in
   [`official-source-map.md`](official-source-map.md).
2. Build evidence with [`../skills/ndss-experiments`](../skills/ndss-experiments/SKILL.md)
   and [`../skills/ndss-reproducibility`](../skills/ndss-reproducibility/SKILL.md), keeping
   [`code/README.md`](code/README.md) beside the repository.
3. Write against [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md)
   and the first pages of the papers in [`exemplars/library.md`](exemplars/library.md).
4. Before upload, run every pass in [`external_tools.md`](external_tools.md) against the
   live CFP — the 2027 cycle already proved that even NDSS's host city can change.
