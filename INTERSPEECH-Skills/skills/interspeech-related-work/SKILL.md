---
name: interspeech-related-work
description: Use when positioning an INTERSPEECH paper in the literature — tracing lineage through the ISCA Archive and its DOIs, covering the ICASSP/ASRU/SLT sibling circuit and challenge series, handling the speech-versus-NLP crossover canon, citing corpora properly, and avoiding the venue misattributions speech reviewers notice instantly.
---

# INTERSPEECH Related Work

At Interspeech, related work is compressed into clauses (the 4-page format leaves
no room for a survey), which raises the stakes: the few citations you make signal
whether you know the field's actual genealogy. Speech has a citation culture with
sharp edges — canonical systems, challenge baselines, and corpus papers each have
one correct citation — and reviewers check.

## The five lanes to cover

| Lane | What reviewers look for | Where it lives |
|---|---|---|
| ISCA lineage | The prior Interspeech/ISCA-workshop papers on your exact task | ISCA Archive (isca-archive.org) |
| IEEE sibling circuit | ICASSP/ASRU/SLT versions of the same line | IEEE Xplore |
| Challenge canon | The relevant challenge (CHiME, VoxSRC, ASVspoof, Blizzard, VoicePrivacy…) and its baseline system | challenge sites + ISCA Archive |
| Crossover ML/NLP | The arXiv/NeurIPS/ICML/ACL end of speech-LLM and SSL work | arXiv + those proceedings |
| Corpus & metric papers | The corpus paper for every dataset, the metric paper for every nonstandard metric | mixed venues — cite the true one |

Missing lane 1 is the deadly one: a paper that cites only arXiv preprints while
ignoring two prior Interspeech papers on the same task tells the area chair the
authors never searched the Archive.

## Search the field like a speech researcher

- **ISCA Archive** (www.isca-archive.org) is open access and searchable across all
  Interspeech years plus ISCA workshops — search it by task term before writing a
  single positioning sentence.
- Interspeech papers carry DOIs of the form `10.21437/Interspeech.<year>-<n>`;
  cite the archival version, not the arXiv mirror, when both exist.
- Sweep the last ~3 editions of Interspeech and the last ICASSP for your task —
  the annual+annual rhythm means the state of the art moves twice a year.
- Check the relevant challenge's latest edition; at Interspeech, "the CHiME-8
  baseline" is a shared reference point that locates your numbers instantly.

## Venue attribution: the trap list

Speech's most-cited papers are scattered across venues, and misattributing them is
a credibility wound. Verified anchors (see `resources/exemplars/library.md` for
the checked list):

- Conformer, SpecAugment, ECAPA-TDNN, Tacotron, SUPERB — **Interspeech** papers
  (2020/2019/2020/2017/2021 respectively).
- LibriSpeech and x-vectors — **ICASSP**, not Interspeech.
- wav2vec 2.0 — **NeurIPS**; Whisper — **ICML**; Common Voice — **LREC**.
- HuBERT — a **journal** (TASLP) paper despite its conference-era fame.

When unsure, resolve the DOI before citing the venue. Never trust a BibTeX file
scraped from arXiv for venue fields.

## Positioning under compression

With one paragraph (or less) of space, use the clause pattern per contrast:

```text
Streaming Conformer variants [3,4] reduce latency but hold WER on
test-other above 6%; adapter-based domain methods [5] recover accuracy
but require target-domain text. We keep the streaming constraint of [3]
while removing the text requirement of [5].
```

Each cited item gets a property and a limitation; your contribution is defined as
the complement. Three such sentences outperform a half-page related-work section.

## Self-citation under double-anonymity

- Third person, always: "extending the system of [7]" even when [7] is yours.
- If your prior system is unmistakably identifiable, cite it anyway — omitting the
  obvious predecessor is worse — but do not claim ownership.
- The anonymity period (from one month pre-deadline to decisions, per the 2025/2026
  policy) also constrains *when* your own extended preprint may appear.

## Corpus and tool citation etiquette

- Every dataset gets its paper cited (and license stated — see
  `interspeech-artifact-evaluation`); every toolkit that shaped results (ESPnet,
  Kaldi, SpeechBrain…) gets its citation.
- Metrics with a defining paper (PESQ, STOI, minDCF conventions) are cited on
  first use if any nonstandard choice is made.

## BibTeX hygiene for a speech bibliography

```bibtex
@inproceedings{gulati20_interspeech,
  title     = {Conformer: Convolution-augmented Transformer
               for Speech Recognition},
  author    = {Gulati, Anmol and others},
  booktitle = {Proc. Interspeech 2020},
  pages     = {5036--5040},
  doi       = {10.21437/Interspeech.2020-3015}
}
```

- `booktitle = {Proc. Interspeech <year>}` is the community norm; do not write
  "INTERSPEECH: Annual Conference of..." variants that fragment your reference
  list's style.
- Keep the DOI field — it is how readers reach the Archive from the PDF.
- Purge arXiv `eprint` entries for papers that have archival versions; mixed
  duplicate entries (same paper cited twice via different keys) are a classic
  reference-page space leak under the 4+1 format.
- The references page is capacity-limited too: with roughly 20–30 entries
  fitting comfortably, every citation must be load-bearing. Cut courtesy
  citations before cutting positioning ones.

## Output format

```text
[Lane coverage] ISCA / IEEE-sibling / challenge / crossover / corpus — hit or gap
[Archive sweep] last-3-editions search done? missing prior art found
[Attribution check] venues verified via DOI for all load-bearing citations
[Positioning clauses] each contrast has property + limitation + complement
[Self-citation] third-person compliance; anonymity-period exposure
[Fix list] <ordered>
```

Archive URLs and the anonymity-period wording were checked 2026-07-08
(`resources/official-source-map.md`); challenge editions roll annually — re-sweep
at writing time, not at submission time.
