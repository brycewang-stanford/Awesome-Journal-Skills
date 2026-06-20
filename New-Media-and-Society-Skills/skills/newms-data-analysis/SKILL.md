---
name: newms-data-analysis
description: Use when conducting and reporting the analysis of a New Media & Society (NM&S) manuscript across qualitative, content/discourse, computational, and mixed methods — making inference transparent and defensible on each tradition's own terms. Strengthens analysis and reporting; it does not collect data.
---

# Data & Analysis (newms-data-analysis)

NM&S spans interpretive, content-analytic, and computational analysis under one interdisciplinary roof.
The standard is the same across them: the analysis must be **transparent**, **credible to a reader from
another tradition**, and matched to what the evidence can support. This skill is about *inference and
reporting*, not study design (`newms-research-design`).

## When to trigger

- Moving from collected data to claims, themes, measures, or results
- A reviewer asked for reliability, robustness, validation, or a clearer analytic trail
- You need to report uncertainty or limits honestly for a cross-method audience

## Qualitative inference (interviews / ethnography)
- **Analytic transparency**: show the path from data to claim — coding/memoing process, how themes were
  built, and how many informants/instances support each theme (avoid "many participants felt…").
- **Negative cases and disconfirmation**: report instances that cut against the reading and how they
  were handled — the strongest signal of credible qualitative work.
- **Quote-to-claim discipline**: each claim is anchored to specific evidence, not an isolated vivid quote.

## Content / discourse analysis
- **Quantitative content analysis**: report **intercoder reliability** with the right statistic
  (Krippendorff's alpha preferred for most designs), the unit of analysis, and how disagreements were
  resolved; report category distributions with uncertainty, not just counts.
- **Interpretive discourse analysis**: make the interpretive logic auditable — what features of the text
  warrant the reading, and what an alternative reading would require.

## Computational analysis
- **Validation first**: report agreement between automated measures and human labels (precision/recall,
  F1, agreement) before interpreting model output as a finding.
- **Robustness**: sensitivity to preprocessing, model/hyperparameter choices, time window, and platform;
  show the result is not an artifact of one pipeline.
- **Inference and uncertainty**: report confidence/credible intervals; respect non-random API sampling;
  do not over-claim causality from observational trace data.

## Inference honesty (all methods)

State plainly what the analysis establishes — description, association, interpretation, or (rarely)
causation — and do not let verbs outrun the design. A cross-method NM&S panel reads candor as strength.

## Robustness & reliability checklist by method

| Method | Minimum credibility move | Common referee ask |
|--------|--------------------------|--------------------|
| Interviews / ethnography | analytic trail + negative cases | "How representative are these quotes?" |
| Quant content analysis | intercoder reliability (alpha) + unit defined | "What's your reliability?" |
| Discourse analysis | auditable interpretive warrant | "Why this reading not another?" |
| Computational | human-label validation + robustness sweep | "Did you validate the classifier?" |

## Worked micro-example (illustrative)

```
Computational: a classifier labels courier posts as "compliance" vs. "contestation."
Validation: 500 hand-coded posts → F1 = 0.84 reported before any substantive claim.
Robustness: result holds across two embeddings + two time windows; stated explicitly.
Inference framing: "posts shift toward compliance after a ranking change" = association, not proof of
  internalization; the qualitative strand supplies the mechanism (triangulation, per mixed design).
```

## Referee pushback → NM&S-specific fix

- *"How do I know the qualitative themes aren't cherry-picked?"* → Supply the analytic trail, theme
  prevalence, and negative cases.
- *"Your classifier is a black box."* → Add human-label validation metrics and a robustness sweep.
- *"You imply causation from observational traces."* → Downgrade the verbs; report as association and say so.

## Calibration anchors

- **Validate before you interpret.** Computational output is not a finding until it is checked against
  human labels.
- **Report what cuts against you.** Negative cases and robustness checks build more trust than a clean story.
- **Match verbs to design.** Description, association, interpretation, causation — name which one, and stop there.

## Anti-patterns

- "Participants said…" with no count, trail, or negative cases
- Content analysis with no reliability statistic or undefined unit of analysis
- Computational results with no validation against human labels
- Robustness checks omitted, leaving the result as a single-pipeline artifact
- Causal language on observational, non-random trace data

## Output format

```
【Method】qualitative / content-discourse / computational / mixed
【Inference type】description / association / interpretation / causation
【Credibility move】analytic trail / reliability stat / human-label validation
【Robustness】sensitivity checks / negative cases reported? [Y/N]
【Next】newms-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reliability, content-analysis, and computational packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — NM&S methodological breadth
