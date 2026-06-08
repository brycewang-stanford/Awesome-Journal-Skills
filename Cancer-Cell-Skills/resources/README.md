# Cancer Cell Resources

Action-oriented resources for the Cancer Cell (Cell Press) skill pack. The `skills/` give advice; this
directory lets an agent **model** a Cancer Cell front-matter/opening and **benchmark** against verified
exemplars. Pair these with the relevant `skills/cc-*/SKILL.md`.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a Cancer Cell **Summary + opening** in Cell Press house style — the mechanistic arc (context → orthogonal validation → mechanism → translational significance) with calibrated verbs. Illustrative **fictional** paper; no real facts. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified Cancer Cell papers** organized by topic × method. Each confirmed on `cell.com/cancer-cell` (DOI `10.1016/j.ccell...` or legacy `S1535-6108`/`j.ccr`). Design positioning only — no fabricated numbers. Includes a sibling-confusion guardrail. |
| [`external_tools.md`](external_tools.md) | External tools and services referenced by the pack (deposition, reporting, image-integrity, nomenclature). |
| `official-source-map.md` | **Cancer Cell-specific policy & facts** (submission portal, STAR Methods / Key Resources Table, data/code deposition, scope, do-not-misattribute list) — the authoritative pack policy source. *Not yet vendored into this pack; until it is, treat the per-skill `cc-*/SKILL.md` policy sections as authoritative and verify against the Cell Press author guide.* |

## Discipline note — no econometric code kit vendored

This is a **cancer-biology** pack (wet-lab + translational oncology). Unlike the economics packs, it does
**not** vendor a `code/` directory of causal-inference / econometrics scripts (Stata/Python DiD, IV, RDD,
DML) — that kit is venue-inappropriate here. Statistical and reproducibility guidance lives in the
skills instead:

- [`../skills/cc-statistics/SKILL.md`](../skills/cc-statistics/SKILL.md) — defining `n`, test choice,
  multiple-comparison correction, error bars, avoiding pseudo-replication.
- [`../skills/cc-study-design/SKILL.md`](../skills/cc-study-design/SKILL.md) — orthogonal validation,
  controls, replicates, power, randomization, blinding.
- [`../skills/cc-reporting-standards/SKILL.md`](../skills/cc-reporting-standards/SKILL.md) — STAR
  Methods, Key Resources Table, rigor/reproducibility, data/code deposition.

## Suggested workflow

1. Confirm venue fit with [`../skills/cc-scope-fit/SKILL.md`](../skills/cc-scope-fit/SKILL.md) — the
   two-pillar bar (mechanistic depth + translational relevance).
2. Draft the front matter and opening with
   [`../skills/cc-structured-abstract/SKILL.md`](../skills/cc-structured-abstract/SKILL.md) and
   [`../skills/cc-writing-style/SKILL.md`](../skills/cc-writing-style/SKILL.md); model them on
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
3. Benchmark your topic × method against verified papers in
   [`exemplars/library.md`](exemplars/library.md), heeding the sibling-confusion guardrail (Cancer Cell
   is not Cell, Cancer Research, Nature Cancer, Cancer Discovery, or Nature Medicine).
4. Ground statistics, design, and reporting in the `cc-*` skills above (no econometric kit applies here).
