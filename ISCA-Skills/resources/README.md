# ISCA Resources

Ground truth and working material for the ISCA skill pack. The `skills/`
directory carries the advice; this directory carries what the advice rests on —
the verified official-source trail, award-anchored exemplar papers, a worked
first-page rewrite for an architecture paper, and the bridge to shared
reproducibility tooling.

## Contents

| Resource | Use it to... |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Trace every 2026-cycle ISCA fact (deadlines, 11-page rule, blinding rules, AE arrangement, sponsorship) to a URL and access date, and see exactly what remains 待核实 — including everything about ISCA 2027. |
| [`external_tools.md`](external_tools.md) | Open the live official surfaces (iscaconf.org, HotCRP, SIGARCH/TCCA postings, ACM DL/dblp) and run the author-side verification passes before upload. |
| [`exemplars/library.md`](exemplars/library.md) | Study six Influential-ISCA-Paper-Award-verified papers as contribution shapes — what the venue's own long-run judgment says an ISCA paper can be. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | Watch a fictional cache-hierarchy paper's abstract and introduction get rebuilt to the venue's bar: measured motivation, mechanism precision, calibrated claims. |
| [`code/README.md`](code/README.md) | Reach the shared ML-conference reproducibility kit and see which architecture-specific checks (simulator pinning, config manifests, hardware-state records) it cannot do for you. |

## Scope note

This is a computer-architecture conference pack. Its evidence culture —
simulator fidelity contracts, configuration archaeology, workload
representativeness, hardware cost accounting — is not the econometrics culture
of the journal packs (no Stata/DiD material belongs here) and not the
leaderboard culture of the deep-learning packs. Where tooling is shared, the
adapter in `code/README.md` says exactly what carries over and what does not.

## Suggested route

1. **Fit and calendar first:**
   [`../skills/isca-topic-selection`](../skills/isca-topic-selection/SKILL.md)
   and [`../skills/isca-workflow`](../skills/isca-workflow/SKILL.md), with the
   exemplars library open for calibration.
2. **Evidence:** [`../skills/isca-experiments`](../skills/isca-experiments/SKILL.md)
   plus [`../skills/isca-reproducibility`](../skills/isca-reproducibility/SKILL.md),
   wiring manifests in from day one.
3. **Prose and packaging:**
   [`../skills/isca-writing-style`](../skills/isca-writing-style/SKILL.md)
   against the worked example, then
   [`../skills/isca-related-work`](../skills/isca-related-work/SKILL.md),
   [`../skills/isca-supplementary`](../skills/isca-supplementary/SKILL.md), and
   [`../skills/isca-submission`](../skills/isca-submission/SKILL.md).
4. **Verify last:** everything in [`official-source-map.md`](official-source-map.md)
   is a dated snapshot; the ISCA 2027 pages, once live, override this pack on
   contact.
