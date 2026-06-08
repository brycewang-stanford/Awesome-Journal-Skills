# NeurIPS / NIPS Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked against the
> official NeurIPS proceedings (`proceedings.neurips.cc` / `papers.nips.cc`) to confirm it actually
> appeared at **NeurIPS / NIPS** (the conference was named *NIPS* through 2017 and *NeurIPS* from 2018).
> Papers that could not be confirmed as NeurIPS/NIPS were **omitted** — this is deliberately a short,
> clean, verified list rather than a long, uncertain one (6 verified beats 15 guessed).
>
> **Sibling-confusion guard.** NeurIPS is **not** ICML, ICLR, CVPR, AAAI, ACL/NAACL, or JMLR. Several
> landmark ML papers live at *those* venues and are excluded below with their real venue so they are
> never misattributed to NeurIPS. See the "Omitted / wrong-venue" section.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent metrics, scores, or findings — read the original on the NeurIPS proceedings page
> before citing any number. For NeurIPS-specific submission, checklist, and reproducibility-track policy,
> see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × problem** is closest to yours, then study how that paper poses a problem,
names a specific gap, and ties its contribution to evidence — the NeurIPS bar (see
[`../../skills/neurips-topic-selection/SKILL.md`](../../skills/neurips-topic-selection/SKILL.md),
[`../../skills/neurips-writing-style/SKILL.md`](../../skills/neurips-writing-style/SKILL.md), and
[`../../skills/neurips-experiments/SKILL.md`](../../skills/neurips-experiments/SKILL.md)). For each, ask
the self-check question before claiming your paper is "NeurIPS-shaped." Model your own abstract/intro on
[`../worked-examples/01-introduction.md`](../worked-examples/01-introduction.md).

---

## By method

### A new architecture/model that reframes a task (general method)

- **Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser & Polosukhin, "Attention Is All You Need," NeurIPS 2017.**
  Verified: `proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html`.
  - **Why it is an exemplar:** replaces an entire modeling paradigm (recurrence/convolution for
    sequence transduction) with a single mechanism (self-attention), and the contribution is the
    *reframing*, not just a metric — the canonical "general method that changes how the task is posed"
    NeurIPS paper.
  - **Self-check:** does your method change how the problem is *posed*, so the value survives even if a
    later model beats your number?

### Architecture for large-scale supervised learning (use-inspired / empirical, vision)

- **Krizhevsky, Sutskever & Hinton, "ImageNet Classification with Deep Convolutional Neural Networks," NIPS 2012.**
  Verified: `papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks`.
  - **Why it is an exemplar:** a deep CNN trained at then-unprecedented scale on a real, hard benchmark,
    with the empirical result (and the GPU-training + dropout recipe) carrying a general lesson about
    deep learning — high-quality empirical finding about models and data.
  - **Self-check:** does your empirical result teach the community something general about models, data,
    or scale, rather than only moving one leaderboard?

### Representation learning from a scalable objective (empirical, NLP/embeddings)

- **Mikolov, Sutskever, Chen, Corrado & Dean, "Distributed Representations of Words and Phrases and their Compositionality," NIPS 2013.**
  Verified: `papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality`.
  - **Why it is an exemplar:** a small change to an objective (negative sampling, subsampling) yields
    higher-quality, cheaper word/phrase representations — a method paper whose contribution is a
    *mechanism and an analysis*, not a benchmark headline.
  - **Self-check:** can you isolate the objective/mechanism that produces your gain, the way an
    ablation in `neurips-experiments` would demand?

### A new generative framework (theory + method, generative modeling)

- **Goodfellow, Pouget-Abadie, Mirza, Xu, Warde-Farley, Ozair, Courville & Bengio, "Generative Adversarial Nets," NIPS 2014.**
  Verified: `proceedings.neurips.cc/paper/2014/hash/f033ed80deb0234979a61f95710dbe25-Abstract.html`.
  - **Why it is an exemplar:** poses generative modeling as a two-player minimax game and analyzes the
    objective's optima — a framework + theory contribution that reorganized a whole subfield, exactly
    the "changes understanding/limits of ML behavior" fit signal in `neurips-topic-selection`.
  - **Self-check:** does your contribution introduce a framework whose properties you can *state and
    analyze*, not just instantiate once?

