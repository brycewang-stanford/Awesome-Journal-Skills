# EPSL Resources

Action-oriented material backing the Earth and Planetary Science Letters (EPSL) skill pack. The
`skills/` directory advises; this directory lets an agent **act** — model a letters-format abstract
and introduction, benchmark against landmark EPSL papers, and confirm policy against official
sources. Pair each item with the matching `skills/epsl-*/SKILL.md`.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | Study a before→after rewrite of an **abstract + introduction** into EPSL house style — process-forward framing, the headline number with a defined uncertainty, cross-disciplinary legibility, and letters-format economy. The paper and all numbers are **fictional**. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **landmark EPSL papers** (Watson & Harrison's zircon-saturation calibration, Hofmann's crust–mantle differentiation framework, Lal's cosmogenic-nuclide foundation, and more), organized by sub-field, each with a self-check question and a verification note. |
| [`official-source-map.md`](official-source-map.md) | The **EPSL-specific policy facts**: Elsevier journal home, Guide for Authors, Editorial Manager entry, letters length, data-policy links — with the official URL behind each fact and "re-check" flags on volatile items. The pack's authority file. |
| [`external_tools.md`](external_tools.md) | The tooling the pack's skills reference — EarthChem/PANGAEA/IRIS/MagIC/PDS repositories, GMT/PyGMT and GPlates, ObsPy, isotope and geochronology reduction software, geodynamic and phase-equilibrium codes. |

## Scope note: no econometrics code kit vendored

EPSL is a solid-Earth and planetary science journal (Elsevier). The shared causal-inference /
econometrics code kit that ships with this repository's economics packs (Stata + Python DID/IV/RDD
pipelines) is **deliberately not vendored here** — it has no purchase on isotope systematics,
seismic inversion, or geodynamic modeling. The discipline-appropriate rigor for EPSL lives in
[`../skills`](../skills/): traceable analytical campaigns
([`epsl-study-design`](../skills/epsl-study-design/SKILL.md)), complete uncertainty budgets
([`epsl-data-analysis`](../skills/epsl-data-analysis/SKILL.md)), and FAIR deposition
([`epsl-reporting-and-reproducibility`](../skills/epsl-reporting-and-reproducibility/SKILL.md)),
with the software index in [`external_tools.md`](external_tools.md).

## Suggested workflow

1. Frame the contribution with
   [`../skills/epsl-topic-selection`](../skills/epsl-topic-selection/SKILL.md) (the process-level
   test) and shape the prose with
   [`../skills/epsl-writing-style`](../skills/epsl-writing-style/SKILL.md), modeling the opening on
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
2. Build the evidentiary chain with
   [`../skills/epsl-study-design`](../skills/epsl-study-design/SKILL.md) (context, traceability,
   discrimination) and [`../skills/epsl-data-analysis`](../skills/epsl-data-analysis/SKILL.md)
   (uncertainty ladders, MSWD, resolution tests); compose the exhibits with
   [`../skills/epsl-figures-and-tables`](../skills/epsl-figures-and-tables/SKILL.md).
3. Benchmark against the sub-field-matched paper in
   [`exemplars/library.md`](exemplars/library.md) and ask its self-check question of your own draft.
4. Confirm length, statements, and portal mechanics in
   [`official-source-map.md`](official-source-map.md); tool up from
   [`external_tools.md`](external_tools.md); preflight with
   [`../skills/epsl-submission`](../skills/epsl-submission/SKILL.md).
