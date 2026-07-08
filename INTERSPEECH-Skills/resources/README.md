# INTERSPEECH Resources

Working materials behind the skill pack. The `skills/` directory tells an agent
*what to do* at each stage of an Interspeech cycle; this directory holds the
evidence layer — verified sources, real exemplar papers, a worked style example,
and the reproducibility tooling adapter.

## Contents

| Resource | Purpose |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Ten verified official sources with URLs and access dates, the 2026 (Sydney) fact base, the reported-only list, and everything marked 待核实 — plus the gateway access-method note. |
| [`external_tools.md`](external_tools.md) | Live official surfaces (conference site, ISCA, Archive, portal) and five author-side verification passes. |
| [`exemplars/library.md`](exemplars/library.md) | Five Interspeech papers verified against the ISCA Archive (title, pages, DOI), one per task lane, with self-check questions and a venue-misattribution guard. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | A fictional streaming-ASR abstract and introduction rewritten from NLP-flavored draft into the Interspeech one-pass shape. |
| [`code/README.md`](code/README.md) | Adapter to the shared ML-conference reproducibility kit plus the five speech-specific checks (scoring rulers, trial lists, audio metadata, licenses, MOS protocols). |

## Boundary note

This is a speech-conference pack. Do not import the econometrics code kits used by
the journal packs in this repository, and do not treat NLP-venue conventions
(appendices, unlimited supplements, ARR-style rolling review) as if they applied
here — Interspeech's 4-page format and ISCA Archive pipeline are their own world.

## A sensible route through the material

1. **Fit first** — [`../skills/interspeech-topic-selection`](../skills/interspeech-topic-selection/SKILL.md)
   plus a skim of [`exemplars/library.md`](exemplars/library.md) to calibrate what
   accepted work looks like per task lane.
2. **Build the evidence** — [`../skills/interspeech-experiments`](../skills/interspeech-experiments/SKILL.md)
   and [`../skills/interspeech-reproducibility`](../skills/interspeech-reproducibility/SKILL.md),
   with [`code/README.md`](code/README.md) as the packaging checklist.
3. **Write to the form** — [`../skills/interspeech-writing-style`](../skills/interspeech-writing-style/SKILL.md)
   against the before/after in [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
4. **Verify the cycle** — [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before anything deadline-shaped, since
   every date in this pack is a 2026 snapshot.