### Scaling study with an empirical regularity (empirical, large language models)

- **Brown, Mann, Ryder, Subbiah, Kaplan, Dhariwal, et al., "Language Models are Few-Shot Learners," NeurIPS 2020.**
  Verified: `papers.nips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html`.
  - **Why it is an exemplar:** a disciplined empirical finding about *scale and in-context learning*,
    evaluated across many tasks — a high-quality empirical contribution about model behavior and
    evaluation rather than a single-benchmark win.
  - **Self-check:** is your empirical claim a *regularity* shown across tasks/scales with honest scope,
    not one number on one dataset?

### A new model class with a theoretical connection (theory + method, generative modeling)

- **Ho, Jain & Abbeel, "Denoising Diffusion Probabilistic Models," NeurIPS 2020.**
  Verified: `papers.nips.cc/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html`.
  - **Why it is an exemplar:** establishes a connection (diffusion models ↔ denoising score matching /
    Langevin dynamics) and derives the training objective from it — the contribution is the *principled
    connection* that makes the method work, not only the sample quality.
  - **Self-check:** does a theoretical connection *explain why* your method works, satisfying the
    "weak scientific explanation is vulnerable" warning in `neurips-submission`?

---

## By topic (each cell is a verified NeurIPS/NIPS paper above)

| Topic | Verified NeurIPS/NIPS exemplar | Year | Venue name that year | Method |
| --- | --- | --- | --- | --- |
| Sequence modeling / architectures | Vaswani et al., "Attention Is All You Need" | 2017 | NIPS | Self-attention architecture |
| Computer vision / supervised learning | Krizhevsky, Sutskever & Hinton, "ImageNet Classification with Deep CNNs" | 2012 | NIPS | Deep CNN (AlexNet) |
| NLP / representation learning | Mikolov et al., "Distributed Representations of Words and Phrases" | 2013 | NIPS | Skip-gram / negative sampling |
| Generative modeling | Goodfellow et al., "Generative Adversarial Nets" | 2014 | NIPS | Adversarial framework + theory |
| Large language models / scaling | Brown et al., "Language Models are Few-Shot Learners" | 2020 | NeurIPS | Empirical scaling study |
| Generative modeling / diffusion | Ho, Jain & Abbeel, "Denoising Diffusion Probabilistic Models" | 2020 | NeurIPS | Diffusion + score-matching connection |

---

## Omitted / wrong-venue (do NOT attribute to NeurIPS — sibling-confusion guard)

To keep the list zero-hallucination, these frequently-misremembered landmark ML papers are **excluded**
because they were **not** published at NeurIPS/NIPS. Listed only as guardrails:

- **Kingma & Ba, "Adam: A Method for Stochastic Optimization" (2015)** — **ICLR**, not NeurIPS.
- **Kingma & Welling, "Auto-Encoding Variational Bayes" / VAE (2014)** — **ICLR**, not NeurIPS.
- **Kipf & Welling, "Semi-Supervised Classification with Graph Convolutional Networks" / GCN (2017)** —
  **ICLR**, not NeurIPS.
- **He, Zhang, Ren & Sun, "Deep Residual Learning for Image Recognition" / ResNet (2016)** — **CVPR**,
  not NeurIPS.
- **Devlin, Chang, Lee & Toutanova, "BERT" (2019)** — **NAACL**, not NeurIPS.

Each of these belongs to a NeurIPS sibling venue (ICLR / CVPR / NAACL). If you want one of them as an
exemplar, cite it to its real venue — never to NeurIPS.

---

## Verification note and how to extend

Each entry above was confirmed on 2026-06-08 by locating its official NeurIPS proceedings page
(`proceedings.neurips.cc` or the legacy `papers.nips.cc`) with the matching year. Before adding any new
paper to this library:

1. Find its **official NeurIPS proceedings page** (not a blog, arXiv, or a SemanticScholar/ACM mirror
   alone) and confirm the year.
2. Confirm the venue is **NeurIPS or NIPS** — not ICML, ICLR, CVPR, AAAI, ACL/NAACL, or JMLR.
3. Update the access-date header. **When in doubt, omit.**
