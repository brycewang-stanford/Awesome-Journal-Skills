# UIST Resources

Action-oriented material backing the UIST skill pack. The `skills/` directory advises;
this directory lets an agent model a UIST-shaped paper against verified exemplars, study
the systems-paper rhetoric on a concrete rewrite, and prepare the supplement and artifact
packages that a demo-culture venue expects.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Trace every UIST fact in the pack to a primary URL with its 2026-07-08 access date, including the access-method note and the explicit 待核实 list. |
| [`external_tools.md`](external_tools.md) | Open the live official surfaces (CFP, Author Guide, PCS, ACM DL, TAPS) and run the five author-side verification passes. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against six DL/dblp-verified UIST papers, 2000-2023, four carrying the Lasting Impact Award — the venue's own definition of its contribution bar. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | Watch a fictional haptics-glove abstract and introduction rebuilt from motivation-essay shape into the UIST capability → mechanism → evidence arc. |
| [`code/README.md`](code/README.md) | Adapt the shared ML-conference reproducibility kit, plus the five UIST-specific passes (video spec, hardware reconstruction, measurement protocols) it cannot run. |

## Scope note

This is an interface-systems conference pack. The evidence objects here are running
systems, video figures, hardware design files, and technical characterizations — not
regression tables. Do not import the econometrics kit; use the shared ML-conference kit
only for the learned components and archive hygiene, as scoped in
[`code/README.md`](code/README.md).

## Suggested route

1. **Route first**: [`../skills/uist-topic-selection`](../skills/uist-topic-selection/SKILL.md)
   for the artifact-subtraction test and the explicit CHI-vs-UIST call, calibrated against
   [`exemplars/library.md`](exemplars/library.md).
2. **Plan evidence and calendar**:
   [`../skills/uist-experiments`](../skills/uist-experiments/SKILL.md) +
   [`../skills/uist-workflow`](../skills/uist-workflow/SKILL.md), with
   [`../skills/uist-reproducibility`](../skills/uist-reproducibility/SKILL.md) ledgers
   installed at build time.
3. **Write and film**: [`../skills/uist-writing-style`](../skills/uist-writing-style/SKILL.md)
   against the worked example;
   [`../skills/uist-supplementary`](../skills/uist-supplementary/SKILL.md) for the video.
4. **Verify and submit**: current-cycle rules via
   [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md), then
   [`../skills/uist-submission`](../skills/uist-submission/SKILL.md) end to end.
