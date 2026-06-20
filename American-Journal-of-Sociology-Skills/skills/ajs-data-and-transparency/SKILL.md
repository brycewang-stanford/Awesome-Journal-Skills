---
name: ajs-data-and-transparency
description: Use when handling data documentation, sharing, and confidentiality for an American Journal of Sociology (AJS) manuscript. AJS does NOT advertise a mandatory editor-verified replication package like APSR/AJPS; document thoroughly, share what you ethically can, and verify the current policy. Prepares documentation; it does not over-state requirements.
---

# Data & Transparency (ajs-data-and-transparency)

AJS's public author guidance is **less prescriptive** on mandatory replication than APSR or AJPS:
there is **no advertised editor-verified reproducibility deposit** comparable to a Dataverse
verification step. Do **not** assert a requirement that AJS does not state. The right posture is:
document thoroughly, share what you ethically can, protect informants, and **confirm the current
supplementary-materials / data-availability policy on the live AJS pages** before submission.

## When to trigger

- Preparing data documentation and any supplementary materials
- Deciding what can be shared given confidentiality, IRB, or proprietary constraints
- Documenting comparative-historical or ethnographic evidence so claims are checkable
- A reader asked how others could verify or build on the analysis

## What AJS does / does not require (verify current wording)

- **No advertised mandatory, editor-verified replication package.** Treat reproducibility as **good
  practice you choose**, not a stated gate; live-check current data-availability or supplementary
  policy before submission.
- **Originality / overlap:** if the paper overlaps your prior published or under-review work, prepare
  a brief **originality statement** saying what is new here.
- **Ethics:** **concurrent submission to more than one journal violates the Press's ethical
  standards** and leads to rejection.

## Good practice (do this even though AJS may not pre-verify)

- **Document provenance and construction.** A README/codebook describing sources, sample construction,
  variable definitions, and analysis steps so the work is checkable.
- **Quantitative:** keep a master script + pinned versions + seeds; be ready to share code even when
  restricted data cannot be redistributed (give an access path).
- **Comparative-historical:** cite primary sources precisely enough that the evidentiary trail can be
  followed.
- **Ethnographic / interview:** protect informants — anonymize, aggregate, or restrict sensitive
  material; a controlled-access repository (e.g., QDR) where appropriate; share what supports the
  claims without exposing participants.
- **Confidentiality first.** Human-subjects protection overrides sharing; state clearly when and why
  data cannot be shared, and what *can* (synthetic data, code, documentation).

## Transparency posture by tradition (an AJS decision table)

AJS is method-pluralist, so "transparency" means a checkable evidentiary trail proportionate to the claim, not a one-size deposit. Confirm current policy wording against the journal's current submission guidelines.

| Tradition | Minimum documentation | Substitute when full sharing is impossible |
|-----------|-----------------------|------------------------------------|
| Quantitative (public data) | master script, codebook, pinned versions, seeds | post code + derivation steps |
| Quantitative (restricted) | as above + an access path | synthetic data + application instructions |
| Comparative-historical | primary-source citations, archive locators | a source appendix readers can retrieve |
| Ethnographic / interview | coding scheme, within-case sampling logic | aggregated excerpts; controlled-access deposit (QDR) |
| Network / computational | boundary rules, tie definitions, missingness | anonymized edgelist + generation code |

## Calibration (where AJS sits, hedged)

AJS's craftsmanship culture means referees value a documentation trail that lets a skeptical reader follow the inference — even though AJS does not advertise an editor-verified replication gate the way some political-science journals do. Unlike a parsimony-first sibling that may lean on one mandatory deposit, at AJS the depth and checkability of the tradition-appropriate trail carry the day; treat thorough documentation as a craft choice, and confirm the live data-availability policy before submission.

Illustrative: a welfare-state study draws on three archives plus a restricted panel that cannot be redistributed. Applying the table, the author posts the script and codebook, adds a source appendix with exact archive locators (an illustrative ~140 primary sources), and supplies a synthetic panel plus data-access steps — documentation chosen to make the inference checkable, not overstated as an AJS-verified deposit.

## Anti-patterns

- Over-stating AJS policy as a mandatory verified replication deposit (it does not advertise one)
- Promising open data that IRB / confidentiality will not allow
- No codebook or documentation, making the analysis uncheckable
- Exposing identifiable information about ethnographic informants
- Submitting elsewhere while under AJS review (violates the Press's ethical standards)
- Treating transparency as one fixed deposit rather than a tradition-appropriate evidentiary trail

## Output format

```
【Sharing posture】what can be shared (data / code / docs / synthetic) and what cannot, and why
【Documentation】README/codebook + provenance + (quant) seeds/pinned versions? [Y/N]
【Confidentiality】informant/participant protection handled? [Y/N]
【Originality statement】prepared if overlap with prior work? [Y/N/NA]
【Policy check】current AJS data/supplementary policy confirmed on live page? [Y/N/live-check needed]
【Next】ajs-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reproducibility tooling and controlled-access options (QDR)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — AJS ethics / originality and the live-check boundary for data policy
