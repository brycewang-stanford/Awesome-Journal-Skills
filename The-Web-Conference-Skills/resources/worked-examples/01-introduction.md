> **Illustrative teaching example.** The paper, system, datasets, and all numbers
> below are **fictional**, constructed solely to demonstrate the Web Conference
> first-page arc. No real-paper facts and no venue policy are invented here.
> Companion skills: [`webconf-writing-style`](../../skills/webconf-writing-style/SKILL.md),
> [`webconf-topic-selection`](../../skills/webconf-topic-selection/SKILL.md),
> [`webconf-experiments`](../../skills/webconf-experiments/SKILL.md).

# Worked Example: A Web Conference Abstract + Introduction (before → after)

Target arc: **web mechanism → gap → typed contribution → scaled evidence →
reusability**, with the two venue-specific tests applied: the *web-native
mechanism* must appear on page one, and every scale adjective must carry a number.

**Fictional paper:** *"Crawl-Aware Ranking: Correcting Freshness Bias in Web-Scale
Retrieval with Recrawl Schedules."* Fictional claim: search rankers trained on
crawled corpora inherit the crawler's revisit policy as a hidden bias, and a
correction using the recrawl schedule improves ranking of fast-changing pages.

---

## Before (how competent teams actually miss this venue)

> **Abstract.** Learning to rank is a fundamental problem in information
> retrieval. Recent transformer-based rankers achieve strong results on standard
> benchmarks. However, real-world corpora are noisy and dynamic. We propose
> CAR-Rank, a novel crawl-aware ranking model with a specialized bias-correction
> module. Extensive experiments on several large-scale datasets demonstrate that
> CAR-Rank significantly outperforms state-of-the-art baselines.
>
> **Introduction.** Search is one of the most important applications on the web.
> With the explosion of online information, ranking quality matters more than
> ever. Deep learning has revolutionized ranking... [two paragraphs of deep
> learning history] ...We evaluate CAR-Rank extensively and show significant
> improvements. Our contributions are: (1) a novel model; (2) a new module;
> (3) extensive experiments.

**Failure diagnosis against this pack:**

- **The web mechanism is missing.** "Noisy and dynamic corpora" is a backdrop
  phrase; nothing yet *requires the Web*. As written, this is a SIGIR-or-anywhere
  paper — the swappability test in `webconf-topic-selection` fails.
- **Unattached adjectives everywhere**: "large-scale," "extensive,"
  "significantly," "state-of-the-art" — zero numbers, zero named baselines,
  exactly the register `webconf-writing-style` bans.
- **Untyped contribution.** "A novel model" is not a contribution type; reviewers
  cannot tell whether to judge it as an algorithm, a measurement, or a system.
- **Generic contribution bullets** ("novel model / new module / extensive
  experiments") that could headline any paper ever submitted.
- **No provenance, no ethics, no reusability** — the crawl data that motivates
  the whole paper is never described.

---

## After (the Web Conference arc, annotated)

> **Abstract.** Web-scale rankers are trained on crawled snapshots, but crawlers
> revisit pages on schedules that favor popular, slowly-changing sites: the
> training corpus systematically under-represents fresh versions of volatile
> pages. We show this **crawl-schedule bias** is a measurable property of the
> corpus, not the ranker: across two public crawl corpora (3.1B and 0.8B pages;
> snapshots dated), volatile-page relevance labels lag their live versions on
> 22-31% of sampled queries. We then propose CAR-Rank, which treats the recrawl
> schedule itself as an observed variable and reweights training pairs by
> staleness probability. On both corpora, CAR-Rank improves NDCG@10 on
> volatile-page queries by 4.1 ± 0.3 and 3.6 ± 0.4 points over five tuned recent
> baselines while remaining within 0.2 points on stable-page queries (5 seeds,
> paired tests). The correction needs only crawler metadata that every archival
> snapshot already ships, and we release code, query sets, and per-file manifests
> under a DOI. *(mechanism → measured gap → typed method → scaled, uncertainty-
> bearing evidence → reusability, in one paragraph)*
>
> **Introduction.**
> *(¶1 — the web mechanism.)* A ranking model never sees the Web; it sees a
> crawl. Crawlers allocate revisits by popularity and observed change rate, so
> the snapshot a ranker trains on is a *policy-weighted sample* of the Web —
> and the policy's fingerprints end up in the ranker. This coupling between
> infrastructure (the crawler) and learning (the ranker) exists only on the open,
> continuously-changing Web; it has no analogue in static-benchmark retrieval.
> *(the sentence that answers "why is this a WWW paper" — quotable by a chair)*
>
> *(¶2 — the gap, each prior line failing for a named reason.)* Freshness-aware
> ranking treats staleness as a *feature* of the page, not a *bias* of the
> corpus, so it recalibrates scores without fixing the training distribution.
> Temporal IR benchmarks refresh labels but inherit whatever revisit policy
> produced the underlying corpus. Debiasing work in recommendation corrects
> exposure bias from *ranking* feedback loops, whereas crawl-schedule bias
> arises *upstream of any ranker*. None of these treats the crawler's schedule
> as data. *(three named lines, three specific failures — no "prior work is
> limited")*
>
> *(¶3 — typed contribution.)* This is an **algorithm-plus-measurement** paper.
> Measurement: a protocol quantifying crawl-schedule bias from snapshot metadata
> alone (Sec. 3), with sampling frame and dead-link accounting stated. Algorithm:
> CAR-Rank's staleness-probability reweighting, derived from the recrawl interval
> distribution (Sec. 4). *(reviewers now know which bar to apply to which half)*
>
> *(¶4 — evidence with scale attached.)* We evaluate on two public, dated crawl
> corpora (3.1B pages, 2025-11 snapshot; 0.8B pages, 2025-06 snapshot), five
> baselines re-tuned under an equal budget with disclosed search spaces, five
> seeds, paired significance tests, and a temporal split matching crawl order —
> random splits leak future recrawls into training (Sec. 5.1). *(the leakage
> sentence preempts the venue's most-caught bug — `webconf-experiments`)*
>
> *(¶5 — reusability and availability.)* The correction consumes only standard
> crawler metadata, so it applies to any snapshot-trained ranker; we release
> code, query sets, and manifests with checksums under a DOI, and state ToS
> posture for both corpora in Sec. 3. *(availability and ethics beside the data,
> not in the appendix)*

---

## What changed, mapped to the skills

| Before-symptom | After-fix | Skill |
| --- | --- | --- |
| Backdrop web ("noisy and dynamic") | Crawler-ranker coupling as page-one mechanism | `webconf-writing-style` |
| Swappable venue | Bias exists only on the live Web | `webconf-topic-selection` |
| "Large-scale, extensive, significant" | 3.1B/0.8B pages, 5 seeds, ±, paired tests | `webconf-experiments` |
| Untyped "novel model" | Algorithm + measurement, judged separately | `webconf-writing-style` |
| No data provenance | Dated snapshots, manifests, ToS posture in body | `webconf-reproducibility` |
| No availability story | DOI-deposited artifact previewed on page one | `webconf-artifact-evaluation` |

> Next: benchmark the rewritten first page against the verified papers in
> [`../exemplars/library.md`](../exemplars/library.md), then re-check every policy
> assumption in [`../official-source-map.md`](../official-source-map.md).
