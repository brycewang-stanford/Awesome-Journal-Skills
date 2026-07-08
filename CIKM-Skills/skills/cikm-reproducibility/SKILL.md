---
name: cikm-reproducibility
description: Use when hardening the reproducibility of a CIKM paper — pinning the pipeline stages where IR, mining, and knowledge-management results silently diverge, documenting KGs and enterprise data that cannot be released, keeping the GenAI disclosure consistent with how code and data were produced, and preparing the post-acceptance release.
---

# CIKM Reproducibility

Reproducibility at CIKM has a venue-specific difficulty: the typical paper chains
components from different communities — an index, a graph, a model, a ruleset — and
each link has its own silent-divergence habits. A reader who cannot rebuild the
chain cannot attribute the result, and a blended review panel contains someone able
to notice each weak link.

## Divergence map for chained pipelines

| Chain link | How results silently drift | Pin |
|---|---|---|
| Text preprocessing / indexing | Tokenizer versions, stopword lists, index-time defaults differ across toolkits | Name toolkit + version + config file in the artifact |
| KG snapshot | Public KGs (Wikidata-class) change daily; entity counts drift | Freeze and state the dump date; ship the extracted subgraph if licensable |
| Candidate generation | Recall stage caps and thresholds rarely reported | Report every cutoff; they bound the final metrics |
| Training | Seeds, hardware nondeterminism, early-stopping criteria | Seed policy + selection rule in the protocol paragraph |
| Evaluation | Metric implementations disagree at tie-breaking and cutoffs | Name the evaluation library version; never hand-roll silently |
| LLM components | Model version/API drift; prompts unlogged | Pin model identifiers and dates; log prompts verbatim in the artifact |

The discipline: for each link, either the artifact pins it or the paper states it.
A link pinned nowhere is where a failed replication will land.

## Unreleasable data, releasable knowledge

CIKM's KM lane routinely involves enterprise corpora, clickstreams, or proprietary
KGs that cannot ship. The venue-honest pattern:

- Describe the unreleasable data statistically (size, schema, class balance,
  collection window) at a level where a reader could construct a synthetic
  analog — then actually provide that analog generator when feasible.
- Run the public-data variant of every headline experiment, even if the effect is
  smaller; a result that exists *only* on invisible data asks the panel for faith.
- State the release position explicitly in the paper ("logs cannot be released;
  the sampling script and schema are in the artifact") rather than leaving the
  reader to discover the gap.

## GenAI disclosure as a reproducibility document

CIKM 2026's mandatory GenAI Usage Disclosure covers code and data, not just prose
(source map, 2026-07-08). Treat it as part of the methods record: if evaluation
scripts, synthetic data, prompts, or labels were generated with AI assistance, the
disclosure plus the artifact should together let a reader judge what that implies
for the result. A disclosure that says "AI used for coding" while the artifact
contains unexplained generated labels is an inconsistency automated compliance
checks — which the conference reserves — or reviewers can catch.

## Environment capture

Chained pipelines multiply environment surface, so capture it in layers:

| Layer | Capture mechanism |
|---|---|
| OS + system libraries | Container image or a documented base image tag |
| Language environments | Lockfiles (exact versions), not loose requirement ranges |
| Toolkit configs | The actual config files, committed — not "default settings" prose |
| Data inputs | Checksums + download scripts, or the frozen extraction (see KG row) |
| Hardware assumptions | GPU/CPU class and memory floor stated where results are timed |

The test is transferability: a lab-mate on a clean machine, without the authors in
the room, reaches the headline table. Running that internal replication before
submission is the single highest-yield reproducibility exercise — it finds the
unpinned link while it can still be pinned.

## Where reproducibility pays at this venue

Three concrete CIKM payoffs beyond principle. First, the blended panel: whichever
lane doubts the result will probe its own link of the chain, so pinning every link
is defense in all three directions. Second, resource-track reviewers and readers
judge *adoptability*, which is reproducibility wearing its public face
(`cikm-artifact-evaluation`). Third, follow-up work: CIKM's back catalog shows
methods becoming standard baselines (DRMM, BERT4Rec); papers get that afterlife
only when third parties can run them — the reproducible version of a method is the
one that accumulates citations as a baseline.

## Release timeline

Anonymized review artifact during submission (see `cikm-supplementary` for what the
budget permits); public repository at camera-ready, with license, versioned release
tag, and the exact commit that produced the proceedings numbers. The 2026
notification-to-camera-ready window is thirteen days — build the release *during*
the review wait (`cikm-workflow` Mode A), not inside that window.

## Honest-failure disclosure

Chained pipelines rarely reproduce perfectly, and the venue-credible move is to
say so first: a REPRODUCING.md that states which numbers regenerate exactly, which
vary within a stated tolerance (GPU nondeterminism, sampling), and which depend on
restricted inputs and therefore only regenerate in public-analog form. Declared
tolerance reads as competence; discovered variance reads as concealment. The same
document is where to state known environment sensitivities ("results verified on
CUDA X; version Y shifts Table 3 by ±0.2") — the sentence that saves a replicator
a week is the sentence that earns the citation.

## One-command bar

```bash
# The replication target for a CIKM chained pipeline:
git clone <repo> && cd <repo>
make setup          # pinned environment, data download or synthetic analog
make table2         # rebuilds the headline table end-to-end from the frozen inputs
```

If `make table2` cannot exist because data is restricted, the repo must say so at
the top and offer the public-variant target instead. Silent partiality — a repo that
looks complete but is not runnable — costs more reviewer goodwill than an honest
scope statement.

## Output format

```text
[Chain audit] <link → pinned where (paper / artifact / nowhere)>
[Data position] <releasable / described+analog / public-variant-only>
[Disclosure consistency] <GenAI section vs. artifact contents>
[Release plan] <review artifact state → camera-ready repo state, dated>
[Weakest link] <the divergence a replicator would hit first>
```
