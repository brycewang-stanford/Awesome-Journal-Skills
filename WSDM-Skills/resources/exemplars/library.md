# WSDM Exemplars Library (lineage × era)

> **Verified via web search on 2026-07-08.** Every row below was confirmed against the
> ACM Digital Library and/or dblp as appearing in a WSDM proceedings volume - title,
> authors, edition, and DOI or dblp key. Papers that could not be cleanly pinned to
> WSDM were left out or moved to the misattribution guard at the bottom. Short and
> verified beats long and guessed.
>
> **Use principle (zero hallucination):** these entries give *positioning patterns*
> only. No result numbers, dataset statistics, or theorem contents are reproduced
> here - read the original in the ACM DL before citing anything beyond the
> bibliographic record.

---

## How to use this library

Each exemplar anchors one of WSDM's long-running research lineages (the table in
[`../../skills/wsdm-related-work/SKILL.md`](../../skills/wsdm-related-work/SKILL.md)
routes a new paper into them). For the row nearest your project, study how the
paper (a) grounds itself in a behavioral fact about web or social data, (b) pairs
a practical setting with a principled mechanism, and (c) scopes its claims to its
data regime - then answer the self-check honestly.

---

## The five verified exemplars

### 1. Click models / position bias - the venue's founding lineage

**Craswell, Zoeter, Taylor & Ramsey, "An experimental comparison of click
position-bias models," WSDM 2008, pp. 87-94. DOI 10.1145/1341531.1341545**
(dblp: `conf/wsdm/CraswellZTR08`). A first-edition WSDM paper.

- **Why it is an exemplar:** takes a single behavioral fact - the probability of
  a click depends on a result's position, not only its relevance - and turns it
  into a model-comparison study, finding the cascade model best explains
  early-rank position bias. The entire click-modeling and propensity-estimation
  literature that WSDM still publishes descends from framing of this kind.
- **Self-check:** can you state, in one sentence, the user-behavior regularity
  your paper models or corrects - and would a log of real interactions exhibit it?

### 2. Unbiased learning-to-rank - principled correction of practical data

**Joachims, Swaminathan & Schnabel, "Unbiased Learning-to-Rank with Biased
Feedback," WSDM 2017 (10th edition, Cambridge, UK), pp. 781-789.
DOI 10.1145/3018661.3018699** (dblp: `conf/wsdm/JoachimsSS17`).

- **Why it is an exemplar:** the canonical WSDM shape - implicit feedback is
  abundant but biased, and the paper supplies a counterfactual estimator
  (inverse propensity weighting for ranking) with theoretical grounding, then
  evidence. "Practical yet principled" as a single paper.
- **Self-check:** if your data is logged under some policy, does your method
  acknowledge the logging bias, and is the correction itself a contribution?

### 3. Sequential recommendation - the neural-era lineage

**Tang & Wang, "Personalized Top-N Sequential Recommendation via Convolutional
Sequence Embedding" (Caser), WSDM 2018 (11th edition).
DOI 10.1145/3159652.3159656.**

- **Why it is an exemplar:** treats a sequence of recent user interactions as an
  "image" over time and latent dimensions and applies convolutional filters to
  capture union-level and point-level sequential patterns - a crisp, nameable
  mechanism for a user-behavior problem, which is why it became a standard
  baseline in the sequential-recommendation literature.
- **Self-check:** does your model design map to a specific structure in user
  behavior, or is it an architecture transplant justified only by metrics?

### 4. Off-policy RL for production recommendation - the industry lineage

**Chen, Beutel, Covington, Jain, Belletti & Chi, "Top-K Off-Policy Correction
for a REINFORCE Recommender System," WSDM 2019 (12th edition, Melbourne),
pp. 456-464** (dblp: `conf/wsdm/ChenBCJBC19`; Google/YouTube).

- **Why it is an exemplar:** production-scale reinforcement learning for
  recommendation with an explicit off-policy correction for learning from logged
  feedback under a top-K action space - industrial evidence and a principled
  estimator in the same paper. The model for how platform teams publish at WSDM
  without reducing the paper to a system report.
- **Self-check:** if your evidence is production-derived, does the paper still
  contain a mechanism an outsider can implement and test?

### 5. Community detection at scale - the graph/social lineage

**Yang & Leskovec, "Overlapping community detection at scale: a nonnegative
matrix factorization approach" (BigCLAM), WSDM 2013 (6th edition), pp. 587-596.
DOI 10.1145/2433396.2433471** (dblp: `conf/wsdm/YangL13`).

- **Why it is an exemplar:** reformulates overlapping community detection as
  scalable nonnegative matrix factorization driven by an observation about how
  real social communities overlap - a graph-mining contribution where the
  modeling assumption comes from measured network structure, and scalability is
  part of the claim rather than an afterthought.
- **Self-check:** does your graph paper state which structural property of real
  networks it exploits, and does the evaluation include a genuinely large graph?

---

## Lineage × era grid

| Lineage | Exemplar | Edition | Era lesson |
| --- | --- | --- | --- |
| Click models / bias | Craswell et al. | 2008 (1st) | Behavioral regularity → model comparison |
| Unbiased LTR | Joachims et al. | 2017 (10th) | Logged data → counterfactual correction |
| Sequential rec | Tang & Wang | 2018 (11th) | Behavior structure → nameable architecture |
| RL for rec (industry) | Chen et al. | 2019 (12th) | Production setting → principled estimator |
| Graph/social mining | Yang & Leskovec | 2013 (6th) | Network measurement → scalable formulation |

Note the arc the grid teaches: across eras and subareas, the constant WSDM shape
is *measured web/social behavior first, mechanism second, scale-honest evidence
third*. Fresh exemplars from the two most recent editions should be added (with
DOIs) each cycle - recent-edition positioning matters more to reviewers than any
classic.

---

## Misattribution guard (do not cite these to WSDM)

Venue errors on famous neighbors are credibility damage in front of a PC that
knows exactly where these appeared:

- **DeepWalk (2014), node2vec (2016), XGBoost (2016)** - KDD.
- **BERT4Rec (2019)** - CIKM.
- **Neural Graph Collaborative Filtering (2019)** - SIGIR.
- **SASRec (2018)** - ICDM.
- **"WTF: The Who to Follow Service at Twitter" (2013)** - WWW.
- The **Tomkins-Zhang-Heavlin reviewing experiment** was *conducted at* WSDM 2017
  but *published in* PNAS (2017) - cite the PNAS article, not the proceedings.

Before adding any row above or below this line, resolve the paper on dblp
(`dblp.org/db/conf/wsdm/`) or the ACM DL and record the DOI. If verification is
unavailable, add it as 待核实 with no venue attribution.
