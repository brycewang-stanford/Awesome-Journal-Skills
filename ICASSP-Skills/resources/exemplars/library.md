# ICASSP Exemplars Library (task × method)

> **Verified via web search and dblp, access date 2026-07-09.** Every paper below was matched
> against the **dblp ICASSP proceedings index** (`dblp.org/db/conf/icassp/`) and/or its **IEEE
> Xplore DOI** to confirm it appeared at the **IEEE International Conference on Acoustics, Speech
> and Signal Processing (ICASSP)** in the stated year — not at a sibling venue. Papers that could
> not be cleanly confirmed as ICASSP were **omitted and documented below**. This is deliberately
> a short, verified list (6 verified beats 15 guessed).
>
> **Sibling-confusion guard:** ICASSP is **not** Interspeech, not ICIP, not EUSIPCO, not WASPAA,
> and not an IEEE SPS *journal* (TASLP/TSP/SPL). Signal-processing landmarks are scattered across
> all of these; several famous "speech" papers are actually Interspeech or journal papers. A
> Google Scholar "ICASSP-like" hit is not proof — each row was checked to be an ICASSP edition.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does
> not reproduce or invent result numbers, table values, or metric deltas — read the original on
> IEEE Xplore before citing anything. For ICASSP policy and the do-not-misattribute list, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

ICASSP's breadth is a feature: the same 4-page object must land a precise **signal-processing
contribution** whether the signal is speech, general audio, an image, or a channel. Pick the row
whose **task × method** is closest to yours, then study how that paper states a concrete problem,
a mechanism, and a **task-matched measurement** on the first two pages. For each, answer the
self-check before claiming your paper is "ICASSP-shaped." Pair this with
[`../../skills/icassp-writing-style/SKILL.md`](../../skills/icassp-writing-style/SKILL.md),
[`../../skills/icassp-topic-selection/SKILL.md`](../../skills/icassp-topic-selection/SKILL.md),
and [`../../skills/icassp-experiments/SKILL.md`](../../skills/icassp-experiments/SKILL.md).

---

## By method

### End-to-end sequence acoustic modeling (speech recognition)

- **Graves, Mohamed & Hinton, "Speech Recognition with Deep Recurrent Neural Networks," ICASSP
  2013, pp. 6645-6649.** Verified: dblp `conf/icassp/GravesMH13`, DOI `10.1109/ICASSP.2013.6638947`.
  - **Why it is an exemplar:** replaces a hand-built pipeline stage with a deep bidirectional
    LSTM trained end-to-end and reports on a standard benchmark — a mechanism change with a
    task-matched number, the ICASSP unit of contribution.
  - **Self-check:** does your paper change a specific block of the signal chain and measure the
    change on an established benchmark, rather than reporting a whole new system in the abstract?

### Attention-based encoder-decoder recognition (speech recognition)

- **Chan, Jaitly, Le & Vinyals, "Listen, Attend and Spell," ICASSP 2016.** Verified: DOI
  `10.1109/ICASSP.2016.7472621`.
  - **Why it is an exemplar:** folds acoustic, pronunciation, and language modeling into one
    attention network and states plainly what the "listener" and "speller" each do — a clean,
    reproducible architectural claim that fits four pages.
  - **Self-check:** can a reader redraw your architecture from the paper alone and see exactly
    which prior components it removes?

### Corpus and resource contribution (data for the community)

- **Panayotov, Chen, Povey & Khudanpur, "Librispeech: an ASR Corpus Based on Public Domain Audio
  Books," ICASSP 2015.** Verified: dblp `conf/icassp/PanayotovCPK15`.
  - **Why it is an exemplar:** a *resource* paper that succeeds at ICASSP by documenting
    construction, licensing, and a baseline recipe so precisely that the corpus becomes a
    community standard — proof that not every ICASSP contribution is a new model.
  - **Self-check:** if your contribution is data, is the construction reproducible and the
    baseline recipe shipped, so others can build on it exactly?

### Neural source separation (audio, beyond recognition)

