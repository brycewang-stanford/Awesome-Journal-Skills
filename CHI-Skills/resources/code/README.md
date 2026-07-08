# CHI Study-Artifact Code Adapter

This directory points CHI authors to the repo-level ML-conference methods kit for
generic artifact smoke-checking, and records what that kit *cannot* check for a
human-subjects HCI submission. It is not an econometrics code library, and CHI is
not a leaderboard venue — most of a CHI artifact package is study material, not
model code.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

```bash
# Smoke-check the anonymous supplement archive before PCS upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/anonymous-supplement
```

## What the generic kit cannot check (CHI-specific passes)

Run these by hand; no script certifies them:

1. **Consent-scope match** — every shared recording, transcript, and log column is
   covered by what participants consented to, including *archival* publication in
   the ACM DL, not just review. (`chi-experiments`, `chi-artifact-evaluation`)
2. **De-identification of humans, not just authors** — participant names, voices,
   faces, employer names in quotes, and small-cell demographics that re-identify.
   The ML kit sweeps for author identity; CHI packages leak *participant* identity.
3. **Instrument completeness** — interview guide, questionnaires, task scripts,
   and codebook present and matching what the methods section claims.
   (`chi-reproducibility`)
4. **Video compliance** — captions (SRT/SBV/VTT) present and accurate; footage
   consented; audio track anonymized during review. (`chi-supplementary`)
5. **Pinned AI conditions** — model name + version/date, prompts, parameters, and
   cached outputs for any LLM/AI-infused condition participants experienced.

Venue policy always comes from [`../official-source-map.md`](../official-source-map.md),
the live `chi2027.acm.org` pages, and the submission/supplementary/camera-ready
skills in this pack — not from this adapter.
