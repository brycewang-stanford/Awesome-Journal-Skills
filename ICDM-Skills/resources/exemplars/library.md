# ICDM Exemplars Library (topic × method)

> **Verified via the IEEE ICDM awards roster and dblp, access date 2026-07-09.** Every paper below
> was confirmed to have appeared at the **IEEE International Conference on Data Mining (ICDM)** by
> matching the **ICDM edition and year** on the official awards pages
> (`icdm.zhonghuapu.com/Awards/...`) and cross-checking **dblp** (`dblp.org/db/conf/icdm`). Papers
> that could not be cleanly confirmed as **ICDM** — as opposed to KDD, CIKM, WSDM, SDM, VLDB, or a
> journal — were **omitted and documented below**. This is deliberately a short, verified list.
>
> **Sibling-confusion guard:** ICDM is **IEEE**-sponsored. It is **not** ACM's KDD/CIKM/WSDM and
> **not** SIAM's SDM. Data-mining fame does not imply ICDM placement: several canonical
> "data-mining" papers actually live at KDD, WWW, or in JMLR/JAIR (see omissions). Each row below
> was checked to be an ICDM edition specifically.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent result numbers, constants, or table values — read the original on IEEE Xplore
> before citing anything. For ICDM-specific policy and the do-not-misattribute list, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **topic × method** is closest to yours, then study how that paper earns an ICDM
slot: a **named data-mining mechanism** on a clearly defined mining task, **strong empirical
baselines**, and a **scalability or discovery-validity argument** that a data-centric IEEE reviewer
can check (the ICDM bar — see
[`../../skills/icdm-writing-style/SKILL.md`](../../skills/icdm-writing-style/SKILL.md),
[`../../skills/icdm-topic-selection/SKILL.md`](../../skills/icdm-topic-selection/SKILL.md), and
[`../../skills/icdm-experiments/SKILL.md`](../../skills/icdm-experiments/SKILL.md)). For each, ask
the self-check before claiming your paper is "ICDM-shaped." Award-winner status is a longevity
signal, not a template to imitate.

---

## By method

### Node proximity on graphs (graph mining / random walks)

- **Tong, Faloutsos & Pan, "Fast Random Walk with Restart and Its Applications," ICDM 2006.**
  Verified: IEEE ICDM **2015 10-Year Highest-Impact Paper Award** (awards roster) + dblp ICDM 2006.
  - **Why it is an exemplar:** takes a well-defined proximity primitive (random walk with restart)
    and makes it **fast enough to be a reusable building block** across applications — the ICDM
    move of turning a mining primitive into infrastructure, not one benchmark win.
  - **Self-check:** is your contribution a mining primitive others can reuse, with an explicit
    cost/scaling argument, rather than a single tuned pipeline?

### Unsupervised anomaly detection (isolation-based mining)

- **Liu, Ting & Zhou, "Isolation Forest," ICDM 2008.**
  Verified: IEEE ICDM **Best Theoretical/Algorithms Paper** recognition (awards roster) + dblp ICDM
  2008.
  - **Why it is an exemplar:** reframes anomaly detection around **isolating** points instead of
    profiling normality, giving a linear-time, low-memory method — a mechanism-first idea whose
    novelty is the *principle*, not a leaderboard.
  - **Self-check:** can you state the single mechanism that makes your method work, and defend it
    with complexity and ablation evidence rather than aggregate accuracy alone?

### Recommendation from implicit signals (collaborative filtering)

- **Hu, Koren & Volinsky, "Collaborative Filtering for Implicit Feedback Datasets," ICDM 2008.**
  Verified: IEEE ICDM **2017 10-Year Highest-Impact Paper Award** (awards roster) + dblp ICDM 2008.
  - **Why it is an exemplar:** models **confidence-weighted implicit feedback** (views, clicks)
    rather than explicit ratings — naming the data regime and building the method around it, the
    `icdm-writing-style` "data regime first" discipline.
  - **Self-check:** does your method start from the *kind of data you actually have* and make that
    regime the reason the mechanism is shaped the way it is?

### Scalable graph mining systems (big-data mining)

