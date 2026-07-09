---
name: icdm-related-work
description: Use when positioning an ICDM (IEEE International Conference on Data Mining) paper's related work - lineage against prior ICDM editions and IEEE data-mining neighbors, the mechanism-contrast novelty sentence, avoiding KDD/SDM/CIKM/WSDM venue misattribution, and citing your own prior work in the third person so the section stays triple-blind-safe.
---

# ICDM Related Work

Position the paper against the data-mining literature the way an ICDM reviewer reads it:
by **mechanism and mining task**, not by benchmark leaderboard. The section has two ICDM
constraints — it must contrast your *mechanism* with prior mechanisms, and it must do so
without breaking the Research Track's triple-blind anonymity or misattributing sibling-venue
work to ICDM.

## Position by mechanism, not by results table

- For each closely related method, state what mechanism it uses and the specific thing your
  mechanism changes: the isolation criterion, the sparsity structure, the walk kernel, the
  sketch, the update rule. "We also do anomaly detection" is not positioning.
- Group prior work by the mining primitive it shares with you, so the reader sees the lineage
  your contribution extends or breaks.
- End the closest-competitor paragraph with a **one-sentence mechanism-contrast**: "Unlike
  [X], which stores the full graph to compute isolation depth, our sketch estimates it in one
  pass with a stated error." That sentence is the novelty claim reviewers quote.

## Cite the ICDM lineage where it exists

ICDM has durable research lines you can anchor to — random walks with restart, isolation-based
detection, sparse linear recommendation, scalable graph systems, corrected time-series
averaging (see `resources/exemplars/library.md`). Situating your work in an ICDM line signals
venue fit. But cite the paper for its *mechanism*, and verify the edition on dblp before
attributing anything.

## The misattribution trap

Data-mining fame does not mean ICDM placement. Getting a venue wrong in related work is a
credibility hit a data-mining reviewer notices immediately.

| Paper / method | Actual venue | Not |
|---|---|---|
| node2vec, DeepWalk | KDD | ICDM |
| LINE (network embedding) | WWW | ICDM |
| SMOTE | JAIR (journal) | ICDM |
| t-SNE, Kernel Two-Sample Test | JMLR (journal) | ICDM |
| Many "SDM" mining papers | SDM (SIAM) | ICDM |

Check each citation's venue on dblp; ICDM, KDD, CIKM, WSDM, and SDM overlap in topic and are
easy to confuse.

## Keep it triple-blind-safe

- Cite your own prior work in the **third person**: "Building on the sketch of [12]," not
  "building on our sketch of [12]."
- Do not signal a research program only your group could have ("in our line of work on X").
- Do not cite an anonymized-breaking preprint by a title that de-anonymizes you; if a
  concurrent arXiv version exists, follow the current call's policy on declaring it.

## Handle concurrent and recent work

- ICDM's June deadline sits after the spring conference season; recent CIKM, WWW, and KDD
  cycles may contain concurrent work. Acknowledge genuinely concurrent results as concurrent,
  not as prior art you failed to beat.
- Because the whole section lives inside the 10-page all-inclusive cap, prune citations that
  do not sharpen the mechanism contrast; a padded related-work section costs you body space.

## Vignette: a novelty sentence that survived review

An author's first draft said "our method is related to random-walk methods and embedding
methods." The revision named the closest competitor's mechanism (full-graph restart
computation), stated the delta (single-pass estimation with a bound), verified on dblp that
the competitor was an ICDM paper and that a wrongly-cited "ICDM" embedding paper was actually
a KDD paper, and rewrote the self-citation in the third person. The section shrank by a third
and the novelty claim became a single quotable sentence.

## Output format

```text
[Positioning] mechanism-contrast / results-only (fix if results-only)
[Novelty sentence] <one-sentence mechanism delta vs closest work>
[Venue check] all citations verified on dblp: yes / misattributions found
[Anonymity] third-person self-cites: yes / leaks found
[Trim list] <citations to cut to protect the 10-page cap>
```
