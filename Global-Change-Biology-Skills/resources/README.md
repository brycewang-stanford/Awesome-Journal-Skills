# GCB Resources

Action-oriented resources for the *Global Change Biology* (GCB) skill pack. The `skills/` give advice;
this directory lets an agent **act** — model a GCB-style abstract + introduction, benchmark against
verified exemplars, and confirm journal policy. Pair these with the relevant `skills/gcb-*/SKILL.md`.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a paper **abstract + introduction** in GCB house style (global-change driver → biological response → mechanism, quantified, significance early). Illustrative **fictional** paper, derived only from this pack's skills. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified GCB papers** (Wiley; DOI `10.1111/gcb...`) organized by method × topic. Design positioning only — no fabricated numbers; includes a sibling-confusion guard and documented omissions. |
| [`official-source-map.md`](official-source-map.md) | **GCB-specific policy & facts:** ScholarOne submission, Wiley data/code-DOI archiving policy, aims-and-scope (molecular-to-biome, aquatic/terrestrial), article types, and live-check notes for volatile caps. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | Global-change **data sources** (climate, flux, biodiversity, traits), R/Python and process-model toolchains, design/synthesis/uncertainty practice, and repositories. |

## Discipline note: no econometric code kit vendored

This is an **environmental-science venue**. Unlike the economics packs, the cross-pack econometrics /
causal-inference code kit (Stata + Python DID/IV/RDD/DML pipeline) is **intentionally not vendored**
here — it is the wrong toolchain for global-change biology. The methods GCB actually rewards (mixed /
hierarchical models, meta-analysis effect sizes, spatial / time-series analysis, and process-model
ensembles with partitioned uncertainty) are pointed to in
[`external_tools.md`](external_tools.md) (R `lme4`/`glmmTMB`/`brms`/`metafor`, Python `xarray`/`terra`
geospatial stack, DGVM / land-surface models) and governed by the analysis norms in
[`../skills/gcb-data-analysis/SKILL.md`](../skills/gcb-data-analysis/SKILL.md).

## Suggested workflow

1. Scope and frame with [`../skills/gcb-topic-selection`](../skills/gcb-topic-selection/SKILL.md) and
   [`../skills/gcb-writing-style`](../skills/gcb-writing-style/SKILL.md); model the abstract + intro on
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
2. Design and analyze with [`../skills/gcb-study-design`](../skills/gcb-study-design/SKILL.md) and
   [`../skills/gcb-data-analysis`](../skills/gcb-data-analysis/SKILL.md), drawing data and toolchains
   from [`external_tools.md`](external_tools.md).
3. Benchmark your driver→response→mechanism framing against verified GCB papers in
   [`exemplars/library.md`](exemplars/library.md).
4. Confirm submission, data/code-DOI archiving, and article-type/word policy in
   [`official-source-map.md`](official-source-map.md) before submitting.
