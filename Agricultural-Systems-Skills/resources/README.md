# Agricultural Systems Resources

Action-oriented resources for the *Agricultural Systems* (AgSy) skill pack (Elsevier; ISSN 0308-521X /
1873-2267). The `skills/` give advice; this directory lets an agent **model a venue-shaped section** and
**benchmark against verified exemplars**. Pair each with the relevant `skills/agsy-*/SKILL.md`.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of an *Agricultural Systems* **abstract + introduction** in AgSy house style — systems framing, an independently **evaluated** model, and **trade-offs across the farming system**. Illustrative **fictional** paper; no real policy invented. Derived only from this pack's own skill files. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified** *Agricultural Systems* papers (DOI `10.1016/j.agsy...`) organized by topic × method. Design positioning only — no fabricated numbers; includes a sibling-confusion guard and documented omissions. |
| [`official-source-map.md`](official-source-map.md) | **AgSy-specific policy & facts:** Elsevier/ScienceDirect home and Guide for Authors, aims & scope (interactions across hierarchical levels), single-anonymized review, article types/front matter, APC/subscription route, and the Option C research-data policy (data **and** code/models). The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | Systems models by scale (process/whole-farm/bio-economic/ABM/integrated-assessment), calibration / sensitivity / uncertainty and multi-objective software, data sources, and reproducibility tooling. |

## No econometrics code kit is vendored

Unlike some economics packs in this repository, **this pack does not vendor a causal-inference / Stata
code kit** — that kit is the wrong tool for an *Agricultural Systems* submission. AgSy is a
**systems-science** journal: a paper analyzes interactions, trade-offs, and emergent behaviour across the
field → farm → landscape → region → food-system levels through **integrated process, whole-farm,
bio-economic, agent-based, or integrated-assessment modelling**. The discipline-appropriate tooling
(APSIM/DSSAT/STICS, FarmDESIGN/MIDAS, GAMS/Pyomo, NetLogo/Mesa, plus calibration, sensitivity,
uncertainty, and multi-objective packages) is catalogued in
[`external_tools.md`](external_tools.md), not duplicated here as runnable code.

## Suggested workflow

1. **Scope and frame** with [`../skills/agsy-topic-selection`](../skills/agsy-topic-selection/SKILL.md)
   and [`../skills/agsy-systems-framing-and-modeling`](../skills/agsy-systems-framing-and-modeling/SKILL.md);
   model the abstract + intro on
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
2. **Choose and evaluate the model** with
   [`../skills/agsy-data-and-model-evaluation`](../skills/agsy-data-and-model-evaluation/SKILL.md),
   selecting tooling from [`external_tools.md`](external_tools.md) (independent observed-vs-simulated fit,
   sensitivity, uncertainty, trade-off/scenario analysis).
3. **Surface implications** with
   [`../skills/agsy-impact-and-implications`](../skills/agsy-impact-and-implications/SKILL.md) — name the
   decision and the trade-off, scoped to the system you modelled.
4. **Polish and prepare front matter** with
   [`../skills/agsy-writing-style`](../skills/agsy-writing-style/SKILL.md) (abstract ≤ 250 words,
   Highlights, graphical abstract).
5. **Benchmark** against verified papers in [`exemplars/library.md`](exemplars/library.md); confirm
   submission, review, and data/model policy in
   [`official-source-map.md`](official-source-map.md).
