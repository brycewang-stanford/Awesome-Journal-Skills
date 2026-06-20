---
name: respol-review-process
description: Use when calibrating expectations and choreography for the Research Policy (RP) review cycle — the double-blind process, the out-of-scope desk screen, handling-editor routing, the Research Note option, and what RP referees reward versus reject. Sets expectations; it does not draft the response letter (respol-rebuttal).
---

# Review Process (respol-review-process)

## When to trigger

- You want realistic odds and timelines before or after submitting to RP
- A desk reject arrived and you need to read whether it was scope, contribution, or fit
- You are deciding whether to position the work as a full article or a Research Note
- A decision letter arrived (reject / major / minor) and you need to plan, not yet write, the response
- You are weighing transfer to a sibling (ICC, Technovation, JPIM) after an RP rejection

## How Research Policy review actually works

RP runs a **double-blind** process (检索于 2026-06；以官网为准): the Editor-in-Chief routes a submission to a **Handling Editor** matched to its area (innovation systems, science/technology policy, entrepreneurship and innovation, university-industry interactions, R&D management, or innovation methodology), who manages the referees and the decision. Before referees, there is a **desk screen** that tests two things: whether the paper is genuinely innovation studies (the out-of-scope filter for econ/management-only papers) and whether the substantive contribution is plausible. Surviving that, expect a small number of expert referees and the standard reject / major-revision / minor-revision / accept ladder. Treat all timeline numbers as volatile and verify on the live journal pages (待核实).

## What RP referees reward vs. punish

| RP referees reward | RP referees punish / desk-reject |
|--------------------|----------------------------------|
| A genuine advance to innovation theory or evidence | Technique-as-contribution with no innovation-studies payoff |
| Construct-disciplined patent/bibliometric or mixed-methods work | "Patents = innovation" and black-box pipelines |
| A claim with an earned policy/managerial implication | A token "implications for policymakers" paragraph |
| Engagement with the RP/SPRU canon | A lit base that is "all economics or management journals" (out of scope) |
| Methodological pluralism fit to the question | A default design forced onto the wrong question |

## Reading the decision letter and planning the cycle

- **Desk reject (scope):** the literature/framing signaled the wrong audience. Re-anchor in innovation studies (→ `respol-topic-selection`, `respol-literature-positioning`) before any other venue.
- **Desk reject (contribution):** the so-what was not RP-grade. Sharpen the advance (→ `respol-contribution-framing`), or consider a sibling honestly.
- **Major revision:** the most common path to acceptance. Triage referee points into (a) must-fix identification/construct issues, (b) framing/positioning, (c) discretionary. Plan the analysis before drafting the letter.
- **Minor revision:** mostly exhibits, clarity, and framing — handle with `respol-tables-figures` / `respol-writing-style`.
- **Research Note pivot:** if the contribution is real but compact, the Note format (~3–5k words, with a justifying cover letter) may fit better than padding a thin full article.

## When to consider a sibling instead

- Firm performance / competitive advantage lens dominates → SMJ.
- Industrial dynamics / capabilities / evolutionary firm theory dominates → Industrial and Corporate Change.
- A managerial how-to or NPD-process study → Technovation / JPIM.
- A pure causal estimate with thin innovation theory → a field economics journal.

## Checklist

- [ ] Expectations set to RP's double-blind, handling-editor process (not a generic top-journal model)
- [ ] The desk-reject risk (scope vs. contribution) is correctly diagnosed
- [ ] Article-type choice (full vs. Research Note) is revisited against the contribution's size
- [ ] Referee points are triaged into must-fix / framing / discretionary before drafting
- [ ] A sibling-venue decision, if any, is made on substance, not just impact factor
- [ ] Timeline/odds claims are marked 待核实, not asserted as fixed

## Anti-patterns

- Treating an out-of-scope desk reject as a quality problem and resubmitting unchanged elsewhere
- Assuming RP timelines/acceptance rates from memory instead of verifying
- Padding a Note-sized contribution into a thin full article (or vice versa)
- Planning the rebuttal before triaging which referee points are binding
- Shopping the paper to a sibling without fixing the underlying framing

## Output format

```text
【Journal】Research Policy
【Skill】respol-review-process
【Stage】pre-submission / desk-reject / major / minor / planning-transfer
【Decision read】scope vs. contribution vs. fixable execution
【Article type revisit】full vs. Research Note
【Referee triage】must-fix / framing / discretionary
【Sibling option】RP-fixable or genuinely SMJ/ICC/Technovation/JPIM?
【Source status】timelines/odds verified or 待核实
【Next skill】respol-rebuttal
```
