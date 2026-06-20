---
name: jimf-rebuttal
description: Use when a Journal of International Money and Finance (JIMF) decision letter has arrived and you need a response-letter strategy for an R&R or a reject-and-resubmit. Plans the revision and response; it does not pre-empt objections before submission (jimf-referee-strategy).
---

# Rebuttal Strategy (jimf-rebuttal)

## When to trigger

- A JIMF decision letter arrived: major/minor revision, reject-and-resubmit, or a transfer offer
- Two referees disagree (one wants more identification, one wants more policy relevance) and you must reconcile
- A referee demands a check you think is wrong, infeasible, or fishing
- You need to convert a long, mixed report into a prioritized, point-by-point response plan

## Reading the JIMF letter

The editor's letter is the contract, not the referee reports. Read the editor's framing first: which concerns they emphasize, whether they signal the contribution is valued, and what they require versus what is "the referee suggests." At an Elsevier field journal the editor's synthesis governs; a referee's pet request can be respectfully declined if the editor did not endorse it and you give a reason. Sort every comment into: **must-do** (editor-endorsed or design-critical), **should-do** (improves the paper, feasible), **push-back** (wrong, infeasible, or out of scope — answered with evidence), and **defer** (out of scope for this paper, acknowledged as future work).

## The response letter, JIMF-style

1. **Open with a summary of the main changes** — the two or three substantive things you did (e.g. cleaned the surprise for the information channel, added time FE, dropped the US and the GFC episode). Editors skim this first.
2. **Point-by-point, quoting each comment**, then your response, then the exact change with location ("new Table 4; Section 5.2, p. 18"). Never answer in prose that the referee must hunt through.
3. **Show, don't assert.** When a referee doubts robustness, add the table and report the number — "the spillover coefficient is 0.40 (s.e. 0.14) with the US excluded; see Appendix Table A6." A JIMF referee is convinced by the new exhibit, not by a promise.
4. **Disagree with evidence and courtesy.** If a requested check is wrong (e.g. clustering at a level that destroys identification), explain the econometrics and offer the defensible alternative; cite the methods literature.
5. **Reconcile divergent referees explicitly.** Tell the editor how you balanced a "more identification" demand against a "more policy" demand, so the editor sees a coherent revision rather than two half-answers.
6. **Track the international margin.** If a revision drifts the paper toward domestic territory, restate why it remains a JIMF contribution.

## Handling the common JIMF revision demands

| Referee demand | The convincing response |
|----------------|--------------------------|
| "Rule out the global financial cycle" | Add time FE so within-time variation identifies; report the surviving coefficient as a new table |
| "Your surprise is contaminated" | Re-purge the surprise (information-channel correction) and show the before/after |
| "Drop the US / the crisis / use NEER" | Run all three; report point-estimate stability, not just significance |
| "Fix the inference" | Re-estimate with two-way / Driscoll–Kraay / wild bootstrap; report the new SEs |
| "Add policy relevance" | Translate the estimate into a bounded counterfactual (bp of spread, % of GDP of flows) |
| "Extend the country sample / period" | Add it if feasible; if data are restricted, say so honestly and show the sub-sample is representative |

Most JIMF revisions are won on the empirical layer, not the prose: a new exhibit with a number settles a dispute that paragraphs cannot.

## Checklist

- [ ] Editor's letter parsed first; must-do vs. referee-only requests separated
- [ ] Every comment sorted: must-do / should-do / push-back / defer
- [ ] Response is point-by-point, each comment quoted, each change located by section/table/page
- [ ] Robustness/identification demands answered with new exhibits and numbers, not assertions
- [ ] Push-backs argued with methods evidence and a courteous tone, not refusals
- [ ] Divergent referees explicitly reconciled for the editor
- [ ] The international contribution restated if the revision risked domestic drift
- [ ] Push-backs offer a defensible alternative with a number, not a flat refusal
- [ ] Scope creep across rounds resisted; the paper's core contribution stays coherent
- [ ] A summary-of-changes paragraph leads the letter

## Anti-patterns

- Treating every referee sentence as mandatory and over-revising into incoherence
- Answering a robustness demand with prose ("we believe the result is robust") instead of the new table
- Refusing a check flatly without an econometric reason or an alternative
- Ignoring the editor's framing and responding only to the referees
- Leaving two divergent referees unreconciled, so the editor sees a contradictory revision
- Letting the revision quietly become a domestic paper while still claiming a JIMF contribution
- Silent changes the referee cannot locate in the manuscript

## The summary-of-changes paragraph (write it first)

The editor reads the opening paragraph of the response before anything else; make it carry the revision. State the two or three substantive changes in plain terms — "we now (i) purge the central-bank information component from the surprise, (ii) add time fixed effects so identification comes from cross-country exposure, and (iii) translate the estimate into basis points of EM spread under a tightening cycle" — and note that the headline result is unchanged (or, honestly, how it changed). A clear summary tells the editor the paper responded seriously before they reach the point-by-point detail, and it frames how every later response should be read.

## Worked vignette (illustrative)

Referee 1 calls the spillover result "the global financial cycle in disguise"; Referee 2 wants "more for policymakers." The plan: (must-do) add time fixed effects and the openness interaction so within-time variation identifies, killing the GFCy objection, and report the surviving coefficient; (should-do) add a counterfactual that translates the estimate into basis points of EM spread under a tightening cycle, serving Referee 2; (reconcile) tell the editor that the identification fix and the policy translation are the same exhibit viewed two ways. The summary paragraph leads with these two changes.

## When to push back, and how

Not every referee request improves the paper, and a JIMF editor respects a reasoned disagreement. Push back when a check is econometrically wrong (e.g. clustering at a level that mechanically destroys identification), when it is out of scope (a different paper), or when it rests on a misunderstanding you can correct. The form: acknowledge the concern, explain the econometrics or the scope with a citation, offer the *defensible alternative* you ran instead, and report its result. "We agree cross-country dependence matters; clustering by region as suggested leaves only four clusters, so instead we report Driscoll–Kraay standard errors (new Table A7), which are robust to both serial and cross-sectional dependence; the coefficient is unchanged." A push-back backed by a number and a method reads as competence; a flat refusal reads as defensiveness.

## Managing the revision timeline and scope creep

Major revisions at field journals can accumulate requests across rounds. Protect the paper's coherence: implement the must-do changes fully, batch the should-do changes so they do not fragment the argument, and resist letting each round add a section that dilutes the contribution. If two rounds of referee requests are pulling the paper toward a different question, raise it with the editor rather than silently complying — a coherent paper that answers the editor's core concern beats an incoherent one that answers every sentence.

## Output format

```text
【Journal】Journal of International Money and Finance
【Skill】jimf-rebuttal
【Decision】major / minor / reject-and-resubmit / transfer
【Editor's emphasis】<what the editor required vs. referee-only>
【Comment triage】must-do / should-do / push-back / defer (counts)
【Evidence added】new exhibits answering the lethal comments
【Referee reconciliation】how divergent demands were balanced
【International margin】restated if revision risked domestic drift? [Y/N]
【Deliverable】point-by-point response letter + revised manuscript
```
