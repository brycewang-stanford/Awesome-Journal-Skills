# GEC Resources

Action-oriented resources for the *Global Environmental Change* (GEC) skill pack. The `skills/` give
advice; this directory lets an agent **act** — model a GEC-style section and benchmark against
verified exemplars. Pair these with the relevant `skills/gec-*/SKILL.md`.

GEC is an **interdisciplinary, social-science-leading** Elsevier journal on the **human and policy
dimensions** of global environmental change. Its work couples human and environmental systems and is
**partly empirical social science** (quasi-experimental and observational designs appear alongside
qualitative, mixed-methods, and conceptual work). The resource layer reflects that: discipline-shaped
writing models and exemplars, plus a pointer to venue-neutral empirical craft — but **no vendored
econometrics code kit** (see below).

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a paper **introduction** in GEC house style — coupling human + environmental systems, a framework that does work, two literatures, policy relevance. Illustrative fictional paper; no real policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified GEC papers** (Elsevier; `10.1016/...gloenvcha`) organized by method × topic, with a sibling-confusion guard. Design positioning only — no fabricated findings. |
| [`official-source-map.md`](official-source-map.md) | **GEC-specific policy & facts:** Elsevier submission, 8,000-word Research Article cap, 3,000-word Perspective cap, <=250-word abstract, Highlights, human-and-policy-dimensions scope, double-anonymized review, Option C data policy, editors/history. The authoritative pack source, refreshed 2026-06-20. |
| [`external_tools.md`](external_tools.md) | External tools, data sources, and software referenced by the pack (quant, qualitative/CAQDAS, governance and environmental data). |

## Shared empirical-methods kit (venue-neutral, cross-pack) — used selectively

GEC publishes empirical social science, and some of it is **quasi-experimental or observational** (e.g.,
staggered-adoption difference-in-differences, IV, RDD, matching on human-dimensions outcomes). For that
subset, the venue-neutral standard referee objections apply. That prose is shared across journal packs
and lives in the repo's shared hub:

- [`../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../shared-resources/empirical-methods/reviewer-objection-checklist.md)
  — the standard referee objections (identification, inference, robustness, mechanism) and how to
  pre-empt them. **Apply this to a GEC paper's quasi-experimental / observational claims**; it does not
  apply to qualitative, conceptual, or purely descriptive work.

**The econometric CODE kit is *not* vendored into this pack.** Unlike economics-method packs, GEC is
methodologically pluralist and social-science-leading, so this resource layer deliberately ships
**no** Stata/Python causal-inference pipeline. If your GEC submission needs that code, use the shared
hub's own `code/` directory (`../../shared-resources/empirical-methods/code`) directly rather than a
copy here.

## Suggested workflow

1. Scope and frame with [`../skills/gec-topic-selection`](../skills/gec-topic-selection/SKILL.md) and
   [`../skills/gec-literature-positioning`](../skills/gec-literature-positioning/SKILL.md); build the
   framework with [`../skills/gec-conceptual-framework`](../skills/gec-conceptual-framework/SKILL.md).
2. Model the introduction on [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md),
   polishing prose with [`../skills/gec-writing-style`](../skills/gec-writing-style/SKILL.md).
3. Defend the design with [`../skills/gec-research-design`](../skills/gec-research-design/SKILL.md); if
   the work is quasi-experimental or observational, pre-empt referees with the shared
   [`reviewer-objection-checklist.md`](../../shared-resources/empirical-methods/reviewer-objection-checklist.md).
4. Sharpen the "so what" with
   [`../skills/gec-policy-relevance-and-implications`](../skills/gec-policy-relevance-and-implications/SKILL.md);
   benchmark against verified GEC papers in [`exemplars/library.md`](exemplars/library.md); confirm
   submission/scope facts in [`official-source-map.md`](official-source-map.md).
