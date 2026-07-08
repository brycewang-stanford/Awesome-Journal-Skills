> **Illustrative teaching example.** The paper, dataset, systems, and every
> number below are **fictional**, invented only to demonstrate ACL house style.
> No real results are reported and no venue policy is invented. Corresponding
> skills: [`acl-writing-style`](../../skills/acl-writing-style/SKILL.md),
> [`acl-experiments`](../../skills/acl-experiments/SKILL.md), and
> [`acl-topic-selection`](../../skills/acl-topic-selection/SKILL.md).

# Worked Example: An ACL-Style Abstract + Introduction (before → after)

This walks the **ACL first-page contract** from `acl-writing-style`: task or
phenomenon first, a real example on page one, a typed contribution, claims
scoped to the languages and models actually tested, and every qualitative
observation attached to a count. It also shows the LLM-era discipline from
`acl-experiments`: prompt sensitivity, contamination awareness, and error
analysis as part of the argument rather than an afterthought.

**Illustrative paper (fictional):** *"When 'Not' Gets Lost in Translation:
Negation Transfer Failures in Multilingual Instruction-Tuned Models."*
Fictional setting: a test suite probing whether instruction-tuned models
preserve negation when answering questions over translated context, in five
languages.

---

## Before (model-first, unscoped — a typical first draft)

> **Abstract.** Large language models have revolutionized NLP. However, they
> still make mistakes. In this paper, we investigate the abilities of LLMs on
> negation. We construct a new benchmark and evaluate several popular models,
> finding that LLMs cannot handle negation and that performance is poor across
> languages. Our findings have important implications for the community.
>
> **Introduction.** LLMs such as GPT-style models have shown remarkable
> capabilities on many tasks. Despite this progress, negation remains
> challenging. Prior work has studied negation in various settings. We propose
> NegBench, a large benchmark for negation, and evaluate many models on it.
> Experiments show that models often fail. We also perform some analysis.
> Section 2 discusses related work...

**Why this fails the ACL bar (per `acl-writing-style` / `acl-experiments`):**

- **Model-first, task-invisible.** The phenomenon (negation transfer under
  translation) never gets defined; "investigate the abilities of LLMs" is not
  a task statement.
- **No example on page one.** A reviewer cannot yet picture a single test item.
- **Unscoped universal claims.** "LLMs cannot handle negation" and "across
  languages" — which models, which prompts, which languages? This is the
  exact reflex-phrasing the style skill's table rewrites.
- **Untyped contribution.** Benchmark? Analysis? Finding? The reader cannot
  classify it, so reviewers cannot calibrate it.
- **No numbers, no uncertainty, no error taxonomy** — "often fail" and
  "performance is poor" are anecdotes wearing a lab coat.
- **No language list in the abstract**, violating the "say your languages up
  front" rule for multilingual claims.

---

## After (phenomenon-first, scoped, example-grounded)

> **Abstract.** When context is machine-translated, does "not" survive?
> We introduce **NegXfer**, a 4,500-item diagnostic suite testing whether
> instruction-tuned models preserve **negation** when answering yes/no
> questions over translated passages in **German, Hindi, Swahili, Turkish,
> and Mandarin**. Items pair minimally contrasting passages ("The trial
> found no benefit" vs "...found a benefit") with questions whose correct
> answers flip. Across six open instruction-tuned models (1B-70B), accuracy
> on negated items trails affirmative twins by **14-31 points**, and the gap
> **widens with translation distance** from English; averaged over five
> prompt paraphrases, variance across prompts is smaller than the negation
> gap (±2.1 vs 14+ points). An error taxonomy over 600 sampled failures shows
> **negation-drop in translation (41%)** and **answer-flip under double
> negation (23%)** dominate. We release items with per-language provenance,
> creation-date stamps, and all model outputs. *(task → languages → scoped
> finding → variance honesty → analysis → artifact, all in one breath.)*
>
> **Introduction.** *(¶1 — phenomenon + example.)* A clinician asking a
> multilingual assistant whether a drug trial succeeded should get opposite
> answers for "the trial found no benefit" and "the trial found a benefit."
> We test whether instruction-tuned models keep that guarantee when the
> passage is translated. In the Swahili condition of our suite, one 8B model
> answers "yes" to both variants in 38% of items — the negation is lost
> between passage and answer. *(a concrete item and a count on page one.)*
>
> *(¶2 — why existing evidence is insufficient.)* Existing negation probes
> are English-centric and pre-instruction-tuning; multilingual benchmarks
> measure end-task accuracy, where negation failures hide inside aggregate
> scores; and translation studies evaluate adequacy, not downstream answer
> consistency. None isolates *transfer* of negation through translation into
> the answer. *(each neighbor gets a named gap — the `acl-related-work`
> contrast pattern.)*
>
> *(¶3 — typed contribution.)* We contribute: (i) a **resource** — NegXfer,
> minimal-pair items in five typologically distinct languages, built by
> native-speaker annotators (guidelines, pay, and agreement in App. C;
> Krippendorff's α = .81); (ii) an **evaluation finding** — the scoped gap
> above, robust across five prompt paraphrases and two decoding settings;
> (iii) an **analysis** — a six-category error taxonomy, double-annotated on
> a 200-item subset (α = .77). *(contribution types named, per
> `acl-topic-selection`.)*
>
> *(¶4 — validity guardrails.)* Passages are drawn from post-cutoff news and
> stamped with creation dates to limit contamination; we report per-language
> results with bootstrap confidence intervals rather than a single average;
> and we verify labels against annotator majority before scoring any model.
> *(the `acl-experiments` floor: contamination, uncertainty, label quality.)*
>
> *(¶5 — scope and stakes.)* Our claims are limited to the five languages,
> six open models, and QA format tested — the Limitations section discusses
> closed models and morphological negation we do not cover. Within that
> scope, the finding is actionable: negation-drop is concentrated in the
> translation step, suggesting targeted contrastive tuning data. *(scoped,
> with the limitation surfaced by the authors first.)*

---

## Why the "after" version meets the bar

- **Task first, model second** — the phenomenon and a page-one example lead;
  model names arrive only inside scoped results (`acl-writing-style`).
- **Languages in the abstract**, typologically justified, per the multilingual
  scoping rule.
- **Every anecdote has a count**: the 38% Swahili example, the 41%/23% error
  categories, agreement statistics for both labels and taxonomy.
- **Prompt-sensitivity honesty**: variance across paraphrases is reported and
  compared against the effect size — the LLM-era reviewer's first question.
- **Contamination stance stated** (post-cutoff items, date stamps), matching
  Responsible NLP checklist expectations (`acl-reproducibility`).
- **Typed contributions** let reviewers grade resource, finding, and analysis
  on their own scales instead of averaging confusion.
- **Releasing model outputs** makes the paper re-scorable without GPUs — the
  cheap turnkey upgrade recommended in `acl-artifact-evaluation`.

> Next: benchmark against real, verified ACL papers in
> [`../exemplars/library.md`](../exemplars/library.md), and confirm current
> submission policy in [`../official-source-map.md`](../official-source-map.md).
