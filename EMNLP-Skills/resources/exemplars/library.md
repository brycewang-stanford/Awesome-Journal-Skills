# EMNLP Exemplars Library (topic × method)

> **Verified via web search, access date 2026-07-08.** Every paper below was checked against the
> **ACL Anthology** (`aclanthology.org/...`) to confirm it appeared in an **EMNLP main-conference
> proceedings volume** — matching the Anthology ID to the EMNLP edition, plus author list, page range,
> and host city. Papers that could not be cleanly pinned to EMNLP (as opposed to a sibling ACL-family
> venue, a workshop, TACL, or a non-ACL venue) were **omitted and documented below**. Six verified rows
> beat fifteen guessed ones.
>
> **Sibling-confusion guard:** the ACL Anthology hosts ACL, NAACL, EACL, AACL, CoNLL, LREC-COLING,
> TACL, WMT, and hundreds of workshops alongside EMNLP. An Anthology URL alone does **not** prove EMNLP:
> `D`-prefixed IDs (through 2019) and `20XX.emnlp-main` IDs are EMNLP; `P`/`20XX.acl-long` are ACL;
> `N` is NAACL; `20XX.findings-emnlp` is the Findings companion, not the main proceedings. Several
> famous "NLP papers" live at ICLR or NeurIPS and never touched EMNLP at all.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It reproduces no
> result numbers, leaderboard scores, or table values — read the original on the Anthology before citing
> anything. For EMNLP-specific policy see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row closest to your **topic × method**, then study how that paper earns the EMNLP bar: a
concrete language-processing problem stated before any architecture, evaluation designed to expose
failure rather than flatter the method, and error analysis that explains *what* the model gets wrong
(see [`../../skills/emnlp-writing-style/SKILL.md`](../../skills/emnlp-writing-style/SKILL.md),
[`../../skills/emnlp-experiments/SKILL.md`](../../skills/emnlp-experiments/SKILL.md), and
[`../../skills/emnlp-topic-selection/SKILL.md`](../../skills/emnlp-topic-selection/SKILL.md)). Ask each
row's self-check question before calling your draft "EMNLP-shaped."

**Anthology ID ↔ EMNLP edition (verified rows below):** D14 = EMNLP 2014 (Doha); D15 = EMNLP 2015
(Lisbon); D16 = EMNLP 2016 (Austin); D19 = EMNLP-IJCNLP 2019 (Hong Kong); 2020.emnlp-main = EMNLP 2020
(online).

---

## By method

### Distributional representation learning (word vectors)

- **Pennington, Socher & Manning, "GloVe: Global Vectors for Word Representation," EMNLP 2014,
  Anthology D14-1162, pp. 1532-1543 (Doha, Qatar).**
  Verified: `aclanthology.org/D14-1162/`.
  - **Why it is an exemplar:** derives the model from an explicit property of co-occurrence
    statistics, then evaluates on multiple task families rather than one. The claim scope matches
    the evidence — a very EMNLP virtue.
  - **Self-check:** does your representation paper explain *why* the objective should capture the
    linguistic signal, or only that scores went up?

### Neural machine translation with attention (structured generation)

- **Luong, Pham & Manning, "Effective Approaches to Attention-based Neural Machine Translation,"
  EMNLP 2015, Anthology D15-1166, pp. 1412-1421 (Lisbon, Portugal).**
  Verified: `aclanthology.org/D15-1166/`.
  - **Why it is an exemplar:** a careful empirical comparison of design variants (global vs local
    attention) on a shared task, with analysis of where each helps — the "empirical methods"
    genre in its purest form.
  - **Self-check:** when you propose variants, do you test them under matched conditions and report
    which one wins *where*, not just on average?

### Benchmark dataset construction (reading comprehension)

- **Rajpurkar, Zhang, Lopyrev & Liang, "SQuAD: 100,000+ Questions for Machine Comprehension of
  Text," EMNLP 2016, Anthology D16-1264, pp. 2383-2392 (Austin, Texas).**
  Verified: `aclanthology.org/D16-1264/`.
  - **Why it is an exemplar:** a resource paper that documents collection, analyzes the reasoning
    types the data demands, establishes human performance, and shows the model-human gap — the
    template EMNLP dataset reviewers still grade against.
  - **Self-check:** does your dataset paper characterize what the data *requires* of a model, with a
    human ceiling, or only report its size?

### Sentence-level representation for retrieval (model adaptation)

