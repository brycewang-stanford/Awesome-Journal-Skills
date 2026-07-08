---
name: acl-supplementary
description: Use when organizing appendices and supplementary material for an ACL paper under ACL Rolling Review, covering the mandatory Limitations and optional ethics sections, appendices after references, anonymized software and data archives, the no-cloud-links rule, and deciding what must stay in the 8-page or 4-page body.
---

# ACL Supplementary

Use this when splitting an ACL paper between body, appendix, and archive. The
governing ARR principle: **reviewers are not required to consider material in
appendices or supplements**, so anything decision-critical that lives only
there is effectively invisible.

## The ACL page anatomy

```text
[ content pages: 8 long / 4 short ]   <- the reviewed argument lives here
[ Limitations (REQUIRED, unlimited) ] <- after conclusion, outside page count
[ Ethics statement (optional) ]
[ References (unlimited) ]
[ Appendices (unlimited, same PDF) ]  <- optional reading for reviewers
+ separate .tgz/.zip archive          <- software / data supplement
```

Missing Limitations is a desk-reject condition; treating it as one throwaway
sentence is a review-stage penalty even when it passes the gate.

## What must not leave the body

- The main results table and the headline comparison.
- Task definition and enough of the method that a reviewer can judge novelty.
- At least a summary of the error analysis — a pointer-only error analysis
  reads as not having one.
- Human-evaluation design in one paragraph: raters, items, agreement.
- The experimental setup at reproduction-outline level; full grids can go down.

## What appendices are good at

- Full prompt texts and few-shot exemplars (reference them per experiment).
- Complete hyperparameter tables and search ranges.
- Per-language / per-dataset breakdowns behind an averaged headline number.
- Annotation guidelines and interface screenshots.
- Extended qualitative examples and additional ablations.
- Proofs or derivations for the occasional formal result.

## Limitations section that actually works

| Weak pattern | Stronger ACL pattern |
|---|---|
| "Results may not generalize" | Name the languages, domains, and model scales actually tested and the nearest untested regime |
| "LLMs can hallucinate" | State which conclusions depend on a specific model snapshot and API behavior |
| Silent on data | Note license constraints, demographic skew, or collection-window bias in the corpora used |
| Written last-minute | Mirrors the risks reviewers will find anyway, defusing them on your terms |

ACL's policy explicitly instructs reviewers not to punish honest limitations,
which makes this section the cheapest goodwill in the whole submission.

## Archive rules and hygiene

- Upload software/data as .tgz or .zip in the OpenReview fields; personal
  cloud-storage links are barred, and any external page must be anonymous and
  untracked.
- Strip authorship trails: git history, notebook metadata, absolute paths with
  usernames, license headers, README contact lines.
- Test the archive on a clean machine: it must unpack, the README must state
  what maps to which table, and nothing should require credentials just to read.
- Include model outputs where feasible so reviewers can verify scoring without
  compute (see `acl-reproducibility`).

## Body-vs-appendix vignette

A long paper introduces a retrieval-augmented QA method with results on six
benchmarks in three languages. Body: method figure, main table (six benchmarks
averaged + per-language block), two-paragraph error analysis, one ablation that
carries the mechanism claim. Appendix: full per-benchmark tables, prompts,
retrieval index details, remaining ablations, annotation guidelines for the
human study. Archive: code, prompts as files, and all model outputs. The test:
a reviewer who never scrolls past the references can still reconstruct and
believe every claim in the abstract.

## Appendix ordering convention that reviewers navigate well

- A: full experimental setup (models, hyperparameters, hardware, budgets).
- B: prompts and few-shot exemplars, one subsection per experiment.
- C: complete results — per-dataset, per-language, per-seed tables behind
  every averaged number in the body.
- D: annotation materials — guidelines, interface, pay, agreement detail.
- E: additional analyses and ablations, each forward-referenced from the
  body at least once (unreferenced appendix content is invisible).
- F: qualitative examples, marked as random or curated — say which.

Number tables and figures continuously with the body so the author response
can cite "Table 9" unambiguously during the discussion phase.

## Ethics statement: when to write one

Write it when the paper involves human subjects or annotators, scraped
user-generated content, demographic inference, dual-use capability, or
release of models/data with realistic misuse paths. Skip it when nothing
applies — the Responsible NLP checklist already covers the routine cases,
and a padded statement invites the very scrutiny it fails to answer.
It shares the unlimited space after the conclusion with Limitations.

## Size and dependency guardrails

- Keep the archive small enough to download on conference-hotel wifi;
  reviewers abandon multi-gigabyte supplements unopened.
- No credentials, no API keys, no gated-model weights — describe access
  paths instead of shipping secrets.
- Pin dependency versions in one environment file; "latest transformers"
  is a different codebase every cycle.
- If data cannot be shared (license, privacy), include the loader code and
  a synthetic sample with identical schema so scripts still run.

## Output format

```text
[Split status] sound / body-overloaded / appendix-dependent
[Limitations quality] substantive / ritual / missing
[Must-move-up] <decision-critical items currently below the fold>
[Archive check] <format/anonymity/clean-machine findings>
[Reviewer-blind spots] <claims visible only outside the body>
```
