---
name: commres-workflow
description: Use as the entry point for any Communication Research (CR) manuscript. Routes to the right CR sub-skill based on lifecycle stage and study type (experiment, survey/panel, or content analysis). It dispatches; it does not draft content.
---

# CR Workflow Router (commres-workflow)

The orchestrator for a *Communication Research* (CR) submission. CR is SAGE's **quantitative,
social-scientific** communication journal — predominantly **hypothesis-testing experiments and
surveys** with rigorous measurement and explicit theory. The router's first job is to confirm the
paper is **theory-driven and quantitatively identified**, then send the user to the matching skill.

## When to trigger

- Starting a new CR paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding whether the study type (experiment / survey-panel / content analysis) is CR-shaped
- Returning with a decision letter (route to `commres-rebuttal`)

## First question: is this a quantitative, theory-testing communication paper?

| Situation | Read | Route to |
|-----------|------|----------|
| Hypothesis-driven experiment or survey, measured constructs | core CR fit | normal pipeline below |
| Computational/text-as-data with **hypothesis tests** on communication processes | in scope if theory-led | pipeline; emphasize measurement validation |
| Mostly qualitative / interpretive / critical | likely off-fit | re-route to *Journal of Communication* / *New Media & Society* before polishing |
| Method/measurement paper for its own sake | off-fit | *Communication Methods and Measures* |

> CR is not multi-paradigm. If the contribution is interpretive or a platform description, the
> generalist or digital-media siblings fit better — decide this **before** investing in the pipeline.

## Routing map (stage → skill)

```text
Idea / fit?                          → commres-topic-selection
Where does it sit in the field?      → commres-literature-positioning
What are the hypotheses & mechanism? → commres-theory-building
Is the design causally defensible?   → commres-research-design
Are the analyses sound?              → commres-data-analysis
Are the exhibits clear?              → commres-tables-figures
Does it read as social science?      → commres-writing-style
Data, code & open practices?         → commres-transparency-and-data
How will it be judged?               → commres-review-process
Ready to submit?                     → commres-submission
Got an R&R / decision?               → commres-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-building → research-design → data-analysis →
tables-figures → writing-style → transparency-and-data → review-process → submission → rebuttal`

Iterate: most CR papers loop theory ↔ design ↔ measurement several times before writing-style. If the
design is **prospective**, route to `commres-transparency-and-data` early to preregister.

## Anti-patterns

- Treating CR like a generalist or qualitative outlet — CR judges quantitative, theory-testing work
- A bare effect with no mechanism (mediation/moderation) — CR rewards process, not main effects alone
- Content analysis without reported intercoder reliability
- Causal language on a single cross-sectional survey
- Leaving the data-availability statement and reproducibility materials until acceptance

## Router pass for Communication Research

Treat this skill as an executable review pass, not a prose hint. First lock the communication process,
the measured constructs, the study design, and the inferential claim; then judge whether the
manuscript answers CR's real reader: a quantitatively trained communication scientist who weighs
theory, measurement validity, identification, and effect interpretation.

- **Do the pass:** Run the pack as a sequence — fit gate, theory/measurement gate, identification
  gate, evidence gate, transparency gate, output contract; stop when a gate lacks evidence.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows so the next agent
  edits rather than rediscovers the issue.
- **Sibling guard:** *Journal of Communication* (ICA flagship, all-paradigm), *Human Communication
  Research* (interpersonal/HCR), *New Media & Society* (digital, more qualitative). If a sibling owns
  the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until `resources/official-source-map.md`
  has been checked for volatile rules and the manuscript has one concrete fix for the largest
  venue-specific risk.

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Study type】experiment / survey-panel / content analysis / computational
【Route to】commres-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — communication data + software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official CR/SAGE URLs behind every fact in this pack
