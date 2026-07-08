# EMNLP NLP Reproducibility Code Adapter

Empirical NLP papers carry artifact types no generic checker fully understands:
prompt files, generation dumps, annotation guidelines, API query logs. This adapter
explains how EMNLP authors should use the repository's shared ML-conference kit — and
which NLP-specific verifications must still happen by hand. (This is not the economics
packs' Stata/DiD/IV/RDD library; nothing here concerns regression pipelines.)

## NLP-specific checks first (the part no script does)

- **Prompts verbatim, one file per reported condition.** A paraphrased prompt in a
  README is not the prompt that produced Table 3.
- **API results are dated observations.** Model identifier + query date range for
  every closed-model number; without dates the measurement target no longer exists.
- **Decoding parameters per experiment** — temperature, top-p, max tokens, stop
  sequences — logged where the run happened, not reconstructed later.
- **Output dumps included.** Full generations behind every reported number let
  reviewers and successors re-score without rerunning models.
- **Annotation records travel with the data:** guidelines, recruitment and pay,
  agreement statistics, adjudication rules — the Responsible NLP checklist's
  human-subjects answers must match these files.
- **License chain documented** for every corpus used or derived; inbound restrictions
  propagate into anything you release.

## Then run the shared kit

The generic package-hygiene checker and its companion documents live at repo level:

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

```bash
# Smoke-check the anonymous package structure before an ARR upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
    /path/to/anonymous-repro-package
```

Treat a passing run as necessary, never sufficient: the script sees files, not
whether your prompts match your paper.

## Where policy actually lives

Nothing in this directory is venue policy. Format caps, checklist enforcement, and
upload mechanics come from [`../official-source-map.md`](../official-source-map.md)
and the live ARR pages; the review-facing judgment calls live in the
`emnlp-experiments`, `emnlp-reproducibility`, `emnlp-supplementary`, and
`emnlp-artifact-evaluation` skills.
