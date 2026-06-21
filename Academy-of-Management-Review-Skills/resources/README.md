# AMR Resources

Action-oriented resources for the Academy of Management Review (AMR) skill pack. The `skills/` give
advice; this directory lets an agent **act** — model an AMR-style *theory* section and benchmark against
verified exemplars. Pair these with the relevant `skills/amr-*/SKILL.md`.

AMR is the Academy of Management's **theory-development journal**: it publishes purely conceptual
articles that build constructs, mechanisms, and propositions, and it does **not** publish empirical
hypothesis-testing studies (those belong at its empirical sibling, the *Academy of Management Journal*,
AMJ). This shapes what is — and is not — vendored here.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a **theory** paper introduction in AMR house style: puzzle → defined constructs → mechanism (the Why) → numbered **propositions** (not hypotheses, no data). Illustrative fictional paper; no policy claims. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified AMR theory papers** organized by theme. Theoretical positioning only — no fabricated constructs or numbers — with a sibling-confusion guard (AMR ≠ AMJ / ASQ / Organization Science / Journal of Management). |
| [`official-source-map.md`](official-source-map.md) | **AMR-specific policy & facts:** theory-only scope, the four contribution paths, ScholarOne/AOM Style Guide mechanics, editor/history, AI-disclosure policy, the contribution-bar editorials (Whetten 1989; Suddaby 2010), and bounded live-check notes. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | External tools for theory work: locating the theoretical conversation, reference management, conceptual-figure (box-and-arrow) tools, and argument-logic aids — **no statistical software**, by design. |

## Why there is no `code/` kit here

The econometrics / causal-inference code kit vendored into empirical packs (e.g., the
Quarterly-Journal-of-Economics pack's Stata + Python pipeline) is **deliberately NOT vendored** into AMR.
AMR is a **theory venue**: there are no datasets, no estimation, and no results section, so a DID / IV /
RDD / DML pipeline has nothing to act on here. The analogous "tooling" for AMR is conceptual, not
statistical — argument-mapping and conceptual-figure aids live in
[`external_tools.md`](external_tools.md). If a project wants a sample, a measure, or a test, it belongs
at AMJ/ASQ/SMJ, not AMR.

## Suggested workflow

1. Frame the puzzle and contribution with
   [`../skills/amr-topic-selection`](../skills/amr-topic-selection/SKILL.md) and
   [`../skills/amr-contribution-framing`](../skills/amr-contribution-framing/SKILL.md); model the intro
   on [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
2. Build the theory with
   [`../skills/amr-theory-development`](../skills/amr-theory-development/SKILL.md) — constructs →
   assumptions → relationships + mechanisms → numbered propositions → boundary conditions.
3. Polish to AOM house style with
   [`../skills/amr-writing-style`](../skills/amr-writing-style/SKILL.md) (propositions, not hypotheses;
   no methods/results/data section).
4. Benchmark against verified AMR papers in [`exemplars/library.md`](exemplars/library.md); confirm
   scope, contribution bar, and submission/format facts in
   [`official-source-map.md`](official-source-map.md) and tooling in
   [`external_tools.md`](external_tools.md).
