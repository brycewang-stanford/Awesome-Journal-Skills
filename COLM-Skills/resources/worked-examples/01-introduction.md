> **Illustrative teaching example.** The paper, benchmark, models, and every number below are
> **fictional**, invented to demonstrate how a COLM-shaped first page differs from a generic
> LLM-paper first page. No real results are reported and no COLM policy is invented.
> Companion skills: [`colm-writing-style`](../../skills/colm-writing-style/SKILL.md),
> [`colm-experiments`](../../skills/colm-experiments/SKILL.md), and
> [`colm-topic-selection`](../../skills/colm-topic-selection/SKILL.md).

# Worked Example: Rebuilding an LLM-Evaluation First Page for COLM (before → after)

COLM's award lineage rewards papers where **the language model is the object of study** and the
measurement is trustworthy. The rebuild below turns a leaderboard-style draft into that shape:
the phenomenon leads, the contamination story is on page one, every model is version-pinned,
and each claim is scoped to what was tested.

**Fictional paper:** *"Rot in the Benchmarks: Measuring How Fast Long-Context Reasoning Suites
Leak into Pre-training Corpora."* Fictional contribution: a dated, renewable benchmark
("TIDEMARK") plus a leakage-rate estimator that predicts when a static suite stops measuring
reasoning.

---

## Before (leaderboard-first draft — the shape COLM reviewers discount)

> **Abstract.** Large language models have shown impressive abilities on long-context
> reasoning. We introduce TIDEMARK, a challenging new benchmark of 2,400 problems. We evaluate
> many popular models, including GPT-style and open-source ones, and find that the best model
> reaches only 61%, showing there is significant room for improvement. We hope TIDEMARK will
> drive progress on long-context reasoning.
>
> **Introduction.** LLMs are increasingly used everywhere, making evaluation important. Existing
> benchmarks are saturated or too easy. We collect harder problems and test many models. Our
> contributions are: (1) a new benchmark; (2) an extensive evaluation; (3) analysis and
> insights. Experiments show our benchmark is challenging for all models.

**Why this fails the COLM bar:**

- **The benchmark is treated as an end, not a measurement instrument** — no argument about
  *what construct* the 2,400 problems measure or why scores can be trusted.
- **Contamination is not even mentioned**, though every static suite decays; a COLM reviewer's
  first question ("was this in pre-training data?") has no answer.
- **"Many popular models" is unpinnable** — no version strings, no decoding parameters, no
  dates; the 61% cannot be reproduced against API models that drift.
- **"Challenging" is the claimed contribution** — difficulty without validity is noise.
- **No phenomenon is studied**; nothing is learned about language models themselves, which is
  the routing signal that this draft belongs at a task-focused venue, if anywhere.

---

## After (COLM arc — phenomenon → measurement validity → pinned evidence → scoped claims)

> **Abstract.** Static reasoning benchmarks decay: once their items leak into pre-training
> corpora, scores measure memorization, not reasoning. We quantify this decay for long-context
> reasoning. TIDEMARK is a benchmark whose items carry verifiable creation dates, letting us
> compare model accuracy on items created before versus after each model's data cutoff. Across
> nine open-weight models (pinned checkpoint hashes) and three API models (version strings and
> query dates in App. A), accuracy on pre-cutoff items exceeds post-cutoff accuracy by 9-21
> points, and the gap grows with each benchmark's public age — our leakage-rate estimator puts
> the "half-life" of a public suite at roughly two release cycles (95% CIs over 5 evaluation
> seeds; full decoding configs released). We conclude that undated leaderboard numbers
> systematically overstate long-context reasoning, and we release TIDEMARK with a renewal
> protocol so post-cutoff items always exist. *(phenomenon → instrument → pinned evidence →
> scoped conclusion, all on page one.)*
>
> **Introduction.** *(¶1 — the phenomenon, first breath.)* When a benchmark item enters a
> model's pre-training corpus, the item stops measuring what it was written to measure. We ask
> how fast this happens for long-context reasoning and how much of today's reported progress
> it explains.
>
> *(¶2 — why existing instruments cannot answer this.)* Existing suites cannot separate
> reasoning from recall for a nameable reason: their items are undated, so pre- versus
> post-cutoff comparisons are impossible. Refresh-based suites replace items but discard the
> old ones, destroying the longitudinal signal. Canary strings detect verbatim leakage but
> miss paraphrase leakage, which we show dominates. *(each alternative fails specifically,
> not "prior benchmarks are limited.")*
>
> *(¶3 — the instrument and its validity argument.)* TIDEMARK items carry cryptographically
> timestamped creation dates. Validity rests on one design assumption, stated here: pre- and
> post-cutoff items are drawn from the same generating process (same authors, template pool,
> difficulty calibration; matched-pairs evidence in §3). Any accuracy gap between them is then
> attributable to exposure, not difficulty drift.
>
> *(¶4 — pinned evidence and scoped claims.)* Every open-weight model is identified by
> checkpoint hash; every API model by version string and query date; decoding parameters,
> prompts, and harness commit are in App. A, and all numbers carry 95% CIs over 5 evaluation
> seeds. We claim the 9-21 point exposure gap **for the twelve models and the item
> distribution tested** — not for "LLMs" — and we report the compute budget (App. F) so the
> measurement itself is reproducible.
>
> *(¶5 — what this changes.)* If public suites have a two-release-cycle half-life,
> leaderboard history needs dating the way epidemiology needs cohorts. TIDEMARK's renewal
> protocol makes the post-cutoff pool permanent. §2 defines the estimator; §3 validates the
> instrument; §4 reports the decay measurements; §5 re-reads three years of public
> leaderboard claims through the exposure gap.

---

## What moved, mapped to the skills

| Draft problem | Rebuild move | Skill |
| --- | --- | --- |
| Benchmark as trophy | Benchmark as *dated measurement instrument* with a validity argument | `colm-topic-selection` |
| Contamination unmentioned | Contamination *is* the research question; exposure gap quantified | `colm-experiments` |
| "Many popular models" | Checkpoint hashes, API version strings, query dates, harness commit | `colm-reproducibility` |
| Bare accuracies | CIs over evaluation seeds; decoding configs released | `colm-experiments` |
| Universal claims | Claims scoped to models and item distribution tested | `colm-writing-style` |
| No phenomenon | A decay law about LMs and their training data — the venue's home genre | `colm-topic-selection` |

> Next: [`../exemplars/library.md`](../exemplars/library.md) shows the real award-winning
> papers whose first pages earn trust this way, and
> [`../official-source-map.md`](../official-source-map.md) carries the verified 2026 policy.
