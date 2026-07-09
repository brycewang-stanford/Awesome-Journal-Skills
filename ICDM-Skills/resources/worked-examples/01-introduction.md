> **Illustrative teaching example.** The paper, method, dataset, and every number below are
> **fictional** and exist only to demonstrate ICDM house style. No real-paper facts, datasets, or
> results are stated, and no policy is invented. Corresponding skills:
> [`icdm-writing-style`](../../skills/icdm-writing-style/SKILL.md),
> [`icdm-topic-selection`](../../skills/icdm-topic-selection/SKILL.md), and
> [`icdm-experiments`](../../skills/icdm-experiments/SKILL.md).

# Worked Example: An ICDM-Style Abstract + Introduction (before → after)

This demonstrates the **ICDM first-page arc** from `icdm-writing-style`:
**data regime → mining task → named mechanism → baseline + scale evidence → why the discovery is
valid** — under ICDM's constraints that everything (including references and appendix) lives inside
**10 IEEE two-column pages** and that the Research Track is **triple-blind**, so the first page must
carry the contribution without any identifying "our earlier system" framing.

The framing also reflects `icdm-topic-selection`: ICDM is strongest when the contribution is a
**data-mining mechanism with defensible discovery claims and a scaling story**, not a pure
learning-theory result (route to SDM) or a broad deep-learning systems win (route to KDD's applied
lane or an ML flagship).

**Illustrative paper (fictional):** *"Isolation Sketches: Sub-Linear Anomaly Detection on Streaming
Interaction Graphs."* Fictional method: a sketch that maintains isolation-style anomaly scores over
an evolving edge stream in one pass.

---

## Before (buries the contribution — typical first-draft abstract + intro)

> **Abstract.** Anomaly detection is an important problem with many applications. Deep learning has
> recently achieved great success. In this paper we propose a novel neural approach for detecting
> anomalies in graphs, which combines an autoencoder with attention, and show that it outperforms
> baselines on several datasets. Our method is efficient and scalable.
>
> **Introduction.** Graphs are everywhere. Anomaly detection on graphs has been studied by many
> researchers using many techniques. Building on our previous deployment experience, we design a
> new architecture that encodes nodes and edges and flags anomalies. We evaluate on standard
> datasets and show strong results. Section 2 covers related work, Section 3 our method, Section 4
> experiments, Section 5 conclusion.

**What's wrong (against `icdm-writing-style` / `icdm-topic-selection` / `icdm-experiments`):**

- **No data regime named** — "graphs are everywhere" is not a mining setting. ICDM wants the data
  regime (here: an unbounded, evolving *edge stream* seen once) on the first page, because the
  regime is what makes the method non-trivial.
- **No named mechanism** — "autoencoder with attention" is an architecture, not a data-mining
  mechanism with a defensible reason to work.
- **Triple-blind leak** — "our previous deployment experience" identifies the authors and is a
  Research Track anonymity violation, not merely a style slip.
- **Scale asserted, not measured** — "efficient and scalable" with no cost model; ICDM reviewers
  read scale claims as testable, not adjectives.
- **Discovery validity ignored** — no argument that flagged anomalies are real rather than
  artifacts of the evaluation, the exact soundness question ICDM referees ask.
- **Over-signposted roadmap** substituting for an argument, wasting first-page space that the
  10-page all-inclusive cap makes precious.

---

## After (ICDM arc — data regime → task → mechanism → baseline + scale → discovery validity)

