---
name: emnlp-artifact-evaluation
description: Use when packaging the artifacts of an EMNLP paper — datasets, annotation guidelines, prompts, evaluation code, and model outputs — as anonymous review-time evidence or public post-acceptance releases, with licensing, data statements, and the inspection order NLP reviewers actually follow.
---

# EMNLP Artifact Evaluation

Use this for evidence packaging around an EMNLP submission. EMNLP has no separate
artifact-badging committee; the artifact *is* part of the scientific claim, filed under
the Responsible NLP checklist and inspected at reviewer discretion. In NLP the artifact
surface is unusually broad — data, labels, prompts, outputs, and scoring code are all
first-class — and each has its own failure mode.

## What NLP reviewers open, in order

Reviewers with thirty minutes and suspicion follow a predictable path:

| Order | Artifact | What they are checking | Cheap failure |
|---|---|---|---|
| 1 | Data sample | Do instances look like the paper's description? | Examples contradict claimed label definitions |
| 2 | Prompt files | Do prompts match the paper's claimed setup? | Prompt contains hints the paper never mentioned |
| 3 | Scoring script | Is the metric computed the standard way? | Custom normalization inflates the headline metric |
| 4 | Annotation guidelines | Could these instructions produce these labels? | Guidelines answer a different question than the task |
| 5 | Output dumps | Are generations as good as the excerpted ones? | Body examples are the best 5 of 500 |

Package for this order: a top-level README that routes to each artifact in one hop, a
data sample small enough to open in a text editor, and prompts stored as files rather
than embedded in code.

## Dataset packaging: the data statement standard

A released corpus travels with documentation or it travels badly:

- **Provenance** — where text came from, collection dates, and the license chain that
  permits redistribution (scraped ≠ redistributable; say what you verified).
- **Annotation record** — who labeled (recruitment, qualifications, compensation),
  under what guidelines (included verbatim), with what agreement (statistic and value),
  and how disagreements were resolved.
- **Composition** — languages, domains, demographic scope of speakers and annotators
  where relevant; the boundaries here feed the Limitations section directly.
- **Intended use** — the task the labels are valid for, and foreseeable misuses; a
  toxicity corpus without a misuse note reads as naive in 2026.
- **Splits and hygiene** — split construction, dedup across splits, and any overlap
  audit against common pretraining corpora.

## Prompts and outputs as archival objects

Treat prompts like code and outputs like data:

```text
artifacts/
├── prompts/
│   ├── task_nli_zeroshot_v3.txt      # verbatim, one file per reported condition
│   └── CHANGELOG.md                  # v1→v3: what changed and which tables use which
├── outputs/
│   ├── model=llama3-8b_seed=42.jsonl # every generation behind every reported number
│   └── sample_100_stratified.jsonl   # reviewer-sized random sample, stratified by error class
└── scoring/
    └── score.py                      # reads outputs/, emits the paper's tables
```

The `outputs/` directory is the underrated one: releasing full generations lets a
reviewer (and later, the field) re-score with better metrics without rerunning models —
the single highest-leverage reproducibility gift an NLP paper can give.

## Review-time anonymity vs release-time findability

The same package lives two lives. At review: anonymized hosting, no usernames in paths,
no lab-identifying data sources, license files present but grant numbers absent. After
acceptance: permanent home, citable version (tag or DOI), README pointing at the
Anthology entry, model cards / data statements filled with the identity-bearing detail
review forbade. Build the package once with an `anonymize.sh` that strips the delta,
rather than maintaining two diverging trees.

## Licensing without a legal department

The checklist asks about licenses in both directions — what you used and what you
release — and most failures are ignorance, not malice:

- **Inbound:** a benchmark's license travels with its derivatives; a corpus built by
  filtering a research-only dataset cannot ship under a commercial-friendly license.
  Record the license of every ingredient at collection time, because reconstructing
  the chain in deadline week fails.
- **Model outputs:** generations from API models may carry terms-of-use restrictions
  on redistribution and on training-data use; releasing an output corpus without
  checking the provider's terms is the current decade's version of scraping-and-
  hoping.
- **Outbound:** pick a standard license (CC for data, a common OSS license for code),
  state it in the README *and* in the paper, and resist inventing bespoke "research
  only, email us" terms that make the artifact uncitable in practice.
- **People in the data:** licensing does not settle privacy; text containing personal
  information needs handling and redaction notes independent of copyright status.

## Restricted and unreleasable material

When data cannot ship (privacy, license, platform terms): release the collection
*pipeline* and filters instead of the corpus; provide a synthetic or public-subset
sample demonstrating the format; state retention terms and whom to contact for
research access. For closed API models, ship exact prompts, dates, decoding
parameters, and full outputs — the model is closed; your measurement of it need not
be. The checklist rewards documented honesty over silent omission in every one of
these cases.

## Versioning after release

An NLP artifact that succeeds gets *used*, and use creates obligations the paper never
mentioned:

- Tag the exact version the camera-ready numbers came from and never move that tag;
  fixes go in new versions with a changelog explaining what results they might shift.
- When label errors are found post-release (they will be), publish errata in the
  repository rather than silently rewriting files other papers already evaluated on —
  benchmark drift breaks comparability for everyone downstream.
- Keep an issue tracker open; the questions users file are a free audit of your
  documentation's gaps and occasionally of your paper's claims.

## Output format

```text
[Package role] review-time evidence / camera-ready release / both
[Inspection path] <README -> data sample -> prompts -> scoring -> outputs: intact?>
[Data statement] <provenance / annotation / composition / use / splits — gaps>
[Anonymity delta] <what anonymize.sh strips; leaks found>
[Unreleasable items] <artifact -> documented workaround>
```
