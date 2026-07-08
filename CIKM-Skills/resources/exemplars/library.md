# CIKM Exemplars Library (lane × era)

> **Verified via web search, access date 2026-07-08.** Every paper below was checked
> against **dblp** (`dblp.org/rec/conf/cikm/...`) and, where retrievable, the **ACM
> Digital Library**, confirming it appeared at the ACM International Conference on
> Information and Knowledge Management — with the edition, host city, and page range
> matched. Candidates that could not be cleanly pinned to CIKM were **omitted and
> logged below**. Short and verified beats long and guessed.
>
> **Sibling-confusion guard:** CIKM's neighbors publish look-alike classics, and the
> IR/mining/KM literature hops venues paper by paper. A famous "graph embedding" or
> "sequential recommendation" paper is *not* CIKM by default — see the omissions list,
> which names the traps actually checked. Before adding any row, open the dblp
> `conf/cikm` record for that exact year.
>
> **Use principle (zero hallucination):** rows give **positioning value only** — why
> each paper is a model of a CIKM-shaped contribution. No result numbers, benchmark
> scores, or architecture details are reproduced here; read the original before citing
> anything beyond the bibliographic record. Policy and cycle facts live in
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Find the row nearest your project's **lane combination** (retrieval × mining × KM),
then study how that paper frames a boundary contribution — the move
[`cikm-writing-style`](../../skills/cikm-writing-style/SKILL.md) calls the
"why the boundary is the hard part" sentence — and answer its self-check before
claiming your paper is CIKM-shaped. Pair with
[`cikm-topic-selection`](../../skills/cikm-topic-selection/SKILL.md) for the venue
decision and [`cikm-related-work`](../../skills/cikm-related-work/SKILL.md) for the
misattribution discipline these rows enforce.

**Edition anchors for the rows below:** 19th = CIKM 2010 (Toronto); 22nd = 2013;
24th = 2015; 25th = 2016; 27th = 2018 (Torino); 28th = 2019 (Beijing).

---

## The verified six

### Entity linking for short text (KM × IR)

