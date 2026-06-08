# AAAI Exemplars Library (topic × method)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked to confirm it
> appeared in the **main technical proceedings of the AAAI Conference on Artificial Intelligence**, with
> an article page on the official AAAI proceedings host (`ojs.aaai.org/index.php/AAAI/...`). Papers that
> could not be cleanly confirmed as *main-conference AAAI* were **omitted and documented below** — this
> is deliberately a short, clean list (5 verified > many guessed).
>
> **Sibling-confusion guard.** "AAAI" here means the **AAAI Conference on Artificial Intelligence main
> technical track only**. It is *not* IJCAI, NeurIPS/NIPS, ICML, ICLR, ACL, CVPR, the AAAI
> Workshop/Symposium (e.g. Fall/Spring Symposium) series, IAAI, EAAI, or *AI Magazine*. Each entry below
> was verified to be on the `ojs.aaai.org/index.php/AAAI` proceedings path, not a sibling venue.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent metrics or specific results — read the original on the AAAI Digital Library
> (`ojs.aaai.org`) before citing any number. For AAAI-specific policy, page limits, and scope, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **topic × method** is closest to yours, then study how that paper makes a *broad AI*
contribution legible to a non-specialist program committee — the AAAI bar (see
[`../../skills/aaai-topic-selection/SKILL.md`](../../skills/aaai-topic-selection/SKILL.md) and
[`../../skills/aaai-writing-style/SKILL.md`](../../skills/aaai-writing-style/SKILL.md)). For each, ask
the self-check question before claiming your paper is "AAAI-shaped."

---

## By method

### Reinforcement learning — fixing a known estimator's bias (RL / deep RL)

- **van Hasselt, Guez & Silver, "Deep Reinforcement Learning with Double Q-Learning," AAAI 2016 (Thirtieth AAAI Conference on Artificial Intelligence).**
  Verified: `ojs.aaai.org/index.php/AAAI/article/view/10295`.
  - **Why it is an exemplar:** isolates a concrete, general defect (Q-value overestimation in DQN),
    explains *why* it happens, and fixes it with a minimal, well-motivated change evaluated across many
    Atari games — a "diagnose a mechanism, then repair it" paper that any RL reviewer can follow.
  - **Self-check:** does your method fix an identified mechanism (not just bump a score), with evidence
    that the mechanism — not the dataset — drives the gain?

### Knowledge-graph completion — convolutional link prediction (representation learning)

- **Dettmers, Minervini, Stenetorp & Riedel, "Convolutional 2D Knowledge Graph Embeddings" (ConvE), AAAI 2018 (Thirty-Second AAAI Conference on Artificial Intelligence).**
  Verified: `ojs.aaai.org/index.php/AAAI/article/view/11573`.
  - **Why it is an exemplar:** a parameter-efficient architecture for link prediction whose claim
    (efficiency *and* accuracy on standard KG benchmarks) is stated crisply and supported with controlled
    comparisons — a clean "new model + fair baselines" contribution.
  - **Self-check:** is your architectural claim backed by parameter/compute-matched comparisons rather
    than an unfair scale advantage?

### Knowledge-graph embedding — separate entity/relation spaces (representation learning)

- **Lin, Liu, Sun, Liu & Zhu, "Learning Entity and Relation Embeddings for Knowledge Graph Completion" (TransR), AAAI 2015 (Twenty-Ninth AAAI Conference on Artificial Intelligence).**
  Verified: `ojs.aaai.org/index.php/AAAI/article/view/9491`.
  - **Why it is an exemplar:** identifies a limitation of translating-embedding models (entities and
    relations forced into one space) and proposes a targeted fix (relation-specific projection) — a
    well-scoped representation-learning advance with a clear before/after motivation.
  - **Self-check:** can you name the prior model's specific limitation your representation removes, in one
    sentence a broad reviewer grasps?

### Text classification — graph neural network over a corpus graph (NLP / graph learning)

