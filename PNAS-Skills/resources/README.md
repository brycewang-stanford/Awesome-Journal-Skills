# PNAS Resources

Action-oriented resources for the *PNAS* (Proceedings of the National Academy of Sciences) skill pack.
The `skills/` give advice; this directory lets an agent **model** PNAS-specific front matter and
**benchmark** against verified exemplars. Pair these with the relevant `skills/pnas-*/SKILL.md`.

PNAS is a **multidisciplinary science journal** spanning Biological, Physical, and Social Sciences. There
is therefore **no single discipline-specific code kit** that fits the readership, so — unlike the
economics packs — **no econometrics / causal-inference code kit is vendored here** (see the note below).
The venue-specific value lives in the two house-style pieces and the verified exemplar library.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of the two PNAS front-matter artifacts — the mandatory **≤120-word Significance Statement** *and* the ~250-word **abstract** — kept genuinely distinct, in PNAS house style. Illustrative **fictional** paper; no invented policy. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified PNAS papers** (every one a `10.1073/pnas…` DOI) organized by field × method across all three divisions. Design/significance positioning only — no fabricated numbers. Includes a sibling-confusion guard (PNAS ≠ *Science* / *Nature* / *Cell* / *PLOS ONE* / *Nature Communications*). |
| [`external_tools.md`](external_tools.md) | **The authoritative pack source map:** PNAS-specific deposition repositories, the Significance-Statement / Classification / in-text-Methods rules, submission tracks (Direct vs Contributed), reporting standards, and official PNAS author-center pages. |

> **On `official-source-map.md`:** the QJE pack keeps its venue policy in a file named
> `official-source-map.md`; in this pack the equivalent authoritative source-of-record is
> [`external_tools.md`](external_tools.md) (PNAS deposition policy, Significance Statement, Classification,
> tracks, and official URLs). There is no separate `official-source-map.md` in PNAS-Skills — use
> `external_tools.md`.

## No econometric / code kit (deliberate)

PNAS is multidisciplinary; a single econometrics or causal-inference command kit would fit only a sliver
of its Social-Sciences readership and none of the Biological/Physical work. So, unlike
[`../../Quarterly-Journal-of-Economics-Skills/resources/code/`](../../Quarterly-Journal-of-Economics-Skills/resources/code/),
**this pack vendors no `code/` directory.** Discipline-appropriate analysis software (R, Python,
domain-specific tools) and the data/code-deposition repositories PNAS requires are listed in
[`external_tools.md`](external_tools.md).

## Suggested workflow

1. **Decide PNAS is right** with [`../skills/pnas-fit`](../skills/pnas-fit/SKILL.md) (cross-division
   significance test; the realistic Science/Nature step-down call).
2. **Draft the Significance Statement early** with
   [`../skills/pnas-significance`](../skills/pnas-significance/SKILL.md), then the abstract with
   [`../skills/pnas-abstract`](../skills/pnas-abstract/SKILL.md) — model both on
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md), keeping the two distinct.
3. **Structure the main text** (Significance → Abstract → Intro → Results → Discussion → in-text Materials
   and Methods → refs) with [`../skills/pnas-writing`](../skills/pnas-writing/SKILL.md).
4. **Benchmark** your field × method against verified PNAS papers in
   [`exemplars/library.md`](exemplars/library.md); confirm deposition and submission policy in
   [`external_tools.md`](external_tools.md).
