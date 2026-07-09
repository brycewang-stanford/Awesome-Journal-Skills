---
name: eacl-reproducibility
description: Use when running the Responsible NLP checklist as a claims audit for an EACL paper, covering hyperparameter and compute disclosure, verbatim prompt and decoding reporting, data-contamination stance, variance and significance reporting, multilingual coverage claims, and consistency between the checklist answers and what the paper actually contains.
---

# EACL Reproducibility

Use this to audit an EACL paper against the **Responsible NLP checklist**, which ARR files at
submission and which the action editor and reviewers read alongside the PDF. The checklist is
not paperwork: **misleading answers are desk-rejection grounds**, and inconsistencies between
the checklist and the paper are what careful EACL reviewers hunt for. Reopen the current
checklist at `aclrollingreview.org/responsibleNLPresearch` before auditing.

## Treat the checklist as a claims audit

Every "yes" in the checklist implies a location in the paper. Walk the paper claim by claim and
confirm each is backed:

| Claim type | Must disclose | Common EACL failure |
|---|---|---|
| Model results | Hyperparameters, tuning, model size | "Default settings" with no numbers |
| Compute | Hardware, run time, total budget | Silent on cost of large runs |
| LLM prompts | Verbatim prompts + decoding params | Paraphrased or omitted prompts |
| Data | Source, license, splits, preprocessing | Undocumented or "on request" data |
| Metrics | Variance over seeds / significance test | Single-run deltas reported as wins |
| Multilingual | Languages, resource levels, per-language results | Aggregate hides where it fails |

## Contamination stance (LLM era)

- State explicitly whether evaluation data could have leaked into training — for closed LLMs
  this is often unknowable, and the honest move is to **say so and bound the risk** rather than
  claim clean evaluation. The "Leak, Cheat, Repeat" exemplar in
  `../../resources/exemplars/library.md` is the reference discipline.
- Where feasible, run an **overlap or decontamination check** and report it.

## Variance and significance floor

```text
Reporting rule of thumb:
  - >= 3-5 seeds for any headline comparison
  - report mean +/- CI or std, not a single run
  - a significance test when two systems are "close"
  - never claim a win on an unreplicated single-run delta
```

## Multilingual coverage honesty

- If the paper claims a **cross-lingual** or **multilingual** result, the checklist audit must
  confirm the languages are named, the resource levels are stated, and **per-language results**
  exist somewhere — an aggregate average is not evidence for every language.
- For lower-resourced languages, confirm dataset provenance and annotation context are
  documented; this is a recurring EACL reviewer expectation.

## Checklist-to-paper consistency sweep

```text
[ ] Every checklist "yes" maps to a section/appendix number
[ ] Hyperparameters + search space stated
[ ] Compute budget stated for expensive runs
[ ] Prompts + decoding params verbatim (if LLMs used)
[ ] Data source, license, splits, preprocessing documented
[ ] Variance/significance reported for headline claims
[ ] Contamination risk addressed honestly
[ ] Per-language results present for multilingual claims
[ ] AI-assistance use disclosed truthfully
```

## Output format

```text
[Reproducibility risk] Low / Medium / High
[Checklist-paper mismatches] <specific "yes" answers not backed in text>
[Disclosure gaps] <hyperparameters/compute/prompts/data>
[Evidence floor] <seeds/variance/significance findings>
[Contamination] <stance + any check run>
[Fix order] <what to add before the cycle deadline>
```
