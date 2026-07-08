# UAI Resources

Working material behind the UAI skill pack. The `skills/` directory tells an agent what
to do; this directory holds what the advice stands on — verified official sources, real
exemplar papers, a worked first-page rewrite, and pointers to reusable reproducibility
tooling.

## Contents

| Resource | Use it to... |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Trace every 2026-cycle fact (dates, caps, criteria, PMLR volumes) to its official URL and access date, and see exactly which items remain 待核实. |
| [`external_tools.md`](external_tools.md) | Open the live AUAI/OpenReview/PMLR surfaces and run the five author-side verification passes before upload. |
| [`exemplars/library.md`](exemplars/library.md) | Position against metadata-verified UAI papers across five lanes (Monte Carlo, causal estimation, conformal, discovery, applied BDL) without misattributing sibling PMLR venues. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | Watch a fictional causal-discovery opening get rebuilt to UAI's four review criteria, move by move. |
| [`code/README.md`](code/README.md) | Reach the shared ML-conference reproducibility kit and the UAI-specific checks the generic tooling cannot do. |

## Scope note

This is a probabilistic-AI conference pack. The evidence culture it encodes — labeled
assumptions, sampler diagnostics, coverage measurement, structure-recovery metrics —
differs from both the econometrics journal packs (no Stata/DiD kit here) and the
general deep-learning conference packs (leaderboard wins are not the endpoint here).

## Suggested route through the pack

1. **Fit first:** [`../skills/uai-topic-selection`](../skills/uai-topic-selection/SKILL.md)
   with the exemplars library open beside it.
2. **Build evidence:** [`../skills/uai-experiments`](../skills/uai-experiments/SKILL.md)
   and [`../skills/uai-reproducibility`](../skills/uai-reproducibility/SKILL.md), using
   [`code/README.md`](code/README.md) for artifact smoke checks.
3. **Write and package:** [`../skills/uai-writing-style`](../skills/uai-writing-style/SKILL.md)
   against the worked example, then
   [`../skills/uai-supplementary`](../skills/uai-supplementary/SKILL.md) and
   [`../skills/uai-submission`](../skills/uai-submission/SKILL.md).
4. **Verify last:** reopen everything in [`official-source-map.md`](official-source-map.md)
   and [`external_tools.md`](external_tools.md) — the 2026 snapshot in this pack ages
   by design.
