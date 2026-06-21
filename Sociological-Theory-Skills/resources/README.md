# ST Resources

Action-oriented resources for the Sociological Theory (ST) skill pack. The `skills/` give
advice; this directory lets an agent **act** — model an ST-style *theory* section and benchmark
against verified exemplars. Pair these with the relevant `skills/soctheory-*/SKILL.md`.

ST is the **American Sociological Association's (ASA) dedicated theory journal** (published by
SAGE): it publishes purely conceptual work that builds concepts, mechanisms, and propositions —
new substantive theories, history of theory, metatheory, formal theory construction, and
synthetic contributions — and it does **not** publish empirical hypothesis-testing studies
(those belong at its empirical siblings, the *American Sociological Review* and the *American
Journal of Sociology*). This shapes what is — and is not — vendored here.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a **theory** paper introduction in ST house style: problem → defined concepts → mechanism → numbered **propositions** (not hypotheses, no data). Illustrative fictional paper; no policy claims. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified ST theory papers** organized by theme. Theoretical positioning only — no fabricated concepts or numbers — with a sibling-confusion guard (ST ≠ ASR / AJS / Theory and Society / EJST). |
| [`official-source-map.md`](official-source-map.md) | **ST-specific policy & facts:** theory scope (the five kinds of theory work), Manuscript Central / ASA-style submission mechanics, the inclusive length cap, the $25 fee, and a "still unverified" list. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | External tools for theory work: locating the theoretical conversation, reference management, conceptual-figure tools, and argument-logic aids — **no statistical software**, by design. |

## Why there is no `code/` kit here

The econometrics / causal-inference code kit vendored into empirical packs is **deliberately NOT
vendored** into ST. ST is a **theory venue**: there are no datasets, no estimation, and no
results section, so a DID / IV / RDD / DML pipeline has nothing to act on here. The analogous
"tooling" for ST is conceptual, not statistical — argument-mapping and conceptual-figure aids
live in [`external_tools.md`](external_tools.md). If a project wants a sample, a measure, or a
test, it belongs at ASR/AJS, not ST.

For background only — the shared, discipline-agnostic reviewer and reporting references that
empirical packs draw on live under
[`../../shared-resources/empirical-methods/`](../../shared-resources/empirical-methods/) (e.g.,
the reviewer-objection checklist and reporting-standards notes). They are **not** part of the ST
workflow and are listed here purely so an agent knows where the empirical material is when a
project turns out to be ASR/AJS-shaped rather than ST-shaped.

## Suggested workflow

1. Frame the problem and contribution with
   [`../skills/soctheory-topic-selection`](../skills/soctheory-topic-selection/SKILL.md) and
   [`../skills/soctheory-contribution-framing`](../skills/soctheory-contribution-framing/SKILL.md);
   model the intro on [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
2. Build the theory with
   [`../skills/soctheory-theory-construction`](../skills/soctheory-theory-construction/SKILL.md) —
   concepts → assumptions → mechanisms → numbered propositions — then make the argument valid with
   [`../skills/soctheory-argument-development`](../skills/soctheory-argument-development/SKILL.md)
   and bound it with
   [`../skills/soctheory-boundary-conditions`](../skills/soctheory-boundary-conditions/SKILL.md).
3. Polish to ASA house style with
   [`../skills/soctheory-writing-style`](../skills/soctheory-writing-style/SKILL.md) (propositions,
   not hypotheses; no methods/results/data section; everything counts toward the length cap).
4. Benchmark against verified ST papers in [`exemplars/library.md`](exemplars/library.md); confirm
   scope, the length cap, the fee, and submission facts in
   [`official-source-map.md`](official-source-map.md) and tooling in
   [`external_tools.md`](external_tools.md).
