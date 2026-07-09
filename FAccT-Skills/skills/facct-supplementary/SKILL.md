---
name: facct-supplementary
description: Use when deciding what belongs in an ACM FAccT paper body versus its endmatter statements, appendices, and supplementary material — the 14-page acmart budget, the extra endmatter page for ethics/adverse-impacts statements, the rule that decision-critical evidence stays in the reviewed pages, mutually-anonymous supplementary material, and how to split an interdisciplinary paper between body, endmatter, and artifact.
---

# FAccT Supplementary

Use this when assembling FAccT supplementary material. Two rules govern the split. First, the
familiar one: **the paper must be judgeable from the reviewed pages alone** — appendices and
released artifacts support the paper, they do not hold the argument. Second, the FAccT-specific one:
the **endmatter statements** (Generative AI Usage, Ethical Considerations, Adverse Impacts,
Positionality) are a distinct zone with their own page allowance and their own anonymity rules — get
that zone right or risk a policy problem independent of the paper's quality.

## The three zones

| Zone | Counts toward the 14-page limit? | Anonymity at submission |
|---|---|---|
| Body (intro → limitations) | Yes (up to 14; 15 if Revised/accepted) | Anonymous |
| Endmatter statements | No — one extra content page allowed | Mixed (see below) |
| Appendix / supplementary / released artifact | Per current CFP — confirm | Anonymous; strip metadata |

## What goes where

| Content | Body (within budget) | Endmatter | Appendix / artifact |
|---|---|---|---|
| The FAccT contribution and who is affected | Yes | — | — |
| Core method / study design / argument | Yes | — | Full parameter grids, extra config |
| Headline disaggregated results + limitations | Yes | — | Full result tables, secondary breakdowns |
| Ethical Considerations, Adverse Impacts | — | Yes | — |
| Generative AI Usage Statement | — | Yes (required) | — |
| Positionality, Acknowledgements, Author Contributions | — | Yes — **only upon acceptance** | — |
| Interview protocol, full codebook, datasheet | Summary + key themes in body | — | Yes |
| Raw data, analysis scripts | — | — | Yes |

If a reviewer would need to open the appendix to know whether the harm is real or the method is
sound, the paper is mis-partitioned — move that evidence into the body.

## The endmatter zone (FAccT-specific, easy to get wrong)

```text
[Generative AI Usage]  REQUIRED for every submission: state whether/how generative AI was used;
                       FAccT prohibits wholesale AI-generated manuscript text
[Ethical Considerations] the concerns you faced and how you addressed them (safe to include anonymized)
[Adverse Impacts]      foreseeable unintended harms once published/deployed, and mitigations
[Positionality]        how the authors' background shapes the work — IDENTITY-REVEALING, so add ONLY
                       upon acceptance; keep it OUT of the anonymous submission
[Author Contributions / Acknowledgements / Competing Interests] also identity-revealing -> acceptance only
```

The extra endmatter page does **not** count against the 14-page limit, so a strong ethics/adverse-
impacts treatment costs you nothing in body space — write it properly rather than cramming a
sentence into the conclusion.

## Mutually-anonymous supplementary rules

```text
[No identity]   no authors, affiliations, acknowledgements, funding, cluster paths, or repo owners
                anywhere in the appendix, artifact, or the statements you DO include at submission
[No positionality] the positionality/acks/contributions statements are withheld until acceptance
[Anonymized links] any released code/data link points at an anonymizing host, not a personal repo
[Clean archive]  no .git history, .DS_Store, credentials, caches, or participant-identifying files
[Opens clean]    verify the archive unzips and a README orients a reader in one minute
```

## Vignette: splitting a mixed-methods paper

A paper auditing a system plus interviewing affected users: the body keeps the contribution, the
study design, the headline **disaggregated** results with uncertainty, the key qualitative themes,
and a limitations subsection; the endmatter carries the required Generative AI Usage Statement, an
Ethical Considerations statement about the consent and re-harm risks, and an Adverse Impacts
statement about how the audit could be misused — with Positionality held for the accepted version.
The appendix/artifact holds the analysis code, the datasheet, the full codebook, and the interview
protocol. Nothing decision-critical lives only in the appendix.

## Output format

```text
[Supplement status] ready / needs fixes / not ready
[Partition check] anything decision-critical outside the body? <none / move: what>
[Page budget] body within limit? endmatter on its allowed extra page? yes/no
[Endmatter] <Generative AI Usage present? ethics/adverse-impacts drafted? positionality withheld?>
[Anonymity] archive + included statements clean of identity + metadata? passed/issues
```
