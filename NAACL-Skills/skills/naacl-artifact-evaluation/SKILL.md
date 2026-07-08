---
name: naacl-artifact-evaluation
description: Use when packaging datasets, models, prompts, or annotation materials for a NAACL-bound submission — building the artifact around the Responsible NLP checklist's artifact questions, documenting provenance and licensing for language data, and handling community-owned or Indigenous-language resources correctly.
---

# NAACL Artifact Evaluation

NAACL has no separate artifact-badging track; artifacts are judged inside
the ARR review itself, through the supplement upload and section B of the
Responsible NLP checklist ("scientific artifacts"). That placement matters:
your artifact documentation is not an optional extra but a set of sworn
answers reviewers cross-examine against the PDF.

## What the artifact must let a reviewer do

- **Trace provenance.** Where did every corpus come from, under what
  license, and does your use match the terms and the creators' intent?
- **Inspect the instrument.** Prompts, annotation guidelines, interface
  screenshots, and pay rates are artifacts too — a human-evaluation claim
  without its instrument is unverifiable.
- **Rerun the cheap parts.** Scoring scripts and metric code should execute
  from the archive alone; nobody will retrain your model, but everybody can
  re-score your outputs if you include them.
- **Audit the data card.** Language varieties, dialect coverage, speaker
  demographics where relevant, known gaps, and intended use.

## Language-data documentation ladder

| Data situation | Minimum documentation for a NAACL reviewer | Extra step |
|---|---|---|
| Standard public benchmark | Version, split, license, citation | Note any known contamination reports |
| Web-scraped text | Collection dates, filtering rules, deduplication, license basis | PII handling statement |
| New annotated corpus | Guidelines, annotator recruitment and pay, agreement scores | Release the guidelines verbatim in the supplement |
| Dialectal / code-switched data | Variety labels and how they were assigned | Native-speaker validation description |
| Indigenous or community-owned language data | Consent and partnership terms, community approval for release | Verify whether public release is permitted *at all* |

The last row is a NAACL signature concern. Work on languages of the Americas
increasingly follows community-controlled data norms: some corpora may be
used but not redistributed, some require named attribution (which conflicts
with anonymous review — use a placeholder and restore at camera-ready), and
some communities set conditions on derived models. "We release everything"
is not automatically the ethical high ground here; the checklist rewards
accuracy about constraints, not maximal openness.

## Anonymous packaging that survives inspection

```text
artifact.zip
├── README.md          # one-screen orientation: what, how, how long
├── data/
│   ├── data_card.md   # provenance, license, varieties, gaps
│   └── samples/       # enough rows to judge quality, not the corpus
├── prompts/           # exact strings, all variants tried
├── eval/
│   ├── score.py       # runs on outputs/ with no network access
│   └── outputs/       # raw model outputs backing the main tables
└── annotation/
    └── guidelines.pdf # the instrument, scrubbed of institution marks
```

Scrub before zipping: repository history, notebook execution metadata,
absolute paths with usernames, license headers naming the lab, and any
consent form carrying institutional letterhead (replace with a redacted
copy; note that the original exists).

## Vignette: a Quechua-Spanish parallel corpus package

A submission introduces a 40k-pair Quechua-Spanish parallel corpus built
with two community organizations, plus MT baselines. The packaging calls
that follow from this skill:

- The corpus itself does **not** ship in the review archive — the
  partnership terms permit research use but defer public release to a
  community decision. The data card states this, and section B of the
  checklist answers "no, with reason" for artifact release.
- What does ship: 200 sample pairs cleared for review purposes, the
  collection protocol, annotator recruitment and payment description, the
  cleaning scripts, and the full MT evaluation pipeline with outputs.
- The consent-form template ships with the letterhead redacted and a note
  that the original is held by the partner organizations.
- The README's first paragraph tells the reviewer exactly which claims the
  archive can and cannot let them verify — pre-empting the "authors refuse
  to release data" misreading with a governance explanation instead.

The result is an artifact that scores as *honest and inspectable* rather
than *incomplete*, which is the realistic best outcome for
community-governed data.

## Cycle-volatile mechanics

Archive size caps, accepted formats, and whether supplements upload as one
file or several are OpenReview-form details that shift between ARR cycles;
read the live submission form before building the final zip, and never
reverse-engineer the limits from a previous cycle's folklore.

## Post-acceptance conversion

At camera-ready, the anonymous bundle becomes the public record: move it to
a persistent host with a DOI or a tagged release, apply the real license,
restore attribution the community partnership requires, and update the
checklist-facing statements in the paper if the release scope changed
between review and publication.

## Output format

```text
[Artifact inventory] <data / code / prompts / guidelines / outputs>
[Checklist B alignment] <each B answer -> where the artifact proves it>
[Provenance gaps] <unlicensed, undocumented, or unclear-consent items>
[Community constraints] <redistribution / attribution / approval terms>
[Anonymity sweep] clean / issues found
[Release plan] <anonymous now -> public form at camera-ready>
```
