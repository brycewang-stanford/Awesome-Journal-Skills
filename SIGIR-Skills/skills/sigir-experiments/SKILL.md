---
name: sigir-experiments
description: Use when designing or auditing the empirical program of a SIGIR paper — choosing test collections that match the claim, metric-cutoff discipline, paired significance testing with multiple-comparison correction, baseline tuning symmetry, ablations that isolate mechanisms, efficiency reporting, and LLM-era evaluation pitfalls.
---

# SIGIR Experiments

SIGIR inherits its experimental culture from the Cranfield/TREC tradition: shared
test collections, pooled relevance judgments, and statistical comparison of systems.
Reviewers audit the *protocol* before they admire the numbers. This skill designs an
evidence program that survives that audit — and flags the LLM-era failure modes that
current program committees have learned to probe.

## Claim → collection matching

The collection lineup is an argument about the claim's scope:

| Claim type | Minimum credible lineup | Watch out for |
|---|---|---|
| Ad-hoc passage/document ranking | MS MARCO dev + TREC DL (multiple years) | Shallow-judgment bias on MARCO; report judged@k on DL |
| Zero-shot / generalization | A BEIR-style multi-collection suite | Cherry-picking subsets; state the full suite or the selection rule |
| Domain-specific retrieval | The domain's standard collection + one general control | Claiming generality from the domain alone |
| Recommendation | ≥2 public interaction datasets with standard splits | Nonstandard splits that break comparability |
| Efficiency | Same quality collections + a latency/memory protocol | Quality-only baselines at different operating points |
| New task / evaluation method | A purpose-built collection with documented judgments | See `sigir-artifact-evaluation` for judgment standards |

Rule: every collection has known ceiling effects and judgment quirks; one sentence
acknowledging the relevant quirk ("MARCO's sparse judgments penalize novel-document
retrieval; we therefore also report ...") converts a vulnerability into credibility.

## Metrics and cutoffs

- Pre-commit to metrics that match the task stage: recall-oriented (R@1000) for
  first-stage retrieval, precision-oriented (nDCG@10, RR@10) for re-ranking and
  user-facing quality, and report both when the pipeline has both stages.
- Fix cutoffs before running; a paper whose cutoff varies by table row is assumed
  to have shopped.
- Compute every system's metrics with the same tool and flags; cross-paper metric
  implementations differ measurably (see `sigir-reproducibility`).

## Significance testing: the house protocol

The community default is the **paired test on per-topic scores** with correction
for multiple comparisons. A defensible standard setup:

```python
# per-topic paired comparison, the SIGIR-standard shape
import ir_measures, scipy.stats as st
ours  = per_topic_scores("runs/ours.trec",  qrels, "nDCG@10")
base  = per_topic_scores("runs/base.trec", qrels, "nDCG@10")
t, p = st.ttest_rel(ours, base)            # paired t-test across topics
# correct across the family of comparisons you actually report:
# Bonferroni/Holm over {baselines} x {collections} x {metrics}
```

- Report the test name, correction, alpha, and n (topics) in the caption.
- Randomization/permutation tests are equally accepted; Wilcoxon is common; what is
  not accepted is *no* test under close deltas.
- Neural systems: ≥3 seeds, mean ± sd; significance on the per-topic means, and say
  which seed's run files ship in the repository.
- Effect size beats star-counting: a 0.3-point significant gain on a 700-topic
  collection is publishable as *analysis*, not as a "substantial improvement."

## Baseline fairness — the objection that kills

The most common fatal review at SIGIR is some form of "the baselines were not given
the same care." Inoculation checklist:

- Equal tuning budget per system, documented (search space, trials, dev split).
- Baselines at current strength: a tuned BM25 (k1/b swept), the strongest published
  configuration of each neural baseline, and at least one recent (last ~2 SIGIR/ECIR
  cycles) system in the family you claim to beat.
- Never mix copied numbers with computed numbers in one table silently; if you must
  quote a published number, mark it and explain the setup match.
- Same first-stage candidates, same re-ranking depth, same truncation for everyone.

## Ablations and analysis

- One ablation per named mechanism: remove/replace it and show the delta on the
  headline metric — "the gain comes from X" needs the X-less row.
- Per-query analysis: win/loss buckets against the best baseline, with one diagnosed
  pattern (query type, length, term rarity) rather than anecdote screenshots.
- Sensitivity: the hyperparameter the method is most proud of gets a sweep plot.

## Pre-registration worksheet (internal, one page, before running)

Freezing these six answers before the first run prevents the shopping patterns
reviewers detect:

1. Primary claim, one sentence, with its scope qualifier.
2. Collections and why each is load-bearing for that scope.
3. Metrics + cutoffs (primary vs secondary, pre-committed).
4. Baseline set + per-system tuning budget.
5. The significance test, correction family, and alpha.
6. The ablation matrix: mechanism → isolating row.

Deviations during the project are fine — logged deviations are method; silent ones
are p-hacking with extra steps.

## LLM-era pitfalls reviewers now probe

- **Contamination**: models trained on the web have seen MARCO/BEIR text; say what
  you can about training-data overlap, and prefer post-cutoff or held-out topics
  where the claim depends on unseen data.
- **LLM-as-judge**: if you evaluate with an LLM assessor, validate it against human
  judgments on a subsample and report agreement; unvalidated LLM judgments as sole
  evidence are a growing desk-level concern.
- **Prompt sensitivity**: report the prompt, temperature, and n-trials for any
  generative component; single-shot generative numbers without variance are the new
  single-seed problem.
- **API drift**: name model versions and dates; "GPT-4" is not a reproducible system
  identifier.

## Output format

```text
[Claim-collection match] lineup adequate for claimed scope y/n; quirks acknowledged y/n
[Metric discipline] task-stage match / fixed cutoffs / single tool: pass each
[Statistics] test + correction + n named / seeds >=3 / effect size discussed
[Baseline fairness] tuning symmetry / current-strength set / no silent copied numbers
[Ablation coverage] mechanisms with isolating rows: <k>/<n>
[LLM-era risks] contamination / judge-validation / prompt-variance / version-pinning
[Weakest link] <the single protocol element a hostile reviewer attacks first>
```
