---
name: colm-experiments
description: Use when designing or auditing the empirical core of a COLM paper — contamination analysis for evaluation data, fair baselines under matched prompting and compute, pinned model versions and decoding parameters, uncertainty over runs and samples, scaling coverage, and honest reporting of API-model comparisons.
---

# COLM Experiments

COLM's reviewer pool works on language models daily, which changes what "rigorous"
means: the failure modes they hunt are not missing error bars alone but the
LM-specific ones — leaked test sets, un-tuned baselines, drifting API models, and
decoding settings that quietly decide the result. Build the evaluation so those four
attacks fail.

## The four LM-specific attacks on your results

**1. Contamination.** Any public benchmark plausibly overlaps the pre-training data
of any recent model. For each evaluation set, either (a) run and report an overlap
analysis against known corpora, (b) use dated or freshly generated items and say so,
or (c) state explicitly that contamination could not be assessed and bound what it
could explain. Silence is the only unacceptable option — and a contamination
paragraph placed *by the results*, not buried in an appendix, defuses the rebuttal
question before it is asked.

**2. Baseline fairness.** "Our method beats the baseline" means nothing if the
baseline got one prompt attempt and your method got fifty. Matched budgets are the
rule: same prompt-engineering effort, same number of few-shot exemplars, same
decoding search, same token budget. Log the effort spent tuning *each* system; the
appendix table of "prompts tried per method" is disarming in review.

**3. Version drift.** Closed models change behind stable-looking names. Pin every
API model with its full version string *and query dates*; pin every open model with
a checkpoint revision hash; pin the evaluation harness commit, because scoring
implementations drift too. A result on an unpinned model is a rumor.

**4. Decoding sensitivity.** Temperature, top-p, max tokens, stop sequences, and the
system prompt are experimental variables. Report them per experiment, and when the
headline claim is close, show it holds under at least one alternative decoding
configuration.

## Uncertainty that matches the noise source

LM evaluations have several distinct randomness sources; report the one that
actually varies in your setup:

| Noise source | When it applies | Report |
|---|---|---|
| Sampling (temperature > 0) | Any stochastic decoding | n samples per item, mean ± CI |
| Training seed | You trained/fine-tuned the model | ≥ 3 seeds where budget allows; else say why not |
| Prompt phrasing | Any prompted evaluation | Sensitivity over ≥ 3 paraphrases for headline numbers |
| Few-shot exemplar choice | In-context learning | Resampled exemplar sets |
| Data ordering / split | Custom splits | Multiple splits or a fixed public split, justified |

Greedy decoding does not make results deterministic across API replicas or hardware;
say what you observed, not what the temperature parameter promises.

## One config per number

Every reported number should trace to a frozen config. A reviewer (or you, during
the May rebuttal) must be able to regenerate any cell:

```yaml
# eval/run-042.yaml — one file per reported table cell group
model:
  name: <open-model-id>
  revision: <checkpoint-hash>        # or: api_version + query_date range
tokenizer_revision: <hash>
harness: {repo: <anonymized>, commit: <sha>}
prompt_file: prompts/task-a/v3.txt   # verbatim, including system prompt
decoding: {temperature: 0.0, top_p: 1.0, max_tokens: 512, stop: ["\n\n"]}
n_samples_per_item: 5
seeds: [13, 41, 97]
compute_log: logs/run-042.cost      # GPU-hours or API spend
```

## Compute disclosure

Report the compute for training *and* evaluation: GPU type and hours for open
models, API spend or token counts for closed ones, plus the total including failed
runs if it changes the picture materially. COLM's community treats compute as part
of the claim — a method that wins by 1 point at 40× evaluation cost is a different
result — and disclosure is what makes the follow-up work possible for smaller labs.

## Scaling and coverage

- If you claim a phenomenon "in LMs," show it across ≥ 2 model families and ≥ 2
  scales, or scope the claim to the models tested.
- If you claim a method helps, include the strongest simple baseline (better
  prompting, more samples, self-consistency) — COLM reviewers reflexively ask
  whether inference-time compute alone reproduces the gain.
- Ablate what your method adds, not what it is built on.

## Human and model-judge evaluation

Two further COLM-relevant rigor points, because so many LM claims rest on judged
outputs rather than exact-match scoring:

- **Model-as-judge is a measurement instrument with its own error.** Report the
  judge model (pinned, like every other model), the judging prompt verbatim, its
  agreement with human raters on a calibration subset, and known judge biases
  (position, length, self-preference) that your protocol controls for. Under the
  2026 COLM policy, LLM-based evaluation is an explicit disclosure category — the
  methodological writeup and the policy disclosure should tell the same story.
- **Human evaluation needs the same design care as a user study**: rater count and
  recruitment, instructions (verbatim, in the appendix), pay, inter-rater
  agreement, and item sampling. "Three of the authors rated outputs" is a
  disclosure, not a protocol — say it plainly if that is what happened.

## Design review checklist

- Contamination story exists for every evaluation set (analysis, dated data, or
  explicit inability statement).
- Budgets matched across systems; tuning effort logged per method.
- Every model, tokenizer, and harness pinned; API query dates recorded.
- Decoding parameters reported per experiment; headline claims checked under one
  alternative config.
- Uncertainty reported for the actual noise source, with n stated.
- Compute disclosed for training and evaluation.
- Claims scoped to tested models/scales unless coverage justifies more.

## Output format

```text
[Evidence verdict] survives the four attacks / vulnerable to: <which>
[Contamination] handled by <analysis / dated data / inability statement> per dataset
[Pinning] models ▢  tokenizers ▢  harness ▢  query-dates ▢
[Uncertainty] <noise source(s)> reported with n = <...>
[Compute] disclosed: <train / eval / both / missing>
[Ordered fixes] <cheapest credibility gain first>
```
