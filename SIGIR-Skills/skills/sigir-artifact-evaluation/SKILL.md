---
name: sigir-artifact-evaluation
description: Use when packaging code, run files, test collections, or judgments for a SIGIR submission — deciding between an artifact inside a full/short paper and a standalone Resources track paper, building reviewer-runnable IR repositories, run-file and qrels hygiene, licensing and datasheets, and single- vs double-anonymous handling.
---

# SIGIR Artifact Evaluation

At SIGIR, "artifact" means something more specific than in most ML venues: the
community's unit of exchange is the **run file + qrels + index recipe**, inherited
from the TREC evaluation tradition. A SIGIR artifact is convincing when a stranger
can rebuild your ranking, score it with standard tooling, and get your table. This
skill covers packaging that artifact — and the routing decision that comes first.

## Routing: artifact-in-paper vs Resources paper

SIGIR 2026 explicitly forbids double-dipping: the same dataset cannot be both a
Resources track submission and the contribution of another paper. Decide ownership:

| Situation | Route |
|---|---|
| Code/runs that back a method claim | Repository cited from the full/short paper |
| New corpus/judgments, and the *resource itself* is the contribution | Resources track (6 pages + refs, **single-anonymous** in 2026) |
| New resource used incidentally by a method paper | Method paper cites it; release separately; do not also submit it as a Resource paper in the same cycle |
| Reproduction study of published results | Reproducibility track (own track in 2026; budget 待核实) |

The anonymity asymmetry matters operationally: Resources reviewers may inspect the
real, non-anonymized resource, while full-paper reviewers must see an anonymized
mirror. Same artifact, two different packaging jobs.

## The reviewer-runnable IR repository

Structure the repository around the evaluation chain, because that is how an IR
reviewer will try to audit it:

```text
repo/
  README.md            # 10-minute path: install -> retrieve -> evaluate -> Table 2
  environment.yml      # or Dockerfile; pin the retrieval toolkit version
  data/DOWNLOAD.md     # scripted fetch for public collections; never redistribute
  indexing/build.sh    # exact analyzer/tokenizer settings — silent nDCG movers
  runs/                # TREC-format run files behind every table row
  qrels/               # only if you created judgments; else pointers + checksums
  eval/score.sh        # ir_measures / trec_eval invocation with exact flags
  eval/significance.py # the paired test that produced the paper's p-values
  MANIFEST.md          # table-of-paper -> script -> run file mapping
```

Non-negotiables:

- **Run files are the artifact.** Ship the exact TREC-format runs behind every
  reported number; they let reviewers verify metrics without re-running GPUs.
- **The index recipe is part of the method.** Stemming, stopwords, max sequence
  length, and doc-splitting settings change scores; record them as code, not prose.
- **Score with community tooling** (`trec_eval`, `ir_measures`, `ranx`, or the
  toolkit's own eval) so numbers are checkable in one command.
- **Checksums for derived data**: qrels subsets, filtered corpora, sampled queries.

```bash
# The audit a reviewer (or you, pre-submission) should be able to run
conda env create -f environment.yml && conda activate repro
bash indexing/build.sh && bash eval/score.sh runs/ours.trec
python eval/significance.py runs/ours.trec runs/bm25.trec  # matches §5?
```

## Judgments and collections as artifacts

If you built topics, judgments, or a corpus:

- Document the **annotation protocol**: assessor pool, guidelines, pay, agreement
  statistics (e.g., Cohen's or Krippendorff's), and adjudication.
- State **pooling**: which systems contributed to the judged pool and to what depth —
  unpooled dense-retrieval evaluation is a known validity trap reviewers probe.
- License explicitly (CC variants for data; note source-document terms separately)
  and include a datasheet: provenance, intended use, known biases, PII handling.
- For web/log-derived data, describe the privacy pipeline; "anonymized internally"
  without method is treated as unusable by careful reviewers.

## Anonymized review packaging (full/short papers)

- Mirror the repo to an anonymous host; scrub commit history (fresh export, not a
  redacted clone), usernames in paths, and institution-specific cluster scripts.
- Keep the mirror **small and runnable**: reviewers grant minutes, not hours. The
  10-minute README path decides whether the artifact helps or is ignored.
- Model checkpoints too large to host anonymously: ship the training script plus the
  exact seed/config, and say so plainly in the README.

## Packaging failures reviewers actually hit

Observed failure modes, in descending frequency:

- The README's first command fails (missing `environment.yml` pin, absolute paths,
  CUDA assumptions) — the reviewer stops there and the artifact scores as absent.
- Run files present but **not mapped to tables** — without a MANIFEST, a reviewer
  cannot tell `runs/final3.trec` from `runs/final3_fixed.trec`.
- Redistributed data the license forbids (qrels, corpus slices) — a policy problem
  that outlasts the review.
- Evaluation script computes a nonstandard metric variant silently (e.g., a
  different gain function for nDCG) — the "numbers don't match" review comment.
- Anonymization done by deletion: the repo compiles but the interesting config was
  "removed for anonymity," which reads as hiding.

## Post-acceptance hardening

- Replace the mirror with the public repository before camera-ready; mint an archival
  DOI (Zenodo or institutional) for the frozen state the paper describes.
- Register resources where the community looks: `ir_datasets` integration, a
  Hugging Face dataset card, or TREC-adjacent registries as fits the artifact.
- Badging: ACM defines artifact badges, but whether SIGIR applies them this cycle was
  not verifiable (待核实) — treat badges as optional polish, run-file hygiene as core.

## Output format

```text
[Artifact route] in-paper repo / Resources paper / Reproducibility track / release-only
[Runnable path] install->index->retrieve->score minutes: <n> (goal <=10 read + run start)
[Run-file coverage] tables backed by shipped runs: <k>/<n>
[Index recipe] scripted y/n; analyzer settings recorded y/n
[Judgment docs] protocol/agreement/pooling/license: complete / gaps <list>
[Anonymity mode] double-anonymous mirror / single-anonymous real repo
[Post-acceptance] DOI plan, ir_datasets/HF registration plan
```
