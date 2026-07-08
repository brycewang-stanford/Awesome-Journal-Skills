---
name: colm-reproducibility
description: Use when hardening a COLM paper's reproducibility story — pinning open-weight checkpoints and tokenizers, handling API-model drift and deprecation honestly, versioning evaluation harnesses and prompts, disclosing compute, and writing availability statements that distinguish what is releasable from what is not.
---

# COLM Reproducibility

Reproducibility at a language-modeling venue is a different problem than at a
classical ML venue, because the central artifact — the model — is often either too
large to rerun or owned by someone else and changing weekly. COLM papers therefore
need a *layered* story: what any reader can redo, what a funded lab can redo, and
what will drift no matter what anyone does. Say which layer each claim lives in.

## The three reproducibility layers

| Layer | Who can redo it | Your obligation |
|---|---|---|
| Exact | Anyone with the artifact | Pinned checkpoint + harness + prompts + decoding → same numbers (within stated sampling noise) |
| Budgeted | A lab with comparable compute | Full training recipe: data, hyperparameters, schedule, hardware, wall-clock, known failure modes |
| Drifting | Nobody, eventually | API-model results: version string, query dates, and an expiry-honest caveat in the paper |

A paper whose headline claim lives entirely in the drifting layer needs to say so on
the page where the claim is made — and ideally to anchor the finding on at least one
open-weight model so the exact layer is not empty.

## API models: the honesty protocol

Closed models are legitimate scientific objects at COLM — much of the field studies
them — but they demand a specific discipline:

- Record the **full version identifier** and the **date range of every query**;
  "GPT-class model, spring 2026" is not a citation.
- Treat model deprecation as a known risk: state which results a reader can expect
  to reproduce only while the version is served.
- Do not average over silent version changes — if a provider updated mid-experiment,
  the runs before and after are different systems.
- Cache raw responses. The response archive *is* the reproducible artifact when the
  model disappears; releasing (input, output) pairs, licenses permitting, converts a
  drifting claim into an exact one about the recorded behavior.

## What "pinned" means, concretely

```bash
# An open-weight result is pinned when all four hashes exist in the paper/repo:
MODEL_REV=8f3c21a       # checkpoint revision, not just the model name
TOKENIZER_REV=8f3c21a   # tokenizers change under stable names too
HARNESS_SHA=$(git -C eval-harness rev-parse --short HEAD)
PROMPTS_SHA=$(sha256sum prompts/*.txt | sha256sum | cut -c1-12)
echo "model=$MODEL_REV tok=$TOKENIZER_REV harness=$HARNESS_SHA prompts=$PROMPTS_SHA"
```

The harness hash matters more than newcomers expect: extraction rules, answer
normalization, and few-shot formatting differ across harness releases and can move
benchmark scores by points. A score without a harness version is not comparable to
anyone else's score.

## Training-side recipe (budgeted layer)

If the paper trains or fine-tunes, report: base checkpoint and revision; dataset
composition with filtering steps and, where possible, released data or reproducible
filtering code; optimizer, learning-rate schedule, batch size, steps/epochs,
precision; hardware and GPU-hours; and everything that went *wrong* — divergences,
restarts, hand-tuned interventions. The failure narrative is what separates a recipe
someone can follow from a recipe that only worked once.

## Compute and cost disclosure

Give a single table: training GPU-hours (or API fine-tuning spend), evaluation
GPU-hours or API token spend, and totals including preliminary experiments if
material. This is a COLM-community expectation for two reasons — cost is part of any
efficiency claim, and disclosure lets smaller groups judge whether replication is
even feasible before they try.

## The availability statement

Write it as commitments, not vibes. For each artifact class — code, prompts,
trained weights, training data, evaluation data, raw model outputs — state one of:
*released at submission (anonymized)*, *released on acceptance*, *available on
request*, or *cannot be released because <specific reason: license, privacy, ToS>*.
"Code will be made available" with no object and no date is the pattern reviewers
have learned to distrust.

Note: no dedicated COLM reproducibility checklist or artifact-certification track
was verifiable for the 2026 cycle (checked 2026-07-08, 待核实 each edition) — this
discipline is enforced by reviewers, not by a form, which in practice makes it
*more* visible in scores, not less.

## When you cannot release

Legitimate blockers exist; the discipline is to substitute the strongest releasable
proxy instead of going silent:

| Blocked artifact | Reason | Releasable proxy |
|---|---|---|
| Training corpus | Licensed / scraped text | Filtering code + corpus statistics + a datasheet of sources |
| Fine-tuned weights | Base-model license forbids derivatives | Training recipe + LoRA/adapter deltas if permitted + eval harness |
| Raw API outputs | Provider ToS limits republication | Scored per-item results + a small quoted-excerpts sample within fair use |
| Human-eval transcripts | Annotator privacy | Aggregated ratings + instructions + anonymized examples with consent |
| Internal eval set | Planned reuse as a held-out set | A public dev split + hash commitments to the held-out items |

The hash-commitment trick in the last row deserves wider use: publishing item
hashes today proves later that the held-out set did not move, which protects both
you and the benchmark.

## Pre-submission audit

- Every number's layer identified (exact / budgeted / drifting), and the paper says
  which.
- Four hashes present for every open-weight result; version strings + query dates
  for every API result; raw responses cached.
- Training recipe complete enough that its absence would be the reviewer's only
  question.
- Compute table present.
- Availability statement itemized by artifact class with concrete commitments.
- Anonymization of released artifacts checked (`colm-submission` sweep) — an
  identity-leaking repo is worse than none at submission time.

## Output format

```text
[Repro layers] exact: <claims> / budgeted: <claims> / drifting: <claims>
[Pinning audit] model ▢ tokenizer ▢ harness ▢ prompts ▢ query-dates ▢
[Response cache] exists / missing for API experiments
[Compute table] present / absent
[Availability] itemized commitments / vague — rewrite
[Top gap] <the one omission a reviewer will find first>
```
