---
name: rt-simulated-referee
description: Use to rehearse peer review before submitting — a calibrated Associate Editor desk-screen plus 2–3 distinct-lens referees for the target venue, adversarially verified and synthesized into a referee report, a decision band, and a prioritized, skill-mapped fix list. A rehearsal that predicts the attack surface; it does not replace real review.
---

# Simulated Referee (rt-simulated-referee)

Run the substantive gauntlet before a real referee does. Full protocol + a worked example:
[`shared-resources/submission-readiness/simulated-referee.md`](../../../shared-resources/submission-readiness/simulated-referee.md).

## When to trigger

- After `rt-submission-readiness` clears the mechanical bar.
- When the author wants to know the decisive objection before submitting.

## Calibrate first (this is what makes it realistic)

Pull the venue's bar from the target pack, not generic intuition: acceptance/desk-reject
reality + mechanics from `resources/official-source-map.md`; what this venue's referees
attack from `*-referee-strategy` + the shared
[`reviewer-objection-checklist`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md);
the fit/identification/robustness bar from the pack's skills. Set strictness to the
venue's selectivity.

## Protocol

1. **AE desk-screen** — fit, general interest, fatal flaws → desk-reject risk; stop if a clear desk reject.
2. **Independent referees** (distinct lenses: identification skeptic · contribution/fit ·
   robustness/reproducibility) each write a structured report.
3. **Adversarial verification** — every major concern must be **real + specific +
   addressable** or be downgraded.
4. **AE synthesis** — one decision band (reject / major / minor / lean-accept) + the 1–3
   decisive issues.
5. **Skill-mapped fix list** — each decisive issue → the pack skill (and its execution
   bridge) that fixes it.

## Orchestration

Spawn one subagent per role with the same manuscript + the calibrated venue bar; collect
independent reports; a final AE-synthesis agent. Distinct lenses + independence catch more
than a single read.

## Hard rules

1. **Calibrate from the pack + source-map**, never generic.
2. **Verify before reporting** (real / specific / addressable).
3. **Map every decisive issue to a skill + execution bridge.**
4. **It's a rehearsal** — output a decision *band* and the decisive issues, never a fake accept probability.

## Output format

```
【Venue】… (calibrated)
【Desk-screen】send out / desk reject — reason; risk low/med/high
【Decision band】reject / major / minor / lean-accept
【Decisive issues (1–3)】each with owning pack skill + concrete fix
【Author action plan】ordered; tie each to a skill + tool
```

Next: address the decisive issues, then `rt-response-to-referees` for a real R&R.
