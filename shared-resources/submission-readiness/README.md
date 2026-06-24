# Submission-Readiness — self-check + simulated referee

The last mile before you hit "submit": run the manuscript against the target venue's bar
and get back (a) a **readiness scorecard** (is it structurally/mechanically complete and
in-scope?) and (b) a **simulated referee report** (would a calibrated AE + referees send
it out, and what would they attack?). Together they cut the most expensive delay in
publishing — a desk reject or a first-round rejection that a pre-check would have caught.

This closes the loop with the other two cross-journal capabilities:

```
journal-match  →  pick the venue        (shared-resources/journal-selection/)
execution-bridge →  run the analysis     (shared-resources/empirical-methods/execution-with-mcp.md)
submission-readiness →  pass the bar before submitting   (this folder)
```

## Contents

| File | What it gives an agent |
|---|---|
| [`readiness-checklist.md`](readiness-checklist.md) | A venue-parameterized **go/no-go scorecard** run on the *user's* manuscript: fit, identification/method, robustness/inference, exhibits, exposition, venue mechanics (page limit / anonymization / fee / data-&-code policy), reproducibility. Per-dimension PASS / FLAG / FAIL + the blocking gaps. |
| [`simulated-referee.md`](simulated-referee.md) | A multi-agent **referee protocol**: an AE desk-screen + 2–3 distinct-lens referees calibrated to the venue, adversarially verified, synthesized into a referee report + a recommendation + a prioritized, skill-mapped fix list. |
| [`response-to-referees.md`](response-to-referees.md) | Turn a referee report (real R&R or the simulated rehearsal) into a **point-by-point response letter + revision plan** — editor first, every comment answered, each empirical fix backed by a real re-run via the pack skill + execution bridge. |

## Design principle (same as the other capabilities)

- **Venue bar comes from the pack, live facts from the source-map.** The criteria are
  read from the target pack's own skills (`*-topic-selection`, `*-identification` /
  `*-methods`, `*-robustness`, `*-tables-figures`, `*-referee-strategy`,
  `*-submission`) and the shared
  [`reviewer-objection-checklist`](../empirical-methods/reviewer-objection-checklist.md) /
  [`reporting-standards`](../empirical-methods/reporting-standards.md); mechanics
  (page limit, fee, anonymization, data policy) from the pack's
  `resources/official-source-map.md`. Nothing is hard-coded or recalled from memory.
- **Built as a shared capability**, not a new SKILL/pack — so it adds no skill/pack to
  the audit tripwires and any pack's `*-workflow` router can invoke it.
- **A pre-check, not a verdict.** It reduces avoidable rejections; it does not replace
  real peer review, and it never claims a paper "will" be accepted.

## How to use

1. Name the target venue (or run `journal-match` first). Load that pack + source-map.
2. Run [`readiness-checklist.md`](readiness-checklist.md) for the mechanical/structural
   go/no-go and the blocking gaps.
3. If readiness passes, run [`simulated-referee.md`](simulated-referee.md) for the
   substantive adversarial review and the prioritized fix list.
4. Map every fix back to the pack's skills (e.g. a TWFE objection →
   `*-identification` + the execution bridge) and iterate before submitting.
