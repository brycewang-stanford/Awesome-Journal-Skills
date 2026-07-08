> **Illustrative teaching example.** The paper, method, numbers, and results below are
> **fictional**, invented solely to demonstrate SIGIR house style. No real-paper facts are
> stated and no venue policy is invented. Companion skills:
> [`sigir-writing-style`](../../skills/sigir-writing-style/SKILL.md),
> [`sigir-experiments`](../../skills/sigir-experiments/SKILL.md), and
> [`sigir-topic-selection`](../../skills/sigir-topic-selection/SKILL.md).

# Worked Example: A SIGIR-Style Abstract + Introduction (before → after)

The target is the SIGIR first-page arc from `sigir-writing-style`:
**task + regime → the specific failure of current practice → the move → calibrated
evidence (collections, metrics, significance) → checkable contribution bullets** — with
the venue's reserved-word discipline ("significant" only with a test) and its
two-dimensional claim culture (quality claims travel with cost tables).

**Fictional paper:** *"Selective Late Interaction: Storage-Bounded Multi-Vector
Retrieval with Per-Document Token Budgets."* Fictional method (SELINT): a
late-interaction retriever that learns how many token vectors each document deserves,
under a global storage budget.

---

## Before (ML-venue register — the draft that reads as a tourist)

> **Abstract.** Recent advances in large language models have revolutionized information
> retrieval. However, existing approaches suffer from efficiency limitations. In this
> paper, we propose SELINT, a novel framework that leverages adaptive token selection to
> significantly improve retrieval performance. Extensive experiments on diverse
> benchmarks demonstrate that SELINT consistently outperforms strong baselines while
> being much more efficient, achieving state-of-the-art results.
>
> **Introduction.** Information retrieval is an important problem with many applications.
> Recently, dense retrieval and late interaction methods have shown remarkable success.
> Despite this progress, these methods face challenges in real-world deployment. To
> address these challenges, we propose a novel adaptive framework... Section 2 reviews
> related work. Section 3 introduces our method...

**Why this fails the SIGIR read** (per `sigir-writing-style` / `sigir-experiments`):

- **No task or regime named**: first-stage or re-ranking? What corpus scale? What
  latency/storage constraint? The reviewer cannot even pick the right mental baselines.
- **"Significantly" with no test**, "state-of-the-art" with no collection named —
  two reserved-word violations in one abstract.
- **The failure of prior work is a mood** ("suffer from efficiency limitations"), not a
  mechanism: *which* cost, growing with *what*?
- **"Diverse benchmarks" hides the lineup**: SIGIR abstracts name collections.
- **Efficiency claimed, no cost dimension quantified** — the claim is two-dimensional,
  the evidence preview is zero-dimensional.
- **LLM-hype opener** signals adjacent-community framing (`sigir-topic-selection`
  Test 1 unanswered: is retrieval the contribution here?).

---

## After (SIGIR register — task, mechanism, calibrated evidence)

> **Abstract.** Late-interaction retrievers store one vector per document token, so index
> size grows with collection verbosity rather than collection relevance: on long-document
> corpora, storage — not quality — is the binding deployment constraint. Fixed-rate token
> pruning shrinks the index but spends the same budget on every document regardless of
> how much of it is retrievable content. We present **SELINT**, which learns a
> **per-document token budget** under a global storage constraint, allocating vectors
> where relevance signals concentrate. On MS MARCO (passage) and two long-document
> collections, SELINT matches full late interaction within 0.3 nDCG@10 at **8× smaller
> indexes**, and improves over fixed-rate pruning at equal storage by 1.9-2.7 nDCG@10
> (paired t-test on per-topic scores, Holm-corrected, p < 0.05; 3 seeds, mean ± sd).
> Query latency is unchanged at matched candidate depth (Table 5). Code, configs, and
> all run files: <repo>.
>
> **Introduction.** *(¶1 — task + regime.)* We study first-stage retrieval with
> late-interaction models under an index-storage budget — the regime where multi-vector
> quality is wanted but per-token storage is not affordable...
>
> *(¶2 — the failure, as mechanism.)* Fixed-rate pruning keeps the top-k vectors of
> every document. But retrievable content is unevenly distributed: boilerplate-heavy
> documents waste their budget while information-dense documents are truncated. We
> quantify this mismatch on <collection>: under a 12.5% global rate, X% of pruned-away
> vectors carry the document's strongest query-match potential...
>
> *(¶3 — the move.)* SELINT treats the budget as an allocation problem...
>
> *(¶4 — evidence, each claim paired.)* Equal-storage comparisons against tuned
> fixed-rate and salience-scored pruning (same first-stage candidates, same training
> data, tuning protocol in §4.2); ablations isolating the allocator (§5.4); per-query
> win/loss analysis by document length (§5.5). All tables report 3-seed mean ± sd with
> paired tests, Holm-corrected.
>
> *(¶5 — contributions, checkable.)* (1) a storage-allocation formulation of token
> pruning; (2) a budget-aware training objective; (3) equal-storage evaluation across
> three collections with significance testing; (4) released run files and index
> configurations for every table.

---

## What changed, mapped to the skills

| Draft problem | Fix applied | Skill rule |
| --- | --- | --- |
| No regime | "first-stage, storage-bounded" in sentence one | First-page arc slot 1 |
| Mood-failure | "spends the same budget on every document" | Failure-as-mechanism |
| Naked "significantly" | Test + correction + seeds in the abstract | Reserved-word discipline |
| Hidden lineup | Collections named, deltas ranged | Calibrated evidence preview |
| One-dimensional claim | Storage table + latency sentence beside quality | Two-dimensional claim culture |
| Vague bullets | Bullets promise artifacts and analyses | Checkable contributions |

Note also what the rewrite does **not** do: it does not claim generality beyond the
three collections, does not call the method "novel" (the mechanism sentence does that
work), and does not promise an appendix — at SIGIR the appendix shares the 9-page
budget, so overflow analyses are promised to the repository instead
(`sigir-supplementary`).

> Next: study real first pages via [`../exemplars/library.md`](../exemplars/library.md)
> (DOI-verified SIGIR papers whose openings execute this arc — ColBERT for the
> two-dimensional claim, NGCF/LightGCN for the mechanism-first recommendation register),
> then verify current formatting rules through
> [`../official-source-map.md`](../official-source-map.md).
