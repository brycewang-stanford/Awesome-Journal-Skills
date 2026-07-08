# STOC Resources

Action-oriented companions to the STOC skill pack. The `skills/` directory gives
venue advice; this directory lets an agent see the advice executed — a rebuilt
first page, dblp-verified exemplar papers, the exact official-source trail, and
the handful of code checks that make sense at a proofs-first venue.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | Watch a journal-style opening get rebuilt into a STOC first page: result, lineage, barrier, technique, consequences. Fully fictional; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Calibrate "STOC-scale" against five dblp/ACM-verified STOC papers across eras, with a STOC-vs-FOCS misattribution guard. |
| [`official-source-map.md`](official-source-map.md) | Trace every 2026-cycle fact to its official URL, see the access-method note, and read the explicit 待核实 list. |
| [`external_tools.md`](external_tools.md) | Open the official surfaces (acm-stoc.org, HotCRP, SIGACT, ACM DL, arXiv/ECCC, dblp) and run the six author-side verification passes. |
| [`code/README.md`](code/README.md) | Apply the few shared-kit tools that survive contact with a no-artifact-track venue, plus STOC-native grep/diff/tarball checks. |

## Scope note

This is a theoretical-computer-science conference pack. There is no experiment
matrix to fill, no seed table to report, and no artifact badge to chase; the
evidence objects are theorem statements, proofs, the public full version, and —
only when a proof genuinely depends on computation — a certificate with an
independent checker. Resist importing empirical-venue scaffolding.

## Suggested route

1. Decide fit with
   [`../skills/stoc-topic-selection`](../skills/stoc-topic-selection/SKILL.md),
   calibrating against [`exemplars/library.md`](exemplars/library.md).
2. Build the paper with
   [`../skills/stoc-writing-style`](../skills/stoc-writing-style/SKILL.md) and
   [`../skills/stoc-supplementary`](../skills/stoc-supplementary/SKILL.md),
   holding the draft against
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
3. Verify claims and versions with
   [`../skills/stoc-reproducibility`](../skills/stoc-reproducibility/SKILL.md)
   and the checks in [`code/README.md`](code/README.md).
4. Before upload, confirm the current cycle's rules through
   [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md), then run
   [`../skills/stoc-submission`](../skills/stoc-submission/SKILL.md) end to end.
