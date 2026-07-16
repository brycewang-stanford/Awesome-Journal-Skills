---
name: lang-research-design
description: Use when defending the empirical design of a Language (LSA) manuscript on the terms of its subfield — elicitation and fieldwork, corpus construction, phonetic measurement, experiment, or the diachronic/typological sample. Language judges each kind of evidence by its own standards, and the design must support the theoretical claim. Defends the design; it does not run the analysis.
---

# Research Design (lang-research-design)

*Language* is method-pluralist: it publishes elicited fieldwork, corpus studies, phonetic and
experimental work, computational modeling, and diachronic/typological comparison, and it judges each by
the standards of *its own subfield*. The job here is to make the design defensible to a general,
possibly cross-subfield, double-anonymous reviewer — and to show the evidence actually supports the
theoretical claim from `lang-theory-building`.

## When to trigger

- Choosing or justifying the design before data collection or analysis
- A reader questioned the elicitation, the consultant sample, corpus coverage, measurement, or the
  typological sample
- Aligning the evidence with the analysis's predictions
- Mixed-evidence work (e.g., corpus + experiment) that must defend each component

## Defend the design (by subfield)

### Elicited / fieldwork data
- Describe **consultant number and background, elicitation method, and the recording/annotation
  workflow**; distinguish elicited judgments from spontaneous/textual data.
- Give data in **numbered examples with Leipzig interlinear glossing** and a source for each token;
  a reader must be able to see the pattern, not take it on faith.

### Corpus / quantitative usage
- Justify **corpus choice, sampling frame, and coding scheme**; report inter-annotator agreement for
  hand-coded variables; state how tokens were extracted and excluded.

### Phonetic / experimental
- Specify **participants, stimuli, task, and measurement** (e.g., forced alignment, formant/pitch
  extraction settings); pre-empt confounds; where predictions are directional, say so in advance.

### Diachronic / typological
- Make **sample construction and genealogical/areal control** explicit; guard against areal or
  bibliographic bias; keep a clear trail from primary sources to the coded generalization.

### Computational / modeling
- State what the model is a model *of*; separate the claim about the grammar from the properties of the
  architecture or training data.

## Match design to claim

The single most common *Language* reviewer objection: **the data cannot bear the generalization.** Walk
the chain: claim → prediction → the observation that would confirm/disconfirm it → the design's leverage
on that observation. A three-language convenience sample cannot ground a universal; either narrow the
claim or widen the evidence — do not overreach.

## Referee-pushback patterns by subfield (the modal Language objection)

| Referee writes… | Subfield | The Language-appropriate fix |
|-----------------|----------|------------------------------|
| "Judgments from one speaker." | fieldwork | add consultants or scope the claim to the idiolect/variety |
| "Cherry-picked corpus tokens." | corpus | report the full extraction + exclusion rule + agreement |
| "Confound with speech rate." | phonetics | control or model it; show the effect survives |
| "Sample is areally biased." | typological | rebalance the sample or restrict the generalization |

## Calibration with a quick example (hedged)

*Language* judges each subfield by its own standard, not a single template; unlike a purely formal venue
that accepts introspective judgments alone, it increasingly expects the evidence base to be visible and
checkable. Illustrative: an author claims a word-order universal from four related languages; a referee
flags "genealogical non-independence." The fix draws a genealogically stratified sample and restates the
claim as a statistical tendency with the mechanism, so the typology can see the pattern fail as well as
hold. Confirm current data expectations on the author pages and in `lang-data-and-transparency`.

## Design pass for Language

Treat this skill as an executable review pass, not a prose hint. First lock the empirical
generalization, evidence base, warrant, and theoretical payoff; then judge whether the manuscript
answers the venue's real reader: linguists across subfields who value grounded analysis, transparent and
checkable evidence, and careful, appropriately scoped generalizations.

- **Do the pass:** lock the unit (segment / token / speaker / language), the sample, the comparison, the
  validity threat, and the minimum decisive evidence before recommending collection or submission.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows so the next agent can
  edit rather than rediscover the issue.
- **Sibling guard:** compare against *Phonology*, *NLLT*, *Journal of Semantics*, *Diachronica*,
  *Language Variation and Change*; if a sibling owns the contribution, recommend re-routing before
  polishing.
- **Stop condition:** do not give submission-ready advice until `resources/official-source-map.md` has
  been checked and the manuscript has one concrete fix for the largest venue-specific risk.

## Anti-patterns

- Grounding a general claim on a convenience sample that cannot support it
- Judgments from a single consultant presented as facts about the language
- Corpus tokens hand-picked with no stated extraction or exclusion rule
- Phonetic effects reported without controlling obvious confounds
- A typological sample with unacknowledged genealogical or areal dependence
- A design that probes something adjacent to, but not, the stated prediction

## Output format

```
【Subfield】fieldwork / corpus / phonetic-experimental / typological-diachronic / computational / mixed
【Claim it must support】from theory-building
【Design leverage】how this evidence bears on the prediction
【Key threats】consultant number, sampling, confounds, non-independence, annotation
【Evidentiary trail】data → glossed examples → claim is legible? [Y/N]
【Verdict】supports the claim / needs tightening / overreaches (fix)
【Next】lang-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — elicitation, corpus, and phonetic tooling by subfield
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Language method-pluralism and evidence expectations