- **Kang, Tsourakakis & Faloutsos, "PEGASUS: A Peta-Scale Graph Mining System," ICDM 2009.**
  Verified: IEEE ICDM **2018 10-Year Highest-Impact Paper Award** (awards roster) + dblp ICDM 2009.
  - **Why it is an exemplar:** unifies many graph-mining operations under one scalable
    matrix-vector abstraction on a distributed backend — a **scale-as-contribution** paper, the
    lane ICDM rewards when the systems idea is genuinely general.
  - **Self-check:** is the scale claim the contribution (with measured behavior across sizes),
    rather than a footnote to an accuracy result?

### Sparse linear recommendation (top-N ranking)

- **Ning & Karypis, "SLIM: Sparse Linear Methods for Top-N Recommender Systems," ICDM 2011.**
  Verified: IEEE ICDM **2020 10-Year Highest-Impact Paper Award** (awards roster) + dblp ICDM 2011.
  - **Why it is an exemplar:** learns a **sparse item-item aggregation** for top-N recommendation
    — a compact, interpretable mechanism with a clear optimization statement, showing ICDM values
    a well-posed method over architectural bulk.
  - **Self-check:** is your method's objective stated plainly enough that a reviewer can see *why*
    it should generalize, before seeing the tables?

### Time-series averaging for classification (temporal mining)

- **Petitjean, Forestier, Webb, Nicholson, Chen & Keogh, "Dynamic Time Warping Averaging of Time
  Series Allows Faster and More Accurate Classification," ICDM 2014.**
  Verified: IEEE ICDM **2023 10-Year Highest-Impact Paper Award** (awards roster) + dblp ICDM 2014.
  - **Why it is an exemplar:** fixes a **methodological flaw in how time series are averaged** so
    that nearest-centroid classification becomes both faster and more accurate — a discovery-
    validity contribution, exactly the ICDM "is the evaluation itself sound?" instinct.
  - **Self-check:** does your paper repair or validate a *method others use incorrectly*, with a
    controlled demonstration, rather than only adding a new model?

---

## By topic (each cell is a verified ICDM paper above)

| Topic | Verified ICDM exemplar | Edition | Method |
| --- | --- | --- | --- |
| Graph proximity / random walks | Tong, Faloutsos & Pan, "Fast Random Walk with Restart" | ICDM 2006 | RWR made fast + reusable |
| Anomaly detection | Liu, Ting & Zhou, "Isolation Forest" | ICDM 2008 | Isolation-based detection |
| Implicit-feedback recommendation | Hu, Koren & Volinsky, "CF for Implicit Feedback" | ICDM 2008 | Confidence-weighted latent factors |
| Scalable graph systems | Kang, Tsourakakis & Faloutsos, "PEGASUS" | ICDM 2009 | Distributed matrix-vector graph mining |
| Top-N recommendation | Ning & Karypis, "SLIM" | ICDM 2011 | Sparse linear item aggregation |
| Time-series classification | Petitjean et al., "DTW Averaging" | ICDM 2014 | Corrected DTW barycenter averaging |

> Six verified ICDM papers across six topic × method cells, all longevity-tested via the
> 10-Year Highest-Impact / Best-Paper roster. The two ICDM-2008 rows (Isolation Forest and
> implicit-feedback CF) show that a single edition can seed durable lines in **different**
> subfields — useful when positioning against "ICDM only rewards graphs."

---

## Omitted for lack of clean ICDM verification (do not attribute to ICDM without re-checking)

To keep the list zero-hallucination, the following were **excluded** — several are exactly the
sibling-venue confusions the header warns about:

- **Grover & Leskovec, "node2vec"** and **Perozzi et al., "DeepWalk"** — canonical graph-embedding
  papers, but both are **KDD**, not ICDM. Omitted.
- **Tang et al., "LINE: Large-scale Information Network Embedding"** — **WWW 2015**, not ICDM.
  Omitted.
- **Chawla et al., "SMOTE"** — the imbalanced-learning classic is in **JAIR (2002)**, not ICDM.
  Omitted.
- **van der Maaten & Hinton, "t-SNE"** and **Gretton et al., "A Kernel Two-Sample Test"** — both
  **JMLR**, not ICDM. Omitted.
- Various **SDM** (SIAM) data-mining papers surface under the same "data mining conference" query —
  SDM is SIAM-sponsored and is **not** ICDM. Omitted unless the ICDM edition is explicit.

Before adding any new paper, confirm the **ICDM edition** on the awards roster or dblp
(`dblp.org/db/conf/icdm`), record authors, year, and edition, and update the access-date header.
When in doubt, omit. If web verification is unavailable, add the row as **待核实 / TO VERIFY** with
**no attribution**.
