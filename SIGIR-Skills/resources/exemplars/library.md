# SIGIR Exemplars Library (topic × method)

> **Verified via web search, access date 2026-07-08.** Every paper below was checked against
> ACM Digital Library / dblp records (through search renderings — the build environment's
> gateway blocked direct fetches; see the access-method note in
> [`../official-source-map.md`](../official-source-map.md)) to confirm it appeared at the
> **International ACM SIGIR Conference on Research and Development in Information
> Retrieval** specifically — with DOI, pages, and edition matched. Papers that could not be
> cleanly pinned to SIGIR were **omitted and listed as guards below**. Deliberately short:
> six verified beats twenty guessed.
>
> **Sibling-confusion guard:** IR's most-cited papers scatter across EMNLP, ICLR, WWW,
> ICML, NAACL, TOIS, and TREC. A famous "retrieval paper" is *not* automatically a SIGIR
> paper — check the DOI prefix and proceedings title before attributing.
>
> **Use principle (zero hallucination):** rows give **design positioning only** — how each
> paper structures task, evidence, and claim. Do not quote result numbers from this file;
> read the original in the ACM DL first.

---

## How to use this library

Find the row nearest your topic × method, then study how that paper (a) names the
retrieval task and collection regime on page one, (b) pairs each claim with a measured
comparison, and (c) leaves an artifact trail the community could re-run — the SIGIR bar
enforced by [`../../skills/sigir-writing-style/SKILL.md`](../../skills/sigir-writing-style/SKILL.md),
[`../../skills/sigir-experiments/SKILL.md`](../../skills/sigir-experiments/SKILL.md), and
[`../../skills/sigir-artifact-evaluation/SKILL.md`](../../skills/sigir-artifact-evaluation/SKILL.md).

## Verified exemplars

### Language-modeling retrieval (probabilistic ranking foundations)

- **Ponte & Croft, "A Language Modeling Approach to Information Retrieval," SIGIR 1998,
  pp. 275-281, DOI 10.1145/290941.291008.** (SIGIR '98 was held in Melbourne — the same
  city as SIGIR 2026.)
  - **Why it is an exemplar:** replaces a scoring heuristic with an explicit generative
    estimation problem — the model *is* the contribution, and the evaluation is standard
    collections against the era's strongest lexical baseline. The founding template for
    "new retrieval model + fair comparison" SIGIR papers.
  - **Self-check:** can you state your ranking function as a principled estimation
    decision, not a tweak?

### Estimation/smoothing analysis (empirical methodology)

- **Zhai & Lafferty, "A Study of Smoothing Methods for Language Models Applied to Ad Hoc
  Information Retrieval," SIGIR 2001, pp. 334-342, DOI 10.1145/383952.384019.**
  - **Why it is an exemplar:** a *study* paper — no new model, but a systematic,
    multi-collection sensitivity analysis that changed community defaults. Proof that
    SIGIR publishes rigorous secondary analysis; the ancestor of today's Reproducibility
    track genre. (Its extended journal version is TOIS 2004, DOI 10.1145/984321.984322 —
    cite the right one.)
  - **Self-check:** does your analysis paper vary the factor systematically across
    collections, or just report one setting's anecdote?

### Graded-relevance evaluation (evaluation methodology)

- **Järvelin & Kekäläinen, "IR Evaluation Methods for Retrieving Highly Relevant
  Documents," SIGIR 2000 (Athens), pp. 41-48, DOI 10.1145/345508.345545.**
  - **Why it is an exemplar:** argues a validity gap (binary relevance under-credits
    systems that surface *highly* relevant documents) and operationalizes the fix — the
    cumulated-gain lineage that led to nDCG. The template for "the metric itself is the
    contribution" papers.
  - **Self-check:** does your evaluation proposal demonstrate a decision the old metric
    gets wrong and the new one gets right? **Attribution trap:** the widely-cited
    "Cumulated Gain-Based Evaluation of IR Techniques" is **TOIS 2002**, not this paper.

### Graph collaborative filtering (recommendation)