- **Reimers & Gurevych, "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks,"
  EMNLP-IJCNLP 2019, Anthology D19-1410, pp. 3982-3992 (Hong Kong).**
  Verified: `aclanthology.org/D19-1410/`.
  - **Why it is an exemplar:** motivates the method from a concrete computational failure of the
    status quo (pairwise cross-encoding does not scale to retrieval), then verifies both quality and
    the claimed efficiency. Practical impact grounded in measurement.
  - **Self-check:** if your pitch includes efficiency, is the efficiency itself measured and
    reported, not just asserted?

### Experimental methodology (reporting and budgets)

- **Dodge, Gururangan, Card, Schwartz & Smith, "Show Your Work: Improved Reporting of Experimental
  Results," EMNLP-IJCNLP 2019, Anthology D19-1224, pp. 2185-2194 (Hong Kong).**
  Verified: `aclanthology.org/D19-1224/`.
  - **Why it is an exemplar:** shows that "best score" comparisons flip once the hyperparameter
    search budget is controlled, and proposes reporting expected validation performance as a
    function of budget. EMNLP publishing a critique of its own evaluation habits is the venue's
    identity in one paper.
  - **Self-check:** would your headline comparison survive if both systems were given the same
    tuning budget — and do you report that budget?

### Statistical rigor of NLP evaluation (meta-analysis)

- **Card, Henderson, Khandelwal, Jia, Mahowald & Jurafsky, "With Little Power Comes Great
  Responsibility," EMNLP 2020, Anthology 2020.emnlp-main.745.**
  Verified: `aclanthology.org/2020.emnlp-main.745/`.
  - **Why it is an exemplar:** a meta-analysis showing typical NLP experiments are statistically
    underpowered, so small reported gains are often indistinguishable from noise. It anchors the
    significance-testing and sample-size expectations that EMNLP reviewers now apply.
  - **Self-check:** is your claimed improvement large enough, on a test set large enough, for the
    difference to be detectable — and did you run the test?

---

## By topic (each cell is a verified EMNLP paper above)

| Topic | Verified EMNLP exemplar | Edition / Anthology ID | Method |
| --- | --- | --- | --- |
| Word representations | Pennington, Socher & Manning, "GloVe" | 2014 / D14-1162 | Count-based log-bilinear vectors |
| Machine translation | Luong, Pham & Manning, "Effective Approaches to Attention-based NMT" | 2015 / D15-1166 | Attention-variant comparison |
| QA / benchmark resources | Rajpurkar et al., "SQuAD" | 2016 / D16-1264 | Crowdsourced dataset + analysis |
| Semantic similarity / retrieval | Reimers & Gurevych, "Sentence-BERT" | 2019 / D19-1410 | Siamese fine-tuning |
| Evaluation methodology | Dodge et al., "Show Your Work" | 2019 / D19-1224 | Budget-aware reporting |
| Statistical rigor | Card et al., "With Little Power Comes Great Responsibility" | 2020 / 2020.emnlp-main.745 | Power meta-analysis |

> Six verified papers across six topic × method cells. The two methodology rows (Show Your Work; With
> Little Power) matter double: they are simultaneously exemplars *and* the standards your experiments
> section will be judged by.

---

## Omitted for lack of clean EMNLP verification (do not attribute to EMNLP without re-checking)

Excluded after checking, several being exactly the sibling-venue traps the header warns about:

- **Devlin et al., "BERT"** — NAACL 2019 (N19-1423), **not EMNLP**. The single most common
  misattribution in NLP-venue lists.
- **Ribeiro et al., "Beyond Accuracy: Behavioral Testing of NLP Models with CheckList"** — ACL 2020,
  not EMNLP; a natural-seeming fit for the evaluation rows above, which is why it is listed here as a
  guardrail.
- **Zhang et al., "BERTScore"** — ICLR 2020; lives on OpenReview/arXiv, not in the Anthology's EMNLP
  volumes.
- **Papineni et al., "BLEU"** — ACL 2002 (P02-1040), not EMNLP.
- **Vaswani et al., "Attention Is All You Need"** — NeurIPS 2017; cited in half of EMNLP but published
  nowhere near it.

Before adding a row, open the paper's Anthology landing page, confirm the volume title names the
Conference on Empirical Methods in Natural Language Processing (main proceedings, not Findings, not a
co-located workshop), then record authors, pages, host city, and update the access-date header. When
verification is unavailable, add the row as **待核实 / TO VERIFY** with no attribution.
