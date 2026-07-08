---
name: sigir-topic-selection
description: Use when deciding whether a project belongs at SIGIR and in which of its tracks — testing whether retrieval is the contribution or the plumbing, forking across full/short/resources/reproducibility/perspectives/industry, and routing misfits to ECIR, CIKM, WSDM, CHIIR, ICTIR, RecSys, TheWebConf, or NLP/ML venues.
---

# SIGIR Topic Selection

Two decisions, in order: (1) is this an information-retrieval contribution at all,
and (2) which SIGIR track owns it. Both are cheaper to get right in October than to
learn from reviews in March. SIGIR 2026's verified lineup — Full, Short,
Perspectives, Resources, Reproducibility, Low Resource Environments, and Industry
tracks — makes the second decision genuinely multi-way.

## Test 1: is retrieval the contribution or the plumbing?

The LLM era floods SIGIR with papers where retrieval is present but incidental.
The discriminating question: **if you swapped the retrieval component for an oracle
(or a black box), would the contribution survive?**

- Survives → the contribution is the downstream system (agent, QA, generation
  quality); route to an NLP/ML venue and cite IR work properly.
- Dies → the contribution is retrieval: ranking quality, efficiency, evaluation
  validity, user search behavior, or the retrieval-specific part of RAG (candidate
  quality, index design, retrieval evaluation). SIGIR-shaped.

Corollary signals of SIGIR fit: the natural headline table has metric@cutoff
columns on named collections; the natural reviewers are IR-evaluation people; the
natural related work includes SIGIR/TOIS/TREC lineage (see `sigir-related-work`).

## Test 2: the track fork

| Your strongest honest sentence starts with... | Track | 2026 anchor |
|---|---|---|
| "We propose/analyze a method and show on N collections..." | Full papers | ≤9 pp excl. refs, double-blind |
| "We report one focused finding..." | Short papers | ≤4 pp excl. refs, own OpenReview group |
| "We built and share a corpus/toolkit/judgments..." | Resources | ≤6 pp + refs, **single-anonymous** |
| "We reproduced (or failed to reproduce) published results..." | Reproducibility | Own track in 2026; details 待核实 |
| "We argue the field should..." | Perspectives | Details 待核实 |
| "We deployed retrieval in production and learned..." | Industry (SIRIP lineage) | Details 待核实 |
| "Search under compute/connectivity/language constraints..." | Low Resource Environments | Feb 5 abstract, Apr 2 notify (2026) |

Fork rules of thumb:

- A full paper needs a *rounded* evidence program; a strong single finding with one
  collection and one deep analysis is a better short paper than a thin full paper.
- The dataset built for your method paper is a **separate routing decision** — the
  cross-track double-submission ban means the dataset goes to Resources only if it
  is not the method paper's claimed contribution.
- Reproducibility is for studies *about* prior results, not for "our paper has good
  reproducibility" (that's `sigir-reproducibility` hygiene).

## Neighbor routing when SIGIR isn't the answer

```text
Contribution center of gravity          -> Better first target
---------------------------------------------------------------
Interactive/user-study search behavior  -> CHIIR (then SIGIR full)
Formal/theoretical IR models            -> ICTIR (SIGIR-affiliated)
Recommender systems end-to-end          -> RecSys (SIGIR takes rec too,
                                           esp. retrieval-flavored: NGCF/LightGCN lineage)
Web platform/graph/user data emphasis   -> TheWebConf (WWW) or WSDM
IR + knowledge management/databases     -> CIKM
European timing or repro emphasis       -> ECIR
Language-technology contribution        -> ACL/EMNLP (retrieval as application)
Efficiency/systems below the ranking    -> systems venues; keep an IR-eval slice for SIGIR
Evaluation campaign participation       -> TREC/NTCIR/CLEF tracks (not archival
                                           substitutes: they *feed* SIGIR papers)
```

TREC deserves the explicit note: it is an evaluation campaign, not a proceedings
competitor. Building on (or contributing to) a TREC track is often the strongest
possible SIGIR pipeline — campaign participation year 1, analysis paper year 2.

## Borderline cases, adjudicated

- **RAG for a downstream task, with a retrieval ablation**: if the ablation is the
  deepest result, extract it into a retrieval-evaluation paper for SIGIR and let the
  system paper go to NLP — two focused papers beat one blurry one.
- **An LLM that rewrites queries**: SIGIR-shaped *if* evaluated as a retrieval
  intervention (per-topic deltas on standard collections), NLP-shaped if evaluated
  on rewrite quality.
- **A new efficiency trick inside an index structure**: SIGIR wants the
  quality-cost frontier; a pure throughput result without ranking-quality context
  fits systems venues better.
- **A user study of searchers**: CHIIR first unless there is a measurable
  system-side consequence (a re-ranker, an interface signal) evaluated IR-style.
- **An evaluation critique with no fix**: Perspectives material, or pair it with a
  demonstrated protocol improvement and aim for full papers.

## Timing and prestige honesty

- SIGIR's single annual cycle (January-pattern deadline) means a misrouted
  submission costs a year unless the fallback ring is pre-planned
  (`sigir-workflow`). Route by contribution type, not venue rank.
- Short papers at SIGIR are archival, cited, and respected — routing a focused
  finding there is a strategy, not a demotion.
- If the honest evidence today is one collection, no significance testing, and an
  unfinished ablation, the choice is not "which track" but "which *cycle*" — a
  rushed January submission burns the year anyway.

One more timing lever: the staggered secondary-track calendar (Resources and LRE
ran weeks behind full papers in 2026) sometimes lets a January full-paper miss
become a same-year February resource or reproducibility submission — but only if
the contribution genuinely re-frames, not as a costume change reviewers see through.

## Scope vocabulary check

SIGIR's own topic language (2026 full-papers page): search and ranking, queries and
query analysis, web search, retrieval models and ranking, efficiency and
scalability (indexing, crawling, compression), recommender systems — plus the
community's standing breadth: evaluation, conversational search, and
retrieval-augmented systems. If the abstract cannot be written naturally in this
vocabulary, revisit Test 1.

## Output format

```text
[IR-contribution test] survives-oracle-swap: yes (route out) / no (SIGIR-shaped)
[Track] full / short / resources / reproducibility / perspectives / industry / LRE
[Fork rationale] <one sentence: why this track owns the strongest honest claim>
[Cross-track conflicts] dataset/method ownership resolved y/n
[Fallback ring] <next venue if rejected, with deadline>
[Cycle honesty] submit this cycle / build one more quarter
```
