---
name: naacl-experiments
description: Use when designing or auditing the experimental program of a NAACL submission — matching evidence to language-coverage claims, keeping cross-lingual comparisons budget-fair, testing on natively authored rather than translated data where the claim requires it, and reporting variance that survives reviewer probing.
---

# NAACL Experiments

Design experiments backwards from the sentence you want the meta-review to
contain. For NAACL-bound work that sentence almost always has a language
scope in it, so the experimental program's first duty is to make the scope
claim measurable — and its second duty is to make every comparison fair
enough that no single reviewer probe collapses it.

## Match the design to the coverage claim

| Claim you want to make | Minimum design that supports it | Design that fakes it |
|---|---|---|
| "Works for language X" | Natively authored X test data, native-speaker error review | Machine-translated English benchmark relabeled as X |
| "Works across the Americas' languages" | Typologically spread sample (e.g., analytic + agglutinative + polysynthetic) | Three Romance languages standing in for a continent |
| "Robust to dialectal variation" | Variety-labeled eval sets, per-variety breakdown | One standard variety plus vibes |
| "Better than baseline B" | B re-run under equal tuning/compute budget, same prompts regime | B's two-year-old published number |
| "Model-agnostic" | ≥3 model families, sizes reported | Two checkpoints of one family |

Translationese deserves its own line of caution: test sets translated from
English preserve English information structure and topic distribution, so
gains measured on them may be gains at modeling translation artifacts.
Where natively authored data cannot be had, say so and mark the limitation
— do not let the table caption imply nativeness the data lacks.

## Budget-fair comparison rules

- Every system in a table gets the same tuning attempts, the same prompt
  engineering effort, and the same test-set exposure; report the attempt
  counts.
- Separate "our method with our infrastructure" from "baseline as published"
  — mixing the two in one column is the most common fairness foul.
- When a hosted API model is a baseline, record query dates and note that
  the comparison is against a moving target.

## Variance and significance floor

- Report mean and spread over ≥3 seeds (or bootstrap over test items when
  training is deterministic); a caption states which.
- Pair headline comparisons with a significance or effect-size statement
  appropriate to the metric; per-language results additionally need
  per-language n, because a 4-point gain on a 200-item Quechua set and on
  a 20,000-item Spanish set are different objects.
- Small multilingual test sets make single-run deltas noise; if the
  per-language sample is small, aggregate honestly and show the intervals.

## The probes NAACL reviewers run

1. **The scope probe:** claim's language list vs. tables' language list.
2. **The fairness probe:** was the strongest baseline given a real chance?
3. **The contamination probe:** could the eval data sit in pretraining?
   State your screening method even when the answer is "cannot rule out."
4. **The mechanism probe:** does any analysis show *why* the gain occurs
   (error classes, ablations), or only *that* it occurs?
5. **The human-eval probe:** who annotated, in which language variety, paid
   how, agreeing how much?

Design so each probe has a prepared landing spot in the paper.

## Experiment ledger

```text
# One row per run, committed with the code
run_id, task, lang, variety, model@rev, prompt_id, seed,
train_data@hash, test_data@hash, metric, value, gpu_h, date
# Tables in the paper are views over this ledger — nothing enters
# a table that lacks a row, and per-language n comes along free.
```

The ledger sounds bureaucratic until the response window, when "R1 asks for
es-MX vs es-AR breakdown" becomes a ten-minute query instead of a lost
weekend.

## Vignette: a dialect-identification study, probe by probe

Fictional setup: classifying Caribbean vs. Andean vs. Rioplatense Spanish
in social media text, claiming "robust dialect ID across Latin American
varieties."

- **Scope probe:** three varieties do not license "across Latin American
  varieties" — either add Central American and Mexican data or rescope the
  claim to the three tested.
- **Fairness probe:** the strongest baseline is a fine-tuned multilingual
  encoder from a prior paper; it gets re-tuned on this study's training
  data with the same search budget, and both budgets appear in a footnote.
- **Contamination probe:** the test tweets postdate every evaluated
  model's training cutoff where cutoffs are published; where they are not,
  the caption says so.
- **Mechanism probe:** a confusion analysis shows the Caribbean-Andean
  errors concentrate in short, lexically neutral posts — evidence the
  model reads topic and orthography, not dialect, in those cases.
- **Human-eval probe:** variety labels came from annotator self-identified
  L1 region plus a validation round; agreement and the adjudication rule
  are reported next to the label counts.

The vignette's lesson: every probe answer becomes a sentence or a caption
*in the paper*, not a private reassurance.

## Audit sequence

1. Write the target meta-review sentence; extract its claims.
2. Map each claim to the table/figure that carries it; kill or downscope
   orphans.
3. Run the five probes adversarially against your own draft.
4. Check every comparison for budget fairness; annotate exceptions.
5. Verify variance reporting exists for every number bolded anywhere.

## Output format

```text
[Target sentence] <the meta-review sentence>
[Claim -> evidence map] <claim: table/figure/analysis>
[Probe results] scope / fairness / contamination / mechanism / human-eval
[Variance status] <where missing>
[Next decisive run] <one experiment, why it changes the decision>
```
