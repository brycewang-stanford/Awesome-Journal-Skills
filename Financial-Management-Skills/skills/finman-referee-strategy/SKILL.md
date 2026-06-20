---
name: finman-referee-strategy
description: Use when pre-empting the objections a Financial Management (FM) referee is likely to raise, before pressing submit — red-teaming the paper from the perspective of an applied-finance reviewer who weighs relevance, rigor, and the "so-what." Anticipates pushback; it does not run the submission preflight (finman-submission) or draft a response to an actual report (finman-rebuttal).
---

# Referee Strategy (finman-referee-strategy)

## When to trigger

- The paper feels finished and you want to find the holes before a referee does
- You suspect a reviewer will call it "incremental," "a specialist paper," or "rigorous but not interesting"
- The identification or sample has a known soft spot you have not yet addressed in the text
- You want to write a cover letter that frames the contribution and pre-empts the obvious objections

## How FM referees read a paper

An FM referee is an applied-finance academic evaluating against the journal's five criteria — **originality, rigor, timeliness, practical relevance, quality** — and against the brand of papers "people actually read." With **300+ submissions a year and a sub-10% acceptance rate**, the default disposition is rejection, and the fastest paths to it are: *not interesting enough for a general audience*, *belongs in a specialist journal*, *identification not credible*, or *no clear so-what*. Notably, because FM **under-weights trivial robustness**, "you didn't run check X" is rarely fatal unless X addresses a real alternative explanation — so do not over-insure against busywork objections; insure against the four that actually sink papers here. The editors aim for a **median 6–8 week turnaround**, so reports tend to be focused; a paper that telegraphs its contribution and pre-empts the live concerns reads as ready.

## Red-team the four FM-fatal objections

| Likely objection | Pre-empt it by |
|------------------|----------------|
| "Not interesting / too narrow for a general audience" | sharpen the general-interest framing and the debate it furthers (`finman-topic-selection`, `finman-writing-style`) |
| "This belongs in JCF / JFQA / JBF" | answer the substitution question inside the intro (`finman-literature-positioning`) |
| "Identification is not credible" | show the design, leads, and the one check that defuses the leading alternative (`finman-identification`, `finman-robustness`) |
| "No clear practical implication" | state an explicit managerial/market so-what with the economic magnitude (`finman-writing-style`) |

## The cover letter as a framing instrument

At FM the cover letter does targeted work: it is the editor's first read on fit and interest, before any referee. Keep it short and make it earn its place:

- **One paragraph on the contribution and the general-interest hook** — what the paper shows and why a broad finance audience cares.
- **One sentence pre-empting the substitution question** — why FM rather than a specialist sibling.
- **Honest scope** — do not oversell to frontier-defining; FM editors discount inflated cover letters fast.
- **Logistics** — confirm exclusivity (not under review elsewhere) and any disclosures.
A cover letter that argues with imagined referees, rather than framing the value, signals defensiveness before the paper is even read.

## Building the defense before submission

1. **Write the three reports a hostile referee would write.** Force yourself to articulate the strongest version of each fatal objection; weak self-critique misses the real holes.
2. **Fix what is cheap and decisive in the paper now** — a flat pre-trend plot, an Oster bound, a magnitude statement — rather than promising it in a cover letter.
3. **Pre-empt in the text, not the cover letter.** Address the substitution and credibility concerns where the referee reads, so they never become a report.
4. **Use the cover letter to frame, not to plead.** State the contribution, the general-interest hook, and (if relevant) why FM over a sibling — briefly. (Whether review is single- or double-blind, and how to anonymize, is 待核实 — confirm in the Wiley/FMA guidelines before naming yourself in the cover materials.)
5. **Suggest appropriate reviewers honestly.** If the system invites suggestions, name scholars who span FM's general-interest breadth, not just your subfield allies.

## Checklist

- [ ] The four FM-fatal objections are each written out as a hostile referee would
- [ ] The "too narrow / not interesting" objection is pre-empted in the framing
- [ ] The substitution objection ("belongs in a specialist journal") is answered in the intro
- [ ] The credibility objection is met with the design plus the one decisive check
- [ ] An explicit practical implication with economic magnitude is present
- [ ] Cheap, decisive fixes are in the paper, not deferred to the cover letter
- [ ] Blinding/anonymization requirements verified or marked 待核实

## Anti-patterns

- Over-insuring against trivial-robustness objections FM does not weight, while leaving a fatal one open
- A defensive cover letter that argues with objections instead of pre-empting them in the text
- Assuming the referee shares your subfield context — they read as a general finance reviewer
- Suggesting only friendly, narrow reviewers from your immediate niche
- Naming yourself in cover materials before confirming the blinding model

## What FM's fast process implies for strategy

FM advertises a **median 6–8 week turnaround including desk rejections**, and the editors commit to explanatory feedback on every submission. Two strategic implications:

- **Desk-reject risk is real and quick.** A paper that does not pass the interest/fit screen on the first page can be returned in days. Front-load the contribution and the general-interest hook so a co-editor skimming the intro sees the value immediately.
- **Reports are focused, not exhaustive.** A short, fast review tends to zero in on the one or two things that would sink the paper. Pre-empting the four fatal objections matters more than covering every conceivable minor point — and means you should not pad the paper trying to anticipate trivial requests.
- **Feedback even on rejection is usable.** If desk-rejected, the explanatory note is a free read on whether the problem is fit (re-target) or execution (revise) before you spend a second fee.

## Worked vignette (illustrative)

A near-final paper on bank loan pricing is strong on data but the author worries about robustness coverage. The red-team reveals the real risk is not robustness — it is "this is a banking paper for JBF." The FM move: add a paragraph to the intro showing the information-frictions mechanism generalizes beyond banks, lead the abstract with that general-interest implication, and state the magnitude in basis points a lending officer would recognize. The substitution objection is now defused in the text, and the author wisely does *not* add three more robustness tables that FM would discount anyway.

## Referee pushback mapped to the pre-emption

- *"Why is this in FM and not a specialist journal?"* → Add the general-interest implication and the substitution answer to the intro before submitting.
- *"Rigorous, but I'm not sure it's interesting."* → Sharpen the hook and the debate the finding furthers; this is a framing fix, not a robustness fix.
- *"The identification doesn't convince me."* → Bring the design, the flat pre-trends, and the one decisive check into the main paper.
- *"I don't see the practical payoff."* → State the managerial/market implication with the economic magnitude in a unit the decision-maker uses.

## Output format

```
【Hostile reports】three strongest objections written out? [Y/N]
【Too-narrow risk】general-interest framing sharpened? [Y/N]
【Substitution risk】"why FM not the sibling" answered in intro? [Y/N]
【Credibility risk】design + one decisive check in place? [Y/N]
【So-what】explicit practical implication + magnitude? [Y/N]
【Blinding】single/double-blind + anonymization verified or 待核实
【Next skill】finman-submission
```