- **Wang, He, Wang, Feng & Chua, "Neural Graph Collaborative Filtering," SIGIR 2019
  (Paris), DOI 10.1145/3331184.3331267.**
  - **Why it is an exemplar:** injects the collaborative signal into embeddings via
    explicit propagation on the user-item graph, evaluated on multiple public interaction
    datasets with released code — recommendation done in SIGIR register.
  - **Self-check:** is your recommendation contribution a mechanism on the interaction
    structure, with public-split comparability?

- **He, Deng, Wang, Li, Zhang & Wang, "LightGCN: Simplifying and Powering Graph
  Convolution Network for Recommendation," SIGIR 2020, DOI 10.1145/3397271.3401063.**
  - **Why it is an exemplar:** an *ablation-as-contribution* paper — strips NGCF's feature
    transforms and nonlinearities and shows the simpler linear propagation wins. The
    NGCF → LightGCN pair is a model research line inside SIGIR: build, then simplify with
    evidence.
  - **Self-check:** if your method beats its predecessor, do you know *which removed or
    added piece* is responsible?

### Late-interaction neural ranking (efficiency-quality trade-off)

- **Khattab & Zaharia, "ColBERT: Efficient and Effective Passage Search via
  Contextualized Late Interaction over BERT," SIGIR 2020 (virtual), DOI
  10.1145/3397271.3401075.**
  - **Why it is an exemplar:** the claim is two-dimensional (effectiveness *and* cost)
    and every table honors both dimensions — quality against BERT re-rankers, latency and
    FLOPs against the same. The modern template for "we move the Pareto frontier" SIGIR
    papers.
  - **Self-check:** if you claim efficiency, does a cost table sit beside every quality
    table at matched operating points?

## Topic × method map

| Topic | Verified exemplar | Edition / DOI | Method family |
| --- | --- | --- | --- |
| Retrieval models | Ponte & Croft | 1998 / 10.1145/290941.291008 | Language modeling |
| Empirical methodology | Zhai & Lafferty | 2001 / 10.1145/383952.384019 | Systematic smoothing study |
| Evaluation | Järvelin & Kekäläinen | 2000 / 10.1145/345508.345545 | Graded-relevance metrics |
| Recommendation | Wang et al. (NGCF) | 2019 / 10.1145/3331184.3331267 | Graph propagation CF |
| Recommendation (simplification) | He et al. (LightGCN) | 2020 / 10.1145/3397271.3401063 | Linear graph convolution |
| Neural ranking + efficiency | Khattab & Zaharia (ColBERT) | 2020 / 10.1145/3397271.3401075 | Late interaction |

## Misattribution guards (checked — do NOT cite these as SIGIR)

- **DPR — Karpukhin et al., "Dense Passage Retrieval for Open-Domain Question
  Answering"**: **EMNLP 2020**, not SIGIR.
- **ANCE — Xiong et al., approximate-nearest-neighbor negative contrastive
  learning**: **ICLR 2021**, not SIGIR.
- **NCF — He et al., "Neural Collaborative Filtering"**: **WWW 2017**, not SIGIR
  (its successors NGCF/LightGCN above *are* SIGIR).
- **RankNet — Burges et al.**: **ICML 2005**, not SIGIR.
- **BERT — Devlin et al.**: **NAACL 2019**; "BERT for ranking" claims need the actual
  ranking-paper venues checked one by one.
- **"Cumulated Gain-Based Evaluation of IR Techniques" — Järvelin & Kekäläinen**:
  **TOIS 2002** (journal), distinct from their SIGIR 2000 paper above.
- **BM25**: cite the Robertson-era TREC/SIGIR-lineage papers for the model and the
  toolkit paper (e.g., Anserini) separately for the implementation — "the BM25 paper"
  is not a single SIGIR citation.

Before adding a row, confirm the proceedings title ("...International ACM SIGIR
Conference on Research and Development in Information Retrieval"), DOI, and pages via
the ACM DL or dblp, then record the access date. When in doubt, put the candidate under
guards, not exemplars. If verification tooling is unavailable, add it as 待核实 with no
attribution.
