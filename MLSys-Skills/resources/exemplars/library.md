# MLSys Exemplars Library (topic × contribution shape)

> **Verified via web search, access date 2026-07-08.** Every paper below was confirmed against the
> venue's own archive (`proceedings.mlsys.org`) or the official conference site (dblp used as a
> secondary cross-check) to have appeared at the **Conference on Machine Learning and Systems**
> (including its first two editions under the SysML name). Papers that could not be cleanly pinned
> to MLSys were left out — a short list you can trust beats a long list you must re-verify.
>
> **Sibling-confusion guard:** the ML-systems literature is scattered across OSDI, SOSP, NSDI,
> ASPLOS, ATC, EuroSys, and the big ML conferences. Famous systems you associate with "MLSys the
> field" often did **not** appear at MLSys the venue — see the omissions section. Never cite a
> serving or training system "at MLSys" on vibes; check the proceedings page.
>
> **Use principle (zero hallucination):** rows give **design positioning only** — how each paper
> frames a systems contribution for this reviewer pool. Speedup numbers, hardware details, and
> configuration specifics must be re-read from the original before being quoted anywhere.

---

## How to use this library

Find the row closest to your project's **topic × contribution shape**, then study how that paper
(a) names a reusable abstraction or mechanism rather than an engineering effort, and (b) ties every
performance claim to a measured workload. That pairing is the MLSys bar — see
[`../../skills/mlsys-writing-style/SKILL.md`](../../skills/mlsys-writing-style/SKILL.md),
[`../../skills/mlsys-experiments/SKILL.md`](../../skills/mlsys-experiments/SKILL.md), and
[`../../skills/mlsys-topic-selection/SKILL.md`](../../skills/mlsys-topic-selection/SKILL.md).

## By contribution shape

### Search-space abstraction for distributed training (systems-for-ML)

- **Jia, Zaharia & Aiken, "Beyond Data and Model Parallelism for Deep Neural Networks," SysML/MLSys 2019.**
  Verified: `proceedings.mlsys.org/paper_files/paper/2019/hash/b422680f3db0986ddd7f8f126baaf0fa-Abstract.html`.
  - **Why it is an exemplar:** defines the SOAP search space (sample, operator, attribute,
    parameter) and pairs it with a fast execution simulator inside FlexFlow — the contribution is
    the **named abstraction plus a cost model**, not the engine's line count.
  - **Self-check:** can you state your search space or design space as crisply as "SOAP," and does
    a cheap predictor let you explore it without running every configuration?

### Community benchmark methodology (benchmarks and measurement)

- **Mattson et al., "MLPerf Training Benchmark," MLSys 2020.**
  Verified: listed in the MLSys 2020 proceedings (`proceedings.mlsys.org/book/2020`).
  - **Why it is an exemplar:** turns "how fast is training?" into a specified, auditable
    methodology — time-to-quality targets, defined workloads, run rules — and seeded the MLPerf
    lineage that later grew into MLCommons. The venue's benchmark-rigor culture in one paper.
  - **Self-check:** if your paper claims a speedup, could a skeptic rerun it under rules as
    explicit as MLPerf's? If your paper *is* a benchmark, does it define quality targets and
    forbidden optimizations, not just a dataset list?

### Optimization algorithm shaped by deployment constraints (federated learning)

- **Li, Sahu, Zaheer, Sanjabi, Talwalkar & Smith, "Federated Optimization in Heterogeneous Networks," MLSys 2020.**
  Verified: MLSys 2020 proceedings (`proceedings.mlsys.org/book/2020`).
  - **Why it is an exemplar:** FedProx is an algorithm paper that earns its systems venue by
    treating device heterogeneity — stragglers, partial work, variable participation — as the
    first-class constraint, with convergence analysis under that constraint.
  - **Self-check:** does a real deployment constraint change your algorithm's design, or is the
    systems setting only in the introduction?

### Analytical cost model driving inference partitioning (LLM serving)

- **Pope, Douglas, Chowdhery, Devlin, Bradbury, Heek, Xiao, Agrawal & Dean, "Efficiently Scaling Transformer Inference," MLSys 2023.**
  Verified: dblp `conf/mlsys/PopeDCDBHXAD23`; MLSys 2023 Outstanding Paper.
  - **Why it is an exemplar:** builds a simple analytical model of inference efficiency, uses it
    to pick multi-dimensional partitioning for 500B+ models on TPU v4, and reports a **Pareto
    frontier over latency and utilization** rather than a single headline number.
  - **Self-check:** do you expose the latency/throughput/cost tradeoff curve, or only the one
    point where your system wins?

### Hardware-friendly model compression with a serving system (quantization)

- **Lin, Tang, Tang, Yang, Chen, Wang, Xiao, Dang, Gan & Han, "AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration," MLSys 2024.**
  Verified: `mlsys.org/virtual/2024/poster/2653`; MLSys 2024 Best Paper Award.
  - **Why it is an exemplar:** couples an insight (protecting ~1% of salient weights, chosen by
    activations, preserves quality) with TinyChat, a runtime that converts the insight into
    measured on-device speedups — the co-design loop MLSys exists to publish.
  - **Self-check:** does your ML-side idea come with the runtime work that proves the hardware
    win, and vice versa?

---

## By topic (all rows verified above)

| Topic | Verified MLSys exemplar | Edition | Contribution shape |
| --- | --- | --- | --- |
| Distributed training strategy | Jia, Zaharia & Aiken, FlexFlow/SOAP | 2019 (SysML) | Search-space abstraction + simulator |
| Benchmark methodology | Mattson et al., MLPerf Training | 2020 | Community measurement rules |
| Federated learning | Li et al., FedProx | 2020 | Algorithm under deployment constraints |
| LLM inference at scale | Pope et al., Efficiently Scaling Transformer Inference | 2023 | Analytical model + partitioning |
| Quantization + serving | Lin et al., AWQ | 2024 | Compression/runtime co-design |

The 2019→2024 spread is deliberate: it shows the venue's center of gravity moving from
training-time parallelism toward LLM inference and on-device serving, which matters when you
position "why now" in the introduction.

---

## Omitted after checking (do not attribute to MLSys without re-verification)

- **vLLM / PagedAttention (Kwon et al.)** — published at **SOSP 2023**, not MLSys, despite being
  the most-cited LLM-serving system. A classic misattribution.
- **PipeDream (Narayanan et al.)** — **SOSP 2019**. Pipeline-parallel training's flagship lives in
  an OS venue.
- **FlashAttention (Dao et al.)** — **NeurIPS 2022**. Kernel-level ML-systems work, but an ML
  conference paper.
- **Megatron-LM scaling papers** — arXiv reports and **SC** papers, not MLSys proceedings.

Before adding a row, open the paper's landing page on `proceedings.mlsys.org` (or the mlsys.org
virtual-site poster page for recent editions), match title, authors, and edition, and update the
access-date header. If verification fails or search is unavailable, add the candidate as
**待核实 / TO VERIFY** with no venue attribution rather than guessing.
