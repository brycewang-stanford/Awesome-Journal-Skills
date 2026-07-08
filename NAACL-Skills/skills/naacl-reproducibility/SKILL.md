---
name: naacl-reproducibility
description: Use when hardening the reproducibility story of a NAACL submission — treating the Responsible NLP checklist as a binding contract, pinning model versions and API access dates, making multilingual evaluation re-runnable, and stating an honest release level instead of an aspirational one.
---

# NAACL Reproducibility

Reproducibility at NAACL is enforced through a document, not a badge: the
Responsible NLP checklist travels with the submission, reviewers read it
against the paper, and answers contradicted by the PDF are grounds for
rejection without review under current ARR policy. The working stance:
every checklist answer is a claim you are prepared to defend in the author
response.

## The contract reading of the checklist

- Answer from what the paper *contains*, never from what the repo will
  eventually contain.
- "No" with a reason is a safe answer; an unsupported "Yes" is a trap you
  set for yourself.
- Point each answer at a location — section, table, appendix — so a reviewer
  verifying it lands somewhere specific.
- Recheck the answers after every major revision; checklists rot faster
  than papers.

## What must be pinned for NLP results in 2026

| Moving part | Pin it as | Why it decays |
|---|---|---|
| Hosted LLM APIs | Model identifier + query date range | Providers swap weights behind stable names |
| Open-weights models | Exact checkpoint hash or revision tag | "Latest" changes under you |
| Decoding | Temperature, top-p, max tokens, seed policy, n samples | Unstated sampling makes numbers unrepeatable |
| Prompts | Verbatim strings, all variants, selection rule | "We used a standard prompt" reproduces nothing |
| Tokenizers / normalization | Version + Unicode normalization form | Silent retokenization shifts multilingual scores |
| Eval metrics | Implementation + version (not just the metric name) | Scorer variants disagree by whole points |
| Data splits | Published split files or generation script + seed | Ad-hoc splits are unrecoverable |

## Multilingual runs: the NAACL-flavored decay modes

Papers committed to NAACL disproportionately evaluate across languages, and
multilingual pipelines decay in language-specific ways: normalization that
strips combining diacritics, sentence splitters that fail on Spanish
inverted punctuation, tokenizers that fragment agglutinative morphology
(Nahuatl, Quechua, Guaraní), and translation-based baselines whose MT system
version was never recorded. Log per-language preprocessing explicitly — a
single global "we lowercase and tokenize" line hides exactly the steps that
differ across the languages you claim to cover.

## A reproducibility manifest worth shipping

```yaml
# repro-manifest.yml — include in the supplement
models:
  - id: example-lm-7b, revision: a1b2c3d, dtype: bf16
  - id: hosted-model-x, api_dates: 2026-05-02..2026-05-19
decoding: {temperature: 0.0, max_tokens: 512, samples: 1}
prompts: prompts/  # verbatim, one file per task x language
data:
  - name: task_es, split_files: splits/es/, license: CC-BY-4.0
  - name: task_gn, split_files: splits/gn/, license: community-terms
scoring: eval/score.py  (chrF++ via sacrebleu 2.4.x, signature logged)
hardware: 4x A100-80GB, ~310 GPU-hours total
seeds: [13, 42, 2026]  # every table reports mean/sd over these
known_gaps: human eval not re-runnable; transcripts included
```

The `known_gaps` line is the point: an honest boundary between re-runnable
and merely documented is what distinguishes a defensible checklist from a
hopeful one.

## Where the investment pays: the response window

Reproducibility rigor is usually sold as ethics; at NAACL it is also
tactics. When a reviewer asks "would the result hold with a different
prompt phrasing?" a team with a pinned manifest and an experiment ledger
answers inside the window with numbers; a team without one answers with
adjectives. Concretely, the manifest converts three recurring review
moments:

1. A contamination worry becomes a lookup ("test items postdate the
   pinned revision's training cutoff") instead of a speculation.
2. A "results seem fragile" score becomes challengeable with the seed
   spread already computed per table.
3. A camera-ready promise becomes credible because the reviewer can see
   the infrastructure that would fulfill it.

Meta-reviews reward the second answer pattern visibly; the checklist is
read as a proxy for whether the authors could defend any number under
pressure.

## Release levels, stated plainly

1. **Re-runnable** — scripts + outputs + splits; a stranger reproduces the
   tables from the archive.
2. **Verifiable** — outputs and scoring included; generation requires
   resources or access the reader may lack.
3. **Documented** — full protocol description; execution not possible
   (private data, community-restricted corpora, retired APIs).

Name the level in the paper. NAACL reviewers penalize mismatch between
claimed and actual level far more than they penalize level 3 honestly held —
especially when community data-governance terms, common in Americas-language
work, are the stated reason.

## Output format

```text
[Checklist audit] <answer -> evidence location -> holds/contradicted>
[Pin table status] <each moving part -> pinned/missing>
[Per-language gaps] <language -> unlogged preprocessing or scorer>
[Release level] re-runnable / verifiable / documented (+ reason)
[Fixes before upload] <ordered>
```
