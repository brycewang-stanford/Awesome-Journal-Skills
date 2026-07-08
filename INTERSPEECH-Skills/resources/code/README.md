# INTERSPEECH Reproducibility Code Adapter

This directory routes Interspeech authors to the repo-level ML conference
reproducibility kit and lists the speech-specific checks that generic tooling
cannot perform. It is deliberately not an econometrics kit and not a speech
toolkit — recipes belong in ESPnet/SpeechBrain/Kaldi-style projects, not here.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Smoke-check an anonymous release package

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/anonymous-release
```

Treat a pass as necessary, never sufficient.

## Speech checks the generic kit does not make

The kit verifies package *structure*; an Interspeech reviewer verifies the
*measurement*. Audit these by hand against
[`../../skills/interspeech-reproducibility/SKILL.md`](../../skills/interspeech-reproducibility/SKILL.md):

1. **Scoring ruler shipped** — text-normalization rules and scorer configuration
   (the things WER silently depends on) are in the package, not just the model.
2. **Trial lists and splits** — speaker-verification trial files and any custom
   partition manifests included or exactly cited.
3. **Audio metadata scrubbed** — WAV/MP3 tags, encoder strings, and hosting
   identity on demo pages, per
   [`../../skills/interspeech-artifact-evaluation/SKILL.md`](../../skills/interspeech-artifact-evaluation/SKILL.md).
4. **Corpus license chain** — every corpus named with its license; nothing
   redistributed that the license forbids; speaker-consent status for any released
   synthetic voices.
5. **Subjective-test protocol** — MOS/CMOS rater counts, instructions, and CI
   method recorded alongside the scores they produced.

Venue policy always comes from the live official pages
([`../official-source-map.md`](../official-source-map.md) records the 2026 trail),
never from this adapter.
