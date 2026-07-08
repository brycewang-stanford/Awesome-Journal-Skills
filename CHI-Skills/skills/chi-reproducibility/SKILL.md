---
name: chi-reproducibility
description: Use when strengthening research transparency for an ACM CHI paper — protocols, instruments, codebooks, analysis scripts, preregistration, and data availability under human-subjects constraints — so methods survive the ADR-Method screening and others can actually build on the work.
---

# CHI Reproducibility

Reproducibility at CHI is not "same script, same numbers." Human-subjects research
reproduces at the level of *protocol and analysis*: could a competent lab run your
study again, and could a skeptic re-derive your findings from your materials? CHI's
screening now names "research transparency" explicitly inside the **ADR-Method**
assisted desk-reject ground, so opacity is a pre-review rejection risk. The working
principle for data: **as open as consent allows, as documented as possible where it
does not.**

## Three layers, three different obligations

| Layer | What must be true | Typical artifacts |
|---|---|---|
| Protocol | Another lab could run the study | Task descriptions, scripts read to participants, stimuli, apparatus specs, recruitment text, screening criteria, compensation |
| Analysis | A skeptic could re-derive results from your data | Analysis code, codebook + coding decisions, exclusion rules, model specifications, software versions |
| Data | Shared where consent permits; described honestly where not | De-identified quantitative data, aggregate tables, transcript excerpts, or a documented reason why not |

The protocol layer is the cheapest and the most neglected: your consent scripts,
questionnaires, and interview guides already exist — publishing them in the
supplement costs an afternoon and answers half of the methods questions reviewers
would otherwise raise (`chi-supplementary`).

## Quantitative transparency

- Ship the analysis pipeline: raw-to-clean transformation, exclusions with counts and
  reasons, and the exact statistical models. Pin versions (R/Python, packages).
- Preregistration (OSF, AsPredicted) is increasingly normal for confirmatory CHI
  studies; during review, link an **anonymized view** only — a named OSF project is
  an anonymization violation (`chi-submission`).
- Report every measured variable somewhere, including ones that showed nothing;
  selective reporting discovered later damages more than a null result ever would.
- Randomization, counterbalancing assignments, and seed-equivalents (trial-order
  generation) belong in the materials, not in folklore.

## Qualitative transparency

Qualitative work cannot ship a replication button; it can ship an audit trail:

- The interview guide or diary prompts, verbatim, including probes.
- The codebook where the method uses one — codes, definitions, example excerpts —
  or, for reflexive approaches, a documented account of how themes developed.
- Analysis-process notes: who coded, how disagreements were handled, memo samples.
- Transcript excerpts beyond those quoted in the paper, where consent allows —
  reviewers increasingly distrust papers whose only visible data is ten quotes.

## Data sharing under human-subjects constraints

Never promise what consent cannot deliver. The honest ladder, top rung you can reach:

1. Full de-identified dataset in a persistent repository (OSF, institutional archive).
2. Partial release: quantitative measures public, recordings withheld.
3. Aggregate data plus instruments and codebook.
4. No data, documented reason (consent scope, re-identification risk, community
   agreements — common and respected in work with vulnerable populations), plus a
   contact path for mediated access if any exists.

For AI-infused systems add: model name **and version/date**, prompts and parameters,
and cached model outputs from the study window, because the hosted model your
participants used will not exist next year. A CHI study of "the assistant" without a
pinned version is unreplicable by construction.

## The availability statement

State per artifact class what is available, where, and why not where not:

```text
Availability. Study protocol, interview guide, questionnaires, and the full
codebook: <repository DOI>. De-identified quantitative data and analysis
scripts (R 4.4, renv lockfile): same repository. Audio recordings and raw
transcripts are not shared, per the consent agreement; extended anonymized
excerpts appear in the supplement. LLM condition: <model+version>, prompts
and all cached outputs included.
```

During review this statement appears with anonymized links; at camera-ready it flips
to named archives (`chi-camera-ready`). Write both versions on the same day so the
promises match.

## Verification before the claim

```bash
# The availability statement is a claim; test it like one.
ls protocol/ instruments/ codebook/ data/ analysis/          # inventory vs statement
grep -rEin 'available (upon|on) request' paper/ && echo "WEAK: replace or justify"
python3 -m venv /tmp/repro && /tmp/repro/bin/pip install -r analysis/requirements.txt \
  && /tmp/repro/bin/python analysis/reproduce_tables.py      # cold-start the pipeline
grep -rEil 'participant|P[0-9]+_(name|email)' data/ | head    # de-identification sweep
```

"Available upon request" earns no credit at CHI — studies of such promises across
fields show most requests go unanswered, and reviewers know it. Either deposit the
artifact or explain the genuine constraint.

## Output format

```text
[Protocol layer] complete / gaps: <missing instruments>
[Analysis layer] pipeline runs cold: yes/no · codebook/audit trail: yes/no
[Data rung] 1-4 on the ladder + one-line justification
[Anonymized-review versions] links safe for PCS: yes/no
[ADR-Method exposure] low/med/high — <the opaquest spot in the methods>
[One-day fixes] <cheapest transparency wins available now>
```
