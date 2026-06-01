---
name: misq-topic-selection
description: Use when shaping or stress-testing a research question for MIS Quarterly — confirming it is a genuine information-systems question, naming which of the four IS traditions (behavioral, design science, economics, organizational) it lives in, and choosing the matching manuscript category before any data are collected or any artifact is built.
---

# Topic Selection & Genre Fit (misq-topic-selection)

## When to trigger

- The idea is interesting but you are not sure it is an *IS* question versus a generic management, marketing, or CS question
- You have a dataset, a platform, or a model and need a question worth a MISQ slot
- You cannot yet say which tradition the paper belongs to, or which submission category fits
- A colleague says "this could go to MISQ" and you need a fit test before committing months of work

## Is it an information-systems question?

MISQ publishes research on the development, use, impact, management, and economics of information technology — IT-based services, the management of IT resources, and the use and impact of IT with managerial, organizational, and societal implications. The IT artifact (a system, algorithm, platform, data, or digitally enabled practice) should be **central**, not incidental. If the technology could be swapped for "any treatment" without changing the theory, the paper is probably not an IS paper.

## Name the tradition — it decides everything downstream

| Tradition | The paper's job | Typical category |
|-----------|-----------------|------------------|
| **Behavioral** | Explain/predict how people and organizations adopt, use, and are affected by IT | Research Article / Research Notes |
| **Design science** | Build and rigorously evaluate a novel, purposeful IT artifact that solves a real problem | Design Science |
| **Economics of IS** | Identify the causal economic effects/mechanisms of IT (markets, platforms, productivity, pricing) | Research Article / Research Notes |
| **Organizational** | Theorize IT in organizational and social context (governance, transformation, work) | Research Article / Theory Development |

MISQ explicitly welcomes **cross-tradition blends** (e.g., a design-science artifact evaluated with a behavioral experiment, or an economics-of-IS question with organizational theory). Name the primary tradition, then declare the blend.

## Choose the matching manuscript category

Self-select the genre up front, because length and evaluation criteria differ:
- **Research Article** — primary empirical category (50 pp).
- **Research Notes** — focused contribution, roughly half a Research Article.
- **Theory Development** — a substantive new theory (55 pp).
- **Theory-Generative Research Synthesis** — synthesis that generates theory (65 pp).
- **Issues and Opinions** and **Design Science** — verify exact limits at misq.umn.edu/categories-lengths (待核实 for some).

Page limits count **everything** (text, tables, figures, references, appendices), so the category constrains the scope of the question.

## Fit test (answer all)

- [ ] Is the IT artifact central to the theory, not interchangeable?
- [ ] Which single tradition is primary, and what (if any) is the blend?
- [ ] Which category fits — and does the question's scope fit that page budget?
- [ ] What does an IS reader learn that they could not get from a top management, marketing, or CS venue?

## Anti-patterns

- A management/marketing study with IT as window dressing → wrong venue.
- A CS systems paper with no theory or no behavioral/economic/organizational evaluation → wrong venue (consider the Design Science track only if you build *and evaluate*).
- Picking a category after writing, then having an over-length manuscript returned.

## Output format

```
【IS question?】central IT artifact: yes/no — why
【Tradition】behavioral / design science / economics / organizational (+ blend)
【Category】Research Article / Research Notes / Theory Dev / Synthesis / Design Science / I&O
【Scope fits page budget?】yes / trim needed
【Next step】misq-theory-development
```
