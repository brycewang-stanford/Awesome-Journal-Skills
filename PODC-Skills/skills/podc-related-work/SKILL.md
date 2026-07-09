---
name: podc-related-work
description: Use when writing the related-work and positioning of an ACM PODC paper — covering the distributed-computing literature lanes (PODC/DISC/SPAA and the JACM / Distributed Computing journals), writing a model-and-bound-precise delta over prior results, distinguishing your model from neighboring ones, and keeping self-citation safe under lightweight double-blind review.
---

# PODC Related Work

Position against results, not topics. In distributed-computing theory a "related" paper is one that
proves a **bound in a comparable model**, and your delta must be stated in the currency the field
uses: **model + problem + cost measure + bound**. A related-work section that lists topics ("several
works study consensus") without the bounds and models tells a PODC reviewer nothing.

## The literature lanes

- **PODC and DISC** — the two distributed-theory flagships; most of your closest prior bounds live
  here. They share the Dijkstra Prize and Dissertation Award and much of a reviewer pool, so their
  results are the ones your reviewers know best.
- **SPAA** — parallel algorithms/architectures; relevant for shared-memory and concurrency results,
  less so for message-passing/fault-tolerance.
- **STOC / FOCS / SODA** — where a distributed result's *sequential* core or a key combinatorial
  lemma may have appeared; cite when your technique descends from sequential theory.
- **Journals — JACM and *Distributed Computing*** — the archival, definitive versions of many
  results (FLP, partial synchrony, linearizability). Cite the **journal version** for the canonical
  statement, and the conference version if you specifically mean that edition.
- **Focused venues — OPODIS, SIROCCO, SSS, ICDCN** — for niche models (mobile agents, networks,
  self-stabilization).
- **Systems venues / arXiv** — for applied or very recent work; cite carefully and note when a
  result is empirical rather than proved.

## Write the delta in the field's currency

For each closest prior result, state the comparison precisely:

```text
[Prior]  <authors, venue/year>: <problem> in <model>, <bound> (e.g., O(n^2) messages, t < n/2, synchronous)
[Ours]   same problem in <model>: <bound> (e.g., O(n log n) messages, t < n/3, partial synchrony)
[Delta]  what improved and at what cost: better message complexity but weaker resilience / stronger
         adversary / different timing model — state the trade honestly
```

The discipline is to make **model differences explicit**. "We improve on [X]" is misleading if [X]
was synchronous and you are asynchronous, or if [X] tolerated more faults. A PODC reviewer will
notice an apples-to-oranges comparison immediately, and it reads as either sloppiness or spin.

## Distinguish your model from neighbors

Much apparent overlap dissolves once models are pinned down. Make sure the reader cannot confuse
your setting with an adjacent one:

- **Synchrony:** a bound under synchrony does not contradict a lower bound under asynchrony.
- **Fault model:** crash-tolerant and Byzantine-tolerant results are not comparable head-to-head.
- **Adversary:** adaptive vs. oblivious changes what is achievable; say which you assume.
- **Cost measure:** a round-optimal protocol may be message-suboptimal; name the measure you optimize
  and acknowledge the others.

## Positioning your contribution

- **Delta-first:** open the related-work discussion (or the introduction's positioning paragraph)
  with what is *new* relative to the nearest result, not with a history of the problem.
- **Concede honestly:** if a prior protocol beats you on one measure while you beat it on another,
  say so. A trade-off stated plainly is a stronger paper than an overclaimed strict improvement.
- **Locate the lower bound:** if your algorithm is optimal, cite (or prove) the matching lower bound
  and say which prior lower bound your result meets or circumvents (by changing the model).

## Self-citation under lightweight double-blind

PODC 2026 is lightweight double-blind, so self-citations must not de-anonymize you:

- Refer to your own prior work in the **third person**: "Prior work [12] shows..." never "In our
  earlier paper [12] we show...".
- Do not write "as we proved in [12]" or "extending our framework [7]".
- Keep the citation itself in the bibliography (do not remove it — that distorts the record); just
  neutralize the *phrasing* that reveals authorship.
- Watch for indirect leaks: "building on the model of [our group's] system X" or an acknowledgement
  of a grant tied to you.

## Common failures

- **Topic lists instead of bound comparisons** — no models, no complexities, no delta.
- **Apples-to-oranges "improvements"** — comparing across incompatible synchrony/fault/adversary
  assumptions without flagging it.
- **Missing the closest result** — a reviewer who works in your subarea knows the one paper you did
  not cite; that omission reads as either ignorance or evasion.
- **Journal-vs-conference confusion** — citing a PODC edition for a result whose canonical statement
  is a JACM article (or vice versa); see the exemplars library's omissions list.
- **Self-citation leak** — first-person references to your own prior work under double-blind.

## Output format

```text
[Lanes covered] PODC/DISC/SPAA/STOC-FOCS-SODA/journals/focused venues — each relevant one present?
[Delta table] for each closest prior result: model, bound, ours, honest trade-off
[Model distinctions] synchrony/faults/adversary/cost-measure differences made explicit?
[Optimality] matching lower bound located/cited/proved?
[Double-blind] self-citations third-person; no grant/group leaks?
[Fix queue] <missing closest results; over/under-claimed deltas; leaks to fix>
```
