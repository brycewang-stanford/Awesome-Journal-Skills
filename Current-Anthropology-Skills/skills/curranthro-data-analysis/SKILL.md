---
name: curranthro-data-analysis
description: Use when executing and reporting the analysis/interpretation for a Current Anthropology (CA) manuscript so it survives expert review and the published CA✩ Comments — disciplined ethnographic/qualitative inference, honest interpretation, and (for biological/archaeological work) sound quantitative analysis. Guides analysis and interpretation norms; it does not fabricate evidence or quotations.
---

# Analysis & Interpretation (curranthro-data-analysis)

CA reviewers and commentators are expert and read across every subfield, so the same results may be read
by an ethnographer, an archaeologist, and a bioanthropologist at once — and for a Major Article, their
critiques are **published as signed Comments** beside your paper. At CA, **interpretation is analysis**:
qualitative inference is held to a real standard, not waved through as "context." This skill covers
execution and reporting norms; design decisions live in `curranthro-research-design`.

## When to trigger

- Building the results/interpretation section from fieldnotes, transcripts, material, or measurements
- A reviewer (or anticipated commentator) asked for more evidence, alternative readings, or robustness
- Reconciling what interlocutors say with what they do, or pre-planned vs. emergent themes
- Making the analysis transparent enough to be credible without exposing protected sources

## Analysis & interpretation norms CA expects

1. **Show the evidence behind the claim.** Ground each interpretive claim in specific, quoted, or
   described evidence (a fieldnote moment, an utterance, an artifact, a measurement) — not assertion.
2. **Pursue the alternative reading.** Name the strongest rival interpretation and show why the evidence
   favors yours; report where it doesn't fit cleanly. A Major Article that pre-empts the obvious Comment
   is far stronger when the Comments arrive.
3. **Disconfirming evidence.** Include cases that complicate the argument rather than curating only
   confirming material; say what you learned from the friction.
4. **Quote and represent fairly.** Translate and contextualize interlocutors' words; do not flatten them
   into illustrations of your theory. Attribute analytics to communities where they originate.
5. **For quantitative subfields** (biological/archaeological): report effect sizes and uncertainty, not
   just significance; pre-specify where possible; correct for multiple comparisons; validate measures;
   avoid conflating ancestry with social race.
6. **Reflexivity in the analysis.** Note how your position shaped which evidence was available and how
   you read it.

## Mixed-methods / computational specifics
- If you code text or use computational tools on field/archival data, document the procedure, validate
  against close reading, and treat outputs as interpretable evidence, not ground truth.
- Keep the qualitative core legible: a table or model never replaces the interpretive argument at CA.

## CA comment-facing analysis ledger

For a CA Major Article, treat analysis as something that must survive not only peer review but also the
published conversation around the paper. Build a comment-facing ledger before drafting results.

| Likely commentator position | Claim they will test | Evidence to prepare | Reply posture |
|-----------------------------|----------------------|---------------------|---------------|
| Adjacent subfield expert | Does this travel beyond the focal case/subfield? | boundary cases, comparative anchors, portability limits | clarify scope without retreating from the central claim |
| Method specialist | Does the evidence warrant the interpretation? | audit trail, rival reading, robustness/triangulation | show what each evidence mode can and cannot decide |
| Area or historical specialist | Are local terms, archives, or chronologies flattened? | contextual detail, source limits, translation choices | acknowledge specificity as part of the contribution |
| Theory critic | Is the concept doing explanatory work or merely labeling? | mechanism, genealogy, counterexample | refine the concept's reach |
| Ethics/community critic | Who bears the cost of the claim? | consent/provenance trail, anonymization logic, attribution | protect participants while answering the analytic point |

Distinguish article type: a **Major Article** needs an agenda-setting claim robust enough for signed
Comments and a Reply; a shorter report can make a bounded empirical contribution, but still needs to
state the limits that commentators would otherwise supply for you.

## Transparency while you work (not at the end)
- Maintain an audit trail linking claims to sources (evidence tables, coded excerpts) so the argument is
  checkable without de-anonymizing protected interlocutors.
- For quantitative work: set/report seeds, pin software versions, keep exhibit numbers matched to outputs
  (see `curranthro-transparency-and-data`).

## Anti-patterns

- Cherry-picked quotes that illustrate the thesis with no disconfirming cases
- Interpretation asserted with no grounding evidence ("informants felt…")
- Treating qualitative evidence as merely decorative around a "real" quantitative result (or the reverse)
- Stars-only tables with no effect sizes/intervals (biological/archaeological work)
- Extracting community analytics without attribution; speaking *for* rather than *with* interlocutors
- Numbers or quotations the underlying record cannot support — commentators will check

## Output format

```
【Main claim】the interpretive/empirical result
【Evidence】what grounds it (fieldnote / utterance / material / measure)
【Article posture】Major Article / report-length contribution; comment exposure named?
【Alternative reading】named and adjudicated?
【Disconfirming evidence】included and addressed? [Y/N]
【Anticipated Comments】top 2-3 commentator objections and prepared evidence
【Quant rigor】(if applicable) effect size + uncertainty + validation
【Reflexivity】position's effect on the analysis noted? [Y/N]
【Reply-ready limit】what the Reply can concede without breaking the argument
【Next】curranthro-tables-figures
```

## What CA reviewers and commentators probe, by mode

| Mode | The check a referee/commentator runs first | The fix that earns trust |
|------|---------------------------------------------|--------------------------|
| Ethnographic / interpretive | Is the claim grounded in shown evidence, or asserted? | Quote/describe the moment; name the rival reading |
| Archival / material | Are the silences and biases of the source read, not ignored? | Read against the grain; state what the archive cannot show |
| Biological / quantitative | Is uncertainty honest and "race" handled carefully? | Effect sizes + intervals; ancestry ≠ social race; validated measures |
| Linguistic | Does the transcript support the indexical claim? | Show the discourse data; tie form to social meaning |

## Calibration anchors (hedged)

- The bar is **agenda-setting significance with honest interpretation**, not within-subfield novelty or
  statistical decoration; a rich case with a thin argument rarely clears CA Major-Article review.
- CA practices methodological pluralism — match the inference standard to the mode, and never trade
  interlocutors' dignity for a sharper claim.
- Specific transparency mechanics can change — confirm against the journal's current guidelines.

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — qualitative-analysis, transcription, and quantitative packages
- [`../../resources/exemplars/library.md`](../../resources/exemplars/library.md) — how verified CA papers ground interpretation
