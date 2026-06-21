---
name: amanthro-data-analysis
description: Use when executing and reporting the analysis/interpretation for an American Anthropologist (AA) manuscript so it survives expert anonymous review — disciplined ethnographic/qualitative inference, honest interpretation, and (for biological/archaeological work) sound quantitative analysis. Guides analysis and interpretation norms; it does not fabricate evidence or quotations.
---

# Analysis & Interpretation (amanthro-data-analysis)

AA reviewers are expert and read across four fields, so the same results section may be read by an
ethnographer, an archaeologist, and a bioanthropologist at once. At AA, **interpretation is analysis**:
qualitative inference is held to a real standard, not waved through as "context." This skill covers
execution and reporting norms; design decisions live in `amanthro-research-design`.

## When to trigger

- Building the results/interpretation section from fieldnotes, transcripts, material, or measurements
- A reviewer asked for more evidence, alternative readings, or robustness
- Reconciling what interlocutors say with what they do, or pre-planned vs. emergent themes
- Making the analysis transparent enough to be credible without exposing protected sources

## Analysis & interpretation norms AA expects

1. **Show the evidence behind the claim.** Ground each interpretive claim in specific, quoted, or
   described evidence (a fieldnote moment, an utterance, an artifact, a measurement) — not assertion.
2. **Pursue the alternative reading.** Name the strongest rival interpretation and show why the
   evidence favors yours; report where it doesn't fit cleanly. AA values honesty about ambiguity.
3. **Disconfirming evidence.** Include cases that complicate the argument rather than curating only
   confirming material; say what you learned from the friction.
4. **Quote and represent fairly.** Translate and contextualize interlocutors' words; do not flatten
   them into illustrations of your theory. Attribute analytics to communities where they originate.
5. **For quantitative subfields** (biological/archaeological): report effect sizes and uncertainty, not
   just significance; pre-specify where possible; correct for multiple comparisons; validate measures;
   avoid conflating ancestry with social race.
6. **Reflexivity in the analysis.** Note how your position shaped which evidence was available and how
   you read it.

## Mixed-methods / computational specifics
- If you code text or use computational tools on field/archival data, document the procedure, validate
  against close reading, and treat outputs as interpretable evidence, not ground truth.
- Keep the qualitative core legible: a table or model never replaces the interpretive argument at AA.

## AA four-field evidence-and-care ledger

Before writing the results section, build an AA ledger that shows how the analysis earns trust across
anonymous four-field review while protecting the people, places, materials, and communities that make
the evidence possible.

| Claim type | Evidence burden | AA-specific check |
|------------|-----------------|-------------------|
| Ethnographic interpretation | fieldnote moment, situated quote, practice, or interaction | alternative reading named; interlocutor dignity preserved |
| Archaeological/material claim | artifact/context record, stratigraphy, archive, or material trace | source limits and silences stated, not hidden |
| Biological/quantitative claim | measure validity, uncertainty, comparison set, effect size | ancestry, population, and social categories not conflated |
| Linguistic/semiotic claim | transcript, translation, interactional sequence, or form-function link | transcript supports the indexical/social claim |
| Public or multimodal claim | image, sound, exhibit, media artifact, or public-facing evidence | consent, caption, and analytic function are explicit |
| Community/accountability claim | collaborative interpretation, feedback, or provenance trail | analytics attributed; extractive phrasing removed |

Use the ledger to decide what can be shown in the manuscript, what belongs in protected notes, and what
must remain undisclosed for ethical reasons. The goal is not maximal transparency; it is accountable
evidence that an AA reviewer can audit without compromising participants or collections.

## Transparency while you work (not at the end)
- Maintain an audit trail linking claims to sources (evidence tables, coded excerpts) so the argument
  is checkable without de-anonymizing protected interlocutors.
- For quantitative work: set/report seeds, pin software versions, keep exhibit numbers matched to
  outputs (see `amanthro-transparency-and-data`).

## Anti-patterns

- Cherry-picked quotes that illustrate the thesis with no disconfirming cases
- Interpretation asserted with no grounding evidence ("informants felt…")
- Treating qualitative evidence as merely decorative around a "real" quantitative result (or the reverse)
- Stars-only tables with no effect sizes/intervals (biological/archaeological work)
- Extracting community analytics without attribution; speaking *for* rather than *with* interlocutors
- Numbers or quotations the underlying record cannot support

## Output format

```
【Main claim】the interpretive/empirical result
【Evidence】what grounds it (fieldnote / utterance / material / measure)
【Four-field mode】ethnographic / material / biological-quant / linguistic / multimodal / community-accountability
【Alternative reading】named and adjudicated?
【Disconfirming evidence】included and addressed? [Y/N]
【Quant rigor】(if applicable) effect size + uncertainty + validation
【Care check】privacy, consent/provenance, attribution, and dignity protected? [Y/N]
【Reflexivity】position's effect on the analysis noted? [Y/N]
【Next】amanthro-tables-figures
```

## What AA reviewers probe, by mode

| Mode | The check a referee runs first | The fix that earns trust |
|------|--------------------------------|--------------------------|
| Ethnographic / interpretive | Is the claim grounded in shown evidence, or asserted? | Quote/describe the moment; name the rival reading |
| Archival / material | Are the silences and biases of the source read, not ignored? | Read against the grain; state what the archive cannot show |
| Biological / quantitative | Is uncertainty honest and "race" handled carefully? | Effect sizes + intervals; ancestry ≠ social race; validated measures |
| Linguistic | Does the transcript support the indexical claim? | Show the discourse data; tie form to social meaning |
| Multimodal | Does the media *argue*, or merely illustrate? | Make the image/sound carry analytic weight, with consent |

## Calibration anchors (hedged)

- The bar is **anthropological significance with honest interpretation**, not within-subfield novelty
  or statistical decoration; a rich case with a thin argument rarely clears AA review.
- AA practices methodological pluralism and an **ethics of care** — match the inference standard to the
  mode, and never trade interlocutors' dignity for a sharper claim.
- Specific transparency mechanics can change — confirm against the journal's current guidelines.

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — qualitative-analysis, transcription, and quantitative packages
- [`../../resources/exemplars/library.md`](../../resources/exemplars/library.md) — how verified AA papers ground interpretation
