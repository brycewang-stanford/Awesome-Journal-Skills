---
name: jais-topic-selection
description: Use when deciding whether a question fits the Journal of the Association for Information Systems (JAIS) and which of its seven manuscript categories to target. Locks the IS phenomenon, the unit of analysis, and the category before theory work begins; it does not build the theory (jais-theory-development) or invent citations.
---

# Topic & Category Selection (jais-topic-selection)

## When to trigger

- You have an interesting IS finding or idea but are unsure JAIS (vs. MISQ / ISR / JMIS) is the right home
- You cannot say in one sentence what the **information-technology artifact or digital phenomenon** is doing in the paper
- You are unsure whether to enter as a Research Article, a standalone Theory paper, a Literature Review, a Research Perspective, Foundational Research, or Policy and Impact
- A coauthor wants a "JAIS-grade" question but the draft reads like a generic management or CS paper

## First: is this a JAIS question at all?

JAIS rewards work where **information systems / digital technology is theoretically load-bearing**, not decorative. The about page describes JAIS as "inclusive in topics, level and unit of analysis, theory, method and philosophical and research approach" and says it "encourages theory based multi- or inter-disciplinary research" (检索于 2026-06；以官网为准). That pluralism is genuine — but it is theory-gated. A descriptive industry report or a pure machine-learning benchmark with no IS theory is a desk-reject regardless of execution quality. Ask: *would an IS scholar in a different sub-tradition still learn something general about technology, organizations, or people from this?*

## Then: pick the right JAIS category (this is the move siblings do not force)

JAIS's distinctive feature is that **theory and review are first-class submission types**, not afterthoughts. Choose deliberately — the category sets the bar your reviewers apply.

| Category (Senior Editor 待核实) | Choose it when… | The bar it sets |
|--------------------------------|-----------------|-----------------|
| **Research Articles** | empirical, modeling, or design work testing/building theory; *primary construct development is discouraged here* | a rigorous, theory-grounded empirical or design contribution |
| **Theory** | the contribution *is* the theory — a new construct, a novel framework, or a novel integration of existing theories | original, generative theory about a novel IS/digital topic |
| **Literature Reviews** (SE Gregory Vial) | a structured synthesis that opens new directions, **or** theory development through review | a method-driven review with a forward-looking theoretical payoff |
| **Research Perspectives** (SE Dirk Hovorka, ~10,000 words) | you are questioning assumptions, critiquing the field, offering constructive guidance | a defensible, generative argument about the discipline |
| **Foundational Research on Novel Digital Phenomena** (SE Varun Grover) | a genuinely new digital phenomenon nobody has studied yet | disciplined description that yields new or *pre-theoretical* insight |
| **Editorials** (6,000–8,000 words) | typically invited commentary on gaps/practices | usually invited — confirm before targeting |
| **Policy and Impact** (SE Roman Beck, 5,000–7,000 words) | theorizing how IS research translates into policy | a credible research-to-policy bridge |

## Scope the length to the category

Most empirical/theory/review/foundational papers should stay under **~15,000 words** — beyond that "are very likely to receive extra scrutiny from the editors and may be returned to be shortened," and **manuscripts over 65 pages including everything will not be sent out for review** (检索于 2026-06；以官网为准). Decide the category *and* its budget now, before you over-build.

## Confirm the IT artifact is theoretically load-bearing

JAIS's inclusiveness is often misread as "anything touching technology fits." It does not. The test is whether the information-technology artifact or digital phenomenon is *doing theoretical work* — whether removing it would collapse the contribution. A study where IT is merely the setting (e.g., "we surveyed employees who happen to use software") is not a JAIS topic no matter how clean the data; a study where a specific affordance of the technology drives the mechanism is. Run this test before committing: name the artifact, then ask what the paper would lose if you swapped it for a non-technological equivalent. If the answer is "nothing," reshape the topic before choosing a category.

## The "why JAIS, not the sibling" test, made concrete

The single most useful pre-submission discipline is answering "why JAIS?" against each near neighbor, because a wrong answer predicts a fit desk-reject. Use this map.

| If a reviewer says it reads like… | The real home might be… | The JAIS-defending move |
|-----------------------------------|-------------------------|--------------------------|
| a hard causal identification result with thin theory | ISR (INFORMS) | foreground the theoretical/conceptual payoff; consider Theory or Research Article with theory first |
| a polished IT-artifact build with light theory | MISQ (design-science identity) | sharpen the generalizable design knowledge; lean into JAIS's theory framing |
| an applied systems/economic-modeling study | JMIS | show the cross-disciplinary theoretical contribution, not just the model |
| a broad management/OR study not about IS | Management Science | confirm the IT artifact is load-bearing, or reroute |
| a literature summary with no forward theory | a review outlet without JAIS's two-genre bar | add method + theoretical destination (Literature Review category) |

If you cannot win the "why JAIS" argument for *any* category, the topic is not yet a JAIS topic — fix that before writing.

## Worked vignette: routing the same study to different categories (illustrative)

Suppose a team has rich field data on how a new decentralized-finance protocol changed lending behavior. The *same evidence* could anchor three different JAIS submissions, and the category choice changes everything downstream. As a **Research Article**, the payoff is a theory-tested empirical result about IT-enabled disintermediation — reviewers will demand identification and validity. As **Foundational Research on Novel Digital Phenomena**, the payoff is the first disciplined account of a genuinely new phenomenon, and over-theorizing too early would be a flaw; reviewers reward careful description and pre-theoretical insight. As a **Theory** paper, the data recede and a new construct (say, "algorithmic trust substitution") plus its nomological net becomes the contribution. Pick before you write: each route has a different Senior Editor, bar, and length budget.

## Checklist

- [ ] The IT artifact / digital phenomenon is load-bearing, not a context decoration
- [ ] The paper teaches something general to IS scholars outside its own sub-tradition (the multi/inter-disciplinary test)
- [ ] One JAIS category is chosen on purpose, and the contribution matches that category's bar
- [ ] If a Research Article: the contribution is not merely "we developed a new construct" (discouraged there — consider Theory)
- [ ] The unit/level of analysis (individual, group, firm, network, society) is named
- [ ] Length budget fits the category (≤~15k typical; ≤65pp absolute)
- [ ] The reason this is JAIS and not MISQ/ISR/JMIS can be stated in one sentence
- [ ] Swapping the IT artifact for a non-technological equivalent would break the contribution (the load-bearing test)
- [ ] Volatile category facts (SE names, word budgets) are treated as 待核实 against the live author page

## Anti-patterns

- Sending an atheoretical phenomenon report to a category that expects theory.
- Picking "Research Article" for a paper whose whole point is a new construct (JAIS discourages primary construct development there; the Theory category fits better).
- Choosing JAIS because it is "easier than MISQ" — fit, not perceived selectivity, drives the routing.
- Defaulting to the catch-all Research Article when Theory, Foundational, or Perspectives is the true genre.
- Naming no unit of analysis, so reviewers cannot tell what the claim is about.

## Output format

```text
【Journal】Journal of the Association for Information Systems (JAIS)
【IS phenomenon / artifact】one sentence; why technology is load-bearing
【Category】Research Article / Theory / Literature Review / Research Perspectives / Foundational / Editorial / Policy and Impact
【Unit/level of analysis】individual / group / firm / network / society
【Length budget】≤~15k words (or category-specific); ≤65pp absolute
【Why JAIS not MISQ/ISR/JMIS】one sentence
【Source status】verified URL / 待核实
【Next skill】jais-theory-development
```
