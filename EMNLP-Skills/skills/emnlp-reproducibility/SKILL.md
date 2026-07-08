---
name: emnlp-reproducibility
description: Use when hardening an EMNLP paper's reproducibility record — answering the Responsible NLP checklist truthfully under desk-reject enforcement, pinning model versions and API snapshot dates, logging decoding parameters and prompts, documenting data licensing and annotation, and reporting compute so another lab could rerun the study.
---

# EMNLP Reproducibility

Use this before submission and again before camera-ready. At EMNLP, reproducibility is
not a virtue signal appended to the paper — it is enforced at the gate: the Responsible
NLP checklist is filed with every ARR submission, ARR has desk-rejected for incorrect,
incomplete, or misleading answers since December 2024, and EMNLP 2025 published the
completed checklist as an appendix of the paper itself. Assume your answers become part
of the public record.

## Checklist as a contract

Answer each section against the frozen PDF, then repair mismatches in whichever
direction is honest:

| Checklist area | The honest-answer test | Frequent violation |
|---|---|---|
| Limitations | Does §Limitations name real boundaries? | Ritual text that admits nothing |
| Artifacts used | License and terms cited for every dataset/model? | "Standard benchmark" with no license line |
| Artifacts created | Intended use and documentation stated? | Dataset released as a bare zip |
| Computational experiments | Hyperparameters, budget, infrastructure reported? | "Details in code" with no code |
| Human subjects / annotation | Instructions, recruitment, pay, consent reported? | Crowdwork treated as free magic |

A "yes" the PDF cannot support is now a desk-reject vector — the only checklist
strategy is making the paper actually deserve its answers.

## The moving-target problem: LLM-era pinning

The reproducibility hazard specific to modern NLP is that the measured object changes
under you. Pin everything that can drift:

```yaml
# repro-pin.yaml — one block per reported experiment
model: <exact identifier, e.g. open-weights checkpoint hash or API model string>
queried: 2026-04-18 .. 2026-05-02        # API results are dated observations
decoding: {temperature: 0.0, top_p: 1.0, max_tokens: 512, stop: ["\n\n"]}
prompt_file: prompts/nli_zero_shot_v3.txt # verbatim, versioned
data: {name: ..., version: ..., split: test, license: CC-BY-4.0}
seeds: [13, 42, 271, 828, 1729]
hardware: 4x A100-80GB, ~11 GPU-hours total
metric_impl: sacrebleu 2.4.0 / evaluate 0.4.2  # scores differ across implementations
```

Two entries deserve emphasis. *Query dates*: an API model result without dates is a
claim about a system that no longer exists. *Metric implementation*: BLEU, ROUGE, and
even F1 vary across implementations and preprocessing; name the package and version or
the number is not comparable to anyone else's.

## Data provenance and annotation records

- Every corpus: source, version, license, and whether its terms permit your use and
  redistribution — the checklist asks, and "found on the internet" fails.
- Every annotation effort: guidelines (released verbatim), annotator recruitment and
  compensation, agreement statistics, and adjudication procedure. These double as
  method details — agreement is evidence about the construct, not HR paperwork.
- Preprocessing is part of the dataset: tokenization, filtering, deduplication, and
  class balancing decisions all change results; script them, don't prose them.

## Release honesty levels

State the level you actually achieve rather than aspirationally overpromising:

1. **Rerunnable** — one script per table, pinned environment, seeds fixed; a stranger
   reproduces the numbers modulo hardware nondeterminism.
2. **Rebuildable** — code and data released with documented manual steps.
3. **Documented** — closed data or models prevent release, but the paper specifies
   enough (prompts, configs, dates, metrics) for a faithful reimplementation.

Level 3 with honest reasons outperforms a broken claim of level 1 in review: NLP
reviewers do try to run things, and a repository that fails on `pip install` converts a
reproducibility strength into a credibility wound.

## Compute and cost reporting

The checklist's computational-experiments section expects infrastructure and budget
answers, and the field increasingly reads them as science rather than logistics:

- Report total compute for the *reported* experiments and, separately, the rough
  multiplier for the search that found them — a method needing 40 exploratory runs to
  hit its configuration is different work to reproduce than one needing 4.
- For API experiments, report call counts and token volumes; "we evaluated GPT-x on
  the benchmark" hides a cost that determines who can replicate you.
- Name the hardware class and wall-clock, not just GPU-hours; memory limits gate
  reproduction more often than FLOPs.
- If a result exists because a large training run cannot be repeated (one seed on the
  big model, five on the small), say so where the result is reported, not only in the
  checklist.

## Cheap habits that pay at review time

- Emit result tables from logged runs programmatically; hand-transcribed numbers drift
  from their logs and reviewers who ask for logs notice.
- Keep a `RESULTS.md` mapping every number in the paper to a run ID.
- Store the exact prompt for every reported LLM number at generation time — prompts
  reconstructed later are fiction with good intentions.
- When randomness is genuinely irreducible (API nondeterminism), quantify it: repeat
  a subset of calls and report observed dispersion.

## Vignette: the number that could not be regenerated

A submission reports 71.4 F1 for its main configuration. During the response window a
reviewer asks for the per-language breakdown; the rerun produces 70.6. The cause is
archaeological: the 71.4 came from a notebook using a since-edited prompt file, on a
dataset version replaced in April. Nothing was dishonest — and nothing was pinned. The
paper now faces a window where every number is suspect. The prevention costs one habit:
no result enters the draft except from a logged run with a pinned config, and the log
ID rides along in a comment next to the table. Papers built this way answer breakdown
requests in an hour and gain credibility from the speed itself.

## Output format

```text
[Checklist audit] <section -> supported / mismatch -> fix>
[Pinning status] <models, dates, decoding, prompts, metrics: pinned or drifting>
[Provenance record] <corpus/annotation items missing license or agreement data>
[Release level] rerunnable / rebuildable / documented — as stated vs actual
[Repair queue] <ordered, cheapest-first>
```
