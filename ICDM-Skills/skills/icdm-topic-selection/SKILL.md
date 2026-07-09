---
name: icdm-topic-selection
description: Use when deciding whether a project is a strong ICDM (IEEE International Conference on Data Mining) fit, choosing among its Research, Applied, and Blue Sky tracks, and comparing ICDM with KDD, SDM, CIKM, WSDM, WWW, ICDE, or the ML flagships by contribution type, sponsor community, and the data-mining routing calendar seen from ICDM's June deadline.
---

# ICDM Topic Selection

Use this before writing. Two decisions happen here: is the work **ICDM-shaped at all**,
and if so, **which track**. ICDM is the IEEE-sponsored data-mining flagship; it rewards a
named data-mining mechanism on a defined mining task with strong baselines and a
scalability or discovery-validity story — not pure learning theory, and not a broad
deep-learning systems result.

## Fit test

- Prefer ICDM when the contribution is a **data-mining method**: pattern discovery, graph
  mining, anomaly detection, temporal/streaming mining, clustering, or scalable analytics,
  with an algorithmic idea and defensible empirical evidence.
- Route to **SDM (SIAM)** if the contribution is primarily mathematical/statistical rigor
  in a mining method — SDM's community weights theory and analysis more heavily.
- Route to **KDD** if the work is large-scale applied discovery or a deployed data-science
  system aimed at the biggest data-mining audience and its two-cycle calendar.
- Route to **CIKM** for information/knowledge management, IR, and database-adjacent work;
  to **WSDM** for web-and-social search and mining; to **WWW/TheWebConf** for web-native
  contributions; to **ICDE/SIGMOD/VLDB** for database-systems results.
- Route to an **ML flagship** (NeurIPS/ICML/ICLR) if the contribution is a general learning
  method with thin data-mining specificity.

## Track fork within ICDM

| Track | 2026 review | Best for |
|---|---|---|
| Research | Triple-blind | A novel mining algorithm/mechanism with baselines and scale evidence |
| Applied | Single-blind (new in 2026) | A deployed/industrial system with measured real-world impact |
| Blue Sky | CCC-sponsored | A visionary, forward-looking position with a research agenda |

If a project is a deployed system whose contribution is the deployment and its measured
outcomes, the Applied Track fits and spares you the triple-blind anonymization burden. If
the contribution is the algorithm and the deployment is illustrative, stay on Research.

## Fit signal table

| Signal in the project | ICDM reading |
|---|---|
| Named mining mechanism + baselines + scaling curve | Core fit — the house genre |
| Anomaly/graph/pattern/stream mining with a discovery-validity argument | Core fit |
| Deployed system with quantified impact, deployment is the point | Applied Track |
| Pure statistical/theoretical mining analysis | Better served at SDM |
| Broad deep-learning method, little mining specificity | Route to an ML flagship |
| Database-systems or query contribution | Route to ICDE/SIGMOD/VLDB |

## The routing calendar from ICDM's seat

ICDM's deadline sits in **June**, conference in **November**. That position matters when
choosing where a finished project goes next: a paper not ready for ICDM's June can often
target CIKM (spring deadline, autumn conference) the same year, WSDM (late-summer deadline,
following spring), SDM (autumn deadline, following spring), or KDD's next cycle. Choose by
community and format fit, not prestige — the same result reads differently to each pool.

## Vignette: where a streaming anomaly detector goes

A project delivers a one-pass anomaly detector for edge streams with a memory bound and
experiments on injected anomalies. ICDM reading: strong Research Track fit — a named
mining mechanism, a scaling argument, and a discovery-validity claim. Strip the mechanism
and keep only "we deployed it and fraud dropped," and it becomes an Applied Track paper
(or a KDD applied submission). Grow it into a pure asymptotic analysis of the sketch with
no system, and SDM becomes the better community.

## Sharpening moves before committing

- Name the mining task and the data regime in one sentence; if you cannot, the ICDM
  framing does not exist yet.
- Name the single mechanism the contribution rests on, and the baseline it beats *for a
  stated reason*, not just on a leaderboard.
- Confirm the whole argument — body, references, appendix — can fit ICDM's 10-page
  all-inclusive cap; a result needing 14 pages is a journal or SDM paper.
- Topic emphasis and track lineup drift between editions; scan the current calls before
  final routing.

## Output format

```text
[Fit] strong ICDM / possible ICDM / better elsewhere
[Track] Research / Applied / Blue Sky
[Best venue] ICDM / KDD / SDM / CIKM / WSDM / WWW / ICDE / ML-flagship / journal
[Contribution sentence] <one sentence naming task + mechanism>
[Top rejection risk] <novelty / baselines / scale / discovery-validity / fit>
[Next action] <experiment, framing, track switch, or venue switch>
```
