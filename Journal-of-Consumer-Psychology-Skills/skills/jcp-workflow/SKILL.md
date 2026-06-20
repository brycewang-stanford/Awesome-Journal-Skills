---
name: jcp-workflow
description: Use when deciding which jcp-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Journal of Consumer Psychology (JCP) submission. Routes — it does not replace — the specialized skills.
---

# JCP Workflow Router (jcp-workflow)

## Overview

This is the router. It tells you **which jcp-* skill to use at the current stage** of a manuscript aimed at the *Journal of Consumer Psychology* (JCP) — the official journal of the **Society for Consumer Psychology (SCP)**, Division 23 of the American Psychological Association, published by **Wiley** (it moved from Elsevier; the resources/official-source-map.md still names the old publisher — 检索于 2026-06；以官网为准). JCP is the field's flagship for **theory-driven, mostly experimental** research on consumer judgment, decision-making, affect, motivation, identity, and persuasion. The contribution that gets a paper in is a **novel psychological PROCESS** — not a new effect, not a new context. A multi-study package that documents an effect, mediates it, and shows theory-predicted moderation is the modal accepted paper.

Operational tells that you are at JCP and not a sibling: the bar is a **psychological mechanism** (mediation/moderation-of-process), not theory-of-the-firm or strategy (that is JM), not interpretive/CCT meaning-making (that is JCR), and not a single flashy effect with no audience-specific implication (that is closer to Psychological Science). JCP runs **double-blind** review (待核实 — confirm on the Wiley author page), formats in **APA Style (7th)**, and takes four manuscript types: **Research Article** (≤50 double-spaced pages incl. everything), **Research Report** (<4,000 words excl. abstract/refs/tables/figures), **Conceptual Review**, and **Research Dialogue**.

## When to trigger

- The user asks "what should I do next?" on a consumer-psychology manuscript
- A draft has an effect but no process story, and the bottleneck is unclear
- Work is ping-ponging between theory, study design, mediation analysis, and the response letter
- A JCP decision letter arrived and the user needs to switch into revision mode
- The team is comparing JCP with JCR, JM/JMR, Marketing Science, or Psychological Science

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Phenomenon may be too applied / not process-focused / wrong outlet | `jcp-topic-selection` |
| There is an effect but no psychological mechanism / hypotheses are "A→B" | `jcp-theory-development` |
| Contribution vs. JCR / JMR / Psych Science is fuzzy or oversold | `jcp-literature-positioning` |
| Experimental design has confounds, weak manipulations, or no power plan | `jcp-methods` |
| Mediation/moderation analysis or measurement of the process needs work | `jcp-data-analysis` |
| The "what's new about the PROCESS" one-liner is not sharp | `jcp-contribution-framing` |
| Means tables / mediation figures are cluttered or asterisk-driven | `jcp-tables-figures` |
| Intro frames an effect not a mechanism; prose buries the contribution | `jcp-writing-style` |
| Ready to submit via ScholarOne; need a preflight + open-science package | `jcp-submission` |
| Want to understand AE/reviewer timeline, desk-reject odds, R&R norms | `jcp-review-process` |
| Received an R&R; need a response-letter and new-studies strategy | `jcp-rebuttal` |

## Default order

`jcp-workflow → jcp-topic-selection → jcp-theory-development → jcp-literature-positioning → jcp-methods → jcp-data-analysis → jcp-contribution-framing → jcp-tables-figures → jcp-writing-style → jcp-submission → jcp-review-process → jcp-rebuttal`

> `jcp-writing-style` is a late polish; do not rewrite the intro before the process is theorized and the mediation/moderation evidence is stable. At JCP the intro must promise a *mechanism*, so it cannot settle until `jcp-data-analysis` has confirmed what the process evidence supports.

## Routing by paper archetype

JCP papers cluster into a few shapes, and the binding constraint differs by shape. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| New effect, no mechanism yet | naming and theorizing the process | `jcp-theory-development` |
| Robust effect, weak process evidence | manipulated mediator / moderation-of-process design | `jcp-methods` → `jcp-data-analysis` |
| Process clear, sibling overlap (looks like JCR/Psych Sci) | staking the consumer-psychology contribution | `jcp-literature-positioning` |
| Short, clean single-mechanism finding | fit to the Research Report (<4,000 word) format | `jcp-topic-selection` → `jcp-submission` |
| Confirmatory theory test, want pre-result review | Registered Report route (待核实) | `jcp-methods` |

## Worked routing example (illustrative)

A user says: "My three studies show that scarcity cues increase impulse purchases, but a reviewer wrote 'this is an effect in search of a process — why does scarcity do this?'" That is the single most common JCP pushback: a documented effect with no *mechanism*. Route to `jcp-theory-development` to name the mediator (e.g., scarcity → perceived competition → arousal → impulse), then to `jcp-methods` to add a study that **manipulates** the proposed mediator or shows the effect dies when the process is blocked, then to `jcp-data-analysis` to run the mediation/moderated-mediation properly. Only once the process number is stable do you return to `jcp-contribution-framing` and `jcp-rebuttal`.

## Anti-patterns

- Treating JCP like JCR (it has **no** interpretive/CCT tradition — JCP is experimental-process)
- Treating JCP like JM/JMR (strategy/firm questions belong there, not here)
- Routing a single-effect paper straight to `jcp-writing-style` while the mechanism is still missing
- Polishing exhibits before the mediation/moderation evidence settles
- Quoting publisher/process facts from the stale source map without re-checking (it says Elsevier; JCP is now Wiley)

## Output format

```text
【Target】Journal of Consumer Psychology
【Archetype】new-effect / weak-process / sibling-overlap / research-report / registered-report
【Current bottleneck】fit / mechanism / positioning / design / process-evidence / exhibits / style / submission / revision
【Next skill】<one jcp-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
