---
name: newms-research-design
description: Use when defending the research design of a New Media & Society (NM&S) manuscript — informant/site logic for interviews and digital ethnography, sampling and coding for content/discourse analysis, data construction and validation for computational work, and integration logic for mixed methods. NM&S judges each tradition on its own terms. Strengthens the design; it does not write code.
---

# Research Design (newms-research-design)

NM&S welcomes many methods and is exacting about each. The design must credibly link the argument
(`newms-theory-building`) to evidence and rule out the leading alternative reading. Pick the section
matching your method; mixed-methods papers must satisfy both relevant sections *and* state how the
strands talk to each other.

## When to trigger

- Specifying sampling, case/site selection, coding, or data construction
- A reviewer questioned generalization, selection, coding reliability, or scraping validity
- Justifying why your design adjudicates the rival reading from `newms-literature-positioning`

## Qualitative — interviews / digital ethnography
- **Informant and site selection justified theoretically**, not by access alone; state recruitment,
  positionality, and access conditions (e.g., joining a platform, gaining moderator trust).
- **Depth, saturation, and negative cases**: how you know you have enough, and how disconfirming cases
  were sought and handled.
- **Online specificity**: handle the blur of public/private space, pseudonymity, and the ethics of
  observing online communities (see `newms-transparency-and-data`).

## Content / discourse analysis
- **Sampling frame** for texts/posts/images: time window, platform, query logic, and what is excluded.
- **Coding scheme** grounded in the argument; report **intercoder reliability** (e.g., Krippendorff's
  alpha / Cohen's kappa) for quantitative content analysis, or a clear analytic trail for interpretive
  discourse work.
- State what counts as evidence for vs. against the reading — discourse analysis is not "quotes I liked."

## Computational
- **Data construction**: API vs. scraping, query terms, time window, deduplication, and the gap between
  the trace data and the social phenomenon (digital traces are not the behavior itself).
- **Validation**: validate automated measures (classifiers, topic models, network metrics) against
  **human-labeled samples**; report agreement and stability; do not treat model output as ground truth.
- **Platform-bias awareness**: APIs sample non-randomly; state what the data can and cannot represent.

## Mixed methods
- Say **why** both strands are needed and **how they integrate** (triangulation, sequential
  explanation, complementarity) — not two studies stapled together.

## The adjudication test (NM&S-specific)

For the **single strongest rival reading**: *"If the rival were true rather than my argument, the
evidence would look like ___; instead it looks like ___."* If you cannot write it, the design does not
yet identify the contribution.

## What NM&S referees demand of each design

| Design | Referee's first demand | Satisfying move |
|--------|------------------------|------------------|
| Interviews / ethnography | "Why these informants/this site?" | theoretical sampling, positionality, negative cases |
| Content / discourse | "Is the coding reliable / the reading defensible?" | reliability stats or a transparent analytic trail |
| Computational | "Is the measure valid; what does the data represent?" | human-label validation, platform-bias statement |
| Mixed | "Why both, and how integrated?" | explicit integration logic |

## Worked micro-example (illustrative)

```
Method: digital ethnography of a courier community + interviews (qualitative, mixed within strand).
Site logic: a worker forum chosen because ranking disputes surface there; not just easy to access.
Negative cases sought: workers who ignore the score → would weaken "datafied control."
Adjudication sentence: "If workers merely gamed the system (resistance), we'd see post-sanction
  workarounds; instead we see anticipatory compliance before any sanction — as datafied control predicts."
```

## Referee pushback → NM&S-specific fix

- *"Your informants look hand-picked."* → Show the theoretical sampling rule and what each case represents.
- *"Scraped data, no validation."* → Add human-labeled validation of the automated measure and a
  platform-bias statement; state what the API does and does not capture.
- *"Quotes cherry-picked."* → Give a coding scheme, an excerpt-to-claim table, and the disconfirming cases.

## Calibration anchors

- **Method-appropriate rigor, one bar.** NM&S won't hold ethnography to a reliability-coefficient
  standard or computational work to "it felt saturated" — but every design must defeat its rival.
- **The adjudication sentence is the test.** If you can't write "if the rival were true the evidence
  would look like ___," the design does not yet earn the contribution.
- **Trace data ≠ behavior.** Naming the gap between API traces and social practice reads as strength.

## Anti-patterns

- Convenience informants/sites dressed up as theory-driven sampling
- Content analysis with no reliability check or analytic trail
- Computational measures reported as ground truth with no human-label validation
- Ignoring the public/private and consent ambiguity of online observation
- A design that cannot distinguish your reading from the leading rival

## Output format

```
【Method】interviews-ethnography / content-discourse / computational / mixed
【Sampling / case / data logic】and how justified
【Validity move】reliability / saturation+negative cases / human-label validation
【Rival ruled out】the adjudication sentence
【Next】newms-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — CAQDAS, content-analysis, and computational tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — NM&S methodological breadth