> **Abstract.** Interaction graphs (payments, messages, click logs) arrive as an **unbounded edge
> stream** that is seen **once** and cannot be stored, yet anomaly detectors are usually defined on
> a materialized graph. We introduce **isolation sketches**, a one-pass structure that maintains
> isolation-style anomaly scores in space **sub-linear in the number of edges**, updating in
> amortized constant time per edge. The mechanism is a randomized partition sketch whose expected
> path length recovers the batch isolation score up to a bounded error we state explicitly. On
> streams where ground-truth injections are known, isolation sketches match a full-storage batch
> detector's ranking while using a small fraction of its memory, and sustain a fixed throughput as
> the stream grows; we report ranking quality and memory with variance over 20 seeded runs.
> *(regime → task → mechanism → error bound → baseline → scale → uncertainty, all on page one.)*
>
> **Introduction.** *(¶1 — regime + task, first breath.)* Many interaction graphs are never
> materialized: edges stream past once — a payment, a message, a click — and must be scored for
> anomalousness **as they arrive**, under memory that cannot grow with the stream. Batch anomaly
> detectors that assume a stored graph do not fit this regime. We give a **one-pass, sub-linear-
> memory** anomaly detector for evolving interaction graphs.
>
> *(¶2 — gap: why existing methods are insufficient, each named.)* Existing approaches fail this
> regime for distinct, nameable reasons. Batch isolation methods need the whole graph in memory, so
> their cost grows with the stream. Reservoir-sampling detectors bound memory but **discard the
> tail edges** where rare anomalies concentrate. Sliding-window graph detectors bound memory by
> *forgetting*, so a slow-building anomaly that spans windows is never scored as one. *(each prior
> line gets a specific failure, not "prior work is limited.")*
>
> *(¶3 — the named mechanism + why it works.)* An **isolation sketch** maintains a bank of
> randomized partitions of the edge space; the expected depth at which an edge is isolated across
> the bank is its anomaly score. We prove this streaming score is an unbiased estimator of the batch
> isolation score with error O(1/√m) in the number of partitions m (Prop. 1), so accuracy is traded
> for memory by a single knob. *(mechanism stated with a checkable guarantee, not an architecture
> diagram.)*
>
> *(¶4 — baseline + scale evidence, each claim paired.)* On synthetic streams with injected
> anomalies where truth is known, isolation sketches recover the batch detector's top-k ranking at
> a small fraction of its memory (Table 1); on three real interaction streams they hold constant
> per-edge latency as the stream length increases by two orders of magnitude (Fig. 2). **All
> numbers carry standard deviations over 20 seeds**, and the partition count, hash family, and
> memory budget are in the appendix within the page cap. *(every claim → table, figure, or bound.)*
>
> *(¶5 — discovery validity + why ICDM + roadmap.)* Because the score is an *unbiased estimate of a
> well-understood batch quantity*, a flagged edge is anomalous in the same sense the batch method
> means — the discovery is not an artifact of streaming. The contribution is a mining primitive for
> a regime where storage is impossible, which is why it belongs at ICDM rather than as one number in
> a systems paper. Section 2 defines the sketch, Section 3 proves the bound, Section 4 reports
> experiments. *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the ICDM bar

Mapped to the skill checklists:

- **Data regime on the first page** — the one-pass, unbounded, cannot-store stream is stated before
  any method detail (`icdm-writing-style`: "name the data regime first").
- **Named mechanism with a reason** — "isolation sketch" is a specific mechanism with an unbiasedness
  bound, not an architecture label (`icdm-topic-selection`: ICDM rewards mechanisms, not model bulk).
- **Scale is measured, not asserted** — constant per-edge latency across two orders of magnitude,
  with a memory knob tied to a stated error (`icdm-experiments`: scale claims are testable).
- **Discovery validity argued** — the flagged anomalies mean what the batch detector means, so the
  finding is not a streaming artifact (`icdm-experiments`: "is the evaluation itself sound?").
- **No overclaiming** — "match the batch ranking at a fraction of memory," with variance over 20
  seeds, not "outperforms baselines" (`icdm-experiments`).
- **Triple-blind clean** — no "our deployment," no identifying system name; the contribution stands
  without author identity (`icdm-submission` anonymity rules).
- **10-page discipline** — the protocol and hash details sit in the appendix **inside** the single
  10-page cap, because at ICDM references and appendix are not a separate budget
  (`icdm-writing-style`, `icdm-supplementary`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, award-verified ICDM
> papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for ICDM-specific submission policy.
