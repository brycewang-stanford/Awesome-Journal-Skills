# Journal of Educational Psychology — Resources

Capability layer for the **Journal of Educational Psychology** (JEP) skill pack. JEP is an experimental
and field-research journal in educational psychology — its evidence comes from classroom/school
experiments, randomized field trials, quasi-experiments, longitudinal studies, and multilevel/SEM/growth
models — so this layer points to **design, power, multilevel/SEM, and open-science** tooling rather than a
vendored econometrics kit. The cross-cutting method guidance lives once in the shared empirical-methods
hub and is linked below as background.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | Before→after rewrite of a JEP Introduction in the educational-question → mechanism → rigorous-design → result-forward style. Fictional teaching paper. |
| [`exemplars/library.md`](exemplars/library.md) | Real, web-verified *Journal of Educational Psychology* papers by topic × method, with a sibling-journal omission guard. Design positioning only — read the originals before citing numbers. |
| [`official-source-map.md`](official-source-map.md) | Venue-specific facts (scope, word/abstract limits, masked review, transparency/JARS, portal, fee) with sourcing discipline and 待核实 markers. |
| [`external_tools.md`](external_tools.md) | External tools / packages relevant to this venue (power for nested designs, multilevel/SEM, preregistration, repositories, JARS). |
| [`code/`](code/) | Runnable R skeletons for cluster-design diagnostics, multilevel/growth models, mediation with indirect-effect intervals, and JARS-ready reproducible tables. |
| [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) | Background: objections referees raise by identification strategy (DiD / IV / RDD / matching / mechanism); useful when a JEP study has a quasi-experimental component. |
| [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) | Background: modern inference + reporting table stakes (SE clustering, multiple-testing, reproducibility) — complements JEP's JARS requirements. |

## How to use

1. **Before drafting tables** — pressure-test the design (especially nesting and cluster-level power) with
   `jedpsych-study-design`; for any quasi-experimental component, sanity-check against the shared
   reviewer-objection checklist (background only).
2. **When building results** — keep the analysis multilevel/SEM-aware (see `jedpsych-data-analysis`);
   report effect sizes with CIs and educational interpretation, and test the mechanism.
3. **When scaffolding code** — adapt [`code/R/00_setup.R`](code/R/00_setup.R) through
   [`code/R/04_reproducible_tables.R`](code/R/04_reproducible_tables.R) to lock the cluster structure,
   model the learning trajectory or mechanism, and produce JARS-ready table notes from a single script.
4. **Before submission** — walk this pack's `official-source-map.md` for venue limits and the
   `jedpsych-submission` checklist; complete the JARS / JARS-REC items.

> Method guidance in the shared hub is venue-neutral; always defer to this pack's skills and
> `official-source-map.md` for what *this* journal specifically requires.
