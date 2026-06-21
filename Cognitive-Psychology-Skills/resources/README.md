# Cognitive Psychology — Resources

Capability layer for the **Cognitive Psychology** (Elsevier) skill pack. This is a model-driven
cognitive-science venue, so the resources here center on **formal modeling, model comparison, and
reproducible model code** rather than a causal-inference pipeline. Cross-cutting method guidance lives
once in the shared empirical-methods hub and is linked below as background.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | Before→after rewrite of a Cognitive Psychology introduction in its house style (theoretical fork → rival models → why prior evidence can't settle it → discriminating design → model-driven contribution). Fictional teaching paper. |
| [`exemplars/library.md`](exemplars/library.md) | Real, web-verified *Cognitive Psychology* papers by topic × method (signal-detection/memory modeling, categorization, decision modeling, language), with a sibling-journal omission guard. Design positioning only — read the originals before citing numbers. |
| [`official-source-map.md`](official-source-map.md) | Venue-specific facts (publisher, portal, scope, review model, data/code policy, house style) with sourcing discipline and 待核实 markers. |
| [`external_tools.md`](external_tools.md) | Cognitive-modeling frameworks, model-comparison and mixed-model packages, repositories, and reproducibility tooling relevant to this venue. |
| [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) | *Background.* General objections referees raise by identification strategy (DiD / IV / RDD / DML / matching / mechanism) — relevant only if your study has a quasi-experimental or panel component; the core modeling objections for this venue live in this pack's skills. |
| [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) | *Background.* Modern inference + reporting table stakes (SE clustering, multiple-testing, reproducibility) — useful as a general reference; defer to `cogpsych-data-analysis` for model-comparison and recovery norms. |

## How to use

1. **Before formalizing the theory** — read `cogpsych-theory-and-hypotheses`; decide the model, the
   rival, and the discriminating prediction your experiments must produce.
2. **When fitting and comparing** — use the modeling/model-comparison tools in `external_tools.md`;
   report parameter and model recovery so the comparison is interpretable (`cogpsych-data-analysis`).
3. **Before submission** — confirm scope/shape, model-comparison completeness, reproducible code, and
   the Elsevier declarations against this pack's `official-source-map.md` and the official guide for
   authors.

> Method guidance in the shared hub is venue-neutral and provided only as background; always defer to
> this pack's skills and `official-source-map.md` for what *Cognitive Psychology* specifically requires.