- **Ferragina & Scaiella, "TAGME: on-the-fly annotation of short text fragments (by
  wikipedia entities)," CIKM 2010, pp. 1625-1628.** Verified:
  `dblp.org/rec/conf/cikm/FerraginaS10.html`; ACM DL DOI 10.1145/1871437.1871689.
  Reported recipient of the 2023 CIKM Test of Time Award (secondary sources; 待核实
  on the official award page).
  - **Why it is an exemplar:** takes a knowledge-management primitive (linking text
    to an encyclopedia's entities) and makes it fast and robust enough for IR-scale
    inputs — snippets, tweets, queries. A four-page-scale idea whose value is the
    *operating point*, not a new model class: quintessential CIKM.
  - **Self-check:** does your contribution make a knowledge operation usable under
    retrieval-grade constraints (latency, brevity, noise)?

### Click-supervised semantic matching (IR × mining, industry-born)

- **Huang, He, Gao, Deng, Acero & Heck, "Learning Deep Structured Semantic Models
  for Web Search using Clickthrough Data," CIKM 2013.** Verified via dblp/CIKM 2013
  proceedings and the authors' publication records (Microsoft Research).
  - **Why it is an exemplar:** DSSM turned behavioral exhaust — clickthrough logs —
    into supervision for semantic matching between queries and documents, a
    mining-lane data insight serving an IR-lane goal, authored from industry. The
    pattern "organizational data asset + representation learning + search payoff"
    remains CIKM's house genre.
  - **Self-check:** does your paper convert a data source one community owns into a
    capability another community needs?

### Graph representation learning (mining × KM)

- **Cao, Lu & Xu, "GraRep: Learning Graph Representations with Global Structural
  Information," CIKM 2015, pp. 891-900.** Verified:
  `dblp.org/rec/conf/cikm/CaoLX15.html`; ACM DL DOI 10.1145/2806416.2806512.
  - **Why it is an exemplar:** CIKM's own milestone in the graph-embedding lineage,
    explicitly positioned against DeepWalk (a KDD paper) by capturing global
    structure — a worked example of stating a delta against a *sibling venue's*
    method, which is what CIKM related-work sections must do.
  - **Self-check:** can you name the nearest KDD/SIGIR/WSDM method and the structural
    information it discards that you keep?

### Relevance matching as its own problem (IR)

- **Guo, Fan, Ai & Croft, "A Deep Relevance Matching Model for Ad-hoc Retrieval,"
  CIKM 2016.** Verified: `dblp.org/rec/conf/cikm/GuoFAC16.html`.
  - **Why it is an exemplar:** DRMM's contribution begins with a *distinction* —
    relevance matching is not the semantic matching NLP models optimize — and builds
    the model from that analysis. The argument-before-architecture structure is the
    strongest opening a method paper can bring to CIKM's blended panel.
  - **Self-check:** does your paper articulate why the neighboring community's
    formulation of the task is the wrong one for your setting?

### Knowledge-graph-aware recommendation (KM × mining × IR — three lanes)

- **Wang, Zhang, Wang, Zhao, Li, Xie & Guo, "RippleNet: Propagating User Preferences
  on the Knowledge Graph for Recommender Systems," CIKM 2018, pp. 417-426.**
  Verified: `dblp.org/rec/conf/cikm/WangZWZLXG18.html`; ACM DL DOI
  10.1145/3269206.3271739; 27th CIKM, Torino.
  - **Why it is an exemplar:** unifies the two prior families (embedding-based and
    path-based KG recommendation) with a propagation mechanism — a genuine
    three-lane paper where the KG is load-bearing, not decorative, exactly the
    "KG-quality sweep" standard `cikm-experiments` demands.
  - **Self-check:** if the knowledge structure were replaced by random side
    information, would your gains survive? (They should not.)

### Bidirectional sequence modeling for recommendation (mining × IR)

- **Sun, Liu, Wu, Pei, Lin, Ou & Jiang, "BERT4Rec: Sequential Recommendation with
  Bidirectional Encoder Representations from Transformer," CIKM 2019.** Verified:
  `dblp.org/rec/conf/cikm/SunLWPLOJ19.html`; 28th CIKM, Beijing.
  - **Why it is an exemplar:** imports a then-new NLP training scheme into the
    interaction-mining setting with the adaptation argument made explicit (why
    bidirectionality and the cloze objective fit behavior sequences). A model for
    the "LLM-era import" paper CIKM now receives in volume — the bar is the
    *adaptation argument*, not the import itself.
  - **Self-check:** does your import explain what breaks without the adaptation,
    with the ablation to match?

---

## Lane coverage matrix

| Lane combination | Exemplar | Edition | Contribution pattern |
| --- | --- | --- | --- |
| KM × IR | TAGME | 2010 (19th, Toronto) | Knowledge primitive at retrieval speed |
| IR × mining | DSSM | 2013 (22nd) | Behavioral data as supervision |
| Mining × KM | GraRep | 2015 (24th) | Structure-aware embedding, sibling-delta framing |
| IR (boundary-argued) | DRMM | 2016 (25th) | Task distinction before architecture |
| KM × mining × IR | RippleNet | 2018 (27th, Torino) | KG as load-bearing signal |
| Mining × IR | BERT4Rec | 2019 (28th, Beijing) | Cross-field import with adaptation argument |

Six verified rows spanning 2010-2019 and every pairwise lane combination — including
one three-lane paper, the profile `cikm-topic-selection` calls the sweet spot.

---

## Omitted after checking (do not attribute to CIKM)

Each of these was considered and **excluded** — they are the misattribution traps a
CIKM bibliography most often contains:

- **DeepWalk (Perozzi et al.) and node2vec (Grover & Leskovec)** — both **KDD**
  (2014, 2016). CIKM's graph-embedding entry in that lineage is GraRep, which cites
  DeepWalk as its contrast.
- **SASRec (Kang & McAuley), "Self-Attentive Sequential Recommendation"** —
  **ICDM 2018**, not CIKM; the transformer-recommender that *is* CIKM is BERT4Rec.
- **NGCF (Wang et al. 2019) and LightGCN (He et al. 2020)** — both **SIGIR**.
  Graph-collaborative-filtering classics live there even though the topic reads
  CIKM-native.
- **Conv-KNRM (Dai et al.)** — **WSDM 2018**; its sibling K-NRM is SIGIR 2017. The
  neural-matching lineage crosses venues almost yearly; check each hop.
- **TransE (Bordes et al.)** — **NeurIPS 2013**. KG embedding's origin paper is not
  at the KG-applications venue.

Before adding a row: confirm the dblp `conf/cikm` record for the exact year, match
the edition number and host city, record authors and pages, and update the access
date above. No clean record — no row; if search is unavailable, add it as
**待核实 / TO VERIFY** with no venue attribution.
