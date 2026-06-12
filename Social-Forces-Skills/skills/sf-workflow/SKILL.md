---
name: sf-workflow
description: Use as the entry point for any Social Forces (SF) manuscript. Routes to the right SF sub-skill based on where you are in the lifecycle, keeping the paper aimed at a general social-science audience and inside the journal's reference-inclusive 10,000-word cap and 10-panel exhibit limit. It dispatches; it does not draft content.
---

# Social Forces Workflow Router (sf-workflow)

The orchestrator for a Social Forces submission. Figure out the stage, then send the user to the
matching skill. SF is a **general social-science** journal (centered on sociology, published by
**Oxford University Press** for **UNC Chapel Hill**) with a reputation for **methodological rigor**.
Two structural facts shape every routing decision: the **10,000-word cap includes the reference
list**, and exhibits are capped at **10 tables and figure panels**.

## When to trigger

- Starting a new SF paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Worried the paper reads as subfield-only rather than for a general social-science audience
- Returning with a decision letter (route to `sf-rebuttal`)

## First check: fit and format

| Situation | Route to |
|-----------|----------|
| Unsure the question matters beyond your subfield | `sf-topic-selection` |
| Strong subfield lit but no general-audience framing | `sf-literature-positioning` |
| A finding without a portable argument | `sf-theory-building` |
| Identification / case-selection / design worries | `sf-research-design` |
| Over 10,000 words **with references counted** | `sf-writing-style` (trim) |
| More than 10 tables and figure panels | `sf-tables-figures` (cut/consolidate) |

## Routing map (stage → skill)

```text
Idea / fit?                          → sf-topic-selection
Where does it sit in the field?      → sf-literature-positioning
What's the portable argument?        → sf-theory-building
Is the design defensible?            → sf-research-design
Are the analyses sound?              → sf-data-analysis
Are the exhibits within 10 panels?   → sf-tables-figures
Does it read for a general audience? → sf-writing-style
Data availability statement ready?   → sf-data-and-transparency
How will it be judged?               → sf-review-process
Ready to submit?                     → sf-submission
Got an R&R / decision?               → sf-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-building → research-design → data-analysis →
tables-figures → writing-style → data-and-transparency → review-process → submission → rebuttal`

Iterate: most SF papers loop theory ↔ design ↔ analysis several times, then spend real effort trimming
prose (references count!) and exhibits (10-panel cap) before writing-style and submission.

## Anti-patterns

- Treating SF like a narrow subfield outlet — it judges work by general social-science significance
- Forgetting that **references count** toward the 10,000-word cap until the final trim
- Letting exhibits drift past 10 panels and discovering it at submission
- Formatting to the ASA Style Guide or an AJS-style house format — SF uses **Chicago 17th author-date**

## Symptom-to-route shortcuts

When a user arrives mid-stream with a complaint rather than a stage, route on the symptom:

| User says | Likely real problem | Route to |
|-----------|---------------------|----------|
| "Reviewer called it descriptive" | Missing portable argument | `sf-theory-building` |
| "It's 1,500 words over" | References counted late | `sf-writing-style` |
| "Reviewer doubts the causal claim" | Identification gap | `sf-research-design` |
| "Feels too niche for SF" | General-significance gap | `sf-topic-selection` |

Worked vignette (illustrative): a user brings a clean networks analysis but a referee wrote "elegant
method, unclear social question." That is not a methods problem — route first to `sf-topic-selection`
and `sf-theory-building` to surface the substantive payoff, then back to `sf-tables-figures` to ration
the panels, only afterward to `sf-submission`.

## Router pass for Social Forces

Treat this skill as an executable review pass, not a prose hint. First lock the social mechanism, data scope, identification or interpretation, and contribution to a wider literature; then judge whether the current manuscript answers the venue's real reader: social-science reviewers who want generalizable social-process evidence across sociology, demography, and policy-adjacent topics.

- **Do the pass:** Run the pack as a sequence: fit gate, evidence gate, writing gate, source-map gate, and final output contract; stop when a gate lacks evidence.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against ASR/AJS for top sociology theory stakes, Demography for population process, JMF for family-specific claims; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Fit】general social-science significance clear? [Y/N]
【Format risk】words (incl. refs) ≤ 10,000? panels ≤ 10? [Y/N]
【Route to】sf-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — sociology data + software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Social Forces URLs behind every fact in this pack
