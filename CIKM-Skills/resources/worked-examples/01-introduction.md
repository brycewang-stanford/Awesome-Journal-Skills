> **Illustrative teaching example.** The system, datasets, numbers, and company
> context below are **fictional**, constructed only to demonstrate CIKM-style framing.
> No real-paper content is reproduced and no conference policy is invented. Companion
> skills: [`cikm-writing-style`](../../skills/cikm-writing-style/SKILL.md),
> [`cikm-topic-selection`](../../skills/cikm-topic-selection/SKILL.md),
> [`cikm-experiments`](../../skills/cikm-experiments/SKILL.md).

# Worked Example: A CIKM-Style Abstract + Introduction (before → after)

The exercise: take a first-draft opening written in generic ML-conference register
and rewrite it for CIKM's **tri-lane readership** — the IR reviewer scanning for task
and evaluation, the mining reviewer scanning for mechanism and delta, the KM/database
reviewer scanning for data reality. The target structure is the four-step first page
from `cikm-writing-style`: **information problem → why the boundary is the hard part
→ mechanism, named → evidence preview, calibrated.**

**Fictional paper:** *"Freshness-Aware Entity Linking for Enterprise Search over
Continuously Edited Wikis."* Fictional setting: an internal wiki whose pages are
edited hourly, an entity linker feeding the search index, and rankings that degrade
as links go stale.

---

## Before (single-lane ML register — the draft that underperforms here)

> **Abstract.** Entity linking is an important task in NLP. We propose FreshLink, a
> novel transformer-based framework with a temporal attention module. Extensive
> experiments demonstrate that FreshLink significantly outperforms state-of-the-art
> baselines on several datasets, proving the effectiveness of our approach.
>
> **Introduction.** Recently, large language models have revolutionized many tasks.
> Entity linking has been widely studied. However, existing methods ignore temporal
> dynamics. To fill this gap, we design a new architecture with three components...
> Our contributions are: (1) a novel framework; (2) a new attention mechanism;
> (3) extensive experiments showing superior performance.

**Why this fails the tri-lane scan** (per `cikm-writing-style` /
`cikm-experiments`):

- **No information problem.** "Entity linking is important" names a task, not a
  problem; the KM reviewer never learns what data reality (hourly edits, stale
  links) breaks existing practice.
- **The boundary sentence is missing.** "Existing methods ignore temporal dynamics"
  gestures at a gap without saying *why the seam is hard* — what specifically fails
  when a linker meets a continuously edited knowledge source.
- **Unpinned vocabulary.** "Novel framework," "significantly outperforms,"
  "state-of-the-art," "several datasets" — every phrase the venue's rewrite table
  flags. *Significantly* appears with no test; the datasets are unnamed.
- **Contribution list without a mechanism name.** The mining reviewer cannot repeat
  what the method does in one clause; "three components" is architecture inventory,
  not an idea.
- **No evidence preview.** Nothing about collections, baselines, effect size, or
  the deployment reality the enterprise setting implies. There is also no hint the
  authors know this is a *retrieval* problem — the linker exists to serve a ranker.

---

## After (CIKM register — problem → boundary → mechanism → calibrated evidence)

> **Abstract.** In enterprise search over continuously edited wikis, entity links
> decay: pages are renamed, merged, and split hourly, and a linker trained on a
> frozen snapshot silently routes queries to stale entities. On our fictional
> six-month wiki trace, 18% of query-relevant entities change identity within a
> week of indexing. We present **FreshLink**, which treats linking decisions as
> *revisable*: each link carries an edit-sensitivity score derived from the wiki's
> revision graph, and the search index re-resolves only the links whose sensitivity
> exceeds a budgeted threshold — reconciliation at a controllable cost. On two
> public entity-linking benchmarks FreshLink matches static linkers (within 0.4 F1);
> on the evolving-wiki trace it improves search nDCG@10 by 3.1 points (paired
> t-test, p < 0.01, 5 runs) over re-linking-everything at one-twelfth the
> recompute. We release the trace generator and evaluation suite; the wiki itself
> cannot be released, and we report the public-analog results alongside.
>
> **Introduction.** *(¶1 — the information problem, in domain terms.)* Organizations
> search their own wikis through indexes enriched by entity linking. Unlike the
> encyclopedic corpora linking research grew up on, an enterprise wiki never sits
> still: pages merge, split, and rename continuously, so the knowledge the index
> relies on decays between reindexing runs.
>
> *(¶2 — why the boundary is the hard part.)* The difficulty is a seam between two
> communities' assumptions. Linking research treats the target knowledge base as
> fixed at inference time; index-maintenance research treats documents as changing
> but their semantics as stable. When the *knowledge base is the thing changing*,
> neither toolset applies: re-linking the corpus on every edit is computationally
> absurd, and ignoring edits mis-routes queries to entities that no longer exist.
>
> *(¶3 — mechanism, named.)* FreshLink makes staleness measurable and reconciliation
> budgeted: an edit-sensitivity score per link, computed from the revision graph,
> and a re-resolution policy that spends a fixed recompute budget where sensitivity
> is highest.
>
> *(¶4 — evidence preview, calibrated, with the data position stated.)* We evaluate
> three ways: linking quality on two public benchmarks (parity check against static
> linkers); end-to-end search quality on a six-month enterprise trace (the headline
> gain, with significance over five runs); and a sensitivity ablation that degrades
> the revision signal to confirm the mechanism carries the gain. The trace cannot be
> released; we ship a trace generator that reproduces its statistics and report all
> results on the public analog as well.

---

## What changed, mapped to the skills

- **The KM lane got a data reality** (hourly edits, rename/merge/split, decay
  statistics) — `cikm-writing-style`'s first scan anchor.
- **The boundary sentence now exists** (¶2: both communities' assumptions fail at
  the seam) — the sentence `cikm-topic-selection` uses to distinguish a two-lane
  CIKM paper from a single-lane specialist paper.
- **The mechanism has a name and one clause** (budgeted re-resolution driven by
  edit sensitivity) — repeatable in a review.
- **Every claim acquired its evidence pattern** — parity claim → public benchmarks;
  headline claim → named metric, test, and run count; mechanism claim → the
  degradation ablation — the claim-lane-evidence contract from `cikm-experiments`.
- **The unreleasable-data position is declared** with a public analog and generator,
  the honesty pattern from `cikm-reproducibility`.
- **Reserved words earned their place**: *significantly* now has a test attached;
  *state-of-the-art* disappeared in favor of named baseline families.

> Next: study the real, dblp-verified boundary papers in
> [`../exemplars/library.md`](../exemplars/library.md) — TAGME and RippleNet are the
> closest structural relatives of this fictional opening — and check current cycle
> rules in [`../official-source-map.md`](../official-source-map.md).
