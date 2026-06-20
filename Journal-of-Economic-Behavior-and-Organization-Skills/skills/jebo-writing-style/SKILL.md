---
name: jebo-writing-style
description: Use when a Journal of Economic Behavior & Organization (JEBO) manuscript's prose buries the behavioral mechanism, or the abstract and introduction do not land for a pluralist behavioral audience. Shapes the mechanism-forward narrative and Elsevier-format front matter; it does not change the analysis.
---

# Writing Style (jebo-writing-style)

## When to trigger

- The abstract describes what you did but not what agents *do* or *why*
- The introduction reaches the behavioral mechanism only on page 4
- The paper reads as a method demonstration, not a behavioral finding
- Prose toggles between psychology jargon and econ jargon without serving either audience
- You are formatting the abstract/keywords/JEL and unsure of JEBO's limits

## The JEBO voice: mechanism-forward, audience-plural

JEBO readers span behavioral theorists, experimentalists, organizational economists, and evolutionary modelers. The prose must make the **behavioral mechanism** the protagonist and stay legible across those communities. Lead with the human behavior and its economic consequence; introduce method as the means, not the message.

A reliable intro arc for JEBO:

1. **The behavioral puzzle / regularity** (one paragraph): a way real agents deviate from the frictionless benchmark, and why it matters for markets, organizations, or institutions.
2. **What we did and the headline result** stated plainly and early (do not make the reader wait for the design section).
3. **The mechanism**: name the channel (image concern, loss aversion, reciprocity, learning, norm) and why this design isolates it.
4. **What it adds** to the specific literature (one sentence; see jebo-literature-positioning).
5. **Roadmap**, brief.

## Abstract: write the behavior, not the procedure

The abstract (**≤250 words**, 检索于 2026-06；以官网为准) should let a reader who skips the paper still learn the behavioral lesson. State the mechanism and the direction/size of the effect, not just "we run an experiment and find significant effects." Avoid undefined abbreviations and references in the abstract.

## Calibrating jargon for a plural audience

| Audience risk | Fix |
|---------------|-----|
| Psychology terms unfamiliar to economists | define on first use; tie to an economic primitive (preference/belief) |
| Game-theory notation that loses experimentalists | give the intuition before the formalism |
| Field-specific lab shorthand (e.g., "MPCR", "strategy method") | expand at first mention |
| Over-claiming external validity from a lab task | bound the claim to what the design supports |

## Front-matter mechanics (Elsevier / ScienceDirect; 检索于 2026-06)

- **Abstract ≤250 words**; **1–7 keywords**; **JEL classification codes** included.
- **References author-date (Elsevier Harvard)**: in-text "(Author, year)"; reference list "Author, Year. Title. Journal vol, pages." — sentence-case article titles, no quotation marks.
- **Declaration of competing interest** and **declaration of generative-AI use** per Elsevier policy.
- A **structured cover letter** is expected via Editorial Manager (see jebo-submission).
- Highlights / graphical abstract optional per Elsevier (待核实 — confirm current requirement).

## Checklist

- [ ] Abstract states the behavioral mechanism and the effect direction/size, ≤250 words, no undefined abbreviations
- [ ] The headline result appears in the first page of the intro, not after the design section
- [ ] The mechanism is named and tied to an economic primitive, legible across JEBO communities
- [ ] Jargon from any one tradition is defined for the others
- [ ] Keywords (1–7) + JEL codes present; references in author-date Elsevier Harvard
- [ ] Competing-interest and generative-AI declarations drafted
- [ ] Claims are bounded to what the design supports (no silent ATE/external-validity leaps)

## Anti-patterns

- An abstract that describes procedure ("we conduct three treatments") but never the behavior found
- Burying the headline behavioral result behind pages of design detail
- Writing for only one JEBO community and alienating the others
- Importing dense psychology or game-theory jargon without translation
- Significance-laden prose ("highly significant") instead of stating the mechanism and magnitude
- Inflating a single lab task into a general behavioral law

## Output format

```text
【Abstract】mechanism + effect direction/size stated? ≤250 words? [Y/N]
【Intro arc】puzzle → result-early → mechanism → contribution → roadmap [Y/N]
【Audience legibility】jargon defined across communities? [Y/N]
【Front matter】keywords(1–7) + JEL + author-date refs + AI/COI declarations [Y/N]
【Claim discipline】bounded to design? [Y/N]
【Next step】jebo-replication-package
```
