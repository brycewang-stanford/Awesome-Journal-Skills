---
name: wber-rebuttal
description: Use when a The World Bank Economic Review (WBER) decision letter has arrived (R&R or reject-with-encouragement) and you need the response-letter strategy — triaging editor vs. referee asks, sequencing new analysis, and writing point-by-point replies for the identification and policy referee archetypes. Plans the revision; it does not run the new analysis.
---

# Rebuttal Strategy (wber-rebuttal)

## When to trigger

- A WBER decision letter arrived (R&R, major/minor revision, or reject-with-encouragement)
- You need to triage which referee asks are deal-breakers vs. optional
- The two referees disagree, or one is identification-focused and the other policy-focused
- You are deciding what new analysis is worth running before resubmitting
- You need to draft the point-by-point response letter

## Read the letter through the WBER lens

WBER revisions almost always hit the journal's two-part bar: the **identification referee** wants the design hardened; the **policy referee** wants relevance, external validity, and cost. The editor's letter is the binding document — **the editor's synthesis outranks any single referee**, and the editor will signal which concerns are essential. Read the editor's framing first, then map each referee point to a referee archetype so your tone and evidence fit the reader. Single-anonymized review means the referees know who you are; engage them as informed colleagues, not adversaries.

## Triage every point

| Tier | What it is | How to handle |
|------|-----------|----------------|
| **Deal-breaker** | The editor or a referee flags it as essential (e.g., "the design is not credible as is") | Do the work fully; lead the response with it; show the new result in the paper |
| **Substantive** | A real concern short of fatal (a robustness gap, an external-validity question) | Address with new analysis or a clear argument; revise the text |
| **Framing** | "Reads like a project report," "clarify the contribution" | Reframe and rewrite; usually cheap, high-return |
| **Optional / misread** | A referee misunderstood, or asks for out-of-scope work | Clarify respectfully; push back with evidence, do not capitulate to scope creep |

Resolve referee disagreements by appealing to the **editor's synthesis** and to evidence — if Referee 1 wants a structural model and Referee 2 wants none, state which serves the paper's question and why, and let the editor's priorities adjudicate.

## Writing the response letter

- **Open with a short summary** of the main changes and the headline that survived.
- **Point-by-point, quote each comment**, then give: what you did, where in the revised paper, and the result.
- **Show numbers, not promises.** "We re-estimated with Callaway–Sant'Anna; the ATT is 4.1pp (s.e. 1.0), up from 3.8pp" beats "we addressed this."
- **Match tone to archetype.** For the identification referee, lead with the diagnostic and the robust estimate. For the policy referee, lead with external validity, scale-up, and cost.
- **Update the data/code package** to match the revised exhibits — WBER's release is a condition of publication, so the deposit must track the final results.
- **Be honest about trade-offs.** If a requested check weakens precision, report it and explain; do not hide it.
- **Respect the 40-page cap** when adding material — move secondary additions to the supplementary appendix.

## Sequencing the revision work

Order the work so the deal-breakers cannot sink the resubmission:

1. **Do the essential analysis first** — the design re-estimation or new evidence the editor flagged as binding. If it changes the headline, everything downstream (exhibits, abstract, model) must follow.
2. **Lock the revised result**, then rebuild exhibits and the data/code package against it.
3. **Rewrite the framing** — intro, contribution, external-validity — to match the new result.
4. **Draft the response letter last**, once you can report concrete numbers and locations.

Never write the response letter promising work you have not yet done; WBER editors and the same referees will re-read, and an unfulfilled promise reads worse than an honest "this check weakened precision, and here is why we still believe the result."

## Checklist

- [ ] Editor's letter read first; essential concerns identified and led with
- [ ] Every referee point triaged (deal-breaker / substantive / framing / optional) and answered
- [ ] Each response quotes the comment, states the change, the location, and the new number
- [ ] Identification asks answered with diagnostics + robust estimates
- [ ] Policy asks answered with external validity / scale-up / cost
- [ ] Referee disagreements resolved by appeal to the editor's synthesis + evidence
- [ ] Data/code package and DOI-linked DAS updated to the revised results
- [ ] Added material respects the 40-page cap; secondary content in the appendix

## Anti-patterns

- Responding to referees before parsing the editor's synthesis (the editor decides)
- "We thank the referee and have addressed this" with no specific change or number
- Capitulating to scope creep that would dilute the paper's question
- Answering the identification referee with policy prose, or vice versa
- Letting the revised paper drift over 40 pages with reactive additions
- Leaving the replication package stale relative to the new exhibits
- Treating single-anonymized referees as anonymous adversaries rather than informed colleagues

## Tone and the single-anonymized referee

WBER's single-anonymized review means the referees know who you are, but you do not know them — so write as if to a respected colleague, never as if scoring points. Thank substantive criticism genuinely, concede what is right, and push back only with evidence and a clear reason. When you disagree, frame it as "we considered this and here is why the alternative would not serve the question," not as a dismissal. Editors weigh the *tone* of a response: a defensive or evasive letter can sink a revision that the analysis would otherwise have saved.

## Worked vignette (illustrative)

A reject-with-encouragement letter says the editor likes the question but Referee 1 calls the TWFE design biased and Referee 2 says the result "won't generalize beyond three districts." Triage: both are deal-breakers. The team re-estimates with a heterogeneity-robust estimator (ATT now 4.1pp, s.e. 1.0, with flat pre-trend leads) and adds an external-validity section comparing the three districts to the national distribution plus a fiscal-cost-at-scale figure. The response letter leads with the editor's two priorities, quotes each referee, shows the new numbers and their locations, and notes the openICPSR-style package and DOI-linked DAS now match the revised tables. The paper stays at 39 pages by moving older specifications to the appendix.

## Output format

```text
【Decision】R&R / major / minor / reject-with-encouragement
【Editor's essential concerns】led-with items
【Triage】deal-breakers / substantive / framing / optional
【Identification responses】diagnostic + robust estimate + location
【Policy responses】external validity / scale-up / cost + location
【Disagreement resolution】how editor synthesis adjudicates
【Package updated】data/code + DOI DAS match revised exhibits? [Y/N]
【Page cap】revision ≤40 pages? [Y/N]
【Next step】resubmit via ScholarOne
```
