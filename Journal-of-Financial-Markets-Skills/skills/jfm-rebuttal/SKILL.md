---
name: jfm-rebuttal
description: Use when drafting the response to an R&R or referee report for a Journal of Financial Markets (JFM) manuscript — turning microstructure objections into a point-by-point response and a revised draft. Plans and drafts the rebuttal; it does not invent evidence or citations.
---

# Rebuttal Strategy (jfm-rebuttal)

## When to trigger

- A JFM decision letter (R&R or reject-and-resubmit) has arrived and a response letter is due
- The referee asks for new microstructure analysis (alternative measures, a placebo, a subsample) and you must plan it
- You disagree with a comment and need to push back without antagonizing the referee
- Comments conflict across referees and the editor must be asked to adjudicate
- The revision risks ballooning and you need to keep it inside the editor's real decision rule

## Structuring the JFM response

The response letter is read by busy specialists; make compliance **visible and verifiable**. The governing principle: do the work, then make it effortless to see you did it.

1. **Open with a short summary** of the main changes and the headline result's stability ("the X-bps effect is unchanged after the requested checks").
2. **Reproduce every comment verbatim**, numbered by referee, each followed by a concise response and a pointer to the exact revised location ("new Table 5, p. 14; Internet Appendix Table IA.3").
3. **Lead with the fatal-if-true comments** the editor flagged (from `jfm-referee-strategy`), then the rest in order.
4. **For new analysis**, state what you ran, the result, and whether the headline survives — show the number, not just "we addressed this."
5. **For push-backs**, concede the framing, then give the microstructure evidence. "The referee is right to worry about endogeneity; the tick-size shock is exogenous to firm fundamentals because …" beats a flat refusal.
6. **For conflicting referees**, name the conflict and ask the editor for guidance rather than silently siding with one.

## Microstructure-specific moves that win R&Rs

- **Measurement-artifact comment** → add the alternative liquidity/impact construct and show the effect holds; this is the single most common JFM ask.
- **Endogeneity comment** → strengthen the design (find/justify the exogenous market-structure variation) rather than adding controls.
- **Inference comment** → re-report with two-way clustering / NW and state it; usually cheap and fully closes the point.
- **"Not microstructure enough"** → sharpen the mechanism framing and add the heterogeneity exhibit showing the effect where the trading-process theory predicts.
- **Generalizability** → add an asset class / venue / period, or scope the claim honestly; do not over-promise.

## Documenting result stability across the revision

Because most JFM revisions add measurement and inference checks, the headline number often shifts slightly. Get ahead of this: maintain a small table (for yourself, and summarized in the letter) showing the headline coefficient under the original and each newly requested specification, so the reader sees the result is stable rather than wondering why a number changed between rounds. If a check does move the estimate materially, explain why in microstructure terms rather than burying it — a transparent "the effect attenuates to X bps once we use realized spreads, consistent with [reason]" is far stronger than a silent change a referee notices.

## Worked response entry (illustrative)

> **Referee 2, Comment 3:** "The spread effect may simply reflect the alternative liquidity measure chosen."
>
> *Response:* We thank the referee for raising this. We now re-estimate the main result using quoted, effective, and realized spreads and the Amihud measure (new Table 4, columns 2-5; full battery in Internet Appendix Table IA.3). The effect ranges from 9 to 14 bps across all four constructs and remains significant at the 1% level, so it is not an artifact of any single measure. We added a sentence to Section 4.2 (p. 15) noting this.

This entry reproduces the comment, names the new analysis, gives the actual numbers and their stability, and points to exact locations. It does not say "we addressed this" — it shows it.

## Sequencing and tone

Order the letter to mirror the editor's priorities: fatal/editor-flagged comments first, then referee-by-referee. Open each referee's section by thanking them and summarizing the changes their report produced. For a genuine disagreement, never refuse flatly — concede the concern's legitimacy, then present the microstructure evidence that resolves it; if it cannot be resolved, scope the claim honestly. When two referees pull in opposite directions, state both positions and ask the editor for direction rather than silently complying with one and ignoring the other. The revised manuscript and Internet Appendix must say exactly what the letter claims they say — an editor will spot-check.

## Checklist

- [ ] Every referee comment reproduced and answered, numbered, with a location pointer
- [ ] Editor-flagged / fatal comments addressed first and most thoroughly
- [ ] New analyses report the actual result and whether the headline survives
- [ ] Measurement-artifact ask answered with an alternative construct
- [ ] Endogeneity ask answered by design, not by adding controls
- [ ] Push-backs concede the concern, then rebut with microstructure evidence
- [ ] Conflicting comments escalated to the editor, not silently resolved
- [ ] Revised draft and Internet Appendix updated consistently with the letter

## Handling the comment you cannot fully satisfy

Some asks cannot be met — the data to run the requested test do not exist, or a requested redesign would not be identified. Do not ignore these and hope, and do not pretend to comply with a token gesture. State plainly what you tried, why the ideal version is infeasible, and the **best available alternative** you ran instead, with its result. "We cannot obtain order-level data for this venue; as the closest feasible test we use consolidated TAQ depth, which shows the same pattern (new IA.5)." Microstructure referees respect a candid constraint far more than a hollow "addressed." If the comment reflects a genuine limitation of the design, acknowledge it as a scope condition in the paper rather than overselling around it — this both answers the referee and pre-empts the same objection in any future round.

## Anti-patterns

- "We have addressed this" with no location pointer or number
- Adding controls when the referee asked for identification
- Arguing down a measurement-artifact concern instead of running the alternative measure
- Defensive or dismissive tone toward a specialist referee
- Silently picking one referee's view when two conflict
- A response letter whose claims the revised draft does not actually support

## Managing scope so the revision converges

R&Rs balloon when authors treat every comment as equal and add analysis without removing anything. Keep the revision converging: anchor on the editor's essential comments, do exactly the work those require, and resist gold-plating the minor ones beyond a sentence and an appendix table. When a referee's suggestion would push the paper away from its microstructure core (e.g., "add a corporate-governance angle"), politely note that it lies outside the paper's market-mechanism focus rather than diluting the contribution to comply. Track a one-line status per comment (done / added exhibit / pushed back / escalated) so nothing is silently dropped — an unaddressed comment is the fastest way to lose a second round.

## Output format

```text
【Journal】Journal of Financial Markets (JFM)
【Skill】jfm-rebuttal
【Summary line】headline result stability after revisions
【Comment ledger】each comment → response → location pointer? [Y/N]
【Fatal first】editor-flagged comments addressed first? [Y/N]
【New analysis】results stated with numbers, headline survives? [Y/N]
【Push-backs】concede-then-rebut with evidence? [Y/N]
【Conflicts】escalated to editor where referees disagree? [Y/N]
【Next step】resubmit via Editorial Manager (re-run jfm-submission preflight)
```
