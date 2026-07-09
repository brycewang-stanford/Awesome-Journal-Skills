---
name: infocom-author-response
description: Use when handling the IEEE INFOCOM post-submission reality — that the venue has traditionally offered no author rebuttal — covering how to write a self-defending submission, how to read and act on an early-reject, what to do after a final reject, and how to use any response window a given cycle does introduce (verify per cycle).
---

# INFOCOM Author Response

Use this after submission, and — more importantly — *before* it. The distinctive INFOCOM fact is
that there is **traditionally no author rebuttal**: reviewer scores and TPC discussion decide, and
you usually never get a turn to reply. So the "author response" that matters most is the one you
bake into the PDF. This skill covers the defensive submission, the early-reject checkpoint, the
post-reject move, and any actual response window a cycle introduces (**待核实** each year).

## The response that counts: a self-defending submission

Because you likely cannot reply, answer the reviewer *in the paper*:

- **Pre-empt the top objection per subarea.** A theory reviewer will question an assumption — state
  and justify it in the system model. A systems reviewer will call a baseline unfair — tune it and
  document the budget. A measurement reviewer will doubt generalization — scope the claim.
- **State limits before a reviewer finds them.** A short "where this does not hold" paragraph
  disarms the objection you could not otherwise rebut.
- **Make every number checkable.** Named simulator, seeds, confidence intervals, and (optionally)
  released scripts turn "I don't believe this" into "I can verify this."

This is the opposite of a rebuttal-driven venue, where authors sometimes ship a thin submission
planning to "fix it in the response." At INFOCOM that plan fails silently.

## Reading an early-reject

INFOCOM's early-reject phase (INFOCOM 2027: 9 Oct 2026) cuts papers before full discussion. Treat
it as signal:

```text
[Uniform low scores]  the paper did not read as INFOCOM-ready to multiple readers -> structural fix
[Scope mismatch]      routed to the wrong subarea, or genuinely off-scope -> re-tag or reroute
[Compliance]          double-blind or length violation flagged -> mechanical, fixable next cycle
-> there is no appeal; diagnose which of these it was and act, do not relitigate
```

An early-reject is rarely a near-miss; a paper the reviewers wanted to discuss survives to the full
round. Read it as "this needs real work," not "this was unlucky."

## After a final reject

- **No rebuttal existed to blame** — the decision reflects the paper as written. Extract the named
  weakness from the reviews and fix *that*, not the phrasing.
- **Reroute by shape.** A built-system reject may fit SIGCOMM/NSDI with a deployment story; an
  analytical reject may fit ToN/JSAC with the full-length treatment the page limit forbade; a
  focused protocol result may fit ICNP.
- **Resubmit deliberately.** A lightly edited resubmission to the next INFOCOM meets a similar
  reviewer pool; change something real (a tuned baseline, a proved case, a larger evaluation).

## If a cycle introduces a response window (verify first)

Should a given INFOCOM add an author-feedback/rebuttal period (**待核实** — do not assume it),
apply the discipline of a scarce turn:

| Pushback | What it signals | Response move |
|---|---|---|
| "The baseline is untuned/unfair" | Soundness doubt | Report the re-run with an equal, documented budget, or justify the choice |
| "The assumption is unrealistic" | Modeling-validity doubt | Bound the gap empirically or scope the theorem; do not hand-wave |
| "Doesn't scale beyond a toy topology" | External-validity limit | Point to the largest evaluated size; add one if the format permits |
| "A proof step is unclear" | Rigor doubt | Give the missing step concisely; point to the appendix/report |

Answer only decision-critical, **verifiable** points; keep it anonymous; do not add claims the
reviewers could not check.

## Calibration

- **Confirm whether a rebuttal exists this cycle** before promising anyone a reply — the default is
  none.
- The PC discussion decides; even where a response window exists, the revised understanding of your
  *existing* paper is what moves a score, not new promises.
- Length and format of any response window vary by cycle; confirm the current instructions.

## Output format

```text
[Situation] pre-submission (defensive) / early-reject / final reject / response-window (待核实)
[Defensive audit] <top objection per subarea -> pre-empted in the PDF? yes/no>
[Early-reject diagnosis] uniform-low / scope / compliance -> action
[Reroute plan] <SIGCOMM/NSDI | ICNP | ToN/JSAC | resubmit-with-change>
[If response window] <decision-critical, verifiable points only; anonymity check>
```