- **Yao, Mao & Luo, "Graph Convolutional Networks for Text Classification" (Text GCN), AAAI 2019 (Thirty-Third AAAI Conference on Artificial Intelligence).**
  Verified: `ojs.aaai.org/index.php/AAAI/article/view/4725`.
  - **Why it is an exemplar:** reframes text classification as node classification on a single
    corpus-level word–document graph — a conceptual move that travels beyond one dataset and is
    intelligible to both NLP and graph-learning reviewers.
  - **Self-check:** does your method offer a reframing (a new way to *pose* the task), not only a new
    score on the old framing?

### Skeleton-based action recognition — spatial-temporal graph convolution (vision / graph learning)

- **Yan, Xiong & Lin, "Spatial Temporal Graph Convolutional Networks for Skeleton-Based Action Recognition" (ST-GCN), AAAI 2018 (Thirty-Second AAAI Conference on Artificial Intelligence).**
  Verified: `ojs.aaai.org/index.php/AAAI/article/view/12328`.
  - **Why it is an exemplar:** generalizes graph convolution to the spatio-temporal skeleton domain,
    turning a structured input (body joints over time) into a principled GCN — a model whose inductive
    bias is the contribution, not a heuristic feature set.
  - **Self-check:** is your model's inductive bias matched to the structure of the data, and is that match
    the reason it wins?

---

## By topic (each cell is a verified AAAI main-conference paper above)

| Topic | Verified AAAI exemplar | Year (conference no.) | Method |
| --- | --- | --- | --- |
| Reinforcement learning | van Hasselt, Guez & Silver, "Double Q-Learning" | 2016 (30th) | Deep RL / value estimation |
| Knowledge-graph completion | Dettmers et al., "ConvE" | 2018 (32nd) | 2D convolutional embeddings |
| Knowledge-graph embedding | Lin et al., "TransR" | 2015 (29th) | Relation-space projection |
| Text classification | Yao, Mao & Luo, "Text GCN" | 2019 (33rd) | Graph convolutional network |
| Action recognition (skeleton) | Yan, Xiong & Lin, "ST-GCN" | 2018 (32nd) | Spatio-temporal GCN |

---

## Omitted for lack of clean main-AAAI verification (do NOT attribute to AAAI without re-checking)

To keep the list zero-hallucination, the following well-known papers were **excluded** after web search
(2026-06-08) because they belong to a **sibling venue** or could not be confirmed on the
`ojs.aaai.org/index.php/AAAI` main-conference path. Listed here purely as guardrails:

- **Hinton, Vinyals & Dean, "Distilling the Knowledge in a Neural Network" (2015)** — circulated as an
  **arXiv** preprint / NIPS-2014 Deep Learning Workshop item; **not** an AAAI main-conference paper.
- **Andrychowicz et al., "Hindsight Experience Replay" (2017)** — published at **NIPS/NeurIPS**, not AAAI.
- **Wang et al., "Dueling Network Architectures for Deep Reinforcement Learning" (2016)** — published at
  **ICML** (best-paper), not AAAI.
- **Helmert, "The Fast Downward Planning System" (2006)** — published in the **Journal of Artificial
  Intelligence Research (JAIR)**, a journal, not the AAAI conference.
- **Moravčík et al., "DeepStack" (2017)** — published in **Science**, not AAAI.
- **Richter, Helmert & Westphal, "Landmarks Revisited" (AAAI-08)** — plausibly AAAI-2008 main conference,
  but a direct `ojs.aaai.org/index.php/AAAI` article page was **not confirmed** before search quota was
  exhausted; omitted pending a clean check rather than attributed on memory.

Before adding any new paper to this library, confirm it on `ojs.aaai.org/index.php/AAAI` (article page,
with the conference number / year) — **not** a workshop, symposium, IJCAI, NeurIPS, ICML, ICLR, ACL,
CVPR, or *AI Magazine* page — and update the access-date header. When in doubt, omit.
