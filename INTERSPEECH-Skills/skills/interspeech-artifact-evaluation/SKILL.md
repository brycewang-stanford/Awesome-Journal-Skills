---
name: interspeech-artifact-evaluation
description: Use when packaging code, models, and audio artifacts for an INTERSPEECH paper — anonymous demo pages and sample audio during double-blind review, public release at camera-ready, checkpoint and recipe distribution, voice-data licensing and speaker-consent hygiene, and the ethics of releasing synthesis or cloning systems.
---

# INTERSPEECH Artifact Evaluation

Interspeech has no badge-granting artifact committee; the artifact culture is
community-enforced instead. Reviewers listen to your samples, and post-publication
readers judge the paper by whether the recipe reproduces. This skill treats
artifacts in the two states an Interspeech cycle forces: **anonymous during review,
permanent after acceptance**. Check the current author instructions for what may be
attached versus linked — attachment rules vary by cycle.

## The speech-specific artifact set

| Artifact | Review-time form | Post-acceptance form |
|---|---|---|
| Audio samples (TTS/VC/enhancement) | Anonymous static demo page or attached files | Permanent samples page linked in camera-ready |
| Code + training recipe | Anonymized repo (no usernames in history/CI) | Public repo, tagged at the paper's commit |
| Model checkpoints | Usually withheld (size, identity risk) | Hosted release with license and card |
| Data/corpus contribution | Described + license stated in paper | Archived with DOI, documented splits |
| Scoring/protocol scripts | In the anonymized repo | In the public repo — the piece most reused |

## Anonymous demo pages without leaks

Audio demos are where Interspeech anonymity dies. Before the deadline, sweep:

- Hosting identity: GitHub Pages under a personal account, university subdomains,
  and cloud buckets named after the lab all deanonymize. Use a fresh neutral host.
- Page furniture: analytics IDs, favicon, footer credits, CNAME records.
- The audio itself: a distinctive proprietary voice can identify the lab as surely
  as a name — consider whether samples themselves are identifying.
- File metadata: WAV/MP3 tags, encoder strings, creation paths.
- Immutability: do not edit the page during review; a changing page suggests
  post-deadline work and can carry timestamps.

## Voice data is personal data

Speech artifacts carry legal and ethical weight that generic ML artifacts do not:

- **Corpus licenses bind derivatives.** VoxCeleb-trained speaker models, LDC-derived
  lexicons, and YouTube-scraped audio each constrain what you may redistribute.
  State, in the paper, the license of every corpus used.
- **Speaker consent** governs sample release: a cloned or converted voice needs the
  source speaker's permission to be published, even "just for the demo page."
- **Cloning/spoofing dual use**: for synthesis and voice-conversion systems, say
  what you release (recipe? checkpoint? nothing beyond samples?) and why. The
  community norm — visible in anti-spoofing challenges like ASVspoof — is to weigh
  release against misuse and to say so explicitly.
- Do not ship raw audio of human subjects unless its license explicitly allows
  redistribution; ship feature extraction from the official corpus instead.

## Minimum viable recipe

A speech result is reproducible when a stranger can regenerate the *number*, not
just run the model. Package for the number:

```text
release/
├── README.md          # env, corpus versions + licenses, one command per table row
├── recipe/            # data prep → training → decoding, in run order
├── conf/              # exact configs/hyperparameters used in the paper
├── scoring/           # the WER/EER/MOS-analysis scripts and text-norm rules
├── RESULTS.md         # expected outputs with tolerances (seeds, CI width)
└── LICENSE            # code license + data-license pointers
```

The `scoring/` directory matters most at this venue: WER moves with text
normalization and EER with trial lists, so publish the measurement, not only the
model (see `interspeech-reproducibility`).

## Timing across the cycle

- **Before submission**: anonymous demo page frozen; repo anonymized if linked.
- **During review**: touch nothing linked from the paper.
- **At camera-ready** (19 June in the 2026 cycle): flip links to permanent public
  homes; tag the repo; add the paper's ISCA Archive DOI to the README.
- **Conference week**: QR to samples on the poster; the demo page is your talk's
  safety net when room audio fails.

## Leak patterns seen in the wild

Concrete ways speech artifacts have deanonymized their authors — sweep for each:

- A demo page hosted at `<university>.github.io/<lab-project>/` linked straight
  from the anonymous PDF.
- Git history in a "fresh" anonymized repo carrying the original committer
  emails (`git log --format='%ae' | sort -u` before sharing).
- WAV files whose RIFF metadata names the workstation user; MP3 ID3 tags naming
  the recording engineer.
- A samples page reusing the lab's distinctive in-house TTS voice from previous
  published demos — recognizable by ear.
- Cloud-bucket URLs containing the grant acronym.
- Analytics or font-loader scripts on the demo page tying it to the lab's other
  properties.

## Checkpoint release decision aid

| Situation | Community-normal release |
|---|---|
| ASR/SSL encoder on licensed-but-public corpora | Recipe + checkpoint |
| Speaker-verification model on VoxCeleb-family data | Recipe + checkpoint, license noted |
| TTS/VC on a consenting or synthetic voice | Recipe + checkpoint + samples |
| TTS/VC cloning a real speaker without release rights | Recipe + samples only; no checkpoint |
| Anything trained on scraped, unlicensed audio | Describe honestly; release nothing derived |

## Output format

```text
[Artifact inventory] samples / code / checkpoints / data / scoring — state of each
[Anonymity sweep] host, page, metadata, voice-identifiability findings
[License chain] corpus licenses → what may be redistributed
[Consent/dual-use] speaker permission status; release decision + rationale
[Release plan] what flips public at camera-ready, where it lives permanently
[Gaps] <ordered fixes>
```

Attachment size limits, link policies, and any new artifact requirements are
cycle-volatile — verify on the current author pages (2026 sources logged in
`resources/official-source-map.md`, checked 2026-07-08).
