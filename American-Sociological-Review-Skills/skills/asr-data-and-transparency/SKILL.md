---
name: asr-data-and-transparency
description: Use when handling data documentation, sharing, and confidentiality for an American Sociological Review (ASR) manuscript. ASR follows the ASA data-sharing policy — share data and documentation after a project's completion or major publications, with confidentiality and proprietary exemptions — rather than a mandatory editor-verified replication deposit. Prepares documentation; it does not over-state requirements.
---

# Data & Transparency (asr-data-and-transparency)

ASR's transparency expectations follow the **ASA data-sharing policy**, which is a professional norm
of **availability** — not (as at some journals) a mandatory, editor-run reproducibility check before
publication. The right posture is: document thoroughly, share what you ethically can, and be explicit
about confidentiality. **Confirm the current supplementary-materials policy on the live page** —
this skill does not assert a verification step the policy does not state.

## When to trigger

- Preparing data documentation and any supplementary materials
- Deciding what can be shared given confidentiality, IRB, or proprietary constraints
- Documenting qualitative or restricted-access data so claims are credible
- A reviewer asked how others could check or build on your analysis

## What the ASA data-sharing policy says (verify current wording)

- Sociologists **share data and pertinent documentation as an integral part of a research plan** and
  **generally make data available after completion of a project or its major publications**.
- **Exemptions**: where proprietary agreements with employers, contractors, or clients preclude
  sharing, or where it is **impossible to share data and protect the confidentiality** of research
  participants.
- Submitting a manuscript elsewhere while under ASR review is **unethical**; findings that already
  appeared elsewhere must be **clearly identified**.

## Good practice (do this even though ASR doesn't pre-verify)

- **Document provenance and construction.** A README/codebook describing sources, sample
  construction, variable definitions, and analysis steps — so the work is checkable.
- **Quantitative**: keep a master script + pinned versions + seeds so results can be regenerated; be
  ready to share code even if restricted data cannot be redistributed (give an access path).
- **Qualitative**: protect informants — anonymize, aggregate, or restrict sensitive material;
  consider a controlled-access repository (e.g., QDR) where appropriate; share what supports the
  claims without exposing participants.
- **Confidentiality first.** Human-subjects protection overrides sharing; state clearly when and why
  data cannot be shared, and what *can* (synthetic data, code, documentation).

## Anti-patterns

- Over-stating ASR's policy as a mandatory verified replication deposit (it is a sharing *norm*)
- Promising open data that IRB/confidentiality will not allow
- No codebook or documentation, making the analysis uncheckable
- Exposing identifiable information about ethnographic informants
- Submitting elsewhere while under ASR review (unethical)

## Output format

```
【Sharing posture】what can be shared (data / code / docs / synthetic) and what cannot, and why
【Documentation】README/codebook + provenance + (quant) seeds/pinned versions? [Y/N]
【Confidentiality】informant/participant protection handled? [Y/N]
【Prior appearance】any overlapping findings identified? [Y/N]
【Policy check】current ASR supplementary-materials policy confirmed? [Y/N/待核实]
【Next】asr-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reproducibility tooling and controlled-access options (QDR)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — ASA data-sharing policy and ethics
