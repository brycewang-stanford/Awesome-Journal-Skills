---
name: jru-rebuttal
description: Use when a Journal of Risk and Uncertainty (JRU) decision letter has arrived and you need a response-letter strategy. Triages referee reports into a revision plan and reply; it does not invent evidence or citations.
---

# Rebuttal Strategy (jru-rebuttal)

## When to trigger

- A JRU decision arrived (R&R, major/minor revision, or reject-and-resubmit) and the team needs a response plan
- Referees disagree — one wants more theory, another wants more robustness — and you must reconcile them
- A report rests on a misreading and you must correct it without sounding defensive
- A requested analysis (a new elicitation, a robustness re-estimate) is large and you must scope what is feasible

## How JRU decisions work and how to read them

JRU's referees are specialists, so a report usually contains a few **deep, technical** objections rather than many shallow ones — and the editor (W. Kip Viscusi) weights the substantive decision-theoretic or measurement concerns heavily. Triage before drafting:

| Comment type | Response move |
|--------------|---------------|
| Goes to the headline primitive (representation, identification, key parameter) | Address fully and first — new analysis if needed; this decides the paper |
| A specialist's standard demand (separate u from w; selection probe; second elicitation device) | Run it; report the result even if it slightly moves the estimate |
| Misreading of the model or the design | Correct precisely, quote the text, and add a clarifying sentence to the paper so the next reader does not misread |
| Disagreement between referees | Make the editor's job easy: state the tradeoff, choose, justify, and note you have satisfied the binding concern |
| Scope expansion beyond the paper | Decline gracefully with a reason; offer a smaller version if it strengthens the core |

## Building the response

1. Open with a brief, genuine summary of what changed and where the headline result now stands (did the parameter move? by how much?).
2. Reproduce each comment verbatim, then respond point-by-point; quote the **revised** manuscript text and give line/section pointers.
3. For every "the model could be X / the estimate is fragile" comment, show the new analysis and whether the **sign and rough magnitude** of the primitive survived (route through `jru-robustness` / `jru-identification` for the actual work).
4. Be candid where a concern is right: narrow the claim rather than defending an overreach — JRU referees reward calibrated claims.
5. Keep the tone collegial and technical; the reviewers are peers in a small specialized field.

## Handling the recurring JRU objections in a reply

The same specialist objections that `jru-referee-strategy` wargames tend to reappear in reports; each has a response pattern that lands well at this journal:

- **"The representation is unfalsifiable / the reference point is fit."** Show the revised model fixes the reference point a priori and name the choice pattern it now forbids — do not argue the point in the abstract, demonstrate it in the text.
- **"The elicitation is not incentive-compatible."** Either add the second device that replicates the parameter, or state the IC assumptions and bound the bias; concede if the mechanism truly presumes EU and the agents are non-EU.
- **"EU with a pessimistic belief explains this."** Report the discriminating comparative static and the new belief-controlled estimate.
- **"Functional form drives the number."** Point to the expanded robustness table and report the across-form stability in the letter, with the actual range of estimates.

## Scoping a major revision

- Triage requested analyses into *decisive* (changes the verdict), *strengthening* (worth doing), and *scope-creep* (decline with reason).
- For a large new elicitation or estimation, state in the letter what you ran, the N or sample, and the result — editors at a specialist journal read methods carefully.
- If two referees pull in opposite directions, do not split the difference silently; name the tradeoff and justify the choice so the editor can adjudicate.

## Checklist

- [ ] Every referee point is reproduced and answered individually
- [ ] The comments touching the headline primitive are addressed first and in full
- [ ] New analyses report whether the sign/magnitude of the key parameter held
- [ ] Misreadings are corrected by quoting revised text, not just asserting the referee was wrong
- [ ] Referee disagreements are reconciled with an explicit, justified choice for the editor
- [ ] Claims are narrowed where the evidence demands it (no defensive overreach)
- [ ] The response letter points to specific revised sections/lines

## Structure of the response document

A response letter that an editor can adjudicate quickly has a predictable shape:

- A one-page **summary of changes** at the top: the headline result's new status, the major new analyses, and where the parameter landed.
- Then a **per-referee section**, each comment quoted in italics and answered immediately below, with a pointer to the revised text ("see Section 4.2, lines X–Y").
- A short **closing** noting any concern you could not fully resolve and why, so the editor is not surprised by the limitations paragraph in the paper.

Number the responses to match the referees' own numbering; referees re-reading the paper want to find their point fast.

## Anti-patterns

- Arguing with a referee instead of either fixing the paper or conceding cleanly
- Answering the easy comments fully and the headline objection vaguely
- Claiming a robustness check "confirms" the result when it actually shifted the estimate — report the shift
- Adding every requested analysis without a coherent story, bloating the paper
- A defensive tone in a small specialist field where the referee may review the paper again

## Worked vignette (illustrative)

A referee writes: "Your ambiguity result is indistinguishable from risk aversion with pessimistic beliefs." Rather than argue, the response adds an independent belief-elicitation and a treatment that varies ambiguity at fixed risk, shows the ambiguity premium persists once beliefs are controlled, and revises the identification section to state this explicitly. The letter reports that α moved modestly (illustrative 0.62 → 0.58) but the qualitative claim is unchanged — a candid, calibrated reply the editor can act on.

## Output format

```text
【Journal】Journal of Risk and Uncertainty
【Skill】jru-rebuttal
【Decision】R&R / major / minor / reject-and-resubmit
【Headline-primitive comments】<list> → addressed first
【New analyses】parameter sign/magnitude held? [Y/N + numbers]
【Misreadings corrected】by quoting revised text [Y/N]
【Referee disagreement】reconciled choice for the editor
【Claims narrowed where needed】[Y/N]
【Next step】re-run jru-robustness / jru-identification for new analyses, then jru-submission to resubmit
```
