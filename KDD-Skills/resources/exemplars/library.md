# KDD Exemplars Library (topic × contribution shape)

> **Verified via web search, access date 2026-07-08.** Every entry below was confirmed against the
> **ACM Digital Library / DBLP** record for an ACM SIGKDD Conference proceedings volume (DOI prefix
> `10.1145/...`), matching title, authors, year, and pages or DOI. Papers that could not be cleanly
> placed in a KDD proceedings volume were left out — a short list that is actually KDD beats a long
> list that quietly mixes in neighbors.
>
> **Neighbor-confusion guard:** KDD is **not** ICDM, SDM, WSDM, CIKM, WWW, RecSys, or NeurIPS. Many
> celebrated "data mining" papers live at those venues (isolation forests at ICDM, LightGBM at
> NeurIPS, Wide & Deep at a RecSys workshop). Citing them as "KDD papers" is a credibility leak in a
> related-work section. Each row below names its DOI so the venue claim is checkable in one click.
>
> **Use principle (zero hallucination):** this library supports **positioning only**. It never
> restates experimental numbers, speedups, or dataset sizes from memory — open the DOI before quoting
> anything. Policy and formatting facts live in [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Find the row closest to your contribution shape, then study how that paper makes a **mining or
systems idea legible at scale**: a named algorithmic mechanism, evidence on large or real data, and
an efficiency or deployment story reviewers can audit. Pair each row's self-check with
[`../../skills/kdd-topic-selection/SKILL.md`](../../skills/kdd-topic-selection/SKILL.md) (Research vs
ADS routing), [`../../skills/kdd-experiments/SKILL.md`](../../skills/kdd-experiments/SKILL.md)
(scale and ablation evidence), and
[`../../skills/kdd-writing-style/SKILL.md`](../../skills/kdd-writing-style/SKILL.md).

---

## Research Track shapes

### Scalable learning system with algorithmic novelty

- **Chen & Guestrin, "XGBoost: A Scalable Tree Boosting System," KDD 2016, pp. 785-794.**
  DOI: `10.1145/2939672.2939785`.
  - **Why it is an exemplar:** the contribution is a **system whose speed comes from named
    algorithmic ideas** (sparsity-aware split finding, cache-aware and out-of-core computation), not
    from unexplained engineering. KDD rewards exactly this pairing: each performance claim traces to
    a mechanism the paper describes and ablates.
  - **Self-check:** can every efficiency claim in your paper be attributed to a specific, described
    design decision rather than to "optimized implementation"?

### Representation learning on graphs (method with a tunable primitive)

- **Grover & Leskovec, "node2vec: Scalable Feature Learning for Networks," KDD 2016, pp. 855-864.**
  DOI: `10.1145/2939672.2939754`.
  - **Why it is an exemplar:** introduces one clean primitive — **biased random walks interpolating
    breadth-first and depth-first exploration** — and shows the primitive, not a pipeline, drives
    results across tasks and networks. The generality argument is structural, not rhetorical.
  - **Self-check:** does your method reduce to one nameable, parameterized mechanism a reviewer
    could re-implement from the paper alone?

- **Perozzi, Al-Rfou & Skiena, "DeepWalk: Online Learning of Social Representations," KDD 2014,
  pp. 701-710.** DOI: `10.1145/2623330.2623732`.
  - **Why it is an exemplar:** an **idea transfer made rigorous** — treating truncated random walks
    as sentences so language-model machinery applies to graphs — with the analogy defended (degree
    and word-frequency distributions) rather than merely asserted. Model for "borrowed technique,
    new domain" framings, the most common KDD submission genre.
  - **Self-check:** if your paper transfers a technique across domains, is the transfer justified by
    a property of the data rather than by fashion?

### Heterogeneous-data mining

- **Dong, Chawla & Swami, "metapath2vec: Scalable Representation Learning for Heterogeneous
  Networks," KDD 2017.** DOI: `10.1145/3097983.3098036`.
  - **Why it is an exemplar:** identifies a concrete failure of homogeneous methods on typed nodes
    and edges, then fixes it with **meta-path-guided walks plus a heterogeneous skip-gram** — the
    delta over DeepWalk/node2vec is stated as a structural claim about the data, the KDD way of
    positioning against one's own lineage.
  - **Self-check:** is your improvement tied to a property of the data regime (heterogeneity, drift,
    sparsity, scale) that the predecessor provably or demonstrably mishandles?

## Applied Data Science shapes

### Deployed industrial system with lessons learned

- **McMahan et al., "Ad Click Prediction: a View from the Trenches," KDD 2013.**
  DOI: `10.1145/2487575.2488200`.
  - **Why it is an exemplar:** the canonical **deployment paper** — a production CTR system where
    the contribution includes what worked, what failed, and why (online learning at scale, memory
    savings, calibration, and negative results). This is the register the ADS track's post-launch
    performance requirement asks for: measured production behavior, not offline benchmarks alone.
  - **Self-check:** does your ADS draft quantify **post-launch** performance and report at least one
    honest negative or surprise from deployment?

---

## By contribution shape (all rows verified above)

| Contribution shape | Verified KDD exemplar | Year / DOI | Track register |
| --- | --- | --- | --- |
| Scalable system + algorithmic mechanism | Chen & Guestrin, "XGBoost" | 2016 / 10.1145/2939672.2939785 | Research |
| One-primitive graph method | Grover & Leskovec, "node2vec" | 2016 / 10.1145/2939672.2939754 | Research |
| Cross-domain technique transfer | Perozzi et al., "DeepWalk" | 2014 / 10.1145/2623330.2623732 | Research |
| Heterogeneous-data extension of a lineage | Dong et al., "metapath2vec" | 2017 / 10.1145/3097983.3098036 | Research |
| Deployed system + lessons learned | McMahan et al., "Ad Click Prediction" | 2013 / 10.1145/2487575.2488200 | Applied / ADS register |

> The DeepWalk → node2vec → metapath2vec chain is itself instructive: three KDD papers forming one
> research lineage, each stating its structural delta over the previous one. Use it as the template
> for positioning an extension paper without sounding incremental.

---

## Omitted after checking (do not attribute to KDD without re-verifying)

- **Liu, Ting & Zhou, "Isolation Forest"** — published at **ICDM 2008**, not KDD. A classic
  data-mining venue trap.
- **Ke et al., "LightGBM"** — **NeurIPS 2017**, not KDD, despite living in every gradient-boosting
  related-work section next to XGBoost.
- **Cheng et al., "Wide & Deep Learning for Recommender Systems"** — a **RecSys 2016 workshop
  (DLRS)** paper, not KDD.
- **"Attention Is All You Need," "BERT," GraphSAGE** — NeurIPS / NAACL / NeurIPS respectively;
  frequently cited alongside KDD graph papers but not KDD publications.

Before adding a new exemplar, confirm the ACM DL or DBLP record shows an ACM SIGKDD Conference
proceedings volume, record title/authors/year/DOI, and refresh the access-date header. If the venue
cannot be confirmed, add the row as **待核实 / TO VERIFY** with no venue attribution, or omit it.
