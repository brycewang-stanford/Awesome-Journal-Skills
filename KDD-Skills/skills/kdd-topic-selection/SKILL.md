---
name: kdd-topic-selection
description: Use when deciding whether a project belongs at KDD and in which track — Research vs Applied Data Science vs Datasets and Benchmarks vs AI for Sciences — or whether it routes to ICDM, SDM, WSDM, CIKM, WWW, VLDB, or an ML flagship. Covers the deployment-evidence fork, data-regime framing, and SIGKDD fit signals before writing.
---

# KDD Topic Selection

Use this before any writing. KDD routing is a **two-stage decision** — first whether
the work is KDD-shaped at all, then which track — and the second stage is the one
teams get wrong, because the Research and ADS tracks want different papers written
about the same system. A submission may enter exactly one of them per cycle.

## Stage 1: is it KDD-shaped?

KDD rewards contributions where **the data regime is the protagonist**: scale, drift,
heterogeneity, noise, sparsity, graph structure, streams, or the friction of real
deployment. Signals:

- The method's value claim references a property of data (works at 10^9 edges, under
  drift, with 0.1% labels) rather than only a property of models.
- There is a mining/discovery/prediction task with measurable output — not purely a
  learning-theory statement or a pure systems benchmark.
- Someone outside the authors' subfield could use the result on their data.

Anti-signals: novelty lives entirely in architecture or loss design (ML flagships);
the contribution is query processing or storage (VLDB/SIGMOD); the core is retrieval
ranking on web corpora (SIGIR/WSDM/WWW may fit better, though overlap is real).

## Stage 2: the track fork

The decisive question: **what is the strongest evidence you can honestly produce?**

| Your strongest honest evidence | Track | The bar you must clear |
|---|---|---|
| New mechanism + ablations + scale curves on (mostly) public data | Research | Delta over the mining lineage, mechanism isolated |
| A system running in production with measurable post-launch outcomes | ADS | **Quantified post-launch performance — its absence is a desk reject (2026 CFP)**; lessons learned expected |
| A dataset/benchmark others will build on, with licenses and baselines | Datasets & Benchmarks | Documentation, provenance, maintenance story |
| Mining/ML advancing a natural-science question | AI for Sciences | Scientific validity alongside method quality |
| A provocative direction without full evidence | Blue Sky Ideas | Argument quality; check the track's own CFP |

Two frequent mis-forks:

- **Deployed system submitted to Research** because the team fears the ADS bar: it
  then competes on mechanism novelty it may not have, while its actual strength
  (deployment evidence) earns no credit.
- **Research prototype submitted to ADS** with projected or offline-only numbers:
  desk-rejected under the post-launch quantification rule. "We could deploy it" is a
  Research-track sentence.
- The blocked-from-deployment exception in the ADS CFP is for documented external
  blockers (regulation, partner constraints), not for "we ran out of time."

## Decision vignette

A team built a fraud-detection model, ran it in shadow mode for two months, and has a
new graph-sampling trick inside it. Three honest papers hide here: (a) the sampling
trick with ablations and public-graph scale curves → **Research**; (b) after full
launch and a measured A/B window → **ADS**; (c) the labeled transaction graph, if
releasable → **Datasets & Benchmarks**. The wrong move is one paper claiming all
three, thinly. Pick the paper whose evidence exists **this cycle** — the dual-cycle
calendar (`kdd-workflow`) makes "ADS next cycle, after the measurement window" a
concrete plan rather than a consolation.

## Neighbor-venue routing

```text
Route AWAY from KDD when:
- contribution = new learning objective/architecture, data regime incidental
    -> NeurIPS / ICML / ICLR
- contribution = mining method, but community/deadline fit favors a sibling
    -> ICDM or SDM (same shape, different scale of venue)
- contribution = web/user-behavior/retrieval centric
    -> WWW / WSDM / SIGIR / RecSys
- contribution = data management, indexing, query execution
    -> VLDB / SIGMOD
- contribution = domain science outcome, method standard
    -> domain journal, or KDD's AI-for-Sciences track if the mining is real
```

If the paper misses at KDD, the reviews tell you which axis failed
(`kdd-review-process`); a mechanism-novelty objection with solid deployment evidence
often means the right venue was the ADS track all along — a track switch, not a
venue switch.

## Fit-signal reference

| Signal in the project | KDD reading |
|---|---|
| Method's win grows with data size or graph density | Core Research fit — scale is the venue's home turf |
| Production system + measurable online outcomes | ADS fit, and only ADS once post-launch numbers exist |
| Contribution is a labeled corpus or benchmark harness | Datasets & Benchmarks, not a Research paper padded with baselines |
| Novel loss/architecture, benchmarks incidental | ML flagship shape; expect "delta over lineage?" pushback at KDD |
| Discovery claim in a natural-science domain | AI for Sciences, or a domain venue if the mining is off-the-shelf |
| Query/index/storage performance is the headline | VLDB/SIGMOD shape |
| The paper's tables would not change if the data were 100x smaller | The scale story is decorative — fix that before routing anywhere |

## Timing interacts with routing

Because KDD runs two cycles, track choice is also schedule choice: a Research paper
can target the nearest cycle, while the ADS version of the same project may need to
wait for its measurement window to close (`kdd-workflow`). When co-authors disagree
on track, the tiebreaker question is: *which paper's gate evidence exists today?*
Projected evidence loses to existing evidence at this venue every time — the ADS
desk-check makes that literal.

## Commit checklist before writing

1. One sentence naming the data regime and why it defeats existing methods.
2. Track chosen from the evidence table above, and the track's specific bar quoted
   from the current CFP (track CFPs are separate documents — read the right one).
3. The nearest KDD-lineage ancestor identified (`kdd-related-work`).
4. The cycle chosen with evidence lead times honored (`kdd-workflow`).

## Output format

```text
[KDD-shaped] yes / no -> <redirect venue>
[Track] Research / ADS / Datasets+Benchmarks / AI4Science / BlueSky
[Evidence basis] <the strongest honest evidence available this cycle>
[Desk-check exposure] ADS post-launch quantification: satisfied / fails / N-A
[Regime sentence] <one sentence>
[Next action] <write / measure / wait a cycle / re-route>
```
