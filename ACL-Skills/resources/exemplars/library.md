# ACL Exemplars Library (contribution type × era)

> **Verified via web search, access date 2026-07-08.** Every paper below was
> checked against the **ACL Anthology** (`aclanthology.org/...`) to confirm it
> appeared at the **Annual Meeting of the Association for Computational
> Linguistics** specifically — matching the Anthology ID to an ACL main
> proceedings volume, plus authors, year, and (where surfaced) pages. Papers
> that could not be cleanly pinned to *ACL the conference* were omitted and are
> listed at the bottom as guardrails. Short and verified beats long and guessed.
>
> **Sibling-confusion guard:** the \*ACL family shares the Anthology, so an
> `aclanthology.org` URL does **not** prove ACL. Legacy IDs encode the venue:
> `P` = ACL main, `N` = NAACL, `D` = EMNLP, `E` = EACL; modern IDs name it
> directly (`2020.acl-main.442`). BERT is **NAACL 2019**, ELMo is **NAACL
> 2018**, "Attention Is All You Need" is **NeurIPS 2017** — none belong here.
>
> **Zero-hallucination rule:** this file gives design positioning only. Reread
> the original before citing any number, and check
> [`../official-source-map.md`](../official-source-map.md) for policy facts.

---

## How to use this library

Match your project to the closest **contribution type**, then study how the
exemplar makes the linguistic object visible on page one, pairs examples with
counts, and scopes its claims — the bar described in
[`../../skills/acl-writing-style/SKILL.md`](../../skills/acl-writing-style/SKILL.md)
and [`../../skills/acl-experiments/SKILL.md`](../../skills/acl-experiments/SKILL.md).
Each entry ends with the self-check question to ask about your own draft.

---

## By contribution type

### Evaluation methodology (metric)

- **Papineni, Roukos, Ward & Zhu, "Bleu: a Method for Automatic Evaluation of
  Machine Translation," ACL 2002.** Verified: `aclanthology.org/P02-1040/`,
  Proceedings of the 40th Annual Meeting, pp. 311-318.
  - **Why it is an exemplar:** proposes a metric with an explicit validity
    argument — cheap, language-independent, and *correlated with human
    judgment* — rather than asserting usefulness. The template for every ACL
    metric paper since: incumbent's failure, proposal, correlation evidence.
  - **Self-check:** does your metric paper validate against human judgments
    before using the metric to rank anything?

### Method with a linguistic problem at its core

- **Sennrich, Haddow & Birch, "Neural Machine Translation of Rare Words with
  Subword Units," ACL 2016.** Verified: `aclanthology.org/P16-1162/`.
  - **Why it is an exemplar:** names a concrete linguistic failure (open
    vocabulary: rare words, morphology, compounds) and solves it with a simple
    transferable mechanism (BPE segmentation). The method outlived the model
    family it was built for — the ACL ideal of "the linguistic insight is the
    contribution."
  - **Self-check:** if your architecture were replaced next year, would your
    paper's core idea still matter?

### Model + honest failure analysis

- **See, Liu & Manning, "Get To The Point: Summarization with Pointer-Generator
  Networks," ACL 2017.** Verified: `aclanthology.org/P17-1099/`.
  - **Why it is an exemplar:** pairs the mechanism (copying + coverage) with a
    named behavioral diagnosis of baseline failures — factual errors,
    repetition — and shows the mechanism addressing them, not just a ROUGE
    delta. Error analysis as argument, not appendix filler.
  - **Self-check:** can you name which error classes your method removes, with
    counts, per `acl-experiments`?

### Short paper: one sharp resource claim

- **Rajpurkar, Jia & Liang, "Know What You Don't Know: Unanswerable Questions
  for SQuAD," ACL 2018 (Volume 2: Short Papers).** Verified:
  `aclanthology.org/P18-2124/`.
  - **Why it is an exemplar:** the canonical 4-page shape — one falsifiable
    point (models cannot abstain), one adversarially built dataset, one
    decisive number (a strong system drops from 86 to 66 F1). Nothing padded,
    nothing missing.
  - **Self-check:** does your short paper make exactly one claim a skeptic
    could test from Table 1 alone?

### Analysis / position with quantified stakes

- **Strubell, Ganesh & McCallum, "Energy and Policy Considerations for Deep
  Learning in NLP," ACL 2019.** Verified: `aclanthology.org/P19-1355/`,
  Proceedings of the 57th Annual Meeting, pp. 3645-3650.
  - **Why it is an exemplar:** a critique paper that earns its claims by
    *measuring* (cost and emissions of training regimes) and converts analysis
    into actionable recommendations — the pattern for ACL's ethics-adjacent
    and Limitations-era writing.
  - **Self-check:** does your position/analysis paper quantify the phenomenon
    it critiques, or only narrate it?

### Evaluation methodology (behavioral testing)

- **Ribeiro, Wu, Guestrin & Singh, "Beyond Accuracy: Behavioral Testing of NLP
  Models with CheckList," ACL 2020 (Best Paper).** Verified:
  `aclanthology.org/2020.acl-main.442/`, pp. 4902-4912.
  - **Why it is an exemplar:** argues held-out accuracy overestimates
    capability, then supplies a task-agnostic testing methodology, tooling,
    and a user study showing practitioners find ~3x more bugs. Method +
    instrument + human evidence in one arc — and a model for the checklist-era
    emphasis on evaluation validity.
  - **Self-check:** does your evaluation contribution demonstrate that people
    (or systems) using it find something accuracy alone missed?

---

## Summary table

| Contribution type | Verified ACL exemplar | Anthology ID | Year |
| --- | --- | --- | --- |
| Metric with validity evidence | Papineni et al., "Bleu" | P02-1040 | 2002 |
| Linguistically-motivated method | Sennrich et al., subword units | P16-1162 | 2016 |
| Model + error analysis | See et al., pointer-generator | P17-1099 | 2017 |
| Short-paper resource claim | Rajpurkar et al., SQuAD 2.0 | P18-2124 | 2018 |
| Quantified analysis/position | Strubell et al., energy & policy | P19-1355 | 2019 |
| Behavioral evaluation methodology | Ribeiro et al., CheckList | 2020.acl-main.442 | 2020 |

> Six verified papers across six contribution types, spanning legacy `P`-series
> and modern Anthology IDs so both citation formats are represented.

---

## Omitted as sibling-venue guardrails (do not attribute to ACL)

- **Devlin et al., "BERT"** — NAACL 2019 (`N19-1423`), not ACL. The single most
  common \*ACL misattribution.
- **Peters et al., "Deep Contextualized Word Representations" (ELMo)** — NAACL
  2018, not ACL.
- **Vaswani et al., "Attention Is All You Need"** — NeurIPS 2017; not in the
  Anthology's ACL proceedings at all.
- **Rajpurkar et al., "SQuAD: 100,000+ Questions..."** — EMNLP 2016 (`D`-series);
  only the *2.0* short paper above is ACL.
- **Pennington et al., "GloVe"** — EMNLP 2014, not ACL.

Before adding a row, open the Anthology entry, confirm the venue line says
"Annual Meeting of the Association for Computational Linguistics" (main
proceedings, not Findings, not a workshop), record ID/authors/year, and update
the access date. If verification is unavailable, add the candidate as
**待核实 / TO VERIFY** with no attribution.
