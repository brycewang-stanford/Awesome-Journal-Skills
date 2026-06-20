---
name: jams-topic-selection
description: Use when choosing or sharpening the research question for a Journal of the Academy of Marketing Science (JAMS) manuscript — confirming it is a broad, managerially consequential marketing-science question and routing it away from sibling marketing journals. Frames the question; it does not build the theory (jams-theory-development) or run the analysis.
---

# Topic Selection (jams-topic-selection)

## When to trigger

- You have a marketing finding or dataset but no crisp, JAMS-sized question
- A coauthor asks "is this a JAMS paper, or does it belong at JM / JMR / Marketing Science / JCR?"
- The question feels narrow, niche, or like a single-context replication
- You can state a method but not the **marketing decision** the answer would change

## What a JAMS question looks like

JAMS is the **Academy of Marketing Science** flagship and the discipline's broad marketing-science outlet. A JAMS-grade question has three properties at once:

1. **Substantive and broad.** It speaks to one of JAMS's core domains — marketing strategy and firm performance, B2B/industrial marketing, services, retailing and channels, sales-force management, branding, innovation/NPD, the marketing–finance interface, sustainability/stakeholder marketing, or consumer behavior — not a hyper-local curiosity.
2. **Theoretically generative.** It promises a *mechanism or framework*, not just a correlation. JAMS rewards papers that explain **why** a marketing relationship holds and **when** it reverses.
3. **Managerially consequential.** A real decision maker (CMO, brand manager, sales VP, channel partner, policy maker) would act differently if the answer came out one way vs. another. This managerial stake is JAMS's signature, not a courtesy paragraph.

If you can only satisfy two of the three, the question is not yet a JAMS question. A broad + managerial question with no theory is consulting; a theory + broad question with no managerial edge drifts toward the modeling or consumer-theory siblings.

## Route it against the siblings before committing

| If the paper's center of gravity is… | The better home is… | JAMS keeps it when… |
|---|---|---|
| Strategy / managerial thought-leadership, big substantive impact | **Journal of Marketing (JM)** | the contribution is a measurement-rich framework with strong method, broad marketing-science fit |
| A methods/measurement advance or a clean identification result | **Journal of Marketing Research (JMR)** | method serves a substantive marketing mechanism, not vice versa |
| An analytical/quant model, equilibrium, or estimation method | **Marketing Science** | the work is empirical with a managerial framework, not modeling-first |
| Consumer psychology / interpretive consumer theory for its own sake | **Journal of Consumer Research (JCR)** | consumer insight is embedded in a broader marketing-strategy/managerial question |

JAMS's sweet spot is the broad marketing-science question with **construct-based theory, strong empirics, and an explicit manager takeaway** — the union the siblings each cover only partly.

## Sharpen the question

- Write the question as one sentence: "Does/How does [marketing construct X] affect [outcome Y] for [unit], and under what conditions?"
- Name the **outcome managers care about** in managerial units (sales, share, CLV, margin, retention, brand equity, firm value).
- Name the **moderators/boundary conditions** that make it a contingency story, not a main effect.
- Identify the **JAMS audience segment** that would champion it — and the one that would desk-reject it as out of scope or incremental.

## Stress-test the question before you commit months to it

- **The reversal test.** Could the relationship plausibly go the other way, or flip under a condition? If both directions are defensible, you have a genuine empirical question; if the answer is obvious, the contribution is thin.
- **The "imagine the result" test.** Sketch the headline finding as if it were already in. Does it change a marketing decision? If neither outcome would alter what a manager does, the question lacks managerial stake.
- **The generalizability test.** Does the answer travel beyond the one dataset/context, or is it bound to a single firm's idiosyncrasy? JAMS wants insight that generalizes across the marketing-science domain.
- **The feasibility test.** Can you actually measure the focal constructs validly and identify the effect with the data you can get? A great question you cannot execute is a dead end — check this with `jams-methods` early.

## Anchor the question to a JAMS domain explicitly

JAMS is broad but not boundless. Before committing, name which core domain your question sits in — marketing strategy and performance, B2B/industrial marketing, services, retailing/channels, sales-force management, branding, innovation/NPD, the marketing–finance interface, sustainability/stakeholder marketing, or consumer behavior — and confirm the question advances that domain's conversation. A question that cannot be filed under a JAMS domain is a fit risk; a question that sits squarely in one but ignores its recent literature reads as incremental. The strongest JAMS questions sit at the **intersection of two domains** (e.g., branding × marketing–finance, services × innovation), where a contingency or mechanism has not yet been worked out.

## Phenomenon-first vs. theory-first entry

A JAMS question can originate two ways, and both are legitimate so long as the destination is the same broad, theory-generative, managerial question:

- **Phenomenon-first:** you notice a real, consequential marketing pattern (a pricing response, a channel shift, a brand reversal, a sales-allocation puzzle) and ask why it happens. This often yields the most managerially vivid JAMS papers, but you must still build the theory to explain the pattern (hand off to `jams-theory-development`) rather than report it.
- **Theory-first:** you start from a marketing-theory tension or an untested boundary condition and design a study to resolve it. Cleaner theoretically, but verify it has a real managerial stake before committing.

Either way, the deliverable from this stage is a *question*, not a finding — declare which entry you took so the framework you build next is honest.

## Checklist

- [ ] One-sentence question with construct, outcome, unit, and conditions
- [ ] All three properties present: broad marketing-science, theory-generative, managerially consequential
- [ ] Outcome expressible in a managerial unit
- [ ] Sibling routing decided explicitly (why JAMS, not JM/JMR/MktSci/JCR)
- [ ] At least one boundary condition / moderator identified
- [ ] The paper is not a single-context replication dressed up as new
- [ ] The question survives the reversal, imagine-the-result, generalizability, and feasibility tests

## Anti-patterns

- A narrow, single-industry curiosity with no broad marketing-science reach
- A method or model looking for an application (route to JMR / Marketing Science instead)
- "Managers should pay attention to X" with no decision a manager would change
- A main-effect-only question with no contingency or mechanism
- New-context replication ("X, but in country/industry/platform Z") framed as novelty

## Output format

```text
【Journal】Journal of the Academy of Marketing Science (JAMS)
【Question】one sentence: construct → outcome (managerial unit), conditions
【Three-property check】broad✓/theory✓/managerial✓ or the missing one
【Why JAMS not sibling】JM / JMR / MktSci / JCR boundary reasoned
【Audience champion vs. desk-reject risk】[...]
【Source status】verified / 待核实 / 检索于 2026-06
【Next skill】jams-theory-development
```
