---
name: facct-reproducibility
description: Use when strengthening ACM FAccT transparency and reproducibility — releasing code, data, and analysis for quantitative audits; documenting datasets and models with datasheets, model cards, and data statements; making qualitative and participatory work auditable without breaking confidentiality; pinning provenance for scraped and model-generated data; and keeping the paper, the supplementary material, and any released artifact consistent.
---

# FAccT Reproducibility

Use this before submission and again before camera-ready. At FAccT, transparency is not only the
*subject* of the field — it is a norm the community holds its own papers to. But FAccT
reproducibility is broader than "does the code run": it spans **releasing and documenting** the data
and models behind an audit, making a **qualitative** study auditable without exposing participants,
and being honest where confidentiality or proprietary access genuinely bars release. The goal is
that a competent reader could trace how you got from evidence to conclusion — and judge whether the
harm you claim is real.

## Transparency map

- **Map each finding to a verifiable location** — a paper section, a table generated from released
  analysis, a codebook, or a documented case record.
- **For quantitative audits:** release the analysis code, the dataset (or documented access), the
  exact metrics and subgroup definitions, and the seeds/versions — enough that a reader could
  re-run the disaggregation and reach your gaps.
- **For qualitative/participatory work:** release what can be shared safely — the interview
  protocol, the codebook, aggregate coded results, consent materials — and state clearly what
  cannot be shared and why (participant confidentiality, community agreement).
- **Document datasets and models, not just release them.** A **datasheet** for a dataset, a **model
  card** for a model, and a **data statement** for a language corpus are the FAccT-native
  documentation genres; use them to record provenance, composition, intended use, and known limits.
- **Keep the paper and artifact consistent.** A disparity in the PDF that no released analysis
  reproduces is the contradiction reviewers read as carelessness — or worse, as an unfalsifiable
  harm claim.

## Documentation-and-availability audit

| Claim in the paper | Weak availability answer | FAccT-ready answer |
|---|---|---|
| "We audit N deployed systems" | "Data available on request" | Released dataset (or documented access) + analysis code + subgroup definitions |
| "Our dataset is representative" | Raw files with no context | A **datasheet**: how collected, who is in it, gaps, intended and off-label uses |
| "Our model behaves fairly" | Weights only | A **model card**: evaluation disaggregated by group, intended use, known failure groups |
| "We interviewed P affected people" | Nothing (privacy cited vaguely) | Protocol + codebook + aggregate results + a clear, specific confidentiality boundary |
| "The LLM produced these outputs" | "We used a chatbot" | Model IDs and dates, prompts, cached raw outputs, sampling settings |

"Available on request" reads as *not available*; convert every such line into a concrete release,
proper documentation, or an explicit, justified exception.

## Provenance pinning

```text
[Scraped/mined data]  record source, extraction date, and terms; archive the extracted dataset,
                      not just the scraper; document deduplication and filtering
[Protected attributes] document how group labels were obtained/inferred and their error
[Models]              record exact model identifiers + access dates; cache raw prompts and outputs;
                      report sampling settings; a live-API-only study re-samples, it does not reproduce
[Qualitative]         version the codebook; log coding decisions; keep an audit trail a second
                      reader could follow
[Consent]             keep the consent/ethics record aligned with what you release
```

## Degrees of reproducibility (state the one you achieved)

- **Turnkey:** one documented command regenerates each disaggregated table/figure from released
  data.
- **Scripted:** analysis scripts exist but need documented manual steps or restricted-data access.
- **Documented:** for qualitative or confidential work, the protocol, codebook, and aggregate
  results let a reader audit the reasoning without re-running.

For FAccT, aim turnkey for anything a reviewer could rerun quickly (a fairness-metric recomputation,
a plot from released results); confidential interview data or proprietary system access stays
documented with the boundary stated. Stating the achieved level honestly beats promising turnkey
behavior that fails.

## Vignette: a mixed-methods accountability study

Consider a study combining a quantitative audit of a benefits system with interviews of claimants.
Its transparency spine: the audit code with pinned data versions and subgroup definitions; the
released (or access-documented) audit dataset with a datasheet; the interview protocol, codebook,
and aggregate themes; the consent and ethics record; and one honest paragraph on what cannot be
shared (claimant identities, the agency's internal data) and why — so the audit is falsifiable and
the qualitative reasoning is auditable, without re-harming participants.

## Consistency and camera-ready pass

- Before submission: every disparity/finding traces to released or documented evidence; datasheets
  and model cards drafted; the artifact is **anonymized** (no author names, institution paths, or
  identity-revealing repository).
- Before camera-ready: swap any anonymized link for a permanent one, finalize the datasheet/model
  card, and align the Ethical Considerations and Adverse Impacts statements with what you release.

## Output format

```text
[Finding inventory] <finding -> evidence location>
[Availability] concrete release / documented access / vague / missing
[Documentation] <datasheet / model card / data statement present where relevant? yes/no>
[Provenance gaps] <scrape terms / proxy labels / model caching / codebook>
[Reproducibility level] turnkey / scripted / documented, stated honestly
[Paper fixes] <must appear in the PDF>
[Artifact fixes] <additions before upload, kept anonymous>
```
