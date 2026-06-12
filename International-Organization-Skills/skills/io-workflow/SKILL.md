---
name: io-workflow
description: Use as the entry point for any International Organization (IO) manuscript. Routes to the right IO sub-skill based on where you are in the lifecycle and which article type (Research Article, Research Note, Essay) fits. IO is the IR-specialist flagship, so the router's first job is to confirm the paper is an international-relations contribution, not a domestic-politics paper with an international label. It dispatches; it does not draft content.
---

# IO Workflow Router (io-workflow)

The orchestrator for an *International Organization* submission. Figure out the stage and the **article
type**, then send the user to the matching skill. IO is the **leading journal of international
relations** — the router's first job is to make sure the **international or cross-border phenomenon is a
major cause or effect**, and that the paper offers a **generalizable theory** of international politics.

## When to trigger

- Starting a new IO paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding among **Research Article / Research Note / Essay**
- Returning with a decision letter (route to `io-rebuttal`)

## First question: is it really an IR paper, and which type?

| Situation | Article type | Route to |
|-----------|--------------|----------|
| Full original IR study, generalizable theory | **Research Article** (≤ 14,000 words) | normal pipeline below |
| Focused single IR contribution | **Research Note** (≤ 8,000 words) | normal pipeline, tighter scope |
| Conceptual / agenda-setting / debate piece | **Essay** (≤ 10,000 words) | `io-theory-building` + `io-literature-positioning` |
| International phenomenon is only backdrop | (off-fit) | back to `io-topic-selection` — re-center the international level |

> If the international or cross-border phenomenon is not a **major cause or effect**, the paper is not
> yet an IO paper — fix that before anything else.

## Routing map (stage → skill)

```text
IR fit / theory worth it?         → io-topic-selection
Where does it sit in IR debates?  → io-literature-positioning
What's the IR theory?             → io-theory-building
Is the international design sound? → io-research-design
Are the analyses sound?           → io-data-analysis
Are the exhibits clear?           → io-tables-figures
Does it read for IR scholars?     → io-writing-style
Repro package + DAS verifiable?   → io-transparency-and-data-policy
How will it be judged?            → io-review-process
Ready to submit?                  → io-submission
Got an R&R / decision?            → io-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-building → research-design → data-analysis →
tables-figures → writing-style → transparency-and-data-policy → review-process → submission → rebuttal`

Iterate: IR papers usually loop theory ↔ design ↔ analysis several times before writing-style.

## Calibrating to the IO house culture

Before routing, internalize what makes *International Organization* distinct from the generalist
flagships. IO is the leading outlet in international relations and international political economy,
published by Cambridge University Press for the IO Foundation. Its culture is **theory-forward**: a clever
identification strategy with a thin argument lands worse here than at an econometrics-driven venue,
because editors and referees reward a portable theory of world politics — institutions, cooperation and
conflict, security, the global economy — over a stand-alone result. IO is also **methodologically
plural**: formal, quantitative, and qualitative work all appear, so never push a qualitatively strong
paper toward a quantitative reframe to "fit." Finally, IO sets a **broad-significance bar** — the
contribution should reshape how IR scholars understand a general phenomenon, not just document one
institution. Hold these three anchors as you dispatch.

## Lifecycle-to-skill decision table

| You can say… | Bottleneck | Send to |
|--------------|-----------|---------|
| "I have data but no general IR claim" | theory deficit | `io-theory-building` |
| "Reviewers say I missed the IR debate" | positioning | `io-literature-positioning` |
| "Is my treaty/membership design causal?" | identification | `io-research-design` |
| "I'm over the word cap (exhibits count)" | length | `io-writing-style` + `io-tables-figures` |
| "Conditional acceptance — they want code" | pre-final verification | `io-transparency-and-data-policy` |
| "A rationalist and constructivist referee clash" | R&R adjudication | `io-rebuttal` |

## Worked routing vignette (illustrative)

A scholar arrives with a finished panel showing that states ratifying a human-rights treaty later report
better compliance, and wants to "submit to IO next week." The router does **not** jump to `io-submission`.
The first diagnostic is the IR-fit screen: is the institution a *major cause*, or is the correlation
driven by **selection into ratification**? Because the causal claim is unestablished and the *general*
mechanism is unstated, the router sends them back through `io-topic-selection` → `io-theory-building` →
`io-research-design` (a ratification-timing design that breaks selection) before any submission step.
Routing the empirics-first instinct into theory-first order is the router's core job at IO.

## Anti-patterns

- Treating IO like a generalist political-science journal (APSR/AJPS/JOP) — IO wants an **IR** theory, not a domestic-politics result with international data attached
- Leading with data when the contribution should be **generalizable theory** about international politics
- Leaving the reproducibility package and Data Availability Statement until acceptance — IO **verifies results and formal proofs before final acceptance**
- Sending a domestic-comparative paper where the cross-border mechanism is incidental

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Article type】Research Article / Research Note / Essay
【IR fit】international phenomenon = major cause/effect? [Y/N]
【Route to】io-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — IR data sources + software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official IO URLs behind every fact in this pack
