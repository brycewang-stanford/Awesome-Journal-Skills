# Reproducibility tooling pointer (EACL)

An EACL paper's evidence travels twice: once as an anonymized archive attached to the
August ARR cycle, and again as a public release after commitment. Both passes benefit from
the same lightweight, dependency-free scaffolding, so this pack does not ship its own copy —
it borrows the repository-wide **ML-conference methods kit**. (That kit is unrelated to the
Stata/econometrics library used by the economics journal packs in this repository.)

## Where the kit lives

The kit sits three levels up, under `shared-resources/ml-conference-methods/`:

- overview and conventions: [`README.md`](../../../shared-resources/ml-conference-methods/README.md)
- run/seed/config planner: [`experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- generic artifact audit: [`reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- smoke checker: [`code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## When to reach for it

Use the planner and matrix **before results exist**, during the design phase driven by
`eacl-experiments`. Run the smoke checker on the archive you intend to attach to ARR, days
before the single cycle deadline — never on deadline night, because there is no later cycle
to absorb a surprise:

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/anonymous-supplement
```

The checker only catches mechanical problems (missing entry points, unreadable archives). A
green result is a floor, not a pass.

## What stays an EACL-specific human job

The generic kit knows nothing about NLP or about EACL's review norms. These remain yours to
verify by hand: verbatim prompt files and decoding settings for LLM results; retained model
outputs so scores can be recomputed; annotator pay, guidelines, and agreement; dataset
license, provenance, and intended-use statements (with extra care for lower-resourced
languages); per-language results behind any multilingual claim; and agreement between the
Responsible NLP checklist and the paper. Those checks live in
[`eacl-reproducibility`](../../skills/eacl-reproducibility/SKILL.md) and
[`eacl-artifact-evaluation`](../../skills/eacl-artifact-evaluation/SKILL.md); policy questions
resolve against [`../official-source-map.md`](../official-source-map.md) and the live ARR CFP,
not against this kit.
