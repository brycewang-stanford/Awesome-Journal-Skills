---
name: eacl-experiments
description: Use when designing or auditing the empirical evidence for an EACL paper, covering tuned and LLM baselines, multilingual breadth matched to the claim, significance and variance floors, human-evaluation agreement, data-contamination controls, ablations, and error taxonomies, so that every stated result is measured rather than asserted.
---

# EACL Experiments

Use this to make an EACL paper's evidence hold up under NLP review. EACL rewards **well-scoped
questions answered with careful controls** over leaderboard maximalism — its best papers include
analyses and critiques, not only state-of-the-art systems (see
`../../resources/exemplars/library.md`). Design the evidence to match the claim exactly, no
broader.

## Baselines that make a comparison fair

- Include a **tuned** baseline, not a strawman: an under-tuned competitor makes a win
  meaningless. State the search space for both your method and the baselines.
- For LLM-based work, include the **obvious prompt/few-shot baseline** and report its prompts and
  decoding settings; a gain over an unreported baseline is not credible.

## Match breadth to the claim

| Claim | Required breadth |
|---|---|
| "Works for language L" | Solid results on L, honestly scoped |
| "Cross-lingual / multilingual" | Enough languages across resource levels; per-language results |
| "General method" | Multiple tasks/datasets, not one convenient benchmark |
| "Robust" | Stress tests / shifts, not just in-distribution |

A multilingual claim backed by two high-resource languages is the classic EACL over-reach — the
morphology-across-57-languages exemplar shows the bar.

## Significance and variance floor

```text
Evidence floor for a headline comparison:
  seeds:        >= 3-5 runs
  report:       mean +/- CI (or std), never a lone run
  significance: a test when systems are close
  ablations:    isolate each component's contribution
```

## Contamination controls

- For any benchmark evaluated with LLMs, **address whether the test data could have leaked**.
  Report an overlap/decontamination check where feasible, or bound the risk honestly for
  closed models. This is a live EACL concern, not a formality.

## Human evaluation done properly

- If human judgments are a result, report the **number of annotators, guidelines, pay, and
  inter-annotator agreement** — an unmeasured human eval is a soft target for reviewers.
- Release the annotation materials (see `eacl-artifact-evaluation`).

## Error analysis as a first-class result

- A **quantified error taxonomy** ("X% agreement errors, Y% named-entity errors, examples in
  Table N") often carries more scientific weight than another decimal of accuracy, and plays to
  EACL's analysis-friendly reviewing.

## Audit checklist

```text
[ ] Baselines tuned, search spaces stated
[ ] LLM baselines with verbatim prompts + decoding
[ ] Breadth matches the claim (per-language results if multilingual)
[ ] >= 3-5 seeds; variance/CIs reported
[ ] Significance test where systems are close
[ ] Ablations isolate each component
[ ] Contamination addressed
[ ] Human eval: annotators, agreement, pay reported
[ ] Error analysis quantified
```

## Output format

```text
[Evidence strength] Strong / Adequate / Weak
[Baseline fairness] <tuned? LLM baseline reported?>
[Breadth vs claim] <matched / over-reaching>
[Variance + significance] <seeds, CIs, tests>
[Contamination + human eval] <controls present?>
[Fix order] <experiments to add/scope before the cycle deadline>
```
