# CSCW Transparency Code Adapter

This directory routes CSCW authors to the repo-level ML/CS conference methods kit —
with a scope warning that matters more here than in any other pack: **much CSCW
evidence is qualitative or human-subjects data that must never enter a public
reproduction package.** Use the shared kit only for the computational slice of a
paper (trace pipelines, statistical analyses, system code), and let the skills
govern what stays out.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Typical use

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/anonymous-analysis-package
```

Run the smoke check only on the **computational package**: analysis scripts,
aggregated or synthetic data, and configuration. It knows nothing about consent
scopes or re-identification risk.

## What the generic kit cannot check (CSCW-specific)

- Whether interview transcripts, chat logs, or community posts in the package
  violate participant consent or a community data-use agreement — see
  [`../../skills/cscw-artifact-evaluation/SKILL.md`](../../skills/cscw-artifact-evaluation/SKILL.md).
- Whether quoted text is reverse-searchable to an identifiable person or community —
  see [`../../skills/cscw-reproducibility/SKILL.md`](../../skills/cscw-reproducibility/SKILL.md).
- Whether a codebook, not raw data, is the right shareable artifact for a
  qualitative study — see
  [`../../skills/cscw-supplementary/SKILL.md`](../../skills/cscw-supplementary/SKILL.md).

Venue policy comes from [`../official-source-map.md`](../official-source-map.md) and
the live cscw.acm.org pages, never from this adapter.
