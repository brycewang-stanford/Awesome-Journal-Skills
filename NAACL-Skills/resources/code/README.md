# NAACL Reproducibility Code Adapter

This directory adapts the repo-level ML-conference reproducibility kit for
NAACL-bound submissions. It contains no venue policy — that lives in
[`../official-source-map.md`](../official-source-map.md) — and no
econometrics tooling; it is the artifact/experiment scaffold plus the
NLP-specific checks the generic kit cannot perform.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

```bash
# Smoke-check the anonymous supplement before an ARR upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
    /path/to/naacl-supplement
```

## What the smoke checker cannot see (do these by hand)

The generic checker validates package hygiene; a NAACL supplement has four
failure surfaces it never touches:

1. **Prompt completeness** — every prompt variant referenced in the paper
   exists verbatim in `prompts/`, per task and per language.
2. **Per-language preprocessing** — normalization, segmentation, and
   tokenizer versions logged for *each* language, not globally (see
   [`../../skills/naacl-reproducibility/SKILL.md`](../../skills/naacl-reproducibility/SKILL.md)).
3. **Annotation instrument** — guidelines, examples shown to annotators,
   and payment description included whenever a human judgment appears in
   any table.
4. **Community-data terms** — for corpora under partnership or
   community-controlled licenses, confirm the archive's contents respect
   redistribution limits *before* upload, not at camera-ready (see
   [`../../skills/naacl-artifact-evaluation/SKILL.md`](../../skills/naacl-artifact-evaluation/SKILL.md)).

Treat the checker as the floor and the two linked skills as the actual bar.
