# The Lancet Resources

Action-oriented resources for the The Lancet skill pack. The `skills/` give the rules; this directory
lets an author **model** a Lancet-shaped submission and **benchmark** it against verified exemplars. Pair
these with the relevant `skills/lancet-*/SKILL.md`.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a clinical-trial **abstract + Research in context panel + Introduction** in Lancet house style — the structured abstract (Background / Methods / **Findings** / **Interpretation** / Funding), the three-part panel, and CONSORT/ITT discipline. Illustrative **fictional** trial; no real facts, no invented policy. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified *The Lancet* papers** organised by topic × design (RCT/CONSORT, meta-analysis/PRISMA, cohort/STROBE, global-burden systematic analysis). Design positioning only — no fabricated numbers; includes a sibling-journal "do-not-misattribute" guard. |
| [`official-source-map.md`](external_tools.md) | **The Lancet-specific policy & facts:** Information for Authors, ICMJE/CONSORT requirements, prospective registration, structured-abstract rules, scope, and a do-not-misattribute list. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | Registries, EQUATOR reporting standards, and software referenced by the pack. |

## Discipline scope — econometric code kit is **not** vendored

The Lancet is a **clinical and global-health** journal. The cross-pack econometrics code kit (Stata/Python
causal-inference pipeline: TWFE/DID, IV, RDD, DML) that ships with economics packs is **deliberately not
vendored here** — it is the wrong toolset for randomised trials, clinical epidemiology, and evidence
synthesis. The discipline-appropriate "pipeline" for this venue is the **reporting and statistics
workflow** below, governed by EQUATOR guidelines (CONSORT/STROBE/PRISMA) rather than econometric
identification.

## Suggested workflow

1. Lock the design and registration with
   [`../skills/lancet-study-design`](../skills/lancet-study-design/SKILL.md); pick the EQUATOR guideline and
   flow diagram with [`../skills/lancet-reporting`](../skills/lancet-reporting/SKILL.md).
2. Report estimates to the Lancet bar (effect size + 95% CI + analysis population) with
   [`../skills/lancet-statistics`](../skills/lancet-statistics/SKILL.md).
3. Model the **abstract + Research in context panel + Introduction** on
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md), guided by
   [`../skills/lancet-abstract`](../skills/lancet-abstract/SKILL.md),
   [`../skills/lancet-research-in-context`](../skills/lancet-research-in-context/SKILL.md), and
   [`../skills/lancet-writing`](../skills/lancet-writing/SKILL.md).
4. Benchmark design positioning against verified papers in
   [`exemplars/library.md`](exemplars/library.md); confirm submission, registration, and abstract policy in
   [`official-source-map.md`](external_tools.md).