- **Hershey, Chen, Le Roux & Watanabe, "Deep Clustering: Discriminative Embeddings for
  Segmentation and Separation," ICASSP 2016.** Verified: DOI `10.1109/ICASSP.2016.7471631`.
  - **Why it is an exemplar:** frames speaker-independent separation as learning an embedding
    where time-frequency bins cluster by source — a genuinely new problem formulation evaluated
    with a signal-quality metric, not a leaderboard tweak.
  - **Self-check:** does your method introduce a formulation a reviewer can restate in one
    sentence, evaluated with the metric that actually matters for the task (here, SDR-type gain)?

### Large-scale audio classification (general audio, not speech)

- **Hershey et al., "CNN Architectures for Large-Scale Audio Classification," ICASSP 2017,
  pp. 131-135.** Verified: dblp `conf/icassp/HersheyCEGJMPPS17`, DOI `10.1109/ICASSP.2017.7952132`.
  - **Why it is an exemplar:** a controlled comparison of CNN architectures on massive weakly
    labeled audio — demonstrating ICASSP's non-speech audio breadth and the value of a clean
    architecture-vs-architecture study with a shared evaluation.
  - **Self-check:** if your paper is a comparison, is one variable moved at a time under a fixed
    protocol, so the reported difference is attributable?

### Deep speaker embeddings (speaker recognition / verification)

- **Snyder, Garcia-Romero, Sell, Povey & Khudanpur, "X-Vectors: Robust DNN Embeddings for
  Speaker Recognition," ICASSP 2018.** Verified: dblp ICASSP 2018 proceedings.
  - **Why it is an exemplar:** a fixed-dimensional DNN embedding with data augmentation,
    evaluated with the field's own scoring (EER / minDCF on standard trial lists) — the template
    for "new representation + task-correct metric" at ICASSP.
  - **Self-check:** are you reporting the community metric on a standard trial list, and did you
    ship or cite the exact split so the number is checkable?

---

## By task (each cell is a verified ICASSP paper above)

| Task | Verified ICASSP exemplar | Edition | Method |
| --- | --- | --- | --- |
| Speech recognition (sequence AM) | Graves, Mohamed & Hinton, "Deep RNN Speech Recognition" | 2013 | Bidirectional LSTM, end-to-end |
| Speech recognition (attention) | Chan et al., "Listen, Attend and Spell" | 2016 | Attention encoder-decoder |
| Corpus / resource | Panayotov et al., "Librispeech" | 2015 | Public-domain ASR corpus + recipe |
| Source separation | Hershey et al., "Deep Clustering" | 2016 | Embedding clustering of TF bins |
| General audio classification | Hershey et al., "CNN Architectures for Audio" | 2017 | CNN architecture comparison |
| Speaker recognition | Snyder et al., "X-Vectors" | 2018 | DNN speaker embeddings, EER/minDCF |

> The 2013 → 2016 recognition pair (RNN transducer-style → attention encoder-decoder) also traces
> a **research line** inside ICASSP, useful when positioning an incremental-but-principled step.

---

## Breadth note and omissions (do not attribute to ICASSP without re-checking)

The verified set above leans toward speech/audio because those editions were easy to confirm on
dblp; ICASSP's **image, video, communications, radar, array, and estimation** tracks are equally
central. Before adding an image/comms exemplar, confirm it on dblp `conf/icassp/` the same way —
do not import a paper that actually lives at **ICIP, EUSIPCO, WASPAA, or an SPS journal**.

Common traps checked and **excluded** to keep this list zero-hallucination:

- **WaveNet** (van den Oord et al.) — an arXiv/DeepMind technical report, **not** an ICASSP paper.
- **Tacotron** and **SpecAugment** — **Interspeech**, not ICASSP; do not cite as ICASSP.
- **Conv-TasNet** (Luo & Mesgarani) — the canonical version is **IEEE/ACM TASLP** (a journal),
  not the ICASSP proceedings; verify which artifact you mean.
- **wav2vec / wav2vec 2.0** — Interspeech / NeurIPS, not ICASSP.

Before adding any new row, confirm the edition on dblp `conf/icassp/<key>` (the proceedings page
names the ICASSP year), record authors, year, and DOI, and update the access-date header. When in
doubt, omit. If web search is unavailable, add the row as **待核实 / TO VERIFY** with **no
attribution**.
