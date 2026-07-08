# NSDI Resources

Working materials that back the `skills/` directory: verified sources, real exemplar
papers, a style rewrite, and a reproducibility adapter. The skills tell an agent what
to do; these files hold the evidence and the checkable references.

## Contents

| Resource | Use it to... |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Trace every venue fact in the pack to a dated official URL, see the access-method note (usenix.org and dblp.org 403'd direct fetches), and read the explicit 待核实 list. |
| [`external_tools.md`](external_tools.md) | Open the live NSDI surfaces (CFP, HotCRP `/deadlines`, artifact call) and run the five author-side verification passes. |
| [`exemplars/library.md`](exemplars/library.md) | Position against five venue-verified NSDI papers (2007-2020) and dodge the Raft/B4/Chord/Spanner/Tor misattribution traps. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | Watch a fictional RPC-retry paper's abstract and introduction get rebuilt into the NSDI operational-evidence arc. |
| [`code/README.md`](code/README.md) | Reach the shared reproducibility kit and see which NSDI-specific artifact properties (topology, traces, timing variance) it cannot check. |

## Scope note

This is a networked-systems conference pack. Evidence here means traces, testbeds, and
deployments — not regression tables. Do not import econometrics tooling from the
journal packs; the shared ML/systems kit under `shared-resources/` is the right base,
with the NSDI-specific gaps listed in [`code/README.md`](code/README.md).

## A suggested route through the pack

1. **Fit first:** [`../skills/nsdi-topic-selection`](../skills/nsdi-topic-selection/SKILL.md)
   against the CFP scope, then compare your plan with
   [`exemplars/library.md`](exemplars/library.md).
2. **Calendar next:** [`../skills/nsdi-workflow`](../skills/nsdi-workflow/SKILL.md) —
   the spring/fall pair changes which deadline you are actually writing for.
3. **Build the evidence:** [`../skills/nsdi-experiments`](../skills/nsdi-experiments/SKILL.md)
   plus [`../skills/nsdi-reproducibility`](../skills/nsdi-reproducibility/SKILL.md) and
   the [`code/README.md`](code/README.md) adapter while experiments still run.
4. **Write and audit:** [`../skills/nsdi-writing-style`](../skills/nsdi-writing-style/SKILL.md)
   with [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md),
   then [`../skills/nsdi-submission`](../skills/nsdi-submission/SKILL.md) against
   [`external_tools.md`](external_tools.md) before upload.
5. **After the decision:** [`../skills/nsdi-author-response`](../skills/nsdi-author-response/SKILL.md)
   if the letter says one-shot revision;
   [`../skills/nsdi-artifact-evaluation`](../skills/nsdi-artifact-evaluation/SKILL.md)
   and [`../skills/nsdi-camera-ready`](../skills/nsdi-camera-ready/SKILL.md) if it says
   accept.
