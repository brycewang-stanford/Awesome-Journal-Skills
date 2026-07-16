---
name: lang-data-and-transparency
description: Use when preparing the data, annotation, and reproducibility materials for a Language (LSA) manuscript — shared datasets and code, glossed corpora, sound files, and the ethics of working with language consultants and communities. Language values transparent, documented data; over-stating a mandated deposit is as wrong as hiding materials. Documents and shares; it does not run the analysis.
---

# Data & Transparency (lang-data-and-transparency)

*Language* increasingly treats **documented, checkable data and reproducible analysis** as a mark of
serious work: a reader should be able to see the pattern and, where quantitative, re-run the model. But
the requirements differ by subfield and evolve, and linguistic data carry **ethical obligations** to
consultants and communities that generic "open data" rhetoric ignores. This skill helps you document,
share, and protect your materials appropriately — without over-stating a deposit mandate the journal
may not impose.

## When to trigger

- Assembling the data/code/annotation to accompany a submission
- Deciding what can and cannot be shared (consultant confidentiality, community agreements, licensed
  corpora)
- A reader asked for the dataset, the glossed corpus, the sound files, or the analysis script
- Writing a data-availability statement

## What "transparent" means at Language (by data type)

### Quantitative (experiment / corpus)
- Share the **analysis-ready data and the script** that reproduces the models, tables, and figures;
  pin package versions and set seeds. A repository (e.g., OSF) with a readme is the norm.
- If the raw corpus is licensed, share the **derived counts + the extraction code** so the pipeline is
  reproducible even when the source text cannot be redistributed.

### Elicited / fieldwork
- Provide **numbered, Leipzig-glossed examples with sources**; where possible, archive recordings and
  annotations in a language archive (e.g., ELAR, PARADISEC, AILLA, TLA) under access terms the
  community agreed to.
- Document the **elicitation and transcription workflow** so another linguist could interpret the data.

### Phonetic
- Share measurement scripts (e.g., Praat scripts) and, where consent allows, the sound files or
  acoustic measurements; state the alignment/measurement settings.

## Ethics of linguistic data (do not skip)

- **Consent and community agreements** govern what may be archived and how; open sharing is not always
  ethical, and "restricted access" is a legitimate, respectful choice.
- **Anonymize** speakers where required; do not expose identities via metadata or audio.
- Credit consultants and communities per current best practice and any community protocol.

## Calibration (do not over- or under-state, hedged)

*Language* rewards transparency as craft, but the pack does **not** assert a specific editor-verified
replication mandate — verify the current data-availability policy on the CUP/LSA author pages before
claiming any gate. The honest posture: share what you ethically can, document what you cannot, and never
present restricted community data as if it were freely open. Illustrative: a variationist study shares
the coded token file, the R script, and a codebook on OSF, but keeps the raw interview audio restricted
under the community agreement and says so in the data statement — transparent and ethical at once.

## Referee/editor conformance check

| Slip reviewers catch | The Language-appropriate fix |
|----------------------|------------------------------|
| "Results not reproducible from what's shared." | post analysis data + script; pin versions, set seeds |
| "Glosses can't be checked." | numbered Leipzig-glossed examples with per-token sources |
| "Licensed corpus can't be shared." | share derived counts + extraction code + a pointer to the source |
| "Speaker identities exposed." | anonymize; restrict audio per consent |
| "Claims a deposit rule that isn't stated." | describe your sharing; verify the live policy, don't invent one |

## Anti-patterns

- Quantitative results with no shared data or script (reviewers cannot reproduce the model)
- Treating community/consultant data as "open" without consent or agreement
- Exposing speaker identities through metadata, audio, or examples
- Glossed data with no source, so a reader cannot verify the token
- Over-stating a journal replication mandate the live policy does not impose (verify first)

## Transparency pass for Language

Treat this skill as an executable review pass, not a prose hint. First lock what evidence underlies each
claim; then judge whether the manuscript answers the venue's real reader: linguists who value checkable
evidence and who also respect the ethics of working with speakers and communities.

- **Do the pass:** for each claim, name where the supporting data and code live, the access terms, and
  any ethical constraint on sharing.
- **Return a ledger:** give `claim / evidence / where-it-lives / sharing-constraint` rows so the next
  agent can act.
- **Sibling guard:** documentation-heavy work may fit *Language Documentation & Conservation*; if a
  sibling owns the contribution, recommend re-routing before polishing.
- **Stop condition:** do not give submission-ready advice until `resources/official-source-map.md` has
  been checked for the current data-availability policy.

## Output format

```
【Data types】experiment / corpus / elicited / phonetic / archival
【Shared】analysis data + script posted (repo/OSF)? [Y/N/NA]
【Glossed examples】numbered, Leipzig, sourced? [Y/N]
【Ethics】consent / community agreement / anonymization handled? [Y/N]
【Data statement】accurate, no over-stated mandate? [Y/N]
【Next】lang-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — archives, OSF, glossing and reproducibility tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Language data-availability policy live-check
