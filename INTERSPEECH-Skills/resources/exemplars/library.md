# INTERSPEECH Exemplars Library (task × contribution)

> **Verified via web search on 2026-07-08.** Every row below was checked against the
> **ISCA Archive** (`www.isca-archive.org/interspeech_<year>/...`) — title, author
> list, page range, and DOI — to confirm the paper genuinely appeared at
> **Interspeech**, the ISCA flagship, and not at a sibling venue. Speech's most
> famous papers are scattered across ICASSP, NeurIPS, ICML, LREC, and journals, so
> venue attribution is checked per paper; anything unconfirmable was omitted or
> listed in the misattribution guard below.
>
> **Use principle (zero hallucination):** these rows give *positioning* only. No
> result numbers, architectures details, or claims are reproduced here — read the
> Archive PDF before citing anything beyond title/venue/DOI.

---

## How to use this library

Find the row nearest your task × contribution type, then study how that paper won
inside **4 pages**: one clearly named move, evaluation in the community's own
metrics, and enough protocol disclosure to be reproduced. Pair each with the
self-check question before calling your own draft "Interspeech-shaped" (see
[`../../skills/interspeech-writing-style/SKILL.md`](../../skills/interspeech-writing-style/SKILL.md)
and
[`../../skills/interspeech-experiments/SKILL.md`](../../skills/interspeech-experiments/SKILL.md)).

## Verified exemplars

### ASR architecture — Conformer (Interspeech 2020)

- **Gulati, Qin, Chiu, Parmar, Zhang, Yu, Han, Wang, Zhang, Wu & Pang,
  "Conformer: Convolution-augmented Transformer for Speech Recognition,"
  Interspeech 2020, pp. 5036–5040, DOI 10.21437/Interspeech.2020-3015.**
  Verified: `www.isca-archive.org/interspeech_2020/gulati20_interspeech.html`.
  - **Why it exemplifies the venue:** one architectural move (convolution inside
    the Transformer block), named once, ablated cleanly, evaluated on the shared
    LibriSpeech yardstick — a complete argument in four pages that became the
    community's default encoder.
  - **Self-check:** can your method be stated as *one* modification to a cited
    standard, with an ablation isolating exactly that modification?

### Training method — SpecAugment (Interspeech 2019)

- **Park, Chan, Zhang, Chiu, Zoph, Cubuk & Le, "SpecAugment: A Simple Data
  Augmentation Method for Automatic Speech Recognition," Interspeech 2019,
  pp. 2613–2617, DOI 10.21437/Interspeech.2019-2680.**
  Verified: `www.isca-archive.org/interspeech_2019/park19e_interspeech.html`.
  - **Why it exemplifies the venue:** a method operating on the *speech
    representation itself* (time/frequency masking on the spectrogram), cheap to
    adopt, evaluated where everyone could verify it. Simplicity presented without
    apology is an Interspeech virtue.
  - **Self-check:** if your method is simple, is the evaluation strong enough to
    carry it — and is the recipe adoptable from the paper alone?

### Speaker verification — ECAPA-TDNN (Interspeech 2020)

- **Desplanques, Thienpondt & Demuynck, "ECAPA-TDNN: Emphasized Channel Attention,
  Propagation and Aggregation in TDNN Based Speaker Verification," Interspeech
  2020, pp. 3830–3834, DOI 10.21437/Interspeech.2020-2650.**
  Verified: `www.isca-archive.org/interspeech_2020/desplanques20_interspeech.html`.
  - **Why it exemplifies the venue:** speaks the speaker-recognition community's
    protocol language — standard trial lists, EER/minDCF — while packing several
    architectural refinements into a coherent, reproducible system that challenge
    participants adopted immediately.
  - **Self-check:** does your evaluation use the official trial lists and both
    operating-point metrics, so results slot into the community's tables?

### Speech synthesis — Tacotron (Interspeech 2017)

- **Wang, Skerry-Ryan, Stanton, Wu, Weiss, Jaitly, Yang, Xiao, Chen, Bengio, Le,
  Agiomyrgiannakis, Clark & Saurous, "Tacotron: Towards End-to-End Speech
  Synthesis," Interspeech 2017, pp. 4006–4010, DOI 10.21437/Interspeech.2017-1452.**
  Verified: `www.isca-archive.org/interspeech_2017/wang17n_interspeech.html`.
  - **Why it exemplifies the venue:** a paradigm claim (text-to-spectrogram
    end-to-end) made credible through subjective evaluation (MOS) plus audio
    samples — evidence a listener can check — rather than through scale alone.
  - **Self-check:** for a generation claim, do MOS protocol details and listenable
    samples back every adjective in your abstract?

### Benchmark / evaluation methodology — SUPERB (Interspeech 2021)

- **Yang, Chi, Chuang, Lai, Lakhotia, Lin, Liu, Shi, Chang, Lin, Huang, Tseng,
  Lee, Liu, Huang, Dong, Li, Watanabe, Mohamed & Lee, "SUPERB: Speech processing
  Universal PERformance Benchmark," Interspeech 2021, pp. 1194–1198,
  DOI 10.21437/Interspeech.2021-1775.**
  Verified: `www.isca-archive.org/interspeech_2021/yang21c_interspeech.html`.
  - **Why it exemplifies the venue:** a resource/benchmark contribution accepted on
    the strength of its design — task suite, frozen-representation protocol,
    leaderboard — showing that Interspeech rewards evaluation infrastructure, not
    only systems.
  - **Self-check:** if your contribution is a resource, is the *protocol* specified
    tightly enough that two labs would produce comparable numbers?

## Task × contribution matrix

| Task lane | Exemplar | Year / pages | Contribution type |
| --- | --- | --- | --- |
| ASR modeling | Conformer | 2020 / 5036–5040 | Architecture |
| ASR training | SpecAugment | 2019 / 2613–2617 | Data augmentation method |
| Speaker verification | ECAPA-TDNN | 2020 / 3830–3834 | System + protocol fluency |
| TTS | Tacotron | 2017 / 4006–4010 | Paradigm + subjective evaluation |
| Self-supervised evaluation | SUPERB | 2021 / 1194–1198 | Benchmark / methodology |

## Misattribution guard — famous speech papers that are NOT Interspeech

Cite these with their true venues; getting them wrong is an instant credibility
loss with speech reviewers:

- **LibriSpeech** (Panayotov et al.) — **ICASSP 2015**, not Interspeech.
- **x-vectors** (Snyder et al.) — **ICASSP 2018**.
- **wav2vec 2.0** (Baevski et al.) — **NeurIPS 2020** (the original wav2vec was a
  conference paper in 2019 — verify its venue before citing; do not assume).
- **Whisper** (Radford et al.) — **ICML 2023**.
- **Common Voice** (Ardila et al.) — **LREC 2020**.
- **HuBERT** (Hsu et al.) — **IEEE/ACM TASLP** (journal), despite its fame in the
  conference era.

## Adding rows

Confirm the candidate on the ISCA Archive: the URL pattern is
`www.isca-archive.org/interspeech_<year>/<firstauthor><yy><suffix>_interspeech.html`,
and the DOI must resolve under prefix `10.21437`. Record authors, pages, DOI, and
update this file's access date. If the Archive page cannot be confirmed, mark the
row **待核实** with no venue attribution — or leave it out. Fewer verified rows
beat many guessed ones.
