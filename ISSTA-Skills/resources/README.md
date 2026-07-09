# ISSTA Resources

The working material behind the ISSTA skill pack. The `skills/` directory says what to do; this
directory holds what that advice stands on — verified official sources, award-certified exemplar
papers, a worked first-page rewrite for a testing paper, and pointers to reusable
package-checking tooling.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Trace every 2026-cycle fact (the single January deadline, the 18-page box, the Major-Revision phase, the ACM badge set) to its official URL and access date, and see what remains 待核实. |
| [`external_tools.md`](external_tools.md) | Open the live conf.researchr.org / HotCRP / ACM DL / Zenodo surfaces and run the author-side verification passes, starting with the submission-model check. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against archival-verified ISSTA papers — Impact-Paper-Award winners across several contribution shapes — and avoid mistaking a sibling-venue paper for an ISSTA one. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | Watch a fictional flaky-test-detection paper's opening get rebuilt against the ISSTA evaluation criteria, move by move. |
| [`code/README.md`](code/README.md) | Reach the shared replication-package tooling plus the ISSTA-specific checks (badge readiness, benchmark provenance, non-determinism disclosure) the generic kit cannot make. |

## Scope note

Everything here assumes a testing-and-analysis contribution: a technique that finds, characterizes,
or reasons about program behaviour, judged on real subjects. That evidence culture — bug-finding
metrics with ground truth, tool baselines run at an equal budget, non-parametric comparison with
effect sizes, and a runnable ACM-badged artifact — is neither an ML leaderboard nor a journal
editorial board. Two anti-patterns to keep out: an econometrics Stata/DiD workflow, and a
benchmark-score ranking framing. And remember that ISSTA rewrites its own rules — the submission
model above all — every edition, so no scaffolding here is permanent.

## Suggested route through the pack

1. **Fit first:** [`../skills/issta-topic-selection`](../skills/issta-topic-selection/SKILL.md)
   with the exemplars library open beside it — routing between ISSTA and ICSE/FSE/ASE is cheapest
   before any writing exists.
2. **Design the evidence:** [`../skills/issta-experiments`](../skills/issta-experiments/SKILL.md)
   and [`../skills/issta-reproducibility`](../skills/issta-reproducibility/SKILL.md), with
   [`code/README.md`](code/README.md) for package smoke checks — benchmark and subject choices
   fixed at design time cannot be second-guessed at rebuttal.
3. **Write and package:** [`../skills/issta-writing-style`](../skills/issta-writing-style/SKILL.md)
   against the worked example, then
   [`../skills/issta-supplementary`](../skills/issta-supplementary/SKILL.md) for the 18-page /
   artifact split and [`../skills/issta-submission`](../skills/issta-submission/SKILL.md) for the
   HotCRP audit.
4. **Verify last:** reopen everything in
   [`official-source-map.md`](official-source-map.md) — the 2026 snapshot ages by design, and the
   submission model is the first thing to re-check.
