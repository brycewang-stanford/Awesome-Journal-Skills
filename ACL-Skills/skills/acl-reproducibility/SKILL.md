---
name: acl-reproducibility
description: Use when strengthening reproducibility evidence for an ACL paper reviewed through ACL Rolling Review, covering the Responsible NLP checklist end to end, hyperparameter and compute reporting, prompt and decoding disclosure for LLM experiments, data contamination auditing, variance across runs, and checklist-to-paper consistency.
---

# ACL Reproducibility

Use this before an ARR deadline and again at camera-ready. At ACL the
reproducibility instrument is the **Responsible NLP checklist**: it is
mandatory, reviewers read it alongside the paper, and ARR policy makes
incorrect or misleading checklist content a desk-rejection ground. Treat it as
a claims audit, not paperwork.

## The checklist as a claims audit

- Section A: a real Limitations discussion and a risks discussion — reviewers
  are told honest limitations must not be penalized, so under-disclosing is
  strictly worse than disclosing.
- Section B: every dataset and model you *used* needs citation, version,
  license, and intended-use consistency (see `acl-artifact-evaluation`).
- Section C: computational experiments — parameters, budget, infrastructure,
  hyperparameter search, and descriptive statistics with error bars.
- Section D: human annotators/participants — instructions, pay, consent,
  ethics-board status, demographics where relevant.
- Section E: AI assistants used in research, coding, or writing.

Every "yes" answer should carry a section/appendix pointer; every "N/A" should
survive a hostile reading of the paper.

## Reporting floor for the modern NLP paper

| Experiment type | Minimum disclosure that survives ACL review |
|---|---|
| Fine-tuned models | Model + version, seeds, LR/schedule, epochs, selection criterion, dev-set use, runs count |
| Prompted LLMs | Exact prompts, decoding params (temperature, top-p, max tokens), model snapshot date/version, n samples |
| API-based closed models | Access dates, version string, cost/queries, caching strategy, note on irreproducibility risk |
| Human evaluation | Instructions, item counts, raters per item, agreement statistic, pay |
| New metrics | Implementation source, correlation evidence, code in supplement |

## Contamination and leakage auditing

- State which evaluation sets could plausibly appear in pretraining corpora
  and what you did about it: n-gram overlap scans, canary checks, dataset
  release date vs model cutoff reasoning.
- For benchmarks you release, record a creation date and content hash so
  future contamination is auditable.
- For claimed generalization, verify the test languages/domains genuinely
  weren't leaked through translation or paraphrase of training data.

## Variance discipline

- Single-run leaderboard deltas are the classic ACL review complaint. Report
  mean and deviation over multiple seeds or prompt paraphrases, and say in the
  caption what the interval is.
- When compute makes many runs impossible, say so, quantify what you could
  (e.g., variance on the smallest model), and scope claims accordingly —
  checklist Section C expects the compute budget stated either way.

## Consistency sweep before submission

1. Grep the paper for every number that a checklist item claims exists
   (error bars, splits, licenses, pay). Missing → fix paper or answer.
2. Check the supplement actually contains what Sections B/C reference.
3. Confirm Limitations mentions the weaknesses your own experiments exposed;
   reviewers notice when the Limitations section dodges the obvious one.
4. Re-answer Section E honestly after the final writing pass — late-stage
   AI-assisted rewriting counts.

## Degrees of reproducibility to declare

```text
turnkey    : one script re-scores released outputs / reruns the pipeline
scripted   : code + configs released; needs GPUs, keys, or gated data
descriptive: enough prose + prompts that a motivated lab could rebuild it
closed     : hinges on private data or deprecated APIs — say so in Limitations
```

Declare the level you actually achieve. At ACL, releasing model *outputs* is
the cheap trick that upgrades many LLM papers from descriptive to turnkey,
because re-scoring needs no compute.

## Prompt-disclosure block that satisfies reviewers

A reusable appendix pattern for each prompted experiment:

```text
Experiment: Table 3, zero-shot NLI
Model: <name + exact version/snapshot + access date>
Decoding: temperature=0.0, top_p=1.0, max_tokens=16
Prompt (verbatim, incl. whitespace):
  "Premise: {premise}\nHypothesis: {hypothesis}\n
   Answer entailment, neutral, or contradiction:"
Paraphrases: 5 variants (App. D.2); reported number = mean over variants
Post-processing: first-token match, case-insensitive; ties -> neutral
Failures: non-parseable outputs counted as errors (2.3% of calls)
```

The last two lines — parsing rules and non-parseable handling — are where
most "we could not reproduce the number" disputes actually originate.

## Cheap wins ranked by effort

1. Release model outputs alongside code (near-zero cost, enables re-scoring).
2. Log and report seeds + run counts in every caption while runs are fresh.
3. Pin dataset versions/commits in the bibliography and README now, not at
   camera-ready when the version has silently moved.
4. Write the compute paragraph (GPUs, hours, total runs incl. failed) the
   week the experiments finish.
5. Save the exact evaluation-script commit used for headline numbers.

## Output format

```text
[Checklist status] consistent / gaps found / contradicts paper
[Section-by-section] <A/B/C/D/E: pass or missing items>
[LLM disclosure] <prompts/decoding/version/date status>
[Contamination stance] <audit done / reasoned / unaddressed>
[Variance reporting] <runs, intervals, caption clarity>
[Fixes] <paper edits vs supplement additions, ordered>
```
