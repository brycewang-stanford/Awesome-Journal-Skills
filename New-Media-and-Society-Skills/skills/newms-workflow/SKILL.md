---
name: newms-workflow
description: Use as the entry point for any New Media & Society (NM&S) manuscript. Routes to the right NM&S sub-skill based on the lifecycle stage and the method (qualitative interviews/ethnography, critical-theoretical, content/discourse analysis, computational, or mixed). It dispatches; it does not draft content.
---

# NM&S Workflow Router (newms-workflow)

The orchestrator for a New Media & Society submission. NM&S is the broad **interdisciplinary**
journal on digital media, the internet, and society, and it is **methodologically pluralist** — so the
router's first job is to confirm the work has stakes for *new media and society broadly* and to send
the user to the skill matching their stage and their method.

## When to trigger

- Starting a new NM&S paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Worried the work reads as a platform case study with no portable argument
- Returning with a decision letter (route to `newms-rebuttal`)

## First question: contribution & method

NM&S asks two things up front. First, **does this say something about new media and society**, not
just about one app or one dataset? Second, **what method carries the claim** — because design and
analysis advice differ sharply:

| Method family | Typical evidence | Routing weight |
|---------------|------------------|----------------|
| Qualitative — interviews, digital ethnography | interview corpus, fieldnotes, online observation | theory ↔ evidence loops heavily |
| Critical / theoretical | concepts, close reading, normative argument | theory-building is the spine |
| Content / discourse analysis | coded texts, posts, images, platform artefacts | coding scheme + intercoder reliability |
| Computational | scraped/API traces, networks, NLP/ML measures | validation against human labels + data ethics |
| Mixed-methods | two strands integrated | design must say how strands talk |

## Routing map (stage → skill)

```text
Idea / fit for NM&S?             → newms-topic-selection
Where does it sit in the field?  → newms-literature-positioning
What's the conceptual argument?  → newms-theory-building
Is the design defensible?        → newms-research-design
Is the analysis/inference sound? → newms-data-analysis
Are the exhibits clear?          → newms-tables-figures
Does it read for the field?      → newms-writing-style
Data ethics + transparency?      → newms-transparency-and-data
How will it be judged?           → newms-review-process
Ready to submit?                 → newms-submission
Got an R&R / decision?           → newms-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-building → research-design → data-analysis →
tables-figures → writing-style → transparency-and-data → review-process → submission → rebuttal`

Iterate: interview, ethnographic, and critical papers loop theory ↔ evidence many times before the
argument settles; do not force them through a single linear pass.

## Symptom-to-skill dispatch

NM&S referees judge interdisciplinary significance and method-appropriate rigor together. Most
symptoms map cleanly to one sub-skill — use this lookup before defaulting to the linear order.

| Symptom you arrive with | Likely root | Route to |
|--------------------------|-------------|----------|
| "A reader says it's just a platform case study" | fit / framing | newms-topic-selection |
| "Reviewer says I ignored relevant fields" | cross-field positioning | newms-literature-positioning |
| "It's called atheoretical / merely descriptive" | no portable concept | newms-theory-building |
| "Reviewer doubts the sampling / case / coding logic" | design | newms-research-design |
| "They want reliability / robustness / validation" | analysis | newms-data-analysis |
| "An exhibit or quote table is unclear" | exhibits | newms-tables-figures |
| "It reads as technical-only or jargon-heavy" | prose for the field | newms-writing-style |
| "How was this scraped — was that ethical?" | data ethics | newms-transparency-and-data |
| "What will reviewers want?" | expectations | newms-review-process |
| "Submitting tomorrow" | preflight | newms-submission |
| "Got an R&R" | response letter | newms-rebuttal |

## Worked micro-example (illustrative routing)

```
User: "I interviewed 30 gig couriers about the app that ranks them, but a colleague says it 'won't fly
  at NM&S — too niche.'"
Router read: the worry is portability, not data → start at newms-theory-building (name the mechanism:
  algorithmic management as datafied control), then newms-literature-positioning (platform-labor +
  surveillance debates), then newms-research-design (informant logic, saturation, positionality).
Method: qualitative interviews → loop theory ↔ evidence.
Then: newms-tables-figures (a quote-to-claim table) → newms-writing-style → newms-transparency-and-data
  (consent + platform-data ethics for the app screenshots).
```

The router resists the linear default and sends the interview study to theory and positioning first.

## Referee-stage pushback → which skill answers it

- *"Not significant for new media and society broadly."* → newms-topic-selection then newms-writing-style.
- *"Method isn't rigorous for its kind."* → newms-research-design in the matching tradition.
- *"Scraping looks ethically dubious."* → newms-transparency-and-data before re-submission.

## Calibration anchors

- **Interdisciplinary significance is the gate, not a garnish.** The work must reach beyond one platform
  and one field; route to topic-selection whenever fit is in doubt.
- **Method sets the path.** Qualitative/critical papers loop theory ↔ evidence repeatedly; computational
  papers stand or fall on validation + data ethics.
- **Confirm volatile specifics** (~8,000-word target, abstract length, current editors) on the live page.

## Anti-patterns

- Treating NM&S like a single-platform trade outlet — the claim must travel beyond one app or site
- Forcing a regression template onto interview, ethnographic, or interpretive work
- A computational paper with strong metrics but no validation and no data-ethics account
- Forgetting the ~8,000-word target (incl. notes, references, tables) and anonymous-review masking

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / ethics / review / submit / rebut
【Method】qualitative / critical-theoretical / content-discourse / computational / mixed
【Route to】newms-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — digital-media data sources + software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official NM&S URLs behind every fact in this pack
