# COLM Exemplars Library (award lineage, first two editions)

> **Verified via web search on 2026-07-08.** COLM is three editions old, so this library is built
> from the venue's own award lineage: the **Outstanding Paper Awards of COLM 2024 and COLM 2025**
> (four per edition; in 2025 awarded to fewer than 0.3% of submissions). Each entry was
> cross-checked against search renderings of the official accepted-paper lists
> (`colmweb.org/2024/AcceptedPapers.html`, `colmweb.org/2025/AcceptedPapers.html`) and, for the
> two Johns Hopkins-affiliated awards, against the JHU CS department's independent coverage.
> Read every paper on OpenReview (the COLM proceedings home) before citing results — this file
> records positioning only, never numbers.
>
> **Venue-confusion guard:** COLM papers are *not* in the ACL Anthology and *not* in a PMLR
> volume. An arXiv page saying "Published as a conference paper at COLM 20XX" is a claim, not a
> proof — confirm the title on the COLM accepted list or the COLM OpenReview group. Conversely,
> many famous LM papers people associate with COLM actually live at ICLR, NeurIPS, or *CL venues,
> because COLM did not exist before 2024. Anything published before October 2024 cannot be a
> COLM paper.

---

## How to use this library

The award set is small but unusually informative, because it shows what a *new* venue chose to
celebrate in its first two years — the clearest available signal of COLM's identity. Three
patterns recur across the eight awards: (a) the language model itself is the object of study,
not a tool applied to a task; (b) careful measurement or analysis beats leaderboard deltas;
(c) claims are scoped to what was actually tested. Match your project to the nearest entry,
then answer its self-check question honestly.

## COLM 2024 Outstanding Papers (first edition, Philadelphia)

- **"Dated Data: Tracing Knowledge Cutoffs in Large Language Models"** — Jeffrey Cheng, Marc
  Marone, Orion Weller, Dawn Lawrie, Daniel Khashabi, Benjamin Van Durme.
  Cross-checked via the JHU CS news item and the 2024 accepted list.
  - *Why it is an exemplar:* interrogates a property every practitioner assumes they know —
    the effective knowledge cutoff — and shows measurement of training-data reality beats the
    label on the model card. Pure "LM as object of study."
  - *Self-check:* does your paper measure something about LMs that the community currently
    takes on faith?
- **"Mamba: Linear-Time Sequence Modeling with Selective State Spaces"** — Albert Gu, Tri Dao.
  Cross-checked via the 2024 accepted list and award coverage.
  - *Why it is an exemplar:* an architecture paper that found its archival home at COLM's first
    edition — evidence the venue publishes foundational modeling work, not only analysis and
    evaluation.
  - *Self-check:* if your contribution is architectural, is the sequence-modeling story (not a
    single downstream task) the spine of the paper?
- **"AI-generated text boundary detection with RoFT"** — Laida Kushnareva, Tatiana Gaintseva,
  Dmitry Abulkhanov, Kristian Kuznetsov, German Magai, Eduard Tulchinskii, Serguei Barannikov,
  Sergey Nikolenko, Irina Piontkovskaya.
  - *Why it is an exemplar:* a societal-impact problem (detecting where generated text begins)
    treated with methodological care rather than alarm — COLM's safety/misuse lane done well.
  - *Self-check:* does your safety or misuse paper deliver a method and an evaluation, not just
    a concern?
- **"Auxiliary task demands mask the capabilities of smaller language models"** — Jennifer Hu,
  Michael Frank.
  - *Why it is an exemplar:* a cognitive-science-flavored critique of evaluation itself,
    showing measured "capability" depends on task framing — the multi-disciplinary community
    COLM says it wants, in action.
  - *Self-check:* could a reviewer from outside core ML read your evaluation-critique paper
    and recognize their field's standards in it?

## COLM 2025 Outstanding Papers (second edition, Montreal)

- **"Hidden in plain sight: VLMs overlook their visual representations"** — Stephanie Fu,
  tyler bonnen, Devin Guillory, Trevor Darrell.
  - *Why it is an exemplar:* diagnostic analysis of *why* vision-language models fail —
    localizing the failure between the visual encoder and the LM — rather than another
    benchmark score. Note COLM's scope reaches multimodal models when the LM is central.
  - *Self-check:* when your model fails, can you say *where* in the stack, with evidence?
- **"Shared Global and Local Geometry of Language Model Embeddings"** — Andrew Lee, Melanie
  Weber, Fernanda Viégas, Martin Wattenberg.
  - *Why it is an exemplar:* interpretability grounded in structure found across models, with
    the finding itself as the contribution — no application required to justify it.
  - *Self-check:* is your interpretability claim demonstrated on more than one model family?
- **"Don't lie to your friends: Learning what you know from collaborative self-play"** — Jacob
  Eisenstein, Reza Aghajani, Adam Fisch, Dheeru Dua, Fantine Huot, Mirella Lapata, Vicky
  Zayats, Jonathan Berant.
  - *Why it is an exemplar:* a training-method paper aimed at calibration/honesty — the
    post-training lane of the CFP — where the mechanism (self-play among agents) is analyzed,
    not just shown to help.
  - *Self-check:* does your post-training paper explain *why* the method changes model
    behavior, beyond the score delta?
- **"Fast Controlled Generation from Language Models with Adaptive Weighted Rejection
  Sampling"** (author list confirmed partially in coverage — pull the full list from the 2025
  accepted list before citing).
  - *Why it is an exemplar:* inference-time machinery — constrained decoding made cheaper —
    showing COLM rewards the generation/inference lane alongside training and evaluation.
  - *Self-check:* does your inference paper quantify the cost-quality trade-off it claims to
    improve?

## Award lineage at a glance

| Edition | Analysis / measurement | Architecture / training | Inference | Safety & evaluation critique |
| --- | --- | --- | --- | --- |
| 2024 (Philadelphia) | Dated Data | Mamba | — | RoFT boundary detection; Auxiliary task demands |
| 2025 (Montreal) | VLM visual representations; Embedding geometry | Collaborative self-play | Adaptive weighted rejection sampling | — |

Both cohorts reward **understanding over leaderboard movement**: five of eight awards are
measurement, analysis, or evaluation-critique papers. If your COLM draft's main evidence is a
single benchmark table, this lineage is a warning.

## Verification recipe before adding entries

1. Find the title on the official accepted list for the claimed edition
   (`colmweb.org/<year>/AcceptedPapers.html`) or in the COLM OpenReview group.
2. Record the full author list from that official source, not from arXiv.
3. Confirm award status from a COLM announcement or an independent institutional page — award
   claims travel badly through secondary blogs.
4. If any step fails, add the entry as **待核实 / TO VERIFY** with no attribution, or omit it.
   Eight verified papers beat thirty guessed ones.
