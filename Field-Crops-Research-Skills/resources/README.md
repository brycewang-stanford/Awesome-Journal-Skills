# Field Crops Research Resources

Action-oriented resources for the *Field Crops Research* (FCR) skill pack. The `skills/` give advice;
this directory lets an agent **act** — model an FCR-style abstract + introduction, benchmark against
verified exemplars, and confirm FCR-specific scope and policy. Pair each resource with the relevant
`skills/fcr-*/SKILL.md`.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of an **abstract + introduction** in FCR house style — yield-gap/agronomy framing, a multi-environment (≥ 2 seasons / multiple sites) design, and G×E reported properly. Illustrative **fictional** paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified FCR papers** (Elsevier, DOI `10.1016/j.fcr…`) organised by topic × method. Framing/design positioning only — no fabricated numbers — with a sibling-journal guard. |
| [`official-source-map.md`](official-source-map.md) | **FCR-specific policy & facts:** Elsevier/Editorial Manager submission, ISSN 0378-4290, scope gate (field-based, multi-environment, field crops, general significance), abstract ≤ 400 words, 3–5 highlights ≤ 85 chars, data-availability and generative-AI declarations. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | External agronomy/crop-science tools, data sources, and software referenced by the pack. |

## No vendored econometrics code kit (agronomy venue)

Unlike the economics packs in this repo, **this pack does not vendor a causal-inference / econometrics
code kit** (TWFE / DID / IV / RDD / DML do-files). FCR is a **field-agronomy and crop-science** journal:
its analytical core is **linear mixed models** for block-design and split-plot multi-environment trials, G×E
and stability analysis (Finlay–Wilkinson, AMMI, GGE), estimated marginal means with SED/LSD, and
crop-model calibration/validation — **not** a reduced-form policy-evaluation pipeline. Vendoring the
econometrics kit here would be off-discipline and misleading. The relevant analysis norms live in
[`../skills/fcr-data-analysis/SKILL.md`](../skills/fcr-data-analysis/SKILL.md) and
[`../skills/fcr-experimental-design/SKILL.md`](../skills/fcr-experimental-design/SKILL.md); software
pointers (R/ASReml/lme4/sommer, GenStat, APSIM/DSSAT, GYGA) are in
[`external_tools.md`](external_tools.md).

## Suggested workflow

1. **Scope and frame.** Clear the scope gate with
   [`../skills/fcr-topic-selection`](../skills/fcr-topic-selection/SKILL.md) and position the gap in
   general terms with
   [`../skills/fcr-literature-positioning`](../skills/fcr-literature-positioning/SKILL.md); model the
   abstract + intro on [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
2. **Design and analyse.** Build a multi-environment, G×E-aware design with
   [`../skills/fcr-experimental-design`](../skills/fcr-experimental-design/SKILL.md) and analyse it with
   [`../skills/fcr-data-analysis`](../skills/fcr-data-analysis/SKILL.md) (mixed models, EMMs with
   SED/LSD, stability analysis); reach for the software in [`external_tools.md`](external_tools.md).
3. **Benchmark.** Compare your framing against verified FCR papers in
   [`exemplars/library.md`](exemplars/library.md).
4. **Preflight.** Confirm scope, abstract/highlights limits, declarations, and submission/data policy in
   [`official-source-map.md`](official-source-map.md) and
   [`../skills/fcr-submission`](../skills/fcr-submission/SKILL.md).
