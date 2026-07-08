---
name: emnlp-experiments
description: Use when designing or auditing the experimental program of an EMNLP paper — baseline fairness and tuning budgets, dataset and language coverage matched to claims, contamination audits for pretrained and API models, significance testing and seed variance, human evaluation protocols, prompt sensitivity, and the error analysis EMNLP reviewers expect.
---

# EMNLP Experiments

Use this while the experimental grid is still cheap to change. EMNLP's reviewing culture
was partly built by papers criticizing NLP's own evaluation habits, so the venue audits
experiments the way a security reviewer audits inputs: assume the design will be probed
for the easiest way to make the headline number lie.

## The five probes reviewers run

1. **Baseline fairness.** Did the comparison systems get the same tuning budget, data,
   and prompt engineering effort as yours? A win over an under-tuned baseline is the
   most common EMNLP soundness objection.
2. **Coverage-claim match.** Do the datasets, domains, and languages span the claim?
   English-only evidence supports English-only sentences.
3. **Contamination.** Could the pretrained or API model have seen the test data? For
   post-2020 NLP this is a default suspicion, not an exotic one.
4. **Variance.** Is the improvement larger than run-to-run noise? Single-run deltas of
   under a point convince no one here.
5. **Mechanism.** Does any experiment isolate *why* the method works, or only that it
   does? Ablations that remove the claimed ingredient are the minimum.

Design the grid so each probe has a prepared answer, and say where in the paper each
answer lives.

## Reporting floor by evidence type

| Evidence type | Minimum reporting at EMNLP | Silent failure it prevents |
|---|---|---|
| Fine-tuned models | seeds, variance, selection criterion, budget | best-of-N passed off as typical |
| API/LLM results | model ID + query dates, decoding params, exact prompts | unreproducible moving-target claims |
| Human evaluation | annotator count, guidelines, agreement, pay, sampling | vibes formatted as a table |
| Dataset creation | collection method, license, agreement, splits | benchmark nobody can audit |
| Significance | test name, units of analysis, correction for multiple comparisons | p-hacking by metric shopping |

## Contamination audit, concretely

For every evaluation set: record its release date against the model's training cutoff;
run n-gram or substring overlap between test instances and any accessible pretraining
or fine-tuning corpora; where training data is closed (API models), state that
directly and, when feasible, add a post-cutoff or perturbed test slice. Report the
audit even when it finds nothing — "we checked" is evidence; silence is a reviewer
question you chose to receive in July instead of answering in May.

## Statistical practice that survives review

- Test at the right unit: sentence-level metrics on the same documents are not
  independent samples; use paired tests over documents or systems-by-item designs.
- Paired bootstrap or approximate randomization are the community's defaults for
  system comparison; report the number of resamples.
- Multiple metrics × multiple datasets × multiple models is a multiple-comparisons
  machine — state how many comparisons the paper makes and correct or temper claims
  accordingly.
- Power matters in the negative direction too: a "no difference" claim from 200 test
  items is an underpowered shrug, not a negative result.

## Prompt sensitivity is an ablation, not an afterthought

Any result mediated by prompts inherits their variance. The minimum grid:

```text
For each headline LLM result:
  - k ≥ 3 semantically equivalent prompt paraphrases  -> report mean ± spread
  - few-shot exemplar reshuffles (if applicable)      -> report order sensitivity
  - decoding: fixed and disclosed (temp, top_p)        -> no silent temperature 0.8
  - exact prompt text                                  -> appendix, verbatim
If the ranking of systems flips across paraphrases, the paper's claim is about
prompts, not systems — and the paper must say so.
```

## Error analysis as an experiment

EMNLP error analysis is a designed study, not a paragraph: sample failures under a
documented scheme (random within strata beats hand-picked), define error categories
with two annotators and report agreement on the categorization itself, then connect
categories to mechanism — which category does the proposed component reduce, and which
does it leave untouched? A good error analysis generates follow-up experiments; a
decorative one generates adjectives.

## Human evaluation, designed like an experiment

When automatic metrics cannot measure the construct (adequacy, coherence, harm), the
human study inherits the full burden of experimental design, and EMNLP reviewers grade
it as one:

- Define the judgment as a question annotators could disagree about *meaningfully* —
  then measure that disagreement (report the agreement statistic and what level you
  consider acceptable for this construct, since chance-corrected agreement on skewed
  labels behaves badly).
- Sample instances for rating by a documented rule; rating each system's outputs on
  different items is a design error, not a shortcut.
- Blind raters to system identity and randomize presentation order; order effects in
  side-by-side preference ratings are large and well known.
- Report rater recruitment, training, compensation, and count — the Responsible NLP
  checklist requires it, and reviewers cross-check the two.
- Analyze ratings with models matching their structure (ordinal, per-rater variance),
  or at minimum report per-item aggregation rules; averaging Likert scales across
  raters and items without comment is the field's most tolerated bad habit, and its
  tolerance is expiring.

## Grid economics under a deadline

When compute or time forces cuts, cut in this order: extra datasets confirming an
already-shown effect first; extra model scales second; never cut the seeds/variance
runs or the contamination audit — they are cheap relative to the review risk they
retire. A smaller grid with variance beats a wider grid of single runs at this venue,
every time.

## Output format

```text
[Probe readiness] <fairness / coverage / contamination / variance / mechanism: ready or gap>
[Reporting-floor gaps] <evidence type -> missing item>
[Statistical plan] <test, unit, corrections, power posture>
[Prompt-sensitivity status] <done / needed / not applicable>
[Error-analysis design] <sampling, categories, agreement, mechanism link>
```
