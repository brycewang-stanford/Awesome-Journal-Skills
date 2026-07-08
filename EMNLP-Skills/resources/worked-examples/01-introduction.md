> **Illustrative teaching example.** The paper, task, systems, and every number below are
> **fictional**, invented only to demonstrate how an EMNLP-style first page is built. No real-paper
> facts or results appear, and no venue policy is invented. Corresponding skills:
> [`emnlp-writing-style`](../../skills/emnlp-writing-style/SKILL.md),
> [`emnlp-experiments`](../../skills/emnlp-experiments/SKILL.md), and
> [`emnlp-topic-selection`](../../skills/emnlp-topic-selection/SKILL.md).

# Worked Example: An EMNLP-Style Abstract + Introduction (before → after)

EMNLP's first-page contract is empirical: **name the language phenomenon or task failure, quantify
it, explain why current systems fail, state what you did, and preview the evidence** — including
where the method still breaks. Reviewers drawn from the ACL pool read for evaluation validity
first: which languages, which datasets, what baselines, what significance evidence, what error
analysis. A first page that leads with architecture novelty and hides the evaluation design reads
as a systems pitch that wandered in from another venue.

**Illustrative paper (fictional):** *"When Politeness Erases Meaning: Diagnosing and Reducing
Pragmatic Drift in Multilingual Instruction-Tuned Summarizers."* Fictional finding: instruction-tuned
summarizers systematically soften or delete speaker commitments ("will" → "may") in languages with
grammaticalized politeness, and a targeted data-augmentation recipe reduces the effect.

---

## Before (architecture-first draft — the kind EMNLP reviewers bounce)

> **Abstract.** Large language models have revolutionized summarization. We present PoliteSumm, a
> novel framework combining instruction tuning with a pragmatic-awareness module. Extensive
> experiments demonstrate that PoliteSumm achieves state-of-the-art performance across multiple
> benchmarks and languages, significantly outperforming strong baselines. Our results highlight the
> potential of pragmatics-aware modeling for real-world applications.
>
> **Introduction.** Summarization is an important NLP task with many applications. Recently, LLMs
> have shown impressive results. However, existing methods do not consider pragmatics. We propose a
> new module that injects pragmatic awareness into the decoder. Experiments on several datasets show
> our method works well in many settings. We also conduct ablation studies. Our contributions are:
> (1) a novel framework; (2) extensive experiments; (3) state-of-the-art results.

**Why this fails the EMNLP read:**

- **No phenomenon.** "Does not consider pragmatics" names nothing a reviewer can verify; the actual
  behavior (commitment softening under grammaticalized politeness) never appears.
- **Evaluation invisible.** "Multiple benchmarks and languages" — which ones? A multilingual claim
  with unnamed languages is the classic EMNLP scope violation.
- **"Significantly" without a test.** The word raises the exact question (what test, how many runs,
  what p-value?) the draft cannot answer.
- **No error analysis promised.** EMNLP expects the authors to know where the method fails before
  the reviewers find out.
- **Contribution list is generic.** "Novel framework / extensive experiments / SOTA" fits every
  rejected paper ever written; nothing is falsifiable.

---

## After (phenomenon-first — the EMNLP arc)

> **Abstract.** Instruction-tuned summarizers do not merely compress text — they *reword* it, and in
> languages with grammaticalized politeness the rewording is systematically biased: speaker
> commitments are softened or deleted. On our new diagnostic set spanning Japanese, Korean, German,
> and English (1,200 human-annotated document-summary pairs), three open instruction-tuned models
> alter the commitment level of 18-31% of obligation statements, versus 6-9% in English. We call
> this *pragmatic drift*, trace it via attention attribution to politeness-marked spans in the
> instruction data, and show that a contrastive augmentation recipe — pairing each polite variant
> with a commitment-preserving reference — cuts drift roughly in half (to 9-14%) without degrading
> ROUGE or human adequacy judgments (n = 480 ratings, paired bootstrap, p < 0.01). Drift remains
> above the English baseline in honorific-rich registers; we release the diagnostic set, annotation
> guidelines, and all prompts.
>
> **Introduction.** *(¶1 — the phenomenon, with a measured example.)* Ask an instruction-tuned model
> to summarize a Japanese meeting transcript and the sentence "the vendor will deliver by March"
> can return as "the vendor may deliver around March." The source committed; the summary hedges.
> On our diagnostic data this is not an anecdote: 18-31% of obligation statements change commitment
> level across three models — a meaning error invisible to ROUGE.
>
> *(¶2 — why current evaluation misses it.)* Standard summarization metrics score lexical or
> embedding overlap, and "may deliver around March" overlaps "will deliver by March" almost
> perfectly. Faithfulness benchmarks target *added* or *contradicted* content, not weakened
> commitment strength; multilingual leaderboards aggregate over languages, hiding a failure
> concentrated where politeness is grammaticalized. Each gap gets its own measurement in Section 3.
>
> *(¶3 — hypothesis and method, scoped.)* We hypothesize the drift is learned from instruction data
> in which polite paraphrases dominate. Attention attribution over politeness-marked spans supports
> this (Section 4). The fix follows the diagnosis: contrastive augmentation pairing polite surface
> forms with commitment-preserving targets. We claim only what we test — four languages, two
> domains (meetings, customer support), open models in the 7-13B range.
>
> *(¶4 — evidence preview, failures included.)* Augmentation halves drift (9-14%) with no
> significant ROUGE or human-adequacy loss (paired bootstrap over 5 seeded runs). Error analysis
> (Section 6) shows the residual failures concentrate in honorific-rich formal registers and in
> Korean indirect quotation — cases we release as a targeted challenge subset.
>
> *(¶5 — contributions, each falsifiable.)* (1) A four-language diagnostic set with annotation
> guidelines and inter-annotator agreement (κ = 0.78); (2) the first quantification of pragmatic
> drift in instruction-tuned summarizers; (3) a data-level mitigation validated with significance
> testing and human evaluation; (4) a public release of data, prompts, and evaluation code.

---

## Why the "after" survives EMNLP review

- **A nameable, measurable phenomenon** leads: pragmatic drift, with rates, before any method talk.
- **Languages are named and claims scoped** to them — no "multilingual" hand-waving; the 7-13B model
  range and two domains bound the claim exactly where the evidence lives.
- **Metric critique is itself empirical:** the paper shows *why* ROUGE misses the failure instead of
  asserting metric inadequacy.
- **Significance evidence is specified** (paired bootstrap, seeded runs, human-rating count), so
  "cuts drift in half" is a testable statement, not adverb inflation.
- **Failure modes are volunteered** — residual drift in honorific registers — which converts the
  Limitations section from ritual to content and pre-empts the strongest reviewer objection.
- **Artifacts are promised concretely** (data, guidelines, prompts, code), matching the Responsible
  NLP checklist answers the submission must file anyway.

> Next: [`../exemplars/library.md`](../exemplars/library.md) shows real, Anthology-verified EMNLP
> papers whose first pages execute this arc, and [`../official-source-map.md`](../official-source-map.md)
> carries the current submission policy this example deliberately does not restate.
