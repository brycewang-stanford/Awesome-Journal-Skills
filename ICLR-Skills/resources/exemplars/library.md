# ICLR Exemplars Library (topic × method)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked to confirm it
> actually appeared at **ICLR (International Conference on Learning Representations)** — not at a sibling
> venue — using the arXiv "Published as a conference paper at ICLR \<year\>" page header and/or the dblp
> `conf/iclr/` record. Papers that could not be confirmed **as ICLR** are **omitted and documented below**.
> It is deliberately a short, clean, verified list (6 verified) rather than a long, guessed one.
>
> **Sibling-confusion guard.** ICLR is *not* NeurIPS, ICML, CVPR, AAAI, or ACL. Landmark deep-learning
> papers are routinely misattributed to ICLR. Confirmed exclusions appear in the "Omitted" section
> (e.g., BERT is NAACL 2019; ResNet is CVPR 2016) so they are never silently added.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent metrics, scores, or quoted findings — read the original on arXiv / OpenReview
> before citing any number. For ICLR-specific policy and scope, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **topic × method** is closest to yours, then study how that paper makes a *simple,
verifiable* central claim carry a *community-wide* representation-learning lesson — the ICLR bar (see
[`../../skills/iclr-topic-selection/SKILL.md`](../../skills/iclr-topic-selection/SKILL.md) and
[`../../skills/iclr-writing-style/SKILL.md`](../../skills/iclr-writing-style/SKILL.md)). For each, ask
the self-check question before claiming your paper is "ICLR-shaped."

---

## By method × topic

### Generative modeling / latent-variable representations (method)

- **Kingma & Welling, "Auto-Encoding Variational Bayes," ICLR 2014.**
  Verified: arXiv `1312.6114`; conference-paper-at-ICLR-2014 (Banff); dblp `conf/iclr/KingmaW14`.
  - **Why it is an exemplar:** one reusable mechanism — the reparameterization trick enabling stochastic
    variational inference at scale — stated cleanly enough to seed an entire generative-modeling subfield
    (the VAE). A "small idea, enormous reach" ICLR paper.
  - **Self-check:** is your core contribution a *mechanism* others can lift into their own models, not a
    single-benchmark architecture?

### Optimization for deep learning (method)

- **Kingma & Ba, "Adam: A Method for Stochastic Optimization," ICLR 2015.**
  Verified: arXiv `1412.6980`; ICLR 2015 conference track; dblp `conf/iclr/KingmaB15`.
  - **Why it is an exemplar:** a simple, broadly applicable optimizer with intuitive hyper-parameters,
    presented so any practitioner could adopt it the next day — community-wide utility over a narrow
    leaderboard win, exactly the "changes how researchers train learning systems" ICLR signal.
  - **Self-check:** does your method help across many models/datasets, or only on the one you tuned it on?

### Sequence representations / attention (method × NLP)

- **Bahdanau, Cho & Bengio, "Neural Machine Translation by Jointly Learning to Align and Translate," ICLR 2015.**
  Verified: arXiv `1409.0473`, PDF header "Published as a conference paper at ICLR 2015"; dblp `conf/iclr/BahdanauCB15`.
  - **Why it is an exemplar:** identifies a concrete representational bottleneck (a fixed-length context
    vector) and removes it with soft attention — a mechanism that generalized far beyond translation.
    The contribution is the *idea*, not the task score.
  - **Self-check:** can you name the specific representational limitation your method removes, and show
    the fix generalizes past the original task?

### Unsupervised representation learning / GANs (method × vision)

- **Radford, Metz & Chintala, "Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks," ICLR 2016.**
  Verified: arXiv `1511.06434`, "Published as a conference paper at ICLR 2016"; dblp `conf/iclr/RadfordMC16`.
  - **Why it is an exemplar:** turns GANs into a *representation-learning* result — architectural
    constraints that yield stable training and features reusable for downstream tasks — and pairs the
    claim with analysis (interpolation, feature transfer), not just samples.
  - **Self-check:** beyond pretty outputs, do you demonstrate the learned representation is *useful* for
    something downstream?

### Graph representation learning (method × structured data)

- **Kipf & Welling, "Semi-Supervised Classification with Graph Convolutional Networks," ICLR 2017.**
  Verified: arXiv `1609.02907`; dblp `conf/iclr/KipfW17` (ICLR 2017 conference track).
  - **Why it is an exemplar:** a localized first-order spectral approximation gives a simple, scalable
    layer that learns representations encoding both graph structure and node features — a minimal model
    that became a default building block. Simplicity *is* the contribution.
  - **Self-check:** is your method the simplest thing that could possibly work for the structure you
    exploit, or could a reviewer strip it down further?

### Architecture / inductive bias at scale (analysis × vision)

- **Dosovitskiy et al., "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale," ICLR 2021.**
  Verified: arXiv `2010.11929`, "Published as a conference paper at ICLR 2021"; dblp `conf/iclr/DosovitskiyB0WZ21`.
  - **Why it is an exemplar:** a clean claim about *inductive bias and scale* — a pure transformer on
    image patches matches or beats CNNs given enough pre-training data — supported by a careful
    data-scale study rather than a single benchmark number. The analysis is the value.
  - **Self-check:** is your headline a *scientific claim* (about bias, scale, or mechanism) backed by a
    controlled study, not just a new state-of-the-art row?

---

## By topic (each cell is a verified ICLR paper above)

| Topic | Verified ICLR exemplar | Year | Method / contribution type |
| --- | --- | --- | --- |
| Generative / latent-variable models | Kingma & Welling, "Auto-Encoding Variational Bayes" | 2014 | Method (VAE / reparameterization) |
| Optimization | Kingma & Ba, "Adam" | 2015 | Method (optimizer) |
| Sequence modeling / attention (NLP) | Bahdanau, Cho & Bengio, "NMT by Jointly Learning to Align and Translate" | 2015 | Method (attention) |
| Unsupervised representation / GANs (vision) | Radford, Metz & Chintala, "DCGAN" | 2016 | Method + analysis |
| Graph representation learning | Kipf & Welling, "Semi-Supervised Classification with GCNs" | 2017 | Method (GCN) |
| Architecture / scale (vision) | Dosovitskiy et al., "An Image is Worth 16x16 Words" (ViT) | 2021 | Analysis + method |

---

## Omitted for sibling-venue confusion or lack of ICLR confirmation (do NOT attribute to ICLR)

To keep the list zero-hallucination and ICLR-specific, the following frequently-misattributed papers were
**excluded** after checking the venue:

- **Devlin et al., "BERT" (2019)** — published at **NAACL-HLT 2019**, *not ICLR*. A canonical
  misattribution; listed here only as a guardrail.
- **He et al., "Deep Residual Learning" (ResNet, 2016)** — published at **CVPR 2016**, *not ICLR*.
- **Goodfellow et al., "Generative Adversarial Nets" (2014)** — published at **NeurIPS/NIPS 2014**, *not
  ICLR*. (The ICLR-verified GAN entry above is the later **DCGAN**, which *is* ICLR 2016.)
- **Vaswani et al., "Attention Is All You Need" (2017)** — published at **NeurIPS/NIPS 2017**, *not ICLR*.
  (The ICLR-verified attention entry above is **Bahdanau et al. 2015**.)

Before adding any new paper to this library, confirm it is **ICLR** specifically — via the arXiv
"Published as a conference paper at ICLR \<year\>" header or the dblp `conf/iclr/` record — and update the
access-date header. When the venue cannot be confirmed as ICLR, **omit** and add it here. When in doubt,
omit.
