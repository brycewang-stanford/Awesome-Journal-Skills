---
name: interspeech-writing-style
description: Use when writing or compressing an INTERSPEECH paper into its 4 content pages — the abstract-and-index-terms opening, task-first framing for a mixed science/engineering readership, table and figure economy, protocol one-liners that preserve rigor under compression, and the cuts that shrink pages without shrinking claims.
---

# INTERSPEECH Writing Style

Four pages is not a short paper; it is a different literary form. The Interspeech
house style evolved to let a reader — who may be a phonetician, an ASR engineer,
or an area chair skimming forty PDFs — extract task, method, corpus, metric, and
delta in one pass. Everything below serves that one-pass property.

## The opening contract

- **Title**: task and mechanism, in community vocabulary. Searchable in the ISCA
  Archive beats clever.
- **Abstract** (~100–150 words): task → limitation of current practice → your move
  → corpus + metric + headline number → one-clause takeaway. Numbers belong in
  Interspeech abstracts; "significant improvements" without a number reads as
  evasion.
- **Index Terms**: the paper kit's index-terms line is your search surface — pick
  the 3–5 terms your intended reviewers actually use.
- **Introduction** (~0.75 column): no history of deep learning. Name the task in
  sentence one, the gap by sentence three, the contribution list by the end.

## Density moves that buy space honestly

| Move | Before | After |
|---|---|---|
| Protocol one-liner | A paragraph on data prep | "We follow the ESPnet LibriSpeech recipe (commit X) except: …" |
| Diff-based method description | Re-derive the known architecture | "As in Conformer [n], with two changes: …" |
| Table consolidation | Separate tables per test set | One table, sets as column groups, best in bold |
| Citation compression | Three sentences of related work per item | Clause-level positioning: "unlike streaming approaches [4,5], we…" |
| Figure economy | Architecture diagram redrawing the standard | One figure that carries the *finding* (error breakdown, trade-off curve) |

The related-work *section* can shrink to a paragraph if positioning is woven into
the introduction — common and accepted at this venue (see
`interspeech-related-work`).

## Speech-community diction

- Report metrics with their conditions attached: "WER 4.8% on test-other (no LM)",
  "EER 0.92% on Vox1-O", "MOS 4.1 ± 0.08". A bare number is a red flag.
- Use canonical corpus/partition names; do not rename "dev-clean" to "validation".
- Past tense for what you did, present for what the system does, no "novel" as a
  self-description — the reviewer decides novelty.
- Acronyms: expand once, then commit. An Interspeech paper drowning in undefined
  acronyms fails the one-pass property for the scientist half of the audience.
- Claims scale with evidence verbs: "improves" needs a CI; "suggests" tolerates a
  trend; "solves" needs more than four pages of anything.

## The compression order (when you are at 5.5 pages)

1. Cut motivation prose — Interspeech readers arrive pre-motivated.
2. Convert method paragraphs to diffs against cited standards.
3. Merge tables; move per-condition detail into a results sentence.
4. Trim the intro's third rehearsal of the contribution.
5. Only then consider dropping an experiment — and if the paper still does not
   fit, that is a Long Paper or journal signal, not a formatting problem.

Never buy space with template tricks; the PDF checker and the format police are
real (see `interspeech-submission`).

## Micro-example: results sentence, before → after

```text
Before (3 lines):  We evaluate our proposed method on the LibriSpeech
dataset. Our method achieves significant improvements over the baseline.
Results are shown in Table 2, which demonstrates the effectiveness.

After (2 lines):  On LibriSpeech, the proposed front end reduces WER from
5.6% to 4.9% on test-other (Table 2; paired bootstrap p<0.01), with the
largest gains on utterances under 3 s.
```

The after-version is shorter *and* carries corpus, metric, delta, significance,
and an analysis hook.

## A working section budget for 4 pages

| Section | Budget | Job |
|---|---|---|
| Abstract + index terms | 0.15 col | task→move→corpus→metric→delta |
| 1. Introduction | 0.75 col | gap, hypothesis, contribution — no history lesson |
| 2. Relation to prior work | 0.3–0.5 col | clause-level positioning (may merge into 1) |
| 3. Method | 1.2 col | the diff against cited standards, one figure max |
| 4. Experimental setup | 0.6 col | corpus, protocol one-liners, disclosure block |
| 5. Results + analysis | 1.5 col | decisive table, ablation, one error-pattern finding |
| 6. Conclusions | 0.2 col | finding restated, scoped future sentence |

Budgets flex ±30% by paper type (science papers grow §4–5, systems papers §3),
but a draft violating the total by a full column will not compress overnight.

## Bilingual/global audience note

Interspeech's readership is the most linguistically diverse of the major ML-adjacent
venues. Prefer plain constructions, keep sentences under ~25 words, and gloss
language-specific phenomena (tone sandhi, pitch accent) in one clause — reviewers
outside your language's community must still follow the claim.

## Titles: a quick calibration

- Weak: "A Novel Deep Learning Framework for Improved Speech Processing" —
  no task, no mechanism, unsearchable.
- Serviceable: "Prosody-Gated Chunking for Streaming ASR on Spontaneous Speech"
  — task, mechanism, condition, all in Archive-searchable vocabulary.
- Community pattern: many memorable Interspeech titles name the system once
  ("Conformer: …", "SpecAugment: …") and then say plainly what it does; earn
  the name *after* the colon with a descriptive clause, not instead of one.

## Output format

```text
[One-pass check] task/method/corpus/metric/delta extractable from p.1? y/n
[Opening] title, abstract-number, index-terms verdicts
[Density audit] paragraphs convertible to one-liners or diffs
[Diction] bare numbers, undefined acronyms, unverifiable verbs found
[Compression plan] ordered cuts to reach 4 pages without claim loss
[Escalation] fits in 4pp / needs Long Paper / needs journal
```

Format facts (4 content pages + references page; Long Paper track parameters)
follow the 2026 cycle as logged in `resources/official-source-map.md`
(2026-07-08); the paper kit of the current cycle is the sole format authority.
